Connecting other clients
========================

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Client
     - Format name
     - Where the file goes
   * - Claude Desktop
     - ``claude``
     - Linux ``~/.config/Claude/claude_desktop_config.json``
   * - Claude Code
     - ``claude-code``
     - ``.mcp.json`` in a project, or ``claude mcp add`` (:doc:`connect-claude-code`)
   * - Cursor
     - ``cursor``
     - Linux ``~/.config/Cursor/User/mcp.json`` (or ``~/.cursor/mcp.json`` if that exists)
   * - VS Code / GitHub Copilot
     - ``vscode`` (alias ``copilot``)
     - Linux ``~/.config/Code/User/mcp.json`` (the user profile)

Download
--------

From the catalog use *Download Config* or *View & Copy*, or:

.. code-block:: bash

   curl -H "Authorization: Bearer $TOKEN" \
        https://mcprack.example.com/api/v1/me/config/cursor
   sudo mcprack user config download alice vscode --out mcp.json

``user config download`` creates the file with mode ``0600``.

.. warning::

   The ``claude``, ``cursor``, ``copilot`` and ``vscode`` formats carry the signed
   path token inside every URL. The file is a credential: do not commit it.

Keep it in sync
---------------

Instead of downloading by hand, run a sync tool: :doc:`../clients/sync-claude`,
:doc:`../clients/sync-cursor`, :doc:`../clients/sync-vscode`.

Claude Desktop remote servers
-----------------------------

Whether Claude Desktop accepts a remote ``url`` entry in
``claude_desktop_config.json`` depends on its version; on versions that do not,
add the server in the application's connector dialog using the name and URL shown
in the catalog (each selected server has a copy button).
