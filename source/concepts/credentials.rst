Credentials and secrets
=======================

Where a credential lives
------------------------

A server declares which environment variables it needs. *Plain* values (an
instance URL, a region) are stored in the database. *Secret* values (tokens,
passwords) go to the secret store, which is one of:

Vaultwarden / Bitwarden
   Set ``BW_SERVER``, ``BW_CLIENTID``, ``BW_CLIENTSECRET`` and ``BW_PASSWORD``.
   mcprack drives the ``bw`` CLI and keeps one vault item per server
   (``BW_ITEM_PREFIX``, default ``MCP-``). The session key is passed to ``bw``
   through the environment, never on its command line.

Local encrypted store
   Used when ``BW_SERVER`` is empty. Values are encrypted with a key derived from
   ``SECRET_KEY``. ``SECRET_KEY_FALLBACKS`` keeps old keys readable during a
   rotation (:doc:`../howto/rotate-secret-key`).

Check the active backend:

.. code-block:: bash

   sudo mcprack secret backend

Setting secrets
---------------

.. code-block:: bash

   sudo mcprack secret set zabbix ZABBIX_TOKEN      # prompts for the value
   sudo mcprack secret list zabbix                  # which keys have a value
   sudo mcprack secret unset zabbix ZABBIX_TOKEN

Resolution at request time
--------------------------

Credentials are resolved when a request arrives, not when the server is
registered: the administrator's shared values first, then the user's own override
on top. The result goes to the per-user process (as its environment) or into the
authentication header of a relayed request. It is never returned to the client.

What a started process inherits
-------------------------------

A per-user process receives only ``PATH``, ``LANG``/``LC_*``, ``HOME``, ``TZ``,
proxy and CA bundle settings, plus the resolved credentials of its own server.
mcprack's own settings — ``SECRET_KEY``, ``BW_*``, ``LDAP_*``, ``SMTP_*``, the
database URL — are never passed on. Add harmless names with
``MCP_CHILD_ENV_ALLOW``. The resolved credentials live in ``/run/mcprack`` (tmpfs,
``0600``) and are removed when the process is stopped.

Exposure to administrators
--------------------------

Reading a server's secrets back in clear text (``reveal_secrets``, the edit form)
and reading another user's override values are recorded in the audit trail with
the administrator and the server, never the values.
