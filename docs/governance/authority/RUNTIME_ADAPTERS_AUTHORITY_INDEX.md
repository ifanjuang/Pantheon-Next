# Pantheon Next — Runtime Adapters Authority Index

Status: candidate support map — populated (runtime-adapters migration group); awaiting review.

This sub-index carries the runtime-adapter rows migrated out of the Current authority map of `docs/governance/AUTHORITY_INDEX.md`, per `docs/governance/AUTHORITY_INDEX_DECOMPOSITION_PLAN.md` (PR D/E, after the coverage checker was extended to read sub-indexes). It keeps tool-specific material away from the tool-agnostic kernel table while preserving the placement rule.

It does not override the authority vocabulary, promotion rule, placement test, tool naming rule, terminology boundary rule or sensitive-path guardrail of `docs/governance/AUTHORITY_INDEX.md`. The master index defines how to read authority; this file only lists where documents sit. Moving a row here changes no authority class and promotes nothing.

## Runtime adapters map

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` | active support doctrine | documented non-implemented | Generic boundary for external runtime memory, checkpoint, graph recall and observability adapters. No memory backend, MCP server, checkpoint engine, observability backend or approval/memory engine implemented. |
| `docs/governance/HERMES_CAPABILITY_BINDINGS.md` | candidate support doctrine | documented non-implemented | Registry for Hermes-side capability slots and preferred bindings: Crawlberg, Nango, Langfuse, Understand-Anything, RAGFlow and Revit local adapter. Governance-readable classification only; not a dependency registry, install queue, plugin marketplace, provider router, runtime roadmap, auto-update plan, approval shortcut or memory promotion queue. |
| `docs/governance/AGENTTRANSFER_HERMES_ARTIFACT_TRANSFER.md` | candidate support doctrine | documented non-implemented | How AgentTransfer may be considered a bounded Hermes-side artifact-transfer binding. Transport receipts are traces, not professional evidence; no install, MCP host, file store, email relay, approval engine, memory engine, external-send channel or runtime is implemented. |
| `docs/governance/HERMES_INTEGRATION.md` | candidate / to verify | documented non-implemented | Tool-specific Hermes Kanban execution-pattern note only. Coordinates runtime patterns only; does not grant approval, memory, scheduling or governance authority. |
| `docs/governance/MCP_POLICY_SERVER_CANDIDATE.md` | candidate / to verify | documented non-implemented | Candidate-only MCP policy plane for read-only governance resources, validation-only policy checks and MCP capability passporting. It does not create an MCP runtime, host, gateway, approval engine or memory engine. |
| `docs/governance/MCP_PANTHEON_MINIMAL_V0.md` | candidate support doctrine | documented non-implemented | Minimal MCP Pantheon posture: read-only resources, validation-only tools, candidate skeletons and reports. Refuses runtime, connector gateway, provider router, scheduler, queue, approval engine, memory promotion and external action server. |
| `docs/governance/REFUSAL_FIXTURES.md` | candidate support doctrine | documented non-implemented | Refusal fixture catalog for future MCP, Hermes adapter and OpenWebUI gate tests. Documentation only; no tests, CI, runtime behavior, MCP tools, OpenWebUI actions, Hermes skills, external actions, approval behavior or memory promotion. |
| `docs/governance/NANGO_HERMES_CONNECTOR_GATEWAY.md` | candidate support doctrine | documented non-implemented | How Nango may be considered a bounded Hermes-side connector gateway for third-party APIs. Does not install Nango; no runtime. |
| `docs/governance/PADDLEOCR_HERMES_SKILL_NOTE.md` | candidate / to verify | documented non-implemented | Placement note for PaddleOCR as a possible document-extraction adapter. Does not implement PaddleOCR. |
| `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` | candidate / to verify | documented non-implemented | Development sequence for a future Pantheon MCP Policy Server. No MCP server, Docker service, installer, dashboard, gateway, connector runtime, scheduler, queue, approval engine, memory engine, router or plugin manager. Partially superseded by the implemented read-only `mcp-server/` artifact; remains useful as development history and must not contradict `WHAT_RUNS.md` or `MODULES.md`. |
| `docs/governance/UNDERSTAND_ANYTHING_HERMES_ADAPTER.md` | candidate support doctrine | documented non-implemented | How Understand-Anything may be considered a bounded Hermes-side structural-analysis capability. Does not install it; no runtime. |
| `docs/governance/PADDLEOCR_DASHBOARD_INSTALL_CANDIDATE.md` | candidate / to verify | documented non-implemented | Dashboard-installable, Hermes-managed OCR placement note. Governs status, scope, evidence and memory boundaries only; no install, runtime, skill, MCP host, OCR pipeline, approval engine or memory promotion. |

## Boundary

This file moves rows; it decides nothing. Authority classes and repo states are copied verbatim from the master index at migration time. Any class change routes through its own reviewed PR against the master index rules.
