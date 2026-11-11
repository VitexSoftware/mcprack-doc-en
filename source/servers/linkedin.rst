mcp-server-linkedin
===================

An MCP server that reads **LinkedIn** through your own browser session (upstream: ``stickerdaniel/linkedin-mcp-server``): profiles, companies, jobs, inbox and connection requests. Companion package: ``mcprack-mcp-server-linkedin``. Binary: ``/usr/bin/mcp-server-linkedin``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-linkedin

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 34 10 56

   * - Variable
     - Required
     - Meaning
   * - ``(browser profile)``
     - yes
     - Log in once with ``mcp-server-linkedin --login``; the session is stored in the server's browser profile

Registration:

.. code-block:: bash

   sudo mcprack server show mcp-server-linkedin
   sudo mcprack server edit mcp-server-linkedin --add-secret-key <SECRET_VARIABLE>
   sudo mcprack secret set mcp-server-linkedin <SECRET_VARIABLE>

Replace ``<SECRET_VARIABLE>`` with each secret variable from the table.

Read-only behaviour: The upstream server has no read-only switch. Tools such as ``send_message`` and ``connect_with_person`` act on your account.

Tools
-----

- Profiles and companies: ``get_person_profile``, ``get_my_profile``, ``get_company_profile``, ``get_company_posts``, ``get_company_employees``, ``search_companies``.
- Jobs: ``search_jobs``, ``get_saved_jobs``.
- Messaging (acts on your account): ``get_inbox``, ``get_conversation``, ``search_conversations``, ``send_message``, ``connect_with_person``.

.. warning::

   Scraping may breach LinkedIn's terms and can get an account restricted. The project is not affiliated with LinkedIn.
