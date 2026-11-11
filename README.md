# mcprack Documentation

![mcprack Documentation](mcprack-doc.svg)
![Packaging: deb](https://img.shields.io/badge/packaging-.deb-red?logo=debian&logoColor=white)

English documentation for [mcprack](https://github.com/VitexSoftware/mcprack) — a catalog and client-configuration portal for MCP (Model Context Protocol) servers — and for the projects around it: the client sync tools, the Ansible collection and the MCP servers that ship a mcprack companion package.

## Contents

- **Getting Started** — what mcprack is, quickstart, installation and upgrading
- **Core Concepts** — architecture, relay and tokens, access control, credentials, audit
- **How-To Guides** — registering servers, granting access, connecting Claude Code and other clients, OAuth, verifying a configuration, key rotation, monitoring
- **Security** — authentication, two-factor authentication, fresh re-authentication, command and URL policies, the audit mirror, an internet-exposure checklist
- **Client Tools** — `mcprack-client`, `mcprack-sync-claude`, `-cursor`, `-vscode`
- **Automation** — the `vitexsoftware.mcprack` Ansible collection
- **MCP Servers with a Companion** — AbraFlexi, Datovka, filesystem, Graylog, GroupOffice, LibreNMS, Mastodon, Semaphore, Subreg, Wazuh, WebDriver
- **Reference** — configuration, CLI, REST API, client formats, troubleshooting
- **Development** — packaging an MCP server with a companion, contributing

## Building Locally

### Prerequisites

```bash
sudo apt install python3-sphinx python3-shibuya-sphinx-theme
```

Or with pip:

```bash
pip install -r requirements.txt
```

### Build HTML

```bash
make html
# Output: build/html/index.html
```

Other formats: `make epub`, `make latex`, `make text`.

## Debian Package

The documentation is also distributed as a Debian package (`mcprack-doc`) that installs the built HTML to `/usr/share/doc/mcprack-doc/html/`.

```bash
dpkg-buildpackage -b --no-sign
sudo apt install ./mcprack-doc_*.deb
# Browse at http://localhost/mcprack-doc/  (requires Apache or Nginx)
```

Apache configuration is enabled automatically on install; an Nginx snippet is installed to `/usr/share/doc/mcprack-doc/mcprack-doc.nginx`.

## Documentation Standards

See [AGENTS.md](AGENTS.md). Key rules: English only; active voice; second person; reStructuredText; always name the language of a code block; only document released, implemented behaviour.

## Related Projects

| Project | Description |
|---|---|
| [mcprack](https://github.com/VitexSoftware/mcprack) | The web application, REST API and CLI |
| [mcprack-client](https://github.com/VitexSoftware/mcprack-client) | Shared library of the sync tools |
| [mcprack-sync-claude](https://github.com/VitexSoftware/mcprack-sync-claude) | Claude Desktop / Claude Code sync |
| [mcprack-sync-cursor](https://github.com/VitexSoftware/mcprack-sync-cursor) | Cursor sync |
| [mcprack-sync-vscode](https://github.com/VitexSoftware/mcprack-sync-vscode) | VS Code / Copilot sync |
| [mcprack-ansible-collection](https://github.com/VitexSoftware/mcprack-ansible-collection) | Ansible collection |
| [mcp-server-abraflexi](https://github.com/VitexSoftware/mcp-server-abraflexi), [-datovka](https://github.com/VitexSoftware/mcp-server-datovka), [-filesystem](https://github.com/VitexSoftware/mcp-server-filesystem), [-graylog](https://github.com/VitexSoftware/mcp-server-graylog), [-groupoffice](https://github.com/VitexSoftware/mcp-server-groupoffice), [-librenms](https://github.com/VitexSoftware/mcp-server-librenms), [-mastodon](https://github.com/VitexSoftware/mcp-server-mastodon), [-semaphore](https://github.com/VitexSoftware/mcp-server-semaphore), [-subreg](https://github.com/VitexSoftware/mcp-server-subreg), [-wazuh](https://github.com/VitexSoftware/mcp-server-wazuh), [-webdriver](https://github.com/VitexSoftware/mcp-server-webdriver) | MCP servers with a mcprack companion package |
