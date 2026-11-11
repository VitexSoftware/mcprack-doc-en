Policies for commands, URLs and installs
========================================

A registered server is run or contacted by the mcprack host. Only administrators
register servers, but an administrator account is exactly what an attacker wants,
so the obvious abuses are closed.

Commands
--------

Always refused, when a server is saved *and* when its process is started (so a row
written directly into the database does not get around it):

- a command in ``/tmp``, ``/var/tmp``, ``/dev/shm``, ``/run/user``, ``/proc`` or
  ``/dev`` — judged on the normalised path (``/usr/bin/../../tmp/x`` is ``/tmp/x``)
  and on where a symbolic link really leads;
- a relative path containing ``/``;
- a command with a NUL byte or a newline.

``COMMAND_ALLOW_VOLATILE_DIRS=true`` lifts the first rule for development.

Strict mode
~~~~~~~~~~~

.. code-block:: bash

   ALLOWED_COMMAND_DIRS=/usr/bin,/usr/local/bin,/var/lib/mcprack/installs

With this set (comma or colon separated absolute directories) the command must lie
inside one of them; a bare name such as ``uvx`` is looked up on ``PATH`` first.
Include ``/var/lib/mcprack/installs`` if you use the package installer.

.. important::

   A directory allowlist cannot make a command safe by itself: ``/usr/bin`` also
   holds shells and interpreters. It keeps a *dropped payload* out; it does not
   replace trusting the servers you register.

URLs
----

A server URL must be ``http`` or ``https``, must not carry credentials (they would
be stored and logged in clear text), and must not point at:

- link-local addresses (``169.254.0.0/16``, ``fe80::/10``) — where cloud metadata
  services live — in any spelling the resolver accepts (``2852039166``,
  ``0xa9fea9fe``, ``::ffff:169.254.169.254``);
- the cloud metadata host names;
- ``0.0.0.0`` / ``::`` and multicast.

The check runs at registration and again at the moment the relay connects, so a
server saved earlier is covered too. ``BACKEND_ALLOW_LINK_LOCAL=true`` allows
link-local backends.

.. note::

   Host *names* are not resolved when checked, so a name that resolves to a
   forbidden address later is not caught (DNS rebinding). Combine the policy with an
   egress filter for the ``mcprack`` user:

   .. code-block:: text

      table inet mcprack_egress {
        chain output {
          type filter hook output priority 0; policy accept;
          meta skuid mcprack ip daddr 169.254.0.0/16 reject
          meta skuid mcprack ip6 daddr fe80::/10 reject
        }
      }

Per-user overrides
------------------

See :doc:`../concepts/access-control`. Process-altering names are always refused; an
endpoint override withholds the shared secrets.

The installer
-------------

*Admin → Install* takes registry package names only (no URLs, paths or VCS
references), runs without a shell, requires an exact version
(``INSTALL_REQUIRE_PINNED``), installs wheels only for pip
(``INSTALL_ALLOW_SOURCE_BUILDS``) and never runs npm lifecycle scripts.

Relay limits
------------

Only protocol headers cross the relay in both directions
(:doc:`../concepts/relay-and-tokens`), a buffered answer is limited to 16 MiB and
at most three servers start at the same time per worker.
