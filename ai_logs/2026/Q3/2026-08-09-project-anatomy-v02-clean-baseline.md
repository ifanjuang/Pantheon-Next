# Project Anatomy V0.2 clean baseline

Date: 2026-08-09

Status: validation-only trace — implemented candidate cleanup.
Boundary profile: validation_only_trace.

## Change

- Added: the explicit V0.2-only first-installation baseline decision and absence tests.
- Updated: the active Project Anatomy schemas, examples, MCP validation surface,
  authority references and Information relation inventory to one canonical V0.2 model.
- Removed: the sandbox-only V0.1 contracts, compatibility registry and adapter, duplicate
  historical model documents, examples and templates from the active repository tree.

## Why

V0.1 was never deployed or used for persisted production data. Keeping a reader,
writer, migration and duplicate carriers would create permanent compatibility debt in a
new installation. Git history remains the truthful record of the discarded sandbox
design.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: yes — schemas, governance references, MCP validation and tests.
Runtime impact: the read-only MCP APU surface validates only the V0.2 baseline.
Authority impact: no automatic authority; V0.2 remains candidate-bearing and human
review remains required for consequential claims and identity alignment.
Schema/test/CI impact: one active APU contract set, direct clean-install assertions and
referential-integrity checks.
External action: GitHub issues #607 and #608 are aligned separately with this baseline.
Memory behavior: none.

## Local distinctions

```text
sandbox history != active compatibility requirement
valid V0.2 claim != professionally accepted truth
candidate identity relation != identity validated
projection != authority
```
