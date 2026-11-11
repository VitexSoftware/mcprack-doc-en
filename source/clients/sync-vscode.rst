mcprack-sync-vscode
===================

Keeps the **VS Code / GitHub Copilot** ``mcp.json`` in sync with mcprack. Built on
:doc:`mcprack-client`. VS Code names the servers map ``servers`` (not
``mcpServers``), and the tool requests the ``vscode`` format from mcprack.

.. code-block:: bash

   sudo apt install mcprack-sync-vscode
   mcprack-sync-vscode configure --url https://mcprack.example.com --token-file ~/.config/mcprack/token
   mcprack-sync-vscode sync
   mcprack-sync-vscode status

The target is the first existing of ``~/.config/Code/User/mcp.json`` and the
``Code - Insiders`` equivalent (Linux), otherwise the stable VS Code user path.
Override with ``--config PATH``.

.. code-block:: bash

   systemctl --user enable --now mcprack-sync-vscode.timer

See :doc:`mcprack-client` for the settings file, the validation of what the server
sends and the exit status.
