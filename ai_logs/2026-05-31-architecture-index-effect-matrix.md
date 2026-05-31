# AI Log — Architecture Index Effect Matrix

Date: 2026-05-31

## Intervention

Added a candidate support doctrine document for classifying architecture document indices / versions by effect class.

Files touched:

```text
docs/governance/ARCHITECTURE_INDEX_EFFECT_MATRIX.md
ai_logs/2026-05-31-architecture-index-effect-matrix.md
```

Related doctrine:

```text
docs/governance/ARCHITECTURE_PROOF_REGISTER.md
docs/governance/DATA_PLATFORM_RECONCILIATION.md
docs/governance/DOCUMENT_INTELLIGENCE.md
docs/governance/REVIEW_QUEUE.md
```

## Status

```text
documented: yes
implemented: no
partial: yes — candidate support doctrine only
```

No SQL schema, migration, Postgres table, Directus cockpit, document versioning engine, storage backend, approval engine, OpenWebUI action, Hermes skill, queue runtime, scheduler or connector was implemented.

## Added concepts

```text
index effect matrix
key index classes
ordinary index classes
phase attachment matrix
review queue triggers for wrong index authority
forbidden shortcuts
```

## Boundary maintained

The matrix classifies what a document index can support.

It does not decide the professional consequence.

Pantheon governs the status.

The human commits the decision.

## Notes

This document should later be reconciled by index files. No index files were edited in this intervention.
