Architecture
============

Components
----------

.. code-block:: text

   browser / CLI / sync tools ──► reverse proxy (TLS) ──► gunicorn :8912 (mcprack Flask app)
                                                              │
         ┌────────────────────────────────────────────────────┼────────────────────┐
         ▼                       ▼                            ▼                    ▼
     database               secret store              per-user FastMCP       per-server relays
   (users, servers,    (Vaultwarden via bw,          composition process  (stdio processes and
    ACL, requests)      or encrypted local store)       (loopback)          network backends)

- **The web application** serves the portal (``/``), the admin area (``/admin``),
  the REST API (``/api/v1``) and the MCP relay (``/proxy/mcp``).
- **The database** holds users, servers, permissions, selections, overrides,
  templates, API and OAuth tokens, login throttling state and the audit trail.
- **The secret store** holds backend credentials, either in Vaultwarden (through
  the ``bw`` CLI) or encrypted locally with a key derived from ``SECRET_KEY``.
- **Per-user composition**: mcprack starts a ``fastmcp`` composition process
  bound to ``127.0.0.1`` for the user. It mounts signed per-server relay URLs
  under stable namespaces and stops after 15 idle minutes. Each stdio backend
  still runs in its own per-user process.

A request, step by step
-----------------------

1. The client calls ``/proxy/mcp/aggregate`` with either a user-scoped signed
   path token or an ``Authorization: Bearer`` header
   (:doc:`relay-and-tokens`).
2. mcprack resolves the user and rebuilds the composition from the user's
   currently selected, enabled and permitted servers.
3. The composition mounts each server's signed per-server relay under a
   namespace derived from its name.
4. The per-server relay checks access again, resolves credentials, starts a
   per-user process for a ``command`` server or connects to a network ``url``.
5. Requests and responses cross both relays with only MCP protocol headers.

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
