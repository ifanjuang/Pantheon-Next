# Evidence Topology Schema Candidate

Status: schema candidate note — not implemented.

Date: 2026-05-30

This document proposes possible future schema fields for Evidence Topology Gate support.

It is not a schema.

It does not modify files under `schemas/`.

It is not validation logic.

It is not runtime configuration.

It is not a Hermes dispatch contract.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

`EVIDENCE_TOPOLOGY_GATE.md` defines reasoning topology doctrine.

The fictional examples under `docs/examples/evidence_topology/` show how topology metadata might appear in future Task Contract and Evidence Pack examples.

This document records candidate fields before any protected schema work.

No field below is active schema until separately reviewed and approved.

## Candidate Task Contract field

Candidate field name:

```yaml
reasoning_topology:
  selected: single_primary_reasoning_context
  reason: cross_source_reasoning_required
  handoff_policy: no_summary_only_handoff
  evidence_policy: source_linked_evidence_items_required
```

Possible `selected` values:

```text
single_primary_reasoning_context
fanout_extract_then_single_synthesis
parallel_independent_workers
router
sequential_handoff
persistent_role_team_handoff
bounded_hermes_swarm
```

This field would declare governance expectations.

It must not be interpreted as runtime dispatch.

## Candidate additional Task Contract fields

```yaml
reasoning_topology:
  selected: persistent_role_team_handoff
  reason: artifact_bound_stage_work
  handoff_policy: bounded_artifact_required
  evidence_policy: handoff_artifacts_and_evidence_items_required
  memory_policy: role_memory_is_not_canonical_memory
  approval_policy: external_effect_requires_gate
  topology_risks:
    - role_memory_confused_with_canonical_memory
    - team_chat_confused_with_evidence_pack
    - handoff_confused_with_approval
  forbidden_handoffs:
    - summary_only_handoff
    - recommendation_without_source_locator
    - direct_publication_without_gate
```

Potential requirements:

- `selected` should be required when task risk is non-trivial;
- `reason` should be human-readable;
- `handoff_policy` should block summary-only transfer for consequential work;
- `evidence_policy` should indicate whether Evidence Items or Handoff Artifacts are expected;
- `approval_policy` should identify where execution must stop.

## Candidate Evidence Item shape

```yaml
evidence_item:
  evidence_id: ei-example-001
  claim: "Class X controls behavior Y"
  source_type: java_source
  source_ref: "src/path/ClassX.java:L120-L156"
  source_location: "method renderSummary"
  supports: ticket_intention_trace
  scope_of_support: "Only supports behavior Y under condition Z"
  confidence: medium
  limitations:
    - "Runtime behavior not tested"
  open_questions:
    - "Does XML condition A gate this branch?"
  scope_warnings:
    - "Do not generalize to adjacent ticket"
```

Candidate rule:

```text
Evidence Items support review.
They are not final conclusions.
```

## Candidate Handoff Artifact shape

```yaml
handoff_artifact:
  handoff_id: ha-example-001
  type: api_contract_note
  from_role: backend
  to_role: frontend
  scope: "New billing endpoint for dashboard display only"
  artifact_ref: "docs/contracts/billing-api-draft.md"
  changed_surface:
    - "GET /api/billing/summary"
  assumptions:
    - "Authentication middleware unchanged"
  blockers:
    - "Response pagination not validated"
  evidence_refs:
    - ei-example-001
  approval_gap: "Frontend may adapt UI, but deployment remains blocked pending review"
```

Candidate rule:

```text
A Handoff Artifact may preserve continuity.
It does not approve the next action.
```

## Candidate Evidence Pack topology section

```yaml
reasoning_topology_record:
  selected: fanout_extract_then_single_synthesis
  reason: many_sources_need_bounded_extraction_but_final_reasoning_must_be_unified
  rejected_topologies:
    - summary_only_supervisor_synthesis
    - unbounded_multi_agent_supervised
  worker_outputs_used:
    - ei-quote-001
    - ei-cctp-001
  handoff_artifacts_used: []
  contradictions_preserved:
    - c-quote-cctp-001
  unresolved_gaps:
    - missing_full_cctp
  approval_impact: user_decision_gate_required_before_external_transmission
```

Candidate rule:

```text
The Evidence Pack records why topology was chosen.
It must not store hidden chain-of-thought or raw runtime traces.
```

## Candidate validation constraints

Potential future validation constraints, if schemas are later changed:

- `selected` must be one of the approved topology values;
- `selected = single_primary_reasoning_context` should require evidence policy for source-linked claims;
- `selected = fanout_extract_then_single_synthesis` should forbid worker final conclusions;
- `selected = persistent_role_team_handoff` should require Handoff Artifacts and memory boundary notes;
- `selected = bounded_hermes_swarm` should require Task Contract scope and approval gap declaration;
- topology metadata must not include runtime IDs as primary governance identifiers;
- topology metadata must not imply dispatch, scheduling, queueing or provider routing.

## Protected work warning

Any real schema change requires separate confirmation because schema files are protected work.

Protected future files include, at minimum:

- `schemas/task_contract.schema.yaml`;
- `schemas/evidence_pack.schema.yaml`;
- `schemas/workflow_manifest.schema.yaml` if topology is ever reflected there;
- schema examples under `schemas/examples/`.

This document does not authorize those changes.

## Rejected schema drift

Reject these future schema mistakes:

```text
reasoning_topology as runtime dispatcher
reasoning_topology as worker scheduler
Evidence Item as approval
Handoff Artifact as approval
role memory as Canonical Memory
runtime trace as Evidence Pack
OpenWebUI display state as governance state
Hermes worker state as Pantheon state
```

## Recommended future sequence

1. Stabilize doctrine and examples.
2. Review whether `reasoning_topology` belongs in Task Contract only, Evidence Pack only, or both.
3. Review compatibility with `TASK_CONTRACTS.md`, `EVIDENCE_PACK.md`, `HERMES_INTEGRATION.md`, `MEMORY.md` and `SCOPE_ISOLATION.md`.
4. Request explicit confirmation before touching `schemas/`.
5. Add tests only after schema structure is approved.

## Final rule

```text
Describe topology before execution.
Do not make topology description execute anything.
```
