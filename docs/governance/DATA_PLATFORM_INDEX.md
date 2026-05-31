# Data Platform Documentation Index

Status: candidate navigation support doctrine  
Scope: Postgres / Directus / storage / workflow / knowledge / architecture-agency domain pack  
Runtime status: non-executable

## Purpose

This index links the first data-platform documents introduced for Pantheon Next.

The documents below define a candidate doctrine for a modular professional data platform. They do not implement a database, Directus project, workflow runtime, OCR pipeline, vector index, email connector, Google Contacts sync or storage connector.

## Read order

Read in this order:

1. `DATA_PLATFORM_STATUS.md`
2. `DATA_PLATFORM_RECONCILIATION.md`
3. `RAW_DERIVED_GOVERNED_RECORDS.md`
4. `DATA_PLATFORM_ARCHITECTURE.md`
5. `WORKFLOW_LIFECYCLE.md`
6. `KNOWLEDGE_INGESTION_AND_MEMORY.md`
7. `ARCHITECTURE_AGENCY_DOMAIN_PACK.md`

## What each document does

### `DATA_PLATFORM_STATUS.md`

Records the candidate status of the data-platform layer.

It makes explicit that the layer is not implemented and does not create a Postgres schema, Directus project, workflow runtime, OCR pipeline, vector database, connector setup, architecture-agency ERP, automatic approval system or automatic memory promotion.

### `DATA_PLATFORM_RECONCILIATION.md`

Reconciles the data-platform candidate layer with existing Pantheon placement doctrine.

Core boundary:

```text
Govern the data platform from Pantheon.
Do not build the data platform inside Pantheon.
```

It defines which parts belong in Pantheon doctrine and which belong in implementation layers such as storage, Directus, external connectors, Postgres schema proposals or execution runtimes.

### `RAW_DERIVED_GOVERNED_RECORDS.md`

Defines where information actually lives when it should not all be forced into Postgres.

Core boundary:

```text
The database does not hold the whole knowledge.
It holds the governed handles: identity, scope, status, provenance, links, extracted facts, approvals and decisions.
```

It separates raw content, derived content, governed records, retrieval objects, provenance objects, evidence objects and approval records.

### `DATA_PLATFORM_ARCHITECTURE.md`

Defines the overall data-platform posture:

```text
Postgres records.
Directus exposes and controls.
Storage keeps files.
Connectors observe and retrieve.
Hermes may execute bounded jobs.
Pantheon governs the status, scope, proof and approval model.
```

It distinguishes stable core objects from domain packs and sets the boundary between registry, cockpit, storage, connectors and execution support.

### `WORKFLOW_LIFECYCLE.md`

Defines progressive workflow authority:

```text
off -> draft -> test -> shadow -> assisted -> active_guarded -> active_durable
```

It establishes the rule that a workflow starts as a proposal and earns durability through tests, observation, review and explicit authorization.

### `KNOWLEDGE_INGESTION_AND_MEMORY.md`

Defines document ingestion and memory separation:

```text
general memory
agency memory
country memory
project memory
derived memory
validated memory
```

It covers uploaded documents, OCR, Markdown conversion, similarity comparison, vectorization discipline, project facts, public API observations, form preparation and contact memory.

### `ARCHITECTURE_AGENCY_DOMAIN_PACK.md`

Defines a candidate architecture-agency pack:

```text
projects
parties
mail intake
quotes
CCTP
site meetings
site reports
finance follow-up
administrative forms
knowledge libraries
contacts sync
```

It translates architecture practice into modular, testable, non-autonomous data registers.

## Boundary statement

These documents are intentionally not an implementation. They prepare a future implementation by defining:

- what should be represented;
- which objects need statuses;
- which actions require approval;
- where workflow authority may increase;
- how general memory and project memory stay separate;
- how a professional domain pack may be added without freezing the system around one user or one office.

## Operating principle

```text
Build the platform that governs change before building the workflows that perform work.
```

This keeps Pantheon Next aligned with its governance-first posture.
