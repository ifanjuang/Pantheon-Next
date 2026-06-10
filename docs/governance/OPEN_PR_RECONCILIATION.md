# Open PR Reconciliation and Integration Plan

Status: validation-only — reconciliation trace, not doctrine.

Reconciliation date: 2026-06-07.

This document takes stock of the recent merges and the currently open pull
requests, classifies them, surfaces the cross-cutting risks, and proposes a
sequenced integration order. It records a position; it does not promote any
candidate, decide an open governance fork or modify any protected path.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Authority: per `AUTHORITY_INDEX.md`, this is validation-only material. It does
not override canonical doctrine, candidate docs or the open PRs it describes.
When it disagrees with `AUTHORITY_INDEX.md` on authority, the index wins.

## Repository health — Governance CI is red on main

Verified on 2026-06-07: the Governance CI workflow is **failing on `main`** and
has been red across the recent merges. The cause is the forbidden-phrase lint
in `.github/workflows/governance-ci.yml`, not a real doctrine breach.

The lint flags an affirmative runtime word unless its section contains a
negation token. Its negation regex recognizes `reject(ed)` but **not** the word
`Refused`, and its queue allow-list recognizes `review queue` / `decision
queue` but **not** `Impact queue`. So legitimately-negated lines trip it:

```text
MCP_POLICY_SERVER_CANDIDATE.md   "Pantheon as provider router." (under Refused:)
MCP_POLICY_SERVER_CANDIDATE.md   "...automatic memory promotion engine." (Refused:)
EVIDENCE_MEMORY_CANONICALIZATION.md / EVIDENCE_MEMORY_DEV_PLAN.md  "Impact queue"
reference_reviews/ELT_REFERENCE_REVIEW.md  "automatic memory promotion;" (rejected list)
```

None of these lines authorize a runtime; each sits under a Refused / rejected /
review-surface context. This is a lint-precision gap. It must be resolved before
the open-PR backlog lands, otherwise every new PR inherits a red check and the
signal becomes worthless. Two clean options, maintainer's call (D0):

```text
D0a  Widen the negation regex (add "refused", allow "impact queue") in the
     workflow. The workflow is not a doctrine-protected path, but CI changes
     are consequential and should be reviewed deliberately.
D0b  Reword the four flagged lines to use lint-recognized negation wording,
     leaving the workflow untouched.
```

This plan recommends D0a (fix the check, not the doctrine) but does not apply
it: greening CI is its own reviewed change, not part of this reconciliation.

## What recently landed on main

Three movements dominate the recent history.

```text
MCP governance vocabulary
  MCP_POLICY_SERVER_CANDIDATE.md (candidate — to verify)
  templates/mcp_capability_passport.yaml
  templates/mcp_external_tool_review.md
  -> Pantheon may speak MCP and passport capabilities.
  -> Pantheon must not become an MCP host, runtime, gateway or executor.

Evidence / Memory separation
  MEMORY.md (active doctrine) keeps memory minimally constrained:
    candidate until approved, scope-bound, evidence-linked, revisable.
  EVIDENCE_MEMORY_CANONICALIZATION.md + EVIDENCE_MEMORY_DEV_PLAN.md
    (candidate — issue #68) add the rigorous evidence path:
    Raw Source -> Evidence Candidate -> Extraction Candidate
    -> Memory Candidate -> Human Gate -> Canonical Memory -> projection.
  -> Evidence is the rigorous log. Memory stays light but only canon by gate.

External runtime memory adapters
  EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md (active support, 0.1.31)
  -> adapters may propose candidates; never canonize, approve or decide scope.
```

The separation the request names is already coherent on main: **memory carries
the minimum constraint (atomic, scoped, revisable, candidate-by-default), while
the evidence path carries the rigor (metadata, speech-act, explainable
confidence, dependency and impact review, audit events).** The open PRs extend
this, they do not contradict it.

## Open PRs — classification

Ten PRs are open, all documentation-only, most still draft. They fall into four
clusters plus two keystones.

### Cluster A — Pantheon Control (dashboard, installer, preflight, MCP server path)

| PR | Adds | State |
|---|---|---|
| #67 | `PANTHEON_CONTROL_DASHBOARD.md`, `PANTHEON_CONTROL_DOCUMENT_MEDIA_STACK.md`, `PANTHEON_CONTROL_OBSERVABILITY_AND_VOICE.md` | draft, candidate |
| #66 | `MODULE_INVOCATION_PREFLIGHT.md` | draft, candidate |
| #72 | `PANTHEON_CONTROL_INSTALLATION.md` | draft, candidate |
| #75 | `PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` | draft, candidate |

This is one coherent perimeter — administration surface, installation boundary,
invocation preflight, and the staged MCP policy-server development path. It is
also the perimeter closest to the CLAUDE.md red lines (no heavy dashboard, no
plugin manager, no MCP runtime, no scheduler). Each PR is correctly bounded as
documented non-implemented, but together they add 5–6 new `PANTHEON_CONTROL_*`
/ MCP documents at once — the doctrine-sprawl risk that issue #41 warns about.

### Cluster B — Evidence -> Memory verification

| PR | Adds | State |
|---|---|---|
| #71 | `ANSWER_VERIFICATION_GATE.md` (V0–V4, C0–C4, `answer_status`) | draft, candidate |
| #76 | `docs/examples/architecture_proof_register/` vertical example | open, ready |

#71 formalizes "memory first, evidence when consequential, status when
deciding, approval when acting." #76 exercises that path end-to-end on a
fictional architecture dossier (proof candidates + Human Decision Gate, no
direct answer). #76 depends conceptually on #71 staying candidate.

### Cluster C — Keystone: governed composition (#53)

| PR | Adds | State |
|---|---|---|
| #53 | `CAPABILITY_REGISTRY.md`, governed-composition section in `WORKFLOW_SCHEMA.md`, two gates, `reference_reviews/SKILL_FORGE_RUNTIMES.md`, `reference_reviews/SKILL_GOVERNANCE.md` | draft |

This is a **dependency keystone**: #66, #67 and #75 all reference it (capability
registry, the two gates, HÉPHAÏSTOS). Landing Cluster A before #53 would leave
dangling references to a non-canonical registry.

### Cluster D — Reference reviews (low coupling, low risk)

| PR | Adds | State |
|---|---|---|
| #73 | `reference_reviews/LLM_SYSTEM_PATTERNS.md` | open, ready |
| #74 | `reference_reviews/BRAINAPI_ARCHITECTURE_WORKFLOW_REVIEW.md` | open, ready |
| #69 | `ai_logs/` document-learning explainer boundary note | draft |

Independent, additive, distillation-only. They only touch their own file plus
`reference_reviews/README.md`.

## Cross-cutting risks

1. **Index contention.** Almost every PR edits the same coordination files —
   `AUTHORITY_INDEX.md`, `MODULES.md`, `STATUS.md`, `CHANGELOG.md`,
   `reference_reviews/README.md`. They all branch from `main` independently, so
   the first merge will create conflicts in every other branch. Merges must be
   serialized and each branch rebased before merge.

2. **Doctrine sprawl (issue #41).** Cluster A adds a family of new perimeter
   documents. Decide the umbrella shape before merging: one `PANTHEON_CONTROL`
   perimeter with sub-sections, or a deliberately-indexed family.

3. **C-scale collision.** `MCP_POLICY_SERVER_CANDIDATE.md` already uses
   `approval_required: C0..C5` (approval ceiling). PR #71 introduces
   `C0..C4` as *consequence* levels. Two different C-scales must not coexist
   unreconciled — rename or unify before #71 lands.

4. **Boundary fork — separate repository.** #67, #72 and #75 all repeatedly ask
   whether Pantheon Control / the MCP policy server should live in a **separate
   repo**. This is the single architectural decision that shapes everything in
   Cluster A. It is unresolved and belongs to the maintainer.

## Decisions needed (maintainer)

These are forks this plan does not decide:

```text
D1  Does Pantheon Control / MCP policy server live in a separate repo,
    or stay as governance docs here until an external implementation exists?
D2  Is Cluster A one PANTHEON_CONTROL perimeter doc with sections,
    or a deliberately-indexed family of documents?
D3  Answer Verification Gate (#71): standalone doctrine, or folded into
    REQUEST_LIFECYCLE.md / MEMORY.md to avoid sprawl?
D4  C-scale: reconcile #71 consequence levels with the MCP approval ceiling
    (rename consequence to a non-C prefix, or unify the scale).
D5  Should EVIDENCE_MEMORY_CANONICALIZATION.md remain support doctrine,
    or be promoted into MEMORY.md after review (its own open question)?
```

## Proposed integration sequence

Each step: rebase the branch on latest `main`, reconcile the index files in
that one PR only, merge, then rebase the next branch. Land the low-risk
independent reviews early to shrink the index-churn surface.

```text
0. Green the Governance CI first (D0). No backlog PR should merge onto a
   red baseline; otherwise its own check is meaningless.

1. Cluster D first (independent, distillation-only):
   #73 -> #74 -> #69
   Smallest footprint; clears reference_reviews/README.md churn early.

2. Keystone #53 (governed composition / capability registry / two gates):
   Resolve D2-adjacent naming, then merge so Cluster A can reference it.

3. Resolve D1 and D2, then Cluster A in dependency order:
   #66 (preflight) -> #67 (dashboard) -> #72 (installation)
   -> #75 (MCP development path)
   Consolidate per D2 before or during merge.

4. Resolve D3 and D4, then Cluster B:
   #71 (answer verification, reconciled) -> #76 (proof-register example)

5. Reconciliation pass:
   Update STATUS.md live-exceptions table, AUTHORITY_INDEX.md rows and
   MODULES.md map once, against the merged state. One ai_logs entry.
```

## Boundary

This plan adds no perimeter, no schema, no test, no runtime and touches no
protected path. It only orders existing documentation work and names the open
decisions.

```text
Pantheon defines the contract.
The tools carry the work.
The validated remains.
```
