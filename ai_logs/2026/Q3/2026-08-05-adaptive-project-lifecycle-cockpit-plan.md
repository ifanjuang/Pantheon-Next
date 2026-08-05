# Adaptive project lifecycle and Cockpit plan — 2026-08-05

Status: completed documentation trace — no implementation or activation.

## Objective

Record the final converged project experience after review of the adaptive lifecycle
roadmap, BIM-management inspiration, GitHub-style task and variant mechanics, and the
existing Pantheon owner doctrines.

## Repository state checked

```text
Pantheon-Next
owner doctrines for six visual card families, five primary navigation spaces,
Document, Information, ProjectClaim, WorkIssue, Decision, APU, ExecutionResult and
bounded write preparation are present.

pantheon-mvp
structured document projection, execution-result persistence, fragment
qualification, APU mapping review and bounded write preparation are present.
```

The PR remains documentation-only. No schema, migration, API, Cockpit code or
adapter is modified.

## Decisions recorded

### Global navigation

```text
Pantheon
Décisions
Affaires
Connaissances
Compétences
Outils
```

`Décisions` remains the cross-agency human inbox. `Connaissances` contains reusable
cross-project knowledge. `Compétences` exposes governed business capabilities.
`Outils` exposes replaceable technical means.

### Visual families and semantic objects

The existing six visual families remain:

```text
Project
Information
Contacts
Work
Decision
Tool
```

```text
UX card family != backend semantic entity
```

`Document` remains a first-class backend semantic object and technical authority
when a file or source record exists. It does not become a seventh visual family in
this roadmap without owner-doctrine convergence.

`Information` is the central visual family for useful project content, including
emails, plans, photographs, tables, CCTP, reports, notes and native Pantheon content.
A card may have no file, one file or several files.

### Project experience

```text
Vue d’ensemble
Contenus
À traiter
Décisions
```

The Project-card back remains the identity sheet: address, parcels, mission, phase,
contacts, surfaces, budget, PLU, authorizations, dates and principal ProjectClaims.
`Anatomie du projet` may be summarized there but does not replace the identity
sheet.

### Information grammar

```text
upper left
-> business kind, professional index, business date

upper right
-> media/data icons: email, PDF, text, table, photo, audio, IFC, etc.

body
-> title, summary, origin, lifecycle status and limits

lower right
-> subject tags, allowed to wrap onto additional lines
```

Tags support search and context but do not define applicability, relation, status or
professional truth.

### Information relations

Informations use a lightweight graph rather than a mandatory parent-child tree.
One response may relate to several prior messages and several messages may respond
to one request.

Initial user-facing meanings are limited to:

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

The exact field, persistence owner and canonical vocabulary remain deferred until
inventory of existing graph, domain-relation and APU contracts.

### Tâches

```text
Tâche UX = WorkIssue internally
```

A Tâche is autonomous and may concern a Project, Information, Decision, Contact,
Anatomy object, several of these or the agency without a Project. Related cards
project the same WorkIssue identity; they do not contain copies.

### Décisions

A Decision is a structured human intervention conditioning continuation. It may
result from low confidence, contradiction, ambiguity, missing information, variant
selection, important external response, authorization, reception or responsibility.

Hermes may propose a Decision. Hermes does not decide.

### Variants

```text
variant != revision != professional index != lifecycle status
```

GitHub branches inspire the UX of competing variants. The roadmap does not yet
create a universal `InformationBranch` object. Existing version and derivation
contracts must be tested first.

### Anatomie du projet

`Anatomie du projet` is the user-facing APU-backed projection covering buildings,
levels, zones, spaces, elements, systems, fire zones, functional sectors,
compartments, flows, paths, work relations and project states.

It may reuse the Information visual grammar but is not an ordinary editable
Information and not a second graph store.

### Knowledge, capabilities and tools

```text
Connaissances
= what Pantheon may know and mobilize across projects.

Compétences
= what Pantheon knows how to accomplish as governed business capabilities.

Outils
= replaceable technical means.
```

Pantheon exposes its governed capabilities, fixed or addable. It does not duplicate
the complete Hermes skill catalogue. Create-skill and create-workflow paths remain
subject to admission and authorization.

## Implementation order

```text
0. owner-doctrine and vocabulary convergence
1. minimal Project, aliases and source intake
2. Information cards with optional Document backing, dates, indices, formats,
   statuses, tags and Contacts
3. Tâches, global/project Decisions and one attention surface
4. minimal Information relation vocabulary after authority inventory
5. ProjectClaims
6. variants validated before any branch object
7. Anatomy relations and projection
8. Compétences registry and bounded Hermes implementation links
9. optional adapters and real-project validation
```

The first usable increment works without APU, Hermes, IFC, Mnemosyne, Paperless or
Docling.

## Artifact updated

```text
docs/roadmaps/ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN.md
```

## Non-effects

```text
no schema
no migration
no API
no Cockpit implementation
no adapter
no runtime execution
no installation
no activation
no task authorization
no Evidence admission
no memory promotion
no project mutation
```

```text
plan documented != implementation completed
Information projected != semantic responsibilities collapsed
Anatomie displayed != APU authority replaced
candidate relation != adopted relation
capability created != capability admitted
reviewed candidate != project mutation
```
