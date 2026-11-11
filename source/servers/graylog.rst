mcp-server-graylog
==================

An MCP server for **Graylog** log management. It runs in one of two modes: ``bridge``
forwards to the experimental built-in MCP endpoint (``/api/mcp``) of Graylog 7.1+,
``api`` serves a fixed set of read-only REST tools. Companion package:
``mcprack-mcp-server-graylog``. Binary: ``/usr/bin/mcp-server-graylog``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-graylog

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 60

   * - Variable
     - Required
     - Meaning
   * - ``GRAYLOG_MODE``
     - no
     - ``bridge`` (default) or ``api``
   * - ``GRAYLOG_URL``
     - no
     - Graylog base URL (default ``http://127.0.0.1:9000``; a trailing ``/api`` is stripped)
   * - ``GRAYLOG_API_TOKEN``
     - yes
     - Graylog API token (secret store); ``GRAYLOG_TOKEN`` is accepted as an alias
   * - ``GRAYLOG_READ_ONLY``
     - no
     - ``true`` by default; in bridge mode hides tools that are not read-only (API mode is always read-only)
   * - ``GRAYLOG_TIMEOUT``, ``GRAYLOG_MAX_CHARS``
     - no
     - Seconds per request (30) and output truncation limit (100000)
   * - ``GRAYLOG_VERIFY_TLS``
     - no
     - ``true`` by default; verify the Graylog certificate

Registration:

.. code-block:: bash

   sudo mcprack server edit mcp-server-graylog \
       --set-env GRAYLOG_URL=https://graylog.example.com \
       --set-env GRAYLOG_MODE=api \
       --add-secret-key GRAYLOG_API_TOKEN
   sudo mcprack secret set mcp-server-graylog GRAYLOG_API_TOKEN

Tools
-----

- API mode (all read-only): ``server_info``, ``stream_list``, ``stream_get``,
  ``search_messages``, ``field_list``.
- Bridge mode: the tools Graylog itself publishes. Mutating ones stay hidden until
  ``GRAYLOG_READ_ONLY=false``.

.. note::

   Prefer ``GRAYLOG_MODE=api`` unless the built-in MCP endpoint is enabled on your
   Graylog. Give searches a Lucene query and a short time window.
