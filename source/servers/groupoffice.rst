mcp-server-groupoffice
======================

An MCP server for **GroupOffice** groupware, built on FastMCP. It talks to
GroupOffice's JMAP-style batch/RPC API. Companion package:
``mcprack-mcp-server-groupoffice``. Binary: ``/usr/bin/mcp-server-groupoffice``
(``groupoffice-mcp-server`` is an alias).

.. code-block:: bash

   sudo apt install mcprack-mcp-server-groupoffice

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 30 12 12 46

   * - Variable
     - Required
     - Default
     - Meaning
   * - ``GROUPOFFICE_URL``
     - yes
     -
     - Base URL of your GroupOffice instance
   * - ``GROUPOFFICE_API_TOKEN``
     - yes
     -
     - Bearer token from *System Settings → API Keys* (needs the "API key generator"
       community module)
   * - ``GROUPOFFICE_READONLY``
     - no
     - ``true``
     - Mutating tools are rejected while true
   * - ``GROUPOFFICE_VERIFY_SSL``
     - no
     - ``true``
     - Verify TLS certificates
   * - ``GROUPOFFICE_TIMEOUT``, ``GROUPOFFICE_MAX_RETRIES``
     - no
     - 30 s, 3
     - Request timeout and connection-level retries
   * - ``GROUPOFFICE_DEBUG``
     - no
     - ``false``
     - Debug logging

Registration:

.. code-block:: bash

   sudo mcprack server edit mcp-server-groupoffice \
       --set-env GROUPOFFICE_URL=https://groupoffice.example.com \
       --add-secret-key GROUPOFFICE_API_TOKEN --allow-user-override
   sudo mcprack secret set mcp-server-groupoffice GROUPOFFICE_API_TOKEN

Store ``GROUPOFFICE_API_TOKEN`` in the secret store. Because the token identifies a
GroupOffice user, a per-user override gives every person their own view of
contacts, calendars and tasks.

Tools
-----

About 80 tools over the main GroupOffice entities — Contacts, Calendars, Tasks,
Notes, Projects, Comments, History, Users and more — following one pattern per
entity: ``query_*``, ``get_*``, ``list_*``, ``create_*``, ``update_*``,
``delete_*``, plus ``upload_*`` and ``download_*`` for files. Create, update, delete
and upload need ``GROUPOFFICE_READONLY=false``.
