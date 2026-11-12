Granting access
===============

Create a user
-------------

.. code-block:: bash

   sudo mcprack user create --username alice --email alice@example.com
   sudo mcprack user promote alice        # make an administrator

LDAP users are created on their first sign-in (:doc:`../security/authentication`);
under ``STRICT_SERVER_PERMISSIONS`` they see nothing until you grant access.

Allow servers
-------------

.. code-block:: bash

   sudo mcprack user server allow alice zabbix
   sudo mcprack user server deny alice zabbix
   sudo mcprack user server list alice

Users can also request access from a denied server's detail card. Review pending
requests under *Admin → Access Requests*. Approving a request allows that user to
use the server but does not subscribe them automatically; they must select it on
the *MCP servers* page. A denied request can be submitted again later.

Pre-select servers for a user (what ends up in their generated configuration):

.. code-block:: bash

   sudo mcprack user server select alice zabbix netbox

Use a template
--------------

.. code-block:: bash

   sudo mcprack template create support --label "Support team"
   sudo mcprack template set-servers support --allow zabbix --allow netbox --select zabbix
   sudo mcprack template apply support alice

Personal credentials
--------------------

If a server allows overrides, a user — or an administrator on their behalf — can
set personal values:

.. code-block:: bash

   sudo mcprack user override set alice zabbix ZABBIX_TOKEN=...
   sudo mcprack user override list alice zabbix
   sudo mcprack user override reset alice zabbix

.. note::

   Prefer the web interface (*Overrides*) or the REST API for secrets: a value
   passed on the command line is visible in the process list. See
   :doc:`../concepts/access-control` for what an override may contain.

Taking access away
------------------

.. code-block:: bash

   sudo mcprack user disable alice          # blocks sign-in, ends sessions, stops processes
   sudo mcprack user revoke-tokens alice    # kills proxy URLs, API tokens, OAuth tokens
   sudo mcprack user delete alice

Disabling or deleting a user stops their running MCP server processes. After
``revoke-tokens`` the user keeps the account and downloads a new configuration.
Administrators have the same actions in *Admin → Users* ("Revoke all tokens") and
in ``POST /api/v1/admin/users/{id}/revoke-tokens``.
