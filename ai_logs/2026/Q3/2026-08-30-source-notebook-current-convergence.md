# 2026-08-30 — converge optional workspace source notebook

## Objective

Reconstruct #839 on exact current `main` `be28801d074231fa62d848e6f03b208410663b69` after #841, #842 and #843, retaining only the source-notebook seam that is still missing.

## Current-state checks

- #841 already owns the optional Obsidian / second-brain behavior boundary.
- #842 is merged and owns the Agent Skills evaluation-pattern distillation for #824 Slice B.
- #843 is merged and keeps the Distillation Registry transitional; it changes that registry and the generated ai-log index, not the source-notebook owner or research skill.
- `SOURCE_NEED_AND_REGISTRY.md` remains the existing owner for source need, Source Leads, Source Registry and source-addition candidates.
- `templates/hermes/skills/source-research/SKILL.md` remains the single research-skill candidate.
- The previous #839 edit to `OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md` is redundant after #841 and is not retained.

## Retained delta

The existing source owner permits an optional human-maintained workspace source notebook as a discovery surface for Source Leads. The existing `source-research` candidate may consult it only inside authorized task/context scope.

```text
workspace source notebook != Source Registry
notebook entry != Source Registry Entry
listed route != inspected source
workspace path != governed identity
workspace access != task authorization
registered source != Evidence
```

A recurrent or consequential route can use the existing promotion path:

```text
notebook entry
-> Source Addition Candidate
-> required review and arbitration
-> Source Registry Entry when accepted
```

No synchronization, repeated use, retrieval result, runtime success or Cockpit projection performs that promotion automatically.

## Deliberate simplification

No second source owner, research skill, registry, retrieval service, Obsidian-specific path, synchronization mechanism, schema or authority surface is introduced.

The optional Obsidian profile is not modified because #841 already defines that replaceable runtime/reference boundary. Source-notebook semantics remain in the existing source owner.

## Audit cleanup

A late review after #842 identified that its new ai_log had not been included in the generated `ai_logs/INDEX.md`. #843 subsequently regenerated that index for its own intervention. The final reconstruction regenerates the index again from current main after adding this log, preserving the #842 and #843 entries and adding this one without a parallel repair path.

## Next safe action

Run focused tests and current governance CI on the exact final head, inspect reviews/threads, and merge #839 only after explicit authorization. #824 Slice C remains separate: challenge search, decision-relevant stopping and private-query minimization are not implemented here.
