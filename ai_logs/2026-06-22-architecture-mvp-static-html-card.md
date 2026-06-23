# AI Log — Architecture MVP static HTML card

Date: 2026-06-22

Actor: ChatGPT

## Context

After creating the Markdown review card and JSON companion for the architecture MVP fictive run, the user approved creating a static HTML rendering.

The goal was to test cockpit readability without implementing Pantheon Control, without backend, without runtime and without JavaScript execution.

## Change made

Created:

- `templates/architecture/review_card_candidate.html`
- `examples/architecture/mvp_dossier_fictif/run_001_manual/04_review_card_candidate.html`

The HTML template is a static placeholder-based template.

The run HTML is a minimal static card displaying:

- candidate status;
- approval ceiling;
- requested effect;
- external action blocked;
- risk level;
- one-line verdict;
- source / missing evidence counts;
- risk stack;
- expected decision;
- links to Markdown, JSON, Evidence Pack and Result Candidate;
- boundary footer.

A fuller JavaScript-based HTML renderer and a fuller pre-rendered HTML card were blocked by the tool safety layer. The final committed instance is intentionally minimal, static and non-executable.

## Boundary preserved

The change is documentation and fictive example output only.

No JavaScript runtime was added.
No UI application was implemented.
No Pantheon Control code was created.
No Hermes profile or Kanban task was created.
No GraphRAG runtime was installed.
No Flexible GraphRAG dependency was installed.
No Docker file was modified.
No `.env` file was touched.
No runtime, gateway, MCP server, connector, vector database, graph database, RDF store, search index, provider router, scheduler, queue, auto-sync or memory engine was created.
No `schemas/`, `tests/`, `operations/`, `platform/`, `pyproject.toml` or `CLAUDE.md` file was modified.
No client data was added.
No external action was performed.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- Static HTML card as UX readability candidate.
- Minimal non-executable card rather than JS renderer.
- Links back to Markdown / JSON / Evidence Pack / Result Candidate as source material.

Refused:

- JavaScript-based renderer at this stage;
- UI implementation;
- backend;
- schema creation;
- runtime integration;
- external action;
- memory promotion.

To verify:

- whether this minimal HTML card is readable enough for a cockpit tile;
- whether the full Markdown card should remain the deeper view;
- whether the JSON companion is sufficient for later rendering.

To arbitrate:

- whether next step is a static index page listing run cards;
- whether next step is Hermes handoff mapping;
- whether next step is a proper Pantheon Control mock page under `docs/assets/`.
