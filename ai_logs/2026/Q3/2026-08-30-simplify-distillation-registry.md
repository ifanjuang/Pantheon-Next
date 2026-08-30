# Distillation Registry simplification — 2026-08-30

## Objective
Keep `DISTILLATION_REGISTRY.md` transitional rather than a permanent encyclopedia or parallel backlog.

## Exact base
`Pantheon-Next/main = 2ed123fed6843aba0acb092ff02c18b85f60f4e7`.

## Observed problem
The registry still contained a future-pattern-card backlog and three rows whose concrete owners are already known: bounded handoff/current-state revalidation, working-plan persistence demotion, and external second opinion as dissent signal.

## Change
The registry now states that absorbed patterns leave the registry. The three redundant rows and the future-pattern-card block are removed. Evaluation-method patterns and the three source-research constraints remain because their destination work is not yet settled. `REJECTED_PATTERNS.md` is unchanged.

## Governance effect
No runtime, schema, Capability, approval rule, Evidence rule, source authority, or professional decision authority is added or removed.

## Verification before merge
Regenerate `ai_logs/INDEX.md`; require Governance CI, Pantheon Architecture Audit, and Obsolete Authority Consistency on exact final HEAD; inspect review comments and threads; revalidate concurrent changes to the owner.
