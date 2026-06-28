# Card Stack Model

Status: candidate support doctrine — review draft for card-based cockpit UX, project/reference separation and run-task navigation.

Review status: explicitly open for re-reading with Claude, ChatGPT and human arbitration.

Runtime status: non-executable.

This document is a working model. It is intentionally not final doctrine. It should remain easy to revise while the card UX, project scenes, run cards, task cards, role references, rites, competences, evidence handling and mobile navigation are tested conceptually.

It does not implement a UI, mobile app, Swiper component, dashboard, frontend route, card renderer, state machine, runtime, workflow engine, graph database, scheduler, queue, skill generator, competence engine, evidence engine, approval engine, memory engine, OpenWebUI Function, OpenWebUI Tool, OpenWebUI Pipe, OpenWebUI Action, Hermes skill, connector or external action.

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
which roles, competences and rites were mobilized;
which gates or questions block transmission;
what can be changed, promoted, refused or validated.
```

The model must be playful enough to use on mobile, but disciplined enough for professional work.

## Current working thesis

```text
Pantheon is the reference project.
Real projects carry runs, project documents and project evidences.
Runs carry tasks.
Tasks mobilize roles, competences, rites, documents, evidences and decisions by reference.
```

French working formula:

```text
Pantheon contient les référentiels.
Les projets contiennent les dossiers réels.
Les runs contiennent les tâches.
Les tâches mobilisent les rôles, compétences, rites, documents, evidences et décisions.
```

This replaces the earlier broad idea that every role, competence, rite, evidence, document, gate and action should appear as peer scenes inside every project.

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

No section of this document promotes a schema, runtime, UI, role, rite, competence, memory rule or implementation.

## Boundary with workflow runtimes

This model is a cockpit and governance grammar. It is not a workflow runner.

A run may be displayed as if it has steps, tasks and progression, but Pantheon does not execute those steps. Execution remains in the appropriate runtime or tool. Pantheon governs status, scope, evidence, approval, memory and external action boundaries.

```text
Task shown is not task executed.
Runtime success is not governance success.
Candidate result is not truth.
Evidence candidate is not proof.
Draft prepared is not transmission approved.
```

## Top-level project separation

### Pantheon project

`Pantheon` is the reference project. It is not a client dossier.

It contains reusable governance and professional method material:

```text
Pantheon
→ Documents
→ Roles
→ Competences
→ Rites
→ Run types
```

These scenes are global and neutral. They are not owned by a project dossier.

| Scene | Content | Notes |
|---|---|---|
| Documents | MAF recommendations, PLU reference patterns, CCTP guides, doctrine, lexicons | General references only; not project proof by themselves. |
| Roles | Zeus, Maître, Athéna, Hermès and other role definitions | Definitions, qualities, responsibilities, limits. |
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

Roles, competences and rites do not become project scenes by default. They are referenced from tasks when mobilized.

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
```

## Card versus reference

A card visible in a run may reference an object from Pantheon or from the project.

```text
Competence in Pantheon = reusable definition.
Competence in a task = mobilized instance or reference.

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

`Role`, `Competence` and `Rite` remain visible as reference scenes inside `Pantheon`. Inside a real project run, they appear first as task fields or linked references.

They become visible sub-cards only when they carry process state.

| Element | Default inside a task | Becomes visible sub-card when |
|---|---|---|
| Role | responsible / contributor / arbitrator | role conflict, external expertise, new role, arbitration, handoff. |
| Competence | competence reference | competence missing, failed, repeated, proposed, productive output requested. |
| Rite | rite reference | proof gap, mission limit, responsibility issue, memory promotion, pre-transmission check. |
| Risk | field in Run / Task / Evidence / Decision | impact is high enough to block or require arbitration. |
| Scope | field in Run / Rite / Decision / Result | mission boundary or responsibility changes the allowed output. |
| Question | Decision subtype | information required from user, MOA, enterprise, BET, authority or Zeus. |
| Gate | Decision subtype | truth, approval, memory, external action or professional commitment is at stake. |
| Action Candidate | productive competence subtype | drafting, PDF production, avenant preparation, task-list production or handoff is requested. |

## Run card

A Run Card is the head card of a run.

It replaces the older idea of treating `Result Candidate` as an ordinary peer card. The run itself must declare the expected result.

Recto should show:

```text
Run title
methodology
expected result
final confidence check
process status
governance status
expected outputs
open gates
date / indice / version
```

Verso should show:

```text
process state;
planned tasks;
added tasks or sub-cards;
documents used;
evidences produced;
roles / competences / rites mobilized;
risks;
scope limits;
open decisions;
run event journal summary.
```

Example:

```text
Run — Reception devis complementaire

Expected result:
Produce a justified candidate opinion, checked contractually, financially and technically, before MOA transmission and possible avenant preparation.

Final confidence check:
Can the advice be supported by project documents, technical reasoning, financial verification and mission-scope discipline, with no unresolved gate?

Expected outputs:
- candidate opinion;
- verification summary;
- draft MOA email;
- candidate avenant preparation.
```

## Task card

A Task Card is the operational unit of a run.

A run contains tasks. A task aggregates references to roles, competences, rites, documents, evidences and decisions.

Recto should show:

```text
task title;
methodology;
expected result;
confidence check;
process status: waiting / processing / success / error;
governance status: candidate / to verify / gate open / validated / refused / out of scope;
responsible role;
competences mobilized;
documents linked;
evidences linked or expected;
date / indice / instance.
```

Verso should show:

```text
process: in progress / completed;
trigger;
inputs used;
steps performed;
output produced;
gaps;
roles consulted;
rites triggered;
decisions linked;
sub-cards spawned;
short run-event history.
```

A task should always have one main responsible role.

A task may have:

```text
zero or more contributor roles;
zero or more competence references;
zero or more rite references;
zero or more document references;
zero or more evidence references;
zero or more decision references.
```

Guideline:

```text
Active analytical or productive task -> at least one competence expected.
Passive wait / document receipt / blocked gate -> zero competence acceptable.
```

## Task responsibility model

| Field | Cardinality | Meaning |
|---|---:|---|
| responsibleRole | 1 | Main role accountable for the task posture. |
| contributorRoles | 0..n | Roles consulted or assisting. |
| arbitrationRole | 0..1 | Zeus or user if a decision must be arbitrated. |
| externalExpertRoles | 0..n | BET, jurist, economist, authority, enterprise, MOA or other external expertise. |

Example:

```yaml
task: Analyse contractuelle devis complementaire
responsibleRole: maitre
contributorRoles:
  - athena
arbitrationRole: zeus
externalExpertRoles: []
competenceRefs:
  - lecture-cctp
  - qualification-hors-marche
  - preparation-avenant
riteRefs:
  - preuve-suffisante
  - limite-mission
```

## Competence inside a task

A competence is a reusable method definition in Pantheon.

Inside a task, it becomes a mobilized reference or a visible sub-card.

### Competence as field

Use when the competence works normally.

```text
Competences:
lecture CCTP · analyse contractuelle · qualification avenant
```

### Competence as sub-card

Use when the competence has its own status.

Examples:

```text
Competence missing: analyse structure required.
Competence failed: financial check impossible because DPGF absent.
Competence repeated: mission-limit check instance B before MOA email.
Competence productive: draft MOA email, produce PDF, prepare avenant.
```

Productive actions are competence subtypes, not external actions.

```text
Competence productive -> prepares candidate output.
Decision / Gate -> authorizes or blocks external effect.
```

## Role inside a task

Roles should not multiply as visible cards in normal cases.

Use fields:

```text
Responsible: Maître
Contributors: Athéna, Hermès
Arbitration: Zeus
```

Create a visible Role sub-card only when the role relation becomes a process object:

```text
external expert required;
role conflict;
new role proposed;
role handoff;
Zeus arbitration needed;
responsibility boundary unclear.
```

## Rite inside a task

Rites are procedures defined in Pantheon and applied in task context.

Use fields when normal:

```text
Rites applied:
proof sufficiency · mission limit
```

Create a visible Rite sub-card when the rite opens, blocks or changes the run:

```text
proof insufficient;
out-of-mission wording detected;
memory promotion requested;
pre-transmission gate needed;
professional responsibility risk detected.
```

## Documents and evidences

Documents and evidences exist as project scenes because they are durable dossier material.

A task references documents and evidences. It may also create evidence candidates.

```text
Project / Documents -> source material.
Project / Evidences -> proof candidates or governed evidences.
Task / Documents -> documents used by reference.
Task / Evidences -> evidences used or produced by reference.
```

A document, photo, message, table, mail, quote or drawing must not move directly from received to trusted. It must be classified, dated, scoped and qualified before it can support a conclusion.

## Decisions

Decision is a compact family for questions, approvals, gates, arbitrations and escalations.

| Subtype | Meaning |
|---|---|
| Question | Information is needed. |
| Approval | User must validate an orientation or draft. |
| Gate | Consequential effect is blocked until explicit decision. |
| Arbitration | Conflicting interpretations must be resolved. |
| Escalation | External or higher authority is required. |

Gate remains the hard subtype. Use it for truth, approval, memory, external action, scope or professional commitment.

## Spawned cards without Flow Adaptation card

The deck should not show a `Flow Adaptation Card` by default.

When a confidence check fails or a signal is detected, the new useful card appears directly in its real nature:

```text
Document missing -> Document sub-card.
Proof weak -> Evidence sub-card.
External action possible -> Decision / Gate.
Question needed -> Decision / Question.
Competence missing -> Competence sub-card.
Rite triggered -> Rite sub-card.
```

Each spawned card must expose its origin.

Minimum fields:

```yaml
origin: added
spawnedBy: task-or-card-id
spawnReason: why it appeared
spawnTrigger: confidence-check-or-signal
spawnedAtStep: run step number
spawnBatchId: optional group id
```

The run may keep a `FlowEvent` journal internally, but this is not a visible card family by default.

## Status model

Cards should separate process status from governance status.

| Status axis | Values |
|---|---|
| processStatus | waiting, processing, success, error |
| governanceStatus | candidate, to_verify, gate_open, validated, refused, out_of_scope |

Important distinction:

```text
Process success does not mean governance validation.
Governance validation does not mean runtime execution.
Runtime execution does not mean external action approval.
```

## Navigation model — current candidate

The current mobile deck candidate uses two axes:

```text
Right -> descend hierarchy.
Left  -> ascend hierarchy.
Up / down -> sibling cards at the current level.
```

The breadcrumb may be rendered inside each card:

```text
home / project / scene / run / task
```

Breadcrumb items should be clickable, visually quiet and borderless.

The navigation model remains candidate. It may change after mobile testing.

## Example — complementary quotation reception

```text
Project: Les Damps
Scene: Runs
Run: Reception devis complementaire
```

Run expected result:

```text
Produce a justified candidate opinion on a complementary quotation, checked contractually, technically and financially, before MOA transmission and possible avenant preparation.
```

Planned tasks:

| Order | Task | Responsible | Competences | Expected result |
|---:|---|---|---|---|
| 1 | Qualifier le devis reçu | Maître | document intake, quote qualification | Quote identified: enterprise, lot, date, indice, amount, object. |
| 2 | Vérifier les pièces marché | Maître | document review | Contractual corpus available or gaps exposed. |
| 3 | Analyse contractuelle | Maître | lecture CCTP, hors marché, avenant | Included / outside market / receivable under reserve / not receivable. |
| 4 | Analyse technique | Athéna | technical coherence, interfaces | Technical necessity and feasibility candidate. |
| 5 | Analyse financière | Athéna | price check, quantity check, duplicate detection | Financial coherence candidate. |
| 6 | Justification avis | Athéna | evidence packaging | Claims linked to documents or marked weak. |
| 7 | Limite mission / responsabilité | Maître | scope discipline | What can be said without over-committing the agency. |
| 8 | Production avis candidat | Athéna | synthesis, professional drafting | Candidate opinion with reserves. |
| 9 | Préparation avenant | Maître | productive competence | Candidate avenant material if receivable. |
| 10 | Rédaction mail MOA | Hermès | productive competence | Draft email only, not sent. |
| 11 | Transmission MOA | Zeus / user | decision gate | Send / correct / block / ask for more evidence. |

Possible spawned cards:

| Signal | Spawned card |
|---|---|
| CCTP missing | Document sub-card: CCTP absent. |
| prestation not found in market pieces | Evidence sub-card: prestation non justifiée contractuellement. |
| structure issue detected | Decision / Escalation: avis structure requis. |
| price incoherent | Evidence or Decision / Question: demander décomposition. |
| out-of-mission wording | Rite sub-card: limite mission. |
| external transmission possible | Decision / Gate: validation before MOA. |

## Example — chantier report production

```text
Project: active project
Scene: Runs
Run: Elaboration CR chantier
```

Expected result:

```text
Produce a candidate chantier report from notes, photos, previous CR, decisions and open points, while preserving mission limits and blocking external transmission until approval.
```

Core task sequence:

```text
qualify inputs;
read previous CR;
classify new / maintained / closed points;
link photos to observations;
produce evidence candidates;
apply mission-limit rite;
produce CR candidate;
prepare draft email;
open transmission gate.
```

Typical spawned cards:

```text
Evidence: photo non localisée;
Decision / Question: demander autre angle;
Rite: formulation prudente;
Decision / Gate: envoi CR bloqué.
```

## Example — post-client-meeting task preparation

```text
Project: design-stage project
Scene: Runs
Run: Preparation liste de taches apres rendez-vous client
```

Expected result:

```text
Transform client-meeting notes into a candidate task list while distinguishing client wishes, project decisions, feasibility checks, agency tasks and external actions.
```

Core task sequence:

```text
extract requests;
separate wishes / decisions / assumptions;
check project and mission scope;
identify feasibility checks;
create candidate task list;
assign responsible roles;
open questions and gates;
prepare follow-up message if requested.
```

Core distinction:

```text
Client wish is not project decision.
Project decision is not agency task.
Agency task is not external action.
External action is not approved action.
```

## Relationship with `WORKFLOW_LIFECYCLE.md`

`WORKFLOW_LIFECYCLE.md` governs the lifecycle of workflows before they affect professional records or external communications.

This document governs the cockpit grammar used to display runs and tasks.

They are complementary:

```text
Workflow lifecycle -> authority, testing, activation and execution boundaries.
Card stack model -> visible run/task/project structure and governance objects.
```

A task card may display a workflow proposal or runtime result, but it does not authorize execution.

## Design warning

The model must resist card inflation.

```text
Do not create a visible card for every concept.
Create visible cards only when the object is orienting, working, blocking, repeated, newly proposed or decision-bearing.
```

The validated remains.
