mcp-server-filesystem
=====================

An MCP server exposing Linux **filesystem** operations, built on FastMCP. Companion
package: ``mcprack-mcp-server-filesystem``. Binary:
``/usr/bin/mcp-server-filesystem``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-filesystem

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Variable
     - Meaning
   * - ``FS_ROOT``
     - Directory every path is confined to (default: the working directory at
       start-up). Paths are resolved against it and rejected if they escape it.
   * - ``FS_READONLY``
     - ``true`` by default; ``false`` allows the mutating tools. Empty or unset is
       read-only.

Tools
-----

- Read-only: ``list_dir``, ``read_file``, ``stat``, ``exists``, ``glob_search``.
- Mutating (need ``FS_READONLY=false``): ``write_file``, ``mkdir``, ``delete``,
  ``move``, ``copy``.

.. warning::

   Under mcprack the server runs as the ``mcprack`` service user **on the mcprack
   host**, so ``FS_ROOT`` is a directory of that host and the files are readable by
   that user. Point ``FS_ROOT`` at a dedicated directory, never at ``/``, and keep
   ``FS_READONLY=true`` unless users really need to write.

Registering with a root directory
---------------------------------

.. code-block:: bash

   sudo mcprack server edit mcp-server-filesystem --set-env FS_ROOT=/srv/shared
   sudo mcprack server test mcp-server-filesystem
