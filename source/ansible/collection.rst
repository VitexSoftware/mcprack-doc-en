Ansible collection
==================

``vitexsoftware.mcprack`` installs, configures and manages mcprack. It covers the
mcprack **application** only: the package, ``/etc/mcprack/env``, an nginx front end,
local administrator accounts and catalog entries. It deliberately does not manage
the runtime of individual MCP servers.

Requirements: Debian or Ubuntu targets, and the ``community.general`` collection
for UFW rules (disable with ``mcprack_firewall_enabled: false``).

The role
--------

``vitexsoftware.mcprack.app``:

1. adds the VitexSoftware apt repository and installs ``mcprack`` (optionally a
   local PostgreSQL server for it);
2. overlays deployment settings onto ``/etc/mcprack/env`` (the package's own
   ``SECRET_KEY`` and database URI are never overwritten);
3. optionally fronts the application with nginx and opens UFW rules;
4. waits for ``/health`` to answer 200;
5. creates the configured local administrators, generating and caching their
   passwords under ``credentials/mcprack-admin-<user>.txt`` (add it to
   ``.gitignore``);
6. registers the configured catalog servers.

.. list-table::
   :header-rows: 1
   :widths: 32 20 48

   * - Variable
     - Default
     - Purpose
   * - ``mcprack_domain``
     - ``mcprack.example.com``
     - Virtual host name and health-check host
   * - ``mcprack_reverse_proxy_enabled``
     - ``true``
     - Front with nginx on ``mcprack_http_port``
   * - ``mcprack_firewall_enabled``
     - ``true``
     - Manage UFW rules
   * - ``mcprack_ufw_allow_from``
     - ``[]``
     - CIDRs allowed through the firewall
   * - ``mcprack_db_type``
     - ``pgsql``
     - dbconfig-common backend
   * - ``mcprack_admin_users``
     - ``[]``
     - Local administrators to create
   * - ``mcprack_catalog_servers``
     - ``[]``
     - Catalog entries to register

Secrets (``mcprack_db_password``, ``mcprack_ldap_bind_password``, ``mcprack_bw_*``)
are empty by default: supply them from a vaulted vars file.

.. code-block:: yaml

   - hosts: mcprack_servers
     become: true
     roles:
       - role: vitexsoftware.mcprack.app
         vars:
           mcprack_domain: mcprack.example.com
           mcprack_ufw_allow_from: ["10.0.0.0/24"]
           mcprack_admin_users: [alice]
           mcprack_catalog_servers:
             - name: netbox
               label: NetBox
               transport: http
               url: "https://netbox.example.com/mcp"
               category: infra

.. note::

   An administrator created by the role must set up two-factor authentication at the
   first sign-in (``MFA_REQUIRED_FOR_ADMINS``). Put ``MFA_REQUIRED_FOR_ADMINS=false``
   into the role's environment overlay if you provision administrators for
   automation only, and use API tokens for that.

Modules
-------

All modules run the ``mcprack`` CLI on the managed node and need ``become: true``
(``/etc/mcprack/env`` is ``root:mcprack 0640``). See ``ansible-doc
vitexsoftware.mcprack.<name>``.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Module
     - Wraps
     - Purpose
   * - ``mcprack_server``
     - ``mcprack server ...``
     - Register, update, remove catalog servers
   * - ``mcprack_user``
     - ``mcprack user ...``
     - Create, update, remove local users; admin flag; enable/disable; password
   * - ``mcprack_user_access``
     - ``mcprack user server allow/deny``
     - Per-user, per-server allow or deny
   * - ``mcprack_user_selection``
     - ``mcprack user server select``
     - A user's pre-selected servers
   * - ``mcprack_user_override``
     - ``mcprack user override ...``
     - Per-user credential overrides
   * - ``mcprack_user_config``
     - ``mcprack user config show/download``
     - Read-only: fetch a rendered client configuration
   * - ``mcprack_secret``
     - ``mcprack secret ...``
     - Set or unset a server's secret keys
   * - ``mcprack_template``
     - ``mcprack template ...``
     - Create, update, remove templates
   * - ``mcprack_template_apply``
     - ``mcprack template apply``
     - Apply a template to a user (one-shot)

.. code-block:: yaml

   - name: Allow Alice to use Zabbix
     vitexsoftware.mcprack.mcprack_user_access:
       username: alice
       server: zabbix
       access: allow
     become: true
