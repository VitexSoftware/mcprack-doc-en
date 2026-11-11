# Documentation standards

Rules for every contribution to this repository.

- English only; active voice; second person ("you").
- reStructuredText (`.rst`) for all source files under `source/`.
- Always name the language of a code block (`.. code-block:: bash`).
- Provide working, copy-paste-ready examples; do not invent options — check them
  with `mcprack COMMAND --help`, the OpenAPI document (`/api/v1/openapi.json`) or
  the source.
- Document only released, implemented behaviour.
- Never put a real credential, token or host name of an actual installation into
  an example (`example.com`, `mcr_...`).
- Keep the per-server pages in `source/servers/` in line with the server's own
  `README.md` and tool list; mark every mutating tool and the variable that allows it.
- Build before you push: `make html` must finish without warnings.
