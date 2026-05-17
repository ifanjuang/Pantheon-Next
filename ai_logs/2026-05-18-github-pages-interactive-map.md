# AI Log — GitHub Pages interactive map setup

Date: 2026-05-18

## Scope

Prepared GitHub Pages-ready documentation assets for the Pantheon Next interactive connection map.

## Files changed

- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`
- `docs/assets/pantheon-map/README.md`
- `docs/index.html`
- `docs/.nojekyll`
- `README.fr.md`
- `README.md`
- `ai_logs/2026-05-18-github-pages-interactive-map.md`

## Summary

Added an interactive D3.js map showing:

- user request and project dossier;
- OpenWebUI as visible screen and container for documents, Knowledge and project spaces;
- Pantheon Next as the method governing entry, minimum necessary context, outputs and memory;
- Hermes Agent as execution workshop;
- Hermes skills as execution capabilities, not approvals;
- local and external LLMs such as Ollama, ChatGPT, Claude and Gemini;
- MCP and external tools such as Google Workspace, Notion and Trello;
- Pantheon memory, for example Postgres, behind a governed Memory Gateway;
- blocked paths such as `Documents -> LLM` without framing and `Hermes -> Postgres` direct write.

Added `docs/index.html` as a GitHub Pages landing page with the interactive map embedded through an iframe.

Added `docs/.nojekyll` so GitHub Pages serves the `docs/` tree without Jekyll processing assumptions.

Updated both README files with a direct link to the interactive map.

## GitHub Pages status

The repository now has files ready for GitHub Pages under `/docs`.

Manual repository settings may still be required:

```text
Settings -> Pages -> Build and deployment -> Source: Deploy from a branch
Branch: main
Folder: /docs
Save
```

Expected Pages URL after activation:

```text
https://ifanjuang.github.io/Pantheon-Next/
```

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The map and Pages site are documentation assets only.

They do not implement:

- OpenWebUI runtime integration;
- Hermes runtime integration;
- LLM provider routing;
- MCP integration;
- Postgres memory runtime;
- automatic memory promotion;
- automatic approvals;
- skill installation;
- scheduler;
- queue;
- hidden workflow runtime.

## Protected areas

No changes were made to:

- `pyproject.toml`;
- `schemas/`;
- `tests/`;
- `operations/`;
- `platform/`;
- Docker files;
- `.env`;
- `CLAUDE.md`.
