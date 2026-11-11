mcp-server-abraflexi
====================

An MCP server for the **AbraFlexi** ERP, built on FastMCP and ``python-abraflexi``.
Companion package: ``mcprack-mcp-server-abraflexi``. Binary:
``/usr/bin/mcp-server-abraflexi`` (``abraflexi-mcp`` is a deprecated alias).

.. code-block:: bash

   sudo apt install mcprack-mcp-server-abraflexi

One server instance is bound to **exactly one AbraFlexi company** for its whole
lifetime. Call the ``server_info`` tool to see which company and URL a running
server uses; the main record-fetching tools echo it back in a ``_context`` block.
For several companies register several entries of the same server with different
variables (:doc:`../howto/register-server`).

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Meaning
   * - ``ABRAFLEXI_URL``
     - Base URL of the AbraFlexi server
   * - ``ABRAFLEXI_COMPANY``
     - Company (accounting unit) to work with
   * - ``ABRAFLEXI_LOGIN``, ``ABRAFLEXI_PASSWORD``
     - Credentials; ``ABRAFLEXI_AUTHSESSID`` can be used instead of a password
   * - ``READ_ONLY``
     - ``true`` by default; ``false`` allows create/update/delete tools
   * - ``ABRAFLEXI_TIMEOUT``
     - Request timeout
   * - ``ABRAFLEXI_MCP_TRANSPORT`` and ``..._HOST``, ``..._PORT``
     - Only for running the server stand-alone over streamable HTTP; mcprack
       always uses ``stdio``

Register the plain values and keep the password in the secret store:

.. code-block:: bash

   sudo mcprack server edit mcp-server-abraflexi \
       --set-env ABRAFLEXI_URL=https://abraflexi.example.com:5434 \
       --set-env ABRAFLEXI_COMPANY=mycompany \
       --set-env ABRAFLEXI_LOGIN=winstrom \
       --add-secret-key ABRAFLEXI_PASSWORD --allow-user-override
   sudo mcprack secret set mcp-server-abraflexi ABRAFLEXI_PASSWORD

Allow users to override ``ABRAFLEXI_LOGIN`` and ``ABRAFLEXI_PASSWORD`` so that every
person acts with their own AbraFlexi account (:doc:`../concepts/access-control`).

Tools
-----

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Group
     - Examples
   * - Identity
     - ``server_info``
   * - Invoices
     - ``invoice_issued_get/create/update/delete``, ``invoice_received_get/create``
   * - Issued-invoice logic
     - ``invoice_issued_match_payment``, ``..._cash_payment``, ``..._deduct_advance``,
       ``..._deduct_zdd``, ``..._link_zdd``, ``..._unlink_zdd``, ``..._overdue_days``,
       ``..._get_email``, ``..._get_recipients``
   * - Contacts, products, banking
     - ``contact_*``, ``product_*``, ``bank_transaction_get/create``
   * - Generic evidence access
     - ``evidence_list``, ``evidence_get``, ``evidence_create/update/delete``,
       attachments, labels, reports, locking, mass update, batch insert/update
   * - Change tracking and webhooks
     - ``changes_enable/disable/get/status``, ``webhook_register/list/get/retry/unregister``
   * - Company
     - ``company_create`` (needs server-admin REST rights)

Writes are refused while ``READ_ONLY`` is ``true``.
