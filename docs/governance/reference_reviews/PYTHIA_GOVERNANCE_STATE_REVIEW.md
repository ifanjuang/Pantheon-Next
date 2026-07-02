# Pythia Governance State Review

Status: external reference / support review — candidate distillation only.

Review date: 2026-07-02

External repository reviewed:

```text
https://github.com/jangles-byte/Pythia
```

This document records what Pantheon Next may learn from Pythia without importing Pythia as doctrine, dependency, runtime, oracle, forecast authority, source of truth, cockpit implementation, MCP surface, approval engine, memory engine or external-action mechanism.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Classification

Pythia is useful as an external reference for a machine-readable situational view.

Pythia should not be imported as a Pantheon component.

Pantheon may distill the pattern:

```text
many inputs -> one consumable view -> downstream agent can inspect context
```

Pantheon must reject the collapse:

```text
consumable view -> truth
prediction -> proof
swarm consensus -> approval
agent-readable state -> authorized action
```

## Relevant Pythia pattern

Pythia exposes a single agent-facing endpoint, described as:

```text
GET /agent/view
```

The useful pattern is not world prediction. The useful pattern is a compact, machine-readable view that lets another system inspect the relevant situation without reconstructing the whole substrate.

In Pythia terms, the view includes a world summary, domains, events by domain, event count, predictions and live stream references.

Pantheon should not reproduce that content model. Pantheon has a different object of governance.

## Candidate Pantheon distillation

The Pantheon analogue is not a `world view`.

It is a `governance view`.

Candidate object:

```text
governance_state_view
```

Purpose:

```text
Expose the current governed situation in one reviewable object so an exposure surface,
execution runtime, MCP read-only policy surface or human cockpit can display the
same status without treating the view as runtime state or approval.
```

Candidate shape:

```yaml
governance_state_view:
  view_id:
  generated_at:
  scope:
    project_ref:
    subject_ref:
    task_contract_ref:
    request_ref:
  posture:
    process_status:
    governance_status:
    approval_ceiling:
    external_effect_possible:
    memory_effect_possible:
    canonical_effect_possible:
  context:
    context_pack_ref:
    context_stack_refs:
    missing_context:
    scope_limits:
  cards:
    workflow_scene_refs:
    evidence_scene_refs:
    document_refs:
    competence_refs:
    method_refs:
    role_quality_refs:
    rite_refs:
    action_candidate_refs:
    gate_refs:
  candidates:
    result_candidate_refs:
    evidence_pack_candidate_refs:
    intent_candidate_refs:
    register_candidate_refs:
  proof:
    top_evidence_refs:
    unresolved_assertions:
    contradictions:
    evidence_gaps:
    certainty_summary:
  decisions:
    open_gates:
    blocked_effects:
    user_decision_needed:
    zeus_arbitration_needed:
    next_allowed_moves:
  traces:
    trace_refs:
    runtime_state_refs:
    outcome_observation_candidates:
  limits:
    not_truth: true
    not_proof: true
    not_approval: true
    not_memory: true
    not_runtime_state: true
    not_action_authorization: true
```

This is not an approved schema. It is a review shape for future doctrine or adapter work.

## Placement

Accepted:

```text
Pythia as external reference for the one-call situational view pattern.
```

Accepted:

```text
A future Pantheon governance-state view may help OpenWebUI, Hermes, a static cockpit
or a read-only MCP policy surface display the same governed situation.
```

Accepted:

```text
Consensus and dissent are useful as review signals when translated into Pantheon
roles, rites, evidence gaps, contradictions and gates.
```

Refused:

```text
Pythia as Pantheon dependency.
Pythia as Pantheon oracle.
Pythia-style predictions as truth, proof, approval or memory.
Swarm consensus as Zeus arbitration.
Agent-readable state as task authorization.
SSE state stream as Pantheon runtime state.
```

To verify:

```text
Whether `governance_state_view` should become a dedicated candidate document,
be folded into CARD_STACK_MODEL.md, or be expressed only in an adapter note.
```

To arbitrate:

```text
Whether the future read-only MCP policy surface should expose a governance-state view,
or only narrower status checks.
```

## Boundary with CARD_STACK_MODEL.md

`CARD_STACK_MODEL.md` already defines the cockpit grammar: cards, scenes, decks, constellation, navigation and gates.

This review does not replace that model.

The candidate relationship is:

```text
CARD_STACK_MODEL.md defines the visible grammar.
governance_state_view would define the serializable read model.
```

The first is UX/governance grammar.

The second, if ever promoted, would be a read-only governance projection that may feed a cockpit, adapter or MCP policy surface.

Neither one implements a UI, runtime, renderer, state machine, approval engine, memory engine, connector, scheduler or action mechanism.

## Boundary with CAPABILITY_PLACEMENT.md

If a governance-state view only displays current status, it belongs to the exposure surface or read-only policy surface as a projection.

If it affects truth, memory, approval, scope, external effect or canonical status, Pantheon governs the rule and the effect must stop at a visible gate.

The view itself must not authorize execution.

## Minimal safe invariant

```text
A governance-state view may expose what is currently known, proposed, blocked or awaiting decision.
It must not decide what is true, approved, remembered or allowed to act.
```

## Possible next document

A later document may be useful:

```text
docs/governance/GOVERNANCE_STATE_VIEW.md
```

Only create it if the concept needs promotion from reference distillation into candidate support doctrine.

Until then, this review remains an external reference / support review.

The validated remains.
