Listen on another address
=========================

By default mcprack's gunicorn listens on ``127.0.0.1:8912``, so only a reverse
proxy on the same host can reach it. Change the listen address when:

- the TLS reverse proxy runs on a **different host**, or
- clients on your intranet connect to mcprack **directly**, without a proxy.

If clients on another host report ``ECONNREFUSED`` for port 8912, the service is
still bound to the loopback address.

The setting is the environment variable ``GUNICORN_BIND`` (``host:port``). You can
set it in ``/etc/mcprack/env`` (:doc:`../reference/configuration`), but a systemd
drop-in is the better place for a per-host network setting: the packaged unit file
is replaced on every package upgrade, while files in
``/etc/systemd/system/mcprack.service.d/`` are never touched by the package.

.. warning::

   gunicorn speaks plain HTTP. A non-loopback address exposes sign-in forms,
   tokens and relay traffic unencrypted to everyone who can reach the port. Use it
   only on a trusted network, restrict the port with a firewall (step 3) and never
   expose it to the internet. For internet access put a TLS proxy in front
   (:doc:`../security/internet-checklist`).

1. Create the drop-in
---------------------

Replace ``192.0.2.10`` with the address of the mcprack host on the network the
clients use:

.. code-block:: bash

   sudo systemctl edit mcprack

In the editor that opens, enter:

.. code-block:: ini

   [Service]
   Environment=GUNICORN_BIND=192.0.2.10:8912

Saving creates ``/etc/systemd/system/mcprack.service.d/override.conf``. To choose
the file name yourself (for example ``bind.conf``), create it by hand:

.. code-block:: bash

   sudo mkdir -p /etc/systemd/system/mcprack.service.d
   sudo tee /etc/systemd/system/mcprack.service.d/bind.conf <<'EOF'
   [Service]
   Environment=GUNICORN_BIND=192.0.2.10:8912
   EOF

Use ``0.0.0.0:8912`` to listen on all addresses only if a firewall limits who can
connect.

2. Reload and restart
---------------------

.. code-block:: bash

   sudo systemctl daemon-reload
   sudo systemctl restart mcprack

3. Restrict the port
--------------------

Allow only the hosts that need access. Example with ``ufw`` (the proxy or client
network is ``198.51.100.0/24``):

.. code-block:: bash

   sudo ufw allow from 198.51.100.0/24 to any port 8912 proto tcp

4. Adjust the public settings
-----------------------------

In ``/etc/mcprack/env``:

- If clients use a host name for this server, set ``PUBLIC_BASE_URL`` to it and
  add any further names to ``TRUSTED_HOSTS``; mcprack rejects other ``Host``
  values.
- On a plain-HTTP intranet install set ``SESSION_COOKIE_SECURE=false``, otherwise
  browsers do not send the session cookie back.

Restart the service again after editing the file.

5. Verify
---------

Check which value the service got and which address it listens on:

.. code-block:: bash

   systemctl show mcprack -p Environment
   sudo ss -ltnp | grep 8912

The listener must show ``192.0.2.10:8912``. If ``GUNICORN_BIND`` is also set in
``/etc/mcprack/env``, make sure only one of the two defines it, otherwise the
value that systemd applies last wins; ``systemctl show`` tells you which.

From a client host, check that the port answers, then verify a client
configuration against the new address (:doc:`verify-config`):

.. code-block:: bash

   curl -sS -o /dev/null -w '%{http_code}\n' http://192.0.2.10:8912/login
   sudo mcprack user config verify USER claude-code --base-url http://192.0.2.10:8912

Revert to loopback
------------------

.. code-block:: bash

   sudo rm /etc/systemd/system/mcprack.service.d/bind.conf
   sudo systemctl daemon-reload
   sudo systemctl restart mcprack
