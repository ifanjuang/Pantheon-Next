# AI Log — Architecture MVP run cards index

Date: 2026-06-23

Actor: ChatGPT

## Context

The user asked to proceed after the static HTML card and asked where it was located.

The next small step was to add a static index page inside the fictive architecture MVP dossier folder so that run cards can be discovered without a backend or Pantheon Control implementation.

## Change made

Created:

- `examples/architecture/mvp_dossier_fictif/index.html`

The index links to:

- `run_001_manual/04_review_card_candidate.html`
- `README.md`
- `corpus/00_manifest.md`
- `run_001_manual/00_task_contract_candidate.md`
- `run_001_manual/01_context_pack_candidate.md`
- `run_001_manual/02_evidence_pack_candidate.md`
- `run_001_manual/03_result_candidate_note.md`
- `run_001_manual/04_review_card_candidate.md`
- `run_001_manual/04_review_card_candidate.json`

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

- static run-card index as a lightweight cockpit discovery surface;
- index located inside the fictive dossier example;
- direct links to all run outputs.

Refused:

- backend;
- dynamic UI;
- schema creation;
- runtime integration;
- external action;
- memory promotion.

To verify:

- whether GitHub Pages serves the examples path as expected;
- whether this index is readable enough as a temporary cockpit list.

To arbitrate:

- whether next step is Hermes handoff mapping or a proper Pantheon Control mock page under `docs/assets/`.
