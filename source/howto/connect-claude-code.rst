Connecting Claude Code
======================

Claude Code reads MCP servers from three scopes: ``local`` (the default of
``claude mcp add``, stored for the current project), ``project`` (a ``.mcp.json`` in
the repository) and ``user`` (all your projects). mcprack generates a dedicated
format for it, ``claude-code``, that contains **no secret**.

The generated file
------------------

.. code-block:: json

   {
     "mcpServers": {
          "mcprack": {
         "type": "http",
             "url": "https://mcprack.example.com/proxy/mcp/aggregate",
         "headers": { "Authorization": "Bearer ${MCPRACK_TOKEN}" }
       }
     }
   }

The URL is the plain relay route; the credential is read by Claude Code from the
``MCPRACK_TOKEN`` environment variable (``${VAR}`` is expanded in ``url`` and
``headers``). So the file can be committed as ``.mcp.json``. The variable has our
own name on purpose: Claude Code reads credential-looking variables such as
``ANTHROPIC_API_KEY`` or ``NPM_TOKEN`` as empty inside the headers of a remote
server.

Step by step
------------

1. **Create a token** with the scope ``proxy:access`` (user menu → API tokens, or
   ``POST /api/v1/tokens``). It expires after 90 days unless you choose otherwise.
2. **Export it** where Claude Code starts — a shell profile, direnv, a secret
   manager; not the repository:

   .. code-block:: bash

      export MCPRACK_TOKEN=mcr_...

3. **Add the aggregate server**, either by saving the download as ``.mcp.json``
   (project scope; Claude Code asks each person to approve a project server once),
   or with the command from the *View & Copy* page:

   .. code-block:: bash

        claude mcp add --transport http --scope user mcprack \
           https://mcprack.example.com/proxy/mcp/aggregate \
          --header "Authorization: Bearer $MCPRACK_TOKEN"

   4. In Claude Code run ``/mcp`` to see the aggregate connection. Its tools,
      resources and prompts are namespaced by MCP server name.

With OAuth enabled
------------------

When ``OAUTH_ENABLED=true`` the generated file has **no** ``headers``: Claude Code
runs the sign-in itself (``/mcp`` → authenticate, or ``claude mcp login``). Ask for
the header anyway with ``?auth=token``. See :doc:`enable-oauth`.

Verify before users try it
--------------------------

.. code-block:: bash

   sudo mcprack user config verify alice claude-code

See :doc:`verify-config`.

If a server shows ``failed``
----------------------------

.. code-block:: bash

   MCPRACK_TOKEN=mcr_... mcprack-mcp-probe --bearer --tools \
       https://mcprack.example.com/proxy/mcp/8

The probe shows at which step the connection breaks. Common causes are in
:doc:`../reference/troubleshooting`.
