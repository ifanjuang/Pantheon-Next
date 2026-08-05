# Adaptive Project Lifecycle and Cockpit Convergence Plan

Status: validation-only roadmap — documented, not implemented.
Boundary profile: candidate_support_note.
Date: 2026-08-05

```text
OpenWebUI exposes conversation and intake.
Hermes executes bounded admitted work.
Pantheon Next governs semantics, authority and consequential transitions.
pantheon-mvp owns executable persistence, APIs, projections and adapters.
The human decides consequential effects.
```

## 1. Objective

Define a simple professional experience that can begin from any practical agency
input — email, mission letter, plan, PLU extract, spreadsheet, photograph, question
or uploaded file — and remain coherent through design, authorization, consultation,
works, reception, GPA, claim and dispute.

The roadmap converges existing contracts and doctrines. It does not create a new
runtime, graph, inbox engine, scheduler, queue, provider router, memory engine,
approval engine or automatic project mutation.

## 2. Product navigation

The accepted first-level navigation remains:

```text
Pantheon
Décisions
Affaires
Connaissances
Compétences
Outils
```

Responsibilities:

```text
Pantheon
= contextual conversation and intake.

Décisions
= cross-agency human inbox for questions, confirmations, arbitrations and
  consequential authorizations.

Affaires
= projects and their complete lifecycle.

Connaissances
= reusable cross-project knowledge: DTU, standards, regulation, MAF guidance,
  jurisprudence, agency doctrine, methods and technical references.

Compétences
= governed business capabilities visible to the user: analyse PLU, CCTP,
  comparison, estimation, reception, responsibility analysis and similar work.

Outils
= replaceable connectors, adapters, services, plugins, MCP entries and runtimes.
```

```text
knowledge retrieved != applicable project rule
capability created != capability admitted
capability available != task authorized
tool installed != tool adopted
```

## 3. Visual families and semantic objects

The Cockpit and the backend deliberately use different vocabularies.

```text
UX card family != backend semantic entity
navigation section != card family
projection != persistence
```

### 3.1 Current visual families

The existing architecture-facing visual grammar remains:

```text
Project
Information
Contacts
Work
Decision
Tool
```

User-facing vocabulary:

```text
Work family -> Tâche
WorkIssue -> internal canonical object
```

`Issue`, `Task`, `Todo`, `Action`, `Ticket` and `WorkItem` are not additional
Pantheon concepts.

### 3.2 Semantic objects

The backend may distinguish, among others:

```text
Project
Document
Information
ProjectClaim
WorkIssue
Decision
Person
Organization
Participation
Knowledge
Capability
Evidence
ResultCandidate
APU objects and relations
```

A `Document` is therefore a first-class semantic object without necessarily
becoming a seventh primary visual family.

## 4. Project experience

The primary project navigation remains deliberately small:

```text
Vue d’ensemble
Contenus
À traiter
Décisions
```

These are server-owned projections.

```text
Vue d’ensemble
-> Project card and current project summary.

Contenus
-> Information cards representing useful project content.

À traiter
-> Tâches, questions, contradictions and review items requiring attention.

Décisions
-> project-scoped Decision objects and their history.
```

Secondary views appear only when useful:

```text
Contacts
Anatomie du projet
Sources et provenance
Outils
```

The global `Décisions` space and the project `Décisions` section are two projections
of the same governed Decision identities, not duplicate records.

## 5. Project card

### 5.1 Front

The front remains a concise operational summary:

```text
project name
location
phase
status
main context
important alerts
```

### 5.2 Back

The back is the project identity sheet. It may expose:

```text
address
parcels
mission
phase and contexts
main client / MOA
principal contacts
surfaces
budget or works amount
PLU / zoning
authorizations
key dates
principal ProjectClaims and provenance posture
```

`Anatomie du projet` does not replace this identity sheet. The back may show a
compact Anatomy summary when useful, with the full projection opened separately.

## 6. Information as the central content surface

`Information` is the principal visual family for project content.

An Information card may present:

```text
email
letter
meeting or site report
note
plan
sketch
photograph
table
CCTP
DPGF
devis
diagnostic
attestation
analysis
synthesis
IFC or other model representation
native Pantheon content
```

It may have no file, one file or several files.

### 6.1 Document boundary

```text
Information card
= user-facing content projection.

Document
= backend authority for a file or source-bearing documentary record.
```

Document owns, when applicable:

```text
original bytes or external source reference
hash
format
pages or native units
attachments
structure and extraction
version and index
provenance
archive state
```

A Document is not duplicated as a second Information semantic object merely for
display. The Information card may project the Document directly or present an
authored/observed synthesis supported by one or more Documents.

### 6.2 Information semantic boundary

A semantic Information is an observation, requirement, analysis, note or synthesis
that retains professional value independently of one source file.

```text
Information
!= ProjectClaim
!= ResultCandidate
!= Decision
!= WorkIssue
```

Examples:

```text
client requirement
site observation
PLU analysis
coordination note
responsibility analysis
project synthesis
```

A structured professional value such as a surface, budget, PLU zone or reception
date normally uses `ProjectClaim` when provenance, date, contradiction or
obsolescence matters.

An unadopted Hermes interpretation remains a `ResultCandidate`. It becomes an
Information only when deliberately retained as an authored or consolidated analysis.

## 7. Information card grammar

### 7.1 Upper left

```text
business kind
professional index when applicable
business date
```

Examples:

```text
CCTP · indice B · 5 août 2026
CR n°14 · réunion du 2 août 2026
Email · reçu le 5 août 2026
```

### 7.2 Upper right

Icons describe the actual media and data modes:

```text
email
PDF
text
table
image
photo
audio
video
DOCX
XLSX
IFC
link
```

Several may coexist.

### 7.3 Body

```text
title
summary
author or origin
lifecycle status
limits or restrictions when relevant
```

### 7.4 Lower right

Subject tags are aligned toward the lower right and may wrap onto additional lines
when needed.

Examples:

```text
couverture
RE2020
juridique
DTU
responsabilité
structure
accessibilité
incendie
réception
sinistre
```

Tags support filtering, discovery and Hermes context selection. They do not replace
relations, status, version, applicability or professional conclusions.

```text
tagged DTU != applicable DTU confirmed
tagged conforme != compliance validated
```

## 8. Dates, variants, revisions, indices and status

The implementation must preserve these differences:

```text
Variant
= concurrent option.

Revision
= successive evolution of the same option.

Professional index
= issued professional version.

Lifecycle status
= position in the content lifecycle.
```

```text
variant != revision
revision != professional index
professional index != lifecycle status
```

Relevant dates may include:

```text
source_date
received_at
issued_at
updated_at
```

The card displays the most relevant business date. Internal technical edits do not
consume a new professional index.

## 9. Relations between Informations

Informations form a lightweight graph, not a mandatory parent-child tree.

A response may relate to several prior emails. Several messages may respond to the
same request. A synthesis may rely on emails, plans, photos and decisions.

Initial user-facing relation meanings remain deliberately limited:

```text
répond à
s’appuie sur
complète
remplace
contredit
dérive de
contient
compare avec
```

The exact storage field, relation authority, vocabulary identifiers and review
status must be decided after inventory of the existing generic graph, domain
relations and APU mapping contracts.

```text
relation shown on a card
!= new relation authority
explicit relation
!= inferred candidate relation
```

Explicit relations are priority context for Hermes. Their absence never means that
Hermes may skip autonomous compatibility checks.

## 10. Variants inspired by GitHub branches

The UX may present `Variantes` for genuinely competing options:

```text
architectural alternatives
technical scenarios
cost scenarios
phasing alternatives
response drafts
functional options
```

A selected variant becomes the current reference through a Decision or other
governed adoption. Rejected alternatives remain historized.

The roadmap does not yet create a universal `InformationBranch` schema. Existing
version, derivation and relation contracts must be inventoried first. A new branch
object is justified only if real-project tests show that relations and revisions are
insufficient.

## 11. Tâches

User-facing name:

```text
Tâche
```

Internal canonical object:

```text
WorkIssue
```

A Tâche is an autonomous action, not a status of an Information and not a child
record copied into each card.

Typical fields:

```text
title
description
owner
due date
priority
status
comments
history
labels when useful
```

Typical statuses:

```text
open
in_progress
waiting
blocked
completed
cancelled
```

A Tâche may concern:

```text
a Project
an Information
a Decision
a Contact
an Anatomy object
several of these at once
or the agency without a Project
```

Each related surface projects the same WorkIssue identity.

## 12. Décisions

A Decision is a structured human intervention that conditions continuation.

It may result from:

```text
low confidence
contradiction
ambiguity
missing information
choice between variants
important external response
authorization
budget arbitration
reception or responsibility decision
```

Hermes may propose a Decision or clarification. Hermes does not decide.

```text
wait for a quote
-> Tâche with waiting status

judge whether the quote is acceptable
-> Decision
```

The global `Décisions` space provides the cross-agency human inbox. The project
section provides the scoped projection.

## 13. Contacts

`Contacts` is an aggregated visual projection grouped by project role, for example:

```text
MOA / client
MOE
BET
companies
control office
SPS
administrations
insurers
experts
```

Backend authority remains separated:

```text
Person
Organization
Participation
```

## 14. Anatomie du projet

`Anatomie du projet` is the user-facing structural, spatial, functional and
technical understanding of an affair.

It may include:

```text
site and parcels
buildings
levels
zones
spaces
elements
systems
fire zones
functional sectors
compartments
flows
paths
relations between works
existing / demolition / projected / as-built states
```

Sources may include plans from architects and engineering offices, sections,
elevations, perspectives, sketches, photographs, CCTP, diagnostics, IFC, Revit and
human observations.

```text
APU
= internal authority for project objects and relations.

Anatomie du projet
= calculated user-facing projection of APU coverage, provenance and uncertainty.
```

It may reuse the Information visual grammar, but it is not an ordinary editable
Information and not a second graph store.

## 15. Relations to Anatomy objects

Informations, Tâches and Decisions must be able to concern project objects such as
spaces, zones, elements or systems.

The roadmap records the capability but does not prescribe a new universal
`related_project_objects[]` field.

Implementation must first inventory and converge:

```text
existing generic graph relations
architecture-domain typed relations
APU mapping and review contracts
card projection definitions
```

The chosen persistence must have one owner and must not create a parallel graph.

## 16. Connaissances, Compétences and Outils

### 16.1 Connaissances

General reusable knowledge outside one affair.

### 16.2 Compétences

Business-facing capabilities such as:

```text
Analyser un PLU
Comparer deux plans
Préparer un DCE
Rédiger un CCTP
Analyser un devis
Préparer une réception
Rapprocher une photo d’un espace
Analyser une responsabilité
```

A Capability may internally reference workflows, knowledge, rules, templates,
responsibilities, rites, places, tools and Hermes implementations.

Pantheon exposes its governed capabilities. It does not duplicate the complete
internal Hermes skill catalogue.

Some capabilities are fixed and protected. Others may be created or proposed
through create-skill or create-workflow paths, subject to admission and authorization.

### 16.3 Outils

Replaceable technical means. Availability does not create adoption or task
authorization.

## 17. Hermes context and compatibility checks

When Hermes works on an Information, priority context may include:

```text
explicitly related Informations
current and competing variants
newer indices
open contradictions
linked Tâches
applicable Decisions
related Anatomy objects
selected general Knowledge
sources and limits
```

Hermes must also search for relevant incompatibilities not yet explicitly related,
including:

```text
version compatibility
phase compatibility
existing / demolition / projected state compatibility
disciplinary compatibility
semantic value conflicts
applicability of general Knowledge
```

Hermes produces candidates, questions and bounded results. It does not directly
create project truth, Evidence, memory promotion or consequential effects.

## 18. Core lifecycle loop

```text
Source
-> Information projection or authored Information
-> explicit and candidate relations
-> Hermes understanding
-> Tâche when action is needed
-> Decision when human arbitration is needed
-> result or new Information
-> Anatomy enriched when project-object relations are adopted
-> Project understanding improved
```

## 19. Required invariants

```text
1. Project is the root of an affair.
2. Information is the central visual family for project content.
3. Document remains backend authority when a file or source record exists.
4. Tâche UX = WorkIssue internally.
5. Decision = structured human intervention conditioning continuation.
6. Contacts = projection of Person, Organization and Participation.
7. Anatomie du projet = calculated APU-backed projection.
8. Connaissances, Compétences and Outils remain distinct responsibilities.
9. Variant != revision != professional index != lifecycle status.
10. Information != ProjectClaim != ResultCandidate.
11. Explicit relation != inferred candidate relation.
12. Projection != persistence.
13. Hermes proposes; Pantheon governs; the human decides consequential effects.
```

## 20. Implementation order

### Slice 0 — authority and vocabulary convergence

Align this roadmap with owner doctrines, registries, schemas and projection
contracts. Do not announce replacement of an owner document from a roadmap alone.

### Slice 1 — minimal Project and source intake

Implement minimal identity, aliases, unassigned source admission, candidate project
matching and correctable linking.

Completion: a project may begin from any practical source without Hermes or APU.

### Slice 2 — Information and Document projection

Implement Information card grammar, optional Document backing, dates, indices,
formats, lifecycle status, subject tags and Contacts.

Completion: email, text, plan, photo, table and CCTP can be represented without
creating a new visual family per format.

### Slice 3 — Tâches, Décisions and attention

Converge WorkIssue as Tâche, global and project Decision projections, contradictions,
questions and one attention surface.

### Slice 4 — Information relations

Add the smallest useful relation vocabulary after inventory of existing relation
authorities. Support one-to-many and many-to-one relations.

### Slice 5 — ProjectClaims and consequential values

Persist and project source-backed professional values without collapsing them into
ordinary Information.

### Slice 6 — Variantes

Validate variants first with relations, revisions and Decision-based selection.
Add a branch object only if real use demonstrates a distinct responsibility.

### Slice 7 — Anatomy relations and projection

Relate project content and Tâches to existing APU objects through the converged
relation authority. Add the `Anatomie du projet` projection only when useful data
exists.

### Slice 8 — Compétences

Expose a governed Pantheon capability registry, fixed and addable capabilities, and
bounded create-skill/create-workflow paths without duplicating Hermes internals.

### Slice 9 — adapters and real-project validation

Validate successively:

```text
one real project without IFC
one project receiving IFC later
one complex ERP, IGH or multi-building project
```

Paperless, Docling, Hermes, Revit, IFC and Mnemosyne remain optional adapters or
implementations. None owns project truth merely because it is connected.

## 21. First usable increment

The first increment is deliberately independent of APU and advanced AI:

```text
minimal Project
aliases
source admission
correctable project linking
Information cards
optional Document backing
formats, dates, indices, statuses and tags
Contacts
Contenus projection
Nouvelles demandes
```

The second increment adds:

```text
Tâches
Décisions
À traiter
ProjectClaims
basic Information relations
```

Anatomy, advanced variants, Compétences integration and external adapters follow
only after the daily project cycle is stable.

## 22. Completion criteria

The roadmap is successfully implemented when:

1. any practical first input can be admitted without loss;
2. Project identity and aliases remain correctable;
3. Information cards represent file-backed and native content consistently;
4. Document authority is preserved without visual duplication;
5. dates, indices, variants, revisions and statuses remain distinct;
6. tags remain descriptive and relations remain structural;
7. Tâches are unique WorkIssues projected in all relevant contexts;
8. global and project Decisions share one identity;
9. Informations support multi-source and multi-response relations;
10. ProjectClaims retain consequential value provenance;
11. Anatomy appears only as an APU-backed projection;
12. Knowledge, Capability and Tool responsibilities remain separate;
13. optional adapters can be disabled without losing authoritative project data;
14. real projects without IFC, with later IFC and with complex building typologies
    pass end-to-end tests.

## 23. Non-goals

This roadmap does not:

- implement schemas, migrations, APIs or Cockpit code;
- create a universal Information backend table for every object;
- create a seventh visual family without owner-doctrine convergence;
- create a mandatory parent-child Information hierarchy;
- create a universal branch system before real validation;
- create a second relation graph;
- make APU, IFC, Hermes, Mnemosyne, Paperless or Docling mandatory;
- make tags authoritative;
- allow Hermes to admit Evidence, promote memory or apply consequential changes;
- qualify the agency/NAS runtime.

```text
plan documented != implementation completed
Information projected != semantic responsibilities collapsed
Anatomie du projet displayed != APU truth replaced
candidate relation != adopted relation
reviewed candidate != project mutation
```
