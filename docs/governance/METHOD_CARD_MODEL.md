# Method Card Model

Status: candidate support doctrine — generic Method Card grammar for governed AI use.

Runtime status: non-executable.

This document defines how Method Cards appear in Pantheon as visible, reviewable, role-proposed structures for AI work.

It does not implement a UI, method selector, reasoning engine, workflow engine, router, scheduler, queue, agent loop, approval engine, memory engine, Hermes skill, schema, connector or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Placement

`REASONING_MODES_LIBRARY.md` frames the raw reasoning-mode library as a candidate **Guide de compétence** stored in `templates/competence/reasoning_modes_guide_candidate.json`.

This document is different.

```text
Reasoning Modes Library
= raw reasoning support / guide de compétence candidate.

Method Card Model
= cockpit-facing grammar for visible professional method cards.
```

The raw library may inspire a Method Card. It does not become a Method Card by itself.

## Core distinction

```text
Role observes.
Method structures.
Competence produces.
Hermes executes.
Evidence supports.
Gate authorizes or blocks.
Human decides.
```

A Method Card is a reusable structure of reasoning, review or professional work discipline.

It can be:

```text
raw_method             -> abduction, deduction, Sagan, Occam, via negativa;
professional_method    -> source_admission, mission_scope_guard, probative_review;
runtime_pattern        -> self-consistency, ReAct, tree-of-thoughts, multi-agent debate.
```

The cockpit should usually show `professional_method` cards, not raw LLM techniques.

## What a Method Card is not

A Method Card is not a Role.

It does not judge, arbitrate, carry jurisdiction or decide status.

A Method Card is not a Competence.

It does not produce a deliverable by itself.

A Method Card is not Evidence.

It does not prove a claim by itself.

A Method Card is not a Gate.

It does not authorize truth, memory, approval, external action or professional commitment.

A Method Card is not a Hermes Skill.

It may be projected into a bounded Hermes task, but the card itself never executes.

## Not owned by MÈTIS

A Method Card is not necessarily MÈTIS.

MÈTIS may propose a method when the question is indirect, blocked, fuzzy, strategic or mal-posed.

But the deck is shared:

```text
ARGOS may propose source_admission, authority_qualification or probative_review.
THEMIS may propose mission_scope_guard, external_commitment_guard or contractual_decomposition.
ATHENA may propose synthesis, constrained_generation or problem_repositioning.
HEPHAISTOS may propose decomposition, sequencing or implementation-structure methods.
ZEUS may request a method change before status arbitration.
```

## Run affordances, not hardcoded steps

A Run type may list method affordances.

It should not force every method on every instance.

```text
Run type
-> possible method families
-> role detects a task tension
-> Method Proposal Candidate
-> bounded Hermes execution if useful
-> Result Candidate + Evidence Pack Candidate
-> Gate if consequential
```

This keeps Pantheon:

```text
flexible in reasoning;
strict in status.
```

## Method Proposal Candidate

A Role proposes a method only when the task exposes a tension, contradiction, uncertainty, failure or opportunity.

Candidate shape:

```text
method_proposal_candidate:
  proposing_role:
  task_ref:
  run_ref:
  detected_problem:
  current_method:
  proposed_method:
  reason:
  expected_gain:
  expected_cost:
  evidence_delta:
  scope_delta:
  memory_delta:
  external_action_delta:
  hermes_profile_hint:
  allowed_outputs:
  forbidden_outputs:
  gate_required:
  stop_condition:
  status: proposed | accepted_internal | needs_zeus | needs_human_gate | rejected | resolved
```

Example:

```text
ARGOS detects conflicting amounts between a quote and a payment situation.
ARGOS proposes authority_qualification.
Allowed output: Evidence Pack Candidate + contradiction list.
Forbidden output: payment approval.
Gate: no if internal only; yes before client or enterprise instruction.
```

## Acceptance levels

```text
Level 1 — internal adjustment
Allowed when internal, reversible, low-cost, non-consequential and visibly traced.

Level 2 — Zeus review
Required if the method changes confidence, source status, proof requirement, scope, cost, memory posture or approval ceiling.

Level 3 — human gate
Required if the method may lead to external transmission, visa, filing, client validation, enterprise instruction, canonical memory, fault recognition or mission extension.
```

## Card fields

Candidate shape, not a schema:

```text
method_card:
  id:
  name:
  deck_level: raw_method | professional_method | runtime_pattern
  family:
  purpose:
  use_when:
  do_not_use_when:
  triggers:
  expected_output:
  source_requirements:
  evidence_expectation: none | source_refs | evidence_pack_candidate_required
  evidence_delta:
  scope_delta:
  guardrails:
  failure_modes:
  stop_condition:
  fidelity_check:
  fitness_check:
  compatible_roles:
  compatible_competences:
  compatible_rites:
  hermes_profile_hint:
  forbidden_outputs:
  gate_triggers:
  visibility: hidden_default | visible_when_selected | visible_when_contested | visible_when_consequential
  status: candidate | active_support | to_verify | rejected | obsolete
```

## Fidelity and fitness

Two checks remain distinct:

```text
Fidelity = did the output actually use the declared method?
Fitness  = was this method appropriate for the problem?
```

A method can be faithful but unfit, fit but poorly applied, both, or neither.

## Hermes handoff

A Method Card may be projected into Hermes only as a bounded task element:

```text
Task Contract
+ Context Pack
+ Method Card or Method Proposal Candidate
+ allowed sources
+ allowed outputs
+ forbidden outputs
+ approval ceiling
+ stop condition
-> Hermes execution
-> Result Candidate + Evidence Pack Candidate + Trace References
```

Hermes may execute the bounded work.

It may not convert method success into proof, approval, memory or external action.

## Relationship with Card Stack

Inside the Pantheon reference project, Method Cards may appear as global method references.

Inside a real task, a method appears first as a field or reference.

It becomes a visible sub-card only when it carries process state:

```text
method proposed;
method contested;
method failed;
method repeated;
method changed output;
method raises proof, scope, cost, status, memory or gate impact.
```

## Core invariant

```text
A Method Card structures thought.
It does not decide status.
It does not prove content.
It does not authorize action.
It does not execute.
```

The validated remains.
