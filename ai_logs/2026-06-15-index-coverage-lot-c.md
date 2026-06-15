# AI Log — Index the 18 top-level candidate docs (Lot C)

Date: 2026-06-15

## Trigger

Lot C of the governance-hygiene pass (map in
`GOVERNANCE_LINKAGE_RECONCILIATION.md`, #138). After Lot A retired the 16
grouped members, 18 genuine top-level candidate docs remained unindexed in
`AUTHORITY_INDEX.md`.

## Doctrine read

`AUTHORITY_INDEX.md` table shape (`Path or area | Authority class | Repo state |
Notes`) and its status vocabulary. Each of the 18 docs was read for its declared
`Status:` and intent so the row reflects the doc rather than a guess.

## Change

Added 18 individual rows to the current authority map, immediately before the
grouped rows. Authority classes mirror each doc's own `Status:`
(`candidate support doctrine` or `candidate / to verify`); the Notes carry the
doc's purpose and its non-runtime guardrail. Coverage is visibility only — no
doc is promoted out of candidate.

Indexed: ARCHITECTURE_DOCUMENT_REVIEW, ARCHITECTURE_INDEX_EFFECT_MATRIX,
ARCHITECTURE_PROOF_REGISTER, ARCHITECTURE_PROOF_REGISTER_IMPLEMENTATION_SPEC,
ARCHITECTURE_TARGET_WORKFLOWS, DOCUMENT_INTELLIGENCE,
EVIDENCE_MEMORY_CANONICALIZATION, EVIDENCE_MEMORY_DEV_PLAN,
MODULE_INVOCATION_PREFLIGHT, NANGO_HERMES_CONNECTOR_GATEWAY,
PADDLEOCR_HERMES_SKILL_NOTE, PANTHEON_COCKPIT_UX_SPEC,
PANTHEON_CONTROL_BOUNDARY, PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT,
RAW_DERIVED_GOVERNED_RECORDS, REVIEW_QUEUE, UNDERSTAND_ANYTHING_HERMES_ADAPTER,
URGENT_REVIEW_TRIAGE.

## Boundary

Documentation only — index rows. No runtime, schema or check-logic change; no
authority class promoted.

## Verification

- Absolute `candidate-not-indexed`: 18 → **0**. The category is now empty.
- Every new row points to an existing file (no `missing-path` raised).
- All four read-only checks with `GOVERNANCE_BASE_REF=origin/main` → exit 0,
  zero new findings.
