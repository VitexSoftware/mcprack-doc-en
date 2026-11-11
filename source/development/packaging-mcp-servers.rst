Packaging an MCP server with a companion
========================================

This is the convention used by the VitexSoftware MCP servers so that a Debian
package for a **stdio** MCP server registers itself in a local mcprack catalog on
install and unregisters on removal, with no manual administrator step.

It is unrelated to *Admin → Install* (a runtime, administrator-driven installation
into ``/var/lib/mcprack/installs``). A companion is a **build-time** package that
only *tells* an already installed mcprack about a binary that apt installed.

Two packages, one source
------------------------

1. ``mcp-server-<name>`` — the server itself.
2. ``mcprack-mcp-server-<name>`` — the companion: only a ``postinst`` and ``prerm``;
   no files (lintian's ``empty-binary-package`` is overridden).

They share ``debian/changelog`` and a version. The companion depends on mcprack and
on the exact build of the server:

.. code-block:: text

   Package: mcprack-mcp-server-<name>
   Architecture: all
   Depends:
    ${misc:Depends},
    mcprack (>= 1.6.0),
    mcp-server-<name> (= ${binary:Version}),
   Description: Registers <Thing> MCP server into mcprack catalog
    Companion package for mcp-server-<name>. Installing it registers
    the binary as an available MCP server in the local mcprack
    instance; removing it unregisters it again.

``debian/mcprack-mcp-server-<name>.lintian-overrides``:

.. code-block:: text

   mcprack-mcp-server-<name>: empty-binary-package

Naming
------

- Server package and entry name: ``mcp-server-<name>`` (rename an older
  ``<name>-mcp-server`` package; keep ``Provides``/``Replaces``/``Breaks`` for the old
  name).
- Companion: ``mcprack-mcp-server-<name>``.
- Do not reuse a catalog name that an HTTP-proxy registration (for example from the
  ``mcp_rack`` Ansible role) already uses: whichever runs last silently overwrites
  the other.

Maintainer scripts
------------------

Both follow one defensive pattern: do nothing, successfully, if mcprack is absent.

``postinst``:

.. code-block:: sh

   #!/bin/sh
   set -e
   case "$1" in
     configure)
       if getent passwd mcprack >/dev/null 2>&1 && [ -d /usr/lib/mcprack ]; then
         su -s /bin/sh mcprack -c "cd /usr/lib/mcprack && set -a; . /etc/mcprack/env; set +a; \
           mcprack server create mcp-server-<name> \
             --label '<Label>' \
             --transport stdio \
             --command /usr/bin/mcp-server-<name> \
             --category debian \
             --enabled" || true
       fi
       ;;
   esac
   #DEBHELPER#
   exit 0

``prerm``:

.. code-block:: sh

   #!/bin/sh
   set -e
   case "$1" in
     remove|deconfigure)
       if getent passwd mcprack >/dev/null 2>&1 && [ -d /usr/lib/mcprack ]; then
         su -s /bin/sh mcprack -c "cd /usr/lib/mcprack && set -a; . /etc/mcprack/env; set +a; \
           mcprack server delete mcp-server-<name> --yes" || true
       fi
       ;;
   esac
   #DEBHELPER#
   exit 0

``server create`` is idempotent, so upgrades and re-installs are safe. Do not put
credentials into the registration; document the variables and let the administrator
set them in the secret store.

Requirements on the server itself
---------------------------------

A server that is registered in mcprack should:

- speak MCP over **stdio** (and may offer HTTP for stand-alone use);
- be **read-only by default**, with one explicit variable to allow writes, and treat
  an empty or unset value as read-only;
- take its credentials from environment variables;
- print nothing but MCP on standard output;
- start in a few seconds (mcprack waits ``MCP_PROXY_HANDSHAKE_TIMEOUT``, 15 s, for
  ``initialize``);
- pass ``mcprack server probe /usr/bin/mcp-server-<name>`` in an autopkgtest — it
  exits 0 only after a complete handshake and a ``tools/list``, which also proves the
  runtime dependencies are installed.
