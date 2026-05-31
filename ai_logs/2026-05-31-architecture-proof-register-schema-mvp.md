# AI Log — Architecture Proof Register Schema MVP

Date: 2026-05-31

## Intervention

Created a dedicated branch with a JSON Schema Draft 2020-12 MVP proposal for the Architecture Proof Register.

Branch:

```text
schema/architecture-proof-register-mvp
```

Files added:

```text
schemas/architecture-proof-register/README.md
schemas/architecture-proof-register/shared.schema.json
schemas/architecture-proof-register/document_family.schema.json
schemas/architecture-proof-register/indexed_document_version.schema.json
schemas/architecture-proof-register/version_event.schema.json
schemas/architecture-proof-register/proof_entry.schema.json
schemas/architecture-proof-register/review_trigger.schema.json
ai_logs/2026-05-31-architecture-proof-register-schema-mvp.md
```

Related issue:

```text
#34 Implement Architecture Proof Register MVP
```

## Status

```text
documented: yes
implemented: partial schema proposal only
runtime implemented: no
database migration implemented: no
```

This is not a Postgres migration and does not create tables.

No RLS policy, Directus collection, object storage layout, OpenWebUI form, Hermes skill, queue runtime, scheduler, approval engine, memory engine or connector was implemented.

## User decisions applied

```text
C — authorize a proposal under schemas/ through branch + PR
B — JSON Schema first
C — full folder with README + separated schemas
B — branch name schema/architecture-proof-register-mvp
C — hybrid locking: strict governance fields + controlled metadata
B — shared.schema.json for common vocabularies
A — JSON Schema Draft 2020-12
B — pantheon:// internal $id identifiers
C — schema status in README/shared only
C — UUID required + optional human_ref
C — hybrid references with labels/context where useful
C — controlled use lists + notes
C — controlled metadata
C — hybrid evidence_refs
C — strict anchors + other with mandatory note
A — dates as YYYY-MM-DD
B — separate calendar and working days
C — split version_status and authority_status
C — detailed authority_status + notes
A — version_status enum validated
severity + consequence_level both kept
C3/C4/C5 external-effect gate rules simplified
requested_use kept in proof_entry and review_trigger
```

## Simplicity decision

After many detailed questions, the user asked to avoid an usine à gaz.

Applied simplification:

```text
only five business schemas
no SQL
no migration
no table design
no validation engine
no attempt to encode every professional edge case
metadata remains controlled
triggers catch only dangerous authority mismatches
```

## Boundary maintained

```text
Store every index.
Govern the effect.
Never let the latest filename decide authority.
```

The proposal is ready for review, not merge as implementation runtime.
