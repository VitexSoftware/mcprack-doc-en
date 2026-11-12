Access control
==============

Servers, permissions and selections
-----------------------------------

Three separate things decide what a user sees:

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Concept
     - Meaning
   * - Enabled
     - Administrator-level switch of a server. A disabled server cannot be
       selected or reached; its information card remains visible to signed-in
       users.
   * - Permission
     - Whether a user *may* use a server (an allow or deny row per user and
       server).
   * - Selection
     - The servers a user *chose* to include in their aggregate endpoint.

With ``STRICT_SERVER_PERMISSIONS=true`` (the default) a user with no permission
rows has no usable servers: access is explicit. Users can still browse server
cards and request permission. This matters because an LDAP account is created on
first login for anybody the directory authenticates. Set it to
``false`` only on a trusted network where everybody may use everything.

Requesting access
-----------------

A user who is not permitted to use an enabled server can submit an access request
from its detail card. Administrators review pending requests under *Admin →
Access Requests*. Approval grants the permission but does not add the server to
the user's subscriptions; the user chooses it on the *MCP servers* page. A denied
request can be submitted again later.

Templates
---------

A *configuration template* bundles permissions and pre-selected servers (for
example "support team"). Applying a template to a user replaces their permissions
and selection with the template's; individual credential overrides are kept.
Templates are not live links — editing one does not change users it was applied
to.

.. code-block:: bash

   sudo mcprack template create support --label "Support team"
   sudo mcprack template set-servers support --allow zabbix --allow redmine --select zabbix
   sudo mcprack template apply support alice

Per-user overrides
------------------

A server can allow users to override individual environment values (for example a
personal API token). Rules that protect the shared credentials:

- A user may set only the names the server declares, plus names that look like a
  credential — whose last word is ``TOKEN``, ``SECRET``, ``PASSWORD``, ``KEY``,
  ``PAT``, ``AUTH``, ``COOKIE`` or similar. Names
  that change how a process behaves (``PATH``, ``LD_*``, ``NODE_OPTIONS``,
  ``PYTHON*``, proxy and CA settings ...) are always refused.
  ``OVERRIDE_UNDECLARED_KEYS=any`` allows other free-form names; the refusal list
  still applies.
- If a user re-points an *endpoint* value (a name ending ``_URL``, ``_HOST``,
  ``_INSTANCE``, ``_ENDPOINT``), the administrator's shared secrets are **not**
  passed along with it: the user's own credentials are used instead.

Administrators
--------------

Administrators can use the admin area and the admin REST API. They need a second
factor (:doc:`../security/two-factor`) and must confirm the password again before
the most dangerous actions (:doc:`../security/reauthentication`).
