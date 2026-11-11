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
   * - :doc:`mcp-server-datovka <datovka>`
     - ``mcprack-mcp-server-datovka``
     - Czech ISDS data boxes (10 tools)
   * - :doc:`mcp-server-filesystem <filesystem>`
     - ``mcprack-mcp-server-filesystem``
     - Linux filesystem operations (10 tools)
   * - :doc:`mcp-server-graylog <graylog>`
     - ``mcprack-mcp-server-graylog``
     - Graylog log management (bridge to built-in MCP, or 5 read-only REST tools)
   * - :doc:`mcp-server-groupoffice <groupoffice>`
     - ``mcprack-mcp-server-groupoffice``
     - GroupOffice groupware (82 tools)
   * - :doc:`mcp-server-librenms <librenms>`
     - ``mcprack-mcp-server-librenms``
     - LibreNMS network monitoring (113 tools)
   * - :doc:`mcp-server-mastodon <mastodon>`
     - ``mcprack-mcp-server-mastodon``
     - Mastodon social network (54 tools)
   * - :doc:`mcp-server-semaphore <semaphore>`
     - ``mcprack-mcp-server-semaphore``
     - Semaphore UI (Ansible automation; 37 tools)
   * - :doc:`mcp-server-subreg <subreg>`
     - ``mcprack-mcp-server-subreg``
     - Subreg.cz domain registrar (21 tools)
   * - :doc:`mcp-server-wazuh <wazuh>`
     - ``mcprack-mcp-server-wazuh``
     - Wazuh 5 security monitoring (12 tools)
   * - :doc:`mcp-server-webdriver <webdriver>`
     - ``mcprack-mcp-server-webdriver``
     - Firefox browser automation (43 tools)

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
