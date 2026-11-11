Client configuration formats
============================

``GET /api/v1/me/config/{client}``, ``/download/{client}`` and ``/view/{client}``
render the same selection in the format of each client.

.. list-table::
   :header-rows: 1
   :widths: 16 20 24 40

   * - Format
     - File
     - Top-level key
     - Credential
   * - ``claude``
     - ``claude_desktop_config.json``
     - ``mcpServers``
     - Signed token in the URL path
   * - ``claude-code``
     - ``.mcp.json``
     - ``mcpServers``
     - ``Authorization: Bearer ${MCPRACK_TOKEN}`` (none with OAuth)
   * - ``cursor``
     - ``mcp.json``
     - ``mcpServers``
     - Signed token in the URL path
   * - ``vscode``, ``copilot``
     - ``mcp.json``
     - ``servers``
     - Signed token in the URL path

An entry for a network server looks like:

.. code-block:: json

   { "type": "http", "url": "https://mcprack.example.com/proxy/mcp/<token>/8" }

mcprack always renders a server as a network entry with its relay URL, whatever the
backend's real transport is: clients never receive a command to run. (A local
``stdio`` entry with ``command`` and ``args`` appears only as a defensive fallback
for a server that has neither a relay URL nor a ``PUBLIC_BASE_URL`` to build it
from; the sync tools refuse such entries.)

.. warning::

   Files in the path-token formats contain a credential. Do not commit them. For a
   file you can commit, use ``claude-code``.
