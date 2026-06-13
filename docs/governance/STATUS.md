# Pantheon Next Status

Status date: 2026-06-01

Pantheon Next is under controlled bootstrap, conceptual stabilization and selective distillation from Pantheon-OS.

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

The repository holds a governance-first Markdown baseline (doctrine, roles, rites, approvals, evidence, memory, knowledge, scope, workflows, integrations), a navigation and authority layer, capability-placement and modular/domain doctrine, evidence-topology doctrine, a reconciled declarative schema baseline with a first validation test, seven lightweight Hermes profile templates, a non-executable `templates/` scaffold, and fictional professional examples.

Migration from Pantheon-OS remains incomplete.

```text
do not migrate unless governance value is proven
```

## How to read repository state

This file no longer re-lists every document. Three indexes are authoritative; consult them rather than duplicating here:

- `AUTHORITY_INDEX.md` — authority class and status of each item (canonical / support / candidate / reference / implementation / obsolete).
- `README.md` — entry point, read path and thematic navigation.
- `MODULES.md` — module map (authority document + status + runtime boundary per governance area).

```text
If STATUS and an index disagree on a file's existence, the index wins.
If they disagree on a file's authority, AUTHORITY_INDEX wins.
STATUS records posture and live exceptions only.
```

## Migrated from Pantheon-OS

Migrated doctrine, not stubs:

- `ARCHITECTURE.md`, `MODULES.md`, `CODE_AUDIT_POST_PIVOT.md`, `TASK_CONTRACT_REVISIONS.md`, `EXECUTION_DISCIPLINE.md`, `ROLE_SIGNALS.md`.

These describe governance structure, migration posture, audit discipline, contract lifecycle, contribution discipline and role-signal doctrine only. They do not implement execution, routing, scheduling, queueing, Docker, endpoints or operations tooling.

## Live exceptions — active candidate / to verify clusters

This table tracks active unresolved clusters that need dashboard visibility. It does not replace `AUTHORITY_INDEX.md`, which remains the full authority and status map.

| Document(s) | Status | Pending |
|---|---|---|
| `ANSWER_VERIFICATION_GATE.md` | candidate — to verify | central doctrine proposal for memory-first answers, evidence escalation and consequential response status; needs review before promotion |
| `DECISION_SURFACE_SPEC.md`, `SPICE_REFERENCE_DISTILLATION.md` | candidate / reference — to verify | decision-surface distillation from Spice review; display/capture only, must not become runtime, approval engine, Evidence Pack, memory engine or Hermes command |
| `DATA_PLATFORM_ARCHITECTURE.md`, `DATA_PLATFORM_INDEX.md`, `DATA_PLATFORM_STATUS.md`, `DATA_PLATFORM_RECONCILIATION.md` | to verify | boundary review (#28, #30) — a data platform must not become a runtime |
| `ARCHITECTURE_AGENCY_DOMAIN_PACK.md`, `KNOWLEDGE_INGESTION_AND_MEMORY.md`, `WORKFLOW_LIFECYCLE.md` | candidate — to verify | own headers declare `candidate`; promotion pending (#30) |
| `ARCHITECTURE_PROOF_REGISTER.md` and related (`ARCHITECTURE_INDEX_EFFECT_MATRIX.md`, `ARCHITECTURE_PROOF_REGISTER_IMPLEMENTATION_SPEC.md`, `ARCHITECTURE_DOCUMENT_REVIEW.md`) | candidate | proof-register slice (#34); schema proposal in PR #35 |
| `DOCUMENT_INTELLIGENCE.md`, `REVIEW_QUEUE.md`, `URGENT_REVIEW_TRIAGE.md`, `RAW_DERIVED_GOVERNED_RECORDS.md`, `EXTERNAL_TOOL_PLACEMENT_REGISTER.md` | candidate | governed document/review model (#29, #33) |
| `MCP_POLICY_SERVER_CANDIDATE.md`, `templates/mcp_capability_passport.yaml`, `templates/mcp_external_tool_review.md` | candidate — to verify | MCP policy plane boundary review — must not become MCP runtime, host, gateway, approval engine or memory engine |
| `schemas/architecture-proof-register/*` | proposal | align to baseline conventions before integration (#37): YAML, `x-boundary`, example+test, shared scope enum + extensions |

Open reconciliation issues: #27 (AgentOS), #28 (data platform), #29 (review queue), #34/#35 (proof register), #37 (schema reconciliation), #41 (process coordination).

## Boundary reminder

All documents above are governance, navigation, support, candidate or reference material. None creates runtime behavior by itself. Promotion of any candidate, and any change under `schemas/`, `tests/`, `operations/`, `platform/`, Docker or `.env`, requires explicit review.

```text
Pantheon defines the contract.
The tools carry the work.
The validated remains.
```
