mcp-server-mastodon
===================

An MCP server for the **Mastodon** social network. Companion package:
``mcprack-mcp-server-mastodon``. Binary: ``/usr/bin/mcp-server-mastodon``
(``mastodon-mcp`` is an alias).

.. code-block:: bash

   sudo apt install mcprack-mcp-server-mastodon

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 30 12 14 44

   * - Variable
     - Required
     - Default
     - Meaning
   * - ``MASTODON_INSTANCE``
     - yes
     -
     - Instance URL (``https://mastodon.social`` or just ``mastodon.social``)
   * - ``MASTODON_ACCESS_TOKEN``
     - yes
     -
     - OAuth access token of the account
   * - ``READ_ONLY``
     - no
     - ``true``
     - Disables all write operations
   * - ``MASTODON_MCP_TRANSPORT``
     - no
     - ``stdio``
     - ``stdio`` or ``streamable-http``; under mcprack it is ``stdio``

Keep ``MASTODON_ACCESS_TOKEN`` in the secret store. Allow users to override it so
that people post as themselves; a shared account makes every post come from one
profile.

.. code-block:: bash

   sudo mcprack secret set mcp-server-mastodon MASTODON_ACCESS_TOKEN

Tools
-----

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Group
     - Examples
   * - Timelines
     - ``timeline_home``, ``timeline_local``, ``timeline_public``, ``timeline_hashtag``
   * - Statuses
     - ``status_get``, ``status_context``, ``status_post``, ``status_delete``,
       ``status_favourite``, ``status_reblog``, ``status_bookmark`` and their inverses
   * - Accounts and social graph
     - ``account_get``, ``account_search``, ``account_follow``, ``account_block``,
       ``account_mute``, ``account_relationships``, ``account_update``
   * - Notifications, lists, search
     - ``notifications_get``, ``notifications_clear``, ``list_create``,
       ``list_accounts_add``, ``search``
   * - Discovery
     - ``trending_tags``, ``trending_statuses``, ``trending_links``, ``directory``
   * - Media and polls
     - ``media_post``, ``poll_vote``

Everything that changes something (posting, following, deleting, updating the
profile) is refused while ``READ_ONLY`` is ``true``.
