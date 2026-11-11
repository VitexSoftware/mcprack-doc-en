mcp-server-datovka
==================

An MCP server for the Czech **ISDS** data box system ("datové schránky"), built on
FastMCP and ``python3-datovka``. Companion package:
``mcprack-mcp-server-datovka``. Binary: ``/usr/bin/mcp-server-datovka``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-datovka

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Variable
     - Default
     - Meaning
   * - ``DATOVKA_USERNAME``
     - *required*
     - ISDS login name
   * - ``DATOVKA_PASSWORD``
     - *required*
     - ISDS password (keep it in the secret store)
   * - ``DATOVKA_URL``
     - production endpoint
     - Use the testing sandbox (``https://ws1.czebox.cz/``) while you try it out
   * - ``DATOVKA_SAVE_DIR``
     - ``~/datovka-attachments``
     - Where ``save_attachments`` writes files
   * - ``READ_ONLY``
     - ``true``
     - ``send_message``, ``send_text_message`` and ``mark_message_read`` refuse while
       it is true

Register the plain values and keep the password in the secret store:

.. code-block:: bash

   sudo mcprack server edit mcp-server-datovka \
       --set-env DATOVKA_URL=https://ws1.czebox.cz/ \
       --add-secret-key DATOVKA_USERNAME --add-secret-key DATOVKA_PASSWORD \
       --allow-user-override
   sudo mcprack secret set mcp-server-datovka DATOVKA_USERNAME
   sudo mcprack secret set mcp-server-datovka DATOVKA_PASSWORD

Data boxes carry legally binding messages. Allow sending only for people who are
entitled to send on behalf of the box, ideally through a per-user override of
``DATOVKA_USERNAME`` and ``DATOVKA_PASSWORD``.

Tools
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Tool
     - Purpose
   * - ``list_received_messages``, ``list_sent_messages``
     - Summaries, most recent first (without a date range ISDS returns about 90 days)
   * - ``get_message``, ``get_sent_message``
     - A full message; attachment bytes only on request (base64)
   * - ``save_attachments``
     - Save documents as files under ``DATOVKA_SAVE_DIR`` (never overwrites), so large
       files do not pass through the conversation
   * - ``find_data_box``
     - Find a recipient's box id by name, trade name or IČO (offline directory first)
   * - ``send_message``, ``send_text_message``
     - Send a message / compose plain text as a PDF and send it (**write**)
   * - ``mark_message_read``
     - Mark as read (**write**)
   * - ``ping``
     - Check that the session is alive
