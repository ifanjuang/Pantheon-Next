# Method Card Model

Status: candidate support doctrine — method and reasoning cards for the Pantheon card deck.

Runtime status: non-executable.

This document defines a card family for reusable methods, reasoning forms and cognitive approaches inside the Pantheon reference deck.

It does not implement a UI, card renderer, selector, orchestrator, reasoning engine, workflow engine, scheduler, queue, agent loop, approval engine, memory engine, OpenWebUI Function, Hermes skill, schema, test, connector or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon needs a way to show *how a task is being thought through* without confusing that method with a Role, Competence, Rite, Evidence item, Action Candidate or Gate.

The practical formula is:

```text
Role regarde.
Method structure.
Competence produces.
Evidence supports.
Gate authorizes or blocks.
Human decides.
```

A Method Card is the missing card family between competence and rite:

```text
A Competence knows how to produce.
A Method structures the reasoning used while producing or reviewing.
A Rite governs a recurring procedural tension.
```

## What a Method Card is

A Method Card is a reusable reasoning structure.

It may express:

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

It helps the cockpit and the execution runtime answer:

```text
Which reasoning shape is being used?
Why this shape here?
What does faithful application look like?
When would this method be inappropriate?
Which guardrails must remain visible?
```

## What a Method Card is not

A Method Card is not a Role.

It does not look, judge, arbitrate, protect a jurisdiction or decide status.

A Method Card is not a Competence.

It does not produce a deliverable by itself.

A Method Card is not a Hermes Skill.

It may be projected into a runtime prompt or skill, but the card itself does not execute.

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
-> Competences
-> Methods / Reasoning
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
method raises a cost or approval concern.
```

## Boundary with MÈTIS

A Method Card is not necessarily MÈTIS.

MÈTIS may propose a Method Card when the demand is fuzzy, indirect, strategic, mal-posed, blocked or oblique.

But MÈTIS does not own the method deck.

Other Roles may also mobilize Method Cards:

```text
ARGOS may mobilize chain-of-verification or source-audit methods.
THEMIS may mobilize Hume, Chesterton, scope-boundary or responsibility methods.
ATHENA may mobilize synthesis, analogy, reframing or steel-manning methods.
HEPHAESTOS may mobilize decomposition, first principles or implementation-sequencing methods.
ZEUS may request a method change before status arbitration.
```

The method deck is shared. A Role selects, contests or requests it according to the task tension.

## Card fields

Minimum shape, candidate only:

```text
method_card:
  id:
  name:
  family: primitive | razor | critique | verification | decision | oblique | creative | diagnostic | synthesis
  movement: frontal | oblique
  purpose:
  use_when:
  do_not_use_when:
  triggers:
  expected_reasoning_shape:
  expected_output:
  guardrails:
  fidelity_check:
  fitness_check:
  compatible_roles:
  compatible_competences:
  compatible_rites:
  cost_hint: low | medium | high | multi-step
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

Methods:
  abduction -> what explains the price difference?
  Occam / Chatton -> simple explanation or missing cause?
  Chesterton fence -> why does the existing clause exist?
  second-order thinking -> consequences of accepting / refusing
  premortem -> how could the decision fail later?

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

A Competence may reference one or more preferred Method Cards.

Example:

```text
Competence: vérifier un devis contre CCTP
Preferred methods:
  abduction
  source verification
  second-order thinking
  Hitchens / Sagan proof discipline
```

The competence still produces candidates. The method only structures the reasoning.

## Interaction with rites

A Rite may prescribe or forbid Method Cards.

Example:

```text
Rite: proof sufficiency
May require:
  chain-of-verification
  Hitchens proof burden
  Sagan proportionality

Rite: mission boundary
May require:
  Chesterton fence
  Hume is/ought split
  second-order thinking
```

The Rite governs a recurring tension. The Method supplies a reasoning form inside that tension.

## Interaction with `reasoning_mods.json`

`schemas/reasoning_mods.json` should not be treated as MÈTIS itself.

It should be read as a candidate method catalog, or a possible seed for a future Method Deck.

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
