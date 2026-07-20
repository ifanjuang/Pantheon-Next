# Add the Document to Knowledge slice contract

Date: 2026-07-20

Status: validation-only trace — schema implemented / external persistence not adopted.
Boundary profile: validation_only_trace.

## Change

- Added a strict transport-neutral schema for Source Document, extraction observation, chunks, Project Document Card, Knowledge publications and version events.
- Added one fictional valid example and focused positive and negative schema tests.
- Documented publication status, parent-project linkage, provenance, non-authority values, optimistic versioning and idempotency requirements.
- Indexed the contract in the governance authority map.

## Why

The project needed one bounded and testable handoff between project documents and reusable Markdown Knowledge before an external PostgreSQL adapter, mobile client or intelligent editor could implement it without inventing a competing data model.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: yes — schema and schema tests, within the requested Document to Knowledge implementation scope.
Runtime impact: none in Pantheon Next; the contract is transport-neutral.
Authority impact: none; generated Knowledge remains neither Evidence, governed memory nor doctrine.
Schema/test/CI impact: one schema, one example and focused validation coverage added.
External action: repository publication only; no source document is read or modified.
Memory behavior: none.

## Local distinctions

```text
schema_valid != adapter transaction enforced
fixture != live parser observation
knowledge publication != Evidence admission
generated_unreviewed != reviewed
offline replay != overwrite permission
```
