# 2026-08-30 — reconstruct Agent Skills evaluation pattern distillation

## Objective

Reconstruct #824 Slice B from exact current `main` `e0797b83e3b596dc7afe194241e7cbfa4343307e` without reusing stale branch history.

The semantic delta was previously prepared in abandoned commit `d6800ac565165bfab82496b2bd62ef977afa9ddc`. During reconstruction, `main` advanced through #841; that merge was revalidated and changes only the optional Obsidian/Second Brain boundary, not the two destination owners of this slice.

## Current-state checks

- #833 is merged and Slice A is complete: `SKILL_LIFECYCLE.md` was absorbed into existing Capability owners.
- #815/#816/#821/#831/#837 have settled the source, exact-retrieval and claim-support seams relevant to this work.
- #841 is merged on the reconstruction base and is orthogonal to this slice.
- `DISTILLATION_REGISTRY.md` and `REJECTED_PATTERNS.md` have not changed since the old Slice B semantic base, so the bounded delta remains applicable.
- #839 remains a separate open source-notebook PR and is not modified or pre-empted here.

## Retained deltas

The existing Distillation Registry receives only the demonstrated patterns that were still missing:

```text
failure-mode-first evaluation
baseline-versus-candidate paired evaluation
evaluator calibration against human labels
creator / evaluator / admission separation
research challenge search
decision-relevant research stop condition
private-query minimization
bounded handoff with current-state revalidation
working-plan persistence demotion
external second opinion as dissent signal
```

The existing Rejected Patterns owner receives only the corresponding missing refusals:

```text
multi-model consensus != proof or authorization
working plan / handoff != current governed state
```

## Deliberately not introduced

No new Skill lifecycle, evaluation platform, benchmark registry, judge authority, research authority, runtime, schema, persistence model, Role, Rite, Space, installer, updater or automatic optimizer is created.

The three research-method entries only route candidate constraints toward the existing `templates/hermes/skills/source-research/SKILL.md`; they do not implement Slice C.

## Preserved boundaries

```text
creator != evaluator != admission authority
skill eval success != admission
self-evaluation != self-admission
benchmark improvement != governance approval
second-model agreement != independent proof
multi-model consensus != authorization
handoff state != current truth
plan persistence != governed project state
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
```

## Next safe action

After this slice is reviewed and merged, revalidate/reconstruct #839 on then-current `main`. Only after that source-notebook seam settles should #824 Slice C test the three bounded `source-research` deltas: challenge search, decision-relevant stopping, and private-query minimization.
