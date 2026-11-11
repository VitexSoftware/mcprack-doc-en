mcp-server-email
================

An MCP server for **reading, searching, organizing and sending email** over IMAP and SMTP (upstream: ``Wh1isper/mcp-email-server``). Companion package: ``mcprack-mcp-server-email``. Binary: ``/usr/bin/mcp-server-email``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-email

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``MCP_EMAIL_SERVER_EMAIL_ADDRESS``
     - yes
     - Mailbox address
   * - ``MCP_EMAIL_SERVER_PASSWORD``
     - yes
     - Password or app password (secret store)
   * - ``MCP_EMAIL_SERVER_IMAP_HOST``
     - yes
     - IMAP host
   * - ``MCP_EMAIL_SERVER_IMAP_PORT``
     - no
     - IMAP port
   * - ``MCP_EMAIL_SERVER_SMTP_HOST``
     - no
     - SMTP host
   * - ``MCP_EMAIL_SERVER_SMTP_PORT``
     - no
     - SMTP port
   * - ``MCP_EMAIL_SERVER_IMAP_SSL / _SMTP_SSL``
     - no
     - Use implicit TLS
   * - ``MCP_EMAIL_SERVER_USER_NAME, _FULL_NAME``
     - no
     - Login and display name
   * - ``MCP_EMAIL_SERVER_IMAP_PASSWORD, _SMTP_PASSWORD``
     - no
     - Separate IMAP/SMTP passwords (secret store)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-email
   sudo mcprack server edit mcp-server-email --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-email <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: See the upstream README and ``/usr/share/mcp-server-email/server.json`` for the full variable list and read-only options.

Tools
-----

- Listing, reading, searching and organizing messages, and sending mail. The package ships its own ``server.json`` with every variable.

.. warning::

   Sending mail is irreversible. Prefer a mailbox the assistant may use, not your personal one.
