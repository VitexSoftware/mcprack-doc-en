Architecture
============

Components
----------

.. code-block:: text

   browser / CLI / sync tools ──► reverse proxy (TLS) ──► gunicorn :8912 (mcprack Flask app)
                                                              │
         ┌────────────────────────────────────────────────────┼────────────────────┐
         ▼                       ▼                            ▼                    ▼
     database               secret store                per-user fastmcp      network backends
   (users, servers,    (Vaultwarden via bw,            processes (loopback,   (relayed, credentials
    ACL, audit)         or encrypted local store)       one per user+server)   injected)

- **The web application** serves the portal (``/``), the admin area (``/admin``),
  the REST API (``/api/v1``) and the MCP relay (``/proxy/mcp``).
- **The database** holds users, servers, permissions, selections, overrides,
  templates, API and OAuth tokens, login throttling state and the audit trail.
- **The secret store** holds backend credentials, either in Vaultwarden (through
  the ``bw`` CLI) or encrypted locally with a key derived from ``SECRET_KEY``.
- **Per-user processes**: for a server with a ``command``, mcprack starts a
  ``fastmcp`` process bound to ``127.0.0.1`` for that (user, server) pair on the
  first request and stops it after 15 idle minutes.

A request, step by step
-----------------------

1. The client calls ``POST /proxy/mcp/...`` with either a signed path token or an
   ``Authorization: Bearer`` header (:doc:`relay-and-tokens`).
2. mcprack resolves the user, checks that the account is active, that the server
   is enabled and that the user selected it and may use it.
3. It resolves the credentials for that user (shared values plus the user's own
   overrides) from the secret store.
4. For a ``command`` server it ensures the per-user process is running; for a
   ``url`` server it opens a connection to the backend.
5. It forwards the request (only protocol headers cross the relay), and streams
   or returns the answer (only protocol headers come back).

Failure handling
----------------

A failed start is classified, so the cause is visible:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Class
     - Meaning
   * - ``spawn_failed``
     - The process could not be launched (binary missing, not executable)
   * - ``exited_early``
     - The process died during start-up; the log tail is in the audit entry
   * - ``startup_timeout``
     - Running, but it never answered on its port in time
   * - ``handshake_error`` / ``http_error``
     - It answered ``initialize`` with an error
   * - ``no_tools``
     - It started but serves no tools (usually crashed while loading)
   * - ``busy``
     - Too many servers are starting at once; retry shortly
   * - ``forbidden``
     - The command is refused by the command policy (:doc:`../security/policies`)

Administrators see the class and the tail of the instance log (Admin → Proxy
instances, the audit trail); users receive the class and who to ask, never log
lines.

Limits
------

- A buffered (non-streaming) backend answer may be at most 16 MiB.
- At most three MCP servers start at the same time in one worker process; others
  wait up to ten seconds (``MCP_COLD_START_CONCURRENCY``, ``MCP_COLD_START_WAIT``).
- Server-sent-event answers are streamed without buffering
  (``X-Accel-Buffering: no``). The standalone ``GET`` stream of Streamable HTTP is
  answered ``405`` for stdio-implemented and Streamable HTTP servers; clients use
  ``POST``.
