Aggregate endpoint and individual relays
========================================

Generated client configurations contain one per-user FastMCP composition URL.
It exposes tools, resources and prompts from the user's currently selected,
enabled and permitted servers. Components are namespaced by server name. Each
server also has an individual relay URL, shown on its detail card when the user
may access and has selected it.

Aggregate path token (default)
------------------------------

.. code-block:: text

  https://mcprack.example.com/proxy/mcp/aggregate/<token>

The token is signed and scoped to one user. It *is* the credential, so a file
that contains it must be treated like a password. Tokens carry a version:
``mcprack user revoke-tokens`` and account disablement invalidate them.
``PROXY_TOKEN_MAX_AGE_SECONDS`` gives new tokens a lifetime.

The ``claude``, ``cursor``, ``copilot`` and ``vscode`` client formats use this
form.

Aggregate Bearer URL
--------------------

.. code-block:: text

  https://mcprack.example.com/proxy/mcp/aggregate
   Authorization: Bearer <credential>

The credential is one of:

- a **personal API token** with the scope ``proxy:access`` (always available,
  ``PROXY_BEARER_ENABLED=true``), or
- an **OAuth access token** issued by mcprack when ``OAUTH_ENABLED=true``
  (:doc:`../howto/enable-oauth`).

The ``claude-code`` format uses this form: the URL can be committed because it
contains no secret.

Individual server URLs
----------------------

The server detail card shows a permitted, enabled and selected server's URL:

.. code-block:: text

  https://mcprack.example.com/proxy/mcp/<token>/<server_id>
  https://mcprack.example.com/proxy/mcp/<server_id>

The first form uses a signed per-server token; the second uses a Bearer
credential. Both routes recheck the user's current permission and selection.
The composition process also connects to these relays, so backend credentials
remain server-side.

Without a credential the aggregate route answers ``401`` with
``WWW-Authenticate: Bearer``. With OAuth enabled, Protected Resource Metadata is
available at ``/.well-known/oauth-protected-resource/proxy/mcp/aggregate``.

API tokens
----------

Users create tokens under *API tokens* or with ``POST /api/v1/tokens``. A token has
a name, scopes and an expiry (90 days unless you ask for another lifetime). Only
its hash is stored; the value is shown once. A token created by another token can
never be more powerful or longer-lived than its creator.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Scope
     - Allows
   * - ``profile:read``
     - Read the user's own profile
   * - ``servers:read``
     - List the servers visible to the user
   * - ``selections:manage``
     - Change the user's server selection
   * - ``overrides:manage``
     - Change the user's credential overrides
   * - ``config:read``
     - Read the user's generated client configuration
   * - ``tokens:manage``
     - Create and revoke tokens
   * - ``proxy:access``
     - Use the aggregate or individual Bearer relay route
   * - ``admin:read`` / ``admin:write``
     - Call the admin REST API (administrators only)
   * - ``*``, or no scope list
     - Unrestricted

.. warning::

   A token that reaches the admin API is a credential outside the second factor.
   An administrator who has not yet set up two-factor authentication — or whose
   session needs fresh re-authentication — cannot create one.

Headers that cross the relay
----------------------------

Towards the backend only protocol headers are sent (``Accept``, ``Content-Type``,
``Mcp-Session-Id``, ``Mcp-Protocol-Version``, ``Last-Event-ID``). The caller's own
``Authorization`` and ``Cookie`` are never forwarded; the backend's credential is
added from the server configuration. Towards the client only ``Content-Type``,
``Mcp-Session-Id``, ``Mcp-Protocol-Version``, ``Cache-Control``, ``Retry-After``
and ``Content-Encoding`` are copied back, so a backend cannot set cookies or
authentication challenges on the mcprack origin.
