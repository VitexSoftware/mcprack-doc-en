mcp-server-wazuh
================

An MCP server for **Wazuh 5**. It reads the manager API (port 55000: agents, groups,
cluster, MITRE) and the indexer (port 9200: events, findings, vulnerability state).
Companion package: ``mcprack-mcp-server-wazuh``. Binary: ``/usr/bin/mcp-server-wazuh``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-wazuh

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 30 12 58

   * - Variable
     - Required
     - Meaning
   * - ``WAZUH_API_URL``
     - no
     - Manager API base URL (default ``https://127.0.0.1:55000``)
   * - ``WAZUH_API_USER``
     - yes
     - Manager API user (secret store); exchanged for a short-lived JWT
   * - ``WAZUH_API_PASSWORD``
     - yes
     - Manager API password (secret store)
   * - ``WAZUH_INDEXER_URL``
     - no
     - Indexer URL (default ``https://127.0.0.1:9200``)
   * - ``WAZUH_INDEXER_USER``, ``WAZUH_INDEXER_PASSWORD``
     - no
     - Indexer credentials (secret store); only the three ``search_*`` tools need them
   * - ``WAZUH_READ_ONLY``
     - no
     - ``true`` by default; ``false`` registers ``restart_agents``
   * - ``WAZUH_VERIFY_TLS``
     - no
     - ``true`` by default; verify manager and indexer certificates
   * - ``WAZUH_TIMEOUT``, ``WAZUH_MAX_CHARS``
     - no
     - Seconds per request (30) and output truncation limit (100000)

Registration:

.. code-block:: bash

   sudo mcprack server edit mcp-server-wazuh \
       --set-env WAZUH_API_URL=https://wazuh.example.com:55000 \
       --set-env WAZUH_INDEXER_URL=https://wazuh.example.com:9200 \
       --add-secret-key WAZUH_API_USER --add-secret-key WAZUH_API_PASSWORD \
       --add-secret-key WAZUH_INDEXER_USER --add-secret-key WAZUH_INDEXER_PASSWORD
   sudo mcprack secret set mcp-server-wazuh WAZUH_API_USER
   sudo mcprack secret set mcp-server-wazuh WAZUH_API_PASSWORD

Tools
-----

- Read-only: ``get_api_info``, ``list_agents``, ``get_agent``, ``get_agents_summary``,
  ``list_groups``, ``get_cluster_status``, ``list_cluster_nodes``, ``search_mitre``,
  ``search_events``, ``search_findings``, ``search_vulnerabilities``.
- Mutating (need ``WAZUH_READ_ONLY=false``): ``restart_agents``.

.. warning::

   ``restart_agents`` interrupts the monitored hosts' agents. Leave
   ``WAZUH_READ_ONLY=true`` unless a user explicitly needs restarts.
