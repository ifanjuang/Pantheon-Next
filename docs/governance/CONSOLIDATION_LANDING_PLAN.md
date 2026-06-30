# Consolidation Landing Plan

Status: validation-only / consolidation proposal — to verify.

Date: 2026-06-30

Scope: repository consolidation, branch and PR landing sequence, status honesty, documentation debt, cockpit/HTML boundary, candidate-doctrine discipline and first vertical slice.

This document consolidates two audit positions:

- ChatGPT global qualitative review of the repository, Markdown/HTML coherence, open PRs and branch landing risk;
- Claude global quality audit `2026-06-30-audit-qualite-global-pantheon-next.md`, especially the specification-heavy / implementation-light warning.

It records a proposed landing plan. It does not promote doctrine, merge branches, change protected paths, implement runtime behavior, approve candidates, or alter memory/proof status.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Executive position

Pantheon Next is doctrinally strong but has entered a phase where adding more candidate doctrine is less valuable than proving, reducing and landing what already exists.

The next phase should not be expansion.

It should be:

```text
status honesty;
branch triage;
document reduction;
public-surface correction;
first governed vertical slice.
```

Core recommendation:

```text
Stop adding horizontal doctrine until the repo can show what runs, what is only documented, what is candidate, and what is deliberately absent.
```

## Guiding rule

A branch, document, template, capability or domain proposal should land only if it reduces ambiguity.

```text
If it adds possibility but blurs status, close or rewrite it.
If it clarifies status, proof, scope, approval, memory or external action, it may land.
```

## Phase 0 — Landing mode

Decision proposed: enter a temporary landing mode.

Allowed during landing mode:

```text
- correct;
- reduce;
- merge equivalent documents;
- classify branches;
- close superseded PRs;
- update status honesty;
- prepare a vertical slice;
- create non-runtime validation plans.
```

Not allowed by default during landing mode:

```text
- new role family;
- new card family;
- new large candidate doctrine;
- new external reference unless it resolves an active decision;
- new runtime implication;
- merge of an unclassified branch.
```

Decision Zeus: Accepté, unless the maintainer explicitly lifts the landing mode for a scoped work package.

## Phase 1 — Status honesty

### 1. Create `WHAT_RUNS.md`

Purpose: distinguish what actually runs from vision, static prototypes and documented non-implemented material.

Minimum structure:

```text
Runs now:
- static GitHub Pages landing;
- Pantheon Control static prototype;
- mcp-server read-only verification surface, if confirmed;
- schemas validation, if confirmed;
- tests, if confirmed.

Does not run:
- OpenWebUI integration;
- Hermes skill execution from Pantheon;
- external action sending;
- automatic approval;
- automatic memory promotion;
- data platform runtime;
- architecture vertical slice, until proven.

Boundary:
static UI is not product availability;
read-only verification is not governance approval;
documentation is not implementation.
```

Decision Zeus: Accepté.

### 2. Reconcile `STATUS.md`, `AUTHORITY_INDEX.md`, `MODULES.md`

Main unresolved point:

```text
mcp-server / dashboard / Pantheon Control status.
```

Current tension to resolve:

```text
- STATUS.md treats the MCP policy plane as candidate / to verify;
- AUTHORITY_INDEX.md treats MCP-related material as candidate / documented non-implemented;
- MODULES.md appears to recognize a bounded read-only MCP policy/validation surface;
- Claude notes that the promised dashboard boundary has drifted into mcp-server + docs/assets/pantheon-control.
```

Required decision:

```text
Option A — MCP remains candidate-only everywhere.
Option B — MCP is recognized as read-only implementation artifact.
Option C — MCP is active support validation surface, strictly read-only.
```

Recommended arbitration:

```text
Use B or C if mcp-server actually runs read-only checks.
Do not leave mixed status.
```

Boundary phrase if B/C is retained:

```text
The read-only MCP verification surface may return status/data.
It does not approve, execute, send, schedule, route, promote memory, or govern by itself.
```

Decision Zeus: À arbitrer.

## Phase 2 — Branch and PR landing

Create or maintain:

```text
docs/governance/OPEN_BRANCH_LANDING_PLAN.md
```

Status: validation-only / branch landing control.

Every open PR and non-merged branch should be classified before merge.

Recommended columns:

```text
PR / branch
subject
kind
protected path touched?
supersedes
superseded by
risk
decision Zeus
action
next step
```

Allowed actions:

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

### Current PR triage

| PR | Subject | Proposed status | Action | Decision Zeus |
|---|---|---|---|---|
| #239 | non-numeric version fix in update verification | protected path / read-only code fix | `PROTECTED_REVIEW` | À vérifier |
| #240 | Method Card -> Hermes handoff template | useful but duplicative risk | `REWRITE` shorter, cross-reference `CAPABILITY_PLACEMENT.md` | Accepté sous réserve |
| #245 | compact architecture method run tests | useful candidate examples | `KEEP_DRAFT`, then merge after #240 decision | À valider |
| #234 | dcode-agent-kit scaffolding reference | external reference candidate | `KEEP_DRAFT`, no card-stack promotion | À vérifier |
| #238 | earlier architecture run tests | superseded | `CLOSE_SUPERSEDED` | Accepté |
| #241 | earlier architecture method deck pruning | superseded by #244 | `CLOSE_SUPERSEDED` | Accepté |
| #233 | earlier method-card model path | superseded by #237 | `CLOSE_SUPERSEDED` | Accepté |

Rule:

```text
No branch lands because it exists.
A branch lands only if it reduces ambiguity or delivers a scoped verified correction.
```

## Phase 3 — Candidate discipline

### Rule of the referent

Claude proposes that `candidate -> active` require an executable consumer.

ChatGPT modification: an executable consumer is ideal but too narrow for governance doctrine.

Recommended rule:

```text
A candidate may be promoted only if it has at least one referent:

1. a validated executable consumer;
2. a schema/test validation path;
3. a documented end-to-end professional case;
4. a real doctrine contradiction it resolves;
5. an explicit human maintainer decision.
```

No candidate may be promoted only because it is well written or repeatedly referenced.

Decision Zeus: Accepté avec modification.

### Candidate metadata

Every candidate / to verify document should declare:

```text
Status:
Created:
Last reviewed:
Decision owner:
Promotion condition:
Review trigger:
```

A candidate older than 90 days without review should be routed to:

```text
promote;
fuse;
archive;
reject;
keep with reason.
```

Decision Zeus: Accepté.

### Complexity budget

Recommended candidate budget:

```text
No new candidate doctrine if the active candidate backlog exceeds the agreed threshold,
unless the new candidate closes, fuses or resolves an existing one.
```

Initial threshold to arbitrate:

```text
20 active candidate doctrine documents not expired.
```

Decision Zeus: À arbitrer.

## Phase 4 — Public surface correction

The public landing currently reads closer to product maturity than repository status warrants.

Required correction:

```text
Add a visible status band:
Pantheon Next currently contains doctrine, static prototypes and selected read-only validation artifacts.
The examples describe target governed behavior.
No external sending, final approval or canonical memory promotion is automated.
```

Recommended wording replacements:

| Current style | Replacement |
|---|---|
| `Pantheon cherche dans tes pièces` | `La méthode cible prévoit une recherche cadrée dans les pièces` |
| `Dans 20 minutes tu as...` | `Objectif cible: transformer une recherche dispersée en relecture cadrée` |
| `Rôles activés` | `Angles de revue mobilisés` |
| `Skills mobilisés` | `Capacités candidates` |

Decision Zeus: Accepté.

## Phase 5 — `base_metier/architecte/`

Claude identifies `base_metier/architecte/` as non-indexed, executable-adjacent and license-sensitive.

Recommended sequence:

```text
1. Inventory files.
2. Identify PDF provenance and license posture.
3. Identify scripts and executable surfaces.
4. Add authority classification if retained.
5. Move scripts toward Hermes or adapter territory.
6. Replace binaries with manifests where possible.
```

Recommended arbitration:

```text
Short term: index + audit + do not promote.
Medium term: extract to Hermes-side repository or external domain corpus storage.
Pantheon keeps only manifests, source policy, domain-pack rules and evidence expectations.
```

Decision Zeus: À arbitrer.

## Phase 6 — Architecture domain consolidation

Move architecture-domain material toward a clear domain-pack area.

Recommended target:

```text
docs/domain-packs/architecture/
```

This should contain the architecture-specific candidate/support doctrine currently spread through many `ARCHITECTURE_*` files.

Recommended approach:

```text
1. Create domain-pack README.
2. Move only in a dedicated PR.
3. Keep `DOMAIN_PACK_SPEC.md` generic.
4. Keep only a pointer/index in `docs/governance/` where needed.
5. Update `AUTHORITY_INDEX.md` and `MODULES.md` after move.
```

Decision Zeus: Accepté, but PR dédiée.

## Phase 7 — Vertical slice

The next proof of value should be a small governed vertical slice, not another doctrine layer.

Recommended first slice:

```text
architecture_devis_reprise
```

Why:

```text
- real professional liability;
- quote / scope / payment risk;
- possible implicit approval;
- strong evidence and source needs;
- clear external-action gate.
```

Minimum path:

```text
request
-> Task Contract Candidate
-> Context Pack / minimum context
-> external runtime or fixture candidate output
-> Result Candidate
-> Evidence Pack Candidate
-> User Decision Gate
-> draft-only output
-> optional Register Candidate
```

Do not start with a full OpenWebUI/Hermes product integration.

Start with:

```text
- fictional source dossier;
- Markdown runbook;
- candidate outputs;
- visible gates;
- optional read-only structural check after approval.
```

Decision Zeus: Accepté.

## Phase 8 — Hygiene work

Recommended quick wins:

```text
- synchronize VERSION and CHANGELOG;
- update STATUS.md date and posture;
- align ROADMAP with AUTHORITY_INDEX;
- remove or archive obsolete references;
- index ai_logs by quarter;
- classify docs/assets/pantheon-control as static prototype;
- resolve legacy zip status;
- unify CI/doctor required-file list if protected-path approval is granted.
```

Protected-path reminder:

```text
schemas/, tests/, pyproject.toml, operations/, platform/, Docker, .env, CLAUDE.md and mcp-server changes require explicit review.
```

## Recommended order

```text
1. Adopt landing mode.
2. Create WHAT_RUNS.md.
3. Reconcile MCP/dashboard/Pantheon Control status.
4. Create OPEN_BRANCH_LANDING_PLAN.md.
5. Close superseded PRs.
6. Put #239 under protected review.
7. Rewrite #240 as specialization only.
8. Review #245 after #240 decision.
9. Correct public landing honesty.
10. Audit base_metier/architecte.
11. Prepare architecture_devis_reprise vertical slice.
```

## Decision summary

Accepted:

```text
landing mode;
WHAT_RUNS.md;
branch landing plan;
public landing correction;
rule of the referent, modified;
candidate metadata;
architecture vertical slice;
ai_logs indexing;
VERSION / CHANGELOG sync;
closing superseded PRs.
```

Refused:

```text
merging branches only because they exist;
adding more candidate layers before consolidation;
presenting static prototypes as product availability;
letting role/skill wording imply autonomous execution;
leaving base_metier unclassified.
```

To verify:

```text
#239 protected fix;
exact non-merged branch list;
obsolete references;
base_metier scripts and license posture;
legacy zip usefulness;
MCP runtime/read-only behavior.
```

To arbitrate:

```text
mcp-server status;
dashboard boundary;
base_metier extraction;
candidate complexity budget;
architecture-domain folder move;
protected-path changes.
```

## Boundary

This document is validation-only.

It records a proposed consolidation and landing sequence.

It does not:

```text
implement a runtime;
create a schema;
modify tests;
change operations;
create a platform component;
install Hermes skills;
create OpenWebUI integration;
approve candidates;
promote memory;
create external actions;
merge branches;
resolve protected-path decisions.
```

The validated remains.
