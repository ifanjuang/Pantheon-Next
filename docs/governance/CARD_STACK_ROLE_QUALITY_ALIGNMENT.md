# Card Stack Role Quality Alignment

Status: candidate support note — terminology alignment for card-stack UX, role qualities and visible governance traces.

This document is not canonical doctrine yet.

It does not implement a UI, dashboard, card renderer, swipe engine, graph view, runtime, workflow engine, scheduler, queue, router, approval engine, memory engine, OpenWebUI Function, Hermes skill, connector or external action.

It reconciles `CARD_STACK_MODEL.md` with the current role-quality vocabulary:

```text
God = governance figure.
Role = function carried by the god.
Jurisdiction = domain the role protects.
Facet = quality that allows the role to protect its jurisdiction.
Expression = contextual manifestation of that quality.
```

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

`CARD_STACK_MODEL.md` already defines a broad candidate UX grammar for cards, scenes, decks, constellation, gates, roles, rites, competences, evidence and actions.

Some phrases in that document still reflect an earlier vocabulary:

```text
Role / God Cards activated;
active facet;
role is active;
Gods are review facets.
```

The current model is more precise:

```text
roles are permanent guardians;
facets are role qualities;
qualities express themselves contextually;
only useful quality expressions become visible;
cards expose those expressions without turning roles into agents.
```

This document explains how to read and update card UX language without rewriting the entire card-stack draft immediately.

## Reading rule

When `CARD_STACK_MODEL.md` says:

```text
Role / God Cards activated
```

read:

```text
Role / God Cards whose qualities materially expressed themselves in the treatment.
```

When it says:

```text
active facet
```

read:

```text
visible role quality expression.
```

When it says:

```text
Gods are review facets
```

read:

```text
Gods are governance roles.
Facets are the qualities through which they review, warn, orient, consult or request gates.
```

## Card family correction

### Role / God Card

A Role / God Card should represent the role as a guardian.

Recommended front:

```text
role name;
jurisdiction;
main visible quality expression;
warning or contribution;
linked gate or next action;
```

Recommended back:

```text
jurisdiction;
protected fields;
qualities / facets;
why the quality expressed itself;
consulted qualities;
reflexes produced;
tactics proposed;
limits;
related gates;
trace of the current expression;
```

Boundary:

```text
A Role / God Card does not make a role an agent.
A role may sense, warn, orient, propose, consult, request a rite and ask for a gate.
It does not execute, approve, send, memorize canonically or replace the human.
```

### Role Quality / Facet Card

A Role Quality / Facet Card should represent one expressed quality, not a whole role and not a protected field.

Recommended front:

```text
role / quality;
expression type: warning | tactic | consultation | gate request | clarification;
reason;
output effect;
```

Recommended back:

```text
role;
jurisdiction;
protected field;
quality type: sensitivity | reflex | orientation | tactic | consultation habit | prudence mode | alert threshold | limit;
context;
consulted quality if any;
status effect;
risk effect;
wording effect;
evidence effect;
next-action effect;
gate effect;
```

Boundary:

```text
A quality expression is not an approval.
A warning is not a decision.
A consultation trace is not hidden chain-of-thought.
A gate request is not gate completion.
```

## Workflow Scene correction

In Workflow Scene, the used-card list should be read or later revised as:

```text
Project
Subject
Workflow / Demarche
Context Stack
Context Cards
Documents / Sources used
Connaissances used
Competences used
Competences created on the flow
Guides / Ressources de competence when relevant
Templates used
Evidence created or relied on
Role / God Cards whose qualities materially expressed themselves
Role Quality / Facet Cards when a quality changed status, risk, wording, evidence or gate
Rite Cards invoked or requested
Action Cards prepared
Gate Cards opened or closed
Trace Cards
Memory / Register Candidate Cards
Gap Cards
Promotion Cards
```

Do not include a role merely because it exists in the governance college.

Do not include a quality merely because it is inherent to the role.

Include it only when it changes the treatment.

## Visibility rule

A role quality should become visible only if it changes at least one of:

```text
status;
risk;
wording;
evidence requirement;
missing information;
next action;
consultation;
rite request;
Zeus arbitration;
gate;
```

If it only comments, decorates or restates the obvious, it remains silent.

## Gesture boundary

Gestures may reveal, request or prepare.

They must not decide.

| Gesture | Allowed meaning | Forbidden meaning |
|---|---|---|
| Tap | open detail / verso | validate |
| Long press | show quick actions | approve automatically |
| Vertical swipe | move through active deck | execute next step |
| Horizontal swipe | change subject / lane | merge decisions |
| Constellation selection | navigate relationships | make graph authoritative |

## Quality trace in cards

Recommended compact trace:

```text
Relevant quality expressions:
- Themis / responsibility sensitivity: warning — possible prescription outside mission.
- Athena / proof sensitivity: evidence gap — source insufficient for conclusion.
- Iris / safer-wording orientation: tactic — reformulate as clarification request.
- Hermes / external-action sensitivity: gate — draft only, not sent.
```

Detailed trace remains second-layer.

## Card stack minimum for first test

For the first site-report test, do not implement all card families.

Use only:

```text
Context Card;
Method / Workflow Card;
Document / Source Card;
Evidence Card;
Role Quality / Facet Card;
Draft Output Card;
Action Card;
Zeus Gate Card;
Trace Card;
```

Success criterion:

```text
The user can see what was used, what was risky, which quality expressed itself, what draft was produced, what action is only candidate, and what gate remains open.
```

## Anti-patterns

```text
Do not rename every card family before testing.
Do not display every role.
Do not display every inherent quality.
Do not let role cards become character panels.
Do not let swipes validate decisions.
Do not let quick actions bypass gates.
Do not let constellation become authority.
Do not let a role-quality warning become a validated conclusion.
```

## Final rule

```text
The card shows the object.
The role guards a jurisdiction.
The quality expresses itself only when useful.
The stack organizes the treatment.
The gate exposes the threshold.
The human decides.
```
