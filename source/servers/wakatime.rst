mcp-server-wakatime
===================

An MCP server that exposes **WakaTime** summaries over stdio. Companion package: ``mcprack-mcp-server-wakatime``. Binary: ``/usr/bin/mcp-server-wakatime``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-wakatime

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``WAKATIME_API_KEY``
     - yes
     - WakaTime API key (secret store)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-wakatime
   sudo mcprack server edit mcp-server-wakatime --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-wakatime <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: Both tools are read-only, so no read-only switch exists.

Tools
-----

- Two read-only summary tools that proxy the WakaTime Summaries API and return raw JSON.
