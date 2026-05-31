# Architecture Proof Register Schemas

Status: implementation proposal — not implemented.

This folder contains a JSON Schema Draft 2020-12 MVP proposal for the Architecture Proof Register.

It is deliberately small. It models only:

```text
document_family
indexed_document_version
version_event
proof_entry
review_trigger
shared vocabularies
```

It does not implement a database, migration, RLS policy, Directus cockpit, storage backend, OpenWebUI form, Hermes skill, queue runtime, scheduler, approval engine, memory engine or connector.

## Design posture

```text
Store every index.
Govern the effect.
Never let the latest filename decide authority.
```

The model is hybrid:

```text
strict for governance fields
flexible through controlled metadata
light enough to avoid an ERP-like schema
```

## Files

```text
shared.schema.json

document_family.schema.json
indexed_document_version.schema.json
version_event.schema.json
proof_entry.schema.json
review_trigger.schema.json
```

## Core rule

A document family groups versions. It is not proof by itself.

A professional claim must reference an indexed document version when evidence is claimed.

A key index may support a strong authority only when required evidence exists or a review trigger is raised.

## MVP limits

This proposal intentionally does not cover:

```text
file storage implementation
OCR
pgvector
full document ingestion
Directus collections
OpenWebUI forms
Hermes skills
automatic approval
automatic action
```

## Source doctrine

This proposal implements the shape defined by:

```text
docs/governance/ARCHITECTURE_PROOF_REGISTER.md
docs/governance/ARCHITECTURE_INDEX_EFFECT_MATRIX.md
docs/governance/ARCHITECTURE_PROOF_REGISTER_IMPLEMENTATION_SPEC.md
```

Issue: #34 Implement Architecture Proof Register MVP.
