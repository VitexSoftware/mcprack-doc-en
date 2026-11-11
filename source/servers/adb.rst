mcp-server-adb
==============

An MCP server that controls an **Android phone over ADB**: calls, text messages, contacts, apps, screen interaction and media. Based on the ``phone-mcp`` plugin. Companion package: ``mcprack-mcp-server-adb``. Binary: ``/usr/bin/mcp-server-adb``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-adb

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``(none)``
     - no
     - No variables; the server talks to the first device that ``adb`` sees

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-adb
   sudo mcprack server edit mcp-server-adb --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-adb <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Tools
-----

- Calls and messages: ``call_number``, ``end_call``, ``receive_incoming_call``, ``send_text_message``, ``receive_text_messages``, ``get_sent_messages``.
- Contacts: ``get_contacts``, ``create_contact``.
- Apps and screen: ``list_installed_apps``, ``launch_app_activity``, ``terminate_app``, ``get_current_window``, ``analyze_screen``, ``interact_with_screen``, ``open_url``, ``play_media``, ``set_alarm``, ``start_screen_recording``.

.. warning::

   This server has no read-only switch. Calling, texting and screen interaction act on the real phone; connect only a device you are willing to let the assistant control, and enable USB debugging only for that device.
