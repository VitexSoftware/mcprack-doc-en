Registering an MCP server
=========================

A server is either a **local command** that mcprack runs per user (``stdio``), or
a **network endpoint** it relays to (``http`` or ``sse``).

With the command line
---------------------

.. code-block:: bash

   # a local stdio server
   sudo mcprack server create zabbix \
       --label "Zabbix" --transport stdio \
       --command /usr/bin/zabbix-mcp \
       --set-env ZABBIX_URL=https://zabbix.example.com/api_jsonrpc.php \
       --enabled
   sudo mcprack secret set zabbix ZABBIX_TOKEN

   # a network server
   sudo mcprack server create netbox \
       --label "NetBox" --transport http \
       --url https://netbox.example.com/mcp --enabled

``server create`` is idempotent: running it again updates the server. Test it:

.. code-block:: bash

   sudo mcprack server test zabbix --timeout 30

The command performs the MCP handshake and prints the tools, resources and prompts.
Test a command without registering it (the form used by package autopkgtests):

.. code-block:: bash

   sudo mcprack server probe /usr/bin/mcp-server-filesystem --set-env FS_READONLY=true

In the web interface
--------------------

*Admin → Servers → New* walks through the same fields. *Autodetect* proposes
environment variables from the server's manifest or documentation; suggestions are
never saved until you submit the form. Creating or editing a server asks you to
confirm your password again if you have not signed in recently
(:doc:`../security/reauthentication`).

Rules for commands and URLs
---------------------------

Both are checked when the server is saved **and** again when it is used
(:doc:`../security/policies`):

- A command in ``/tmp``, ``/var/tmp``, ``/dev/shm`` ... or a relative path is
  refused. ``ALLOWED_COMMAND_DIRS`` makes this an allowlist.
- A URL must be ``http`` or ``https``, without credentials, and must not point at
  a link-local or cloud metadata address.
- ``command`` wins over ``url`` when both are set; leave the unused one empty.

Installing packages for a server
--------------------------------

*Admin → Install* installs a pip or npm package or pulls a Docker image and
registers it. Inputs are validated, packages must be pinned to an exact version
(``INSTALL_REQUIRE_PINNED``), pip installs wheels only
(``INSTALL_ALLOW_SOURCE_BUILDS`` changes that) and npm never runs lifecycle
scripts. If you use ``ALLOWED_COMMAND_DIRS`` include
``/var/lib/mcprack/installs``.

Servers that register themselves
--------------------------------

A server shipped as a Debian package with a *companion* package appears in the
catalog as soon as the companion is installed — see :doc:`../servers/index`.

Enabling and disabling
----------------------

.. code-block:: bash

   sudo mcprack server disable zabbix     # hides it from everybody
   sudo mcprack server enable zabbix
   sudo mcprack server show zabbix
   sudo mcprack server list
