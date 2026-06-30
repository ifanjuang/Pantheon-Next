# Open Branch Landing Plan

Status: validation-only / branch landing coordination — active.

Date: 2026-06-30

This document coordinates the landing, rewrite, closure or extraction of open PRs and unmerged branches during the Pantheon Next consolidation phase.

It does not create doctrine, approve a merge, modify protected paths, execute Hermes, create runtime behavior, create a scheduler, create a queue, approve external actions or promote memory.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Next currently has several open or superseded branches produced by parallel human, ChatGPT and Claude work.

The goal is not to merge everything.

The goal is to land only what reduces ambiguity, preserves doctrine boundaries and clarifies status.

Working rule:

```text
A mergeable PR is not necessarily admissible.
A useful branch may still be superseded, overbroad, protected, contradictory or outside Pantheon.
A branch that adds possibility but blurs status should not land.
A branch that reduces ambiguity may land.
```

## Landing decisions

Use the following decisions:

```text
MERGE
REBASE
REWRITE
SPLIT
EXTRACT_PARTIAL
CLOSE_SUPERSEDED
CLOSE_REFUSED
PROTECTED_REVIEW
KEEP_DRAFT
WAIT_FOR_CLAUDE
DONE
```

## Current queue

| PR / branch | Current state | Subject | Risk | Decision Zeus | Action | Condition before merge/close |
|---|---|---|---|---|---|---|
| #247 `chatgpt/consolidation-landing-plan` | closed unmerged | Added `CONSOLIDATION_LANDING_PLAN.md`, overlapping with `REPOSITORY_CONSOLIDATION_LANDING_PLAN.md` already landed on `main`. | duplicate planning docs / divergent names | accepted as direction, superseded in repo state | DONE / CLOSE_SUPERSEDED | Closed without merge after comparison; no unique extraction needed. |
| #246 `claude/repo-quality-analysis-9sqw56` | open ready, merge blocked | Claude global quality audit under `docs/audits/`. | useful audit but must remain validation-only; some points already superseded by landing work | accepted as validation-only audit source | WAIT_FOR_CLAUDE / REBASE | Needs rebase/update before merge if retained. |
| #245 `chatgpt/architecture-method-run-tests-tiers-main` | open ready | Compact architecture-domain Method Card run tests; supersedes #238. | adds examples after method-card stack; must remain compact | to validate | REVIEW then MERGE if still compact | Review against `METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md`. Confirm no hidden runtime or cockpit overload. |
| #240 `chatgpt/method-hermes-handoff-template` | closed unmerged | Candidate Method Card -> Hermes handoff template. | duplicated `CAPABILITY_PLACEMENT.md` governed handoff doctrine; too large | accepted as direction, superseded | DONE / CLOSE_SUPERSEDED | Replaced by `METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md`; closed without merge. |
| #239 `claude/update-unknown-fix` | closed merged | Non-numeric update version fix. | protected path; already reviewed and merged | accepted | DONE | Merged as `af1f8d8df31b3268f38a53ac12263924771a733f`; status spine updated. |
| #238 `chatgpt/architecture-method-run-tests` | closed unmerged draft | Original architecture method run tests. | superseded by #245 | accepted | CLOSE_SUPERSEDED | Already closed; keep historical only. |
| #241 `chatgpt/architecture-method-deck-pruning` | closed unmerged | Architecture method deck visibility tiers. | superseded by #244 | accepted | CLOSE_SUPERSEDED | Already closed; keep historical only. |
| #244 `chatgpt/architecture-method-deck-tiers-main` | closed merged | Replacement for #241; visibility tiers. | landed | accepted | DONE | Merged. |
| #233 `chatgpt/method-card-model` | closed unmerged | Original Method Card model and architecture deck. | superseded by #237 | accepted | CLOSE_SUPERSEDED | Already closed; keep historical only. |
| #237 `chatgpt/reconcile-method-cards-html` | closed merged | Reconciled Method Cards and deck prototype. | landed | accepted | DONE | Merged. |
| #234 `docs/dcode-agent-kit-placement` | open draft | dcode-agent-kit as external reference for Hermes-side scaffolding. | external reference could contaminate core Card Stack if promoted too early | to verify | KEEP_DRAFT | Keep as external reference only; do not alter Card Stack or Skill Lifecycle until consolidation stabilizes. |

## Recommended order

```text
1. Finish Claude AUTHORITY_INDEX.md alignment.
2. Keep #246 waiting for Claude/rebase if the audit is to be merged.
3. Review #245 against the new Method Card Hermes specialization.
4. Keep #234 as external reference candidate until Skill Lifecycle / Capability Placement consolidation is ready.
5. Inventory branches without open PR.
```

## PR #247 decision note

#247 was superseded because `docs/governance/REPOSITORY_CONSOLIDATION_LANDING_PLAN.md` already landed on `main` with a more explicit status and current follow-up documents.

Decision:

```text
Accepted as direction.
Closed without merge.
No unique content extraction required.
```

## PR #246 decision note

Claude's audit should be treated as:

```text
validation-only / audit source
```

It may be merged if:

- it is clearly marked non-canonical;
- it does not modify protected paths;
- it does not silently promote recommendations;
- it does not contradict current `WHAT_RUNS.md`, `STATUS.md`, `MODULES.md` and the active status-spine reconciliation.

Current state:

```text
Accepted in principle.
Ready for review.
Merge currently blocked / needs rebase or branch update.
```

## PR #240 decision note

#240 was useful in direction but too broad as a landing artifact.

It has been replaced by:

```text
docs/governance/METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md
```

The replacement keeps only:

- what Method Cards add to a Hermes handoff;
- compact examples;
- bad handoff examples;
- review checklist;
- Method Card-specific stop conditions.

It avoids restating:

- generic Effect Classes;
- generic Capability Gap doctrine;
- generic Evidence Pack doctrine;
- approval levels;
- idempotence discipline;
- canonical governed execution handoff.

Decision:

```text
Accepted as direction.
Original PR closed without merge.
Replacement is candidate support doctrine / documented non-implemented / to verify.
```

## PR #245 review target

#245 is useful only if it remains compact.

Acceptable shape:

```text
case -> primary method -> guardrail -> verification -> specialist only if triggered -> gate
```

Do not let it become a visible method-chain encyclopedia.

Review it against:

```text
docs/governance/METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md
```

Decision:

```text
To validate next.
```

## PR #234 review target

#234 may remain as an external reference.

Acceptable:

```text
dcode-agent-kit as reference for Hermes-side scaffolding patterns.
```

Refused:

```text
Pantheon runtime;
Pantheon skill installer;
source of truth;
approval engine;
memory engine;
automatic capability admission;
dependency to install.
```

Decision:

```text
Keep draft until Skill Lifecycle / Capability Placement consolidation is ready.
```

## Branches without PR

Still required:

```bash
git fetch --all --prune
git branch -r --no-merged origin/main
```

For each branch:

```bash
git log --oneline origin/main..origin/BRANCH
git diff --stat origin/main...origin/BRANCH
git diff --name-status origin/main...origin/BRANCH
```

Classification:

```text
Docs-only and reduces ambiguity -> PR / review.
Duplicate or superseded -> close/delete after confirmation.
Protected path -> protected review.
Too broad -> split.
Outside Pantheon -> external reference or refuse.
```

## Boundary

This plan is operational coordination only.

```text
It does not merge anything.
It does not close anything.
It does not approve anything.
It does not promote doctrine.
It does not modify protected paths.
```

The validated remains.
The rest is merged, rewritten, extracted, refused or closed.
