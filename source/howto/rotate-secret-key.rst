Rotating the SECRET_KEY
=======================

``SECRET_KEY`` signs sessions, relay path tokens and password-reset links, keys
the local secret store, and authenticates the audit mirror. mcprack refuses to
start with a missing, placeholder (``change-me``, ``dev-...``), short (under 32
characters) or low-variety key.

Rotating it naively would sign everybody out, break every client configuration and
make the local secret store unreadable. Keep the old key as a *fallback*:

1. Generate a new key:

   .. code-block:: bash

      python3 -c "import secrets; print(secrets.token_hex(32))"

2. Edit ``/etc/mcprack/env``:

   .. code-block:: bash

      SECRET_KEY=<new key>
      SECRET_KEY_FALLBACKS=<old key>

   Several old keys are comma separated; each must be as strong as a ``SECRET_KEY``.

3. ``sudo systemctl restart mcprack``.

Everything signed or encrypted with an old key still verifies or decrypts; new
material uses the new key. Remove a fallback when nothing signed with it is left:
session cookies expire after ``SESSION_LIFETIME_SECONDS`` (8 hours), path tokens
after ``PROXY_TOKEN_MAX_AGE_SECONDS``, and the audit mirror lines stay verifiable
for as long as the fallback is listed.

.. note::

   The locally encrypted secrets are re-encrypted only when they are saved again.
   Keep the fallback until you have re-saved them, or moved to Vaultwarden.
