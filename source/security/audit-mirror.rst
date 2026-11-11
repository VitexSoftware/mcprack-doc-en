The audit mirror
================

The audit table can be edited by anyone with database access, and nothing in it
would show. So every audit event is **also** written, as one authenticated line, to
places the database does not control:

- **standard error** — the systemd journal (``journalctl -u mcprack | grep AUDIT``),
  which you can ship off the host;
- optionally a **file**: ``/var/log/mcprack/audit.log`` by default when that
  directory is writable (``AUDIT_LOG_FILE=/other/path``, or ``off``), rotated by the
  packaged logrotate rule.

A line holds the row's id, the same fields as the row (never bodies or credentials)
and a MAC (HMAC-SHA-256) keyed from ``SECRET_KEY``; ``SECRET_KEY_FALLBACKS`` keeps
lines verifiable after a rotation. An event whose database row could not be
written — database down, or sabotaged — is still logged, with ``"id": null``.
``AUDIT_MIRROR_ENABLED=false`` switches the mirror off, ``AUDIT_MIRROR_STDERR=false``
only the journal copy.

Verifying
---------

.. code-block:: bash

   sudo mcprack audit-verify                            # /var/log/mcprack/audit.log and rotated copies
   sudo mcprack audit-verify --log /srv/shipped/audit.log --days 30
   sudo mcprack audit-verify --strict                   # rows without a line fail too

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Report
     - Meaning
   * - ``DELETED``
     - A line with no row: the row was removed
   * - ``ALTERED``
     - A row that differs from its line (the fields are named); a user or server
       reference that became empty because the user or server was deleted is not
       reported
   * - ``TAMPERED LOG``
     - A line whose MAC is wrong: the log was edited (or ``SECRET_KEY`` changed
       without ``SECRET_KEY_FALLBACKS``)
   * - ``REUSED ID``
     - Two different events carry one id: a row was deleted and the next event
       was given its id
   * - ``warning: ... no line in the log``
     - A row nobody logged: inserted, or written while the mirror was off
       (a failure with ``--strict``)

Exit status 1 for the first four, 2 if there is no log to check. Lines older than
``AUDIT_RETENTION_DAYS`` are not checked, because ``audit-archive`` legitimately
removes those rows. After *restoring a database backup* new events reuse ids the
backup lost, so ``REUSED ID`` is expected: rotate the log when you restore and
verify the new one.

What it proves
--------------

It is tamper **evidence**, not prevention, and it only means something if the
attacker cannot also rewrite the log. Ship the journal off the host
(``systemd-journal-upload``, rsyslog ``imjournal``) or make the file append-only
(``chattr +a``). Run ``audit-verify`` from cron and alert on a non-zero exit.

How the file is opened
----------------------

The log directory belongs to the service user while the command line tool may run
as root, so the file is opened without following symbolic links, must be a plain
file with a single hard link, is never a FIFO, and its owner and mode are set only
on a file just created (root hands it to the directory's owner). An existing file
is never ``chown``-ed or ``chmod``-ed.
