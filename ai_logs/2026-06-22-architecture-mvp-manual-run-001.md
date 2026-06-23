# AI Log — Architecture MVP manual run 001

Date: 2026-06-22

Actor: ChatGPT

## Context

The user asked to proceed after creating the Flexible GraphRAG reference review, architecture MVP fictive corpus and templates.

The next step was to run the fictive slice manually without any RAG runtime, GraphRAG runtime, MCP tool, parser, connector, auto-sync or external action.

Active doctrine was checked before producing the run outputs:

- `docs/governance/STATUS.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

The fictive corpus under `examples/architecture/mvp_dossier_fictif/corpus/` was read and used as the only admitted source perimeter.

## Change made

Created the first manual run output folder:

- `examples/architecture/mvp_dossier_fictif/run_001_manual/00_task_contract_candidate.md`
- `examples/architecture/mvp_dossier_fictif/run_001_manual/01_context_pack_candidate.md`
- `examples/architecture/mvp_dossier_fictif/run_001_manual/02_evidence_pack_candidate.md`
- `examples/architecture/mvp_dossier_fictif/run_001_manual/03_result_candidate_note.md`

## Run result

The run concludes that the admitted corpus is sufficient for internal candidate review but insufficient for any external response or professional validation.

Main blockers identified:

- missing dimensioned plans;
- fictive / non-official PLU source;
- unverified load-bearing status and non-visible lintel;
- no reinforcement dimensioning;
- contractor estimate excluding structure, planning, humidity and thermal studies;
- thermal assumptions without wall composition or final dimensions;
- dampness / slope / water-management uncertainties;
- no approval for external response.

## Boundary preserved

The change is documentation and fictive example output only.

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

- Manual run of the fictive architecture MVP slice.
- Candidate-only Task Contract, Context Pack, Evidence Pack and Result Candidate outputs.
- User Decision Gate candidate for any external response.

Refused:

- external contractor response;
- final regulatory conclusion;
- structural validation;
- thermal validation;
- memory promotion;
- professional delivery;
- GraphRAG installation or runtime use.

To verify:

- whether the manual run shape should become the expected baseline for future Hermes profile execution;
- whether the output folder naming convention should be standardized;
- whether a second run should test graph relation extraction manually.

To arbitrate:

- whether to keep the next MVP step document-only;
- whether to create a simple review card / cockpit display for this run;
- whether to map this run to a future Hermes `doc-intake` -> `evidence-review` -> `architecture-domain` Kanban sequence.
