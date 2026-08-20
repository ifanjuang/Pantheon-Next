# Category Classification Model

Status: validation-only proposal — implemented as schemas.

## Purpose

This proposal specializes `AGENCY_DATA_SYSTEM_OF_RECORD.md` for the distinction between hierarchical `Category` records, transversal `Tag` vocabulary and the Card/Collection projection that exposes classification in the Cockpit. It does not replace that owner document or create an independent authority family.

It generalizes the useful part of the earlier `knowledge_folder` candidate without creating a second Folder backend model.

```text
Category
= stable logical classification/navigation record

CategoryAssignment
= explicit N:N link from one owner record to one Category

Collection
= Cockpit projection of a Category or another declared child relation

Tag
= transversal controlled vocabulary
```

The server remains authoritative for persisted categories and assignments. A Card is only a projection.

## Implementation status

The validation contract is implemented in this repository through `schemas/category_classification.schema.yaml` and its tests.

The operational candidate is implemented in `pantheon-mvp`:

```text
pantheon-mvp #328
→ PostgreSQL Category + CategoryAssignment owner records
→ human-gated writes and bounded reads
→ hierarchy / assignment integrity and concurrency tests
```

The Cockpit Card/Collection projection is still converging. `Category` persistence being implemented does not mean the final recursive Cockpit projection, legacy scalar-category migration or multi-Project reuse model is complete.

```text
schema implemented != Cockpit projection complete
Category persisted != legacy scalar category migrated
CategoryAssignment available != Project reuse solved
```

## Core distinctions

```text
Category != Tag
Category != physical folder
Category != Project ownership
Category != scope or authorization
Category != lifecycle status
CategoryAssignment != EntityRelation
CategoryAssignment != Evidence
CategoryAssignment != approval
Collection != persisted Category by necessity
UI grouping != business truth
```

`agency_entity_relations` remains reserved for qualified semantic relations such as `relies_on`, `responds_to`, `supersedes` and `contradicts`. Ordinary classification must not be encoded as one of those relations.

The existing Tag Registry remains the shared vocabulary for type and subject tags. Category does not replace it.

## Category record

A Category has stable identity and at most one direct parent.

```text
category_id
title
description
parent_category_id | null
applies_to[]
sort_order
revision
created_by
updated_by
created_at
updated_at
archived_at | null
```

The single-parent rule is deliberate. It keeps category navigation a predictable tree while allowing the classified entities themselves to appear in several branches through N:N assignments.

```text
one Category -> zero or one parent Category
one Category -> zero or many child Categories
one entity -> zero or many Categories
one Category -> zero or many entities
```

Cycles are invalid.

```text
A -> B -> A
= invalid
```

A Category may constrain the entity types it accepts through `applies_to`. That constraint limits classification compatibility only; it does not authorize reading, writing, executing or approving the entity.

## Category assignment

`CategoryAssignment` links an existing owner record to an existing Category without changing the record's identity or authority.

Minimum shape:

```text
assignment_id
category_id
entity_type
entity_id
assigned_by
assigned_at
revision
retired_at | null
retired_by | null
```

An active `(category_id, entity_type, entity_id)` link is unique. Removing an assignment retires the link rather than rewriting or deleting the classified entity.

The same entity may have several active assignments.

Example:

```text
document:plui-metropole
  -> Category Urbanisme
  -> Category Référentiels

same document identity
same source
no copied bytes
no duplicate business record
```

## Project reuse is separate

Category classification does not solve project ownership or project reuse.

A Project-specific owner may keep its primary/owner Project while an explicit scope or project-link mechanism makes the same stable entity visible from other Projects. That mechanism must remain separate from CategoryAssignment.

```text
classified under Urbanisme
!= linked to Project Lieurey

linked to Lieurey
!= owned by Lieurey
```

This separation is required before generalizing `Information.project_id`, `doc_documents.parent_project_id` or other current single-Project owners.

## Card / Collection projection

The Cockpit may project a Category as a container Card with a child Collection.

```text
Category Card
  -> child_collection
       -> child Category Cards
       -> assigned entity Cards
```

The same mechanism recurses without a fixed depth.

The projected collection order may place child Categories before directly assigned entities, but ordering is presentation policy, not authority.

An entity with no Category assignment must not disappear. It remains visible in the relevant owner/project/root collection according to that collection's query.

A record assigned to several Categories may appear in several Collections while retaining one `entity_type + entity_id` identity.

```text
one entity
many bounded presentations
no identity duplication
```

## Knowledge convergence

The earlier Knowledge UX note used `knowledge_folder` as a candidate conceptual backend object. Its useful semantics are retained here and generalized:

```text
knowledge_folder.parent_folder_id
-> Category.parent_category_id

knowledge_folder_item_link
-> CategoryAssignment
```

Do not add a parallel persisted `Folder` model for Cockpit classification.

Human-facing copy may use familiar navigation wording when needed, but the backend/classification authority remains Category. Physical NAS or Markdown directories remain source/storage organization and are not automatically Category records.

```text
physical directory != Category
Cockpit Category move != source-byte relocation
Category retirement != source deletion
```

## Tag coexistence

Tags remain non-hierarchical transversal qualifiers managed through their existing registry vocabulary.

Typical use:

```text
Category: Réglementations / Urbanisme
Tags: plu, zone-naturelle, maison-individuelle
Status: reviewed
```

These axes remain independent.

```text
category assignment != tag assignment
category assignment != reviewed
reviewed != approved
```

## Hermes rule

Hermes may suggest a Category or CategoryAssignment under a bounded task, but suggestion is not persistence.

```text
suggested Category != created Category
suggested assignment != persisted assignment
persisted assignment != validated fact
runtime_success != classification authority
```

Any write uses the owner API and applicable human/consequential gate. No Category grants runtime capability or task authorization.

## Hindsight / retrieval rule

Associative retrieval may suggest likely categories, related records or missing assignments. Those suggestions remain retrieval output until admitted by the owner path.

```text
recalled != truth
suggested relation != persisted relation
stored != validated
```

Structured navigation must continue to work when Hindsight or another associative memory is unavailable.

## Migration posture

Current implementation fields such as:

```text
agency_information_cards.category TEXT
agency_information_cards.type_tags JSONB
agency_information_cards.subject_tags JSONB
doc_documents.parent_project_id
```

remain observed compatibility inputs until their consumers are inventoried and migrated. The persisted Category model must not silently reinterpret the text `category` column as a canonical Category identity.

Current progression:

```text
1. introduce Category + CategoryAssignment owner records;            DONE in pantheon-mvp #328
2. expose owner read projection and integrity tests;                 DONE in pantheon-mvp #328
3. map existing scalar categories explicitly where justified;       NOT DONE
4. move Cockpit navigation to Category Card/Collection projection;   IN PROGRESS
5. retire legacy scalar classification after all consumers migrate;  NOT DONE
```

## Boundary

This proposal introduces no runtime, scheduler, queue, provider router, plugin manager, memory engine, approval engine or automatic classification authority.

```text
Category valid != category approved as truth
Category assigned != task authorized
Category visible != source authoritative
Collection loaded != entity validated
```