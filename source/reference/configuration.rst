Configuration reference
=======================

All settings are environment variables in ``/etc/mcprack/env`` (``KEY=value`` lines;
quote values that contain spaces or ``$``). Restart the service after a change:
``sudo systemctl restart mcprack``. Defaults are shown in parentheses.

Core
----

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Variable
     - Meaning
   * - ``SECRET_KEY``
     - Signs sessions, relay tokens and reset links; keys the local secret store and
       the audit mirror. At least 32 characters, no placeholder, or the service
       refuses to start.
   * - ``SECRET_KEY_FALLBACKS``
     - Comma-separated old keys that stay valid (:doc:`../howto/rotate-secret-key`)
   * - ``SQLALCHEMY_DATABASE_URI``
     - Database (set by the installer; SQLite by default)
   * - ``PUBLIC_BASE_URL``
     - Public address; used for reset links, OAuth metadata and as the accepted
       ``Host``
   * - ``TRUSTED_HOSTS``
     - Further accepted host names (comma separated)
   * - ``GUNICORN_BIND``
     - (``127.0.0.1:8912``) Where gunicorn listens; to change it per host see
       :doc:`../howto/change-listen-address`
   * - ``GUNICORN_THREADS``
     - (``8``) Threads per worker
   * - ``SESSION_COOKIE_SECURE``
     - (``true``) Set ``false`` only for plain-HTTP intranet installs
   * - ``SESSION_LIFETIME_SECONDS``
     - (``28800``) Session length
   * - ``MAX_CONTENT_LENGTH``
     - (``2097152``) Request body limit
   * - ``DEMO_MODE``, ``DEMO_USERNAME``, ``DEMO_PASSWORD``
     - Public demo mode (:doc:`../security/internet-checklist`)

Accounts and sign-in
--------------------

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Variable
     - Meaning
   * - ``PASSWORD_MIN_LENGTH``
     - (``12``)
   * - ``LOGIN_MAX_FAILURES``
     - (``5``) per account and address
   * - ``LOGIN_ACCOUNT_MAX_FAILURES``, ``LOGIN_IP_MAX_FAILURES``
     - (``50``, ``30``) per account, per address
   * - ``LOGIN_FAILURE_WINDOW_SECONDS``
     - (``900``)
   * - ``LOGIN_LOCK_BASE_SECONDS``, ``LOGIN_LOCK_MAX_SECONDS``
     - (``30``, ``3600``)
   * - ``LOGIN_THROTTLE_ENABLED``
     - (``true``)
   * - ``LOGIN_RATE_LIMIT``, ``PASSWORD_RESET_RATE_LIMIT``
     - Flask-Limiter budgets per worker (``10 per minute;50 per hour``,
       ``5 per minute;20 per hour``)
   * - ``RATELIMIT_STORAGE_URI``
     - (``memory://``)
   * - ``LDAP_ENABLED``, ``LDAP_SERVER``, ``LDAP_BASE_DN``, ``LDAP_USER_OU``,
       ``LDAP_USER_FILTER``, ``LDAP_BIND_DN``, ``LDAP_BIND_PASSWORD``
     - Directory settings (:doc:`../security/authentication`)
   * - ``LDAP_STARTTLS``, ``LDAP_CA_FILE``, ``LDAP_TLS_VALIDATE``, ``LDAP_REQUIRED_GROUP``
     - TLS and group restriction
   * - ``SMTP_HOST``, ``SMTP_PORT``, ``SMTP_USERNAME``, ``SMTP_PASSWORD``,
       ``SMTP_USE_TLS``, ``SMTP_FROM``
     - Mail for password reset
   * - ``PASSWORD_RESET_MAX_AGE_SECONDS``
     - (``3600``)
   * - ``MFA_REQUIRED_FOR_ADMINS``
     - (``true``)
   * - ``MFA_ISSUER``, ``MFA_PENDING_SECONDS``, ``MFA_RECOVERY_CODE_COUNT``
     - (``mcprack``, ``300``, ``10``)
   * - ``ADMIN_REAUTH_SECONDS``
     - (``600``) Freshness window for dangerous admin actions; ``0`` = off

Access, tokens and OAuth
------------------------

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Variable
     - Meaning
   * - ``STRICT_SERVER_PERMISSIONS``
     - (``true``) A user without grants sees no server
   * - ``PROXY_TOKEN_MAX_AGE_SECONDS``
     - Lifetime of path tokens (unset = no expiry; fresh installs: 90 days)
   * - ``PROXY_BEARER_ENABLED``
     - (``true``) Bearer relay route with ``proxy:access`` API tokens
   * - ``API_TOKEN_DEFAULT_EXPIRY_DAYS``
     - (``90``) ``0`` = tokens do not expire by default
   * - ``OVERRIDE_UNDECLARED_KEYS``
     - (``credentials``) or ``any``
   * - ``OAUTH_ENABLED``
     - (``false``)
   * - ``OAUTH_ACCESS_TOKEN_EXPIRES``, ``OAUTH_REFRESH_TOKEN_EXPIRES``
     - (``3600``, ``2592000``) seconds
   * - ``OAUTH_ALLOWED_REDIRECT_HOSTS``, ``OAUTH_ALLOWED_REDIRECT_PREFIXES``
     - (``claude.ai,claude.com``, empty)
   * - ``OAUTH_MAX_CLIENTS``, ``OAUTH_UNUSED_CLIENT_TTL_HOURS``,
       ``OAUTH_CLIENT_MIN_AGE_SECONDS``
     - (``500``, ``24``, ``900``)
   * - ``OAUTH_TOKEN_RATE_LIMIT``, ``OAUTH_REGISTER_RATE_LIMIT``
     - (``30 per minute``, ``10 per minute;100 per hour``)

Servers, processes and policies
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Variable
     - Meaning
   * - ``FASTMCP_BIN``
     - Path of ``fastmcp`` if it is not on ``PATH``
   * - ``MCP_PROXY_HANDSHAKE_TIMEOUT``
     - (``15``) Seconds a freshly started process has to answer ``initialize``
   * - ``MCP_COLD_START_CONCURRENCY``, ``MCP_COLD_START_WAIT``
     - (``3``, ``10``) Servers starting at once per worker; seconds to wait for a slot
   * - ``MCP_CHILD_ENV_ALLOW``
     - Extra variable names a started process may inherit (secrets are never allowed)
   * - ``ALLOWED_COMMAND_DIRS``
     - Strict command allowlist (empty = off)
   * - ``COMMAND_ALLOW_VOLATILE_DIRS``
     - (``false``) Allow commands in ``/tmp`` etc. (development)
   * - ``BACKEND_ALLOW_LINK_LOCAL``
     - (``false``) Allow link-local backend URLs
   * - ``INSTALL_REQUIRE_PINNED``, ``INSTALL_ALLOW_SOURCE_BUILDS``
     - (``true``, ``false``) Package installer rules

Secrets
-------

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Variable
     - Meaning
   * - ``BW_SERVER``, ``BW_CLIENTID``, ``BW_CLIENTSECRET``, ``BW_PASSWORD``
     - Vaultwarden connection; empty ``BW_SERVER`` = local encrypted store
   * - ``BW_ITEM_PREFIX``
     - (``MCP-``)
   * - ``BW_BIN``
     - (``/usr/bin/bw``)
   * - ``BW_COMMAND_TIMEOUT``, ``BW_LOCK_TIMEOUT``, ``BW_ENV_CACHE_TTL``
     - (``12``, ``20``, ``60``) seconds

Audit and monitoring
--------------------

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Variable
     - Meaning
   * - ``AUDIT_RETENTION_DAYS``
     - (``90``)
   * - ``AUDIT_MIRROR_ENABLED``, ``AUDIT_MIRROR_STDERR``
     - (``true``, ``true``)
   * - ``AUDIT_LOG_FILE``
     - Unset: ``/var/log/mcprack/audit.log`` if writable; a path; or ``off``
   * - ``MONITORING_TOKEN``, ``MONITORING_USER_ID``, ``MONITORING_CACHE_TTL``
     - ``/health/servers`` (:doc:`../howto/monitoring`)
   * - ``OTEL_ENABLED``, ``OTEL_EXPORTER_OTLP_ENDPOINT``, ``OTEL_SERVICE_NAME``,
       ``OTEL_EXPORTER_OTLP_PROTOCOL``, ``OTEL_TRACES_SAMPLER``,
       ``OTEL_TRACE_UI_URL_TEMPLATE``
     - OpenTelemetry
