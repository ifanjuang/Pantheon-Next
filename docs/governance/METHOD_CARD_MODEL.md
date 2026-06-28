# Method Card Model

Status: candidate support doctrine — method and reasoning cards for the Pantheon card deck.

Runtime status: non-executable.

This document defines a card family for reusable methods, reasoning forms and professional AI-control approaches inside the Pantheon reference deck.

It does not implement a UI, card renderer, selector, orchestrator, reasoning engine, workflow engine, scheduler, queue, agent loop, approval engine, memory engine, OpenWebUI Function, Hermes skill, schema, test, connector or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon needs a way to show *how a task is being worked through* without confusing that method with a Role, Competence, Rite, Evidence item, Action Candidate or Gate.

The practical formula is:

```text
Role observes.
Method structures.
Competence produces.
Hermes executes.
Evidence supports.
Gate authorizes or blocks.
Human decides.
```

A Method Card is the missing card family between competence and rite:

```text
A Competence knows how to produce.
A Method structures the reasoning and review discipline used while producing.
A Rite governs a recurring procedural tension.
```

For professional AI use, a Method Card is not only a mental model. It is a control surface for AI work:

```text
what kind of problem is being treated;
which sources must enter;
which source status is required;
which output candidate shape is expected;
which assertions need evidence;
which effects are forbidden;
where the execution runtime must stop;
which gate appears if the output becomes consequential.
```

## What a Method Card is

A Method Card is a reusable reasoning and work-structuring pattern.

It may express raw reasoning forms:

```text
deduction;
induction;
abduction;
analogy;
Occam / Chatton / Sagan / Hitchens-style proof discipline;
Bayesian updating;
premortem;
inversion;
second-order thinking;
via negativa;
reframing;
metis-style oblique approach;
first-principles reasoning;
chain-of-verification;
steel-manning;
root-cause analysis.
```

It may also express professional architecture-agency methods:

```text
source admission;
authority qualification;
assertion mapping;
contractual decomposition;
mission-scope guard;
external-commitment guard;
probative review;
phase-gate review;
constrained generation;
problem repositioning.
```

It helps the cockpit and the execution runtime answer:

```text
Which work discipline is being used?
Why this discipline here?
Which source status is required?
What does faithful application look like?
When would this method be inappropriate?
Which guardrails must remain visible?
Where must the runtime stop?
```

## What a Method Card is not

A Method Card is not a Role.

It does not look, judge, arbitrate, protect a jurisdiction or decide status.

A Method Card is not a Competence.

It does not produce a deliverable by itself.

A Method Card is not a Hermes Skill.

It may be projected into a runtime prompt, Kanban task, profile instruction or skill, but the card itself does not execute.

A Method Card is not Evidence.

It does not support a factual assertion by itself.

A Method Card is not a Gate.

It does not authorize truth, memory, approval, external action or professional commitment.

A Method Card is not canonical memory.

It may propose a learning candidate after use, but it never promotes itself or its outcome into the Registre Probatoire.

## Placement in the card deck

Method Cards live in the `Pantheon` reference project, alongside Roles, Competences, Rites, Run types and Documents.

```text
Pantheon
-> Documents
-> Roles
-> Methods / Reasoning
-> Competences
-> Rites
-> Run types
```

They are global and neutral. They are not owned by a client project.

Inside a real project run, a Method appears first as a task field or linked reference.

It becomes a visible sub-card only when it carries process state:

```text
method proposed;
method selected;
method contested;
method failed;
method repeated;
method changed the output;
method requires fidelity check;
method requires fitness check;
method raises a cost, proof, scope or approval concern.
```

## Boundary with MÈTIS

A Method Card is not necessarily MÈTIS.

MÈTIS may propose a Method Card when the demand is fuzzy, indirect, strategic, mal-posed, blocked or oblique.

But MÈTIS does not own the method deck.

Other Roles may also mobilize Method Cards:

```text
ARGOS may mobilize chain-of-verification, source admission, source-audit or authority-qualification methods.
THEMIS may mobilize mission-scope, responsibility, Hume, Chesterton or external-commitment methods.
ATHENA may mobilize synthesis, analogy, reframing, constrained generation or steel-manning methods.
HEPHAISTOS may mobilize decomposition, first principles, sequencing or implementation-structure methods.
ZEUS may request a method change before status arbitration.
```

The method deck is shared. A Role selects, contests or requests a method according to the task tension.

## Adaptive method proposal

Methods should not be hardcoded as fixed steps inside a Run.

A Run defines the professional terrain:

```text
objective;
expected result candidate;
risk families;
source expectations;
approval ceiling;
forbidden effects;
possible method families;
stop conditions.
```

A Role may then propose a Method Card when the active task exposes a tension, failure, contradiction, uncertainty or opportunity.

```text
Run in progress
-> active Task
-> Role detects a tension
-> Role proposes a Method Proposal Candidate
-> Pantheon qualifies the effect
-> Hermes executes only if bounded
-> Result Candidate + Evidence Pack Candidate return
-> Gate appears if consequence requires it
```

This keeps the system:

```text
flexible in reasoning;
strict in status.
```

## Method Proposal Candidate

When a Role proposes a method, the proposal must be explicit enough to be reviewable.

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
  impact_on_evidence:
  impact_on_scope:
  impact_on_memory:
  impact_on_external_action:
  hermes_profile_hint:
  allowed_outputs:
  forbidden_outputs:
  gate_required:
  stop_condition:
  status: proposed | accepted_internal | needs_zeus | needs_human_gate | rejected
```

Examples:

```text
ARGOS detects two contradictory amounts between a quote, a situation and a signed amendment.
ARGOS proposes: authority qualification.
Reason: the analysis cannot proceed until source precedence is clear.
Allowed output: Evidence Pack Candidate + contradiction list.
Forbidden output: validation of payment.
Gate: no, if internal only.
```

```text
THEMIS detects that a draft sentence says "we validate" in a context that may imply professional commitment.
THEMIS proposes: mission-scope guard.
Reason: risk of implicit instruction or mission extension.
Allowed output: prudent wording candidate + approval gap.
Forbidden output: external transmission.
Gate: yes before sending.
```

## Acceptance levels

Not every method change deserves friction.

```text
Level 1 — internal adjustment
A Role may propose and apply a light method if the work is internal, reversible, low-cost, non-consequential and visibly traced.

Level 2 — Zeus review
The proposal needs status arbitration if it changes confidence, source status, proof requirement, scope, cost, memory posture or approval ceiling.

Level 3 — human gate
The proposal requires a human decision if it may lead to external transmission, visa, filing, client validation, enterprise instruction, canonical memory, fault recognition or mission extension.
```

Changing method is therefore free only while its effects remain non-consequential.

## Run affordances, not hardcoded steps

A Run type may list method affordances.

It should not force every method on every instance.

Example:

```text
Run type: reception of complementary quotation

Possible method affordances:
  source admission;
  authority qualification;
  contractual decomposition;
  diagnostic cause analysis;
  mission-scope guard;
  decision premortem;
  external-commitment guard.

Rule:
  activate only when a Role detects a relevant tension.
```

Example in use:

```text
Task: analyze complementary quotation
Current method: contractual decomposition
ARGOS detects: inconsistent amount between signed quote and situation
ARGOS proposes: authority qualification
Status: accepted_internal
Hermes profile: evidence-review
Return: Evidence Pack Candidate + questions
```

```text
Task: draft answer to enterprise
Current method: synthesis transmissible
THEMIS detects: wording may imply agency instruction
THEMIS proposes: mission-scope guard
Status: needs_human_gate before transmission
```

## Card fields

Minimum shape, candidate only:

```text
method_card:
  id:
  name:
  deck_level: raw_method | professional_method | runtime_pattern
  family: primitive | razor | critique | verification | decision | oblique | creative | diagnostic | synthesis | professional_guardrail
  movement: frontal | oblique
  purpose:
  professional_use:
  use_when:
  do_not_use_when:
  triggers:
  expected_reasoning_shape:
  expected_output:
  output_candidate_shape:
  source_requirements:
  evidence_expectation: none | source_refs | evidence_pack_candidate_required
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
  cost_hint: low | medium | high | multi-step
  visibility: hidden_default | visible_when_selected | visible_when_contested | visible_when_consequential
  status: candidate | active_support | to_verify | rejected | obsolete
```

This is not an approved schema. If a machine-checkable schema is later proposed under `schemas/`, that requires a separate protected-path review.

## Fidelity and fitness

Two checks must remain distinct.

```text
Fidelity = did the output actually use the declared method?
Fitness  = was this method appropriate for the problem?
```

A method may be:

```text
faithful but unfit;
fit but poorly executed;
faithful and fit;
neither faithful nor fit.
```

The two verdicts must not be collapsed into one generic quality score.

## Professional method deck

The visible cockpit deck should prefer professional method cards over raw cognitive labels.

Recommended core candidates:

```text
source_admission;
authority_qualification;
assertion_mapping;
diagnostic_cause_analysis;
mission_scope_guard;
external_commitment_guard;
probative_review;
decision_premortem;
contractual_decomposition;
phase_gate_review;
constrained_generation;
problem_repositioning.
```

Raw reasoning cards may remain available as internal method material, but the user-facing card should usually be professional.

Example:

```text
User-facing card: mission_scope_guard
Internal methods:
  Chesterton fence;
  Hume is/ought split;
  second-order thinking;
  responsibility boundary check.
```

## Runtime patterns

Some items from `reasoning_mods.json` should not become visible professional cards.

They are better treated as runtime patterns for Hermes or another execution runtime:

```text
chain-of-thought prompting;
self-consistency;
Tree of Thoughts;
Graph of Thoughts;
ReAct;
self-refine;
multi-agent debate;
analogical prompting.
```

These may be used internally when appropriate, but they should not be mistaken for professional method authority.

Pantheon should ask for exposed justification, not hidden private reasoning.

Expected exposed justification:

```text
sources used;
assertions retained;
hypotheses;
checkable steps;
uncertainties;
candidate conclusion;
forbidden effects respected.
```

## Hermes handoff

A Method Card may be projected into a Hermes Kanban task, profile request, delegate task or skill prompt.

The handoff must remain bounded:

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

Hermes may execute the bounded method. It may not convert method success into proof, approval, memory or external action.

## Method use in a task

Example: reception of a complementary quotation.

```text
Task:
  verify a complementary quotation against contract scope and project evidence.

Roles:
  THEMIS -> mission / contract boundary
  ARGOS  -> source and clause verification
  ZEUS   -> status arbitration

Competences:
  verify quotation against CCTP / CCAP
  produce comparison table
  draft prudent client response

Possible method proposals:
  source_admission -> is the quotation admissible as a project source?
  authority_qualification -> which source prevails if amounts differ?
  contractual_decomposition -> what was included, excluded or changed?
  diagnostic_cause_analysis -> what explains the difference?
  mission_scope_guard -> would the answer extend the agency role?
  external_commitment_guard -> can anything be sent?

Evidence:
  quotation received
  signed contract
  CCTP / CCAP clauses
  relevant mails
  previous validation trace

Gate:
  can a response be sent?
  does it imply mission extension?
  does client approval become required?
```

## Interaction with competences

A Competence may reference preferred Method Cards or method affordances.

Example:

```text
Competence: vérifier un devis contre CCTP
Preferred method affordances:
  source_admission;
  authority_qualification;
  contractual_decomposition;
  mission_scope_guard.
```

The competence still produces candidates. The method only structures the reasoning and review discipline.

## Interaction with rites

A Rite may prescribe, recommend or forbid Method Cards.

Example:

```text
Rite: proof sufficiency
May require:
  assertion_mapping;
  probative_review;
  source_admission.

Rite: mission boundary
May require:
  mission_scope_guard;
  external_commitment_guard;
  second-order thinking.
```

The Rite governs a recurring tension. The Method supplies a reasoning form inside that tension.

## Interaction with `reasoning_mods.json`

`schemas/reasoning_mods.json` should not be treated as MÈTIS itself.

It should be read as a candidate raw method catalog, or a possible seed for a future Method Deck.

Its content must remain candidate unless reviewed, normalized and given an explicit authority status.

If retained under `schemas/`, it should eventually become either:

```text
1. a real machine-checkable schema, with protected-path review;
2. or be moved out of `schemas/` into templates, governance docs or reference material.
```

Until then, it should not silently act as canonical schema, runtime selector or orchestration policy.

## Core invariant

```text
A Method Card structures thought.
It does not decide status.
It does not prove content.
It does not authorize action.
It does not execute.
```

Only the validated remains.
