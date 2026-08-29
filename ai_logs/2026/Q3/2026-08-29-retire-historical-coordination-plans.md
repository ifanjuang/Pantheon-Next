# Retire historical coordination plans

Date: 2026-08-29
Issue: #787
Base `main`: `290fdd9ba4f35137b75780b4a32648113d14008c`
Branch: `codex/787-retire-historical-coordination-plans`

## Objective

Continue the #787 current-authority owner audit by removing two documents whose useful responsibilities have already converged into current owners or repository history.

## `REPOSITORY_SIMPLIFICATION_PLAN.md`

Observed state:

- status still claimed `active doctrine`;
- content explicitly described `phase 1 simplification`, predecessor migration rules, temporary stub policy and a phase-1 target tree;
- the current repository has already completed/changed those transitions through later convergence work;
- exact filename search found no current consumer outside historical `ai_logs`.

Owner test:

The file no longer owns a current responsibility. Current repository posture, read path, status, authority, contribution discipline and historical provenance are already owned by `STATUS.md`, `WHAT_RUNS.md`, `AUTHORITY_INDEX.md`, `CONTRIBUTING.md`, `CLAUDE.md` and Git/`ai_logs` as applicable.

Disposition: remove the completed plan; preserve history in Git.

## `REQUEST_ORCHESTRATION.md`

Observed state:

- the file itself says the filename is historical compatibility vocabulary and renames the concept to Request Coordination;
- it classifies intent/scope/domain/risk, role viewpoints, Task Contract need, Evidence expectations, approval, memory, output and escalation;
- current `REQUEST_LIFECYCLE.md` already owns proportional request activation, Case/Situation intake, request decomposition, source/context seams, output consequence, risk/escalation and the handoff toward Task Contract / Evidence / approval owners;
- exact filename search found no current Markdown consumer outside historical `ai_logs`.

Owner test:

No independent current responsibility survives. Keeping a second active document for the same intake/coordination path would recreate the parallel-owner pattern #787 is removing.

The first PR validation exposed one machine-readable consumer: `schemas/workflow_manifest.schema.yaml` still listed the compatibility path in `governance_refs.default`. That reference was migrated to `docs/governance/REQUEST_LIFECYCLE.md`. The schema shape and behavior are unchanged; only the governance-owner pointer moves to the surviving owner.

Disposition: remove the compatibility document; Git history preserves the former vocabulary and rationale.

## Net effect on #787 baseline

```text
current-authority gaps after #834: 32
removed in this slice:              2
expected remaining:                30
```

## Preserved boundaries

```text
request coordination != runtime orchestration
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
```

No new owner, runtime path, router, workflow engine or authority concept is introduced. The Workflow Manifest schema is modified only to replace a dead governance reference with the existing request-lifecycle owner.

## Validation

Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact final head and reviews/threads/comments have been inspected.
