mcp-server-subreg
=================

An MCP server for the **Subreg.cz** domain registrar, exposing its SOAP API; built
on FastMCP and ``python3-subreg-client``. Companion package:
``mcprack-mcp-server-subreg``. Binary: ``/usr/bin/mcp-server-subreg``.

.. code-block:: bash

   sudo apt install mcprack-mcp-server-subreg

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 60

   * - Variable
     - Required
     - Meaning
   * - ``SUBREG_LOCATION``
     - yes
     - SOAP endpoint, e.g. ``https://soap.subreg.cz/cmd.php``
   * - ``SUBREG_URI``
     - yes
     - SOAP namespace URI, e.g. ``https://soap.subreg.cz/soap``
   * - ``SUBREG_LOGIN``
     - yes
     - Subreg account login
   * - ``SUBREG_PASSWORD``
     - yes
     - Subreg account password (secret store)
   * - ``SUBREG_READONLY``
     - no
     - ``true`` by default; ``false`` allows domain, DNS, contact and billing writes

Registration:

.. code-block:: bash

   sudo mcprack server edit mcp-server-subreg \
       --set-env SUBREG_LOCATION=https://soap.subreg.cz/cmd.php \
       --set-env SUBREG_URI=https://soap.subreg.cz/soap \
       --set-env SUBREG_LOGIN=myaccount \
       --add-secret-key SUBREG_PASSWORD
   sudo mcprack secret set mcp-server-subreg SUBREG_PASSWORD

Tools
-----

- Read-only: ``check_domain``, ``info_domain``, ``domains_list``, ``pricelist``,
  ``get_pricelist``, ``get_credit``, ``users_list``, ``info_user``, ``get_dns_zone``,
  ``info_contact``, ``contacts_list``, ``info_order``, ``get_tld_info``.
- Mutating (need ``SUBREG_READONLY=false``): ``register_domain``, ``renew_domain``,
  ``delete_domain``, ``add_dns_record``, ``delete_dns_record``, ``create_contact``,
  ``update_contact``, ``credit_correction``.

.. warning::

   Registering, renewing and deleting domains spends credit and affects production
   names. Never enable writes for an assistant that you would not trust with the
   registrar account, and try new workflows against a test account first.
