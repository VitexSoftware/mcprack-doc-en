Authentication and sessions
===========================

Accounts
--------

**Local accounts** always work. **LDAP / Active Directory** is optional
(``LDAP_ENABLED=true``): any account the directory authenticates is created on its
first sign-in, with no server access until you grant it (see
:doc:`../concepts/access-control`).

.. code-block:: bash

   # /etc/mcprack/env
   LDAP_ENABLED=true
   LDAP_SERVER=ldaps://dc.example.com
   LDAP_BASE_DN=dc=example,dc=com
   LDAP_USER_OU=ou=Users,dc=example,dc=com
   LDAP_USER_FILTER=(sAMAccountName=%(user)s)
   LDAP_BIND_DN=cn=mcprack,ou=Service,dc=example,dc=com
   LDAP_BIND_PASSWORD=...
   LDAP_REQUIRED_GROUP=CN=mcprack-users,OU=Groups,DC=example,DC=com

- Use ``ldaps://`` or ``LDAP_STARTTLS=true``; the directory certificate is verified
  (``LDAP_CA_FILE``, ``LDAP_TLS_VALIDATE``). Plain ``ldap://`` still works and is
  flagged in the log: directory passwords would cross the network in clear text.
- ``LDAP_REQUIRED_GROUP`` restricts sign-in to members of one group (checked
  through ``memberOf``).

Passwords
---------

Newly set passwords need at least ``PASSWORD_MIN_LENGTH`` (12) characters and must
not be empty, a common password, a simple sequence or based on the user name. The
rule applies everywhere a password is set: the web form, the REST API, the CLI,
first-administrator creation and password reset. Existing passwords are untouched.

Login throttling
----------------

Failed sign-ins are counted in the database, so the limits hold across all workers
and survive a restart:

- per **account and address** (``LOGIN_MAX_FAILURES``, 5),
- per **account** over all addresses (``LOGIN_ACCOUNT_MAX_FAILURES``, 50),
- per **address** (``LOGIN_IP_MAX_FAILURES``, 30),

within ``LOGIN_FAILURE_WINDOW_SECONDS`` (900). A locked key waits
``LOGIN_LOCK_BASE_SECONDS`` (30), doubling each time up to
``LOGIN_LOCK_MAX_SECONDS`` (3600). The answer is ``429`` with ``Retry-After``. An
attempt is counted *before* the password is checked, and a stranger's failures lock
only their own address, not the real owner. The same counters apply to
two-factor codes, password re-confirmation and every other check of a password.
The typed user name is never written to the audit trail (it is often a password
pasted into the wrong box). In ``DEMO_MODE`` only the address counter applies.

A reverse proxy should add its own limit (for example fail2ban on the Apache log;
gunicorn only ever sees ``127.0.0.1``).

Sessions
--------

The session cookie is ``HttpOnly``, ``Secure`` and ``SameSite=Lax`` and lasts
``SESSION_LIFETIME_SECONDS`` (8 hours). It carries the account's *session version*;
changing the version ends every session of that account on the server. That
happens on: logout from the menu (a POST ends **all** sessions of the account; a
plain ``GET /logout`` ends only this browser), a password change, disabling the
account, revoking its tokens, switching two-factor authentication on or off. A
fresh session is created at every sign-in; nothing a visitor put in the old one
survives except the language.

Password reset
--------------

With ``SMTP_HOST`` configured, *Forgot password* e-mails a link valid for
``PASSWORD_RESET_MAX_AGE_SECONDS`` (1 hour). The link is built from
``PUBLIC_BASE_URL`` (never from the request's ``Host``), the token holds a
fingerprint of the current password so it works once, and the answer does not
reveal whether the address exists. A reset does **not** bypass two-factor
authentication.

Hosts and proxies
-----------------

Set ``PUBLIC_BASE_URL``. mcprack then accepts only that host (add more with
``TRUSTED_HOSTS``), and answers an unknown ``Host`` with a plain ``400``.
gunicorn listens on ``127.0.0.1`` and mcprack trusts exactly **one** proxy hop for
``X-Forwarded-For/-Proto/-Host/-Prefix``; the sample vhost removes any such header
a client sends. A forwarded prefix that is not a plain path (``//evil.example``)
is dropped.
