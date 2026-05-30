# Pre-Execution Simulation

Status: active support doctrine — governed pre-execution stress test pattern.

This document defines how Pantheon Next may use simulation results before high-risk execution or delivery.

It does not add a runtime.

It does not add an agent.

It does not add a simulator, evaluator, scheduler, queue, provider router, observability backend, MCP layer, A2A layer, hidden workflow runner, automatic approval system, automatic memory system or self-improvement loop.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pre-execution simulation is a governed method for stress-testing a candidate action before it becomes execution, delivery, transmission, memory or doctrine.

It is useful when an output may look correct but fail under realistic pressure:

```text
ambiguous client interpretation
contradictory third-party response
missing source
scope expansion
external transmission risk
professional liability
memory overreach
repository mutation risk
prompt, skill or workflow change
```

Pantheon uses simulation to reveal risk before action.

Pantheon does not use simulation to replace approval.

## Core rule

```text
A simulation can reveal failure modes.
It cannot authorize execution.
```

Simulation output is a candidate signal.

It may support an Evidence Pack.

It may trigger a User Decision Gate.

It must not approve, execute, transmit, merge, promote memory or mutate doctrine by itself.

## Relationship to Future AGI

This pattern is partly inspired by Future AGI's reliability framing around simulation, evaluation, guardrails, tracing and optimization.

The Pantheon interpretation is intentionally narrower:

```text
simulate -> evaluate -> summarize -> expose -> decide
```

Not:

```text
simulate -> optimize -> auto-improve -> auto-promote
```

Future AGI may inspire external Hermes-side simulation or evaluation candidates.

It must not become a Pantheon runtime, gateway, observability backend, provider router, self-improvement loop or approval authority.

See `docs/governance/reference_reviews/FUTURE_AGI.md`.

## When to use

Pre-execution simulation should be considered when a task touches:

```text
C3 canonical governance review
C4 trust-boundary review
C5 critical review
external write or transmission
professional responsibility
repository mutation
protected governance files
memory promotion
scope expansion
provider or gateway configuration
prompt, skill or workflow update
high-risk automation proposal
```

It is especially useful when the main risk is not whether the candidate is fluent, but how it behaves under pressure.

## Professional examples

Architecture and project-management examples:

```text
A client email may be read as approval of a disputed quote.
A contractor may answer a clarification request by expanding scope.
A CCTP gap may make a draft look stronger than the evidence allows.
A recovery-work note may imply acceptance of defective work.
A site-meeting summary may create unintended contractual framing.
```

Governance and repository examples:

```text
A documentation patch may imply implementation.
A reference review may be mistaken for dependency adoption.
A score may be treated as approval.
A trace may be treated as proof.
A recurring observation may be treated as Canonical Memory.
```

## Simulation inputs

A simulation request should be bounded by a Task Contract or review note when the task is non-trivial.

Recommended inputs:

```text
candidate_action
candidate_output
intended_recipient_or_effect
task_scope
excluded_scope
allowed_sources
risk_level
approval_ceiling
memory_rule
simulation_goal
personas_or_scenarios
success_and_failure_conditions
expected Evidence Pack summary
```

Inputs must not include secrets, private payloads, credentials or broad dossier material unless explicitly scoped and approved.

## Simulation scenarios

Useful scenario types:

```text
recipient_misinterpretation
source_gap
contradictory_reply
scope_expansion
unsupported_claim
professional_liability
external_effect
memory_overreach
privacy_leak
repository_mutation
provider_or_gateway_drift
prompt_or_skill_regression
unanswerable_question
```

Simulation should use the smallest scenario set that can reveal the material risk.

It should not become an unlimited adversarial theatre.

## Hermes boundary

Hermes may execute a simulation only as an external runtime capability under Task Contract.

Hermes may produce:

```text
Simulation Result Candidate
Trajectory Evaluation Candidate
Guardrail Signal
Risk Note
Capability Gap
Improvement Candidate
Evidence Pack Candidate
```

Hermes must not:

```text
approve the candidate
execute the real action because simulation passed
send or publish the output
merge repository changes
promote memory
mutate doctrine
install tools or skills
broaden scope silently
```

Hermes completion does not mean Pantheon approval.

## OpenWebUI boundary

OpenWebUI may expose:

```text
simulation requested
simulation not required
simulation running externally
simulation completed
simulation failed
simulation inconclusive
simulation risk detected
simulation blocked by scope
simulation blocked by approval
User Decision Gate required
```

OpenWebUI may display a simulation summary, scenario list, risk note, limitation, Evidence Pack Candidate reference and user decision options.

OpenWebUI must not display simulation pass as approval.

OpenWebUI must not run simulation by UI state alone.

OpenWebUI must not hide failed or inconclusive simulation results.

## Evidence Pack impact

When simulation affects legitimacy, the Evidence Pack may include a simulation entry.

Recommended structure:

```text
simulation_id
linked_task_contract
simulation_goal
candidate_tested
scenario_set
persona_or_edge_case_summary
inputs_considered
excluded_inputs
result_status
risks_detected
limitations
trajectory_notes
approval_impact
memory_impact
User_Decision_Gate_impact
recommended_next_action
```

Allowed evidence:

```text
scenario summary
failure modes
risk notes
capability gaps
concise rationale
result status
approval implication
memory implication
```

Forbidden evidence:

```text
hidden chain-of-thought
raw scratchpad
raw autonomous debate
unredacted private payloads
secrets or credentials
runtime state required to resume execution
provider routing logs as proof
simulation transcript as approval
```

## Result statuses

Recommended simulation statuses:

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

These statuses are governance signals.

They are not runtime states.

They do not execute anything.

## Evaluation and scoring

Simulation may include evaluation scores, guardrail results or trajectory checks.

Those signals must be interpreted conservatively:

```text
evaluation score -> review signal
guardrail pass -> risk signal only
trajectory check -> execution-quality signal
simulation pass -> candidate confidence only
simulation failure -> possible escalation trigger
```

They must not become:

```text
C0-C5 approval
proof by themselves
delivery authorization
memory promotion
doctrine mutation
provider routing authority
```

## Improvement Candidates

A simulation may produce an Improvement Candidate.

An Improvement Candidate should identify:

```text
observed_failure
simulation_scenario
candidate_affected
proposed_change
expected_benefit
risk_note
affected_scope
approval_requirement
memory_implication
rollback_or_supersession_path
```

An Improvement Candidate must not become:

```text
automatic merge
automatic prompt promotion
automatic skill activation
automatic workflow update
automatic doctrine mutation
automatic memory promotion
automatic provider change
```

## User Decision Gate triggers

A simulation should trigger or support a User Decision Gate when:

```text
simulation detects material risk
simulation contradicts apparent output quality
simulation is inconclusive but external effect remains high
simulation suggests scope expansion
simulation suggests memory promotion
simulation suggests prompt, skill, policy or workflow change
simulation result conflicts with available evidence
simulation score is being treated as approval
simulation requires private data outside current scope
```

User-facing options may include:

```text
continue_as_draft
continue_with_reserve
request_missing_source
narrow_scope
split_into_variants
revise_candidate
run_bounded_followup_simulation
escalate_approval
block_delivery
block_transmission
reject_memory_candidate
allow_improvement_candidate_review
```

## Relationship to Task Contracts

A Task Contract may require pre-execution simulation for high-risk tasks.

It may define:

```text
simulation_required
simulation_goal
scenario_set
allowed_inputs
excluded_inputs
approval_ceiling
expected Evidence Pack entry
User Decision Gate triggers
memory rule
optimization_candidate_rule
```

It must not define:

```text
automatic simulation execution inside Pantheon
scheduler behavior
queue behavior
provider routing
hidden workflow execution
automatic approval after simulation pass
automatic memory promotion from simulation
```

## Relationship to approvals

Simulation can support approval review.

It does not grant approval.

C3 and above should treat simulation as one possible evidence input when the task risk justifies it.

C4 and C5 should require explicit human or governed approval when simulation affects external effect, trust boundary, professional liability, protected files, runtime configuration, memory or doctrine.

## Relationship to memory

Simulation output is not memory.

A simulation may support a Memory Candidate only when:

```text
the claim is explicit
the scope is defined
the evidence link is clear
the risk is recorded
the approval path is declared
```

Simulation repetition does not create Canonical Memory.

Simulation confidence does not create Canonical Memory.

Simulation-derived memory must follow `MEMORY.md` and `SCOPE_ISOLATION.md`.

## Forbidden drift

Pre-execution simulation must never become:

```text
Pantheon runtime
simulation backend
agent runtime
hidden workflow runner
scheduler
queue
provider router
automatic approval engine
automatic memory promoter
self-improvement loop
prompt auto-optimizer
guardrail authority
observability backend
MCP or A2A layer
```

If simulation pass becomes permission to act, the boundary has failed.

If simulation output becomes proof without governed evidence, the boundary has failed.

If simulation failure mutates prompts, skills, memory, doctrine or workflows automatically, the boundary has failed.

## Final rule

```text
Simulation tests the candidate.
Evidence frames the result.
ZEUS arbitrates status and procedure.
OpenWebUI exposes the decision surface.
The human decides when risk remains material.
Only the validated remains.
```
