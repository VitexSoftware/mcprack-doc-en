mcp-server-raynet
=================

An MCP server for the **Raynet CRM** REST API: business cases, companies, people, leads and activities. 32 read tools and 27 write tools. Companion package: ``mcprack-mcp-server-raynet``. Binary: ``/usr/bin/mcp-server-raynet``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-raynet

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``RAYNET_API_TOKEN``
     - yes
     - Bearer token (secret store)
   * - ``RAYNET_BASE_URL``
     - no
     - API base URL (default ``https://app.raynet.cz/api/v2/``)
   * - ``RAYNET_WRITE_ENABLED``
     - no
     - ``false`` by default; ``true`` exposes the 27 write tools
   * - ``RAYNET_CACHE_TTL``
     - no
     - Seconds to cache value lists (default ``300``)
   * - ``RAYNET_MAX_CONCURRENCY``
     - no
     - Concurrent requests (default ``3``, capped at 3)
   * - ``RAYNET_DATE_FORMAT``
     - no
     - ``native`` or ``iso8601``

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-raynet
   sudo mcprack server edit mcp-server-raynet --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-raynet <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: Read-only until ``RAYNET_WRITE_ENABLED=true``; the companion sets ``false``.

Tools
-----

- Read: 32 tools. Write (need ``RAYNET_WRITE_ENABLED=true``): 27 tools.
