mcp-server-semaphore
====================

An MCP server for **Semaphore UI**, the web interface for Ansible. Companion
package: ``mcprack-mcp-server-semaphore``. Binary:
``/usr/bin/mcp-server-semaphore`` (``semaphore-mcp`` is an alias). The upstream
source directory is ``semaphore-mcp-server``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-semaphore

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Variable
     - Default
     - Meaning
   * - ``SEMAPHORE_URL``
     - 
     - Base URL of the Semaphore UI instance
   * - ``SEMAPHORE_TOKEN``
     - 
     - API Bearer token (create it in the Semaphore UI)
   * - ``READ_ONLY``
     - ``true``
     - ``false`` enables write operations (creating, launching, stopping, deleting)
   * - ``DEBUG``
     - unset
     - ``true`` for verbose logging

Registration:

.. code-block:: bash

   sudo mcprack server edit mcp-server-semaphore \
       --set-env SEMAPHORE_URL=https://semaphore.example.com \
       --add-secret-key SEMAPHORE_TOKEN --allow-user-override
   sudo mcprack secret set mcp-server-semaphore SEMAPHORE_TOKEN

Launching a task runs an Ansible playbook, so it can change real systems. Keep the
server read-only for most users, and give Semaphore a token whose project rights
match what the person may do.

Tools
-----

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Group
     - Examples
   * - Projects
     - ``project_list/get/create/delete``
   * - Tasks
     - ``task_list/get/launch/stop/delete``, ``task_output``
   * - Templates
     - ``template_list/get/create/delete``
   * - Inventories, repositories, environments, keys
     - ``inventory_*``, ``repository_*``, ``environment_*``, ``key_*``
   * - Schedules and events
     - ``schedule_create/delete/list``, ``event_list``
   * - Server and user
     - ``server_info``, ``server_ping``, ``user_get_current``, ``user_tokens``
