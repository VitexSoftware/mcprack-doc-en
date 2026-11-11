mcprack-sync-claude
===================

Keeps the MCP configuration of **Claude Desktop** — and optionally **Claude Code** —
up to date from a mcprack catalog. Built on :doc:`mcprack-client`.

Install and set up
------------------

.. code-block:: bash

   sudo apt install mcprack-sync-claude
   mcprack-sync-claude configure --url https://mcprack.example.com --token-file ~/.config/mcprack/token

Sync
----

.. code-block:: bash

   mcprack-sync-claude sync                 # Claude Desktop
   mcprack-sync-claude sync --dry-run       # show what would change
   mcprack-sync-claude sync --claude-code   # merge into ~/.claude.json instead
   mcprack-sync-claude status

Default target on Linux: ``~/.config/Claude/claude_desktop_config.json``. Only the
``mcpServers`` key is updated; other keys and servers you added yourself are kept.
The managed server names are remembered in
``~/.local/state/mcprack-sync/<tool>.managed.json``.

.. note::

   ``--claude-code`` writes into ``~/.claude.json``, a file Claude Code itself
   rewrites. The tool detects a concurrent save and merges again, but for a
   project it is usually cleaner to use the secret-free ``.mcp.json`` described in
   :doc:`../howto/connect-claude-code`.

Automatic updates
-----------------

.. code-block:: bash

   systemctl --user enable --now mcprack-sync-claude.timer

The timer runs two minutes after boot and then hourly.
