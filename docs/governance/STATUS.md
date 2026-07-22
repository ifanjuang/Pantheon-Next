# Pantheon Next Status

Status: canonical — primary repository posture and active document index.

Status date: 2026-07-22

Pantheon Next is the self-contained canonical governance repository under controlled stabilization and repository-status reconciliation.

## Doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next is a governance-first repository. It is not an execution runtime.

It does not implement an agent loop, tool runtime, provider router, internal scheduler, message/job/agent queue, message bus, hidden workflow runner, automatic approval system or automatic memory promotion. This single boundary applies to every document listed here; individual docs restate it only where useful.

## Current posture

Status: partial but structurally coherent.

The repository holds a governance-first Markdown baseline (doctrine, roles, rites, approvals, evidence, memory, knowledge, scope, workflows, integrations), a navigation and authority layer, capability-placement and modular/domain doctrine, evidence-topology doctrine, a runtime-status honesty map, a reconciled declarative schema baseline with validation tests where present, seven lightweight Hermes profile templates, a non-executable `templates` scaffold, static documentation/prototype assets, fictional professional examples and a bounded read-only policy/verification package under protected-path discipline.

That package now has two projections over one transport-neutral application facade:

```text
local MCP stdio consultation
internal-network HTTP policy/preflight adapter
```

Both return policy, validation and candidate data only. Neither projection executes, approves, sends, schedules, installs, updates, routes providers or promotes memory.

The active architecture remains explicitly split between:

```text
Pantheon kernel -> tool-agnostic governance rules.
Adapters        -> tool-specific projections, bindings and runnable configurations outside the kernel.
```

During controlled bootstrap, kernel rules may still be revised when a durable governance invariant is missing. Tool releases remain adapter review events by default; they justify a kernel change only when the existing abstract governance model cannot classify the new consequence.

Historical migration is closed. Pantheon Next has no live source dependency on its retired predecessor.

```text
do not migrate unless governance value is proven
```

## Runtime-status honesty map

`WHAT_RUNS.md` is the current support map for what runs, what is static, what is partial or to verify, what is documented non-implemented and what is voluntarily absent.

It does not replace `AUTHORITY_INDEX.md` or `MODULES.md`.

It prevents public, module or branch language from implying live capabilities where the repository only contains documentation, static prototypes, candidate doctrine, validation tests or partial read-only verification artifacts.

Current reconciled runtime-status point:

```text
mcp-server / policy HTTP adapter / dashboard / Pantheon Control
```

After protected review and merge of PR #239, `mcp-server/` is no longer only a future candidate in repository terms. It is a bounded read-only verification artifact, still partial / to verify as a whole.

The current artifact includes governed-source listing, allowlisted architecture explanations, qualification of caller-provided capability-status candidates, policy classification, candidate preparation and provided-evidence verification. The `pantheon-policy-api` candidate projects the same service over authenticated internal HTTP for deterministic Hermes preflight. It does not implement live runtime inventory, remote MCP, private knowledge retrieval, a permission authority, an approval store or external execution.

The external `pantheon-modules` Hermes dashboard-plugin template can produce a partial live operational inventory after separate installation and enablement in Hermes. Pantheon qualifies caller-provided observations; it does not become a second inventory producer or runtime.

```text
implemented read-only / partial / protected path
```

This classification must not imply execution, approval, sending, scheduling, provider routing, installing, updating or memory promotion.

## How to read repository state

This file no longer re-lists every document. The repository-state spine is split across entry, status, authority, module and contribution files; consult them rather than duplicating here:

- `docs/governance/README.md` — governance entry point and read path.
- `README.md` — repository entry point.
- `CONTRIBUTING.md` — contribution guardrail and protected-path discipline.
- `AUTHORITY_INDEX.md` — authority class and status of each item (canonical / support / candidate / reference / implementation / obsolete).
- `MODULES.md` — module map (authority document + status + runtime boundary per governance area).
- `WHAT_RUNS.md` — runtime-status honesty map (what runs, what is static, what is partial/to verify, what is absent).

```text
If STATUS and an index disagree on a file's existence, the index wins.
If they disagree on a file's authority, AUTHORITY_INDEX wins.
If WHAT_RUNS and a module description disagree on runtime availability, treat the item as partial / to verify until reconciled.
STATUS records posture and live exceptions only.
```

## Inherited and independently maintained doctrine

Migrated doctrine, not stubs:

- `ARCHITECTURE.md`, `MODULES.md`, `CODE_AUDIT_POST_PIVOT.md`, `TASK_CONTRACT_REVISIONS.md`, `EXECUTION_DISCIPLINE.md`, `ROLE_SIGNALS.md`.

These describe governance structure, migration posture, audit discipline, contract lifecycle, contribution discipline and role-signal doctrine only. They do not implement execution, routing, scheduling, queueing, Docker, endpoints or operations tooling.

## Live exceptions — active candidate / to verify clusters

This table tracks active unresolved clusters that need dashboard visibility. It does not replace `AUTHORITY_INDEX.md`, which remains the full authority and status map.

| Document(s) | Status | Pending |
|---|---|---|
| `WHAT_RUNS.md` | active support — to verify | runtime-status honesty; must not promote partial implementations by implication |
| `ANSWER_VERIFICATION_GATE.md` | candidate — to verify | central doctrine proposal for memory-first answers, evidence escalation and consequential response status; needs review before promotion |
| `DECISION_SURFACE_SPEC.md`, `SPICE_REFERENCE_DISTILLATION.md` | candidate / reference — to verify | decision-surface distillation from Spice review; display/capture only, must not become runtime, approval engine, Evidence Pack, memory engine or Hermes command |
| `DATA_PLATFORM_ARCHITECTURE.md` | to verify | boundary review (#28, #30) — a data platform must not become a runtime; former `DATA_PLATFORM_INDEX.md` and `DATA_PLATFORM_STATUS.md` were absorbed here, while `DATA_PLATFORM_RECONCILIATION.md` is historical only |
| `DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md`, `DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`, `RAG_INGESTION_PIPELINE.md`, `PANTHEON_MVP_VERTICAL_BINDING.md`, `PANTHEON_MVP_COCKPIT_RECONCILIATION.md` | external executable candidate implemented externally / not adopted | External commit `7f8989a` implements the cards-first cockpit, bounded previews and signed Knowledge update gate. Installation, target-runtime health, live Hermes binding, real-dossier authorization, activation and production deployment remain absent. `pantheon-mvp#45` separately proposes a synthetic static demo using the canonical MVP assets; it remains unmerged and not deployed. |
| `AGENCY_DOMAIN_PACK.md`, `KNOWLEDGE_INGESTION_AND_MEMORY.md`, `WORKFLOW_LIFECYCLE.md` | candidate — to verify | own headers declare `candidate`; promotion pending (#30) |
| `PROOF_REGISTER.md` and related (`INDEX_EFFECT_MATRIX.md`, `PROOF_REGISTER_IMPLEMENTATION_SPEC.md`, `DOCUMENT_REVIEW.md`) | candidate | proof-register slice (#34); schema proposal in PR #35 |
| `DOCUMENT_INTELLIGENCE.md`, `REVIEW_QUEUE.md`, `URGENT_REVIEW_TRIAGE.md`, `RAW_DERIVED_GOVERNED_RECORDS.md`, `EXTERNAL_TOOL_PLACEMENT_REGISTER.md` | candidate | governed document/review model (#29, #33) |
| `MCP_POLICY_SERVER_CANDIDATE.md`, `PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`, `templates/mcp_capability_passport.yaml`, `mcp-server/`, the HTTP API implementation contract, `Dockerfile.policy-api`, `compose.policy-api.yaml` | implemented read-only / partial / protected path | shared transport-neutral policy service, local MCP stdio projection and authenticated internal HTTP preflight candidate; HTTP deployment, Hermes enforcement wiring and real-environment activation remain to verify; none may become runtime, approval engine, sender, scheduler, provider router, installer, updater or memory engine |
| `schemas/architecture-proof-register/*` | proposal | align to baseline conventions before integration (#37): YAML, `x-boundary`, example+test, shared scope enum + extensions |

Open reconciliation issues remain historical signals until rechecked against the current authority index and open PR state.

## Historical reconciliations (removed 2026-07-07)

One-shot reconciliation and landing documents did their work and were removed in the governance cleanup; their full text stays in git history and the removal mapping lives in `ai_logs/2026-07-07-governance-cleanup-pass-a.md`:

```text
CONCEPTUAL_STABILIZATION.md
DATA_PLATFORM_RECONCILIATION.md
GOVERNANCE_LINKAGE_RECONCILIATION.md
OPEN_BRANCH_LANDING_PLAN.md
OPEN_PR_RECONCILIATION.md
POST_CONSOLIDATION_HANDOFF.md
REPOSITORY_CONSOLIDATION_LANDING_PLAN.md
STATUS_SPINE_RECONCILIATION.md
```

Future reconciliations record their outcome here (one line) and in `ai_logs/`; a reconciliation document is a working document, not doctrine.

## Historical reconciliations (recorded 2026-07-22)

```text
PANTHEON_MVP_COCKPIT_RECONCILIATION -> external cockpit implementation pinned at pantheon-mvp@7f8989a, classified as validation-only and kept uninstalled, unadopted and inactive; canonical demo ownership moved to pantheon-mvp#45 while Pantheon Next retains only an orientation link; logged in ai_logs/2026-07-22-mvp-cockpit-status-and-demo-link.md.
```

## Historical reconciliations (recorded 2026-07-08)

```text
README_ENTRY_REFACTOR             -> README / README.fr / CONTRIBUTING / public intro split; logged in ai_logs/2026-07-08-readme-entry-refactor.md.
STATUS_RUNTIME_READ_PATH          -> STATUS / WHAT_RUNS / MODULES read-path and test-status alignment; logged in ai_logs/2026-07-08-status-runtime-read-path.md.
AUTHORITY_PROTECTED_PATH_ALIGNMENT -> AUTHORITY_INDEX / IMPLEMENTATION_ARTIFACTS protected-path and implementation-artifact status alignment; logged in ai_logs/2026-07-08-authority-protected-path-alignment.md.
STATIC_PAGES_RUNTIME_LANGUAGE      -> public/static prototype wording pass for Pantheon Control and RAG page; logged in ai_logs/2026-07-08-static-pages-runtime-language.md.
PUBLIC_COCKPIT_WORDING_RULE        -> assets registry rule for public cockpit labels before landing-page refactor; logged in ai_logs/2026-07-08-public-cockpit-wording-rule.md.
ISSUE_183_PUBLIC_COCKPIT_COMMENT   -> GitHub issue #183 comment carrying the cockpit wording requirement into the landing refactor; logged in ai_logs/2026-07-08-issue-183-public-cockpit-comment.md.
GUARD_READONLY_VERIFICATION        -> read-only guard and pytest configuration review; CI, pytest and link status not run; logged in ai_logs/2026-07-08-guard-readonly-verification.md.
```

## Boundary reminder

All documents above are governance, navigation, support, candidate, validation-only, implementation-artifact or reference material. None creates runtime behavior by itself. Promotion of any candidate, and any change under `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `CLAUDE.md`, `mcp-server/` or GitHub Actions requires explicit review.

```text
Pantheon defines the kernel.
Adapters express the tools.
The tools carry the work.
The validated remains.
```
