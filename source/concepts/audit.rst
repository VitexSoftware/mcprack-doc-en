The audit trail
===============

mcprack records security-relevant events: sign-ins and failures, configuration
downloads, credential access, proxy starts and stops, administrator changes,
password and two-factor changes, OAuth consents and token issues.

An entry holds the time (UTC), the acting user, the server, the action and its
result, a short message, the source address and a request id that groups the
events of one request. **Request bodies, tool arguments and credential values are
never written.**

Registering or editing a server defines what the service user executes, so those
entries say what changed: the old and new **command**, the **URL host** (the path
only as a fingerprint — webhook URLs keep a secret in the path), the number of
**arguments with a ``sha256`` fingerprint** (never the arguments, which sometimes
carry a token) and the **names** of added or removed environment keys.

Viewing and retention
---------------------

Administrators browse the trail at **Admin → Audit Log** or through
``GET /api/v1/audit-log``. ``AUDIT_RETENTION_DAYS`` (default 90) is the retention
window; nothing is deleted automatically. Export and purge old entries:

.. code-block:: bash

   sudo mcprack audit-archive --dry-run
   sudo mcprack audit-archive                  # JSON, then delete
   sudo mcprack audit-archive --format csv --output /srv/archive/audit.csv

Tamper evidence
---------------

The table is append-only by convention. To make changes by somebody with database
access visible, every event is also written, authenticated, outside the database
(:doc:`../security/audit-mirror`).
