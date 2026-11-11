mcp-server-redmine
==================

An MCP server for **Redmine** (upstream: ``jztan/redmine-mcp-server``): projects, issues, time tracking, wiki, versions and files. Companion package: ``mcprack-mcp-server-redmine``. Binary: ``/usr/bin/mcp-server-redmine``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-redmine

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``REDMINE_URL``
     - yes
     - Redmine base URL
   * - ``REDMINE_API_KEY``
     - yes
     - API key (legacy auth mode; secret store). Alternatively ``REDMINE_USERNAME`` + ``REDMINE_PASSWORD``
   * - ``REDMINE_AUTH_MODE``
     - no
     - ``legacy`` (default), ``legacy-per-user``, ``oauth``, ``oauth-proxy`` or ``api-key-login``
   * - ``REDMINE_MCP_READ_ONLY``
     - no
     - ``false`` by default; ``true`` blocks all create/update/delete tools
   * - ``REDMINE_MCP_ALLOW_TOOLS``
     - no
     - Expose only these tools (comma-separated)
   * - ``REDMINE_MCP_TRANSPORT``
     - no
     - The companion sets ``stdio``

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-redmine
   sudo mcprack server edit mcp-server-redmine --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-redmine <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: Set ``REDMINE_MCP_READ_ONLY=true`` to block writes; the companion does not set it.

Tools
-----

- Read and write tools for issues, projects, time entries, wiki pages, versions, relations and files (79 tools). The upstream README lists them.
