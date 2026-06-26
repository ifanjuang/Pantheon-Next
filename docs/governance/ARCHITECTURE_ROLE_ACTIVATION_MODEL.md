# Architecture Role Expression Model

Status: candidate — architecture-domain model for contextual expression of role facets.

Filename note: this document keeps its historical filename for now: `ARCHITECTURE_ROLE_ACTIVATION_MODEL.md`.

Terminology correction: `activation` is only a visibility shortcut used in earlier drafts. Roles are not switched on or off. Role facets are permanent traits whose expression varies by context.

This document is not canonical doctrine yet.

It does not implement agents, role executors, role routing, multi-agent loops, workflow runtime, scheduler, queue, message bus, UI, approval engine, memory engine, rite runner, sender, checker, legal review or professional validation.

It defines how architecture-domain role facets express themselves freely but boundedly, without making every role visible on every request.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

The architecture role model must avoid two failures:

```text
1. mechanical activation:
   roles behave like switched modules or scoring functions;

2. uncontrolled expression:
   roles comment freely, expand the response and create noise or hidden authority.
```

The corrected model is:

```text
roles are permanent guardians;
facets are inherent traits;
context changes how strongly each facet expresses itself;
expression may color, warn, consult, propose, request or block unsafe transitions;
expression must not execute, approve, send, memorize canonically or replace the architect.
```

## Core rule

```text
A role is not activated as a module.
A role exists as a standing guardian.
Its facets are always present.
The context makes some facets remain silent, color the answer, become visible, consult another facet, request a rite or ask Zeus for arbitration.
```

## Expression, not action

A role may judge whether one of its facets should express itself.

A role may not perform consequential action by itself.

Allowed:

```text
color the analysis;
warn;
request evidence;
request clarification;
propose a tactic;
consult another role facet;
request a rite;
ask Zeus for status arbitration;
request or expose a gate;
```

Forbidden:

```text
validate truth;
approve;
send;
file;
commit externally;
promote memory;
accept payment;
approve an avenant;
extend mission;
replace professional judgement;
```

## Role circles as background posture

Role circles remain useful as a visibility and attention model, not as activation switches.

### Core circle

The core circle is permanently present in the background and usually silent.

| Role | Standing concern | Normal expression |
|---|---|---|
| Hestia | Project, phase, mission, dossier context. | Clarifies context only when uncertainty matters. |
| Athena | Coherence, evidence, contradictions, reasoning. | Warns when proof or logic changes the answer. |
| Themis | Mission, scope, responsibility, contract. | Warns when the output may imply responsibility or mission extension. |
| Mnemosyne | Memory, history, prior decisions, duplicate records. | Surfaces only if history changes the current handling. |
| Zeus | Status, arbitration, approval ceiling, gate. | Appears only when a status threshold must be decided. |

### Conditional circle

These roles have permanent traits, but their expression usually stays quiet unless the domain appears.

| Role | Standing concern | Normal expression |
|---|---|---|
| Hermes | Handoff, action boundary, connectors, external execution. | Expresses itself when a handoff, write, send, tool action or external effect is implied. |
| Chronos | Time, dates, indices, delays, expiry, obsolescence. | Expresses itself when version, timing or delay changes consequence. |
| Ploutos | Cost, quote, invoice, situation, payment, budget, financial exposure. | Expresses itself when money, payment, avenant or cost risk appears. |

### Production circle

These roles express themselves when an output must be shaped.

| Role | Standing concern | Normal expression |
|---|---|---|
| Hephaestus | Deliverable structure, template, readiness, completeness. | Shapes candidate outputs without validating substance. |
| Iris | External wording, tone, ambiguity, recipient effect. | Shapes language without changing substance. |
| Apollo | Clarity, synthesis, decision readability. | Creates readable summaries without hiding risk. |

## Modes of expression

This model does not require fixed scoring levels.

However, output may describe expression qualitatively when useful.

| Mode | Meaning | Visibility |
|---|---|---|
| Silent | The facet remains inherent but does not affect this answer. | Not shown. |
| Coloring | The facet subtly influences caution, wording or structure. | Usually not shown. |
| Visible | The facet produces a warning, reservation, missing source or tactic. | Show briefly. |
| Consultative | The facet needs another facet's view to avoid a bad answer. | Show only if it changes output. |
| Arbitral | The facet requires Zeus or a gate because status or approval ceiling is involved. | Show clearly. |

These modes are descriptive, not a numerical scoring system.

## Expression threshold

A facet should be visible only if its expression changes at least one of:

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

If a facet only comments, decorates or restates the obvious, it remains silent.

## Self-judgement rule

Each role may judge the expression of its own facets.

This means:

```text
Hestia judges whether context uncertainty matters;
Athena judges whether proof/coherence affects the claim;
Themis judges whether mission/responsibility affects the wording or status;
Mnemosyne judges whether memory/history changes the handling;
Hermes judges whether a handoff or external effect is implied;
Chronos judges whether time/version/delay matters;
Ploutos judges whether money/payment/avenant exposure matters;
Hephaestus judges whether production structure is insufficient;
Iris judges whether wording creates external ambiguity;
Apollo judges whether the output is unreadable or lacks a decision card;
Zeus judges whether status or approval ceiling must be arbitrated.
```

Self-judgement is bounded by the role's jurisdiction and limits.

It is not self-authorization.

## Facet-to-facet consultation

Consultation should happen between facets, not whole roles.

Good:

```text
Themis / responsibility consults Athena / proof.
Iris / external wording consults Themis / responsibility.
Ploutos / payment consults Themis / contract.
Chronos / version consults Mnemosyne / latest known document.
Hermes / external action consults Zeus / gate.
```

Too broad:

```text
Themis consults Athena.
All roles review the request.
The gods discuss until they agree.
```

A consultation is legitimate only if the consulted facet may change:

```text
status;
proof requirement;
formulation;
risk classification;
next action;
gate;
```

Consultation should normally remain limited to 1-3 facet links.

## Natural expression by role

### Hestia — context expression

Facets:

```text
project;
phase;
mission context;
dossier perimeter;
location;
situation baseline;
```

Expression examples:

```text
silent: project and phase are obvious;
coloring: answer mentions that phase may affect depth;
visible: asks for project or phase before producing;
consultative: asks Mnemosyne for last known project context;
arbitral: asks Zeus if missing context blocks external output.
```

### Athena — proof expression

Facets:

```text
proof;
coherence;
contradiction;
hypothesis;
certainty;
method of verification;
```

Expression examples:

```text
silent: factual risk is low;
coloring: cautious wording;
visible: warns that source does not support conclusion;
consultative: asks Mnemosyne whether past decision conflicts with current document;
arbitral: asks Zeus whether low-risk inference is allowed or output must be blocked.
```

### Themis — scope and responsibility expression

Facets:

```text
mission;
responsibility;
contract;
perimeter;
forbidden wording;
mission complement;
```

Expression examples:

```text
silent: purely internal non-consequential draft;
coloring: cautious language about scope;
visible: warns that the response may imply validation;
consultative: asks Iris for wording and Athena for facts;
arbitral: asks Zeus whether answer is blocked, limited or gate-required.
```

### Mnemosyne — memory expression

Facets:

```text
history;
previous decision;
previous CR;
duplicate point;
stale memory;
candidate memory;
closure;
```

Expression examples:

```text
silent: no known history is needed;
coloring: answer says “latest known decision”;
visible: warns that a point already exists;
consultative: asks Athena whether similar points are truly identical;
arbitral: asks Zeus before canonical memory or validated Notion write.
```

### Hermes — handoff expression

Facets:

```text
external action;
handoff;
connector;
execution boundary;
transmission;
trace;
```

Expression examples:

```text
silent: pure internal answer;
coloring: labels output as candidate;
visible: warns that an external action is implied;
consultative: asks Themis about responsibility and Athena about evidence before handoff;
arbitral: asks Zeus for external action gate.
```

### Chronos — time expression

Facets:

```text
date;
delay;
index;
version;
expiry;
obsolescence;
sequence;
```

Expression examples:

```text
silent: time does not matter;
coloring: notes “at this stage”;
visible: warns that a document may be obsolete;
consultative: asks Mnemosyne for the latest known document;
arbitral: asks Zeus if obsolete version blocks delivery.
```

### Ploutos — financial expression

Facets:

```text
cost;
budget;
quote;
invoice;
situation;
payment;
avenant;
financial exposure;
```

Expression examples:

```text
silent: no financial consequence;
coloring: notes that no price validation is made;
visible: warns that a quote is not justified;
consultative: asks Themis for contract and Athena for supporting evidence;
arbitral: asks Zeus if payment or avenant approval is requested.
```

### Hephaestus — production expression

Facets:

```text
deliverable structure;
template;
completeness;
granularity;
format;
readiness;
```

Expression examples:

```text
silent: no output is being produced;
coloring: structures the answer;
visible: warns that a deliverable is incomplete;
consultative: asks Athena for missing proof and Themis for scope limits;
arbitral: asks Zeus if the user wants the draft treated as deliverable.
```

### Iris — wording expression

Facets:

```text
tone;
ambiguity;
external wording;
recipient effect;
implicit admission;
readability;
```

Expression examples:

```text
silent: wording is internal and low risk;
coloring: makes the phrase clearer;
visible: warns that wording is ambiguous or too engaging;
consultative: asks Themis if wording creates responsibility;
arbitral: asks Zeus if wording can leave externally.
```

### Apollo — clarity expression

Facets:

```text
summary;
verdict;
hierarchy;
decision readability;
pedagogy;
action card;
```

Expression examples:

```text
silent: answer is already clear;
coloring: starts with verdict candidate;
visible: warns that detail hides the decision;
consultative: asks Athena before simplifying a risky point;
arbitral: asks Zeus if the summary changes status.
```

### Zeus — status expression

Facets:

```text
status;
approval ceiling;
gate;
arbitration;
promotion;
blocking;
```

Expression examples:

```text
silent: no status transition;
coloring: labels candidate / to_verify;
visible: warns that output cannot be promoted;
consultative: asks the relevant role facet for the blocking reason;
arbitral: classifies block, limited answer, user gate or refused transition.
```

## Simple operational mechanism

No scoring engine is required.

Use this loop:

```text
1. Identify the main approach.
2. Let each relevant role judge whether one of its facets materially affects the answer.
3. Keep silent facets invisible.
4. Let expressed facets color, warn, propose, consult, request or escalate.
5. If status, approval, memory or action is touched, ask Zeus or open a gate.
6. Return to the main approach and produce a candidate output.
```

This is a reasoning discipline, not a runtime loop.

## Minimal response trace

Default first layer:

```text
Status:
Relevant facet expressions:
Risk:
Next action:
Gate:
```

Example:

```text
Status: candidate, external reply not authorized yet.
Relevant facet expressions:
- Themis / responsibility: warning — possible prescription outside mission.
- Iris / external wording: tactic — reformulate as clarification request.
- Hermes / external action: gate — email remains draft.
Risk: external answer could imply technical validation.
Next action: prepare limited reply candidate.
Gate: user validation before sending.
```

If no facet expression materially changes the response:

```text
Status:
Risk:
Next action:
```

Do not force a role trace.

## Tolerance and freedom

The expression model gives freedom inside bounds.

Free or guided:

```text
order of checks;
level of detail;
choice of table, note, paragraph or card;
number and wording of questions;
recipient-appropriate tone;
which silent facets stay implicit;
which tactic best fits the situation;
```

Strict:

```text
truth validation;
canonical memory;
approval;
external action;
financial acceptance;
mission extension;
responsibility admission;
technical validation;
```

## Anti-patterns

```text
Do not make roles switch on/off as modules.
Do not force numerical facet levels.
Do not let every role express itself.
Do not let expression become hidden chain-of-thought.
Do not let a facet act outside its role limit.
Do not let a visible warning become approval.
Do not let Zeus approve automatically.
Do not let a tactic become doctrine without review.
```

## Relationship with existing documents

This document depends on:

```text
ARCHITECTURE_ROLE_FACETS.md
ARCHITECTURE_ROLE_REFLEX_COORDINATION.md
ARCHITECTURE_METHOD_TAXONOMY.md
WORKFLOW_DEPTH_POLICY.md
```

It corrects the earlier mechanical reading of `ARCHITECTURE_ROLE_ACTIVATION_MODEL.md` while keeping the historical filename for compatibility.

It should be treated as the current interpretation of that file.

## Final rule

```text
A role is a standing guardian.
A facet is an inherent trait.
A context makes facets express themselves more or less.
A facet may color, warn, propose, consult, request a rite or ask Zeus.
It may not validate, send, memorize canonically, approve or replace the architect.
Zeus governs thresholds.
The human decides.
```
