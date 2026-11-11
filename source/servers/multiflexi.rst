mcp-server-multiflexi
=====================

An MCP server for the **MultiFlexi** API: applications, jobs, companies, users, run templates, credentials and event sources. Companion package: ``mcprack-mcp-server-multiflexi``. Binary: ``/usr/bin/mcp-server-multiflexi``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-multiflexi

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``MULTIFLEXI_HOST``
     - yes
     - MultiFlexi API host URL
   * - ``MULTIFLEXI_USERNAME``
     - yes
     - Username for basic authentication
   * - ``MULTIFLEXI_PASSWORD``
     - yes
     - Password (secret store)
   * - ``MULTIFLEXI_READONLY``
     - no
     - ``true`` by default; hides all mutating tools
   * - ``MULTIFLEXI_VERIFY_SSL``
     - no
     - Verify certificates (default ``true``)
   * - ``MULTIFLEXI_TIMEOUT, _MAX_RETRIES``
     - no
     - Timeout in seconds (``30``) and retries (``3``)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-multiflexi
   sudo mcprack server edit mcp-server-multiflexi --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-multiflexi <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: Read-only by default (``MULTIFLEXI_READONLY=true``).

Tools
-----

- Read-only: ``get_*`` and ``list_*`` tools for apps, jobs, companies, users, run templates, credentials, topics and event sources.
- Mutating (need ``MULTIFLEXI_READONLY=false``): ``create_job``, ``update_runtemplate``, ``update_credential``, ``set_event_rule``, ``delete_event_rule``, ``assign_user_to_company`` and similar.
