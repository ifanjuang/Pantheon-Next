# Card Stack Model

Status: candidate support doctrine — review draft for card-based cockpit UX, project/reference separation and run-task navigation.

Review status: explicitly open for re-reading with Claude, ChatGPT and human arbitration.

Runtime status: non-executable.

This document is a working model. It is intentionally not final doctrine. It should remain easy to revise while the card UX, project scenes, run cards, task cards, role references, rites, methods, competences, evidence handling and mobile navigation are tested conceptually.

It does not implement a UI, mobile app, Swiper component, dashboard, frontend route, card renderer, state machine, runtime, workflow engine, graph database, scheduler, queue, skill generator, competence engine, evidence engine, method selector, reasoning engine, approval engine, memory engine, OpenWebUI Function, OpenWebUI Tool, OpenWebUI Pipe, OpenWebUI Action, Hermes skill, connector or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon needs a cockpit UX that makes governance visible without turning governance into a technical maze.

The card model must let the user understand:

```text
where they are;
which project is active;
which run is being reviewed;
which task is currently being processed;
which documents were used;
which evidences support or weaken the result;
which roles, methods, competences and rites were mobilized;
which gates or questions block transmission;
what can be changed, promoted, refused or validated.
```

The model must be playful enough to use on mobile, but disciplined enough for professional work.

## Current working thesis

```text
Pantheon is the reference project.
Real projects carry runs, project documents and project evidences.
Runs carry tasks.
Tasks mobilize roles, methods, competences, rites, documents, evidences and decisions by reference.
```

French working formula:

```text
Pantheon contient les référentiels.
Les projets contiennent les dossiers réels.
Les runs contiennent les tâches.
Les tâches mobilisent les rôles, méthodes, compétences, rites, documents, evidences et décisions.
```

This replaces the earlier broad idea that every role, method, competence, rite, evidence, document, gate and action should appear as peer scenes inside every project.

## Non-finality rule

This document is deliberately written as a candidate.

It may be revised after:

```text
Claude review;
ChatGPT review;
professional UX walkthrough;
mobile prototype testing;
card count testing;
workflow example testing;
architecture-domain example testing;
Langflow / LangGraph / Flowise / Dify adapter comparison.
```

No section of this document promotes a schema, runtime, UI, role, method, rite, competence, memory rule or implementation.

## Boundary with workflow runtimes

This model is a cockpit and governance grammar. It is not a workflow runner.

A run may be displayed as if it has steps, tasks and progression, but Pantheon does not execute those steps. Execution remains in the appropriate runtime or tool. Pantheon governs status, scope, evidence, approval, memory and external action boundaries.

```text
Task shown is not task executed.
Runtime success is not governance success.
Candidate result is not truth.
Evidence candidate is not proof.
Draft prepared is not transmission approved.
Method selected is not reasoning validated.
```

## Top-level project separation

### Pantheon project

`Pantheon` is the reference project. It is not a client dossier.

It contains reusable governance and professional method material:

```text
Pantheon
→ Documents
→ Roles
→ Methods / Reasoning
→ Competences
→ Rites
→ Run types
```

These scenes are global and neutral. They are not owned by a project dossier.

| Scene | Content | Notes |
|---|---|---|
| Documents | MAF recommendations, PLU reference patterns, CCTP guides, doctrine, lexicons | General references only; not project proof by themselves. |
| Roles | Zeus, Maître, Athéna, Hermès and other role definitions | Definitions, qualities, responsibilities, limits. |
| Methods / Reasoning | Deduction, abduction, Occam, Sagan, premortem, inversion, second-order thinking, via negativa, reframing and other reasoning structures | Structures thought; does not judge, produce, prove, approve or execute. |
| Competences | Analysis, verification, synthesis, drafting, PDF production, task-list production, contract qualification | Competence definitions and reusable method. |
| Rites | Proof sufficiency, mission limit, responsibility, pre-transmission gate, memory promotion, evidence review | Procedures, not runtime steps. |
| Run types | CR chantier, reception of complementary quotation, post-client-meeting task preparation | Reusable governed methods. |

### Real project

A real project is a dossier.

It contains only the material that belongs to the actual project:

```text
Project
→ Runs
→ Documents
→ Evidences
```

| Scene | Content | Notes |
|---|---|---|
| Runs | Runs in progress, completed runs, run candidates | Operational view. |
| Documents | Project-specific documents, mails, plans, photos, quotes, reports | Source status must be visible. |
| Evidences | Project-specific evidence candidates or governed evidences | Not automatically promoted by runtime success. |

Roles, methods, competences and rites do not become project scenes by default. They are referenced from tasks when mobilized.

## Core hierarchy

```text
Pantheon / Project
→ Scene
→ Run
→ Task
→ Detail
```

For a real project:

```text
Les Damps
→ Runs
→ Reception devis complementaire
→ Taches
→ Analyse contractuelle
```

For the reference project:

```text
Pantheon
→ Competences
→ Analyse contractuelle

Pantheon
→ Methods / Reasoning
→ Abduction
```

## Card versus reference

A card visible in a run may reference an object from Pantheon or from the project.

```text
Competence in Pantheon = reusable definition.
Competence in a task = mobilized instance or reference.

Method in Pantheon = reusable reasoning structure.
Method in a task = mobilized reasoning approach or contested prescription.

Rite in Pantheon = procedure definition.
Rite in a task = applied instance or triggered check.

Role in Pantheon = role definition.
Role in a task = responsible, contributor, arbitrator or external expert.
```

The run should not duplicate the full Pantheon reference card unless the referenced item becomes important to the current process.

Practical rule:

```text
Field if normal.
Sub-card if it works, blocks, fails, repeats, is newly proposed or requires arbitration.
```

## Visible card families

The visible families should stay compact.

```text
Project
Scene
Run
Task
Document
Evidence
Decision
```

`Role`, `Method`, `Competence` and `Rite` remain visible as reference scenes inside `Pantheon`. Inside a real project run, they appear first as task fields or linked references.

They become visible sub-cards only when they carry process state.

| Element | Default inside a task | Becomes visible sub-card when |
|---|---|---|
| Role | responsible / contributor / arbitrator | role conflict, external expertise, new role, arbitration, handoff. |
| Method | reasoning reference | method proposed, contested, failed, repeated, changed, requires fidelity check or fitness check. |
| Competence | competence reference | competence missing, failed, repeated, proposed, productive output requested. |
| Rite | rite reference | proof gap, mission limit, responsibility issue, memory promotion, pre-transmission check. |
| Risk | field in Run / Task / Evidence / Decision | impact is high enough to block or require arbitration. |
| Scope | field in Run / Rite / Decision / Result | mission boundary or responsibility changes the allowed output. |
| Question | Decision subtype | information required from user, MOA, enterprise, BET, authority or Zeus. |
| Gate | Decision subtype | truth, approval, memory, external action or professional commitment is at stake. |
| Action Candidate | productive competence subtype | drafting, PDF production, avenant preparation, task-list production or handoff is requested. |

## Method cards

Method Cards are documented separately in `METHOD_CARD_MODEL.md`.

Core invariant:

```text
A Method Card structures thought.
It does not decide status.
It does not prove content.
It does not authorize action.
It does not execute.
```

Practical formula:

```text
Role regarde.
Method structure.
Competence produces.
Evidence supports.
Gate authorizes or blocks.
Human decides.
```
