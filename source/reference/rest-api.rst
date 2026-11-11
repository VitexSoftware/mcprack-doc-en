REST API
========

The API lives under ``/api/v1``. The machine-readable description is served at
``/api/v1/openapi.json`` (OpenAPI 3).

Authentication
--------------

- **Bearer token** — a personal API token: ``Authorization: Bearer mcr_...``. What
  it may do is limited by its scopes (:doc:`../concepts/relay-and-tokens`).
- **Session cookie** — the browser session. State-changing requests then need the
  CSRF token in the ``X-CSRFToken`` header. Administrators with a cookie session
  need two-factor authentication and, for dangerous actions, a fresh confirmation
  (``POST /auth/reauth``, :doc:`../security/reauthentication`).

Answers are JSON: ``{"data": ...}`` (with ``pagination`` for lists) or
``{"error": {"code": ..., "message": ...}}``. Common codes: ``unauthorized`` (401),
``forbidden`` and ``insufficient_scope`` (403), ``reauth_required`` and
``mfa_required`` (403), ``invalid_request`` (400), ``conflict`` (409).

Endpoints for users
-------------------

.. list-table::
   :header-rows: 1
   :widths: 12 38 50

   * - Method
     - Path
     - Purpose
   * - GET
     - ``/me``
     - The current user's profile
   * - GET, POST
     - ``/tokens``
     - List / create API tokens (value shown once; scopes and expiry in the body)
   * - DELETE
     - ``/tokens/{tokenId}``
     - Revoke a token
   * - GET
     - ``/servers``
     - Servers visible to the user
   * - GET, PUT
     - ``/me/selections``
     - The selected servers
   * - GET, PUT, DELETE
     - ``/me/overrides/{serverId}``
     - Personal credential overrides (``?reveal=1`` returns the values)
   * - GET
     - ``/me/config/{client}``
     - Generated configuration: ``claude``, ``claude-code``, ``cursor``, ``vscode``,
       ``copilot``. ``?auth=token|oauth`` selects the header form for ``claude-code``
   * - POST
     - ``/auth/reauth``
     - Confirm password (and code) for administrator actions

Administrator endpoints
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 12 46 42

   * - Method
     - Path
     - Purpose
   * - GET, POST
     - ``/admin/servers``
     - List (``?include_health=1``) / register servers
   * - GET, PUT, DELETE
     - ``/admin/servers/{serverId}``
     - One server (``?reveal_secrets=1`` returns its secrets — audited)
   * - GET, POST
     - ``/admin/users``
     - List / create users
   * - GET, PUT, DELETE
     - ``/admin/users/{userId}``
     - One user and their permissions
   * - GET, PUT
     - ``/admin/users/{userId}/selections``
     - A user's selection
   * - GET, PUT, DELETE
     - ``/admin/users/{userId}/overrides/{serverId}``
     - A user's override
   * - GET
     - ``/admin/users/{userId}/config/{client}``
     - A user's generated configuration
   * - POST
     - ``/admin/users/{userId}/mfa-reset``
     - Switch off two-factor authentication
   * - POST
     - ``/admin/users/{userId}/revoke-tokens``
     - Revoke all programmatic credentials
   * - POST
     - ``/admin/users/{userId}/apply-template``
     - Apply a template
   * - GET, POST
     - ``/admin/templates``
     - List / create templates
   * - GET, PUT, DELETE
     - ``/admin/templates/{templateId}``
     - One template
   * - GET
     - ``/audit-log``
     - The audit trail (filterable)

A token needs ``admin:read`` for GET and ``admin:write`` for everything else.

Example
-------

.. code-block:: bash

   TOKEN=mcr_...
   curl -s -H "Authorization: Bearer $TOKEN" https://mcprack.example.com/api/v1/servers
   curl -s -X POST -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
        -d '{"name": "ci", "scopes": ["proxy:access"], "expires_in_days": 30}' \
        https://mcprack.example.com/api/v1/tokens
