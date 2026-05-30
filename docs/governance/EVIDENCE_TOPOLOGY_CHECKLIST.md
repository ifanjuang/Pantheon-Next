# Evidence Topology Checklist

Status: active checklist — documentation-level governance support.

Date: 2026-05-30

This checklist helps decide whether a task should use a single primary reasoning context, fan-out extraction, persistent role-team handoff or bounded Hermes swarm.

It supports `EVIDENCE_TOPOLOGY_GATE.md`.

It is not a schema.

It is not runtime configuration.

It is not a Hermes dispatch file.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Core question

```text
What topology preserves the proof chain with the smallest safe complexity?
```

Do not start from agent count.

Start from the shape of evidence.

## Fast decision table

| Situation | Preferred topology | Why |
|---|---|---|
| The answer depends on connecting evidence across sources | `single_primary_reasoning_context` | The decisive inference must not be fragmented. |
| Many sources must be inspected, but final reasoning must compare them | `fanout_extract_then_single_synthesis` | Extraction can be distributed; judgment must remain consolidated. |
| Tasks are independent and do not require hidden cross-source inference | `parallel_independent_workers` | Parallelism is useful and low-risk. |
| The first problem is category or domain selection | `router` | Routing classifies; it does not decide truth. |
| Each step produces a bounded artifact that the next step can verify | `sequential_handoff` | Handoff is safe only when artifact and evidence are reviewable. |
| Stable lanes own distinct artifacts or stages | `persistent_role_team_handoff` | Continuity is useful, but handoff must remain artifact-bound. |
| Execution needs capacity, not judgment | `bounded_hermes_swarm` | Swarm may multiply hands, not authority. |

## Twelve gating questions

Answer these before choosing topology.

### 1. Does the answer depend on a proof chain across sources?

Examples:

```text
email -> contract -> site report -> professional risk
Jira comment -> code -> XML config -> design note
quote -> CCTP -> photos -> client instruction
```

If yes, prefer:

```text
single_primary_reasoning_context
```

or:

```text
fanout_extract_then_single_synthesis
```

Do not use summary-only specialist agents.

### 2. Does the decisive material fit in one context window?

If yes, prefer one consolidated reasoning context.

If no, allow extraction first, then synthesize from selected Evidence Items.

### 3. Can workers extract facts without concluding?

If yes, fan-out may be safe.

If workers must interpret the whole case to be useful, do not split too early.

### 4. Would a summary lose decisive details?

If yes, summary-only handoff is forbidden.

Require Evidence Items with source locators.

### 5. Is there a real parallelism benefit?

Use parallel workers only when the work is independent or source extraction is large.

Do not use multi-agent merely to make the workflow look sophisticated.

### 6. Is the work stage-bound and artifact-bound?

If each role owns a distinct artifact, persistent role-team handoff may be useful.

Examples:

```text
architecture note -> backend contract -> frontend adaptation -> review note
research digest -> campaign brief -> draft -> editorial note -> metadata package
```

Require Handoff Artifacts.

### 7. Does the topology create external effect risk?

External effects include:

- sending;
- publishing;
- filing;
- deploying;
- merging;
- notifying;
- modifying a repository;
- creating client-facing output.

If yes, require approval gate.

### 8. Does the topology affect memory?

If role memory, worker state or repeated observations appear useful, keep them runtime-side unless promoted through governed Memory Candidate review.

```text
role memory != Canonical Memory
runtime state != Pantheon memory
```

### 9. Does the task need a User Decision Gate?

Trigger a gate if topology changes:

- risk;
- scope;
- cost;
- delay;
- external transmission;
- mutation;
- memory impact;
- evidence sufficiency.

### 10. Does a worker need broader scope than the Task Contract allows?

If yes, stop.

Return a scope gap.

Do not expand silently.

### 11. Are the handoffs reviewable?

A safe handoff contains:

- claim;
- source reference;
- source location;
- scope of support;
- confidence;
- limitation;
- open question;
- approval gap;
- artifact reference when relevant.

If the handoff is only prose, it is not enough for consequential work.

### 12. Who has authority?

Workers may collect.

Hermes may execute.

OpenWebUI may expose.

Pantheon governs status.

The human decides when approval is required.

## Decision outputs

A topology decision should produce a short record:

```yaml
topology_decision:
  selected: fanout_extract_then_single_synthesis
  reason: many_sources_but_unified_final_reasoning_required
  rejected:
    - summary_only_multi_agent_supervisor
    - direct_worker_conclusion
  required_outputs:
    - evidence_items
    - contradiction_ledger
    - approval_gap
  user_decision_gate: required_before_external_transmission
```

## Minimal safe defaults

When uncertain:

```text
single context for inference
fan-out only for extraction
role-team only for bounded artifacts
swarm only for execution capacity
User Decision Gate for unresolved stakes
```

## Red flags

Stop and review if the proposed topology contains:

```text
more agents therefore more reliable
summary-only handoff
worker final conclusion
team chat as evidence
role memory as canonical memory
visible canvas as approval
Conductor as Zeus
swarm as judgment
runtime trace as Evidence Pack
```

## Final rule

```text
Do not distribute judgment before preserving the proof chain.
```
