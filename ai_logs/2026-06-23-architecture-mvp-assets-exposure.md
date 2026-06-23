# AI Log — Architecture MVP assets exposure

Date: 2026-06-23

Actor: ChatGPT

## Context

The user asked to proceed after GitHub Pages access to the `examples/` path could not be confirmed.

The safer publication path is `docs/assets/`, which is already used as the static asset area for Pantheon Next pages.

## Change made

Created:

- `docs/assets/architecture-mvp/index.html`

This page is a static exposed mirror of the architecture MVP run card.

It links back to the canonical source material under:

- `examples/architecture/mvp_dossier_fictif/`
- `run_001_manual/04_review_card_candidate.md`
- `run_001_manual/04_review_card_candidate.json`
- `run_001_manual/02_evidence_pack_candidate.md`
- `run_001_manual/03_result_candidate_note.md`

## Boundary preserved

The original example folder was not deleted or moved.

The new page is static HTML only.
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

- duplicate the static MVP cockpit card under `docs/assets/architecture-mvp/` for likely GitHub Pages exposure;
- keep `examples/` as canonical source material;
- use a static mirror rather than a runtime UI.

Refused:

- moving or deleting the source example;
- backend;
- JavaScript renderer;
- schema creation;
- runtime integration;
- external action;
- memory promotion.

To verify:

- whether GitHub Pages serves `docs/assets/architecture-mvp/index.html` after publication delay.

To arbitrate:

- whether this should later become a proper Pantheon Control mock page with shared CSS / JS, or remain a static review artifact.
