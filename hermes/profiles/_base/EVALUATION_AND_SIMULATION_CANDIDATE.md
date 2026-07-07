# Hermes Evaluation and Simulation Candidate

Status: Hermes capability candidate template — not installed, not implemented.

This document describes a possible Hermes-side evaluation and simulation capability.

It does not install a tool.

It does not install Future AGI.

It does not create a Hermes skill.

It does not create a Pantheon runtime, OpenWebUI tool, simulator, evaluator, queue, scheduler, provider router, gateway, observability backend, MCP layer, A2A layer, automatic approval system, automatic memory system or self-improvement loop.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

This candidate describes how Hermes might later execute bounded simulations and evaluations for high-risk candidate outputs.

It is intended to support:

```text
pre-execution simulation
trajectory evaluation
guardrail signaling
risk note generation
Evidence Pack Candidate preparation
Improvement Candidate drafting
```

It does not authorize actual execution, installation or dependency adoption.

## Candidate identity

```yaml
capability_candidate: hermes_evaluation_and_simulation
owner_layer: hermes
status: not_installed_candidate
pantheon_role: none
canonical_authority: none
governed_by:
  - docs/governance/HERMES_INTEGRATION.md
  - docs/governance/PRE_EXECUTION_SIMULATION.md
  - docs/governance/HERMES_INTEGRATION.md
  - docs/governance/TASK_CONTRACTS.md
  - docs/governance/EVIDENCE_PACK.md
  - docs/governance/APPROVALS.md
  - docs/governance/MEMORY.md
  - docs/governance/SCOPE_ISOLATION.md
  - docs/governance/EXTERNAL_TOOLS_POLICY.md
  - docs/governance/OPENWEBUI_INTEGRATION.md
  - docs/governance/EXTERNAL_TOOLS_POLICY.md
```

## Candidate components

The candidate capability may be decomposed into:

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

These are design terms only.

They are not implemented classes, tools, workers or services.

## Component responsibilities

### simulation_runner

Runs a bounded simulation against one candidate action or output.

Inputs:

```text
candidate_action
candidate_output
simulation_goal
scenario_set
allowed_context
excluded_context
approval_ceiling
memory_rule
```

Outputs:

```text
Simulation Result Candidate
risk_detected status
limitations
recommended_next_action
```

Must not:

```text
execute real action
send output
publish output
merge patch
promote memory
broaden scope
```

### persona_suite

Defines optional synthetic recipient or stakeholder viewpoints.

Examples:

```text
client_reads_as_approval
contractor_reads_as_scope_validation
reviewer_checks_source_gap
admin_reads_as_submission_ready
professional_checks_liability
```

Personas are scenario devices.

They are not users.

They are not agents.

They do not create authority.

### scenario_set

Defines the risk situations to test.

Examples:

```text
recipient_misinterpretation
scope_expansion
source_gap
unsupported_claim
external_effect
memory_overreach
repository_mutation
prompt_or_skill_regression
```

Scenario sets must remain minimal.

Hermes should not expand scenarios indefinitely without Task Contract revision.

### trajectory_eval

Reviews the path, not just the final text.

It may inspect:

```text
source selection
assumption handling
scope preservation
tool-use sequence
risk escalation
approval boundary
memory boundary
```

It must not act as an LLM judge with final authority.

### guardrail_signal

Reports whether a candidate appears to violate a declared policy, scope, memory rule, privacy rule, external tool rule or approval ceiling.

A guardrail signal is a risk note.

It is not policy authority.

### trace_summary

Summarizes governance-relevant execution observations.

Allowed:

```text
what was tested
which scenarios were used
which sources were considered
which risks appeared
what was excluded
what remains uncertain
```

Forbidden:

```text
raw chain-of-thought
raw scratchpad
hidden debate transcript
secrets
unredacted private payloads
provider credentials
full runtime logs as proof
```

### simulation_evidence_summary

Formats the simulation output so it can support an Evidence Pack Candidate.

It should map:

```text
candidate -> scenario -> observed failure mode -> risk -> limitation -> approval implication
```

It must not claim the Evidence Pack is approved.

### improvement_candidate_builder

Transforms a detected weakness into a proposed improvement.

Allowed candidates:

```text
revise draft wording
add source requirement
add User Decision Gate trigger
add evidence checklist item
add prompt constraint
add skill anti-pattern
add rejected-pattern note
```

Forbidden changes:

```text
automatic prompt promotion
automatic skill activation
automatic workflow change
automatic doctrine mutation
automatic memory promotion
automatic provider change
automatic repository merge
```

### capability_gap_reporter

Reports that the bounded simulation cannot be safely executed.

Gap examples:

```text
missing allowed source
missing approval ceiling
missing scenario set
scope exceeds Task Contract
private data outside allowed context
external evaluator unavailable
risk cannot be safely simulated
```

## Required input envelope

A Hermes evaluation and simulation candidate run requires:

```yaml
required_inputs:
  task_contract: required
  candidate_action_or_output: required
  simulation_goal: required
  risk_level: required
  approval_ceiling: required
  memory_rule: required
  allowed_context: required
  excluded_context: required
  scenario_set: required
  evidence_requirements: required
  user_decision_gate_policy: required
```

## Optional input envelope

Optional inputs:

```yaml
optional_inputs:
  persona_suite: optional
  guardrail_checks: optional
  trajectory_eval_criteria: optional
  external_eval_tool_reference: optional
  expected_output_schema: optional
  example_failure_modes: optional
```

External eval tools remain external references unless separately approved.

## Forbidden inputs

A Hermes evaluation and simulation candidate must not receive:

- unbounded OpenWebUI Knowledge;
- raw OpenWebUI database or vector-store access;
- unrelated project context;
- unrestricted production traces;
- unredacted confidential payloads without approval;
- provider secrets;
- repository write authority by default;
- memory promotion authority;
- doctrine mutation authority;
- approval authority.

## Required outputs

A valid candidate run should return:

```yaml
required_outputs:
  result_status: required
  candidate_tested: required
  scenario_set_used: required
  risks_detected: required
  limitations: required
  approval_impact: required
  memory_impact: required
  external_effect_impact: required
  evidence_summary: required
  recommended_next_action: required
```

Optional outputs:

```yaml
optional_outputs:
  trajectory_evaluation_candidate: optional
  guardrail_signal: optional
  capability_gap: optional
  improvement_candidate: optional
  user_decision_gate_recommendation: optional
```

## Output status vocabulary

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

These are governance-facing statuses.

They are not internal Hermes runtime states.

## Example output skeleton

```yaml
simulation_result_candidate:
  linked_task_contract: example-task-contract-id
  candidate_tested: client_email_candidate_v1
  result_status: risk_detected
  scenario_set_used:
    - recipient_misinterpretation
    - scope_expansion
    - source_gap
  risks_detected:
    - may imply professional validation
    - may exceed available evidence
    - may require User Decision Gate before transmission
  limitations:
    - simulated from bounded fictional context
    - no real contract interpretation performed
  approval_impact: transmission_blocked_pending_review
  memory_impact: no_memory_by_default
  external_effect_impact: no_send_without_approval
  recommended_next_action: revise_candidate_or_open_user_decision_gate
```

## Task Contract example

```yaml
task_contract:
  task_id: hermes-simulation-example-001
  task_type: pre_execution_simulation
  candidate_action: send_client_email
  risk_level: high
  approval_ceiling: no_external_transmission
  simulation_goal: detect whether the candidate email may imply validation
  allowed_context:
    - selected_quote_excerpt
    - selected_cctp_excerpt
    - reception_status_note
  excluded_context:
    - other_projects
    - unrelated_client_files
    - unverified_legal_conclusions
  scenario_set:
    - client_reads_as_approval
    - contractor_reads_as_scope_validation
    - later_dispute_uses_email_as_evidence
  expected_outputs:
    - Simulation Result Candidate
    - Evidence Pack Candidate entry
    - User Decision Gate recommendation if risk remains
  memory_rule: no_memory_by_default
```

## Execution discipline

If Hermes runs this candidate capability in a future approved sandbox, it should follow:

```text
smallest scenario set
read-only context
no production credentials
no external write
no automatic send
no memory write
no prompt promotion
no skill activation
no workflow update
clear Evidence Pack Candidate return
```

## OpenWebUI exposure candidate

OpenWebUI may later expose:

```text
simulation requested
simulation status
candidate tested
scenario summary
risk summary
limitations
recommended decision options
Evidence Pack Candidate link
```

OpenWebUI must not expose:

```text
button that runs unbounded simulation
simulation pass as approval
auto-send after simulation pass
auto-memory after repeated result
auto-optimize after score threshold
```

## Anti-patterns

Reject:

- Hermes simulation as approval;
- simulation pass as delivery permission;
- score threshold as prompt promotion;
- guardrail pass as policy approval;
- trace summary as Evidence Pack by itself;
- synthetic persona as real user proof;
- Improvement Candidate as automatic update;
- OpenWebUI simulation button bypassing Task Contract;
- Future AGI installation by implication;
- provider gateway adoption by convenience.

## Minimal sandbox test

A first sandbox test, if ever approved separately, should use:

```text
fictional task
read-only context
no production credentials
no protected files
no external write
no canonical memory writes
small scenario set
clear simulation result candidate
Evidence Pack Candidate return
User Decision Gate recommendation when risk remains
```

The sandbox output should be reviewed by Pantheon before any broader adoption.

## Final rule

```text
Hermes may test a candidate.
Hermes must not validate it.
Pantheon governs what the test means.
The human decides when risk remains material.
```
