Enabling MCP OAuth
==================

With OAuth, MCP clients such as Claude sign in themselves and hold revocable
Bearer tokens instead of a secret in a URL.

.. code-block:: bash

   # /etc/mcprack/env
   OAUTH_ENABLED=true
   PUBLIC_BASE_URL=https://mcprack.example.com

mcprack then serves the discovery documents (``/.well-known/oauth-protected-resource``,
``/.well-known/oauth-authorization-server``) and the endpoints ``/oauth/authorize``,
``/oauth/token``, ``/oauth/register`` and ``/oauth/revoke``. The relay URL becomes
``/proxy/mcp/<server_id>`` and answers ``401`` with a challenge that points clients
at the discovery document. Path-token URLs keep working.

Redirect policy
---------------

Dynamic client registration is open (the MCP specification allows it), so the
redirect addresses a client may register are limited:

- loopback addresses (``http://127.0.0.1:port/...``, ``localhost``),
- ``https://`` addresses of hosts in ``OAUTH_ALLOWED_REDIRECT_HOSTS`` (default
  ``claude.ai,claude.com``; ``*.example.com`` is allowed),
- addresses starting with a prefix in ``OAUTH_ALLOWED_REDIRECT_PREFIXES``
  (custom schemes of desktop applications).

The consent page shows the user exactly where the authorization code will be sent.

Tokens and limits
-----------------

- Access tokens last ``OAUTH_ACCESS_TOKEN_EXPIRES`` seconds (default 3600),
  refresh tokens ``OAUTH_REFRESH_TOKEN_EXPIRES`` (30 days). Tokens are stored as
  hashes.
- At most ``OAUTH_MAX_CLIENTS`` (500) clients are kept. Unused clients are removed
  after ``OAUTH_UNUSED_CLIENT_TTL_HOURS`` (24) and may be evicted to make room, but
  never one registered in the last ``OAUTH_CLIENT_MIN_AGE_SECONDS`` (15 minutes)
  or one with a pending authorization.
- Registration is rate limited per client address (per ``/64`` for IPv6):
  ``OAUTH_REGISTER_RATE_LIMIT``. A coordinated flood from many addresses can still
  fill the client table; restrict ``/oauth/register`` at the reverse proxy if that
  matters.
- Consent, client registration and token issue are audited.

``mcprack user revoke-tokens USER`` revokes OAuth tokens too.
