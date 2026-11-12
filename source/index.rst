.. title:: mcprack Documentation

Welcome to mcprack's documentation!
===================================

.. image:: _static/project-logo.svg
   :alt: mcprack logo
   :align: center
   :width: 96px

**mcprack** is a catalog and client-configuration portal for `MCP
<https://modelcontextprotocol.io/>`_ (Model Context Protocol) servers. An
administrator registers MCP servers once; every user gets one aggregate MCP URL
for their permitted subscriptions and a ready-to-use configuration for Claude
Desktop, Claude Code, Cursor or VS Code. Users can browse all registered servers
and request access from an administrator. Clients never start a local process
and never see a backend credential: they talk to a per-user FastMCP composition
endpoint on the mcprack server.

**Version 1.8.0** adds a per-user FastMCP composition endpoint, aggregate client
configurations, server subscription requests and a separate server discovery
page. It also includes two-factor authentication (required for administrators),
fresh re-authentication for dangerous administrator actions, a tamper-evident
audit mirror, command and URL policies, classified start-up diagnostics,
``mcprack user config verify`` and a secret-free Claude Code configuration format.

Key Features
------------

- **One catalog, many clients**: generated configuration for Claude Desktop,
  Claude Code, Cursor and VS Code / GitHub Copilot.
- **One aggregate endpoint**: the per-user FastMCP composition exposes tools,
  resources and prompts from subscribed servers under stable namespaces.
- **Per-server access**: users browse the registry, request denied access, and
  can copy an individual relay URL from a permitted server's detail card.
- **Credentials stay on the server**: shared credentials live in Vaultwarden or in
  an encrypted local store, and are injected when a request arrives. Users can
  override individual values for themselves.
- **Access control**: per-user server permissions, configuration templates,
  personal API tokens with scopes, optional MCP OAuth for clients such as Claude.
- **Security for the open internet**: LDAP or local accounts, two-factor
  authentication, login throttling, CSRF and session revocation, a command and
  URL destination policy, an audit trail with an HMAC-signed mirror.
- **Operations**: Debian packages, a systemd unit, an Apache vhost, Zabbix
  monitoring endpoint, OpenTelemetry, an Ansible collection.

Related projects
----------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Project
     - Purpose
   * - `mcprack <https://github.com/VitexSoftware/mcprack>`_
     - The web application, REST API and ``mcprack`` command line tool
   * - `mcprack-client <https://github.com/VitexSoftware/mcprack-client>`_
     - Shared library of the sync tools
   * - `mcprack-sync-claude <https://github.com/VitexSoftware/mcprack-sync-claude>`_,
       `-cursor <https://github.com/VitexSoftware/mcprack-sync-cursor>`_,
       `-vscode <https://github.com/VitexSoftware/mcprack-sync-vscode>`_
     - Keep a client's MCP configuration in sync with mcprack
   * - `mcprack-ansible-collection <https://github.com/VitexSoftware/mcprack-ansible-collection>`_
     - ``vitexsoftware.mcprack`` Ansible collection
   * - ``mcp-server-*``
     - MCP servers that ship a ``mcprack-mcp-server-*`` companion package —
       see :doc:`servers/index`

Getting Started
---------------

1. :doc:`quickstart` — a running instance and a first server in ten minutes
2. :doc:`install` — installation, the files mcprack uses, upgrading
3. :doc:`howto/connect-claude-code` — connect Claude Code

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   what-is-mcprack
   quickstart
   install

.. toctree::
   :maxdepth: 2
   :caption: Core Concepts

   concepts/architecture
   concepts/relay-and-tokens
   concepts/access-control
   concepts/credentials
   concepts/audit

.. toctree::
   :maxdepth: 2
   :caption: How-To Guides

   howto/register-server
   howto/grant-access
   howto/connect-claude-code
   howto/connect-other-clients
   howto/enable-oauth
   howto/verify-config
   howto/change-listen-address
   howto/rotate-secret-key
   howto/monitoring

.. toctree::
   :maxdepth: 2
   :caption: Security

   security/overview
   security/authentication
   security/two-factor
   security/reauthentication
   security/policies
   security/audit-mirror
   security/internet-checklist

.. toctree::
   :maxdepth: 2
   :caption: Client Tools

   clients/mcprack-client
   clients/sync-claude
   clients/sync-cursor
   clients/sync-vscode

.. toctree::
   :maxdepth: 2
   :caption: Automation

   ansible/collection

.. toctree::
   :maxdepth: 2
   :caption: MCP Servers with a Companion

   servers/index
   servers/companion-packages
   servers/abraflexi
   servers/adb
   servers/cc-token-saver
   servers/coinbase
   servers/datovka
   servers/email
   servers/filesystem
   servers/googleoffice
   servers/graylog
   servers/groupoffice
   servers/invokeai
   servers/librenms
   servers/linkedin
   servers/magento
   servers/mastodon
   servers/ms-365
   servers/multiflexi
   servers/netbox
   servers/nextcloud
   servers/patreon
   servers/raynet
   servers/redmine
   servers/semaphore
   servers/subreg
   servers/wakatime
   servers/warden
   servers/wazuh
   servers/webdriver
   servers/zabbix

.. toctree::
   :maxdepth: 2
   :caption: Reference

   reference/configuration
   reference/cli
   reference/rest-api
   reference/client-formats
   reference/troubleshooting

.. toctree::
   :maxdepth: 2
   :caption: Development

   development/packaging-mcp-servers
   development/contributing
