# 2026-09-05 — proposal/outcome feedback metrics

## Objective

Distill the useful human-correction instrumentation pattern from `dtiger1889-ops/obsidian-agent-integration` without importing its Obsidian staging frontmatter, approval ledger or lifecycle as Pantheon owners.

## Verified baseline

```text
Pantheon-Next main = fd39f1d377d57eb2dc03060c0f93b21763b745b7
```

Current main, recent commits, open PRs/issues and current evaluation/data-platform owners were checked before the change.

`docs/governance/DATA_PLATFORM_ARCHITECTURE.md` already owns the conceptual records needed for this observation:

```text
workflow_action_proposals
workflow_action_executions
approval_records
audit_events
```

It already states that the platform records what was proposed, accepted, executed and reversible. A second feedback ledger would therefore duplicate ownership.

## Convergence

`hermes/profiles/_base/EVALUATION_AND_SIMULATION_CANDIDATE.md` now permits a derived `proposal_outcome_feedback` evaluation view over existing records.

The view keeps exact references to proposal/version, human disposition, actual resulting object/effect and later correction/reversal when present. Candidate metrics include acceptance, material override, abstention/held/unresolved, reformulation/reclassification, proposal-to-decision duration and later correction/reversal.

The contract requires:

- recomputing from proposal versus actual records rather than trusting a hand-stamped outcome label;
- reporting evaluated class, time window and sample size;
- reading material disagreements individually before generalizing;
- treating override as a disagreement signal rather than automatic model error;
- preventing metrics from auto-rewriting prompts, skills, policy, doctrine, routing, bindings or memory.

## Preserved boundaries

```text
metric != truth
override != model error
acceptance != Evidence
feedback observation != memory promotion
correlation != authorization
```

No schema, database table, approval lifecycle, feedback ledger, memory path or optimizer is added.

## Verification

`tests/test_proposal_outcome_feedback_contract.py` verifies both halves of the convergence: existing proposal/approval/execution/audit owners remain the source records, while the Hermes evaluation profile remains a derived, non-authoritative consumer.

GitHub CI is the execution gate because the local container cannot reach GitHub.

## Status

The evaluation contract is prepared. Real acceptance/override/correction rates remain unmeasured until actual governed workflows produce enough comparable reviewed cases; no numerical performance claim is made here.
