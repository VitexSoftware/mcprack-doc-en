MCP servers with a mcprack companion
====================================

These MCP servers are packaged as Debian packages **together with a companion
package** that registers them in a local mcprack catalog. Install the companion and
the server appears in the catalog; remove it and the entry disappears
(:doc:`companion-packages`).

.. list-table::
   :header-rows: 1
   :widths: 24 26 50

   * - Server package
     - Companion
     - Integrates
   * - :doc:`mcp-server-abraflexi <abraflexi>`
     - ``mcprack-mcp-server-abraflexi``
     - AbraFlexi ERP (74 tools)
   * - :doc:`mcp-server-adb <adb>`
     - ``mcprack-mcp-server-adb``
     - Android phone control over ADB
   * - :doc:`mcp-server-cc-token-saver <cc-token-saver>`
     - ``mcprack-mcp-server-cc-token-saver``
     - Local-LLM delegation (9 tools)
   * - :doc:`mcp-server-coinbase <coinbase>`
     - ``mcprack-mcp-server-coinbase``
     - Coinbase Advanced Trade API
   * - :doc:`mcp-server-datovka <datovka>`
     - ``mcprack-mcp-server-datovka``
     - Czech ISDS data boxes (10 tools)
   * - :doc:`mcp-server-email <email>`
     - ``mcprack-mcp-server-email``
     - IMAP/SMTP email
   * - :doc:`mcp-server-filesystem <filesystem>`
     - ``mcprack-mcp-server-filesystem``
     - Linux filesystem operations (10 tools)
   * - :doc:`mcp-server-googleoffice <googleoffice>`
     - ``mcprack-mcp-server-googleoffice``
     - Google Workspace
   * - :doc:`mcp-server-graylog <graylog>`
     - ``mcprack-mcp-server-graylog``
     - Graylog log management (bridge to built-in MCP, or 5 read-only REST tools)
   * - :doc:`mcp-server-groupoffice <groupoffice>`
     - ``mcprack-mcp-server-groupoffice``
     - GroupOffice groupware (82 tools)
   * - :doc:`mcp-server-invokeai <invokeai>`
     - ``mcprack-mcp-server-invokeai``
     - InvokeAI image generation (5 tools)
   * - :doc:`mcp-server-librenms <librenms>`
     - ``mcprack-mcp-server-librenms``
     - LibreNMS network monitoring (113 tools)
   * - :doc:`mcp-server-linkedin <linkedin>`
     - ``mcprack-mcp-server-linkedin``
     - LinkedIn through a browser session
   * - :doc:`mcp-server-magento <magento>`
     - ``mcprack-mcp-server-magento``
     - Magento 2 store queries (14 tools)
   * - :doc:`mcp-server-mastodon <mastodon>`
     - ``mcprack-mcp-server-mastodon``
     - Mastodon social network (54 tools)
   * - :doc:`mcp-server-ms-365 <ms-365>`
     - ``mcprack-mcp-server-ms-365``
     - Microsoft 365 mail, calendar and tasks
   * - :doc:`mcp-server-multiflexi <multiflexi>`
     - ``mcprack-mcp-server-multiflexi``
     - MultiFlexi automation platform
   * - :doc:`mcp-server-netbox <netbox>`
     - ``mcprack-mcp-server-netbox``
     - NetBox infrastructure data (read-only)
   * - :doc:`mcp-server-nextcloud <nextcloud>`
     - ``mcprack-mcp-server-nextcloud``
     - Nextcloud groupware
   * - :doc:`mcp-server-patreon <patreon>`
     - ``mcprack-mcp-server-patreon``
     - Patreon creator data
   * - :doc:`mcp-server-raynet <raynet>`
     - ``mcprack-mcp-server-raynet``
     - Raynet CRM (59 tools)
   * - :doc:`mcp-server-redmine <redmine>`
     - ``mcprack-mcp-server-redmine``
     - Redmine project management (79 tools)
   * - :doc:`mcp-server-semaphore <semaphore>`
     - ``mcprack-mcp-server-semaphore``
     - Semaphore UI (Ansible automation; 37 tools)
   * - :doc:`mcp-server-subreg <subreg>`
     - ``mcprack-mcp-server-subreg``
     - Subreg.cz domain registrar (21 tools)
   * - :doc:`mcp-server-wakatime <wakatime>`
     - ``mcprack-mcp-server-wakatime``
     - WakaTime summaries (2 tools)
   * - :doc:`mcp-server-warden <warden>`
     - ``mcprack-mcp-server-warden``
     - Vaultwarden/Bitwarden vault
   * - :doc:`mcp-server-wazuh <wazuh>`
     - ``mcprack-mcp-server-wazuh``
     - Wazuh 5 security monitoring (12 tools)
   * - :doc:`mcp-server-webdriver <webdriver>`
     - ``mcprack-mcp-server-webdriver``
     - Firefox browser automation (43 tools)
   * - :doc:`mcp-server-zabbix <zabbix>`
     - ``mcprack-mcp-server-zabbix``
     - Zabbix monitoring (3 tools)

The tool counts are those of the current source. Every server in this list is
**read-only by default**: a variable named ``READ_ONLY``, ``*_READONLY`` or
similar must be set to ``false`` before any tool that changes something works. An
empty or unset value stays read-only. Keep it that way until a user actually needs
writes, and prefer a *per-user override* of the credentials over a shared account
with write rights.

Installing a server and registering it
--------------------------------------

.. code-block:: bash

   sudo apt install mcprack-mcp-server-mastodon     # pulls in mcp-server-mastodon
   sudo mcprack server show mcp-server-mastodon
   sudo mcprack server edit mcp-server-mastodon \
       --set-env MASTODON_INSTANCE=https://mastodon.social \
       --add-secret-key MASTODON_ACCESS_TOKEN --allow-user-override
   sudo mcprack secret set mcp-server-mastodon MASTODON_ACCESS_TOKEN

The registration contains only the command; **credentials are not part of it**. Set
them as described on each server's page.

Other MCP servers
-----------------

Any MCP server can be registered by hand (:doc:`../howto/register-server`) without
a companion package. A companion is worth building when you package the server for
Debian yourself (:doc:`../development/packaging-mcp-servers`).
