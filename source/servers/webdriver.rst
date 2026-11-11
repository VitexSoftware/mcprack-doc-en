mcp-server-webdriver
====================

An MCP server giving an AI agent direct access to a **Firefox** browser through
Selenium WebDriver: browser control, plus DevTools information (JavaScript errors,
console output, failed network resources, computed CSS) captured over WebDriver
BiDi. Companion package: ``mcprack-mcp-server-webdriver``. Binary:
``/usr/bin/mcp-server-webdriver``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-webdriver

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Variable
     - Default
     - Meaning
   * - ``WEBDRIVER_READONLY``
     - ``true``
     - ``false`` allows page-mutating tools (click, fill, upload, select,
       ``execute_js``, key presses, dialogs, cookies, storage)
   * - ``GECKODRIVER_PATH``
     - unset
     - Absolute path to ``geckodriver`` (highest priority)
   * - ``GECKODRIVER_AUTO_INSTALL``
     - ``true``
     - ``false`` disables the webdriver-manager fallback
   * - ``FIREFOX_BINARY``
     - unset
     - A custom Firefox executable
   * - ``FIREFOX_PROFILE``, ``FIREFOX_PROFILE_DIR``
     - unset
     - A named profile, or a profile directory

Tools
-----

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Group
     - Tools
   * - Session
     - ``browser_open``, ``browser_close``, ``browser_status``
   * - Navigation
     - ``browser_navigate``, ``browser_back``, ``browser_forward``,
       ``browser_refresh``, ``browser_screenshot``
   * - Inspection
     - ``browser_get_title/url/source/text/attribute``, ``browser_find_elements``,
       ``browser_get_cookies``, ``browser_get_storage``
   * - Interaction (need ``WEBDRIVER_READONLY=false``)
     - ``browser_click``, ``browser_fill``, ``browser_select``, ``browser_execute_js``,
       ``browser_press_key``, ``browser_upload_file``, dialogs, cookies, storage
   * - DevTools
     - ``devtools_report``, ``devtools_js_errors``, ``devtools_console``,
       ``devtools_network_failed``, ``devtools_network_all``, ``devtools_computed_css``,
       ``devtools_element_info``, ``devtools_css_variables``, ``devtools_performance``

.. warning::

   The browser runs on the mcprack host as the service user. Page-mutating tools
   and ``browser_execute_js`` act with that browser's cookies and network position
   (including your internal network). Keep it read-only unless you need it, and
   combine it with the egress filter described in :doc:`../security/policies`.
   Firefox and ``geckodriver`` must be installed on the host.
