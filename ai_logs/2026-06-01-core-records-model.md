# AI Log — Core Records Model

Date: 2026-06-01

## Scope

Added `docs/governance/CORE_RECORDS_MODEL.md`: the tool-agnostic, profession-agnostic
record model shared by every domain (contact, organization, scope, document, message,
event, decision, membership, party role) and the rule that keeps dossiers separated by
`scope_id`.

This answers a practical user question: a multi-profession system needs a base for
contacts, dossier separation, document pieces and emails that is common to every trade,
with the profession-specific objects layered on top.

## Why

The user is building toward a system usable across liberal professions. Contacts,
separated dossiers, documents and emails are not architecture-specific — they are the
common backbone. Placing them in one profession's pack would force a rewrite for the
next profession. This document fixes them once, in a stable core, with domain packs
extending it.

Scope is the load-bearing rule: every core record carries `scope_id`, which guarantees
dossier watertightness, confidentiality and controlled reuse. The scope vocabulary and
isolation rule are owned by `SCOPE_ISOLATION.md`; this model references that rather than
restating it.

## Files changed

Added:

- `docs/governance/CORE_RECORDS_MODEL.md`;
- `ai_logs/2026-06-01-core-records-model.md`.

Updated:

- `CHANGELOG.md`;
- `docs/governance/MODULES.md` (module map row);
- `docs/governance/AUTHORITY_INDEX.md` (authority map row).

Indexing note: `STATUS.md` and `README.md` are being rewritten in PR #42; the new
document should be added to their read path when #42 lands, to avoid a merge conflict
on those two files. MODULES and AUTHORITY_INDEX are updated here.

## Governance boundary

Documentation only.

It does not implement a database, schema, table, migration, connector, email intake,
contact synchronization, OCR, vector index, runtime or executable artifact. The real
database, row-level scope enforcement and connectors are adapters outside Pantheon that
conform to this model.

## Relation to existing doctrine

- `SCOPE_ISOLATION.md` owns scope vocabulary and isolation; this model applies it to records.
- `MEMORY.md` / `KNOWLEDGE_TAXONOMY.md`: a filed record is not memory or evidence by itself.
- `MODULAR_DOMAIN_REORIENTATION.md`: the core is the stable base; domain packs extend it.
- `DATA_PLATFORM_*` (candidate): implementation-side register families realize this model.
- `REVIEW_QUEUE.md` (candidate): surfaces attribution and merge decisions.

## Explicit non-implementation

No files were touched under:

```text
schemas/
tests/
operations/
platform/
Docker
.env
pyproject.toml
CLAUDE.md
```

## Boundary phrase

```text
The core records what every profession shares.
The scope keeps each dossier separate.
The domain pack adds the profession.
Nothing is filed, merged or reused without a governed decision.
```
