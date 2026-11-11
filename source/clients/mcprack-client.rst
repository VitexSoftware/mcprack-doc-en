mcprack-client
==============

``mcprack-client`` is the shared library behind the ``mcprack-sync-*`` tools. It is
standard-library Python only. Its job: fetch a user's generated configuration from
mcprack and merge it into a client's own configuration file, safely.

You normally install one of the sync tools (``mcprack-sync-claude``, ``-cursor``,
``-vscode``); this page documents what they have in common.

Settings
--------

``~/.config/mcprack/client.env`` (``0600``; ``/etc/mcprack/client.env`` is read
first, the environment overrides both):

.. code-block:: bash

   MCPRACK_URL=https://mcprack.example.com
   MCPRACK_TOKEN=mcr_...
   MCPRACK_TRUSTED_ORIGINS=https://other.example.com   # optional
   MCPRACK_ALLOW_INSECURE=1                            # optional

Create the file with ``configure``; give the token as a file or at the hidden
prompt (the value of ``--token`` would be visible in the process list):

.. code-block:: bash

   mcprack-sync-claude configure --url https://mcprack.example.com --token-file ~/.config/mcprack/token
   mcprack-sync-claude configure --url https://mcprack.example.com          # prompts

Create the API token in mcprack (user menu → API tokens); the ``config:read`` scope
is enough.

How a sync works
----------------

1. The tool fetches ``/api/v1/me/config/<client>``.
2. It **validates the whole answer** (below). If anything is wrong nothing is
   written and the exit status is ``3``.
3. It merges: servers mcprack manages are added or updated, servers mcprack
   managed before and no longer selects are removed, everything else in the file
   (preferences, servers you added yourself) is kept. ``--replace`` replaces the
   whole servers map instead.
4. It writes atomically.

What is accepted from the server
--------------------------------

The configuration is written into files where an entry with ``command`` is **a
program the client runs**. So a tampered answer must not be able to add one. Only
what mcprack really sends is accepted:

- entries consisting of ``type`` (``http`` or ``sse``), ``url`` and ``headers``
  only — never ``command``, ``args``, ``env``, ``cwd``;
- a ``url`` on the **same origin** as ``MCPRACK_URL`` (scheme, host, port). If mcprack
  builds its URLs from a ``PUBLIC_BASE_URL`` that differs from the address you
  reach it on, list it in ``MCPRACK_TRUSTED_ORIGINS`` (or ``configure
  --trusted-origin``);
- no ``${VAR}`` or ``${env:VAR}`` in a ``url`` or header, because clients substitute
  those from your environment. The one exception is
  ``Authorization: Bearer ${MCPRACK_TOKEN}``;
- header names that are plain RFC 7230 tokens, single-line values;
- server names of 1–64 letters, digits, ``.``, ``_``, ``-`` or space.

Transport
---------

The token is sent only over ``https`` or to loopback. Plain ``http`` to another
host needs ``MCPRACK_ALLOW_INSECURE=1`` (``configure --allow-insecure``).
Redirects are never followed (the token must not leave the host you configured),
the answer is limited to 4 MiB and text from the server is stripped of control
characters before it is printed.

Writing the file
----------------

- A backup ``<file>.bak`` is created with mode ``0600`` (it holds everything the
  original does — for ``~/.claude.json`` that includes OAuth tokens).
- A symbolic link is followed: the target is written, the link stays.
- The file's own permissions are kept.
- An answer that changes nothing does not touch the file.
- If the client saved the file while the tool was merging (Claude Code rewrites
  ``~/.claude.json`` constantly) the merge is redone on top of the newer content,
  up to three times.

Exit status
-----------

.. list-table::
   :widths: 10 90

   * - 0
     - Success (or ``--dry-run``)
   * - 1
     - Network, API or file error
   * - 2
     - Missing settings
   * - 3
     - The answer was refused by validation; nothing was written
