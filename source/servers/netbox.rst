mcp-server-netbox
=================

A **read-only** MCP server for **NetBox** infrastructure data (upstream: ``netboxlabs/netbox-mcp-server``). Companion package: ``mcprack-mcp-server-netbox``. Binary: ``/usr/bin/mcp-server-netbox``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-netbox

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``NETBOX_URL``
     - yes
     - NetBox base URL
   * - ``NETBOX_TOKEN``
     - yes
     - API token (secret store)
   * - ``VERIFY_SSL``
     - no
     - Verify certificates (default ``true``)
   * - ``NETBOX_TIMEOUT``
     - no
     - Request timeout in seconds (default ``30.0``)
   * - ``NETBOX_READONLY``
     - no
     - ``true`` by default; guards the REST client against writes
   * - ``TRANSPORT``
     - no
     - ``stdio`` (default) or ``http``; mcprack needs ``stdio``
   * - ``ENABLE_PLUGIN_DISCOVERY``
     - no
     - Discover plugin object types at startup (default ``false``)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-netbox
   sudo mcprack server edit mcp-server-netbox --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-netbox <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: All tools are read-only.

Tools
-----

- ``netbox_get_objects``, ``netbox_get_object_by_id``, ``netbox_search_objects``, ``netbox_get_changelogs``.
