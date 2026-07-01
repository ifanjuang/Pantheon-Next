# Open Branch Landing Plan

Status: validation-only / branch landing coordination — active.

Date: 2026-07-01

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
DEFER
DONE
```

## Current landing sequence

| PR / branch | Current state | Subject | Risk | Decision Zeus | Action | Condition before merge/close |
|---|---|---|---|---|---|---|
| #249 `claude/fix-runtime-phrase-landing-queue` | closed merged | Reworded affirmative landing-order wording that tripped the runtime-phrase guard. | CI red on runtime phrase guard; wording could suggest runtime queue if left unchanged | accepted | DONE | Merged as `641bd9237b1538fe238f6190f6b8c39203afa581`; no protected path modified. |
| #248 `claude/authority-index-mcp-alignment` | closed merged | Applied deferred `AUTHORITY_INDEX.md` rows for `mcp-server/` and `docs/assets/pantheon-control/`; removed temporary alignment note. | authority-index drift / MCP status ambiguity | accepted | DONE | Merged as `4790bf7a9e149e372954d53b04c46c459dfd7b97`; read-only artifact recognized without authority expansion. |
| #247 `chatgpt/consolidation-landing-plan` | closed unmerged | Added `CONSOLIDATION_LANDING_PLAN.md`, overlapping with `REPOSITORY_CONSOLIDATION_LANDING_PLAN.md` already landed on `main`. | duplicate planning docs / divergent names | accepted as direction, superseded in repo state | DONE / CLOSE_SUPERSEDED | Closed without merge after comparison; no unique extraction needed. |
| #246 `claude/repo-quality-analysis-9sqw56` | open ready, merge blocked | Claude global quality audit under `docs/audits/`. | useful audit but must remain validation-only; some points already superseded by landing work | accepted as validation-only audit source | WAIT_FOR_CLAUDE / REBASE | Needs rebase/update before merge if retained. |
| #245 `chatgpt/architecture-method-run-tests-tiers-main` | open ready, with Claude | Compact architecture-domain Method Card run tests; supersedes #238. | useful examples, but stale branch and `AUTHORITY_INDEX.md` conflict risk after #248 | accepted on substance | WAIT_FOR_CLAUDE / REBASE | Claude is updating; preserve #248 authority rows; merge only if compact and non-conflicting. |
| #240 `chatgpt/method-hermes-handoff-template` | closed unmerged | Candidate Method Card -> Hermes handoff template. | duplicated `CAPABILITY_PLACEMENT.md` governed handoff doctrine; too large | accepted as direction, superseded | DONE / CLOSE_SUPERSEDED | Replaced by `METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md`; closed without merge. |
| #239 `claude/update-unknown-fix` | closed merged | Non-numeric update version fix. | protected path; already reviewed and merged | accepted | DONE | Merged as `af1f8d8df31b3268f38a53ac12263924771a733f`; status spine updated. |
| #238 `chatgpt/architecture-method-run-tests` | closed unmerged draft | Original architecture method run tests. | superseded by #245 | accepted | CLOSE_SUPERSEDED | Already closed; keep historical only. |
| #241 `chatgpt/architecture-method-deck-pruning` | closed unmerged | Architecture method deck visibility tiers. | superseded by #244 | accepted | CLOSE_SUPERSEDED | Already closed; keep historical only. |
| #244 `chatgpt/architecture-method-deck-tiers-main` | closed merged | Replacement for #241; visibility tiers. | landed | accepted | DONE | Merged. |
| #233 `chatgpt/method-card-model` | closed unmerged | Original Method Card model and architecture deck. | superseded by #237 | accepted | CLOSE_SUPERSEDED | Already closed; keep historical only. |
| #237 `chatgpt/reconcile-method-cards-html` | closed merged | Reconciled Method Cards and deck prototype. | landed | accepted | DONE | Merged. |
| #234 `docs/dcode-agent-kit-placement` | closed merged | dcode-agent-kit as external reference for Hermes-side scaffolding. | external reference could contaminate core Card Stack if promoted too early | accepted as external reference only | DONE | Merged as `e9ef05c179e2404d28bb379e3d27bbafca057d31`; no Card Stack or Skill Lifecycle change. |
| #228 `feat/update-verification` | closed unmerged | Same non-numeric update-version fix as #239. | duplicate protected-path landing | accepted as content, superseded by #239 | DONE / CLOSE_SUPERSEDED | Closed without merge. Same head SHA as #239 before merge. |
| #218 `claude/governed-composition-land` | open ready, mergeable | Governed composition examples and schema fields. | touches `schemas/`; cannot land in docs-only cleanup | accepted as direction | PROTECTED_REVIEW | Requires explicit protected-path schema/test review before merge. |
| #217 `chatgpt/operational-brain-distillation-20260625` | closed merged | Operational context corpus in memory/knowledge doctrine. | risk of external Brain being read as Pantheon memory engine | accepted as candidate/support memory doctrine | DONE | Merged as `149bed9e0ada144d6e453520ced7b73dff4534a4`; documented non-implemented. |
| #190 `docs/first-principles-crawl4ai-qualification` | open draft, merge blocked | First-principles skill candidate, Crawl4AI adapter review, new capability effect rite. | broad candidate bundle; capability sprawl during consolidation | accepted as direction, not for current landing | KEEP_DRAFT / DEFER | Split later into smaller PRs after Capability Placement / Skill Lifecycle consolidation. |
| #189 `chatgpt/crawl4ai-hermes-skill` | open draft, merge blocked | Crawl4AI Hermes web extraction skill candidate. | overlaps with #190; may imply too-ready skill template | accepted as direction, not for current landing | KEEP_DRAFT / DEFER | Reconcile with #190 later; likely rewrite as adapter/reference review before any landing. |

## Recommended order

```text
1. Let Claude finish #245, then review/merge if compact and non-conflicting.
2. Keep #246 waiting for Claude/rebase if the audit is to be merged.
3. Treat #218 only through protected schema/test review.
4. Defer #190/#189 until Capability Placement / Skill Lifecycle consolidation.
5. Inventory branches without open PR.
```

## PR #249 decision note

#249 corrected CI-blocking affirmative runtime phrase use.

Decision:

```text
Accepted.
Merged.
Documentation wording fix only.
```

Boundary:

```text
No runtime.
No protected path.
No weakening of the runtime-phrase guard.
```

## PR #248 decision note

#248 completed the deferred authority-index alignment for MCP and Pantheon Control.

Decision:

```text
Accepted.
Merged.
```

Status impact:

```text
mcp-server/ = implementation artifact / read-only verification surface.
docs/assets/pantheon-control/ = implementation artifact / static prototype.
```

Boundary:

```text
Implementation artifact != authority.
Read-only verification != approval.
Static prototype != live cockpit.
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

Current state after #248 / #249:

```text
Accepted on substance.
Claude is updating / rebasing.
Do not overwrite or regress #248 authority-index rows.
```

## PR #218 protected review note

#218 touches `schemas/` and therefore cannot be merged under docs-only landing rules.

Protected paths:

```text
schemas/README.md
schemas/examples/workflow_manifest.example.yaml
schemas/workflow_manifest.schema.yaml
```

Before merge, verify:

```text
schema additions against WORKFLOW_SCHEMA.md and CAPABILITY_REGISTRY.md;
examples validate against schema;
no runtime implication is introduced by schema vocabulary;
governed_composition remains validation metadata only;
status-spine / WHAT_RUNS posture remains coherent.
```

## PR #217 decision note

#217 has landed as candidate/support memory doctrine.

Decision:

```text
Accepted.
Merged.
Documented non-implemented.
```

Boundary:

```text
Operational context corpus retrieves.
Runtime memory recalls.
Sources support.
Candidates propose.
Pantheon qualifies status.
Registre Probatoire alone carries governed reliance.
Human validates.
```

## PR #234 decision note

#234 has landed as an external reference review.

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
Accepted as external reference only.
Merged.
No Card Stack or Skill Lifecycle change during this landing sequence.
```

## PR #190 / #189 deferred capability references

#190 and #189 remain useful but deferred.

Accepted direction:

```text
first-principles review may be a Hermes-side analytical skill candidate;
Crawl4AI may be a Hermes-side web/document extraction adapter candidate;
new capability effect review is a valid governance question.
```

Refused boundary:

```text
no Pantheon runtime;
no crawler service;
no Docker/API service;
no plugin manager;
no automatic ingestion;
no approval engine;
no memory engine;
no automatic rule mutation.
```

Future handling:

```text
reconcile #189 with #190;
split #190 if retained;
review after Capability Placement / Skill Lifecycle consolidation.
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
