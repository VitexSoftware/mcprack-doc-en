mcp-server-librenms
===================

An MCP server for **LibreNMS** network monitoring (113 tools): devices, ports, alerts,
inventory, locations, services, logs, graphs, billing, pollers and Oxidized configs. It
is a fork of `mhajder/librenms-mcp <https://github.com/mhajder/librenms-mcp>`_ 1.13.0.
Companion package: ``mcprack-mcp-server-librenms``. Binary:
``/usr/bin/mcp-server-librenms`` (``librenms-mcp`` is a compatibility symlink).

.. code-block:: bash

   sudo apt install mcprack-mcp-server-librenms

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 60

   * - Variable
     - Required
     - Meaning
   * - ``LIBRENMS_URL``
     - yes
     - LibreNMS base URL, e.g. ``https://librenms.example.com``
   * - ``LIBRENMS_TOKEN``
     - yes
     - LibreNMS API token (secret store)
   * - ``READ_ONLY_MODE``
     - no
     - The companion sets ``true``; only the 76 read-only tools are registered. Set ``false`` to enable the rest
   * - ``LIBRENMS_VERIFY_SSL``, ``LIBRENMS_TIMEOUT``
     - no
     - Verify the TLS certificate (``true``) and the request timeout
   * - ``DISABLED_TAGS``
     - no
     - Comma-separated tool tags to hide

Registration:

.. code-block:: bash

   sudo mcprack server edit mcp-server-librenms \
       --set-env LIBRENMS_URL=https://librenms.example.com \
       --add-secret-key LIBRENMS_TOKEN
   sudo mcprack secret set mcp-server-librenms LIBRENMS_TOKEN

Tools
-----

Read-only tools (for example ``alerts_get``, ``alert_get_by_id``, device, port,
inventory, log and graph queries) are always available. Mutating tools (creating,
updating and deleting devices, alert rules, groups, services and so on) need
``READ_ONLY_MODE=false``; ``tests/test_standards.py`` in the server repository enforces
that every tool carries a title and explicit read-only, destructive, idempotent and
open-world hints.

.. warning::

   Deleting devices or removing ports from groups is not reversible from the
   assistant. Keep ``READ_ONLY_MODE=true`` unless a user needs writes, and use a
   LibreNMS token with the narrowest role that works.
