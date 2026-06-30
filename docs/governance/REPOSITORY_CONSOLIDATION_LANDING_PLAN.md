# Repository Consolidation Landing Plan

Status: validation-only / landing coordination — to verify.

Date: 2026-06-30

Source inputs:

- Global qualitative audit requested by the maintainer.
- Claude candidate audit: `2026-06-30-audit-qualite-global-pantheon-next.md`.
- ChatGPT governance review and branch-landing arbitration.
- Current repository doctrine: `STATUS.md`, `MODULAR_DOMAIN_REORIENTATION.md`, `CAPABILITY_PLACEMENT.md`, `DOMAIN_PACK_SPEC.md`, `AUTHORITY_INDEX.md`, `MODULES.md`.

This document records an execution order for consolidation. It does not create doctrine, promote candidates, implement runtime behavior, approve a merge, modify protected paths, install tools, execute Hermes, create a scheduler, create a queue, create an approval engine or promote memory.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Next has reached a consolidation threshold.

The repository is doctrinally coherent, but the number of candidate documents, open PRs, branches, prototypes and status layers creates a risk of self-bureaucratization.

The next work sequence should not add a new conceptual layer. It should land, classify, reduce, close, rewrite or prove what already exists.

Working rule:

```text
No new major candidate doctrine until the current landing queue is classified.
Reduce ambiguity before adding capability.
A branch that adds possibility but blurs status should not land.
A branch that reduces ambiguity may land.
```

## Core diagnosis

### Accepted from Claude audit

Claude's audit correctly identifies a structural risk:

```text
Pantheon is currently specification-heavy and implementation-light.
The layer intended to govern runtime complexity can reproduce complexity in prose.
```

This is a real risk. The answer is not to turn Pantheon into a runtime. The answer is to add status honesty, landing discipline and one bounded vertical slice that proves the governance loop.

### ChatGPT nuance

A candidate should not require executable runtime in every case. Some doctrine can be active if it resolves a real governance conflict or defines a durable invariant.

Therefore, the promotion rule should be:

```text
A candidate may be promoted only if it has at least one referent:
1. a validated executable consumer;
2. a schema/test consumer;
3. a documented end-to-end professional case;
4. a real doctrine contradiction it resolves;
5. an explicit maintainer decision with scope and status.
```

No candidate should become active merely because it is well written, old, repeated or convenient.

## Non-negotiable boundaries

This landing plan must not touch without explicit approval:

- `schemas/`;
- `tests/`;
- `pyproject.toml`;
- `operations/`;
- `platform/`;
- Docker files;
- `.env` files;
- `CLAUDE.md`;
- `mcp-server/`;
- GitHub Actions or CI scripts.

Allowed without separate confirmation, subject to review:

- `README*`;
- `CHANGELOG.md`;
- `docs/governance/*.md`;
- `docs/assets/*.md`;
- `ai_logs/*.md`;
- `hermes/profiles/*.md`;
- `templates/`;
- fictional examples and checklists.

## Phase 0 — Landing freeze

Status: accepted.

Immediate rule:

```text
No new concept, role, card family, major external reference, heavy template or new doctrine branch until the landing queue is classified.
```

Allowed work during freeze:

- create status-honesty documents;
- reconcile status conflicts;
- close superseded PRs;
- rewrite overgrown PRs;
- split protected-path work;
- correct public overclaiming;
- prepare a vertical slice plan;
- update Notion tracking.

Done when:

```text
All open PRs and relevant unmerged branches have a landing decision:
merge / rewrite / split / close superseded / close refused / protected review / keep draft.
```

## Phase 1 — Create `WHAT_RUNS.md`

Status: accepted.

Purpose: make repository status honest at system level, not only file by file.

Proposed path:

```text
docs/governance/WHAT_RUNS.md
```

Minimum content:

```text
Runs now:
- static GitHub Pages landing — documentation/demo;
- Pantheon Control static prototype — static UI, candidate/demo data;
- mcp-server read-only verification surface — yes/partial/to verify;
- schemas validation — yes/partial/to verify;
- tests — yes/partial/to verify.

Does not run:
- OpenWebUI integration;
- Hermes skill execution from Pantheon;
- external sending;
- automatic approval;
- automatic memory promotion;
- data platform runtime;
- architecture vertical slice.

Boundary:
Static UI is not product availability.
Read-only validation is not approval.
Documentation is not implementation.
```

Decision Zeus: accepted.

Repo state: documented non-implemented until created.

Next action: create the file before merging additional method/handoff PRs.

## Phase 2 — Reconcile status spine

Status: to arbitrate.

Target files:

- `STATUS.md`;
- `AUTHORITY_INDEX.md`;
- `MODULES.md`;
- possibly `CLAUDE.md` after explicit approval;
- future `WHAT_RUNS.md`.

Main conflict to resolve:

```text
mcp-server / dashboard / Pantheon Control
```

Current tension:

- Some doctrine treats MCP policy server as candidate / to verify.
- Some module wording suggests an active read-only verification surface.
- Claude audit identifies a `dashboard/` boundary promised in instructions but implemented in practice through `mcp-server/` and static Pantheon Control assets.

Options:

```text
A. Conservative:
   mcp-server remains candidate / to verify everywhere.

B. Honest read-only artifact:
   mcp-server is classified as an implementation artifact / read-only verification surface.
   It verifies and returns status data.
   It does not approve, execute, send, schedule, route providers or promote memory.

C. Future dashboard split:
   Create or reserve a separate dashboard module later.
```

Recommendation:

```text
Choose B short term.
Reserve C for later only when there is a real dashboard module.
Do not keep a paper boundary that no longer matches the repo.
```

Decision Zeus: to arbitrate.

Next action: maintainer decides B-1, then update the status spine in a dedicated PR.

## Phase 3 — Branch and PR landing queue

Status: accepted.

Every open PR or unmerged branch must receive one landing decision.

Allowed landing decisions:

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
```

Minimum table to maintain:

| PR / branch | Subject | Type | Protected path? | Replaces | Replaced by | Risk | Decision Zeus | Action |
|---|---|---|---|---|---|---|---|---|
| #239 | non-numeric version fix | code / tests | yes | — | — | protected path | to verify | PROTECTED_REVIEW |
| #240 | Method Hermes handoff template | docs candidate | no | — | — | duplicates handoff doctrine | accepted with changes | REWRITE |
| #245 | compact architecture method run tests | docs examples | no | #238 | — | low if compact | to validate | KEEP_DRAFT then MERGE |
| #234 | dcode-agent-kit reference | external reference | no | — | — | reference contaminates doctrine | to verify | KEEP_DRAFT |
| #238 | architecture method run tests | docs examples | no | — | #245 | superseded | accepted | CLOSE_SUPERSEDED |
| #241 | architecture method deck pruning | docs candidate | no | — | #244 | superseded | accepted | CLOSE_SUPERSEDED |
| #233 | method card model | docs candidate | no | — | #237 | superseded | accepted | CLOSE_SUPERSEDED |

Rules:

```text
1. Do not merge branches directly into main.
2. Do not merge a PR only because it is mergeable.
3. Close superseded PRs after confirming their replacement contains the retained decision.
4. Protected-path PRs are reviewed separately from documentation-only PRs.
5. If a branch is useful but too broad, split or cherry-pick into a clean branch.
```

Local inspection commands for branches without PR:

```bash
git fetch --all --prune
git branch -r --no-merged origin/main

git log --oneline origin/main..origin/BRANCH
git diff --stat origin/main...origin/BRANCH
git diff --name-status origin/main...origin/BRANCH
```

Decision Zeus: accepted.

Next action: create or maintain the landing table, then process PRs in order.

## Phase 4 — PR-specific decisions

### PR #239 — update version fix

Decision Zeus: to verify.

Classification:

```text
protected review
```

Reason:

- touches code/tests/read-only verification behavior;
- likely useful bug fix;
- must not be bundled with doctrine cleanups.

Next action:

```text
Review patch.
Confirm read-only boundary.
Run tests.
Merge only after explicit protected-path approval.
```

### PR #240 — Method Hermes handoff template

Decision Zeus: accepted with changes.

Classification:

```text
rewrite before merge
```

Keep:

- Method Card specific contribution;
- short architecture examples;
- checklist for Method Card to Hermes handoff;
- stop conditions specific to method projection.

Remove or replace by links:

- effect classes;
- canonical governed handoff;
- Capability Gap;
- Evidence Pack;
- approval levels;
- idempotency;
- generic Hermes boundaries.

Reason:

```text
CAPABILITY_PLACEMENT.md already owns governed execution handoff doctrine.
#240 must specialize it, not restate it.
```

### PR #245 — compact architecture method run tests

Decision Zeus: to validate.

Classification:

```text
keep draft; merge after #240 is rewritten or explicitly bypassed.
```

Requirement:

```text
Remain compact.
No new doctrine.
No new card family.
No hidden runtime claim.
```

### PR #234 — dcode-agent-kit reference

Decision Zeus: to verify.

Classification:

```text
external reference / candidate-only.
```

Requirement:

```text
Do not modify Card Stack now.
Do not promote skill scaffolding into Pantheon runtime.
Index as reference only if retained.
```

## Phase 5 — Public honesty fix

Status: accepted.

Target:

```text
docs/index.html
README.md / README.fr.md if needed
```

Problem:

The public-facing landing may imply product maturity beyond the actual repository status.

Required correction:

```text
Add an explicit status banner:
Pantheon Next currently contains doctrine, documentation, static prototypes and partial read-only verification artifacts.
The examples show target behavior.
No external transmission, approval or canonical memory promotion is automated by Pantheon.
```

Wording cleanup:

| Current pattern | Replace with |
|---|---|
| `Pantheon cherche dans tes pièces` | `La méthode cible prévoit une recherche cadrée dans les pièces` |
| `Dans 20 minutes tu as...` | `Objectif: transformer une recherche dispersée en relecture cadrée` |
| `Rôles activés` | `Angles de revue affichés` |
| `Skills mobilisés` | `Capacités candidates` |

Decision Zeus: accepted.

Next action: documentation/UI wording PR only.

## Phase 6 — `base_metier/architecte/` decision

Status: to arbitrate.

Claude audit flags this zone as:

- not indexed;
- containing PDFs and possible license exposure;
- containing Python scripts;
- closer to Hermes, a domain corpus or an adapter than to Pantheon kernel.

Options:

```text
A. Extract to a separate Hermes/domain repository.
B. Keep temporarily but index, audit license, move scripts out of kernel scope.
C. Remove.
```

Recommendation:

```text
Choose A as target.
Use B as short-term transition.
Do not leave it unindexed.
```

Immediate action:

```text
1. Inventory files.
2. Identify PDFs and license/provenance.
3. Identify scripts and executable behavior.
4. Add authority/index classification if it remains in repo.
5. Move scripts to Hermes/adapters later under explicit review.
```

Decision Zeus: to arbitrate.

## Phase 7 — Candidate discipline

Status: accepted with modification.

Add to `AUTHORITY_INDEX.md` or a support doctrine note:

```text
Candidate promotion requires a referent.
```

Referent types:

```text
validated executable consumer;
schema/test consumer;
end-to-end professional case;
real doctrine contradiction resolved;
explicit maintainer promotion decision.
```

New candidate metadata requirement:

```text
Status:
Created:
Last reviewed:
Decision owner:
Promotion condition:
Review trigger:
```

Review trigger:

```text
If a candidate remains unreviewed for more than 90 days, it must be promoted, fused, archived, refused or explicitly renewed.
```

Decision Zeus: accepted.

Next action: apply prospectively first; retrofit high-risk candidates later.

## Phase 8 — Repository hygiene

Status: accepted / to verify depending on item.

Actions:

```text
1. Align VERSION and CHANGELOG.
2. Decide whether VERSION remains authoritative.
3. Archive or relink obsolete docs.
4. Correct roadmap references to demoted stubs.
5. Add ai_logs/INDEX.md and quarterly grouping.
6. Reclassify docs/assets/pantheon-control as static prototype, not plain asset.
7. Review legacy/Pantheon-OS-main.zip and remove if not necessary.
8. Identify duplicated examples between examples/ and docs/examples/.
```

Protected-path note:

```text
CI, doctor, pyproject, tests and mcp-server dependency fixes require explicit approval and separate PRs.
```

Decision Zeus: mixed — mostly accepted; protected fixes to verify.

## Phase 9 — Architecture domain pack organization

Status: accepted as direction, PR dedicated.

Proposal:

```text
docs/domain-packs/architecture/
```

Move architecture-domain documents gradually into a dedicated folder rather than letting `docs/governance/` become the home of every architecture candidate.

Short-term path:

```text
1. Create architecture domain-pack index.
2. Keep canonical/general docs in docs/governance/.
3. Move or alias ARCHITECTURE_* candidates in a dedicated PR.
4. Update AUTHORITY_INDEX.md and docs/governance/README.md.
```

Decision Zeus: accepted, but not first.

Dependency:

```text
Do after status spine and branch landing queue.
```

## Phase 10 — Vertical slice proof

Status: accepted as major next milestone.

Candidate case:

```text
architecture_devis_reprise
```

Reason:

- strong professional responsibility signal;
- common agency workflow;
- risk of implicit validation;
- source/evidence needs;
- external-action boundary visible;
- good demonstration of draft vs sent.

Target loop:

```text
request
-> Task Contract
-> minimal Context Pack
-> execution runtime candidate output
-> Evidence Pack Candidate
-> Decision Gate
-> draft-only output
-> Register Candidate if validated
```

First proof should be documentation + fixtures before protected tests:

```text
1. fictional source dossier;
2. Task Contract example;
3. Evidence Pack Candidate example;
4. Decision Gate example;
5. candidate output;
6. runbook;
7. later: read-only test if explicitly approved.
```

Decision Zeus: accepted.

Boundary:

```text
The vertical slice proves governance flow.
It does not make Pantheon an execution runtime.
Hermes or another runtime executes outside Pantheon.
```

## Overall execution order

### Step 1 — immediate

```text
Create WHAT_RUNS.md.
Create/maintain branch landing table.
Correct landing public status wording.
```

### Step 2 — status spine

```text
Reconcile STATUS.md, AUTHORITY_INDEX.md and MODULES.md.
Decide mcp-server/dashboard classification.
```

### Step 3 — branch triage

```text
Close superseded PRs.
Review #239 separately.
Rewrite #240.
Review #245.
Keep #234 as reference-only if retained.
List and classify branches without PR.
```

### Step 4 — hygiene

```text
Version/CHANGELOG.
Obsolete docs.
Roadmap refs.
ai_logs index.
legacy zip.
base_metier inventory.
```

### Step 5 — structure

```text
Architecture domain-pack folder.
Candidate metadata discipline.
Complexity budget.
```

### Step 6 — proof

```text
architecture_devis_reprise vertical slice.
```

## Final rule

```text
Pantheon does not need more possible futures right now.
It needs fewer ambiguous statuses and one proof loop.

The validated remains.
The rest must be candidate, archived, refused or outside Pantheon.
```

## Boundary note

This document is a coordination artifact. It records a proposed plan. It does not create a runtime, merge a branch, approve a PR, promote doctrine, authorize protected-path changes, execute Hermes, send anything externally or promote memory.
