# Adaptive Project Lifecycle and Cockpit Convergence Plan

Status: validation-only roadmap — documented, not implemented.
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

Define a simple project experience that can begin from any practical agency input —
email, mission letter, plan, PLU extract, spreadsheet, photograph, question or
uploaded file — and remain coherent through design, authorization, consultation,
works, reception, GPA, claim and possible dispute.

The implementation must converge on existing concepts before adding new ones.

```text
receive or create material
-> preserve the source
-> resolve or suggest the project
-> classify as Document or Information when useful
-> relate it to project objects when known
-> expose only useful attention
-> require a human only for consequential ambiguity
-> apply governed changes through a separate operation
```

This roadmap does not create a runtime, inbox engine, scheduler, queue, provider
router, plugin manager, memory engine, approval engine or automatic project mutation.

## 2. Governing model

Pantheon distinguishes three levels.

```text
Project
├── governed project cards
└── project objects
```

### 2.1 Governed project card types

The project uses one common card family with distinct business types:

```text
Project
Document
Information
Work
Decision
Contact
Tool
```

The shared card shell does not erase the business distinction between the types.

```text
Document
= a real documentary object or source-bearing record

Information
= an intentionally authored or consolidated project statement

Work
= something to do, in progress or completed

Decision
= an explicit governed choice or arbitration
```

A PDF, plan, email, CCTP, IFC, photograph or issued report must not be duplicated as
Information merely to appear in the Cockpit.

### 2.2 Project objects

APU remains the internal authority for project objects and their relations.

Typical project objects include:

```text
site
building
level
zone
space
element
system
path
```

APU is an internal model name. The user-facing lens is **Objets du projet**.

### 2.3 Relations from cards to project objects

Any governed project card may relate to one or more project objects through a
shared, lightweight relation mechanism.

```text
Document / Information / Work / Decision
-> related_project_objects[]
-> APU project objects
```

These references do not duplicate project objects and do not create a second graph.
A candidate relation remains revisable until accepted according to its consequence.

Relations between cards remain separate:

```text
related_cards[]
```

### 2.4 Anatomie du projet

**Anatomie du projet** is the user-facing synthesis of the project's current
understanding.

It is not:

```text
not a new card type
not a second database
not a Knowledge object
not a replacement for APU
```

It is a calculated projection displayed on the verso of the Project card and may
summarize:

```text
reference documents
identified buildings, levels, zones, spaces, elements and systems
existing / demolition / projected / as-built coverage
confirmed and candidate card-to-object relations
contradictions
open questions
```

Selecting a summary item may open the **Objets du projet** lens or the relevant
source cards.

## 3. Required authority distinctions

```text
source stored != source qualified
retrieved != truth
projected != persisted
Document != Information
Information Card != Information semantic object
card relation candidate != confirmed project relation
Project attribute != ProjectClaim
ProjectClaim != Evidence
source_backed != verified
verified != approved
review disposition != applied mutation
runtime success != professional validation
memory relation != project relation
conversation != Decision
UI status != authorization
Anatomie du projet != authoritative storage
```

Typical authoritative objects:

```text
Project
Document
Information
Decision
WorkIssue
ProjectClaim
Evidence
validated APU objects and relations
```

Typical review objects:

```text
ChangeCandidate
ExecutionResult
ResultCandidate
ClarificationRequest
ReviewDisposition
FragmentQualificationCandidate
APU mapping candidate
```

Typical projection/configuration objects:

```text
Card Projection Definition
Navigation Registry
Cockpit card model
saved view definition
Anatomie du projet projection
```

## 4. Target Cockpit hierarchy

The Cockpit is an adaptive projection, not a fixed storage tree.

### 4.1 Root spaces

```text
Pantheon
Affaires
Connaissances
Outils
```

`Connaissances` is reserved for general, cross-project material reusable by several
projects, for example:

```text
DTU and standards
MAF recommendations and professional responsibility guidance
regulation and jurisprudence
agency doctrine and methods
technical references
reusable details
lessons learned
```

A retrieved general knowledge item is not automatically applicable to a project.
Applicability and provenance remain qualified.

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

The project exposes four primary navigation sections:

```text
Vue d’ensemble
Contenus
À traiter
Décisions
```

These sections are navigation projections, not card types.

```text
Vue d’ensemble
-> Project identity, current phase and key state
-> verso: Anatomie du projet

Contenus
-> Documents
-> Informations

À traiter
-> Work
-> questions
-> contradictions
-> candidates requiring attention

Décisions
-> Decision cards and their governed history
```

Secondary lenses appear only when useful:

```text
Contacts
Objets du projet
Sources et provenance
Outils
```

Mnemosyne is not a primary project navigation family. Its useful output appears in
contextual Information, attention, history or advanced diagnostic surfaces.

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
summaries and candidate relations
```

Governed use adds:

```text
Décisions
ProjectClaims
history and provenance
```

Advanced use adds optional lenses:

```text
Objets du projet
Evidence detail
external memory diagnostics
adapters
relationship views
```

Unused capabilities remain invisible. Disabling an optional capability must not
remove authoritative project data.

## 5. Project lifecycle coverage

The same core model supports:

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

Domain phases belong to the architecture pack. They do not create a separate card
family or exclusive navigation tree.

## 6. Source-first intake

Any incoming source must be preservable before full classification.

The implementation reuses `document_source` and Dossier Situation Intake. It must
not create a competing universal `InboxItem` ontology.

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
4. no Project is silently created unless explicitly requested;
5. a human question is required only when a wrong choice could have a material
   consequence.

## 7. Document and Information behavior

### 7.1 Document

Document is a first-class card and semantic object.

Typical Documents include:

```text
plan
CCTP
DPGF
email
letter
photograph
spreadsheet
report
IFC
administrative authorization
```

Document types declare their behavior instead of hardcoding it in the Cockpit:

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

### 7.2 Information

Information is limited to intentionally authored, extracted, observed or
consolidated project statements that have their own value independently of the
source document.

Examples:

```text
client requirement
site observation
project synthesis
PLU analysis
coordination note
responsibility analysis
confirmed project value
candidate interpretation
```

An Information card may cite one or more Documents and relate to one or more project
objects. It must preserve whether the statement is observed, inferred, confirmed,
contested or superseded.

### 7.3 Card relations

Documents, Informations, Work and Decisions can all reference project objects.

Example:

```text
Document: AVP D
-> concerns space.living-room

Information: infiltration observed
-> concerns element.window-f32

Work: verify high ventilation
-> concerns space.bedroom-2

Decision: retain existing wall
-> concerns element.wall-m042
```

The object remains authoritative in APU. The card relation remains a separate,
sourced and revisable assertion.

## 8. ProjectClaim use

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
-> human review proportionate to consequence
-> separate governed command when required
-> claim created, superseded, contested or retired
```

A ReviewDisposition never creates a claim by itself.

## 9. One attention surface

The `À traiter` projection aggregates existing objects without copying them:

```text
WorkIssues
ClarificationRequests
ChangeCandidates
ResultCandidates
candidate card-to-object relations
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

The strength of the gate is proportionate to consequence.

```text
reversible low-consequence relation
-> one explicit confirmation may be sufficient

new stable identity, merge, deletion, state change or professional conclusion
-> separate command and stronger authorization
```

## 10. Review versus application

The existing execution-result contract remains the single Hermes result conduit.
No new generic Candidate, Proposal, HermesQuestion or CardInteraction concept is
introduced.

```text
Task Contract
-> Hermes execution
-> ExecutionResult
-> typed ResultCandidate
-> ClarificationRequest where needed
-> human ReviewDisposition
-> separate domain command when consequence requires it
-> authoritative mutation
-> append-only governed event
```

The recently defined APU mapping and write-preparation contracts are internal
implementation details. The Cockpit exposes only the user decision and its effect.

## 11. Mnemosyne boundary

Mnemosyne remains optional external cognitive memory.

It may enrich context, but it does not define a project card family, project object
or authoritative project relation.

```text
memory stored != project knowledge adopted
memory relation != related_project_objects relation
memory available != project readable
```

Mnemosyne timeout or absence must not block Project, Document, Information,
Decision, WorkIssue, ProjectClaim or APU projections.

## 12. Implementation slices

### Slice 0 — baseline scenarios and branch reconciliation

Lock end-to-end scenarios and identify reusable work before code changes.

Checks include first email without project, plan with approximate project name,
new document index, photographs, conflicting value, reception reservation,
claim/dispute context, minimal project and unavailable external memory.

### Slice 1 — authority and vocabulary convergence

Confirm one owner for Project, Document, Information, Work, Decision, ProjectClaim,
APU objects, card-to-object relations and projections. Update existing registries;
do not create a second registry.

Completion: the vocabulary in this roadmap matches schemas, registries and card
projection definitions.

### Slice 2 — shared project-object reference contract

Define one lightweight reference contract usable by Document, Information, Work and
Decision cards.

Initial semantics remain deliberately small:

```text
relation: concerns | located_in | applies_to | compares
status: candidate | confirmed | rejected
certainty: optional E0-E4
```

Completion: no per-card `room_id`, `wall_id`, `zone_id` or parallel graph is needed.

### Slice 3 — Project minimum, aliases and source admission

Implement minimal Project identity, correctable aliases, unassigned sources,
candidate project matches and explicit linking/relinking.

Completion: any supported source can be preserved and corrected before full project
classification.

### Slice 4 — Document series, event documents and internal structure

Consolidate doctype behavior, indices, technical revisions, issued/received state,
event accumulation and structure-before-chunking.

Completion: the system distinguishes a new index, a new event and a technical edit
without duplicate Information storage.

### Slice 5 — Information and card-to-object relations

Implement intentionally authored or extracted Information plus candidate and
confirmed relations from cards to project objects.

Completion: Document, Information, Work and Decision all use the same relation
mechanism, while APU remains the object authority.

### Slice 6 — ProjectClaim persistence and projection

Implement bounded create, supersede, contest and retire operations with provenance
and optimistic revision checks.

Completion: Project cards expose current professional values with source and
history.

### Slice 7 — attention and decision projection

Build one server-owned attention projection over WorkIssue, clarification,
candidate, contradiction, claim and source states.

Completion: all actionable items appear in one UX surface without backend copying.

### Slice 8 — adaptive Cockpit and Anatomie du projet

Implement the four primary project sections and optional lenses through server-owned
projection definitions and registries.

Add the `Anatomie du projet` verso projection to the Project card. It summarizes
APU coverage and related card assertions without becoming authoritative storage.

Completion: minimal projects remain minimal; advanced projects expose additional
lenses without a second Cockpit.

### Slice 9 — governed application and event journal

Apply reviewed consequential changes through explicit commands and record receipts
and authoritative events. Low-consequence reversible relations use the lightest
sufficient gate.

Completion: proposal, review, command, mutation and receipt remain auditable without
forcing every minor relation through the strongest workflow.

### Slice 10 — external adapters and real-project validation

Connect source intake, Docling, Paperless, Hermes, IFC/Revit and Mnemosyne only
through existing contracts and optional bindings.

Validate first on one real project without IFC, then on one project with IFC, then
on one complex ERP or multi-building project.

Completion: no adapter owns project truth merely because it is connected.

## 13. Pull request sequencing

Recommended Pantheon Next sequence:

```text
project-card-and-object-reference-convergence
project-source-intake-contract
document-and-information-boundary
general-knowledge-boundary
adaptive-project-cockpit-and-anatomy-model
```

Recommended pantheon-mvp sequence:

```text
project-aliases-and-source-intake
shared-project-object-references
document-series-and-event-documents
information-and-reference-review
attention-projection
adaptive-project-cockpit-and-anatomy
project-lifecycle-acceptance-tests
```

Do not add another candidate conduit, graph, memory store or approval engine.

## 14. First usable increment

```text
minimal Project
aliases
source admission
correctable project linking
Document cards
Information cards only when semantically justified
shared related_project_objects references
Contenus projection
Nouvelles demandes
```

It must work without Hermes, Mnemosyne, advanced APU inference, Paperless, Docling,
IFC or Revit.

The second increment adds:

```text
À traiter
candidate object relations
ProjectClaims
Décisions
governed application
Anatomie du projet verso
```

## 15. Completion criteria

The convergence is complete when:

1. any practical first input can be admitted;
2. no source is lost because classification is incomplete;
3. a Project can begin with minimal identity;
4. Document is a distinct card and semantic object;
5. Information is not a universal backend container;
6. Connaissances is reserved for reusable cross-project material;
7. Document, Information, Work and Decision can reference project objects through
   one shared mechanism;
8. APU remains the single authority for project objects;
9. Anatomie du projet is a calculated Project-card verso projection;
10. phases and claim/dispute contexts are facets rather than exclusive folders;
11. consequential Project values retain ProjectClaim provenance;
12. Hermes results remain non-authoritative;
13. review strength is proportionate to consequence;
14. one attention projection aggregates actionable states;
15. optional adapters and memory do not burden or block minimal projects;
16. no competing registry, renderer, candidate conduit or graph is introduced;
17. one real non-IFC project and one complex project pass end-to-end validation.

## 16. Non-goals

This roadmap does not:

- implement PostgreSQL migrations, APIs or Cockpit code;
- create a universal Information or Inbox entity;
- create one card per fragment or minor observation;
- create a second project-object graph;
- expose APU, ExecutionResult or authorization internals as primary UX;
- treat Mnemosyne as a project card family;
- copy general Connaissances automatically into project truth;
- authorize automatic Evidence admission, memory promotion or professional
  validation;
- qualify the agency/NAS runtime environment.

```text
plan documented != implementation completed
Anatomie du projet projected != project truth persisted
candidate relation != confirmed relation
reviewed candidate != project mutation
lab accepted != production qualified
```
