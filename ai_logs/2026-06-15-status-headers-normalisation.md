# AI Log — Status-header normalisation (Lot B)

Date: 2026-06-15

## Trigger

Second batch of the governance-hygiene pass mapped in
`docs/governance/GOVERNANCE_LINKAGE_RECONCILIATION.md` (merged via #138). The
user chose status-header normalisation as the first edit batch.

## Doctrine read

- `.github/scripts/check_status_headers.py` — matching is a **substring** test:
  the `Status:` value must contain one accepted family token. Detection reads
  the first line in the first 10 lines that starts with `status:`.
- `.github/scripts/check_index_coverage.py` — a doc whose `Status:` contains
  `candidate` must be indexed. This constrained the family choice (see below).
- `docs/governance/AUTHORITY_INDEX.md` — vocabulary alignment.

## Change

Normalised the `Status:` header of 18 governance docs:

- 3 had no `Status:` line — added one (AGENTS.md → canonical; ROADMAP.md →
  active support; STATUS.md → canonical, matching its existing index row).
- 15 had a descriptive value with no accepted family token — kept the
  descriptive tail and led with an accepted family:
  - active doctrine: ARCHITECTURE, EXECUTION_DISCIPLINE, MODULES,
    PRODUCT_DIFFERENTIATION, REPOSITORY_SIMPLIFICATION_PLAN, ROLE_SIGNALS,
    VISUAL_LANGUAGE
  - canonical: GLOSSARY (owner of the certainty/decision axes)
  - support review: AI_LEARNING_REPOS_DISTILLATION, CODE_AUDIT_POST_PIVOT
  - active support: CORE_CONCEPTS_MAP
  - illustrative: NARRATIVE
  - reference: TASK_CONTRACT_REVISIONS
  - to verify: MARKDOWN_DOSSIER_WORKFLOW, RAG_INGESTION_PIPELINE

### Notable decision

MARKDOWN_DOSSIER_WORKFLOW and RAG_INGESTION_PIPELINE are documented-not-
implemented proposals. The natural token `candidate` was **avoided**: it would
have made `check_index_coverage` immediately require them in AUTHORITY_INDEX.md,
creating a new violation. `to verify` conveys the same "documented, not yet
verified" status without the index obligation.

## Boundary

Documentation only — header lines. No runtime, schema, check-logic, dependency
or protected-path change. No doc reclassified into `candidate`, so the authority
index is untouched.

## Verification

- `check_status_headers.py` absolute findings: 18 → **0**.
- All four read-only checks with `GOVERNANCE_BASE_REF=origin/main` → exit 0,
  zero new findings.
- Candidate-doc set vs `origin/main`: unchanged (no new index obligation). The
  one pre-existing `reference_reviews/AGENTCANVAS_TRACE_VISUALIZATION.md`
  finding comes from commit `fd74740`, not this batch; it belongs to the
  `reference_reviews/` group that Lot A (check alignment) will cover.
- Diff: 18 files, header lines only.
