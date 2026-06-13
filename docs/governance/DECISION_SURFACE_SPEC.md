# Decision Surface Specification

Status: candidate support specification — OpenWebUI-facing decision review surface, not runtime doctrine by itself.

This document defines a display and review pattern for consequential decisions.

It is inspired in part by external decision-card patterns reviewed in `SPICE_REFERENCE_DISTILLATION.md`, but it does not import Spice, depend on Spice, install Spice, create a decision runtime or create a new approval engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Canonical boundaries remain governed by:

- `STATUS.md`;
- `CAPABILITY_PLACEMENT.md`;
- `USER_DECISION_GATE.md`;
- `EVIDENCE_PACK.md`;
- `MODULAR_DOMAIN_REORIENTATION.md`;
- `DOMAIN_PACK_SPEC.md`.

If this document conflicts with those files, the canonical governance documents win.

## Purpose

A decision surface makes a consequential choice reviewable before the system acts, transmits, remembers, validates or escalates.

It answers:

```text
What is being decided?
What options exist?
What evidence supports them?
What is blocked?
What approval is required?
What remains candidate?
```

It prevents the cockpit from showing a smooth answer when the correct governance posture is a visible decision.

## What it is

A decision surface is an OpenWebUI-facing review object.

It may be rendered as a card, panel, modal, page section or structured output.

It may display:

- decision question;
- relevant scope;
- candidate options;
- selected recommendation candidate;
- rejected options;
- source and evidence references;
- objections;
- constraints;
- risk triggers;
- approval requirement;
- expected Hermes handoff;
- expected output candidate;
- expected Evidence Pack Candidate;
- memory and transmission effects.

## What it is not

A decision surface is not:

- a runtime;
- a hidden workflow;
- an approval engine;
- a source of truth;
- a Registre Probatoire entry;
- an Evidence Pack;
- canonical memory;
- a Task Contract by itself;
- a Hermes skill;
- an OpenWebUI Function specification;
- a queue item;
- a scheduler record;
- a command to execute.

## Trigger conditions

A decision surface should be shown when a task involves at least one consequential boundary:

```text
truth_status
source_conflict
scope_expansion
professional_risk
external_effect
transmission
memory_promotion
approval_uncertainty
role_conflict
canonical_effect
```

It may also appear before lower-risk work when the user explicitly asks to compare options.

## Relationship to User Decision Gate

A User Decision Gate is mandatory when unresolved tension requires human choice.

A decision surface is the presentation form that can expose that gate.

```text
User Decision Gate = governance trigger and decision requirement.
Decision surface = display and capture surface.
```

The surface must not hide the gate behind a recommendation.

## Minimum shape

```text
decision_surface_candidate:
  surface_id:
  status: candidate | to_verify | human_decision_required | blocked | approved_for_handoff
  linked_task_contract:
  linked_context_pack:
  linked_evidence_pack_candidate:
  decision_question:
  scope:
    dossier:
    domain:
    source_boundary:
    excluded_scope:
  trigger_conditions:
  candidate_options:
    - option_id:
      label:
      description:
      allowed_effect:
      forbidden_effects:
      required_approval:
      expected_result_candidate:
      expected_evidence_pack_candidate:
      memory_effect:
      transmission_effect:
      risk_level:
      source_refs:
      objections:
  selected_recommendation_candidate:
    option_id:
    rationale_summary:
    confidence_status: supported | partially_supported | unsupported | conflicted
  rejected_options:
    - option_id:
      rejection_reason:
  unresolved_tensions:
  approval_boundary:
  handoff_preview:
  user_decision_required:
  raw_artifact_refs:
```

This is a support shape, not an executable schema.

Any future executable schema belongs under `schemas/` and requires explicit approval.

## Display modes

A decision surface should support several views without changing governance status.

### Compact

The default professional view:

```text
Decision needed:
Recommended procedure:
Why:
Required approval:
Blocked effects:
Next safe action:
```

### Sources

Equivalent purpose: show why the output is reviewable.

```text
sources_view:
  source_refs:
  source_status:
  missing_sources:
  stale_sources:
  contradictory_sources:
  claims_without_source:
```

Rule:

```text
shown source != validated source
```

### Why

The rationale view must be concise and reviewable. It must not expose hidden chain-of-thought.

```text
why_view:
  selected_option:
  decisive_constraints:
  decisive_evidence:
  rejected_trade_offs:
  uncertainty:
  objections:
  what_would_change_the_decision:
```

### Details

Expanded audit card:

```text
details_view:
  decision_question:
  scope:
  trigger_conditions:
  candidate_options:
  evidence_refs:
  constraint_checks:
  approval_boundary:
  execution_boundary:
  memory_boundary:
  transmission_boundary:
  result_candidate_expectation:
  evidence_pack_candidate_expectation:
  outcome_observation_expectation:
```

### Raw

Developer / reviewer inspection only.

```text
raw_view:
  normalized_payload:
  trace_refs:
  runtime_refs:
  connector_refs:
  validation_warnings:
```

Raw data is not proof, doctrine or memory.

## Option statuses

Each option must state its consequence.

Recommended option statuses:

```text
safe_draft
continue_with_reserve
request_missing_source
narrow_scope
prepare_variants
escalate_approval
block_delivery
block_transmission
allow_candidate_handoff
reject_memory_candidate
allow_memory_candidate_review
```

Avoid vague user prompts.

Do not ask:

```text
What do you want to do?
```

Prefer:

```text
Choose one procedure. Each option has a different evidence, approval, memory or transmission consequence.
```

## Handoff preview

If the decision may lead to Hermes execution, the surface may show a handoff preview.

```text
handoff_preview:
  target_runtime: Hermes | other_execution_runtime
  requested_effect: read_only | internal_state_change | external_effect | canonical_effect
  allowed_inputs:
  forbidden_effects:
  expected_result_candidate:
  expected_evidence_pack_candidate:
  idempotency_required:
  approval_required:
```

The surface must block `canonical_effect` as runtime work.

Runtime success is not governance approval.

## Approval boundary

The surface must separate:

```text
recommendation_candidate
approval_to_prepare
approval_to_handoff
approval_to_transmit
approval_to_remember
approval_to_validate
```

Only the appropriate approval may unlock the corresponding next step.

An approval to prepare a draft is not approval to transmit it.

An approval to run Hermes is not approval to canonize the result.

## Memory boundary

A decision surface may propose a memory consequence.

Allowed:

```text
memory_effect: none | candidate_only | review_required | rejected
```

Forbidden:

```text
automatic_memory_promotion
canonical_memory_by_display
cross_dossier_memory_without_scope
secret_or_raw_payload_memory
```

## Evidence relationship

The decision surface may reference an Evidence Pack Candidate.

It is not itself the Evidence Pack.

When the surface affects legitimacy, the Evidence Pack may record:

- decision question;
- options presented;
- sources referenced;
- unresolved tensions;
- user decision;
- approval boundary;
- blocked effects;
- outcome observation.

## Outcome observation

After execution, the return path should produce an Outcome Observation Candidate.

```text
outcome_observation_candidate:
  acted: true | false
  external_effect: true | false
  canonical_effect: false
  changed_objects:
  unchanged_objects:
  produced_candidates:
  blocked_items:
  follow_up_needed:
  approval_still_required:
  evidence_refs:
```

The decision surface may display this outcome, but it must not validate it.

## UX requirements

The surface should be readable by a professional user, not only by developers.

Required UX properties:

- short default summary;
- visible status label;
- visible blocked effects;
- evidence/source expansion;
- objection expansion;
- explicit next safe action;
- no implied approval;
- no hidden external effect;
- no visual confusion between candidate and validated states.

## Rejected collapses

```text
decision surface = approval
decision surface = evidence pack
decision surface = memory promotion
decision surface = Hermes command
decision surface = runtime state
decision surface = source of truth
recommendation = human decision
handoff preview = authorized handoff
shown source = validated evidence
raw artifact = proof
```

## Professional example

User request:

```text
Prepare a response to the client confirming that the quote is acceptable.
```

Surface:

```text
Decision needed: transmission risk detected.

Recommended procedure:
Draft a neutral clarification email instead of confirming acceptance.

Why:
The quote may include scope not confirmed by the current specification.
Sending acceptance could create contractual ambiguity.

Options:
1. safe_draft — prepare a neutral clarification email.
2. request_missing_source — block until the disputed scope is verified.
3. prepare_variants — draft two versions for review.
4. block_transmission — no client-facing response.

Required approval:
Approval to draft: low.
Approval to send: blocked pending human decision.

Blocked effects:
- no email sent;
- no quote approved;
- no memory promoted;
- no Registre Probatoire entry modified.
```

## Final rule

```text
The surface shows the decision.
Pantheon governs the status.
Hermes executes only if authorized.
The human decides.
```
