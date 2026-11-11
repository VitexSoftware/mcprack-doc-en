Security overview
=================

mcprack sits between AI clients and systems that hold real credentials, and it runs
other people's programs. This chapter describes what it does about that and what
you have to configure.

Threat model
------------

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Who
     - What mcprack does
   * - The internet
     - TLS in front, a default-deny virtual host, secure cookies, CSRF protection,
       login throttling, strict host checking (``PUBLIC_BASE_URL``)
   * - A user with a password
     - Per-user permissions, per-user processes, scrubbed environment,
       credentials resolved server-side, overrides limited by policy
   * - A stolen session or password
     - Two-factor authentication, server-side session revocation, password and
       code re-confirmed before dangerous actions
   * - A compromised administrator
     - Command and URL policies, audit entries that name the command, an
       HMAC-signed audit mirror outside the database
   * - A malicious or broken MCP server
     - Allowlisted request/response headers, size limits, no access to mcprack's
       own secrets, classified start-up failures

What it does not do
-------------------

- An MCP server is a program running as the service user. mcprack does not sandbox
  it beyond the systemd unit and a scrubbed environment: there is no separate user
  or container per server. Install only servers you trust.
- The loopback ports of the per-user ``fastmcp`` processes are predictable and not
  authenticated; do not run untrusted local users on the mcprack host.
- The audit mirror makes tampering *visible*; it does not prevent it
  (:doc:`audit-mirror`).

Where to go
-----------

.. list-table::
   :widths: 30 70

   * - :doc:`authentication`
     - Local accounts, LDAP, sessions, login throttling, password reset
   * - :doc:`two-factor`
     - TOTP, recovery codes, who must have it, how to recover
   * - :doc:`reauthentication`
     - The password again before dangerous actions
   * - :doc:`policies`
     - Command location, URL destinations, overrides, installer
   * - :doc:`audit-mirror`
     - ``flask audit-verify`` and shipping the log
   * - :doc:`internet-checklist`
     - The list to go through before exposing an instance
