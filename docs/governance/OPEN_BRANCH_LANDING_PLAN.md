# Open Branch Landing Plan

Status: validation-only / branch landing coordination — active.

Date: 2026-07-03

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

## Current landing roadmap — 2026-07-03

The current strategy is **A -> B -> C**:

```text
A. Land the repository cleanly.
B. Then improve the visible UX prototype.
C. Then prove the external OpenWebUI -> Hermes loop outside this repo.
```

This order is deliberate. Pantheon Next should not add more candidate doctrine while older drafts, external-reference PRs and runtime-honesty issues are still open.

### Step 1 — Post-Claude cleanup

Action:

```text
REWRITE / MERGE SMALL
```

Scope:

- replace brittle OpenWebUI event-count language such as `28+ events` with `current event catalog, verify at implementation time`;
- mark `GET /health` in the Hermes OpenAI-compatible connection template as `to verify` until confirmed against the actual Hermes runtime;
- record that PR #250 touched `pyproject.toml` and `mcp-server/pyproject.toml` despite a PR description saying no protected-path change;
- do not touch schemas, tests, Docker, operations, platform, `.env` or runtime code in this cleanup unless a separate protected review is opened.

Decision Zeus:

```text
Accepted.
```

Repo state:

```text
documented non-implemented / cleanup only
```

### Step 2 — Reduce old draft noise (#189 / #190)

| PR | Current state | Subject | Decision Zeus | Action | Condition / note |
|---|---|---|---|---|---|
| #189 `chatgpt/crawl4ai-hermes-skill` | open draft, merge blocked | Crawl4AI Hermes web extraction skill candidate. | accepted as direction, superseded or partially redundant | CLOSE_SUPERSEDED or EXTRACT_PARTIAL | Likely close if #190 or a shorter future adapter review covers the useful part. Do not merge as-is. |
| #190 branch `first-principles-crawl4ai-qualification` | open draft, merge blocked | First-principles skill candidate, Crawl4AI adapter review, new capability effect rite. | accepted as direction, overbroad for current landing | SPLIT or EXTRACT_PARTIAL | Extract only if `NEW_CAPABILITY_EFFECT_REVIEW.md` still adds a missing governance rite not already covered by `CAPABILITY_PLACEMENT.md` / `SKILL_LIFECYCLE.md`. Otherwise close. |

Boundary:

```text
no Pantheon runtime
no crawler service
no Docker/API service
no plugin manager
no automatic ingestion
no approval engine
no memory engine
no automatic rule mutation
```

### Step 3 — Qualify external-reference PRs (#265 / #260)

| PR | Current state | Subject | Decision Zeus | Action | Condition / note |
|---|---|---|---|---|---|
| #265 `forever-ai-components` review | open draft | Card UX affordance inspiration. | accepted as external reference candidate | REVIEW THEN MERGE or CLOSE | Land only as `external reference / candidate`; no dependency, renderer, component import, runtime or doctrine source. |
| #260 `Pythia` review | open draft | Candidate `governance_state_view` inspiration. | accepted as external reference candidate | REVIEW THEN MERGE or FOLD INTO EXISTING DOC | Avoid standalone API sprawl. Prefer reference review or folding into `CARD_STACK_MODEL.md` / cockpit status work later. |

Boundary:

```text
External references may inspire.
They do not govern Pantheon.
```

### Step 4 — Review #269 runtime-health prototype

| PR | Current state | Subject | Decision Zeus | Action | Condition / note |
|---|---|---|---|---|---|
| #269 `runtime-health prototype` | open draft | Static Pantheon Control `Santé / Runtime` UX page. | accepted as UX direction, to verify before merge | REVIEW THEN MERGE if strictly static | Merge only if there are no real network calls, no service control, no backend dependency, no scheduler, no observability backend, no approval engine and no memory effect. |

Allowed framing:

```text
Pantheon Control may display runtime-health candidates.
```

Forbidden framing:

```text
Pantheon monitors services live.
Pantheon controls services.
Pantheon replaces Portainer, Grafana, Langfuse or Hermes dashboards.
Pantheon decides health truth automatically.
```

### Step 5 — Keep #264 as maintainer / external-infra block

Issue #264 remains outside ordinary documentation landing.

Open items:

```text
tag v0.1.59
tag v0.1.60
base_metier PDF licence decision
optional git-history purge for old PDFs
real OpenWebUI -> Hermes run on external infrastructure
```

Decision Zeus:

```text
À arbitrer / maintainer-only.
```

Repo state:

```text
not implemented in Pantheon Next
```

### Step 6 — External proof loop after cleanup

After steps 1-5, the next proof should not be another doctrine document.

Target external scenario:

```text
OpenWebUI
-> sends a bounded Task Contract
-> Hermes executes a candidate skill
-> Hermes returns Result Candidate + Evidence Pack Candidate
-> Pantheon verifies status / gates
-> OpenWebUI displays the decision expected
-> human accepts, refuses or requests revision
```

This proves the separation:

```text
surface exposes
runtime executes
Pantheon governs
human decides
```

The live run belongs outside this repository. The repository may record only the governed contract, templates, expected evidence and result status.

## Historical landing sequence

| PR / branch | Current state | Subject | Decision Zeus | Action | Condition / note |
|---|---|---|---|---|---|
| #268 `claude/openwebui-primitive-map` | closed merged | OpenWebUI primitive mapping for templates. | accepted | DONE | Merged as `752af412e030b40656937aa7d1875160f2d81648`; documentation clarification only. |
| #267 `claude/align-openwebui-hermes-upstream` | closed merged | OpenWebUI/Hermes upstream alignment, SKILL.md templates and connection reference. | accepted with to-verify notes | DONE | Merged as `ac5166c3478ef7aa388ff7c58fc9850acbeec8eb`; event names corrected, health endpoint still to verify. |
| #266 `chatgpt/tripartite-mcp-refusal-docs` | closed merged | Tripartite interface spec, minimal MCP posture and refusal fixtures. | accepted after index fix | DONE | Merged as `c08002ea16e30f0ff73e8919ec239b3b39f1641d`; indexed in `AUTHORITY_INDEX.md` as candidate support doctrine / documented non-implemented. |
| #263 `claude/vertical-slice-phase2-bridge` | closed merged | Candidate Hermes/OpenWebUI wiring for vertical slice phase 2. | accepted as bridge only | DONE | Merged as `8cf145f2757d03c9e31586278d4232c45c4e3c26`; no live run. |
| #259 `claude/vertical-slice-devis-reprise` | closed merged | Governed vertical slice architecture_devis_reprise phase 1. | accepted | DONE | Merged as `29ba1e9d96ee3948592c2f2fd90f6c8c237cc9f8`; proves governance spine, not runtime. |
| #258 `claude/domain-pack-architecture-move` | closed merged | Architecture domain pack moved to `docs/domain-packs/architecture`. | accepted | DONE | Merged as `c9a45d9aa64ee6cd3b52b493aef08ea93ef478e4`; reference-complete move. |
| #256 `claude/referent-rule` | closed merged | Candidate promotion requires referent. | accepted | DONE | Merged as `f9ef0e70ec6166d08e616c70c1ecfdea22a1a91c`; anti-sprawl rule. |
| #255 `claude/base-metier-deversion-pdfs` | closed merged | PDF de-versioning and manifest. | accepted with maintainer follow-up | DONE | Merged as `70d79271061f9a3eab5c03ce77ce9c66244e9dbd`; history not purged, licence not decided. |
| #254 `claude/base-metier-inventory` | closed merged | Read-only inventory of architecture corpus. | accepted | DONE | Merged as `2002d013c925ef89e209b53e79c127623aa5de03`; validation-only. |
| #253 `claude/bilingual-glossary` | closed merged | Single EN/FR glossary section. | accepted | DONE | Merged as `914799cf659261c233cb4fd5b7baf1b0f4ccc0bd`; vocabulary only. |
| #252 `claude/ai-logs-index` | closed merged | `ai_logs/INDEX.md` and generator. | accepted | DONE | Merged as `a0a80c4a6962a653393cd03d869d1c9f9b23be5f`; navigation only. |
| #251 `claude/claude-md-mcp-ui-dashboard-alignment` | closed merged | Protected `CLAUDE.md` alignment. | accepted as B-1 exception | DONE | Merged as `c8a71ce1e397d87b4ebd25bf332dcf6dbe065e59`; protected-path precedent. |
| #250 `claude/version-changelog-realign` | closed merged | Version / changelog realignment. | accepted with caveat | DONE | Merged as `e45f37276f0ee2153909efd660ac4d4fa1720001`; description understated protected path changes. |
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
| #234 branch `dcode-agent-kit-placement` | closed merged | dcode-agent-kit as external reference for Hermes-side scaffolding. | accepted as external reference only | DONE | Merged as `e9ef05c179e2404d28bb379e3d27bbafca057d31`; no Card Stack or Skill Lifecycle change. |
| #228 `feat/update-verification` | closed unmerged | Same non-numeric update-version fix as #239. | accepted as content, superseded by #239 | DONE / CLOSE_SUPERSEDED | Closed without merge. Same head SHA as #239 before merge. |
| #218 `claude/governed-composition-land` | closed merged | Governed composition examples and schema fields. | accepted after protected review fixes | DONE | Merged as `830bf9100bb2f572af6cf13390abc1e7bbe30b39`; protected `schemas/` change landed after Codex rebase/fixes. |
| #217 `chatgpt/operational-brain-distillation-20260625` | closed merged | Operational context corpus in memory/knowledge doctrine. | accepted as candidate/support memory doctrine | DONE | Merged as `149bed9e0ada144d6e453520ced7b73dff4534a4`; documented non-implemented. |

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

#218 landed after protected schema review and Codex correction.

Protected paths:

```text
schemas/README.md
schemas/examples/workflow_manifest.example.yaml
schemas/workflow_manifest.schema.yaml
```

Accepted:

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

Protected review fix requirements recorded before merge:

```text
capability_steps[] must require a complete governance signature;
post_execution_evidence.required == true must require answer_verification and probative_certainty;
negative schema tests must prove under-specified steps and incomplete required evidence gates fail validation;
no runtime implication must be introduced by schema vocabulary.
```

Current state:

```text
Merged.
Protected schema change accepted as validation metadata / documented non-implemented.
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
