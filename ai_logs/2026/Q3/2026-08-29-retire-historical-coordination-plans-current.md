# Retire historical coordination plans — current replay

Date: 2026-08-29
Issue: #787
Base `main`: `ccfdebe3b2e39486167481790b2f97ce9b1129bf`
Branch: `codex/787-retire-historical-coordination-plans-current`
Supersedes work proposed in: #836

## Objective

Continue the #787 current-authority owner audit from current `main` by removing two documents whose useful responsibilities have already converged into current owners or repository history, while migrating the one machine-readable compatibility reference discovered by #836.

## Observed need

`REPOSITORY_SIMPLIFICATION_PLAN.md` still claimed active doctrine but described phase-1 simplification, predecessor migration, temporary stubs and a historical target tree. Current repository posture, status, authority and contribution owners already carry the surviving responsibilities.

`REQUEST_ORCHESTRATION.md` explicitly retained a historical compatibility filename while restating request intake/coordination responsibilities already owned by `REQUEST_LIFECYCLE.md` and specialist Task Contract, Evidence, approval and memory owners.

## Owner tests

### Repository simplification plan

No distinct current responsibility survives. Current repository posture, read path, status, authority, contribution discipline and provenance are already owned by `STATUS.md`, `WHAT_RUNS.md`, `AUTHORITY_INDEX.md`, `CONTRIBUTING.md`, `CLAUDE.md`, Git and `ai_logs/` as applicable.

Disposition: remove; Git history retains provenance.

### Request orchestration / coordination

No independent current responsibility survives after request lifecycle convergence. Keeping a second active intake/coordination owner would recreate the parallel-owner pattern #787 is removing.

Disposition: remove; `REQUEST_LIFECYCLE.md` remains the request-lifecycle owner.

## Affected consumers

The #836 validation found one machine-readable consumer: `schemas/workflow_manifest.schema.yaml` listed `docs/governance/REQUEST_ORCHESTRATION.md` in `governance_refs.default`.

This replay changes only that pointer to `docs/governance/REQUEST_LIFECYCLE.md`. The schema shape and runtime semantics are unchanged.

A fresh compare from #836's base to current `main` showed no intervening modification to the two removed documents, the Workflow Manifest schema, or the prior decision-log surface. The replay therefore preserves all concurrent work while avoiding a stale-branch merge.

## Migration and rollback

- remove `docs/governance/REPOSITORY_SIMPLIFICATION_PLAN.md`;
- remove `docs/governance/REQUEST_ORCHESTRATION.md`;
- retarget the Workflow Manifest governance reference to `REQUEST_LIFECYCLE.md`;
- preserve rationale in this `ai_log` and Git history.

Rollback is a normal Git revert of this replay slice.

## Authority impact

No authority promotion and no replacement owner is introduced. The surviving responsibilities already belong to current owners.

```text
request coordination != runtime orchestration
indexed != promoted
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
```

## Runtime impact

None. The schema change is a governance-reference migration only; no scheduler, router, workflow engine, runtime path or external action is introduced.

## Role / Rite / Space

- Role: THEMIS for authority-boundary review; MNEMOSYNE for provenance continuity.
- Rite: #787 documentation-owner convergence.
- Space: governance repository plus a protected schema reference migration.

## Validation

Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact final head and reviews, threads and comments have been inspected.
