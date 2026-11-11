mcp-server-googleoffice
=======================

An MCP server for **Google Workspace** (Gmail, Calendar, Drive, Docs, Sheets, Slides, Forms, Tasks, Contacts, Chat); upstream: ``taylorwilsdon/google_workspace_mcp``. Companion package: ``mcprack-mcp-server-googleoffice``. Binary: ``/usr/bin/mcp-server-googleoffice``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-googleoffice

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``GOOGLE_OAUTH_CLIENT_ID``
     - yes
     - OAuth 2.0 client ID (secret store)
   * - ``GOOGLE_OAUTH_CLIENT_SECRET``
     - yes
     - OAuth 2.0 client secret (secret store)
   * - ``USER_GOOGLE_EMAIL``
     - no
     - Default Google account for tool calls
   * - ``WORKSPACE_MCP_CREDENTIALS_DIR``
     - no
     - Stored OAuth token directory; use a per-user path
   * - ``GOOGLE_SERVICE_ACCOUNT_KEY_JSON / _FILE``
     - no
     - Service-account key for domain-wide delegation
   * - ``DWD_ALLOWED_DOMAINS``
     - no
     - Domains the service account may impersonate
   * - ``WORKSPACE_MCP_READ_ONLY``
     - no
     - The companion sets ``true``: read-only scopes and tools only
   * - ``WORKSPACE_MCP_TOOLS, _TOOL_TIER, _PERMISSIONS, _DISABLED_TOOLS``
     - no
     - Choose which services and tools load

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-googleoffice
   sudo mcprack server edit mcp-server-googleoffice --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-googleoffice <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: The companion sets ``WORKSPACE_MCP_READ_ONLY=true`` and ``MCP_SINGLE_USER_MODE=1``.

Tools
-----

- Tools per Google service; narrow them with ``WORKSPACE_MCP_TOOLS`` or ``WORKSPACE_MCP_TOOL_TIER``.
