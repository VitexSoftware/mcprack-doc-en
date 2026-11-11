Monitoring
==========

Zabbix
------

``/health`` (unauthenticated) only reports that the application and its database are
up. To catch a broken MCP server before users do, ``GET /health/servers`` performs a
real MCP handshake (``initialize`` and ``tools/list``) against every enabled server
and returns one entry each (``ok``, ``tools``, ``latency_ms``, ``error``). A backend
that crashed on start-up reports ``ok: false`` although the relay itself still
answers 200.

Enable it in ``/etc/mcprack/env`` (the endpoint answers ``404`` while the token is
unset):

.. code-block:: bash

   MONITORING_TOKEN=<long random string>
   MONITORING_USER_ID=<id of a normal mcprack user used for probing>
   MONITORING_CACHE_TTL=120        # optional, seconds between background refreshes

   curl -H "Authorization: Bearer $MONITORING_TOKEN" https://mcprack.example.com/health/servers

Probes run as ``MONITORING_USER_ID`` (that user's credentials and overrides apply).
A server that needs configuration this user lacks is reported as ``ok: null,
error: "unconfigured"`` and is not alerted on. Results come from a background
refresh, never from inside the request, so the first call after a restart returns
``{"pending": true}``.

The package ships a Zabbix 7.4 template in
``/usr/share/doc/mcprack/zabbix/template_mcprack.yaml``: **MCPrack by HTTP**
(health, per-server discovery with status, tools, latency and last error, triggers
for stale reports and a down endpoint; set ``{$MCPRACK.URL}`` and the secret macro
``{$MCPRACK.MONITOR_TOKEN}`` on the host) and **MCPrack service by Zabbix agent**
(systemd unit state and TLS certificate expiry; Zabbix agent 2).

Restrict the endpoint at the reverse proxy (see the commented ``Require ip`` block
in the sample vhost, :doc:`../security/internet-checklist`).

OpenTelemetry
-------------

Set ``OTEL_ENABLED=true`` and ``OTEL_EXPORTER_OTLP_ENDPOINT``. mcprack traces
relayed calls, proxy starts and configuration generation. ``OTEL_SERVICE_NAME``,
``OTEL_EXPORTER_OTLP_PROTOCOL`` and ``OTEL_TRACES_SAMPLER`` are honoured;
``OTEL_TRACE_UI_URL_TEMPLATE`` makes the audit log link to your trace UI. The
audit ``request_id`` correlates an audit entry with its trace.

Logs
----

.. code-block:: bash

   sudo journalctl -u mcprack -f
   sudo tail -f /var/log/mcprack/error.log

The audit mirror is in the journal (``grep AUDIT``) and in
``/var/log/mcprack/audit.log``: :doc:`../security/audit-mirror`.
