# AI Log — Repair truncated tail of AUTHORITY_INDEX.md

Date: 2026-06-27

Actor: Claude (claude-opus-4-8)

## Context

Started as a review of the prior ChatGPT work logged in
`ai_logs/2026-06-26-role-facet-expression-model.md` (contextual role-facet
expression model), with the intent to continue its open `To verify` item:
indexing the four role documents in `AUTHORITY_INDEX.md`.

Investigation showed that item was already resolved on `main`: commit
`094d0a9` ("docs: index card stack and role quality cluster") had already
added the four role rows (`ARCHITECTURE_METHOD_TAXONOMY.md`,
`ARCHITECTURE_ROLE_FACETS.md`, `ARCHITECTURE_ROLE_REFLEX_COORDINATION.md`,
`ARCHITECTURE_ROLE_ACTIVATION_MODEL.md`) plus two card-stack rows
(`CARD_STACK_MODEL.md`, `CARD_STACK_ROLE_QUALITY_ALIGNMENT.md`).

The same commit, however, introduced a defect. While adding those map rows
(13 insertions) it also deleted 107 trailing lines of the file
(369 -> 268 lines), dropping four governance sections:

- `## Domain pack rule`
- `## External runtime memory adapter rule`
- `## Data platform rule`
- `## Sensitive-path guardrail` (ending in the required end-sentinel
  "Those paths require explicit approval in their own work package.")

This is the exact "partial read written back as full-file replacement"
failure mode that `.github/scripts/check_no_truncation.py` exists to catch.
That tripwire was firing on `main` (268 lines < 300 minimum; sentinel
absent) and consequently on PR #229's merge ref.

## Change made

Updated:

- `docs/governance/AUTHORITY_INDEX.md`

Restored the truncated tail verbatim from the last intact version
(`0efdd87`, 369 lines) onto `main`'s current map-complete file. The current
authority map — including the card-stack and role-quality rows added by
`094d0a9` — is preserved unchanged; only the lost tail (terminology
reserved-word block, closing paragraph, and the four sections above) was
restored. Result: 375 lines, end-sentinel present.

PR #229 was rebased onto current `main` and its now-redundant role-doc
index rows (already present on `main`) were dropped, so the PR carries only
the truncation repair.

## Verification

Ran the read-only governance checks locally with the CI base ref
(`GOVERNANCE_BASE_REF`):

- `check_no_truncation.py`: OK (length and end-sentinel restored).
- `check_status_headers.py`, `check_internal_links.py`: OK.
- `check_index_coverage.py`, `check_axis_vocabulary.py`: exit 0 under the
  base ref. Their unindexed-doc and `schemas/` vocabulary findings are
  pre-existing on `main`, unrelated to this change, and are not introduced
  by it.

## Boundary preserved

The change is one governance index document only. No promotion to canonical
doctrine. No `schemas/`, `tests/`, `operations/`, `platform/`, Docker,
`.env`, `pyproject.toml` or `CLAUDE.md` change. No agent, runtime, router,
scheduler, queue, approval engine or memory engine. No external action. No
Registre Probatoire entry.

## Repo state

Documented non-implemented. The restored sections are governance text, not
executable artifacts.

## Decision status

Accepted:

- restore the lost tail of `AUTHORITY_INDEX.md` (the tripwire's prescribed
  remedy: restore a lost tail from git history);
- keep `main`'s authority map (card-stack and role-quality rows) intact;
- drop the redundant role-doc indexing originally proposed in PR #229.

To note for the human:

- the truncation originated in `094d0a9` on `main`; this repair brings
  `main` back to green on the truncation tripwire via PR #229;
- the `ARCHITECTURE_ROLE_ACTIVATION_MODEL.md` filename-vs-title mismatch and
  the architecture-specific-vs-generic scope of the expression model remain
  open for human arbitration (unchanged).
