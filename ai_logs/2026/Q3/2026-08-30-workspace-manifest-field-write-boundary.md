# Workspace manifest field/write boundary

Date: 2026-08-30

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Updated the existing Obsidian/Hindsight owner to separate deterministic
  technical manifest refresh from human or governed field changes.
- Updated the existing Workspace Manifest Inspector candidate with a read-only
  first slice, one propose-only `workspace-manifest` skill shape and a bounded
  multi-document Markdown discussion posture.
- Updated the existing architecture-agency organization owner with optional
  shallow Hermes and reconstructible autonomous working areas.
- Extended the existing workspace-organization regression test instead of
  creating a parallel contract or test owner.

## Why

The prior boundary correctly forbade silent second-brain manifest mutation but
did not distinguish a future deterministic refresh of exact technical
observations from changes to human comments, semantic fields or professional
status. The integration plan also needed to place multi-document Hermes working
discussions without replacing the exact-revision comment owner.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none; the first executable slice remains read-only.
Authority impact: none; existing document, currentness, discussion, Decision,
Evidence and approval owners remain unchanged.
Schema/test/CI impact: one existing regression test extended; no schema or CI
workflow added.
External action: none.
Memory behavior: optional Second Brain remains write-bounded to an explicitly
designated reconstructible area and gains no manifest authority.

## Local distinctions

```text
technical observation refresh != human or governed field mutation
workspace discussion != exact-revision professional comment
manifest discussion ref != Decision or approval
documented boundary != implemented writer
```
