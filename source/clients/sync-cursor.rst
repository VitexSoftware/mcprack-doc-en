mcprack-sync-cursor
===================

Keeps the **Cursor** IDE's ``mcp.json`` in sync with mcprack. Built on
:doc:`mcprack-client`; the key of the servers map is ``mcpServers``.

.. code-block:: bash

   sudo apt install mcprack-sync-cursor
   mcprack-sync-cursor configure --url https://mcprack.example.com --token-file ~/.config/mcprack/token
   mcprack-sync-cursor sync
   mcprack-sync-cursor sync --dry-run
   mcprack-sync-cursor status

The target file is the first that exists of ``~/.config/Cursor/User/mcp.json`` and
``~/.cursor/mcp.json`` (Linux; the macOS and Windows equivalents are used there);
otherwise the first is created. Override it with ``--config PATH``.

Automatic updates:

.. code-block:: bash

   systemctl --user enable --now mcprack-sync-cursor.timer

The settings file is shared with the other sync tools. The commands ``configure``,
``sync`` and ``status`` and the safety rules are described in :doc:`mcprack-client`.
