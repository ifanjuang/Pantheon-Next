# AI Log — Coverage Checker Sub-Index Extension (PR C)

Date: 2026-07-05

Repository: `ifanjuang/Pantheon-Next`

## Context

Explicitly approved by the user ("vas-y") after the obsolete/absent
group landed (#283). This is step PR C of
`AUTHORITY_INDEX_DECOMPOSITION_PLAN.md`: the one step that modifies a
`.github/scripts` checker, which the plan reserved for explicit
approval. It unblocks candidate-row migration to sub-indexes.

## Design principle

```text
The master index remains the sole interpreter and the single
registration point. A sub-index under docs/governance/authority/
extends the coverage corpus only if the master file itself cites its
path. An unregistered file under authority/ extends nothing.
```

## Change made

```text
.github/scripts/check_index_coverage.py:
- new SUBINDEX_PREFIX constant and registered_subindexes(): sub-index
  paths cited in the master file that exist;
- index_text() now concatenates the master text with the registered
  sub-index texts; candidate membership, grouped rows and the
  missing-path validation all operate on the combined corpus;
- docstring records the policy and its approval date.
Read-only behavior preserved; baseline mechanism unchanged.
```

Documentation updated in the same change: the grouped-row paragraph of
`AUTHORITY_INDEX.md` documents the registered-sub-index rule, and
section 7 of the decomposition plan records the resolution.

## Verification

```text
Scenario 0 — current tree: pass.
Scenario 1 — candidate row (WORKFLOW_LIFECYCLE.md) moved from the
  master into registered GOVERNANCE_AUTHORITY_INDEX.md: pass (this
  failed before the extension).
Scenario 2 — same row present only in an unregistered
  authority/UNREGISTERED_TEST.md: fail with exactly the expected
  candidate-not-indexed violation.
Restored tree: pass. Full governance check suite green with
GOVERNANCE_BASE_REF=origin/main; mcp-server doctor tests OK (no
coverage mirror exists in doctor.py).
```

## Pre-existing debt observed (not fixed here)

```text
Four candidate docs are unindexed on main and masked by the CI
baseline: CARD_STACK_KNOWLEDGE_CORPUS_ALIGNMENT.md,
METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md,
MISSING_INFORMATION_DISCIPLINE.md, WORKFLOW_DEPTH_POLICY.md.
They predate this change and remain baseline exceptions; indexing
them is a separate hygiene pass for the maintainer to schedule.
```

## Repo state

```text
Coverage checker sub-index support: implemented (read-only check).
Candidate-row migration: unblocked, not performed here.
```
