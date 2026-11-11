mcp-server-cc-token-saver
=========================

An MCP server that **delegates simple tasks to a local LLM** (any OpenAI-compatible endpoint, for example Ollama or LM Studio) so that a cloud assistant spends fewer tokens. Companion package: ``mcprack-mcp-server-cc-token-saver``. Binary: ``/usr/bin/mcp-server-cc-token-saver``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-cc-token-saver

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``OPENAI_BASE_URL``
     - no
     - OpenAI-compatible API base URL (default ``http://localhost:1234/v1``)
   * - ``OPENAI_API_KEY``
     - no
     - Key sent to the endpoint (default ``none``; usually ignored; secret store)
   * - ``LOCAL_MODEL_NAME``
     - no
     - Model to request (default ``qwen2.5-7b-instruct``)
   * - ``LOCAL_LLM_TEMPERATURE``
     - no
     - Sampling temperature (default ``0.7``)
   * - ``LOCAL_LLM_MAX_TOKENS``
     - no
     - Maximum tokens per response (default ``-1``, no limit)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-cc-token-saver
   sudo mcprack server edit mcp-server-cc-token-saver --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-cc-token-saver <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: All tools only query the local model; none changes external state.

Tools
-----

- ``query_local_llm``, ``query_local_llm_with_context``, ``list_available_models``, ``switch_model``, ``summarize_text``, ``generate_commit_message``, ``generate_unit_tests``, ``explain_code``, ``translate_text``.
