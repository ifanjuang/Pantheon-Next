# Architecture Reflex Operating Model

Status: candidate — operating model for architecture-domain reflexes.

This document is not canonical doctrine yet.

It does not implement a runtime, agent router, workflow engine, scheduler, queue, UI, connector, memory engine, approval engine, document generator or automatic action system.

It defines a compact operating model so architecture-domain reflexes remain composable, bounded and usable without becoming an usine a gaz.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Architecture workflows can multiply quickly:

```text
CCTP from plan;
Cerfa from project data;
site report finalization;
photo chantier doubt;
invoice / quote review;
lot and insurance review;
material choice;
client response;
DTU / source check;
Notion observation candidate.
```

The purpose of this model is to reduce them to a shared operating grammar.

```text
Fewer workflows.
More reusable reflexes.
One decision grammar.
Compact outputs by default.
Deeper proof only when consequence requires it.
```

## Core rule

```text
Every architecture request is handled as:
Request -> Depth -> Context -> Reflexes -> Candidate -> Gate.
```

This shape is conceptual only. It is not a runtime sequence owned by Pantheon.

## Six universal objects

### 1. Request

What the user asks.

Examples:

```text
summarize this document;
prepare a CCTP;
finish this site report;
check this invoice;
choose a facade material;
reply to this client;
write this into Notion;
```

The request must identify, or ask for, the expected output.

### 2. Depth

Depth follows `WORKFLOW_DEPTH_POLICY.md`:

```text
Fast    -> short candidate, minimal checks;
Normal  -> bounded project context;
Deep    -> consequential review with Evidence Pack Candidate and gates.
```

Depth must be visible in the answer.

### 3. Context

Context is not the whole dossier by default.

Minimum useful context may include:

```text
project;
phase;
mission scope;
latest decision;
latest CR;
open observations;
lot / enterprise;
received document;
known constraints;
missing information;
```

Context stays candidate until source status is qualified.

### 4. Reflexes

A reflex is a situation-to-reaction pattern.

```text
situation detected -> checks to perform -> risks to expose -> candidate output -> gates if needed.
```

A reflex is lighter than a workflow. Several reflexes may apply to one request.

### 5. Candidate

The output remains candidate until the human validates it.

Examples:

```text
Summary Candidate;
CCTP Draft Candidate;
CR Draft Candidate;
Material Choice Candidate;
Invoice Review Candidate;
Mission Boundary Reply Candidate;
Notion Observation Candidate;
```

### 6. Gate

A gate is required when the candidate could create:

```text
external effect;
validated Notion / memory state;
canonical project status;
financial approval;
contractual acceptance;
technical validation;
mission extension;
responsibility implication.
```

Preparing is not sending. Drafting is not validation.

## User-facing intents

The user should not need to name reflexes.

Use four simple intents:

```text
Answer   -> explain, summarize, advise internally;
Verify   -> check sources, status, risk, missing information;
Produce  -> prepare a document, CR, CCTP, note, table, mail candidate;
Act      -> write, send, notify, update, validate, file.
```

`Act` always triggers boundary classification before any handoff.

## Reflex families

### Business reflexes

Business reflexes produce domain outputs:

```text
Document Summary Reflex;
Plan Reading Reflex;
CCTP from Plan Reflex;
Cerfa Fill Reflex;
Site Report Finalization Reflex;
Photo Chantier Observation Reflex;
Invoice / Quote Review Reflex;
Lot Scope and Insurance Reflex;
Material Choice Reflex;
Client Response Reflex;
DTU / Local Source Check Reflex;
```

### Safety reflexes

Safety reflexes qualify consequence:

```text
Workflow Depth Triage;
Missing Information Discipline;
Assumption Ledger;
Mission and Responsibility Boundary;
External Action Gate;
Memory / Notion Write Gate;
Evidence Sufficiency Check;
Source Version Check;
```

Business reflexes may be optional. Safety reflexes become mandatory when their trigger is present.

## Default answer card

Every response should start with a compact card when the task is project-facing.

```text
Depth:
Status:
Request understood:
What I can say now:
What is missing:
Risk:
Next action:
```

Detailed evidence, contradictions, assumptions and source tables should remain second-layer unless Deep depth is required.

## Reflex selection rule

Select the fewest reflexes that can safely answer the request.

Examples:

```text
User: “résume ce devis”
Reflexes: Document Summary + Invoice / Quote Review if money risk is present.

User: “on met quoi en facade ?”
Reflexes: Material Choice + Missing Information + Mission Boundary if external output is implied.

User: “fais le CR chantier”
Reflexes: Site Report Finalization + Open Points Reconciliation + Mission Boundary + External Action Gate.

User: “réponds à l’entreprise”
Reflexes: Client / Enterprise Response + Mission Boundary + External Action Gate.
```

Do not activate all known reflexes by default.

## Escalation rule

Escalate only when:

```text
risk trigger appears;
user asks for deeper verification;
source contradiction matters;
external effect is requested;
memory / Notion validated write is requested;
mission boundary is unclear;
financial / contractual / insurance / regulatory / technical consequence appears.
```

Otherwise, keep the answer short.

## Stop rule

Stop instead of over-processing when:

```text
the project is unknown;
the mission scope is unknown and consequence is high;
the source is unreadable;
the target object is unclear;
the official version is unknown for a consequential source;
the user asks for an external action but approval is missing;
a decisive source gap already blocks conclusion.
```

A stop is not a failure. It is a safe status.

## Mission boundary as cross-cutting rule

Every candidate that could be read externally must pass the mission / responsibility check.

```text
Can this be read as validation?
Can this be read as instruction?
Can this widen our mission?
Can this imply technical, financial, planning, insurance or regulatory responsibility?
```

If yes, the output must include limitation wording or be blocked pending human decision.

## Compactness rule

The first answer must be usable in less than one minute.

Recommended first layer:

```text
1. answer / verdict candidate;
2. missing information;
3. risk;
4. next action;
5. gate if needed.
```

Do not present a full Evidence Pack unless the user asks or Deep depth requires it.

## Learning rule

Repeated user corrections may become a Learning Candidate.

They must not automatically become doctrine.

```text
correction -> pattern candidate -> strategy candidate -> reviewed adoption -> baseline.
```

## Final rule

```text
Pantheon does not replace the architect.
It reads, qualifies, links, alerts, prepares and blocks unsafe status transitions.
The architect decides.
```
