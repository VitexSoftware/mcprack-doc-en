Installation
============

Debian and Ubuntu packages
--------------------------

mcprack is packaged for Debian 12/13 and Ubuntu 24.04 in the VitexSoftware
repository.

.. code-block:: bash

   sudo apt install mcprack

Optional components:

.. code-block:: bash

   sudo apt install python3-fastmcp        # per-user stdio proxies (a Recommends: installed by default)

For the Vaultwarden secret backend install the Bitwarden CLI (``bw``) and set
``BW_BIN`` if it is not at ``/usr/bin/bw``.

Files and directories
---------------------

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Path
     - Purpose
   * - ``/etc/mcprack/env``
     - All settings (``root:mcprack``, mode ``0640``). Read by the service and by
       the ``mcprack`` command.
   * - ``/etc/mcprack/admin-credentials``
     - First administrator's generated password (root only; remove after use)
   * - ``/var/lib/mcprack``
     - Database (SQLite by default), installed packages, ``.bw`` Vaultwarden state
   * - ``/run/mcprack``
     - Volatile state of the per-user proxy processes (tmpfs, ``0700``)
   * - ``/var/log/mcprack``
     - ``access.log``, ``error.log`` and the audit mirror ``audit.log``
   * - ``mcprack.service``
     - systemd unit running gunicorn (4 workers, ``gthread``, 8 threads)

The command line tool
---------------------

``/usr/bin/mcprack`` loads ``/etc/mcprack/env`` when it can read it and forwards to
the management CLI, so run it with ``sudo``:

.. code-block:: bash

   sudo mcprack user list
   sudo mcprack server list

See :doc:`reference/cli`.

Configuration after installation
--------------------------------

Edit ``/etc/mcprack/env`` and restart the service:

.. code-block:: bash

   sudo systemctl restart mcprack

At least set ``PUBLIC_BASE_URL``. The settings are listed in
:doc:`reference/configuration`. The installer never overwrites an existing
``/etc/mcprack/env``.

Database
--------

The package asks ``dbconfig-common`` which engine to use: SQLite (the default, in
``/var/lib/mcprack``), PostgreSQL or MySQL/MariaDB (install ``python3-psycopg2`` or
``python3-pymysql``). The choice ends up in ``SQLALCHEMY_DATABASE_URI`` in
``/etc/mcprack/env``. Migrations run on upgrade; to run them by hand:

.. code-block:: bash

   sudo mcprack db upgrade

Upgrading from 1.6.x
--------------------

Back up the database first. The upgrade applies these migrations: per-user token
and session versions, ``materialize_server_permissions``, ``add_login_throttle``
and ``add_user_mfa``. They are reversible (``mcprack db downgrade``).

What changes for existing installations:

- **Server access is now explicit.** ``STRICT_SERVER_PERMISSIONS`` is ``true`` by
  default. The migration grants every existing user the servers that are enabled
  at that moment, so nobody loses access; new servers and new users need a grant.
- **Administrators are asked for two-factor authentication** the first time they
  open the admin area (:doc:`security/two-factor`). Set
  ``MFA_REQUIRED_FOR_ADMINS=false`` to postpone it on a trusted network.
- **Passwords** set from now on need 12 characters. Existing passwords still work.
- **A weak or placeholder ``SECRET_KEY`` refuses to start.** Rotate with
  ``SECRET_KEY_FALLBACKS`` (:doc:`howto/rotate-secret-key`).
- **Admin API tokens created before the upgrade are not asked for a code.** Review
  and rotate them.
- **Old ``/proxy/mcp/<token>/<id>`` URLs keep working** until they expire or you run
  ``mcprack user revoke-tokens``; users should download a new configuration.
