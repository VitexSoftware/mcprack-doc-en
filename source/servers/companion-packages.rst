Companion packages
==================

A companion package is a Debian package named ``mcprack-mcp-server-<name>`` built
from the same source as ``mcp-server-<name>``. It ships no files. Its maintainer
scripts talk to mcprack:

``postinst``
   Registers the server in the local catalog, as the ``mcprack`` user:

   .. code-block:: bash

      mcprack server create mcp-server-<name> \
          --label '<Label>' \
          --transport stdio \
          --command /usr/bin/mcp-server-<name> \
          --category debian \
          --enabled

``prerm`` (on ``remove`` and ``deconfigure``)
   Unregisters it:

   .. code-block:: bash

      mcprack server delete mcp-server-<name> --yes

Both do nothing — successfully — when mcprack is not installed on the host, so a
companion never blocks an installation or a removal on a machine that does not run
mcprack.

Dependencies
------------

.. code-block:: text

   Depends: mcprack (>= 1.6.0), mcp-server-<name> (= ${binary:Version})

The exact-version dependency makes apt install and upgrade the pair together. All
companions in this documentation require mcprack 1.6.0 or newer and share their
version with the server.

What you get, and what you still do
-----------------------------------

.. list-table::
   :widths: 50 50

   * - **Automatic**
     - **Manual**
   * - A catalog entry named ``mcp-server-<name>``, category *debian*, enabled
     - Set the server's credentials (:doc:`../concepts/credentials`)
   * - Removal of the entry on uninstall
     - Grant users access and let them select it (:doc:`../howto/grant-access`)
   * -
     - Check that it starts: ``sudo mcprack server test mcp-server-<name>``

If you change the entry by hand (extra ``--set-env`` values, another label) a later
upgrade of the companion runs ``server create`` again, which updates the same
entry; keep your credentials in the secret store, not in the registration.

Command-line options the packages use
-------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Option
     - Meaning
   * - ``--transport stdio``
     - The server speaks MCP over standard input/output; mcprack runs it per user
   * - ``--command``
     - Absolute path of the installed binary
   * - ``--category debian``
     - Groups these entries in the catalog
   * - ``--set-env KEY=VALUE``
     - A non-secret environment value (needs mcprack 1.5.4 or newer)

The command must also pass mcprack's command policy (:doc:`../security/policies`);
``/usr/bin/...`` always does.
