Fresh authentication for dangerous actions
==========================================

An administrator's browser session can be stolen, and a stolen session has already
passed the password and the second factor. So the actions that run code, change who
has access or move secrets need the password — and the code, for an account with
two-factor authentication — **again**, unless the session was authenticated in the
last ``ADMIN_REAUTH_SECONDS`` (600). Signing in counts.

What asks again
---------------

- registering, editing, deleting and auto-detecting servers;
- installing and uninstalling packages;
- creating and changing user accounts (including making somebody an administrator);
- resetting somebody's two-factor authentication;
- moving the secret store between Vaultwarden and the local store;
- creating an API token that could reach the admin API.

Everything that only reads, or takes access away (revoking tokens, stopping a
proxy, templates, per-user overrides), stays one click.

How it looks
------------

In the web interface the action redirects to *Confirm your identity* and back; the
form you were filling in is not saved, so you submit it again. Over the REST API
the answer is ``403`` with the code ``reauth_required``:

.. code-block:: bash

   curl -b cookies -H "X-CSRFToken: $CSRF" -H 'Content-Type: application/json' \
        -d '{"password": "...", "code": "123456"}' \
        https://mcprack.example.com/api/v1/auth/reauth

The response ``{"data": {"fresh_for": 600}}`` is valid for that many seconds.
Wrong answers are throttled and audited like sign-in failures; a wrong password
never uses up a code.

What it does not affect
-----------------------

- **Bearer tokens** are credentials of their own, with scopes and an expiry.
- Ordinary users, and the public demo.

``ADMIN_REAUTH_SECONDS=0`` switches the check off. A session from before the
upgrade has no timestamp and is asked once.

For developers
--------------

``mcprack/reauth.py`` lists the guarded endpoints (``SENSITIVE_ENDPOINTS``) and,
with a reason, every other mutating admin endpoint. A test walks the URL map and
fails for a new admin route that is in neither list, so the decision cannot be
skipped. An endpoint that issues a long-lived credential must also decide in its
view (``CHECKED_IN_THE_VIEW``): otherwise a stolen session could simply mint itself
a token.
