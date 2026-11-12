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

mcprack listens on ``127.0.0.1:8912`` only (to change that, see
:doc:`howto/change-listen-address`). Put a TLS reverse proxy in front of
it (see :doc:`security/internet-checklist` for a ready Apache vhost) and set the
public address:

.. code-block:: bash

   sudoedit /etc/mcprack/env
   #   PUBLIC_BASE_URL=https://mcprack.example.com
   sudo systemctl restart mcprack

Sign in as ``admin``. Administrators must set up two-factor authentication
before they can use the admin area (:doc:`security/two-factor`).

3. Subscribe to a server and connect Claude Code
------------------------------------------------

1. Open *MCP servers*, subscribe to *Filesystem MCP Server*, and save. If the
   administrator has not allowed access, open its card and request access.
2. Return to the overview. It shows the aggregate URL and the servers available
   through it.
3. Create an API token with the scope ``proxy:access`` (user menu → API tokens).
4. On your workstation:

.. code-block:: bash

   export MCPRACK_TOKEN=mcr_...
      claude mcp add --transport http --scope user mcprack \
         https://mcprack.example.com/proxy/mcp/aggregate \
       --header "Authorization: Bearer $MCPRACK_TOKEN"

The exact commands for your servers are shown on the *View & Copy* page of the
``claude-code`` client. See :doc:`howto/connect-claude-code`.

4. Check it
-----------

.. code-block:: bash

   sudo mcprack user config verify alice claude-code

The command does what the client will do (``initialize`` then ``tools/list``)
against the aggregate endpoint. Use ``--server filesystem`` to probe one
subscribed server through its individual relay.

Next steps
----------

- :doc:`howto/register-server` — add your own servers
- :doc:`howto/grant-access` — control who sees what
- :doc:`security/overview` — what to configure before exposing mcprack
