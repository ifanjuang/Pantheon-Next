# Governance Linkage & Status Reconciliation

Status: validation-only

Date: 2026-06-15

Purpose: a single read-only map of the governance-hygiene findings the four
read-only doctor checks surface on `main`, with a proposed batch order. This
note changes no other file and decides nothing; each batch below is a separate
governed candidate, prepared one dedicated PR at a time, after the user picks
it up.

## How to read this

These findings are currently tolerated by the CI **baseline policy** (dated
2026-06-11): when `GOVERNANCE_BASE_REF` is set, pre-existing violations are
treated as baseline exceptions, so CI stays green. They are *debt*, not
regressions. A careful file-by-file pass would retire them and shrink the
baseline.

Totals on `main` (commit of this note's base): **67 findings** —
8 broken internal references, 33 unindexed candidate docs, 18 status-header
issues, 8 axis-vocabulary findings (6 of which sit in protected `schemas/`).

Source of truth for vocabulary and statuses: `docs/governance/GLOSSARY.md` and
`docs/governance/AUTHORITY_INDEX.md`. Re-run any check locally with
`python3 .github/scripts/<check>.py` (full scan) or with
`GOVERNANCE_BASE_REF=origin/main` (CI-equivalent, baseline-aware).

---

## Batch 1 — Broken internal references (8) — `check_internal_links.py`

Smallest and safest. Each reference either needs a real target, a corrected
link, or removal/marking as planned. Per-finding judgement (target prefixes are
omitted below so this note does not itself register a broken link):

| Source file | Line | Missing target | Likely resolution |
| --- | --- | --- | --- |
| `docs/governance/AUTHORITY_INDEX.md` | 122 | `DATA_PLATFORM_*.md` (glob) | Checker limitation: the index intentionally groups a family with a glob. Leave as baseline, or teach the checker to accept glob groupings. No content change. |
| `docs/governance/DATA_PLATFORM_RECONCILIATION.md` | 576 | `implementation/data-platform/` | Planned directory, not present. Reword as planned/non-existent rather than a live link. |
| `docs/governance/DATA_PLATFORM_RECONCILIATION.md` | 582 | `adapters/data-platform/` | Same: planned directory. Reword as planned. |
| `docs/governance/GLOSSARY.md` | 155 | `profiles/hephaestus/` | Real typo: the directory is `profiles/hephaistos/`. Correct the spelling. |
| `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` | 160 | `PANTHEON_CONTROL_DASHBOARD.md` | Target never created; the surviving doc is `PANTHEON_CONTROL_BOUNDARY.md`. Relink or mark as not-yet-written. |
| `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` | 161 | `PANTHEON_CONTROL_INSTALLATION.md` | Same: relink to the boundary doc or mark planned. |
| `docs/governance/reference_reviews/2026-06-06-truememory-memory-patterns.md` | 840 | `evidence-memory/` (schemas) | Non-existent schema dir referenced in a reference review. Mark as illustrative/planned. |
| `docs/governance/reference_reviews/2026-06-06-truememory-memory-patterns.md` | 1014 | `PANTHEON_EVIDENCE_MEMORY.md` | Non-existent doc. Relink to `EVIDENCE_MEMORY_CANONICALIZATION.md` / `MEMORY.md` or mark planned. |

Boundary: documentation-only relinks. No new runtime, no new directory created
unless explicitly approved.

## Batch 2 — Status-header normalisation (18) — `check_status_headers.py`

Each governance doc must declare a `Status:` line in its first 10 lines whose
value belongs to an accepted family (see the check's `ACCEPTED_FAMILIES`:
`canonical`, `active doctrine`, `active support`, `support doctrine`,
`support review`, `candidate`, `to verify`, `validation-only`,
`external reference`, `reference`, `implementation artifact`,
`voluntarily absent`, `obsolete`, `refused`, `stub`, `example`,
`illustrative`).

Missing entirely (3) — **mandatory files, handle with extra care**:

- `docs/governance/AGENTS.md`
- `docs/governance/ROADMAP.md`
- `docs/governance/STATUS.md`

Unsupported value — needs to map to an accepted family while keeping the
descriptive tail (15):

- `docs/governance/AI_LEARNING_REPOS_DISTILLATION.md`
- `docs/governance/ARCHITECTURE.md`
- `docs/governance/CODE_AUDIT_POST_PIVOT.md`
- `docs/governance/CORE_CONCEPTS_MAP.md`
- `docs/governance/EXECUTION_DISCIPLINE.md`
- `docs/governance/GLOSSARY.md`
- `docs/governance/MARKDOWN_DOSSIER_WORKFLOW.md`
- `docs/governance/MODULES.md`
- `docs/governance/NARRATIVE.md`
- `docs/governance/PRODUCT_DIFFERENTIATION.md`
- `docs/governance/RAG_INGESTION_PIPELINE.md`
- `docs/governance/REPOSITORY_SIMPLIFICATION_PLAN.md`
- `docs/governance/ROLE_SIGNALS.md`
- `docs/governance/TASK_CONTRACT_REVISIONS.md`
- `docs/governance/VISUAL_LANGUAGE.md`

Note: several use the form `migrated and distilled from Pantheon-OS @ ...`. The
fix keeps the provenance but leads with an accepted family, e.g.
`Status: canonical — migrated and distilled from Pantheon-OS @ ...`. The exact
family per file is a content decision to confirm during the batch.

## Batch 3 — Authority-index coverage (33) — `check_index_coverage.py`

Docs whose `Status:` contains `candidate` must appear in
`docs/governance/AUTHORITY_INDEX.md`. The following candidate docs are not yet
indexed. Indexing is a single careful edit to `AUTHORITY_INDEX.md`, best done by
cluster:

Architecture cluster:

- `docs/domain-packs/architecture/DOCUMENT_REVIEW.md`
- `docs/domain-packs/architecture/INDEX_EFFECT_MATRIX.md`
- `docs/domain-packs/architecture/PROOF_REGISTER.md`
- `docs/domain-packs/architecture/PROOF_REGISTER_IMPLEMENTATION_SPEC.md`
- `docs/domain-packs/architecture/TARGET_WORKFLOWS.md`

Data-platform cluster:

- `docs/governance/DATA_PLATFORM_ARCHITECTURE.md`
- `docs/governance/DATA_PLATFORM_INDEX.md`
- `docs/governance/DATA_PLATFORM_RECONCILIATION.md`
- `docs/governance/DATA_PLATFORM_STATUS.md`

Single docs:

- `docs/governance/DOCUMENT_INTELLIGENCE.md`
- `docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md`
- `docs/governance/EVIDENCE_MEMORY_DEV_PLAN.md`
- `docs/governance/MODULE_INVOCATION_PREFLIGHT.md`
- `docs/governance/NANGO_HERMES_CONNECTOR_GATEWAY.md`
- `docs/governance/PADDLEOCR_HERMES_SKILL_NOTE.md`
- `docs/governance/PANTHEON_COCKPIT_UX_SPEC.md`
- `docs/governance/PANTHEON_CONTROL_BOUNDARY.md`
- `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`
- `docs/governance/RAW_DERIVED_GOVERNED_RECORDS.md`
- `docs/governance/REVIEW_QUEUE.md`
- `docs/governance/UNDERSTAND_ANYTHING_HERMES_ADAPTER.md`
- `docs/governance/URGENT_REVIEW_TRIAGE.md`

Reference-review cluster (`reference_reviews/`):

- `docs/governance/reference_reviews/AGENTOS.md`
- `docs/governance/reference_reviews/ASSERT.md`
- `docs/governance/reference_reviews/DIRECTORY_MCP.md`
- `docs/governance/reference_reviews/ELT_REFERENCE_REVIEW.md`
- `docs/governance/reference_reviews/FUTURE_AGI.md`
- `docs/governance/reference_reviews/NANGO.md`
- `docs/governance/reference_reviews/QUARKDOWN.md`
- `docs/governance/reference_reviews/SKILL_FORGE_RUNTIMES.md`
- `docs/governance/reference_reviews/SUB_AGENT_MCP.md`
- `docs/governance/reference_reviews/UNDERSTAND_ANYTHING.md`

Rite:

- `docs/governance/rites/RITE_TRIGGER_CATALOGUE.md`

Open question for this batch: whether `reference_reviews/*` candidate docs should
each be indexed individually, or whether the grouped index row
`reference_reviews/` is meant to cover them (in which case the check's
`candidate_docs` rule, not the index, is what should change). To arbitrate
before editing.

## Batch 4 — Axis vocabulary (8) — `check_axis_vocabulary.py`

Most delicate: 6 of 8 live in protected `schemas/`. Per `CLAUDE.md`, protected
paths get a **validation-only proposal** (the proposed change printed in a
governance note), never a direct edit, until the user explicitly approves.

Editable (docs) — 2:

- `docs/examples/evidence_topology/evidence_pack_topology_examples.yaml` lines 93, 112: field `confidence:` should read `certainty:` (axis E) unless explicitly legacy.

Protected `schemas/` — proposal-only — 6:

- `schemas/evidence_pack.schema.yaml` line 143: `confidence:` → `certainty:`
- `schemas/examples/evidence_pack.example.yaml` line 42: `confidence:` → `certainty:`
- `schemas/examples/evidence_pack.example.yaml` line 82: consequence-like context uses the C-axis (`approval_impact: C3 ...`); consequence is axis K, C is the approval ceiling.
- `schemas/examples/role_signal.example.yaml` line 9: `confidence:` → `certainty:`
- `schemas/examples/role_signal.example.yaml` line 22: C-axis used for a consequence-like context.
- `schemas/role_signal.schema.yaml` line 74: `confidence:` → `certainty:`

## Proposed order

1. Batch 1 — broken internal references (8). Smallest, highest signal, mostly relinks/typos.
2. Batch 2 — status-header normalisation (18). Mechanical but touches mandatory files; confirm family per file.
3. Batch 3 — authority-index coverage (33). One edit to `AUTHORITY_INDEX.md`, by cluster; resolve the `reference_reviews/` grouping question first.
4. Batch 4 — axis vocabulary (8). Docs first; `schemas/` as a validation-only proposal pending explicit approval.

Each batch: rebase on `main`, fix, re-run the relevant check with
`GOVERNANCE_BASE_REF=origin/main` to confirm zero new findings, one draft PR,
one `ai_logs/` entry.

## Boundary

This note is read-only governance documentation. It adds no runtime, approval
engine, memory engine, connector, scheduler or external action, and touches no
other file. Every batch it proposes remains a candidate routed through the
normal review before anything lands.
