# AI Log — Architecture MVP review card JSON companion

Date: 2026-06-22

Actor: ChatGPT

## Context

After creating the static Markdown review/cockpit card for the architecture MVP fictive run, the user approved the next step: a JSON companion for future UI rendering.

The goal was to make the review card machine-readable without creating a schema or implementing Pantheon Control.

## Change made

Created:

- `templates/architecture/review_card_candidate.json`
- `examples/architecture/mvp_dossier_fictif/run_001_manual/04_review_card_candidate.json`

The template JSON is explicitly marked as:

```text
template candidate — non-executable data shape; not a schema
```

The run JSON companion captures:

- boundary flags;
- card identity;
- display status;
- one-line verdict;
- corpus snapshot;
- critical absent sources;
- key claims;
- contradictions;
- risk stack;
- wording status;
- expected decision;
- next evidence requests;
- card-level output posture.

A first larger JSON attempt was blocked by the tool safety layer, likely due to long free-text content. A compact data-first JSON companion was created instead.

## Boundary preserved

The change is documentation and fictive example data only.

No JSON schema was added.
No UI was implemented.
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

- JSON companion as data candidate for future UI rendering.
- Compact data-first representation instead of long text duplication.
- Keep schema work out of scope.

Refused:

- schema creation;
- UI implementation;
- runtime integration;
- external action;
- memory promotion.

To verify:

- whether the JSON shape is sufficient for a static HTML card;
- whether the field names should later be normalized through a schema proposal;
- whether Markdown remains the human source and JSON remains UI companion.

To arbitrate:

- whether the next step is static HTML rendering or Hermes handoff mapping.
