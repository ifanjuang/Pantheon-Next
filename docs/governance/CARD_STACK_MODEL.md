# Card Stack Model

Status: candidate support doctrine — review draft for a card-based cockpit UX built on scenes, decks, cards and a constellation, with the run/task objects living inside the Workflow Scene.

Review status: explicitly open for re-reading with Claude, ChatGPT and human arbitration.

Runtime status: non-executable.

This document is a working model. It is intentionally not final doctrine. It should remain easy to revise while the card UX, scenes, decks, navigation axes, run/task objects, role/method/competence/rite references, evidence handling and mobile navigation are tested conceptually.

It does not implement a UI, mobile app, Swiper component, dashboard, frontend route, card renderer, state machine, runtime, workflow engine, graph database, scheduler, queue, skill generator, competence engine, method selector, reasoning engine, evidence engine, approval engine, memory engine, OpenWebUI Function, OpenWebUI Tool, OpenWebUI Pipe, OpenWebUI Action, Hermes skill, connector or external action.

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
which roles, methods, competences and rites were mobilized;
which gates or questions block transmission;
what can be changed, promoted, refused or validated.
```

The model must be playful enough to use on mobile, but disciplined enough for professional work.

## Hard rule

```text
A card  = one identifiable entity.
A scene = a filtered, ordered presentation of cards.
A deck  = the vertical reading / depth order inside a scene.
A constellation = project switching and global reading.
```

A card may appear in several scenes, but it is never duplicated as a different object merely because another scene displays it. One object, many presentations.

A card family is the entity, not its lifecycle state. Lifecycle is a status field, not a separate family.

## Working thesis

```text
Pantheon is the reference project (referentials).
Real projects carry runs, project documents and project evidences.
A run carries tasks.
Tasks mobilize roles, methods, competences, rites, documents, evidences and decisions by reference.
A subject is a scope label used to filter scenes, not a navigation level.
The Workflow Scene is exhaustive for the cards mobilized in a treatment.
The Evidence Scene is scoped by project and subject.
The Competence and Method scenes are global and neutral.
The Constellation is the map used to change project and read the graph.
Gates remain the decision surfaces.
```

The navigation backbone is three levels:

```text
Project -> Scene -> Deck -> Card / sub-card
```

French working formula:

```text
Pantheon contient les référentiels.
Les projets contiennent runs, documents et evidences.
Le run contient les tâches.
Le sujet est une étiquette de scope, pas un niveau de navigation.
La scène Workflow est exhaustive pour les cartes mobilisées.
La scène Evidence est cadrée par projet et sujet.
Les scènes Compétences et Méthodes sont globales et neutres.
La constellation permet de changer de projet.
Les gates exposent le statut et les décisions.
```

This deliberately keeps roles, methods, competences and rites as references inside a treatment, not as peer scenes inside every project.

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

## Navigation specification

One gesture means one thing. The horizontal axis must not mean several different things.

The mobile prototype uses:

```text
Vertical axis   = ascend / descend the hierarchy or deck depth.
Horizontal axis = previous / next sibling card or branch at the current level.
```

| Level | Axis | What it changes | Why |
|---|---|---|---|
| Global | Constellation / project card | Project | Changing project is too heavy for an ordinary sibling swipe. |
| Project | Rail / tabs | Scene | Workflow, Evidence, Documents, Gates, Actions, Traces, Competences, Methods. |
| Scene / Deck | Vertical | Deck depth / hierarchy | Read or descend the treatment in order: context, method, sources, evidence, outputs, actions, gates. |
| Same level | Horizontal | Sibling cards / branches | Move between sibling runs, tasks, method sub-cards, evidences or gates. |
| Card | Tap | Recto / verso | Recto = five-second read; verso = governed detail. |
| Card | Long press | Quick actions | Edit, request source, open gate, archive, merge — never auto-validate. |

A subject is a scope label that filters scenes; it is not a navigation level and does not own the horizontal axis.

Formula:

```text
The project is chosen in the constellation.
The scene changes by rail.
The deck reads and descends vertically.
Horizontal moves between sibling cards at the current level.
The card is understood at the recto.
Evidence, trace and gates are checked at the verso.
```

A long press prepares a candidate or opens a gate. It never commits an external effect by itself.

## Scenes and decks

Keep the scenes few but sufficient.

A scene is selected by the rail; its deck reads vertically. The scope filter column is a label, not a navigation axis.

| Scene / deck | Scope filter | Deck (vertical) | Purpose | Main entities |
|---|---|---|---|---|
| Workflow / Traitement | project + subject + active request | treatment order | understand what is being produced | Run, Task, context, method, sources, evidence, role qualities, draft, actions, gates, trace |
| Evidence / Preuves | project + subject | assertions / proofs / gaps | verify what supports a claim | Assertion, source, evidence, contradiction, gap, status |
| Documents / Sources / Connaissances | project or global, by category | documents then extracted knowledge | separate raw file, source, professional knowledge | Document, source, project knowledge, métier knowledge |
| Gates / Arbitrages | project, subject or global | open / blocked / resolved | see what awaits decision | Gate, arbitration, expected decision, options |
| Actions | project + subject or global | candidate / ready / blocked | track what can be done or sent | candidate email, Notion write candidate, export, reminder |
| Traces / Mémoire | project + subject | trace, register candidate, register entry | know what was done, kept, validated or abandoned | Trace, ledger, register candidate, register entry |
| Compétences | global, not project, by competence subject | maturity | capitalize reusable capability | Competence with maturity field |
| Méthodes / Reasoning | global, not project, by method family | raw / professional / runtime-pattern | expose reusable method cards without making them runtime selectors | Method Card, Method Proposal Candidate pattern, method guide reference |
| Templates / Ressources | global or métier, by family | templates and guides | reuse without confusing with proof | Template, guide, resource, example |
| Constellation | global | visual relations | global orientation | projects, subjects, tensions, gates, dependencies |

The Competence Scene stays global and neutral: a competence may be used by a project, but never becomes project-owned.

The Method Scene also stays global and neutral: a method may structure a task, but never becomes proof, approval, execution or project-owned truth.

## Pantheon reference project vs real project

### Pantheon project

`Pantheon` is the reference project, not a client dossier. It holds reusable governance and professional method material:

```text
Pantheon
-> Documents (references, doctrine, lexicons)
-> Roles (definitions, qualities, limits)
-> Methods / Reasoning (method cards, reasoning guides, runtime-pattern boundaries)
-> Competences (definitions, reusable method, maturity)
-> Rites (procedures, not runtime steps)
-> Run types (reusable governed methods)
```

These reference scenes are global and neutral; they are not owned by a project dossier.

### Real project

A real project is a dossier. It contains only its own material:

```text
Project
-> Subjects
-> Runs
-> Documents
-> Evidences
```

Roles, methods, competences and rites do not become project scenes by default. They are referenced from tasks when mobilized.

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
Record          (statuses: working, register_candidate, register_entry, obsolete)
Competence      (maturity: durable, candidate, on-the-flow, need, gap)
Method          (raw_method, professional_method, runtime_pattern)
Role
Rite
Constellation
```

Two consolidations versus an earlier draft:

```text
Working draft / Register Candidate / Registre Probatoire entry / promotion / obsolete
are NOT separate families. They are statuses of one Record.

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
| Method | method reference / method affordance | method proposed, contested, failed, repeated, changed, creates evidence delta, scope delta or gate request. |
| Competence | competence reference | competence missing, failed, repeated, proposed, productive output requested. |
| Rite | rite reference | proof gap, mission limit, responsibility issue, memory promotion, pre-transmission check. |
| Risk | field on Run / Task / Evidence / Decision | impact is high enough to block or require arbitration. |
| Scope | field on Run / Rite / Decision / Result | mission boundary or responsibility changes the allowed output. |
| Question | Decision subtype | information required from user, MOA, enterprise, BET, authority or Zeus. |
| Gate | Decision subtype | truth, approval, memory, external action or professional commitment is at stake. |
| Action Candidate | productive competence subtype | drafting, PDF production, avenant preparation, task-list production or handoff is requested. |

Role / God cards show useful quality expressions, not activated agents, and appear only when a quality changes the treatment.

Method cards show useful reasoning or review discipline, not activated agents, and appear only when the method changes proof, scope, cost, status, task quality or action boundary.

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

Status reuses the governed status vocabulary. Risk reuses the existing C and K axes and E0–E4 certainty — not a parallel faible/moyen/fort scale.

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
| Parent | 1 | Evidence -> Subject |
| Main source | 1–3 | Evidence -> Document |
| Affects | 1–5 | Gate -> Action / Draft |
| Produces | 1–3 | Run -> Draft / Action |
| Blocks | 1–3 | Gap -> Gate |
| Supports | 1–5 | Evidence -> Assertion |
| Contradiction | rare | Evidence A <-> Evidence B |
| Promotion | 1 | Competence-on-the-flow -> Competence candidate maturity |
| Method proposal | 1–3 | Role expression -> Method Proposal Candidate |
| Trace | many, collapsed | grouped Trace cards |

A card shows only its main link on the recto. The verso shows useful links. The constellation shows the many relations.

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
Method accepted does not mean conclusion validated.
```

## Workflow Scene — the run/task deck

The Workflow Scene is the complete narrative of a treatment. Its deck contains the run and its task sequence, plus only the cards actually mobilized.

### Run card

The Run Card is the head of the run; the run declares the expected result.

Recto: run title, methodology, expected result, final confidence check, process status, governance status, expected outputs, open gates, date / indice / version.

Verso: process state, planned tasks, added tasks/sub-cards, documents used, evidences produced, roles/methods/competences/rites mobilized, risks, scope limits, open decisions, run event journal summary.

### Task card

The Task Card is the operational unit; it aggregates references to roles, methods, competences, rites, documents, evidences and decisions.

Recto: task title, methodology, expected result, confidence check, process status, governance status, responsible role, method references or method proposals, competences mobilized, documents linked, evidences linked/expected, date / indice / instance.

Verso: trigger, inputs, steps, output, gaps, roles consulted, method proposals, methods used, rites triggered, decisions linked, sub-cards spawned, short run-event history.

A task always has one main responsible role.

| Field | Cardinality | Meaning |
|---|---:|---|
| responsibleRole | 1 | Main role accountable for the task posture. |
| contributorRoles | 0..n | Roles consulted or assisting. |
| methodRefs | 0..n | Method Cards currently structuring the task. |
| methodProposalCandidates | 0..n | Role-proposed method changes or additions. |
| arbitrationRole | 0..1 | Zeus or user if a decision must be arbitrated. |
| externalExpertRoles | 0..n | BET, jurist, economist, authority, enterprise, MOA. |

Guideline:

```text
Active analytical or productive task -> at least one competence expected.
Passive wait / document receipt / blocked gate -> zero competence acceptable.
Method references are optional until a run affordance becomes useful or a role detects a tension.
Competence productive -> prepares a candidate output.
Decision / Gate -> authorizes or blocks an external effect.
```

### Method inside a task

A method may appear as:

```text
method affordance;
method reference;
Method Proposal Candidate;
visible Method sub-card.
```

Use a field when normal:

```text
Methods: source_admission · contractual_decomposition · mission_scope_guard
```

Create a Method Proposal Candidate when a role detects a tension:

```yaml
proposingRole: argos
detectedProblem: conflicting amount between quote and situation
currentMethod: contractual_decomposition
proposedMethod: authority_qualification
expectedGain: clarify source precedence
evidenceDelta: resolves_conflict
scopeDelta: clarifies_scope
gateRequired: false
status: accepted_internal
```

Create a visible Method sub-card when the method carries process state:

```text
Method proposed: ARGOS proposes authority_qualification.
Method contested: THEMIS requests mission_scope_guard before transmission.
Method failed: contractual_decomposition impossible because CCTP is missing.
Method repeated: probative_review instance B before client email.
Method changed output: constrained_generation removed unsupported claims.
Method opens gate: external_commitment_guard blocks send until approval.
```

Core invariant:

```text
Method sub-card -> structures reasoning or review discipline.
Competence sub-card -> prepares candidate output.
Decision / Gate -> authorizes or blocks external effect.
```

### Spawned cards expose their origin

The deck shows no `Flow Adaptation Card`. When a confidence check fails or a signal is detected, the new useful card appears in its real nature and exposes its origin:

```text
Document missing -> Document sub-card.
Proof weak -> Evidence sub-card.
Method useful -> Method Proposal Candidate or Method sub-card.
Competence missing -> Competence sub-card.
Rite triggered -> Rite sub-card.
External action possible -> Decision / Gate.
Question needed -> Decision / Question.
```

Minimum origin fields:

```yaml
origin: added
spawnedBy: task-or-card-id
spawnReason: why it appeared
spawnTrigger: confidence-check-or-signal
spawnedAtStep: run step number
```

### Default CR deck order

```text
1  Project compact     where am I?
2  Subject             what topic?
3  Run / Method        which method, what status?
4  Constraint Ledger   pinned constraints and decisions
5  Context             mission, phase, scope
6  Documents / Sources notes, prior CR, photos, mails, CCTP
7  Evidence            candidate assertions + proofs + gaps
8  Method / Procedure  methods, tactics used, method proposals if visible
9  Role qualities      only qualities that change the treatment
10 Draft Output        CR / mail / note / table (Record, status working)
11 Actions             prepared: mail, Notion, export
12 Gates               decisions to take
13 Trace / Memory      what stays as trace or may be promoted
```

### Answer-first default

The deck above is the full, comprehensive view. The Workflow Scene should not open on all thirteen cards. The default landing state is answer-first:

```text
Draft Output + main Gate + top Evidence,
with the full deck available on demand,
and the primary gate kept visible as a sticky badge while scrolling.
```

Comprehensiveness is available, not the landing screen.

## Other scenes

```text
Evidence Scene: project + subject scoped. Assertion -> source/evidence -> status.
Documents Scene: distinguishes Document, Source, Connaissance.
Gates Scene: open / blocked / resolved gates awaiting decision.
Actions Scene: candidate / ready / blocked actions; external effect stays gated.
Traces / Memory Scene: trace, ledger, memory candidate, register.
Competences Scene: global and neutral; usage references do not make a competence project-owned.
Methods Scene: global and neutral; raw reasoning library, professional cards and runtime-pattern boundaries stay distinct.
Constellation: orientation only, not the main decision surface. Gates remain decisive.
```

## Examples

### Reception of a complementary quotation

```text
Project: Les Damps · Subject: devis complementaire · Scene: Workflow
Run: Reception devis complementaire
Expected result: justified candidate opinion before MOA transmission and possible avenant preparation.
```

| Order | Task | Responsible | Methods | Competences | Expected result |
|---:|---|---|---|---|---|
| 1 | Qualifier le devis reçu | Maître | source_admission | document intake, quote qualification | Quote identified. |
| 2 | Vérifier les pièces marché | Maître | authority_qualification | document review | Corpus available or gaps exposed. |
| 3 | Analyse contractuelle | Maître | contractual_decomposition | lecture CCTP, hors marché, avenant | Included / outside market / receivable / not. |
| 4 | Analyse technique | Athéna | site_observation_review if site fact | technical coherence | Necessity and feasibility candidate. |
| 5 | Analyse financière | Athéna | quote_variation_review | price/quantity/duplicate check | Financial coherence candidate. |
| 6 | Justification avis | Athéna | probative_review | evidence packaging | Claims linked to documents or marked weak. |
| 7 | Limite mission | Maître | mission_scope_guard | scope discipline | What can be said without over-committing. |
| 8 | Production avis candidat | Athéna | constrained_generation | synthesis, drafting | Candidate opinion with reserves. |
| 9 | Rédaction mail MOA | Hermès | external_commitment_guard | productive competence | Draft email only, not sent. |
| 10 | Transmission MOA | Zeus / user | external_commitment_guard | decision gate | Send / correct / block / ask for evidence. |

Spawned cards on signals: CCTP missing -> Document sub-card; conflicting amount -> Method Proposal Candidate `authority_qualification`; proof weak -> Evidence sub-card; out-of-mission wording -> Method sub-card or Rite sub-card; external transmission -> Decision/Gate.

### Chantier report production

```text
Subject: visite de chantier · Run: Elaboration CR chantier
Sequence: qualify inputs with source_admission; read previous CR; classify points;
apply site_observation_review; produce evidence candidates; apply mission_scope_guard
if wording may engage; produce CR candidate; prepare draft email; open external_commitment_guard.
```

Spawned: Evidence (photo non localisée); Method Proposal Candidate (site_observation_review); Decision/Question (autre angle); Method sub-card (mission_scope_guard); Decision/Gate (envoi CR bloqué).

### Post-client-meeting task preparation

```text
Subject: réunion client · Run: Preparation liste de taches
Sequence: extract requests; separate wishes/decisions/assumptions; check project and mission scope;
propose methods if tensions appear; create candidate task list; open questions and gates.
```

Core distinction:

```text
Client wish is not project decision.
Project decision is not agency task.
Agency task is not external action.
External action is not approved action.
Method proposal is not validation of the conclusion.
```

## What to avoid

| Bad card | Why | Replacement |
|---|---|---|
| Full CR chantier card | becomes a mini-dossier | Run + Draft Output + Evidence + Gates |
| AI / God card with a character | decorative, vague | Role quality card only when a quality changes the treatment |
| Proof/document card | conflates source and proof | Document card, then Evidence card |
| Decision/memory card | conflates arbitration and canon | Gate card, then Record |
| Project competence card | makes the competence project-owned | global Competence card + usage reference |
| Raw LLM method card as authority | confuses runtime pattern with professional method | professional Method card + runtime pattern hidden or traced |
| Validated action card | implicit execution | Action card + separate Gate card |
| Everything-linked graph card | unreadable | Constellation as a view, not a decision entity |
| Family per lifecycle state | inflates families | one Record family + status field |

## Relationship with other documents

```text
REASONING_MODES_LIBRARY.md — raw reasoning modes as Guide de compétence candidate.
METHOD_CARD_MODEL.md — generic Method Card grammar and Method Proposal Candidate.
METHOD_DECK.md — architecture-domain professional method cards.
ITERATIVE_DELIBERATION_LIFECYCLE.md — deliberation behind a Workflow Scene.
CARD_STACK_ROLE_QUALITY_ALIGNMENT.md — Role / God cards as quality expressions, not agents.
COMPETENCE_MODEL.md — Connaissance / Guide / Ressource / Competence vocabulary.
WORKFLOW_LIFECYCLE.md — authority, testing, activation and execution boundaries.
```

A task card may display a workflow proposal or runtime result, but it does not authorize execution.

## Design warning

The model must resist card inflation.

```text
Do not create a visible card for every concept.
Create visible cards only when the object is orienting, working, blocking, repeated,
newly proposed or decision-bearing.
A family is an entity; lifecycle is a status field.
A method is visible only when it changes proof, scope, cost, status, action or task quality.
```

The validated remains.

## Boundary

This document is a UX / governance candidate.

It creates no runtime, no UI, no schema, no database, no tool call, no connector, no skill, no approval engine and no memory engine. Any implementation belongs later in the appropriate exposure surface or execution runtime, under the existing placement doctrine, and remains a candidate until reviewed.

---

## Absorbed: Card Stack Knowledge Corpus Alignment (2026-07-07)

Formerly `docs/governance/CARD_STACK_MODEL.md`; absorbed verbatim during the governance cleanup (pass B). Headings demoted one level; content unchanged.

Original status: candidate support note — card-stack terminology alignment for Connaissance as non-project documentary corpus.

This document is not canonical doctrine yet.

It does not implement a UI, dashboard, search engine, RAG pipeline, document ingestion engine, vector database, OCR pipeline, knowledge registry, evidence engine, memory engine, approval engine, OpenWebUI plugin, Hermes skill, connector or external action.

It reconciles `CARD_STACK_MODEL.md` with the intended meaning of `Connaissance` in the cockpit card deck.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### Purpose

The card-stack vocabulary must avoid confusing:

```text
project material;
source material;
evidence;
context;
validated memory;
professional documentary knowledge;
competence resources;
```

The term `Connaissance` should be reserved for the documentary corpus outside a specific project.

Examples:

```text
PLU / urbanism documents;
MAF recommendations;
CCTP guides;
professional lexicons;
agency doctrine;
regulatory notes;
insurance notes;
method guides;
technical reference dossiers;
standard details;
reference checklists;
professional doctrine distilled from reliable sources.
```

### Core correction

In the card stack:

```text
Connaissance = non-project documentary corpus, qualified or structured for professional reuse.
```

It is not:

```text
a project file;
a project-specific fact;
a raw source attached to one dossier;
a proof by itself;
a canonical memory;
a competence;
a template;
an action;
```

### Clean separation

| Object | Meaning | Example | Project-owned by default? |
|---|---|---|---|
| Document / Source | Raw or retrieved material. | PDF, mail, plan, photo, notice, PLU file, MAF PDF. | It depends on source. |
| Connaissance | Qualified documentary corpus outside projects. | PLU rule note, MAF recommendation digest, CCTP guide, lexicon. | No. |
| Context | Current project situation. | Phase APD, mission DET, commune, client, lot. | Yes. |
| Evidence | A source selected to support an assertion. | PLU article supporting a facade-material claim. | Scoped to assertion/project/subject. |
| Memory Candidate | Fact proposed for future retention. | “For project X, facade material A was rejected.” | Yes, until promoted. |
| Register Entry | Validated memory / proof register entry. | Human-validated scoped claim. | Scoped. |
| Competence | Reusable ability. | “Read a PLU and extract facade constraints.” | No. |
| Guide / Resource de competence | Material used to learn or operate a competence. | Tutorial, checklist, example file. | No. |
| Template | Reusable output structure. | Mail response, CR chantier, CCTP article skeleton. | No. |

### Working rule

```text
A project can use a Connaissance.
A Connaissance does not become project-owned because it was used.
A project-specific extraction from a Connaissance becomes Evidence, Context or Memory Candidate depending on its role.
```

Example:

```text
PLU of Rouen as documentary corpus -> Connaissance Card.
Article used to check a facade choice for project Poussin -> Evidence Card scoped to Poussin / facade.
Decision “zinc accepted for this project” -> Memory Candidate / Register after gate.
Ability “check PLU facade materials” -> Competence Card.
```

### Deck implications

#### Documents / Sources Scene

This scene may show raw files or retrieved sources, including project documents and non-project documents.

Examples:

```text
uploaded CR chantier;
photo chantier;
client email;
CCTP project file;
PLU PDF;
MAF recommendation PDF;
lexicon page;
agency guide;
```

A raw document is not yet a Connaissance merely because it exists.

#### Connaissances Scene

The Connaissances scene should be a documentary corpus scene, not a project working scene.

Candidate horizontal families:

```text
Urbanisme / PLU;
Assurance / MAF;
CCTP / marchés;
Réglementation;
Construction / chantier;
Lexiques;
Agence / doctrine interne;
Méthodes professionnelles;
Références techniques;
```

Candidate vertical order:

```text
Validated / accepted knowledge;
Candidate knowledge;
To verify;
Obsolete / superseded;
Gaps / needed knowledge;
Blank knowledge card;
```

#### Workflow Scene

A Workflow Scene may include `Connaissances used` only when the treatment actually relies on the documentary corpus.

Do not include all relevant-looking knowledge by default.

#### Evidence Scene

When a Connaissance supports a project assertion, it appears through an Evidence Card.

The Evidence Card must keep scope visible:

```text
Project:
Subject:
Assertion:
Connaissance used:
Source excerpt:
Status:
Freshness:
Gate:
```

#### Competence Scene

A competence may use Connaissances, guides and resources.

But:

```text
Connaissance = professional content.
Competence = reusable ability.
Guide / Resource = support for operating or learning a competence.
```

A MAF recommendation digest is Connaissance.

A procedure for applying the MAF recommendation in a client email is a Competence or Template, depending on form.

### Connaissance Card

#### Recto — five-second reading

```text
Title:
Family: PLU | MAF | CCTP | Lexique | Réglementation | Agence | Technique
Authority: official | professional | agency | external | candidate
Status: accepted | candidate | to_verify | obsolete | refused
Scope: non-project corpus
Freshness:
One-line use:
```

Examples:

```text
PLU Rouen — zones UB facade rules
Urbanisme / PLU · official · to_verify
Scope: non-project corpus
Use: facade material constraints for Rouen projects.
```

```text
MAF — limites de mission / responsabilité
Assurance / MAF · professional · candidate
Scope: non-project corpus
Use: wording guardrail for client / enterprise replies.
```

#### Verso — detailed card

```text
source_document:
source_type:
authority_class:
version_or_date:
freshness_status:
content_summary:
usable_claims:
limitations:
related_competences:
related_templates:
related_evidence_cards:
related_projects_using_it:
review_status:
next_review_date:
```

### Relationship with project documents

Project-specific documents should not be reclassified as Connaissance by default.

Examples:

| Project item | Better card type |
|---|---|
| Client email | Document / Source Card |
| Uploaded photo | Document / Source Card |
| Previous CR for this chantier | Document / Source Card + Trace / Memory if validated |
| Project CCTP | Document / Source Card; Evidence when supporting claim |
| Project PLU excerpt used for a decision | Evidence Card scoped to project |
| Decision made from PLU | Memory Candidate / Register after gate |

### Relationship with external documentary corpus

External documentary corpus may become Connaissance when it is:

```text
qualified;
structured;
scope-marked;
authority-classed;
freshness-marked;
usable across projects;
not merely attached to one project;
```

Examples:

```text
PLU family summary;
MAF wording caution note;
CCTP article guide;
terminology lexicon;
ERP classification reference;
fire-safety reminder note;
agency standard detail commentary;
```

### Relationship with Evidence

Connaissance is not proof by itself.

A Connaissance becomes part of evidence only when it supports a scoped assertion.

```text
Connaissance Card -> used by Evidence Card -> supports Assertion -> may affect Gate.
```

### Relationship with Memory

Connaissance is reusable documentary material.

Memory is what was validated or decided in a specific scope.

Do not use Connaissance as a bypass around memory gates.

### Relationship with Templates

A template structures output.

A Connaissance informs content.

Example:

```text
Template: mail response hors mission.
Connaissance: MAF recommendation on responsibility boundary.
Evidence: specific mission contract clause for current project.
Gate: user approval before sending.
```

### Anti-patterns

```text
Do not classify every project note as Connaissance.
Do not let project-specific facts pollute the general knowledge corpus.
Do not treat PLU / MAF / CCTP guides as automatically current.
Do not treat Connaissance as Evidence without scoped assertion.
Do not treat Connaissance as canonical memory.
Do not let Connaissance become a competence.
Do not let competence resources become Connaissance unless they contain professional content.
```

### Final rule

```text
Documents are sources.
Connaissances are reusable documentary corpus outside projects.
Evidence is scoped support for an assertion.
Memory is validated retention.
Competence is reusable ability.
Template is reusable structure.
Gate is decision threshold.
The human decides.
```

---

## Absorbed: Card Stack Role Quality Alignment (2026-07-07)

Formerly `docs/governance/CARD_STACK_MODEL.md`; absorbed verbatim during the governance cleanup (pass B). Headings demoted one level; content unchanged.

Original status: candidate support note — terminology alignment for card-stack UX, role qualities and visible governance traces.

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

### Purpose

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

### Reading rule

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

### Card family correction

#### Role / God Card

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

#### Role Quality / Facet Card

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

### Workflow Scene correction

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

### Visibility rule

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

### Gesture boundary

Gestures may reveal, request or prepare.

They must not decide.

| Gesture | Allowed meaning | Forbidden meaning |
|---|---|---|
| Tap | open detail / verso | validate |
| Long press | show quick actions | approve automatically |
| Vertical swipe | move through active deck | execute next step |
| Horizontal swipe | change subject / lane | merge decisions |
| Constellation selection | navigate relationships | make graph authoritative |

### Quality trace in cards

Recommended compact trace:

```text
Relevant quality expressions:
- Themis / responsibility sensitivity: warning — possible prescription outside mission.
- Athena / proof sensitivity: evidence gap — source insufficient for conclusion.
- Iris / safer-wording orientation: tactic — reformulate as clarification request.
- Hermes / external-action sensitivity: gate — draft only, not sent.
```

Detailed trace remains second-layer.

### Card stack minimum for first test

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

### Anti-patterns

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

### Final rule

```text
The card shows the object.
The role guards a jurisdiction.
The quality expresses itself only when useful.
The stack organizes the treatment.
The gate exposes the threshold.
The human decides.
```
