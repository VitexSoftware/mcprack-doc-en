Command line reference
======================

``mcprack`` loads ``/etc/mcprack/env`` when it can read it, so run it with
``sudo`` (or as a member of the ``mcprack`` group). ``mcprack COMMAND --help`` shows
the options of any command.

Servers
-------

.. list-table::
   :widths: 34 66

   * - ``server list`` / ``show NAME``
     - List servers / show one's non-secret configuration
   * - ``server create NAME``
     - Create a server, or update it in place (idempotent). Options: ``--label``,
       ``--transport stdio|http|sse``, ``--command``, ``--arg`` (repeatable),
       ``--url``, ``--category``, ``--enabled/--disabled``, ``--set-env KEY=VALUE``
   * - ``server edit NAME``
     - Change label, description, category, command, args, URL, auth header,
       environment (``--set-env``, ``--unset-env``), ``--add-secret-key``,
       ``--allow-user-override``
   * - ``server enable`` / ``disable NAME``
     - Show or hide a server
   * - ``server delete NAME``
     - Delete a server and its stored secrets
   * - ``server import-env NAME FILE``
     - Import ``KEY=VALUE`` pairs from a ``.env`` file; credential-looking keys go to
       the secret store
   * - ``server test NAME``
     - Connect, perform the MCP handshake and print tools, resources and prompts
       (``--timeout``, ``--json``)
   * - ``server probe COMMAND``
     - The same for a command that is not registered (``--set-env``)

Secrets
-------

.. list-table::
   :widths: 34 66

   * - ``secret backend``
     - Which backend is active
   * - ``secret list SERVER``
     - Which declared keys have a value
   * - ``secret set SERVER KEY``
     - Set a value (``--value`` or a hidden prompt)
   * - ``secret unset SERVER KEY``
     - Remove a value

Users
-----

.. list-table::
   :widths: 34 66

   * - ``user list``, ``create``, ``delete``
     - Manage local accounts (``create --username --password --email --admin``)
   * - ``user promote`` / ``demote``
     - Grant or revoke the administrator flag
   * - ``user enable`` / ``disable``
     - Allow or block sign-in (disabling also stops their MCP processes)
   * - ``user passwd``
     - Reset a local password
   * - ``user revoke-tokens USER``
     - Kill proxy URLs, API tokens and OAuth tokens; stop their processes
   * - ``user mfa-status USER`` / ``mfa-reset USER``
     - Two-factor state; switch it off and end their sessions
   * - ``user server allow|deny USER SERVER``
     - Permission for one server
   * - ``user server list USER`` / ``select USER SERVER...``
     - Show state / set the servers in the generated configuration
   * - ``user override list|set|reset``
     - Individual credential values (:doc:`../concepts/access-control`)
   * - ``user config show|download|verify USER [CLIENT]``
     - Print, save (mode ``0600``) or verify the generated configuration
       (:doc:`../howto/verify-config`)

Templates
---------

``template list``, ``show``, ``create NAME --label``, ``delete``,
``set-servers NAME --allow/--deny/--select/--deselect SERVER``, ``apply NAME USER``.

Maintenance
-----------

.. list-table::
   :widths: 34 66

   * - ``create-admin``
     - Create the first local administrator (``--username``, ``--password-file`` or
       prompt)
   * - ``init-config``
     - Initialise or repair ``/etc/mcprack/env`` (generates ``SECRET_KEY``)
   * - ``db upgrade`` / ``downgrade`` / ``current`` / ``history``
     - Database migrations
   * - ``audit-archive``
     - Export and delete old audit entries (``--days``, ``--format json|csv``,
       ``--output``, ``--dry-run``)
   * - ``audit-verify``
     - Compare the audit table with its signed mirror
       (:doc:`../security/audit-mirror`)

Stand-alone tool
----------------

``mcprack-mcp-probe [--tools] [--call NAME --args JSON] [--method M] [--bearer] URL``
probes any MCP HTTP endpoint (:doc:`../howto/verify-config`).
