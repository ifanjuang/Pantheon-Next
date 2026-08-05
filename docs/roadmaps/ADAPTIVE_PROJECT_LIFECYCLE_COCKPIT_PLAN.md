# Adaptive Project Lifecycle and Cockpit Convergence Plan

Status: validation-only roadmap — documented non-implemented.
Boundary profile: candidate_support_note.

Date: 2026-08-05

```text
OpenWebUI exposes conversation and intake.
Hermes Agent executes bounded admitted work.
Pantheon Next governs semantics, authority and consequential transitions.
pantheon-mvp owns executable persistence, APIs, projections and adapters.
The human decides consequential effects.
```

## 1. Objective

This roadmap consolidates the project lifecycle, document intake, project values,
review surfaces, memory boundaries and Cockpit navigation discussed for the
architecture-agency domain.

The target is a system that can begin from any practical first input — email,
mission letter, plan, PLU extract, spreadsheet, photograph, question or uploaded
file — and remain coherent through design, authorization, consultation, works,
reception, GPA, claim and possible dispute.

The user experience must remain simple:

```text
receive or create material
-> preserve the source
-> resolve or suggest the project
-> expose only useful attention
-> require a human only for consequential ambiguity
-> apply governed changes through a separate operation
```

This roadmap does not create a runtime, inbox engine, scheduler, queue, provider
router, plugin manager, memory engine, approval engine or automatic project
mutation.

## 2. Repository state and existing coverage

The plan builds on existing authority and implementation rather than introducing
parallel concepts.

Existing semantic and governance surfaces include:

- `docs/domain-packs/architecture/PROJECT_CARD_DECK_COMPOSITION.md`;
- `docs/domain-packs/architecture/PROJECT_OBJECT_MODEL.md`;
- `docs/governance/DOSSIER_SITUATION_INTAKE.md`;
- `docs/governance/DOCUMENT_LIFECYCLE_GOVERNANCE.md`;
- `docs/governance/DOCUMENT_PRODUCTION_LIFECYCLE.md`;
- `docs/governance/AGENCY_DATA_SYSTEM_OF_RECORD.md`;
- `docs/governance/CARD_STACK_MODEL.md`;
- `docs/governance/PANTHEON_COCKPIT_INFORMATION_ARCHITECTURE.md`;
- `docs/governance/PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md`;
- `schemas/project_claim.schema.yaml`;
- `schemas/execution_result.schema.yaml`;
- `docs/governance/authority/PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json`.

Existing executable MVP coverage includes append-only persistence of typed Hermes
execution results, clarification requests and human review dispositions. These
records explicitly do not mutate Project, APU, Evidence or memory.

The Hermes 0.20.0 governed profile has passed an ephemeral laboratory acceptance.
That result does not qualify the agency/NAS installation, production activation or
future task authorization.

## 3. Governing distinctions

### 3.1 Authority classes

The implementation must keep at least these classes distinct:

```text
authoritative objects
review objects
projection definitions
runtime objects
external memory
external sources
```

Typical authoritative objects:

```text
Project
Document
ProjectClaim
Decision
WorkIssue
Evidence
validated APU objects
```

Typical review objects:

```text
ChangeCandidate
ExecutionResult
ResultCandidate
ClarificationRequest
ReviewDisposition
FragmentQualificationCandidate
```

Typical projection/configuration objects:

```text
Card Projection Definition
Navigation Registry
Cockpit card model
saved view definition
```

### 3.2 Required non-equivalences

```text
source stored != source qualified
retrieved != truth
projected != persisted
Information Card != Information semantic object
Document != Information
Project attribute != ProjectClaim
ProjectClaim != Evidence
source_backed != verified
verified != approved
review disposition != applied mutation
runtime success != professional validation
memory relation != project relation
conversation != Decision
UI status != authorization
```

## 4. Target Cockpit hierarchy

The Cockpit is an adaptive projection of a governed project graph, not a fixed
storage tree.

### 4.1 Root spaces

```text
Pantheon
Affaires
Connaissances
Outils
```

These are navigation spaces. They do not create new business entities.

### 4.2 Affaires

```text
Affaires
├── Nouvelles demandes
├── Tous les projets
└── Vues enregistrées
    ├── Études
    ├── Autorisations
    ├── Consultation
    ├── Chantier
    ├── Réception / GPA
    ├── Sinistres ouverts
    ├── Contentieux
    └── Archives
```

A project may appear in several views. Phase, reception, claim and dispute are
facets or contexts, not mutually exclusive folders.

### 4.3 Project navigation

The project exposes four primary sections:

```text
Vue d’ensemble
Contenus
À traiter
Décisions
```

Secondary lenses appear only when useful and available:

```text
Contacts
Mémoire
Outils
APU / spatial understanding
Evidence / provenance detail
```

The existing visual families remain:

```text
Project
Information
Contacts
Work
Decision
Tool
```

A visual family is not a backend ontology.

### 4.4 Progressive disclosure

Minimal use:

```text
Project
Contenus
Recherche
Contacts
```

Assisted use adds:

```text
À traiter
Hermes questions
notes and summaries
```

Governed use adds:

```text
Decisions
ProjectClaims
history and provenance
```

Advanced use adds optional lenses:

```text
APU
Evidence
Mnemosyne
adapters
D3 relationship views
```

Unused capabilities remain invisible. Disabling an optional capability must not
remove authoritative project data.

## 5. Project lifecycle coverage

The same core model must support:

```text
prospect / incoming request
mission proposal and contracting
survey / diagnosis / feasibility
design phases
planning authorization
consultation and works contracting
site execution
reception and reservations
GPA / post-reception follow-up
claim / insurance context
dispute / litigation
closure, archive and later reopening
```

Domain phases belong to the architecture pack. The universal Cockpit core remains
Project, Content, Work, Decisions, Contacts and Tools.

## 6. Source-first intake

Any incoming item must be preservable before full classification.

The implementation must reuse `document_source` and the existing Dossier Situation
Intake function. It must not create a competing universal `InboxItem` ontology.

Minimum admission state:

```text
source_id
source_kind
origin
raw_source_ref
received_at
received_by
declared_project_name
project_ref optional
candidate_project_refs
classification_status
source_date optional
source_version optional
confidentiality optional
```

Initial classification statuses:

```text
unassigned
suggested
linked
excluded
```

Rules:

1. source preservation precedes classification;
2. weak uncertainty does not block intake;
3. project linking remains correctable;
4. no Project is silently created unless the user explicitly requests creation;
5. a human question is required only when a wrong choice could have a material
   consequence.

## 7. Project minimum and aliases

A Project must be creatable from incomplete material.

Minimum first shape:

```text
project_id
display_name
aliases
status
created_at
revision
```

Optional early fields:

```text
project_type
location
principal_contact_refs
mission summary
```

Aliases are first-class matching material and may include client name, address,
locality, historic project name, commercial name, former code or a reviewed common
misspelling. Alias matching suggests identity; it does not replace stable project
identity.

The model separates one main phase from simultaneous contexts:

```text
phase: chantier
contexts: [reception_partielle, sinistre_ouvert]
```

## 8. Document and Information convergence

### 8.1 Information Card

`Information` remains a broad professional visual family. It may project a
Document, email, report, note, synthesis, analysis or administrative item.

### 8.2 Information semantic object

A distinct Information object is justified only for intentionally authored,
structured and versioned professional content produced or consolidated inside
Pantheon, such as:

```text
feasibility note
project synthesis
PLU analysis
coordination memo
responsibility analysis
dispute chronology draft
```

A PDF, plan, email, CCTP or issued CR must not be duplicated as an Information
object merely to appear in the Information visual family.

### 8.3 Document behavior

Document types declare behavior instead of hardcoding it in the Cockpit:

```yaml
revision_mode: versioned | event
origin_mode: produced | received | found
```

Versioned examples:

```text
plan
CCTP
DPGF
notice
surface schedule
revisable report
```

Event examples:

```text
email
letter
site report
invoice
visa
observation report
reception record
```

Initial lifecycle vocabulary:

```text
production
issued
received
superseded
archived
```

Each doctype owns the subset it uses. There is no universal lifecycle shared by
all objects.

## 9. ProjectClaim use

Stable identity and ordinary non-consequential description may remain directly on
Project. Professional values whose provenance, date or contradiction matters use
ProjectClaim semantics.

Priority claim families:

```text
surfaces
site area
footprint
budget
contract amount
PLU zone
parcel references
ERP classification
occupancy
authorization references and dates
reception date
```

Application path:

```text
source
-> extraction or relation candidate
-> human review
-> separate governed command
-> claim created, superseded, contested or retired
```

A ReviewDisposition never creates a claim by itself.

## 10. One attention surface

The `À traiter` projection aggregates existing objects without copying them:

```text
WorkIssues
ClarificationRequests
ChangeCandidates
ResultCandidates
contradictions
contested claims
unassigned sources
pending decisions
```

The user sees practical actions rather than internal type names:

```text
Répondre
Confirmer
Corriger
Appliquer
Rejeter
Demander une révision
Ouvrir la source
Archiver
```

The UI must present counts and consequences, for example:

```text
3 éléments à traiter
1 question
1 document à confirmer
1 valeur contradictoire
```

## 11. Review versus application

The existing execution-result contract remains the single Hermes result conduit.
No new generic `Candidate`, `Proposal`, `HermesQuestion` or `CardInteraction`
concept is introduced.

Target path:

```text
Task Contract
-> Hermes execution
-> ExecutionResult
-> typed ResultCandidate
-> ClarificationRequest where needed
-> human ReviewDisposition
-> separate domain command
-> authoritative mutation
-> append-only governed event
```

Initial event families may include:

```text
ProjectCreated
SourceLinked
SourceRelinked
DocumentIssued
DocumentSuperseded
ProjectClaimCreated
ProjectClaimSuperseded
DecisionRecorded
WorkIssueOpened
WorkIssueResolved
ObjectArchived
ProjectReopened
```

This event journal is an audit surface, not a scheduler or queue.

## 12. Mnemosyne boundary

Mnemosyne remains optional external cognitive memory.

It may receive broad context after an interaction:

```text
conversation or useful excerpt
summary or reasoning
preferences and anecdotes
source_refs
current_project_id optional
candidate_project_refs optional
```

After an authoritative mutation, it may also receive a governed event projection:

```text
event kind
project and object refs
previous and new value where relevant
source refs
decision ref
human actor
timestamp
```

A ReviewDisposition alone is insufficient for governed-memory publication. The
business mutation must have occurred.

Cockpit reads memory through a bounded read adapter. Hermes is not invoked merely
to open a project or render a graph. Mnemosyne timeout or absence must not block
Project, Document, Decision, WorkIssue or Claim projections.

## 13. Implementation slices

### Slice 0 — baseline scenarios and branch reconciliation

Objective: lock end-to-end scenarios and identify reusable work before code changes.

Checks:

- first email without project;
- plan with approximate project name;
- PLU or spreadsheet received first;
- new document index;
- new site report event;
- conflicting project value;
- reception reservation;
- claim/dispute context;
- minimal project with no advanced modules;
- Mnemosyne unavailable.

Existing MVP branch posture:

- `agent/execution-result-persistence-clean` is behind `main` with no unique commit;
- `agent/mobile-knowledge-variant-review` is divergent and must not be merged as a
  second review architecture. Reusable UX elements are reconsidered only after the
  common review and apply services are stable.

### Slice 1 — authority convergence in Pantheon Next

Add explicit authority class, owner schema, lifecycle owner, projection references,
implementation status and compatibility status to the existing ownership mapping
where useful. Do not create a second registry.

Completion: each relevant object has one clear semantic, implementation, lifecycle
and projection owner.

### Slice 2 — Project minimum and aliases

Pantheon Next owns the contract; pantheon-mvp owns PostgreSQL, API and tests.

Completion: a Project can begin with minimal identity and later accept corrected
aliases without migration to another model.

### Slice 3 — source admission and project resolution

Implement unassigned source storage, candidate project matches, explicit linking
and relinking. Preserve provenance and idempotency.

Completion: any supported source can be found and corrected even before project
classification.

### Slice 4 — document series and event documents

Consolidate doctype behavior, indices, technical revisions, issued/received state
and event accumulation.

Completion: the system distinguishes a new index, a new event and an internal
technical edit without duplicate Information storage.

### Slice 5 — ProjectClaim persistence and projection

Implement bounded create, supersede, contest and retire operations with provenance
and optimistic revision checks.

Completion: Project cards expose current professional values with source and
history.

### Slice 6 — attention and decision projection

Build one server-owned attention projection over WorkIssue, clarification,
candidate, contradiction, claim and source states.

Include MVP issue `#93` by validating WorkIssue `close_reason` before PostgreSQL.

Completion: all actionable items appear in one UX surface without backend copying.

### Slice 7 — adaptive Cockpit projection

Implement four primary project sections and optional lenses through server-owned
projection definitions and registries, not hardcoded DOM injection.

Include MVP issue `#94`: `New information` remains a synthetic creation affordance,
not a persisted business entity, and belongs to the Project content projection.

Completion: minimal projects remain minimal; advanced projects expose additional
lenses without a second Cockpit.

### Slice 8 — governed apply command and event journal

Create explicit application commands after review and record authoritative events.

Completion: proposal, review, command and resulting state remain separately
auditable.

### Slice 9 — Mnemosyne adapter

Implement non-blocking cognitive write, governed event projection and read-only
memory lens.

Completion: memory enriches context but never becomes required project authority.

### Slice 10 — skills and external adapters

Connect source intake, project matching, document identity, revision comparison,
claim extraction, contradiction detection, WorkIssue proposal, drafting and memory
enrichment through existing Task Contract and ExecutionResult boundaries.

Paperless preserves and manages sources. Docling provides structure candidates.
Revit/APU adds spatial depth when needed. OpenWebUI handles conversation and user
input. None of these components owns Project truth merely because it is connected.

## 14. Pull request sequencing

Recommended Pantheon Next PRs:

```text
governed-object-authority-convergence
project-source-intake-contract
document-lifecycle-and-doctype-behavior
project-claim-application-boundary
adaptive-project-cockpit-model
governed-event-memory-boundary
```

Recommended pantheon-mvp PRs:

```text
project-aliases-and-source-intake
document-series-and-event-documents
project-claims-persistence
attention-projection-and-workissue-validation
governed-apply-event-journal
adaptive-project-cockpit
mnemosyne-memory-adapter
project-lifecycle-acceptance-tests
```

The divergent mobile branch is reviewed only after the common attention and apply
services exist. Useful diff, annotation, A/B review, accessibility and offline UX
may be ported; parallel storage and lifecycle ownership are not.

## 15. First usable increment

The first usable increment is deliberately small:

```text
minimal Project
aliases
source admission
correctable project linking
Documents
Contenus projection
Nouvelles demandes
```

It must work without Hermes, Mnemosyne, APU, advanced Evidence, Paperless, Docling
or Revit.

The second increment adds:

```text
ProjectClaims
À traiter
questions
Decisions
separate governed application
```

Advanced modules arrive only after those two increments are stable.

## 16. Validation and completion criteria

The convergence is complete when all of the following are verified:

1. any practical first input can be admitted;
2. no source is lost because classification is incomplete;
3. a Project can begin with minimal identity;
4. aliases improve matching without replacing stable identity;
5. phases and claim/dispute contexts are facets rather than exclusive folders;
6. document indices and event documents are distinct;
7. Documents are not duplicated as Information solely for display;
8. consequential Project values retain ProjectClaim provenance;
9. Hermes results remain non-authoritative;
10. review and application remain separate operations;
11. one attention projection aggregates actionable states;
12. optional lenses do not burden minimal projects;
13. Mnemosyne failure does not block the Cockpit;
14. no competing registry, renderer or candidate conduit is introduced;
15. prospect, design, authorization, works, reception, GPA, claim and dispute
    scenarios pass end to end;
16. mobile and desktop expose equivalent consequential actions and provenance.

## 17. Non-goals

This roadmap does not:

- implement PostgreSQL migrations or APIs;
- create a new universal entity hierarchy;
- delete the existing Information compatibility path;
- create one card per email, document fragment or minor design edit;
- create a Production card family;
- make phase folders authoritative;
- copy Mnemosyne into a second Pantheon graph store;
- authorize automatic Evidence admission or memory promotion;
- authorize Hermes installation, activation or future task execution;
- qualify the agency/NAS runtime environment;
- merge the divergent mobile branch.

```text
plan documented != implementation completed
schema present != runtime adopted
lab accepted != production qualified
reviewed candidate != project mutation
optional memory unavailable != project unavailable
```
