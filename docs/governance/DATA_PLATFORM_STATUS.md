# Data Platform Status

Status: candidate support status note  
Scope: data platform candidate documents introduced for Pantheon Next  
Runtime status: non-executable

## Purpose

This document records the current status of the data-platform candidate layer.

It exists so the new Postgres / Directus / workflow / knowledge / architecture-agency documents can be tracked without prematurely promoting them to canonical active doctrine in `STATUS.md`.

Read with:

- `DATA_PLATFORM_RECONCILIATION.md` for boundary placement;
- `DATA_PLATFORM_INDEX.md` for reading order;
- `MODULAR_DOMAIN_REORIENTATION.md` for domain-pack placement;
- `CAPABILITY_PLACEMENT.md` for capability placement.

## Current posture

The data-platform layer is a candidate governance support layer.

It is not implemented.

It does not create:

- a Postgres schema;
- a Directus project;
- a workflow runtime;
- an OCR pipeline;
- a vector database;
- a Google Drive connector;
- an SFTP connector;
- a Google Contacts sync;
- a Gmail intake workflow;
- an architecture-agency ERP;
- an automatic approval system;
- automatic memory promotion.

## Candidate documents

The current candidate set is:

- `DATA_PLATFORM_STATUS.md`;
- `DATA_PLATFORM_INDEX.md`;
- `DATA_PLATFORM_RECONCILIATION.md`;
- `DATA_PLATFORM_ARCHITECTURE.md`;
- `WORKFLOW_LIFECYCLE.md`;
- `KNOWLEDGE_INGESTION_AND_MEMORY.md`;
- `ARCHITECTURE_AGENCY_DOMAIN_PACK.md`.

## Candidate value

These documents clarify how Pantheon Next may later govern:

- modular professional data registers;
- stable core objects versus domain packs;
- user-suggested workflows;
- test, shadow and assisted workflow modes;
- general knowledge versus project memory;
- file ingestion, OCR, Markdown conversion and vectorization boundaries;
- contact and organization synchronization boundaries;
- architecture-agency objects such as projects, CCTP, quotes, site reports, finance follow-up and administrative forms.

## Reconciled boundary

```text
Pantheon does not become the data platform.
Pantheon governs the legitimacy, status, scope, memory and approval rules of data-platform behavior.
```

```text
The database records.
The workflow proposes.
The evidence supports.
The approval validates.
The human decides.
```

## Boundary rule

```text
Candidate platform doctrine does not authorize runtime implementation.
```

Any future implementation must still pass through:

- schema proposal;
- module activation review;
- workflow lifecycle review;
- approval policy definition;
- evidence and memory boundary review;
- connector legitimacy review;
- security and confidentiality review.

## Next review questions

Before promotion into active doctrine, the repository should clarify:

1. Which core table families are truly stable enough to become schema candidates?
2. Which architecture-agency objects belong in the first domain pack slice?
3. Which workflows should be modeled first: quote intake, site report preparation, finance follow-up or knowledge ingestion?
4. Which storage profile should be treated as the first reference profile: local/NAS, hosted, or hybrid?
5. How should Directus be described: cockpit candidate, admin UI candidate, or schema-exposure candidate?
6. What connector gateway posture should be used for Gmail, Google Drive, Google Contacts and public APIs?
7. What level of schema detail belongs in governance docs versus future implementation docs?

## Promotion condition

The candidate set may be promoted only when it preserves the existing Pantheon boundary:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

And when it keeps the reconciled data-platform boundary intact:

```text
Govern the data platform from Pantheon.
Do not build the data platform inside Pantheon.
```
