Checklist for an internet-facing instance
=========================================

1. **Secrets.** A strong ``SECRET_KEY`` (the service refuses a weak one);
   ``PUBLIC_BASE_URL`` set (it also restricts the accepted ``Host``);
   ``GUNICORN_BIND`` left on ``127.0.0.1``.
2. **TLS reverse proxy** with a dead-end default virtual host, forwarded headers
   removed and size limits — the sample below.
3. **Restrict the admin plane.** ``/admin`` and ``/api/v1/admin`` can register
   servers, i.e. run commands. Limit them by address or client certificate.
4. **Grant servers explicitly** (``STRICT_SERVER_PERMISSIONS`` is on by default) and
   prefer OAuth or short-lived proxy tokens (``PROXY_TOKEN_MAX_AGE_SECONDS``).
5. **Two-factor authentication** for administrators (the default); review API
   tokens created before it existed.
6. **Command policy**: consider ``ALLOWED_COMMAND_DIRS``.
7. **Egress filtering** of the ``mcprack`` user (:doc:`policies`).
8. **fail2ban** on the Apache access log.
9. **Audit mirror shipped off the host**, and ``mcprack audit-verify`` from cron.
10. **Verify** with ``curl -H 'Host: x.invalid' https://<server>/login`` (it must
    not reach mcprack) and with a real password-reset e-mail.

Sample Apache virtual host
--------------------------

Copy ``/usr/share/doc/mcprack/apache-mcprack.conf`` to
``/etc/apache2/sites-available/mcprack.conf``, adjust the names and certificate
paths, then:

.. code-block:: bash

   sudo a2enmod ssl proxy proxy_http headers
   sudo a2ensite mcprack
   sudo systemctl reload apache2

The essentials:

.. code-block:: apache

   # Unknown Host names land here and go nowhere.
   <VirtualHost *:443>
       ServerName default.invalid
       SSLEngine on
       SSLCertificateFile    /etc/ssl/certs/ssl-cert-snakeoil.pem
       SSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key
       <Location "/">
           Require all denied
       </Location>
   </VirtualHost>

   <VirtualHost *:443>
       ServerName mcprack.example.com
       SSLEngine on
       SSLCertificateFile    /etc/letsencrypt/live/mcprack.example.com/fullchain.pem
       SSLCertificateKeyFile /etc/letsencrypt/live/mcprack.example.com/privkey.pem
       SSLProtocol -all +TLSv1.2 +TLSv1.3

       # Never trust what the client says about itself.
       RequestHeader unset X-Forwarded-For
       RequestHeader unset X-Forwarded-Host
       RequestHeader unset X-Forwarded-Proto
       RequestHeader unset X-Forwarded-Prefix
       RequestHeader unset X-Real-IP
       RequestHeader unset Forwarded

       LimitRequestBody      2097152
       LimitRequestFields    50
       LimitRequestFieldSize 8190

       ProxyPreserveHost On
       # MCP responses can be long-lived event streams: do not buffer them.
       ProxyPass        "/" "http://127.0.0.1:8912/" flushpackets=on timeout=60
       ProxyPassReverse "/" "http://127.0.0.1:8912/"

       #<LocationMatch "^/(admin|api/v1/admin)(/|$)">
       #    Require ip 10.0.0.0/8 192.168.0.0/16
       #</LocationMatch>

       RequestHeader set X-Forwarded-Proto "https" env=HTTPS
       Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
   </VirtualHost>

Allow at least 60 seconds of read timeout for the proxy, and do not let an nginx
in front buffer ``text/event-stream`` answers (mcprack sets ``X-Accel-Buffering:
no``). If the proxy runs on a different host, change ``GUNICORN_BIND`` and restrict
the port to that host.

fail2ban
--------

A failed sign-in answers 200 (the form again) or 429, a good one 302:

.. code-block:: ini

   # /etc/fail2ban/filter.d/mcprack-login.conf
   [Definition]
   failregex = ^<HOST> \S+ \S+ \[[^\]]+\] "POST /(login|forgot-password|oauth/register)\S* HTTP/[0-9.]+" (200|429)

   # /etc/fail2ban/jail.d/mcprack.conf
   [mcprack-login]
   enabled  = true
   filter   = mcprack-login
   logpath  = /var/log/apache2/mcprack-access.log
   maxretry = 10
   findtime = 10m
   bantime  = 1h

Public demo instances
---------------------

``DEMO_MODE=true`` (with ``DEMO_USERNAME`` and ``DEMO_PASSWORD``) pre-fills the
sign-in form for a shared account. All routes that register servers, change
accounts or passwords or move secrets are refused, including through the REST API,
overrides accept only declared names, and two-factor authentication and fresh
re-authentication are not asked for. Never use it with real data.
