mcp-server-magento
==================

An MCP server for **Magento 2** over its REST API: products, stock, categories, orders and revenue. Written in Node.js. Companion package: ``mcprack-mcp-server-magento``. Binary: ``/usr/bin/mcp-server-magento``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-magento

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``MAGENTO_API_TOKEN``
     - yes
     - Bearer token (secret store)
   * - ``MAGENTO_BASE_URL``
     - yes
     - REST base URL, e.g. ``https://shop.example.com/rest/V1``
   * - ``MAGENTO_READ_ONLY``
     - no
     - The companion sets ``true``; hides ``update_product_attribute``
   * - ``MAGENTO_INSECURE_TLS``
     - no
     - ``true`` disables TLS verification (development only)
   * - ``MAGENTO_TIMEOUT_MS``
     - no
     - HTTP timeout in milliseconds (default ``30000``)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-magento
   sudo mcprack server edit mcp-server-magento --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-magento <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: The companion sets ``MAGENTO_READ_ONLY=true``.

Tools
-----

- Read-only: ``get_product_by_sku``, ``get_product_by_id``, ``search_products``, ``advanced_product_search``, ``get_product_categories``, ``get_related_products``, ``get_product_stock``, ``get_product_attributes``, ``get_revenue``, ``get_order_count``, ``get_product_sales``, ``get_revenue_by_country``, ``get_customer_ordered_products_by_email``.
- Mutating (need ``MAGENTO_READ_ONLY=false``): ``update_product_attribute``.
