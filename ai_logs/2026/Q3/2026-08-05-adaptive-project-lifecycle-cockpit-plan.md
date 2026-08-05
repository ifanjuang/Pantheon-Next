# Adaptive project lifecycle and Cockpit plan — 2026-08-05

Status: completed documentation trace — no implementation or activation.

## Objective

Record the converged project-card taxonomy, Cockpit hierarchy and implementation
plan after review of the adaptive lifecycle roadmap.

## Repository state checked

```text
Pantheon-Next
project, document, execution-result, APU mapping and bounded write-preparation
contracts present

pantheon-mvp
structured document projection, execution-result persistence, fragment
qualification, APU mapping review and bounded write preparation present
```

The PR remains documentation-only. No schema, migration, API, Cockpit code or
adapter is modified.

## Decisions recorded

1. The Cockpit is an adaptive projection, not a fixed storage tree.
2. Project navigation uses four primary sections:

```text
Vue d’ensemble
Contenus
À traiter
Décisions
```

3. These navigation sections are not card types.
4. The shared project-card family retains distinct business types:

```text
Project
Document
Information
Work
Decision
Contact
Tool
```

5. `Document` is a first-class card and semantic object. It is not projected only
   through the Information family.
6. `Information` is limited to project statements, observations, analyses and
   syntheses that have value independently of their source document.
7. A Document must not be duplicated as Information merely for display.
8. `Connaissances` is reserved for general cross-project content such as DTU,
   regulation, MAF guidance, jurisprudence, agency methods and reusable technical
   references.
9. A retrieved general knowledge item is not automatically applicable project
   truth.
10. APU remains the internal authority for project objects.
11. The user-facing APU lens is `Objets du projet`.
12. Documents, Informations, Work and Decisions may all reference project objects
    through one lightweight shared mechanism.
13. Card-to-card relations remain distinct from card-to-project-object relations.
14. `Anatomie du projet` is the user-facing synthesis of project understanding.
15. `Anatomie du projet` appears on the verso of the Project card and is a calculated
    projection, not a new card type, database or Knowledge object.
16. The project secondary lenses are limited to useful business surfaces:

```text
Contacts
Objets du projet
Sources et provenance
Outils
```

17. Mnemosyne is optional external memory and does not define a primary project
    navigation family.
18. Review strength must remain proportionate to consequence. A reversible relation
    to an existing object should not be forced through the same gate as a new stable
    identity, merge, deletion, state change or professional conclusion.
19. The existing ExecutionResult conduit remains the single Hermes candidate path.
20. The first usable increment must work without Hermes, Mnemosyne, Paperless,
    Docling, IFC or Revit.

## Target hierarchy

```text
Pantheon
├── Affaires
├── Connaissances
└── Outils
```

Within a project:

```text
Projet
├── Vue d’ensemble
│   └── verso: Anatomie du projet
├── Contenus
│   ├── Documents
│   └── Informations
├── À traiter
│   ├── Travaux
│   ├── Questions
│   └── Contradictions
└── Décisions
```

Optional lenses:

```text
Contacts
Objets du projet
Sources et provenance
Outils
```

## Implementation direction

The next bounded implementation work should converge existing contracts rather than
add abstractions:

```text
shared project-object reference contract
-> Document / Information / Work / Decision adoption
-> candidate and confirmed relation review
-> adaptive Cockpit projection
-> Anatomie du projet verso
-> validation on real projects
```

No second graph, candidate conduit, memory store, universal Information object or
approval engine is introduced.

## Artifact updated

```text
docs/roadmaps/ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN.md
```

The roadmap was shortened and aligned with the final vocabulary and hierarchy.

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
Anatomie du projet projected != project truth persisted
candidate relation != confirmed relation
review path present != domain mutation implemented
```
