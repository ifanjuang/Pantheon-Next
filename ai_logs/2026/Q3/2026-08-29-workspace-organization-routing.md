# Workspace organization routing — 2026-08-29

## Objective

Prevent workspace/vault proposals from treating the recommended IFJA folder profile as mandatory or overlooking the existing `Affaires`, `Connaissances`, manifestability and Cockpit projection owners.

## Convergence

`docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md` remains the architecture-domain owner. Its shallow project hierarchy and five-family Knowledge corpus are clarified as an optional recommended profile rather than a Pantheon prerequisite.

`CLAUDE.md` now routes workspace-organization changes through that owner together with the Workspace Manifest Inspector, Structured Agency Interface and qualified Obsidian/Hindsight reference profile. The existing Architecture Authority Index records the optional posture. Consumer documents point back to the owner without restating the full organization model.

## Preserved invariants

```text
recommended structure != mandatory structure
folder/path != governed identity
unclassified folder != invalid folder
Hermes classification proposal != filesystem mutation
Cockpit Space != required physical root folder
```

## Boundary

Documentation and regression-only convergence. No folder, source file, manifest, governed identity, Cockpit state, retrieval state, runtime, database, approval or external effect is created or changed.

## Verification rule

Merge only after the focused regression test and repository governance checks pass on the exact proposed head.
