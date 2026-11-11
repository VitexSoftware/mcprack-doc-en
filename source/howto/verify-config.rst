Verifying a configuration
=========================

.. code-block:: bash

   sudo mcprack user config verify USERNAME [CLIENT]

``CLIENT`` defaults to ``claude-code``. For every server in the user's generated
configuration the command does what an MCP client will do:

1. ``initialize`` (asking for protocol 2025-06-18),
2. ``notifications/initialized``,
3. ``tools/list``.

and prints one line per server:

.. code-block:: text

   OK    zabbix: 12 tool(s), protocol 2025-06-18, 1.4s
   FAIL  netbox: initialize: HTTP 502 ...
   2 server(s) verified.

The exit status is 0 only if every server answered with tools. The probe goes
through the same path as a real client — the reverse proxy and TLS, authentication,
the relay and the MCP server behind it — so a green result is meaningful.

Options
-------

``--base-url URL``
   Probe another origin with the same paths, for example ``http://127.0.0.1:8912``
   to test mcprack itself without the reverse proxy and find which hop breaks.

``--server NAME``
   Check only this server (repeatable).

``--timeout SECONDS``
   Per-server limit; a cold start takes a while. Default 60.

``--insecure``
   Allow sending the credential over plain ``http`` to a non-loopback host.

Credentials during the check
----------------------------

For the ``claude-code`` format the command creates a token with the scope
``proxy:access`` valid for 15 minutes, uses it, and removes it (also when the
check fails). The creation is audited. The other formats carry the credential in
the URL, so no token is created.

The credential — the Authorization header or the path token in the URL — is only
sent over ``https`` or to loopback; redirects are never followed with it.

The stand-alone probe
---------------------

``mcprack-mcp-probe`` checks any MCP HTTP endpoint when you only have a URL:

.. code-block:: bash

   mcprack-mcp-probe https://mcprack.example.com/proxy/mcp/<token>/7
   MCPRACK_TOKEN=... mcprack-mcp-probe --bearer --tools https://mcprack.example.com/proxy/mcp/7
   mcprack-mcp-probe --call list_dir --args '{"path": "."}' URL

``--bearer`` reads the token from ``MCPRACK_TOKEN`` (never from the command line).
