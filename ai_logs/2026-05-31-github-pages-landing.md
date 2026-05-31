# AI Log — GitHub Pages Landing Page

Date: 2026-05-31

## Context

The user wanted to develop the GitHub Pages surface as the public showcase for Pantheon Next, not only as a technical D3.js diagram.

The user chose the option to make `docs/index.html` the proper landing page.

## Changed files

- `docs/index.html`
- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`
- `ai_logs/2026-05-31-github-pages-landing.md`

## What changed

`docs/index.html` was refactored into a static public landing page that explains:

- the problem Pantheon addresses;
- the core doctrine: OpenWebUI exposes, Hermes executes, Pantheon governs;
- the target architecture;
- the role of the interactive D3 map;
- optional modules such as Langflow, LangGraph, Langfuse and provenance support;
- rejected drift patterns;
- the real project status and non-runtime boundary;
- links to the interactive map, `STATUS.md`, `CAPABILITY_PLACEMENT.md`, `BRIDGE_CONTRACT.md`, `EXECUTION_MINIMALISM.md`, the template registry and the GitHub repository.

The D3 map was also adjusted so that:

- files under `docs/` remain reachable from GitHub Pages through relative links;
- files outside `docs/` such as `templates/` and `hermes/` point directly to the GitHub repository.

## Boundary

This intervention is a static documentation and website update only.

It does not implement OpenWebUI, Hermes, Langflow, LangGraph, Langfuse, provenance support or a Pantheon Bridge.

It does not create runtime behavior, tool execution, scheduler, queue, provider router, OpenWebUI plugin, Hermes skill, Langflow flow, LangGraph runtime, Langfuse backend or graph runtime.

## Risks and limitations

The landing page and map are static HTML assets.

The public site may take time to refresh on GitHub Pages after the commit.

The page is a showcase and navigation layer, not canonical doctrine. Governance documents remain authoritative.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```
