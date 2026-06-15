# AI Log — Governance linkage & status reconciliation overview

Date: 2026-06-15

## Trigger

After merging #136, the user asked to start a careful, file-by-file pass to
"relier et vérifier" each file, and chose to produce an overview map first
before any edit.

## Doctrine read

- `CLAUDE.md` (protected paths, candidate rule, one-PR-per-batch work rules)
- `.github/scripts/check_internal_links.py`, `check_index_coverage.py`,
  `check_status_headers.py`, `check_axis_vocabulary.py` (to understand the
  baseline policy and detection logic)
- `.github/workflows/governance-ci.yml` (how the checks are invoked, baseline ref)

## Change

Added one read-only governance note:

- `docs/governance/GOVERNANCE_LINKAGE_RECONCILIATION.md` (Status: validation-only)

It maps the 67 findings the four read-only doctor checks surface on `main`
(8 broken internal references, 33 unindexed candidate docs, 18 status-header
issues, 8 axis-vocabulary findings — 6 in protected `schemas/`) and proposes a
batch order: links → status headers → index coverage → axis vocabulary, one
draft PR per batch, `schemas/` handled as validation-only proposals only.

No other file is touched. Each batch stays a candidate pending review.

## Boundary

Documentation only. No runtime, approval engine, memory engine, connector,
external action, schema, test, dependency, platform, operation or Docker
change. No protected path edited.

## Verification

- The note's missing-target citations omit the recognised path prefixes so the
  note does not itself register a broken internal reference.
- `Status: validation-only` is an accepted family and not `candidate`, so the
  note does not add an index-coverage obligation.
- All four doctor checks run with `GOVERNANCE_BASE_REF=origin/main` → exit 0,
  zero new findings. Forbidden-phrase replica on the new note → 0.
- Diff limited to:
  - `docs/governance/GOVERNANCE_LINKAGE_RECONCILIATION.md`
  - `ai_logs/2026-06-15-governance-linkage-reconciliation.md`
