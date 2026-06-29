# Method Hermes Handoff Template

Status: candidate support template — bounded handoff template for projecting Method Cards into Hermes execution.

Runtime status: non-executable.

This document defines a reviewable template for handing a Method Card or Method Proposal Candidate from Pantheon to Hermes.

It does not implement a Hermes skill, profile, router, queue, scheduler, workflow engine, approval engine, memory engine, connector, schema, test or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A Method Card structures work. Hermes executes only a bounded task. Pantheon keeps status, proof, memory, scope, approval and external-action boundaries.

This template answers:

```text
Why is Hermes being called?
Which Method Card structures the call?
Which sources may enter?
Which outputs may return?
Which outputs are forbidden?
Where must Hermes stop?
Which gate appears if the result becomes consequential?
```

The template is a governance artifact, not an executable configuration.

## Relationship with existing doctrine

This document does not replace Task Contracts, Capability Placement or the general governed execution handoff boundary.

It specializes the handoff for one use case:

```text
A Role has proposed or selected a Method Card for a Task,
and Hermes may execute a bounded candidate-producing step.
```

It keeps the existing invariant:

```text
Runtime completion does not mean governance approval.
Task success does not mean truth, proof, memory or professional validation.
Trace is not Evidence Pack.
Runtime state is not Pantheon memory.
```

## When to use this template

Use this template when:

```text
a Method Card structures a bounded Hermes task;
a Method Proposal Candidate has been accepted internally;
a task needs evidence review, cautious drafting, contradiction search, source qualification or bounded synthesis;
a run must be rerun because a threshold failed;
a role needs Hermes to produce a Result Candidate under explicit limits.
```

Do not use it when:

```text
the task is only a human decision;
the expected effect is direct external action;
the source perimeter is unclear;
the approval ceiling is missing;
the work would require professional authority rather than candidate production;
confidential or provider-sensitive material would be exposed without explicit authorization;
the runtime is being asked to validate, approve, send, file, remember or instruct.
```

## Two-level handoff

Pantheon should distinguish the proposal from the executable instruction.

### 1. Handoff Candidate

A Handoff Candidate explains why a Hermes call may be useful.

It is still a candidate. It does not execute.

```yaml
handoff_candidate:
  id:
  run_ref:
  task_ref:
  proposing_role:
  detected_problem:
  failed_threshold:
  current_method:
  proposed_method:
  reason:
  expected_gain:
  expected_cost: low | medium | high
  density_cost: low | medium | high
  source_perimeter:
  evidence_delta:
  scope_delta:
  memory_delta:
  external_action_delta:
  approval_ceiling:
  gate_required:
  allowed_runtime:
  forbidden_effects:
  status: proposed | accepted_internal | needs_zeus | needs_human_gate | rejected
```

### 2. Executable Hermes Handoff

An Executable Hermes Handoff is the bounded instruction that Hermes may execute.

```yaml
executable_hermes_handoff:
  id:
  handoff_candidate_ref:
  task_contract:
    objective:
    expected_result_candidate:
    professional_context:
    approval_ceiling:
    stop_condition:
  context_pack:
    project_ref:
    run_ref:
    task_ref:
    subject:
    phase:
    constraints:
    known_decisions:
    open_questions:
  method:
    method_card_ref:
    method_name:
    method_family:
    fidelity_check:
    fitness_check:
  sources:
    allowed_sources:
    required_sources:
    forbidden_sources:
    missing_sources:
    source_minimization_rule:
  outputs:
    allowed_outputs:
    required_output_shape:
    forbidden_outputs:
    evidence_pack_candidate_required: true | false
    trace_required: true | false
  gates:
    gate_if:
    gate_type:
    required_actor:
  runtime:
    runtime: hermes
    profile_hint:
    provider_constraints:
    cost_limit:
    latency_limit:
    retry_limit:
  return_contract:
    result_candidate:
    evidence_pack_candidate:
    uncertainty_list:
    contradiction_list:
    trace_references:
    stop_reason:
```

This is a template, not a schema.

If it later becomes machine-checkable, that requires a separate protected-path review.

## Minimum handoff fields

A Hermes handoff is inadmissible if it lacks any of these fields:

```text
objective;
expected candidate output;
source perimeter;
allowed outputs;
forbidden outputs;
approval ceiling;
stop condition;
return contract.
```

For professional architecture use, add:

```text
project or dossier;
phase;
mission scope;
source status;
external-action ceiling;
client / enterprise / authority effect if any.
```

## Approval ceiling

The approval ceiling tells Hermes what the result may become at most.

Allowed ceilings:

```text
draft_only;
internal_analysis_candidate;
evidence_pack_candidate;
question_list;
comparison_table_candidate;
wording_candidate;
ready_for_human_review;
blocked_until_source;
blocked_until_gate.
```

Forbidden ceilings:

```text
validated_truth;
professional_approval;
client_decision;
enterprise_instruction;
visa_issued;
filing_done;
payment_approved;
canonical_memory;
external_transmission.
```

## Stop conditions

A stop condition must be explicit.

Typical stop conditions:

```text
required source missing;
source conflict unresolved;
claim cannot be supported;
mission boundary unclear;
external action would be required;
confidence below threshold;
provider / runtime failure changes adequacy;
cost or latency ceiling reached;
sensitive data exposure unresolved;
output would imply professional validation.
```

When a stop condition occurs, Hermes should return:

```text
partial Result Candidate if useful;
Evidence Pack Candidate if any;
missing source or question list;
stop reason;
next recommended gate or human question.
```

It should not guess past the stop condition.

## Output discipline

Hermes may return candidates.

```text
Result Candidate;
Evidence Pack Candidate;
contradiction list;
uncertainty list;
source table;
safer wording candidate;
comparison table candidate;
question list;
trace references.
```

Hermes must not return final effects.

```text
final truth;
professional validation;
approval;
external send;
filing;
payment instruction;
enterprise instruction;
client decision;
canonical memory promotion;
reserve lifting;
fault recognition.
```

## Evidence Pack Candidate

An Evidence Pack Candidate is required when the returned result may support:

```text
truth claim;
client-facing answer;
enterprise-facing answer;
administrative filing;
payment or quote opinion;
reception or reserve position;
canonical memory;
phase transition;
professional commitment.
```

It should include:

```yaml
evidence_pack_candidate:
  assertions:
    - assertion:
      source_ref:
      source_status:
      confidence:
      contradiction:
      allowed_reuse_scope:
  missing_evidence:
  uncertainty:
  stop_reason:
```

This remains candidate until reviewed under Pantheon evidence and gate rules.

## Gate mapping

The handoff must declare what gate appears if Hermes returns a usable candidate.

| Effect detected | Gate |
|---|---|
| external email or message | external_commitment_gate |
| client approval or choice | client_decision_gate |
| enterprise instruction | enterprise_instruction_gate |
| administrative filing | filing_gate |
| visa / EXE position | visa_commitment_gate |
| payment, quote or financial recommendation | payment_or_quote_gate |
| reception or reserve lifting | reception_gate |
| mission extension | mission_scope_gate |
| canonical memory | memory_promotion_gate |
| fault or responsibility statement | responsibility_gate |

If no gate is required, the handoff should say why:

```text
internal only;
reversible;
low risk;
no memory effect;
no external action;
no professional commitment.
```

## Cost and density review

A rerun is not free. Pantheon should check whether the expected gain justifies the cost.

```text
low cost:
rewrite with safer wording;
source table;
assertion mapping;
short contradiction check.

medium cost:
contractual decomposition;
quote variation review;
CERFA field review;
site observation review.

high cost:
full CR reconstruction;
multi-source contradiction analysis;
phase-gate review;
large MoA review;
long dossier synthesis.
```

A high-cost handoff may require Zeus review even if the output remains internal.

## MoA runtime pattern note

If the selected Method Card is a runtime pattern such as Hermes MoA Review Mode, the handoff must add:

```text
provider exposure review;
source minimization;
cost / latency ceiling;
why single-model execution is insufficient;
disagreement notes required;
aggregator output remains Result Candidate;
no higher authority status.
```

MoA is a runtime pattern, not a truth upgrade.

## Example A — source conflict in complementary quote

### Handoff Candidate

```yaml
handoff_candidate:
  proposing_role: ARGOS
  detected_problem: quote amount conflicts with payment situation
  failed_threshold: source precedence
  current_method: contractual_decomposition
  proposed_method: authority_qualification
  expected_gain: identify candidate source priority
  expected_cost: medium
  evidence_delta: resolves_conflict
  scope_delta: clarifies_scope
  memory_delta: none
  external_action_delta: none if internal; opens_gate before recommendation
  approval_ceiling: evidence_pack_candidate
  gate_required: false internally; true before transmission
  forbidden_effects:
    - payment approval
    - quote validation
    - client recommendation
    - enterprise instruction
```

### Executable Hermes Handoff

```yaml
executable_hermes_handoff:
  task_contract:
    objective: compare conflicting financial sources
    expected_result_candidate: contradiction table and candidate source priority
    approval_ceiling: evidence_pack_candidate
    stop_condition: required source missing or conflict not resolvable from provided sources
  context_pack:
    project_ref: project id
    run_ref: complementary_quote_review
    task_ref: analyze source conflict
    phase: chantier / ACT / DET as applicable
    constraints:
      - do not approve payment
      - do not validate quote
  method:
    method_card_ref: authority_qualification
    fidelity_check: compare only source authority and conflicts
    fitness_check: method is fit only if sources can be identified and dated
  sources:
    allowed_sources:
      - quote
      - payment situation
      - signed amendment
      - relevant emails
    required_sources:
      - quote
      - at least one conflicting source
    forbidden_sources:
      - unsourced memory
      - guessed contract clauses
    source_minimization_rule: only include excerpts necessary to compare amount, object, date and authority
  outputs:
    allowed_outputs:
      - conflict table
      - candidate source priority
      - uncertainty list
      - Evidence Pack Candidate
    forbidden_outputs:
      - payment approval
      - quote validation
      - external wording
      - enterprise instruction
    evidence_pack_candidate_required: true
    trace_required: true
  gates:
    gate_if: result will be sent or used for payment recommendation
    gate_type: payment_or_quote_gate
    required_actor: human
  runtime:
    runtime: hermes
    profile_hint: evidence-review
    retry_limit: 1
  return_contract:
    result_candidate: required
    evidence_pack_candidate: required
    uncertainty_list: required if any source is weak
    contradiction_list: required
    trace_references: required
    stop_reason: required if incomplete
```

## Example B — risky wording before email

```yaml
handoff_candidate:
  proposing_role: THEMIS
  detected_problem: draft says "we validate"
  failed_threshold: mission scope / external commitment
  proposed_method: mission_scope_guard
  expected_gain: produce safer wording candidate
  evidence_delta: weakens_claim
  scope_delta: requires_mission_gate
  external_action_delta: opens_gate
  approval_ceiling: wording_candidate
  gate_required: true before send
```

Hermes may produce safer wording.

Hermes may not send the email.

## Example C — CERFA field as claim

```yaml
handoff_candidate:
  proposing_role: ARGOS
  detected_problem: surface field filled from plan label without calculation source
  failed_threshold: field-as-claim proof
  proposed_method: cerfa_field_claim_review
  expected_gain: separate candidate value from filing-ready value
  evidence_delta: raises_question
  external_action_delta: opens_gate before filing
  approval_ceiling: field_value_candidate
  gate_required: true before filing
```

Hermes may return field value candidate + missing evidence.

Hermes may not mark the form signature-ready.

## Bad handoffs

### Bad handoff — vague rerun

```text
Do better and make the answer more reliable.
```

Why it fails:

```text
no method;
no source perimeter;
no forbidden outputs;
no approval ceiling;
no stop condition.
```

### Bad handoff — hidden external effect

```text
Prepare and send the corrected email.
```

Why it fails:

```text
preparation and external action are collapsed;
Gate is bypassed;
Hermes is asked to act, not only produce a candidate.
```

### Bad handoff — method as validation

```text
Run probative_review and validate the conclusion.
```

Why it fails:

```text
method success is confused with proof;
proof review is confused with approval;
human and Zeus gates are bypassed.
```

## Review checklist

Before allowing Hermes execution, check:

```text
Is the objective bounded?
Is the source perimeter explicit?
Are allowed outputs explicit?
Are forbidden outputs explicit?
Is the approval ceiling explicit?
Is there a stop condition?
Is the expected return shape explicit?
Is an Evidence Pack Candidate required if the result may become consequential?
Is a gate declared if external action, memory, approval or professional commitment may follow?
Is Hermes still only the runtime?
```

If any answer is no, the handoff remains inadmissible.

## Final invariant

```text
A Method Hermes Handoff lets Hermes work.
It does not let Hermes decide.
It does not let Hermes validate.
It does not let Hermes remember.
It does not let Hermes act externally.
```

The validated remains.
