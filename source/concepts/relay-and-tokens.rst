The relay and its credentials
=============================

Every selected server is exposed to a client as a relay URL. There are two forms.

Path token (default)
--------------------

.. code-block:: text

   https://mcprack.example.com/proxy/mcp/<token>/<server_id>

``<token>`` is a signed, per-user value. It *is* the credential, so a file that
contains it must be treated like a password. Tokens carry a version: changing the
user's token version (``mcprack user revoke-tokens``, disabling the account) kills
every URL at once. ``PROXY_TOKEN_MAX_AGE_SECONDS`` gives new tokens a lifetime;
fresh installations default to 90 days.

Used by the ``claude``, ``cursor``, ``copilot`` and ``vscode`` client formats.

Bearer (no secret in the URL)
-----------------------------

.. code-block:: text

   https://mcprack.example.com/proxy/mcp/<server_id>
   Authorization: Bearer <credential>

The credential is one of:

- a **personal API token** with the scope ``proxy:access`` (always available,
  ``PROXY_BEARER_ENABLED=true``), or
- an **OAuth access token** issued by mcprack when ``OAUTH_ENABLED=true``
  (:doc:`../howto/enable-oauth`).

This is the form of the ``claude-code`` format: the URL can be committed to a
repository because it contains no secret.

Without a credential the route answers ``401`` with ``WWW-Authenticate: Bearer``.

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
     - Use the Bearer relay route
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
