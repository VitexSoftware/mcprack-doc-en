Troubleshooting
===============

First steps
-----------

.. code-block:: bash

   sudo systemctl status mcprack
   sudo journalctl -u mcprack -n 100 --no-pager
   sudo mcprack server test NAME --timeout 30
   sudo mcprack user config verify USER claude-code --base-url http://127.0.0.1:8912

The last command probes mcprack without the reverse proxy. If it works and the same
without ``--base-url`` does not, the problem is in the proxy or TLS.

The service does not start
--------------------------

``SECRET_KEY`` is missing, a placeholder, shorter than 32 characters or too
uniform — the log says which. Generate one:
``python3 -c "import secrets; print(secrets.token_hex(32))"``. For a rotation see
:doc:`../howto/rotate-secret-key`.

Cannot sign in on plain HTTP
----------------------------

The session cookie is ``Secure`` by default and a browser does not send it back
over ``http://``. Put TLS in front, or on a trusted intranet set
``SESSION_COOKIE_SECURE=false``.

A client reports 401
--------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Situation
     - Cause
   * - Bearer URL (``/proxy/mcp/<id>``), no header
     - Missing credential. Set ``MCPRACK_TOKEN`` where the client starts.
   * - Bearer, token rejected
     - The token needs the ``proxy:access`` scope and must not be expired or revoked
   * - Path-token URL
     - Token expired (``PROXY_TOKEN_MAX_AGE_SECONDS``), revoked, the user is
       disabled, or the key was rotated without ``SECRET_KEY_FALLBACKS``
   * - Claude Code shows the variable empty
     - The variable must be exported in the environment Claude Code is started from

A client reports 502 with a message
-----------------------------------

The message names the class of failure (:doc:`../concepts/architecture`). The
administrator sees the log tail in the audit trail and *Admin → Proxy instances*.

``exited early``
   The command died at start. Run it as the service user:
   ``sudo -u mcprack /usr/bin/mcp-server-X`` and read the error. Typical: a missing
   Python dependency or a required variable that is not set.

``serves no tools``
   Started but crashed while loading — usually a wrong credential or URL. Check
   ``sudo mcprack server test NAME``.

``did not answer within ... s``
   A cold start slower than ``MCP_PROXY_HANDSHAKE_TIMEOUT`` (15 s). Raise it.

``busy``
   Many servers starting at once; retry. Tune ``MCP_COLD_START_CONCURRENCY``.

``refused by policy`` / "not permitted by the administrator's policy"
   The command is in a refused directory or outside ``ALLOWED_COMMAND_DIRS``
   (:doc:`../security/policies`).

``points at a backend address that is not allowed``
   A server URL is link-local or a metadata address.

An administrator is redirected to set up two-factor authentication
------------------------------------------------------------------

That is ``MFA_REQUIRED_FOR_ADMINS`` (:doc:`../security/two-factor`). For a
scripted setup against the REST API with a session cookie, the answer is ``403
mfa_required``; use an API token instead.

"Confirm your identity" appears
-------------------------------

The session did not sign in or confirm within ``ADMIN_REAUTH_SECONDS``
(:doc:`../security/reauthentication`).

A configuration sync is refused
-------------------------------

Exit status 3 means the answer contained something the client never accepts. The
messages name the server and the key. If the URLs point to another origin than
``MCPRACK_URL``, set ``MCPRACK_TRUSTED_ORIGINS`` (:doc:`../clients/mcprack-client`).

Vaultwarden errors
------------------

Users see a generic message; the cause is in the log (``journalctl -u mcprack``).
``sudo mcprack secret backend`` shows the active store. A failing ``bw`` login is
usually a wrong ``BW_CLIENTID``/``BW_CLIENTSECRET``/``BW_PASSWORD`` or an
unreachable ``BW_SERVER``.

Audit verification fails
------------------------

See the table in :doc:`../security/audit-mirror`. ``TAMPERED LOG`` right after a
``SECRET_KEY`` change means the old key is missing from ``SECRET_KEY_FALLBACKS``.
