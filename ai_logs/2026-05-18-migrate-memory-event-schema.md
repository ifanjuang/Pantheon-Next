# Migrate MEMORY_EVENT_SCHEMA

Date: 2026-05-18

## Scope

Phase C migration PR. Replaces the `docs/governance/MEMORY_EVENT_SCHEMA.md` stub with content migrated from the Pantheon-OS snapshot.

Files changed:

- `docs/governance/MEMORY_EVENT_SCHEMA.md` (stub → migrated);
- `ai_logs/migration-mapping.md` (row updated: `pending` → `migrated`).

## Snapshot reference

```text
Source archive : legacy/Pantheon-OS-main.zip
Captured in    : Pantheon-Next commit 9c2354b
Source file    : Pantheon-OS-main/docs/governance/MEMORY_EVENT_SCHEMA.md
Source length  : 236 lines
Migrated length: ~210 lines
```

## Doctrinal transformations applied

- Stub header replaced by `Status: migrated from Pantheon-OS snapshot at legacy/Pantheon-OS-main.zip (Pantheon-Next commit 9c2354b)`.
- Source line added under the Status header.
- Title kept short: `# Memory Event Schema`.
- Anti-runtime reminder reinforced at the top and as a final section.
- Event model preserved as documentation reference, not as a schema under `schemas/`.
- Event types preserved as an illustrative and non-exhaustive list.
- Relationship section added with cross-references to `MEMORY.md`, `SCOPE_ISOLATION.md`, `APPROVALS.md`, `EVIDENCE_PACK.md` and `KNOWLEDGE_TAXONOMY.md`.
- No off-canonical Pantheon Role introduced.
- No `HEPHAESTUS` spelling introduced.

## Doctrine boundary

This PR does not:

- introduce a runtime, scheduler, queue, message bus, provider router, workflow engine, plugin manager, skill installer, memory writer or automatic promotion mechanism;
- add or modify any file under `schemas/`, `tests/`, `operations/`, `platform/`, repository root, `pyproject.toml`, `.env*` or Docker;
- modify any existing Hermes profile.

The migrated document contains YAML examples in fenced code blocks. They are documentation references inside a Markdown file, not a schema definition under `schemas/`.

## Coordination

Lot 3 (Memory and knowledge).

`MEMORY.md` migration is still pending.

`EPISTEMIC_CONTROL.md` and `EPISTEMIC_CONTROL_PROPAGATION.md` remain stubs because their OS source introduces off-canonical Pantheon Roles and requires separate doctrinal arbitration.
