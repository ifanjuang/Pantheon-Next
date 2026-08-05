# Adaptive project lifecycle and Cockpit plan — 2026-08-05

Status: completed documentation trace — no implementation or activation.

## Objective

Record the final converged project experience after review against the current
Pantheon owner doctrines, BIM-management practice and GitHub-style task and variant
mechanics.

## Repository state checked

```text
Pantheon-Next
owner doctrines for six visual card families and six primary navigation spaces,
plus Document, Information, ProjectClaim, WorkIssue, Decision, APU,
ExecutionResult and bounded write preparation.

pantheon-mvp
structured document projection, execution-result persistence, fragment
qualification, APU mapping review and bounded write preparation.
```

The PR remains documentation-only.

## Final decisions

### Navigation

```text
Pantheon
Décisions
Affaires
Connaissances
Compétences
Outils
```

### Visual families and semantic objects

The six visual families remain:

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

`Document` remains a first-class backend semantic object and source/file authority.
It does not become a seventh visual family in this roadmap.

`Information` is the default project-content presentation family when no more
specific projection is required. It is not the exclusive presentation of a
Document: viewers, revision lists, timelines and source browsers remain valid.

### Tâches

The `Work` family uses **Tâches** as its principal UX label.
`WorkIssue` is the principal canonical object projected in this family.

Canonical statuses remain:

```text
open
in_progress
waiting
review
done
cancelled
```

Possible UX labels remain projections only:

```text
À faire
En cours
En attente
À relire
Terminé
Annulé
```

### Information relations

Informations use a lightweight graph rather than a mandatory parent-child tree.
The first implementation is limited to four demonstrated meanings:

```text
répond à
s’appuie sur
remplace
contredit
```

The following remain candidates until real-project validation demonstrates distinct
responsibilities:

```text
complète
dérive de
contient
compare avec
```

The exact field, persistence owner and canonical vocabulary remain deferred until
inventory of existing graph, domain-relation and APU contracts.

### Project and Anatomy

The Project-card back remains the identity sheet: address, parcels, mission, phase,
contacts, surfaces, budget, PLU, authorizations, dates and principal ProjectClaims.
`Anatomie du projet` may be summarized there but does not replace the identity
sheet. It remains a calculated APU-backed projection, not an editable Information or
second graph.

### Knowledge, capabilities and tools

```text
Connaissances
= reusable cross-project knowledge.

Compétences
= governed business capabilities.

Outils
= replaceable technical means.
```

```text
Créer une compétence
-> crée ou propose une Capability candidate gouvernée dans Pantheon.

Implémenter cette compétence
-> peut demander à Hermes de préparer un Skill ou Workflow candidat.

Capability candidate created
!= Hermes Skill implemented
!= Capability admitted
!= Task authorized
```

## Implementation order

```text
0. owner-doctrine and vocabulary convergence
1. minimal Project, aliases and source intake
2. Information-family cards with optional Document backing, dates, indices,
   formats, statuses, tags and Contacts
3. Tâches, global/project Decisions and one attention surface
4. four minimal Information relations after authority inventory
5. ProjectClaims
6. variants validated before any branch object
7. Anatomy relations and projection
8. Compétences registry and bounded Hermes implementation links
9. optional adapters and real-project validation
```

The first usable increment works without APU, Hermes, IFC, Mnemosyne, Paperless or
Docling.

## Non-effects

```text
no schema
no WorkIssue lifecycle change
no migration
no API
no Cockpit implementation
no adapter
no runtime execution
no Hermes Skill or Workflow creation
no capability admission
no task authorization
no Evidence admission
no memory promotion
no project mutation
```

```text
plan documented != implementation completed
Information default projection != exclusive Document presentation
Work family != WorkIssue identity
candidate relation != adopted relation
Anatomie displayed != APU authority replaced
Capability candidate != Hermes Skill implemented
Capability admitted != task authorized
```