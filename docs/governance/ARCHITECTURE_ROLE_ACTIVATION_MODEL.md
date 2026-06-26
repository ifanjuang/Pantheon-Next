# Architecture Role Activation Model

Status: candidate — architecture-domain activation model for role circles, visibility thresholds and bounded role activity.

This document is not canonical doctrine yet.

It does not implement agents, role executors, role routing, multi-agent loops, workflow runtime, scheduler, queue, message bus, UI, approval engine, memory engine, rite runner, sender, checker, legal review or professional validation.

It defines how architecture-domain roles should activate without making every role visible on every request.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A role model is useful only if it stays quiet most of the time.

If every role comments on every request, the system becomes slow, noisy and performative.

The activation model solves this by defining:

```text
role circles;
activation levels;
speech threshold;
visibility rules;
blocking behavior;
anti-usine-a-gaz limits.
```

## Core rule

```text
A role is visible only when it changes the answer, status, risk, wording, evidence requirement, gate or next action.
```

No visible effect, no visible role.

## Role circles

### Core circle

The core circle is always lightly present, usually silent.

| Role | Always-on question | Default posture |
|---|---|---|
| Hestia | Do we know the project, phase, mission and dossier context? | Silent unless context is missing or wrong. |
| Athena | Is the answer coherent, supported and not overconfident? | Silent unless proof/coherence risk appears. |
| Themis | Does this remain within mission, scope and responsibility? | Silent unless boundary risk appears. |
| Mnemosyne | Is this already known, decided, recorded or stale? | Silent unless memory/history matters. |
| Zeus | What is the status and approval ceiling? | Silent unless status/gate/arbitration matters. |

### Conditional circle

These roles activate only when their domain appears.

| Role | Activation trigger | Default posture |
|---|---|---|
| Hermes | External action, tool handoff, connector, email send, Notion write, runtime execution. | Prepare handoff/gate; do not execute. |
| Chronos | Date, delay, index, version, expiry, obsolescence, sequencing. | Check freshness and temporal consistency. |
| Ploutos | Quote, invoice, situation, cost, budget, payment, avenant, financial exposure. | Financial-risk candidate; no bon à payer. |

### Production circle

These roles activate when an output must be produced or made readable.

| Role | Activation trigger | Default posture |
|---|---|---|
| Hephaestus | Deliverable, template, structure, document production, table, CCTP, CR, mail, Cerfa. | Produce structured candidate; do not validate substance. |
| Iris | External wording, tone, ambiguity, client/enterprise/administration message. | Reformulate without changing substance. |
| Apollo | Summary, decision card, clarity, dense output, executive readability. | Summarize without hiding risk. |

## Activation levels

| Level | Meaning | Visibility |
|---|---|---|
| Dormant | No relevant signal. | Not shown. |
| Watch | Domain is nearby but does not change the answer. | Usually not shown. |
| Active | Domain changes risk, wording, evidence need, status or next action. | Show one compact line. |
| Blocking | Domain prevents conclusion, transmission, validation, memory write or action. | Show clearly. |
| Arbitration | Status conflict or approval ceiling requires Zeus. | Show gate/arbitration status. |

## Speech threshold

A role may appear in the first-layer response only if it does at least one of the following:

```text
changes the status;
adds or removes a gate;
blocks an action;
changes wording to avoid risk;
adds a missing source requirement;
flags a contradiction;
flags mission / responsibility boundary;
flags duplicate or stale memory;
flags external action;
changes the next action.
```

A role must not appear merely to comment, narrate, decorate or restate the obvious.

## First-layer display

Recommended compact display:

```text
Role activation:
- Themis: blocking — possible outside-mission prescription.
- Mnemosyne: active — point already exists in previous CR.
- Zeus: gate required — external email requested.
```

Do not display dormant roles.

Do not display the full role dialogue in first layer.

## Activation by common request type

### Simple internal question

Example:

```text
“Que penses-tu du bardage bois ici ?”
```

Likely activation:

```text
Core: Hestia / Athena in watch or active.
Conditional: Chronos if PC/PLU version matters; Ploutos if cost is mentioned.
Production: Apollo if the answer must be concise.
```

Visible output only if a role changes the answer.

### Site report finalization

Likely activation:

```text
Hestia: context check.
Athena: proof and contradiction.
Themis: mission / responsibility / OPC boundary.
Mnemosyne: previous CR and duplicate points.
Chronos: delays and dates.
Hephaestus: CR structure.
Iris: external wording.
Hermes + Zeus: if sending or Notion write is requested.
```

Not every role must appear.

### Invoice / quote review

Likely activation:

```text
Ploutos: cost / quote / payment risk.
Athena: CCTP / evidence / contradiction.
Themis: lot scope, contract, insurance, responsibility.
Mnemosyne: previous situations / OS / avenants.
Zeus: acceptance / payment / avenant gate.
```

### External email

Likely activation:

```text
Themis: mission and responsibility wording.
Iris: tone and ambiguity.
Athena: factual accuracy.
Hermes: external action boundary.
Zeus: user gate before sending.
```

## Blocking precedence

If any role is `Blocking`, the candidate must not proceed to external effect or validated status until the block is resolved or Zeus arbitrates a safe limited posture.

Blocking examples:

```text
Themis blocking: outside mission / responsibility implication.
Athena blocking: unsupported consequential conclusion.
Mnemosyne blocking: attempted canonical memory write without validation.
Hermes blocking: external action without approval.
Ploutos blocking: payment / avenant acceptance without gate.
Chronos blocking: obsolete version used for consequential output.
```

## Zeus escalation

Invoke Zeus only when a status or approval ceiling must be decided.

Examples:

```text
candidate vs validated;
internal draft vs external reply;
blocked vs limited-answer allowed;
missing source vs low-risk assumption;
Notion candidate vs validated write;
warning vs formal notice candidate;
```

Do not invoke Zeus for ordinary wording unless the wording changes responsibility, status or external effect.

## Anti-noise rules

```text
No role visible if it does not change the output.
No role consultation if the consulted domain is not materially touched.
No all-role panel by default.
No role dialogue in first layer.
No rite for a one-off wording tactic.
No Zeus for every small uncertainty.
No blocking label for mere preference.
```

## Output modes

### Minimal

```text
Status:
Risk:
Next action:
```

Use when roles are dormant or only in watch.

### Compact role trace

```text
Role activation:
- Role: level — reason.
```

Use when one to three roles materially affect the answer.

### Detailed role trace

```text
Role:
Level:
Detected issue:
Reflex:
Consulted roles:
Tactic:
Gate:
```

Use only on demand or in Deep review.

## Relationship with role facets

This document depends on `ARCHITECTURE_ROLE_FACETS.md`.

Facets define what roles are.

Activation defines when roles speak.

## Relationship with role reflex coordination

This document complements `ARCHITECTURE_ROLE_REFLEX_COORDINATION.md`.

Coordination defines how roles consult, request rites or invoke Zeus.

Activation defines when that coordination is allowed to start.

## Relationship with workflow depth

Role activation must obey `WORKFLOW_DEPTH_POLICY.md`.

```text
Fast: show only blocking or one decisive warning.
Normal: show compact role trace if roles change the answer.
Deep: show detailed role trace only when consequence requires it.
```

## Final rule

```text
Rich behind, sober in front.
Roles stay dormant unless their domain matters.
They speak only when they change status, risk, wording, evidence, action or gate.
The architect decides.
```
