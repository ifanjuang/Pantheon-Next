# Optional Obsidian second-brain boundary — 2026-08-29

## Objective

Record Obsidian second-brain behavior as an optional Hermes workspace capability without creating a parallel workspace, manifest, memory or governance owner.

## Convergence

`docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md` now distinguishes the Hermes Obsidian operation surface from optional second-brain knowledge-maintenance behavior. It keeps both subordinate to existing Pantheon workspace, manifest, identity, Evidence and approval owners.

`docs/architecture/WORKSPACE_MANIFEST_INSPECTOR_CANDIDATE.md` permits optional skills to discover, read, lint and propose corrections for manifests while refusing silent manifest semantics, status mutation or file moves. Repository routing and regression coverage prevent the optional posture from being forgotten.

## Preserved invariants

```text
workspace works without Obsidian skill or second-brain package
second-brain behavior != manifest authority
second-brain memory != Evidence
missing manifest != error by default
skill proposal != consequential write authorization
existing folder organization remains usable
```

## Boundary

Documentation and regression-only convergence. The external `eugeniughelbur/obsidian-second-brain` package is compatibility-observed, not installed, adopted, activated or qualified. No vault, manifest, file, memory, runtime, database, Cockpit state or external effect is created or changed.

## Verification rule

Merge only after the focused regression test and repository governance checks pass on the exact proposed head.
