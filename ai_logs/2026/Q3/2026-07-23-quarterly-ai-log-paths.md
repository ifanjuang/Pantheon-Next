# 2026-07-23 — Quarterly AI log paths

Status: validation-only intervention trace.
Boundary profile: validation_only_trace.

## Change

New AI intervention logs now use:

```text
ai_logs/<year>/Q<n>/YYYY-MM-DD-<slug>.md
```

The generated index now discovers both quarterly subdirectories and the historical flat corpus. A differential read-only check validates only newly added paths, including consistency between the filename date, year directory and calendar quarter.

## Historical corpus

The existing flat logs remain at their current paths. This change performs no mass move, rewrite, classification, digest or deletion. Existing references remain valid.

## Effects

- Pantheon governs trace placement and retention rules.
- CI checks newly added repository paths only.
- Hermes performs no logging migration or compaction.
- OpenWebUI has no role in repository trace placement.
- Any future removal from the working tree remains a reviewed human decision after reference verification.

## Boundary

```text
quarterly path != scheduler
index generation != trace approval
new-path validation != historical migration
working-tree removal != Git-history deletion
```

No runtime, professional data, approval, Evidence admission, Register entry or external action is introduced.
