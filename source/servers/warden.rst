mcp-server-warden
=================

An MCP server for **Vaultwarden / Bitwarden** through the Bitwarden CLI (``bw``): items, TOTP codes, notes, folders, organizations and Sends. Binary: ``warden-mcp``. Companion package: ``mcprack-mcp-server-warden``. Binary: ``/usr/bin/warden-mcp``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-warden

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``READONLY / KEYCHAIN_READONLY``
     - no
     - ``true`` by default; hides and rejects mutating tools
   * - ``KEYCHAIN_BW_HOME_ROOT``
     - no
     - Root for per-profile ``bw`` state (default ``${HOME}/bw-profiles``)
   * - ``KEYCHAIN_SYNC_ON_WRITE``
     - no
     - Run ``bw sync`` before writes (default ``true``)
   * - ``TOOL_PREFIX``
     - no
     - Public tool namespace (default ``keychain``)
   * - ``WARDEN_MCP_STDIO``
     - no
     - Force stdio mode (mcprack needs stdio)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-warden
   sudo mcprack server edit mcp-server-warden --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-warden <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: Read-only by default. Credentials for the vault come from ``bw`` profile state, not from this catalog entry.

Tools
-----

- Tools are named ``keychain_*`` (for example ``keychain_status``, ``keychain_sync``) plus search, read and, when writes are enabled, create/update/move tools.

.. warning::

   This server hands vault secrets to the assistant. Restrict it to a dedicated vault or collection and keep it read-only.
