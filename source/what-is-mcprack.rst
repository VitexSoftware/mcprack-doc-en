What is mcprack?
================

The problem
-----------

Giving an AI client access to an MCP server normally means installing the server
on every workstation, putting its credentials into a JSON file and keeping both up
to date. That scales badly and leaks secrets into files that get copied, committed
and backed up.

How mcprack solves it
---------------------

.. code-block:: text

   AI client (Claude, Cursor, VS Code ...)
           │   HTTPS, one URL per server
           ▼
   mcprack  /proxy/mcp/...        ← identifies the user, checks permissions
           │
           ├─ server has a command → per-user fastmcp process (loopback)
           └─ server has a URL     → relay to that backend
                                     (credentials injected on the server)

1. An administrator **registers** MCP servers (a local command, or a network URL)
   and stores their credentials once.
2. A user **selects** the servers they are allowed to use and **downloads or
   syncs** the generated configuration.
3. The client sends every request to mcprack, which authenticates the caller,
   starts or reaches the backend and forwards the request.

Who uses what
-------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Role
     - Typical tasks
   * - Administrator
     - Register servers, store credentials, grant access, apply templates, read
       the audit trail, run ``mcprack`` CLI commands
   * - User
     - Choose servers, set personal credential overrides, create API tokens,
       download or sync the client configuration
   * - Operator
     - Install the package, configure ``/etc/mcprack/env``, put a reverse proxy in
       front, monitor the service

What mcprack is not
-------------------

- It does not implement MCP servers; it hosts and relays them. Servers that ship
  a mcprack *companion package* register themselves — see :doc:`servers/index`.
- It is not an identity provider. It authenticates against local accounts or LDAP
  / Active Directory, and issues OAuth tokens only for MCP clients.
