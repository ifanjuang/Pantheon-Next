# 2026-08-30 — prune absorbed research distillations

## Objective

Apply the transitional Distillation Registry rule after #844 merged #824 Slice C.

## Observed state

- `main` at branch creation: `b7eae049504588bb1bdd052ae597bdabfe26ee91`.
- #844 merged private-query minimization, challenge search and decision-relevant stopping into the single existing `source-research` candidate.
- `DISTILLATION_REGISTRY.md` explicitly requires adopted patterns to leave the registry when no distinct cross-cutting review purpose remains.

## Change

Remove only these now-absorbed rows:

- Research challenge search;
- Decision-relevant research stop condition;
- Private-query minimization.

Keep the evaluation-method rows because #824 D/E has not yet run.

## Boundary

```text
pattern absorbed by owner -> remove duplicate registry entry
Git/issue/ai_log provenance != current authority
Slice C complete != evaluation pilot complete
```

No runtime, schema, Capability, Evidence, authorization or professional-decision behavior changes.
