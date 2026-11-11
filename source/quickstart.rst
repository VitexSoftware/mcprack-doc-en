Quickstart
==========

This page takes a fresh Debian or Ubuntu host to a working instance with one MCP
server and one connected client.

1. Install
----------

.. code-block:: bash

   sudo apt install mcprack mcp-server-filesystem mcprack-mcp-server-filesystem

The package creates the ``mcprack`` system user, generates a ``SECRET_KEY`` in
``/etc/mcprack/env``, creates an initial administrator ``admin`` and writes its
password to ``/etc/mcprack/admin-credentials`` (readable by root only). The
companion package ``mcprack-mcp-server-filesystem`` registers the filesystem
server in the catalog (see :doc:`servers/companion-packages`).

2. Open the portal
------------------

mcprack listens on ``127.0.0.1:8912`` only. Put a TLS reverse proxy in front of
it (see :doc:`security/internet-checklist` for a ready Apache vhost) and set the
public address:

.. code-block:: bash

   sudoedit /etc/mcprack/env
   #   PUBLIC_BASE_URL=https://mcprack.example.com
   sudo systemctl restart mcprack

Sign in as ``admin``. Administrators must set up two-factor authentication
before they can use the admin area (:doc:`security/two-factor`).

3. Pick a server and connect Claude Code
----------------------------------------

1. In the catalog, tick *Filesystem MCP Server* and save.
2. Create an API token with the scope ``proxy:access`` (user menu → API tokens).
3. On your workstation:

.. code-block:: bash

   export MCPRACK_TOKEN=mcr_...
   claude mcp add --transport http --scope user filesystem \
       https://mcprack.example.com/proxy/mcp/1 \
       --header "Authorization: Bearer $MCPRACK_TOKEN"

The exact commands for your servers are shown on the *View & Copy* page of the
``claude-code`` client. See :doc:`howto/connect-claude-code`.

4. Check it
-----------

.. code-block:: bash

   sudo mcprack user config verify alice claude-code

The command does what the client will do (``initialize`` then ``tools/list``) for
every URL in the configuration and prints one line per server.

Next steps
----------

- :doc:`howto/register-server` — add your own servers
- :doc:`howto/grant-access` — control who sees what
- :doc:`security/overview` — what to configure before exposing mcprack
