mcp-server-nextcloud
====================

An MCP server for **Nextcloud**: notes, calendar, contacts, files (WebDAV), Deck, Talk, mail, news, Collectives and shares. Companion package: ``mcprack-mcp-server-nextcloud``. Binary: ``/usr/bin/mcp-server-nextcloud``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-nextcloud

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``NEXTCLOUD_HOST``
     - yes
     - Nextcloud base URL
   * - ``NEXTCLOUD_USERNAME``
     - yes
     - Nextcloud user (basic-auth mode)
   * - ``NEXTCLOUD_PASSWORD``
     - yes
     - App password (secret store; basic-auth mode)
   * - ``NEXTCLOUD_VERIFY_SSL, NEXTCLOUD_CA_BUNDLE``
     - no
     - Certificate verification and custom CA bundle
   * - ``NEXTCLOUD_OIDC_CLIENT_ID, _CLIENT_SECRET, _SCOPES``
     - no
     - OIDC authentication instead of basic auth (secret store for the secret)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-nextcloud
   sudo mcprack server edit mcp-server-nextcloud --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-nextcloud <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: The upstream server has no single read-only switch; see its README and ``server.json``. Use an app password for an account with limited rights.

Tools
-----

- Tool groups: ``nc_notes_*``, ``nc_calendar_*``, ``nc_contacts_*``, ``nc_webdav_*``, ``nc_share_*``, ``nc_mail_*``, ``nc_news_*``, ``deck_*``, ``talk_*``, ``collectives_*``, ``nc_shopping_list_*``.
