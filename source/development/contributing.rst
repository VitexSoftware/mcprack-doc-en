Contributing
============

Documentation
-------------

This documentation lives in `mcprack-doc-en
<https://github.com/VitexSoftware/mcprack-doc-en>`_. Edit the ``.rst`` file under
``source/``, build and check:

.. code-block:: bash

   make html
   # open build/html/index.html

Pushing to ``main`` rebuilds the Read the Docs site and the Debian package
``mcprack-doc``.

Rules: English, active voice, second person; reStructuredText; always name the
language of a code block; copy-pasteable examples; document only behaviour that is
released and implemented. See ``AGENTS.md``.

Code
----

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Repository
     - Notes
   * - `mcprack <https://github.com/VitexSoftware/mcprack>`_
     - Flask application. Tests: ``pytest`` (about 1500). Every security fix has a
       regression test that fails without the fix.
   * - `mcprack-client <https://github.com/VitexSoftware/mcprack-client>`_
     - Standard library only
   * - ``mcprack-sync-*``
     - Thin wrappers around ``mcprack_client.cli.run_cli``
   * - `mcprack-ansible-collection <https://github.com/VitexSoftware/mcprack-ansible-collection>`_
     - Role and modules

Conventions that matter when you change mcprack:

- A new mutating **admin route** must be classified in ``mcprack/reauth.py`` and
  ``mcprack/demo.py``; tests fail until it is.
- A new **audit action** goes into ``AuditLogEntry.ACTIONS``; the message must never
  contain a credential, an argument or a request body.
- Routes that issue a long-lived credential must call ``reauth.needed()`` in the
  view.
- A new setting belongs in ``mcprack/config.py`` with its default, and in the
  reference page.
- Migrations must be reversible.
