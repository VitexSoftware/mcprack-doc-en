mcp-server-patreon
==================

An MCP server for your **Patreon** creator data over stdio. Companion package: ``mcprack-mcp-server-patreon``. Binary: ``/usr/bin/mcp-server-patreon``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-patreon

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``PATREON_ACCESS_TOKEN``
     - yes
     - Creator access token (secret store)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-patreon
   sudo mcprack server edit mcp-server-patreon --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-patreon <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: All tools only read data; there is no write switch.

Tools
-----

- ``fetch_identity``, ``fetch_campaigns``, ``fetch_campaign``, ``fetch_members``, ``fetch_posts``, ``fetch_post`` and further read tools.
