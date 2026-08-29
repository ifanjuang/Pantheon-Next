# 2026-08-29 — distill Agent Skills evaluation and continuity patterns

## Objective

Continue #824 Slice B from exact base `29f395a1cc9066c8436212f2f7d2bcf296b5724a` after the Skill lifecycle owner was absorbed into existing Capability owners.

The external review corpus includes Anthropic `skill-creator`, `ai-evals-course/evals-skills`, Scoville Research/Plan/Handoff and related second-opinion tooling, plus the broader Agent Skills review already recorded in #824.

This slice records only demonstrated governance/method deltas not already owned. It does not create an Agent Skills stack document, install a Skill, choose a runtime binding or modify an evaluation schema.

## Existing patterns not duplicated

`REJECTED_PATTERNS.md` already covers, among others:

```text
automatic skill installer
skill auto-updater
eval pass as approval
eval pass as automatic optimization
LLM judge as final authority
automatic external action
self-evolution / self-improving authority
direct skill manager adoption
popularity-based approval
```

`DISTILLATION_REGISTRY.md` already covers evaluation scores as signals, trajectory evaluation, Improvement Candidates, unanswerable-question testing, source freshness and least-capability review.

Those rules were not restated as new entries.

## New positive distillations retained

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

These patterns route only to existing owners such as `PRE_EXECUTION_SIMULATION.md`, `EVIDENCE_PACK.md`, `CAPABILITY_REGISTRY.md`, `EXTERNAL_TOOLS_POLICY.md`, `WORKFLOW_FORGING_PROTOCOL.md`, `WORK_ISSUE_AND_DELEGATED_MERGE_MODEL.md`, `CONTEXT_PACKS.md` and the existing Hermes `source-research` candidate template.

## New explicit rejections retained

```text
multi-model consensus != proof or authorization
working plan / handoff != current governed state
```

The safe alternatives are source-grounded verification, visible dissent, Work Issue/Context Pack continuity and re-reading current authoritative state before resume.

## Deliberately not imported

No:

- marketplace or installer;
- auto-update or sync mechanism;
- generic eval platform;
- benchmark leaderboard;
- judge authority;
- second planning persistence model;
- second memory system;
- autonomous optimizer;
- second Research owner;
- new Role, Rite or governed Space.

## Next slice

#824 Slice C may test only the three research deltas already routed to the existing `templates/hermes/skills/source-research/SKILL.md`:

1. challenge search;
2. decision-relevant stopping condition;
3. private-query minimization.

Before that slice, revalidate #830 and the #815/#816/#821/#831 source/retrieval work so the Skill does not duplicate source, currentness, retrieval or Evidence authority.

## Preserved invariants

```text
creator != evaluator != admission authority
skill eval success != admission
self-evaluation != self-admission
benchmark improvement != governance approval
handoff state != current truth
plan persistence != governed project state
second-model agreement != independent proof
multi-model consensus != authorization
retrieved != truth
memory != Evidence
runtime success != authorization
```
