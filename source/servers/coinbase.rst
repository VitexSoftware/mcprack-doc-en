mcp-server-coinbase
===================

An MCP server for the **Coinbase Advanced Trade API**: account balances, market data and orders. Package: ``coinbase-mcp-server``; companion: ``mcprack-mcp-server-coinbase``. Companion package: ``mcprack-mcp-server-coinbase``. Binary: ``/usr/bin/coinbase-mcp-server``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-coinbase

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``COINBASE_API_KEY_NAME``
     - yes
     - Coinbase API key name (secret store)
   * - ``COINBASE_PRIVATE_KEY``
     - yes
     - Matching private key (secret store)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-coinbase
   sudo mcprack server edit mcp-server-coinbase --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-coinbase <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: The README documents no read-only switch. Use a read-only API key for anything but deliberate trading.

Tools
-----

- Account and balance queries, market data and order placement; see the upstream README for the current tool list.

.. warning::

   This server can place **real trades** with valid keys. Create API keys with the narrowest permissions, test with a key that cannot trade, and never let an assistant trade unattended.
