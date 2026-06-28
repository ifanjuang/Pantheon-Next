# Card Stack Model

Status: candidate support doctrine — review draft for a card-based cockpit UX built on scenes, decks, cards and a constellation, with the run/task objects living inside the Workflow Scene.

Review status: explicitly open for re-reading with Claude, ChatGPT and human arbitration.

Runtime status: non-executable.

This document is a working model. It is intentionally not final doctrine. It should remain easy to revise while the card UX, scenes, decks, navigation axes, run/task objects, role/competence/rite references, evidence handling and mobile navigation are tested conceptually.

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
which project and subject are active;
which run/treatment is being reviewed;
which cards were mobilized;
which documents and evidences support or weaken the result;
which roles, competences and rites were mobilized;
which gates or questions block transmission;
what can be changed, promoted, refused or validated.
```

The model must be playful enough to use on mobile, but disciplined enough for professional work.

## Hard rule

```text
A card  = one identifiable entity.
A scene = a filtered, ordered presentation of cards.
A deck  = the vertical reading order inside a scene.
A constellation = project switching and global reading.
```

A card may appear in several scenes, but it is never duplicated as a different object merely because another scene displays it. One object, many presentations.

A card family is the entity (a noun), not its lifecycle state. Lifecycle is a status field, not a separate family (see Card families).

## Working thesis

```text
Pantheon is the reference project (referentials).
Real projects carry runs, project documents and project evidences.
A run carries tasks.
Tasks mobilize roles, competences, rites, documents, evidences and decisions by reference.
A subject is a scope label (a project topic) used to filter scenes, not a navigation level.
The Workflow Scene is exhaustive for the cards mobilized in a treatment.
The Evidence Scene is scoped by project and subject.
The Competence Scene is global and neutral.
The Constellation is the map used to change project and read the graph.
Gates remain the decision surfaces.
```

The navigation backbone is three levels: Project → Scene → Deck (→ Card).

French working formula:

```text
Pantheon contient les référentiels.
Les projets contiennent runs, documents et evidences.
Le run contient les tâches.
Le sujet est une étiquette de scope (un thème de projet), pas un niveau de navigation.
La scène Workflow est exhaustive pour les cartes mobilisées.
La scène Evidence est cadrée par projet et sujet.
La scène Compétences est globale et neutre.
La constellation permet de changer de projet.
Les gates exposent le statut et les décisions.
```

This deliberately keeps roles, competences and rites as references (fields) inside a treatment, not as peer scenes inside every project.

## Non-finality rule

This document is a candidate. It may be revised after:

```text
Claude review;
ChatGPT review;
professional UX walkthrough;
mobile prototype testing;
card count testing;
workflow example testing;
architecture-domain example testing.
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

## Navigation specification

One gesture means one thing. The horizontal axis must not mean several different things.

The backbone is three levels: Project → Scene → Deck (→ Card).

| Level | Axis | What it changes | Why |
|---|---|---|---|
| Global | Constellation / project card | Project | Changing project is too heavy for a plain swipe. The constellation orients between projects, subjects, gates, tensions and dependencies. |
| Project | Rail / tabs | Scene | Workflow, Evidence, Documents, Gates, Actions, Traces. |
| Scene | Vertical | Cards of the active deck (deck order) | Read the treatment in order: context, method, sources, evidence, outputs, actions, gates. |
| Scene | Horizontal | Sibling cards / branches at the current level | Optional, when siblings exist (e.g. sibling runs). |
| Card | Tap | Recto / verso | Recto = five-second read; verso = governed detail. |
| Card | Long press | Quick actions | Edit, request source, open gate, archive, merge — never auto-validate. |

A subject is a scope label that filters scenes (e.g. the Evidence Scene scoped to one topic); it is not a navigation level and does not own the horizontal axis.

Formula:

```text
The project is chosen in the constellation.
The scene changes by rail.
The deck reads vertically.
Horizontal moves between sibling cards at the current level.
The card is understood at the recto.
Evidence, trace and gates are checked at the verso.
```

Axis note (open): an alternative candidate assigns left/right to hierarchy depth and up/down to siblings. This document uses the mapping above; the choice remains candidate until mobile testing.

A long press prepares a candidate or opens a gate. It never commits an external effect by itself.

## Scenes and decks

Keep the scenes few but sufficient.

A scene is selected by the rail; its deck reads vertically. The "scope filter"
column is a label (project / subject / status), not a navigation axis.

| Scene / deck | Scope filter | Deck (vertical) | Purpose | Main entities |
|---|---|---|---|---|
| Workflow / Traitement | project + subject + active request | treatment order | understand what is being produced | Run, Task, context, method, sources, evidence, role qualities, draft, actions, gates, trace |
| Evidence / Preuves | project + subject | assertions / proofs / gaps | verify what supports a claim | Assertion, source, evidence, contradiction, gap, status |
| Documents / Sources / Connaissances | project or global, by category | documents then extracted knowledge | separate raw file, source, professional knowledge | Document, source, project knowledge, métier knowledge |
| Gates / Arbitrages | project, subject or global | open / blocked / resolved | see what awaits decision | Gate, arbitration, expected decision, options |
| Actions | project + subject or global | candidate / ready / blocked | track what can be done or sent | candidate email, Notion write candidate, export, reminder |
| Traces / Mémoire | project + subject | trace, memory candidate, register | know what was done, kept, validated or abandoned | Trace, ledger, memory candidate, register |
| Compétences | global, not project, by competence subject | maturity | capitalize reusable capability | Competence (with maturity field) |
| Templates / Ressources | global or métier, by family | templates and guides | reuse without confusing with proof | Template, guide, resource, example |
| Constellation | global | visual relations | global orientation | projects, subjects, tensions, gates, dependencies |

The Competence Scene stays global and neutral: a competence may be used by a project, but never becomes project-owned.

## Pantheon reference project vs real project

### Pantheon project

`Pantheon` is the reference project, not a client dossier. It holds reusable governance and professional method material:

```text
Pantheon
→ Documents (references, doctrine, lexicons)
→ Roles (definitions, qualities, limits)
→ Competences (definitions, reusable method, maturity)
→ Rites (procedures, not runtime steps)
→ Run types (reusable governed methods)
```

These reference scenes are global and neutral; they are not owned by a project dossier.

### Real project

A real project is a dossier. It contains only its own material:

```text
Project
→ Subjects
→ Runs
→ Documents
→ Evidences
```

Roles, competences and rites do not become project scenes by default. They are referenced from tasks when mobilized.

## Card families — entity, not lifecycle state

Families stay compact. A family is the entity; lifecycle is a status field.

Primary visible families:

```text
Project
Subject
Scene
Run
Task
Document
Connaissance
Evidence
Decision        (subtypes: Question, Approval, Gate, Arbitration, Escalation)
Record          (statuses: working, memory_candidate, register, obsolete)
Competence      (maturity: durable, candidate, on-the-flow, need, gap)
Role
Rite
Constellation
```

Two consolidations versus an earlier draft:

```text
Draft / Memory Candidate / Register / Promotion / Obsolete are NOT five families.
They are statuses of one Record (a fact/output/decision moving through its lifecycle),
consistent with the "one object, N revisions" invariant (ITERATIVE_DELIBERATION_LIFECYCLE.md).

Competence and Competence-on-the-flow are one family with a maturity field, not two.
```

Field-versus-sub-card rule:

```text
Field if normal.
Sub-card if it works, blocks, fails, repeats, is newly proposed or requires arbitration.
```

| Element | Default inside a task | Becomes a visible sub-card when |
|---|---|---|
| Role | responsible / contributor / arbitrator | role conflict, external expertise, new role, arbitration, handoff. |
| Competence | competence reference | competence missing, failed, repeated, proposed, productive output requested. |
| Rite | rite reference | proof gap, mission limit, responsibility issue, memory promotion, pre-transmission check. |
| Risk | field on Run / Task / Evidence / Decision (C / K axes) | impact is high enough to block or require arbitration. |
| Scope | field on Run / Rite / Decision / Result | mission boundary or responsibility changes the allowed output. |
| Question | Decision subtype | information required from user, MOA, enterprise, BET, authority or Zeus. |
| Gate | Decision subtype | truth, approval, memory, external action or professional commitment is at stake. |
| Action Candidate | productive competence subtype | drafting, PDF production, avenant preparation, task-list production or handoff is requested. |

Role / God cards show useful quality expressions, not activated agents, and appear only when a quality changes the treatment (see `CARD_STACK_ROLE_QUALITY_ALIGNMENT.md`).

## Universal card field contract

Every card carries a minimal recto and a stable verso.

Recto — five-second read:

```text
[Title]
Family · Scope
Status · Risk
1-line summary
Next action
Gate: yes / no
```

```text
Status reuses the governed status vocabulary (candidate / to_verify / gate_open /
validated / refused / out_of_scope). Risk reuses the existing C (consequence) and
K (approval) axes and E0–E4 certainty — not a parallel faible/moyen/fort scale.
```

Verso — governed detail:

| Section | Content |
|---|---|
| Definition | what the card represents |
| Source / origin | where it comes from |
| Detailed status | why this status |
| Useful links | sources, evidence, gates, actions |
| History | creation, modifications, trace |
| Risks | mission, proof, memory, action, finance |
| Possible actions | edit, request source, open gate, archive — never auto-validate |
| Limits | what the card does not decide |

## Typed, capped, local links

Links are typed and local, so the interface never shows ten arrows per card.

| Link type | Recommended max | Example |
|---|---:|---|
| Parent | 1 | Evidence → Subject |
| Main source | 1–3 | Evidence → Document |
| Affects | 1–5 | Gate → Action / Draft |
| Produces | 1–3 | Run → Draft / Action |
| Blocks | 1–3 | Gap → Gate |
| Supports | 1–5 | Evidence → Assertion |
| Contradiction | rare | Evidence A ↔ Evidence B |
| Promotion | 1 | Competence-on-the-flow → Competence (candidate maturity) |
| Trace | many, collapsed | grouped Trace cards |

```text
A card shows only its main link on the recto.
The verso shows the useful links.
The constellation shows the many relations.
```

## Status model

Cards separate process status from governance status.

| Status axis | Values |
|---|---|
| processStatus | waiting, processing, success, error |
| governanceStatus | candidate, to_verify, gate_open, validated, refused, out_of_scope |

```text
Process success does not mean governance validation.
Governance validation does not mean runtime execution.
Runtime execution does not mean external action approval.
```

## Workflow Scene — the run/task deck

The Workflow Scene is the complete narrative of a treatment. Its deck contains the run and its task sequence, plus only the cards actually mobilized.

### Run card

The Run Card is the head of the run; the run declares the expected result (no separate peer "Result Candidate" card).

Recto: run title, methodology, expected result, final confidence check, process status, governance status, expected outputs, open gates, date / indice / version.

Verso: process state, planned tasks, added tasks/sub-cards, documents used, evidences produced, roles/competences/rites mobilized, risks, scope limits, open decisions, run event journal summary.

### Task card

The Task Card is the operational unit; it aggregates references to roles, competences, rites, documents, evidences and decisions.

Recto: task title, methodology, expected result, confidence check, process status, governance status, responsible role, competences mobilized, documents linked, evidences linked/expected, date / indice / instance.

Verso: trigger, inputs, steps, output, gaps, roles consulted, rites triggered, decisions linked, sub-cards spawned, short run-event history.

A task always has one main responsible role.

| Field | Cardinality | Meaning |
|---|---:|---|
| responsibleRole | 1 | Main role accountable for the task posture. |
| contributorRoles | 0..n | Roles consulted or assisting. |
| arbitrationRole | 0..1 | Zeus or user if a decision must be arbitrated. |
| externalExpertRoles | 0..n | BET, jurist, economist, authority, enterprise, MOA. |

Guideline:

```text
Active analytical or productive task -> at least one competence expected.
Passive wait / document receipt / blocked gate -> zero competence acceptable.
Competence productive -> prepares a candidate output.
Decision / Gate -> authorizes or blocks an external effect.
```

### Spawned cards expose their origin

The deck shows no `Flow Adaptation Card`. When a confidence check fails or a signal is detected, the new useful card appears in its real nature (Document, Evidence, Decision/Gate, Decision/Question, Competence, Rite) and exposes its origin:

```yaml
origin: added
spawnedBy: task-or-card-id
spawnReason: why it appeared
spawnTrigger: confidence-check-or-signal
spawnedAtStep: run step number
```

### Default CR deck order (human-logical)

```text
1  Project compact     where am I?
2  Subject             what topic?
3  Run / Method        which method, what status?
4  Constraint Ledger   pinned constraints and decisions
5  Context             mission, phase, scope
6  Documents / Sources notes, prior CR, photos, mails, CCTP
7  Evidence            candidate assertions + proofs + gaps
8  Method / Procedure  method, tactics used
9  Role qualities      only qualities that change the treatment
10 Draft Output        CR / mail / note / table (Record, status working)
11 Actions             prepared: mail, Notion, export
12 Gates               decisions to take
13 Trace / Memory      what stays as trace or may be promoted
```

### Answer-first default

The deck above is the full, comprehensive view. The Workflow Scene should NOT open on all thirteen cards. The default landing state is answer-first:

```text
Draft Output + main Gate + top Evidence,
with the full deck available on demand (expand),
and the primary gate kept visible as a sticky badge while scrolling.
```

Comprehensiveness is available, not the landing screen.

## Other scenes

```text
Evidence Scene: project + subject scoped. Assertion -> source/evidence -> status.
  Not global by default. Shows contradictions, gaps, validated and obsolete evidence,
  affected actions and gates.
Documents Scene: distinguishes Document (raw support), Source, Connaissance (structured
  professional/regulatory/contractual knowledge). A document never moves from received to
  trusted without being classified, dated, scoped and qualified.
Gates Scene: open / blocked / resolved gates awaiting decision.
Actions Scene: candidate / ready / blocked actions; external effect stays gated.
Traces / Memory Scene: trace, constraint & decision ledger (working state), memory
  candidate, register. The ledger is governed working state, never canon.
Competences Scene: global and neutral; maturity vertical (durable / candidate /
  on-the-flow / need / gap); usage references do not make a competence project-owned.
Constellation: orientation only, not the main decision surface. Gates remain decisive.
```

## Examples

### Reception of a complementary quotation

```text
Project: Les Damps · Subject: devis complementaire · Scene: Workflow
Run: Reception devis complementaire
Expected result: a justified candidate opinion, checked contractually, technically and
financially, before MOA transmission and possible avenant preparation.
```

| Order | Task | Responsible | Competences | Expected result |
|---:|---|---|---|---|
| 1 | Qualifier le devis reçu | Maître | document intake, quote qualification | Quote identified. |
| 2 | Vérifier les pièces marché | Maître | document review | Corpus available or gaps exposed. |
| 3 | Analyse contractuelle | Maître | lecture CCTP, hors marché, avenant | Included / outside market / receivable / not. |
| 4 | Analyse technique | Athéna | technical coherence | Necessity and feasibility candidate. |
| 5 | Analyse financière | Athéna | price/quantity/duplicate check | Financial coherence candidate. |
| 6 | Justification avis | Athéna | evidence packaging | Claims linked to documents or marked weak. |
| 7 | Limite mission | Maître | scope discipline | What can be said without over-committing. |
| 8 | Production avis candidat | Athéna | synthesis, drafting | Candidate opinion with reserves. |
| 9 | Préparation avenant | Maître | productive competence | Candidate avenant material if receivable. |
| 10 | Rédaction mail MOA | Hermès | productive competence | Draft email only, not sent. |
| 11 | Transmission MOA | Zeus / user | decision gate | Send / correct / block / ask for evidence. |

Spawned cards on signals: CCTP missing → Document sub-card; prestation not found → Evidence sub-card; price incoherent → Decision/Question; out-of-mission wording → Rite sub-card; external transmission → Decision/Gate.

### Chantier report production

```text
Subject: visite de chantier · Run: Elaboration CR chantier
Sequence: qualify inputs; read previous CR; classify new/maintained/closed points; link
photos to observations; produce evidence candidates; apply mission-limit rite; produce CR
candidate; prepare draft email; open transmission gate.
Spawned: Evidence (photo non localisée); Decision/Question (autre angle); Rite (formulation
prudente); Decision/Gate (envoi CR bloqué).
```

### Post-client-meeting task preparation

```text
Subject: réunion client · Run: Preparation liste de taches
Sequence: extract requests; separate wishes/decisions/assumptions; check project and mission
scope; identify feasibility checks; create candidate task list; assign responsible roles;
open questions and gates; prepare follow-up message if requested.
Core distinction:
  Client wish is not project decision.
  Project decision is not agency task.
  Agency task is not external action.
  External action is not approved action.
```

## What to avoid

| Bad card | Why | Replacement |
|---|---|---|
| "Full CR chantier card" | becomes a mini-dossier | Run + Draft Output + Evidence + Gates |
| "AI / God card" with a character | decorative, vague | Role quality card only when a quality changes the treatment |
| "Proof/document card" | conflates source and proof | Document card, then Evidence card |
| "Decision/memory card" | conflates arbitration and canon | Gate card, then Record (memory candidate / register) |
| "Project competence card" | makes the competence project-owned | global Competence card + usage reference |
| "Validated action card" | implicit execution | Action card + separate Gate card |
| "Everything-linked graph card" | unreadable | Constellation as a view, not a decision entity |
| Family per lifecycle state | inflates families | one Record family + a status field |

## Relationship with other documents

```text
ITERATIVE_DELIBERATION_LIFECYCLE.md — the deliberation behind a Workflow Scene; the
  Constraint & Decision Ledger surfaces here as a pinned working-state card.
CARD_STACK_ROLE_QUALITY_ALIGNMENT.md — Role / God cards as quality expressions, not agents.
COMPETENCE_MODEL.md — Connaissance / Guide / Ressource / Competence vocabulary.
WORKFLOW_LIFECYCLE.md — authority, testing, activation and execution boundaries; this
  document governs the visible run/task/project structure, not execution.
```

A task card may display a workflow proposal or runtime result, but it does not authorize execution.

## Design warning

The model must resist card inflation.

```text
Do not create a visible card for every concept.
Create visible cards only when the object is orienting, working, blocking, repeated,
newly proposed or decision-bearing.
A family is an entity; lifecycle is a status field.
```

The validated remains.

## Boundary

This document is a UX / governance candidate.

It creates no runtime, no UI, no schema, no database, no tool call, no connector, no skill, no approval engine and no memory engine. Any implementation belongs later in the appropriate exposure surface or execution runtime, under the existing placement doctrine, and remains a candidate until reviewed.
