# Dependent repositories — doctrine evolution proposal

Date: 2026-07-23

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added: `docs/governance/DEPENDENT_REPOS_DOCTRINE_EVOLUTION.md`, a candidate proposal
  arising from a deep analysis of the `Pantheon-Next` ↔ `pantheon-mvp` coupling
  (issue #448; first corrections in `pantheon-mvp#48`).
- Proposed five doctrine additions: (1) name the external vendoring consumption
  relationship; (2) reconcile the exposure-surface map with the running MVP cockpit;
  (3) make the `BOUNDARY_STANDARD.md` boundary verifiable via a read-only check;
  (4) structure `ai_logs` (partition + decisional/operational classification +
  compaction) instead of deleting; (5) elevate drift-monitoring of consumed artifacts
  to a first-class rule.
- Updated: none (proposal only; `CLAUDE.md` untouched).
- Removed: none.

## Why

The doctrine names its internal zones but is silent on the external dependent that now
consumes the governance core, and describes an exposure topology (dashboard "voluntarily
absent") that no longer matches reality. A vendored copy had drifted onto a retired
decision word with nothing watching that drift class. The proposal closes the gap in
doctrine text without changing any canonical rule.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none.
Authority impact: none — candidate proposal added; `CLAUDE.md` remains authoritative and unedited.
Schema/test/CI impact: none.
External action: none.
Memory behavior: none.

## Local distinctions

```text
proposal != canonical text
declared boundary != verified boundary
provenance compaction != provenance deletion
vendored copy != upstream authority
described doctrine != exercised doctrine
```
