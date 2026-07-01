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

Pantheon Next has had several open or superseded branches produced by parallel human, ChatGPT, Claude, Codex and other assistant work.

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
WAIT_FOR_CODEX
DEFER
DONE
```

## Current landing sequence

| PR / branch | Current state | Subject | Decision Zeus | Action | Condition / note |
|---|---|---|---|---|---|
| #249 `claude/fix-runtime-phrase-landing-queue` | closed merged | Reworded affirmative landing-order wording that tripped the runtime-phrase guard. | accepted | DONE | Merged as `641bd9237b1538fe238f6190f6b8c39203afa581`; no protected path modified. |
| #248 `claude/authority-index-mcp-alignment` | closed merged | Applied deferred `AUTHORITY_INDEX.md` rows for `mcp-server/` and `docs/assets/pantheon-control/`; removed temporary alignment note. | accepted | DONE | Merged as `4790bf7a9e149e372954d53b04c46c459dfd7b97`; read-only artifact recognized without authority expansion. |
| #247 `chatgpt/consolidation-landing-plan` | closed unmerged | Duplicate consolidation landing plan. | accepted as direction, superseded in repo state | DONE / CLOSE_SUPERSEDED | Closed without merge; no unique content extraction required. |
| #246 `claude/repo-quality-analysis-9sqw56` | closed merged | Claude global quality audit under `docs/audits/`. | accepted as validation-only audit source | DONE | Merged as `7e7f4bcd9c94a4c57ca8d7993fd3390ce1512491`; audit is dated, non-canonical and not current status doctrine. |
| #245 `chatgpt/architecture-method-run-tests-tiers-main` | closed merged | Compact architecture-domain Method Card run tests; supersedes #238. | accepted on substance | DONE | Merged as `6358efa80d4acb21d88a259ce2193ecb03850de2`; candidate support examples / documented non-implemented. |
| #240 `chatgpt/method-hermes-handoff-template` | closed unmerged | Candidate Method Card -> Hermes handoff template. | accepted as direction, superseded | DONE / CLOSE_SUPERSEDED | Replaced by `METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md`; closed without merge. |
| #239 `claude/update-unknown-fix` | closed merged | Non-numeric update version fix. | accepted | DONE | Merged as `af1f8d8df31b3268f38a53ac12263924771a733f`; status spine updated. |
| #238 `chatgpt/architecture-method-run-tests` | closed unmerged draft | Original architecture method run tests. | accepted, superseded | DONE / CLOSE_SUPERSEDED | Superseded by #245. |
| #241 `chatgpt/architecture-method-deck-pruning` | closed unmerged | Architecture method deck visibility tiers. | accepted, superseded | DONE / CLOSE_SUPERSEDED | Superseded by #244. |
| #244 `chatgpt/architecture-method-deck-tiers-main` | closed merged | Replacement for #241; visibility tiers. | accepted | DONE | Merged. |
| #233 `chatgpt/method-card-model` | closed unmerged | Original Method Card model and architecture deck. | accepted, superseded | DONE / CLOSE_SUPERSEDED | Superseded by #237. |
| #237 `chatgpt/reconcile-method-cards-html` | closed merged | Reconciled Method Cards and deck prototype. | accepted | DONE | Merged. |
| #234 `docs/dcode-agent-kit-placement` | closed merged | dcode-agent-kit as external reference for Hermes-side scaffolding. | accepted as external reference only | DONE | Merged as `e9ef05c179e2404d28bb379e3d27bbafca057d31`; no Card Stack or Skill Lifecycle change. |
| #228 `feat/update-verification` | closed unmerged | Same non-numeric update-version fix as #239. | accepted as content, superseded by #239 | DONE / CLOSE_SUPERSEDED | Closed without merge. Same head SHA as #239 before merge. |
| #218 `claude/governed-composition-land` | open ready / Codex updating | Governed composition examples and schema fields. | accepted as direction, protected review required | WAIT_FOR_CODEX / PROTECTED_REVIEW | Codex is rebasing and applying protected-review fixes: complete step signatures, V/E required when evidence gate required, negative schema tests. Merge only after final re-review. |
| #217 `chatgpt/operational-brain-distillation-20260625` | closed merged | Operational context corpus in memory/knowledge doctrine. | accepted as candidate/support memory doctrine | DONE | Merged as `149bed9e0ada144d6e453520ced7b73dff4534a4`; documented non-implemented. |
| #190 `docs/first-principles-crawl4ai-qualification` | open draft, merge blocked | First-principles skill candidate, Crawl4AI adapter review, new capability effect rite. | accepted as direction, not for current landing | KEEP_DRAFT / DEFER | Split later after Capability Placement / Skill Lifecycle consolidation. |
| #189 `chatgpt/crawl4ai-hermes-skill` | open draft, merge blocked | Crawl4AI Hermes web extraction skill candidate. | accepted as direction, not for current landing | KEEP_DRAFT / DEFER | Reconcile with #190 later; likely rewrite as adapter/reference review before any landing. |

## Recommended order

```text
1. Let Codex finish #218, then perform final protected schema/test review.
2. Defer #190/#189 until Capability Placement / Skill Lifecycle consolidation.
3. Inventory branches without open PR.
4. Use #246 as dated audit input only; do not treat it as current authority map.
```

## PR #246 decision note

#246 has landed as a dated global quality audit.

It should be treated as:

```text
validation-only / audit source
```

It is useful for:

- spotting doctrine/code/status drift;
- recording B-1 to B-8 arbitration candidates;
- documenting the specification-heavy / implementation-light risk;
- preserving a dated critique from Claude's review pass.

It must not be treated as:

- current repository status;
- canonical doctrine;
- an authority index;
- implementation evidence;
- approval;
- memory promotion;
- external-action authorization.

Decision:

```text
Accepted.
Merged.
Dated audit source only.
```

## PR #218 protected review note

#218 touches `schemas/` and therefore requires protected review.

Protected paths:

```text
schemas/README.md
schemas/examples/workflow_manifest.example.yaml
schemas/workflow_manifest.schema.yaml
```

Direction accepted:

```text
governed_composition as optional validation metadata on Workflow Manifest;
CERFA and marché public examples as documented non-implemented examples;
no forge engine;
no dispatch;
no scheduling;
no memory promotion;
composition_dispatch: false;
forge_execution: false.
```

Blocking requirements before merge:

```text
capability_steps[] must require a complete governance signature;
post_execution_evidence.required == true must require answer_verification and probative_certainty;
negative schema tests must prove under-specified steps and incomplete required evidence gates fail validation;
no runtime implication must be introduced by schema vocabulary.
```

Current state:

```text
Codex is rebasing and applying the protected-review fixes.
Do not merge until re-review confirms schema/test alignment.
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
