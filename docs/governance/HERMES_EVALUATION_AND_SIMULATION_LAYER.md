# Hermes Evaluation and Simulation Layer

Status: active support doctrine — Hermes-side evaluation and simulation boundary.

This document defines how Pantheon Next frames a possible Hermes-side evaluation and simulation layer.

It does not implement Hermes.

It does not install Future AGI.

It does not add a runtime, simulator, evaluator, provider router, scheduler, queue, worker, gateway, observability backend, MCP layer, A2A layer, automatic approval system, automatic memory system or self-improvement loop.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

The Hermes Evaluation and Simulation Layer is a candidate execution capability that may later allow Hermes to test candidate actions before real delivery, mutation, memory or doctrine effects.

Pantheon defines the legitimacy frame.

Hermes may execute the bounded test.

OpenWebUI may expose the result.

The human decides when material risk remains.

## Relationship to Pre-Execution Simulation

`PRE_EXECUTION_SIMULATION.md` defines the governance pattern.

This document defines the Hermes-side boundary for that pattern.

The governing rule remains:

```text
A simulation can reveal failure modes.
It cannot authorize execution.
```

The Hermes layer exists only to produce reviewable signals.

It must not convert simulation, evaluation, guardrails or optimization into approval.

## Relationship to Future AGI

Future AGI is treated as an external reference and optional inspiration source.

Useful concepts:

```text
simulation
evaluation
trajectory review
guardrail signal
trace summary
improvement candidate
```

Rejected imports:

```text
Future AGI as Pantheon runtime
Future AGI gateway as Pantheon provider router
Future AGI tracing backend as Pantheon observability backend
Future AGI optimization as self-improvement
Future AGI eval pass as approval
Future AGI simulation pass as delivery authorization
```

See:

- `docs/governance/reference_reviews/FUTURE_AGI.md`;
- `docs/governance/PRE_EXECUTION_SIMULATION.md`;
- `docs/governance/DISTILLATION_REGISTRY.md`;
- `docs/governance/REJECTED_PATTERNS.md`;
- `docs/governance/TENSIONS_AND_RISKS.md`.

## Layer placement

| Layer | Responsibility |
|---|---|
| Pantheon Next | defines scope, risk, approval ceiling, evidence expectations and memory rule |
| Hermes Agent | may execute bounded simulation or evaluation under Task Contract |
| OpenWebUI | exposes simulation request, status, summary, risks and User Decision Gate |
| External references | may inspire methods but do not authorize adoption |

## Candidate capability set

A future Hermes evaluation and simulation capability may include:

```text
simulation_runner
persona_suite
scenario_set
trajectory_eval
guardrail_signal
trace_summary
simulation_evidence_summary
improvement_candidate_builder
capability_gap_reporter
```

These are candidate capability names.

They are not implemented components.

They are not Pantheon modules.

They are not OpenWebUI tools.

They are not approved Hermes skills.

## Use when

Consider this layer only when a task involves one or more of:

```text
external transmission
client-facing professional communication
repository mutation
protected governance files
memory proposal
prompt, skill or workflow update
provider or gateway configuration
ambiguous recipient interpretation
professional liability
unanswerable or insufficient evidence risk
high-impact automation proposal
```

Common examples:

```text
client email may imply quote validation
site note may imply reception or acceptance
repository patch may imply implementation
prompt change may alter future governance behavior
memory candidate may overgeneralize project facts
external API action may create irreversible effect
```

## Do not use when

Do not require this layer for:

```text
simple rewrite
translation
low-risk summary
minor wording polish
internal brainstorm
single-source excerpt extraction
low-risk draft without transmission
```

If the simulation cost creates more governance noise than value, use a lighter review path.

## Required Task Contract fields

A Hermes simulation or evaluation run must be bounded by a Task Contract or equivalent review note.

Recommended fields:

```text
task_id
candidate_action
candidate_output
intended_recipient_or_effect
risk_level
approval_ceiling
scope
excluded_scope
allowed_sources
excluded_sources
allowed_tools
forbidden_tools
simulation_required
simulation_goal
scenario_set
persona_set_if_any
evaluation_criteria
guardrail_checks_if_any
expected_outputs
evidence_pack_requirements
memory_rule
user_decision_gate_triggers
```

The Task Contract must be narrow enough that Hermes can refuse or report a capability gap when the request exceeds scope.

## Required outputs

Hermes may return:

```text
Simulation Result Candidate
Trajectory Evaluation Candidate
Guardrail Signal
Trace Summary
Risk Note
Capability Gap
Improvement Candidate
Evidence Pack Candidate
```

Required output fields:

```text
linked_task_contract
candidate_tested
scenario_set_used
inputs_considered
inputs_excluded
result_status
risks_detected
limitations
approval_impact
memory_impact
external_effect_impact
recommended_next_action
```

## Result status vocabulary

Allowed status values should stay aligned with `PRE_EXECUTION_SIMULATION.md`:

```text
not_required
proposed
blocked_by_scope
blocked_by_approval
ready_for_external_execution
completed_no_material_risk
completed_with_reserve
risk_detected
source_gap_detected
scope_gap_detected
external_effect_risk_detected
memory_risk_detected
inconclusive
failed
superseded
```

These are governance signals.

They are not runtime states.

They do not execute anything.

## Evidence interpretation

Hermes simulation output may support an Evidence Pack Candidate as:

```text
scenario summary
failure mode
risk note
trajectory note
guardrail signal
capability gap
improvement candidate
approval implication
memory implication
```

It must not become:

```text
approval
proof by itself
Registre Probatoire entry
delivery authorization
repository merge authorization
doctrine mutation
provider routing authority
```

Raw traces, scratchpads, hidden debates, secrets, unredacted private payloads and provider credentials must not be copied into Evidence Packs.

## OpenWebUI exposure

OpenWebUI may expose:

```text
simulation requested
simulation not required
simulation running externally
simulation completed
simulation failed
simulation inconclusive
risk detected
capability gap
approval required
User Decision Gate required
```

OpenWebUI may display:

```text
candidate tested
scenario summary
risk summary
limitations
Evidence Pack Candidate link
recommended next action
user decision options
```

OpenWebUI must not:

```text
run simulation by UI state alone
approve output by displaying a pass status
hide failed or inconclusive simulations
promote memory from simulation
send or publish based on simulation result
turn simulation status into governance truth
```

## Approval boundary

Simulation may affect approval review.

It does not grant approval.

Hermes must report approval implications such as:

```text
no approval needed beyond draft review
approval required before transmission
approval required before repository mutation
approval required before memory proposal
approval required before prompt, skill or workflow change
approval required before external tool or provider change
```

Hermes must not infer approval from:

```text
simulation pass
score threshold
guardrail pass
successful run
user silence
repeated pattern
model confidence
```

## Memory boundary

Hermes may propose a Register Candidate only when the Task Contract allows it.

Simulation output is not memory.

Repeated simulation results are not a Registre Probatoire entry.

A simulation-derived Register Candidate must identify:

```text
claim
scope
source_or_evidence_link
risk
approval_requirement
revocation_or_supersession_path
```

## Improvement Candidate boundary

An Improvement Candidate is the only valid translation of optimization output.

It may propose:

```text
prompt adjustment
skill constraint
workflow note
evidence requirement
User Decision Gate trigger
example update
rejected-pattern note
```

It must not perform:

```text
automatic prompt promotion
automatic skill activation
automatic workflow change
automatic doctrine mutation
automatic memory promotion
automatic provider change
automatic repository merge
```

## Capability gap rule

Hermes must surface a capability gap when it cannot perform a safe bounded simulation.

Examples:

```text
missing source
missing scenario set
missing approval ceiling
scope exceeds contract
private data outside authorized scope
external tool not allowed
required evaluator unavailable
risk cannot be tested safely
```

A capability gap is a governance signal, not a failure to hide.

## Forbidden drift

This layer must never become:

```text
Pantheon runtime
Hermes installation guide
OpenWebUI execution tool
provider router
gateway
observability backend
scheduler
queue
worker manager
MCP or A2A layer
simulation backend owned by Pantheon
automatic approval engine
automatic memory engine
self-improvement loop
```

If Hermes simulation can approve its own result, the boundary has failed.

If OpenWebUI can trigger unbounded simulation, the boundary has failed.

If Pantheon must run the simulator, the boundary has failed.

## Final rule

```text
Pantheon defines why a candidate must be tested.
Hermes may test it under contract.
OpenWebUI shows the test and the decision surface.
The human decides when risk remains material.
```
