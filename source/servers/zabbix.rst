mcp-server-zabbix
=================

An MCP server that gives **complete Zabbix API access through three tools** (Zabbix 6.0+; upstream: ``mpeirone/zabbix-mcp-server``). Companion package: ``mcprack-mcp-server-zabbix``. Binary: ``/usr/bin/mcp-server-zabbix``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-zabbix

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``ZABBIX_URL``
     - yes
     - Zabbix server URL
   * - ``ZABBIX_TOKEN``
     - yes
     - API token (secret store); or ``ZABBIX_USER`` + ``ZABBIX_PASSWORD``
   * - ``READ_ONLY``
     - no
     - ``true`` by default; ``false`` allows write API methods
   * - ``VERIFY_SSL``
     - no
     - Verify certificates (default ``true``)
   * - ``ZABBIX_API_WHITELIST, ZABBIX_API_BLACKLIST``
     - no
     - Regex lists of allowed and blocked API methods
   * - ``ZABBIX_API_TIMEOUT``
     - no
     - Seconds (default ``30``)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-zabbix
   sudo mcprack server edit mcp-server-zabbix --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-zabbix <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: Read-only by default (``READ_ONLY=true``).

Tools
-----

- ``zabbix_api`` (call any API method), ``zabbix_api_list``, ``zabbix_api_docs``.
