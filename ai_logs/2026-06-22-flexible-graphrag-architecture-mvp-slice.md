# AI Log — Flexible GraphRAG architecture MVP slice

Date: 2026-06-22

Actor: ChatGPT

## Context

The user asked to execute the recommended next step after analysis of the AI stack progress:

1. distill Flexible GraphRAG as a reference review;
2. create a narrow architecture MVP fictive dossier slice;
3. add templates for Task Contract, Context Pack Candidate, Evidence Pack Candidate and Result Candidate.

Active Pantheon doctrine was checked first:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

No existing Flexible GraphRAG-specific review, PR or issue was found before creating the new files.

## Source reviewed

External source:

- `https://github.com/stevereiner/flexible-graphrag`

Flexible GraphRAG was reviewed as an external document-intelligence / hybrid retrieval / GraphRAG platform reference, not as an approved Pantheon component.

## Change made

Created:

- `docs/governance/reference_reviews/FLEXIBLE_GRAPHRAG_REVIEW.md`
- `templates/architecture/task_contract_candidate.md`
- `templates/architecture/context_pack_candidate.md`
- `templates/architecture/evidence_pack_candidate.md`
- `templates/architecture/result_candidate_note.md`
- `examples/architecture/mvp_dossier_fictif/README.md`
- `examples/architecture/mvp_dossier_fictif/corpus/00_manifest.md`
- `examples/architecture/mvp_dossier_fictif/corpus/01_mail_client_programme.md`
- `examples/architecture/mvp_dossier_fictif/corpus/02_extrait_plu_fictif.md`
- `examples/architecture/mvp_dossier_fictif/corpus/03_notice_site_existante.md`
- `examples/architecture/mvp_dossier_fictif/corpus/04_cctp_lot_maconnerie.md`
- `examples/architecture/mvp_dossier_fictif/corpus/05_cctp_lot_menuiseries.md`
- `examples/architecture/mvp_dossier_fictif/corpus/06_cr_chantier_fictif.md`
- `examples/architecture/mvp_dossier_fictif/corpus/07_devis_entreprise_fictif.md`
- `examples/architecture/mvp_dossier_fictif/corpus/08_note_structure_fictive.md`
- `examples/architecture/mvp_dossier_fictif/corpus/09_notice_thermique_fictive.md`
- `examples/architecture/mvp_dossier_fictif/corpus/10_photo_commentee_fictive.md`

## Boundary preserved

The change is documentation and fictive examples only.

No Flexible GraphRAG dependency was installed.
No Docker file was modified.
No `.env` file was touched.
No runtime, gateway, MCP server, connector, vector database, graph database, RDF store, search index, provider router, scheduler, queue, auto-sync or memory engine was created.
No `schemas/`, `tests/`, `operations/`, `platform/`, `pyproject.toml` or `CLAUDE.md` file was modified.
No client data was added.
No external action was performed.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- Flexible GraphRAG as external document-intelligence and hybrid retrieval reference.
- Flexible GraphRAG as possible sandbox candidate for architecture-domain corpus review.
- Flexible GraphRAG as possible source of Fragment, Retrieval, Graph and Evidence Pack Candidates.
- A narrow fictive architecture corpus as first MVP slice.

Refused:

- Flexible GraphRAG as Pantheon runtime.
- Flexible GraphRAG as Registre Probatoire or canonical memory.
- Flexible GraphRAG as source of truth, proof authority or approval engine.
- Flexible GraphRAG as autonomous ingestion / auto-sync pipeline.
- Flexible GraphRAG MCP server as unrestricted tool surface.
- Flexible GraphRAG as production data platform before admission review.

To verify:

- Parser provenance.
- Auto-sync disablement.
- MCP permissions.
- Graph extraction reliability.
- RDF / ontology value for architecture.
- Source-fragment-provenance export.
- Hermes / Kanban compatibility.

To arbitrate:

- Whether first sandbox is document-only or includes graph extraction.
- Whether cloud parsing is allowed for non-sensitive test material.
- Whether MCP server remains disabled until capability passport review.
- Whether Flexible GraphRAG is a benchmark tool, future adapter or rejected overkill.
