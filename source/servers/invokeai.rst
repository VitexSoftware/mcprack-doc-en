mcp-server-invokeai
===================

An MCP server for **InvokeAI** image generation: text-to-image, image-to-image and upscaling against a local InvokeAI instance. Companion package: ``mcprack-mcp-server-invokeai``. Binary: ``/usr/bin/mcp-server-invokeai``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-invokeai

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``INVOKEAI_BASE_URL``
     - no
     - InvokeAI REST API (default ``http://127.0.0.1:9090``)
   * - ``INVOKEAI_READ_ONLY``
     - no
     - ``true`` registers only the read-only tools
   * - ``INVOKEAI_UPLOAD_ROOT``
     - no
     - ``:``-separated directories from which ``img2img`` and ``upscale_image`` may read local files (default ``$HOME`` and the temp directory)

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-invokeai
   sudo mcprack server edit mcp-server-invokeai --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-invokeai <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: ``INVOKEAI_READ_ONLY=true`` hides all image-creating tools.

Tools
-----

- Read-only: ``list_models``, ``get_queue_status``.
- Creating (not idempotent): ``generate_image``, ``img2img``, ``upscale_image``.
