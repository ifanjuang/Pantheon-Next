# Pantheon Next — Runtime Adapters Authority Index

Status: candidate support map — populated (runtime-adapters migration group); awaiting review.

This sub-index carries the runtime-adapter rows migrated out of the Current authority map of `docs/governance/AUTHORITY_INDEX.md`, per `docs/governance/AUTHORITY_INDEX_DECOMPOSITION_PLAN.md` (PR D/E, after the coverage checker was extended to read sub-indexes). It keeps tool-specific material away from the tool-agnostic kernel table while preserving the placement rule.

It does not override the authority vocabulary, promotion rule, placement test, tool naming rule, terminology boundary rule or sensitive-path guardrail of `docs/governance/AUTHORITY_INDEX.md`. The master index defines how to read authority; this file only lists where documents sit. Moving a row here changes no authority class and promotes nothing.

## Runtime adapters map

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `docs/governance/EXTERNAL_RUNTIME_THREAT_MODEL_REVIEW.md` | active support doctrine | documented non-implemented | Review method for external runtimes, mixed AI workspaces and privileged capability surfaces. Classifies exposure, host-control, untrusted content, evidence and gates. No scanner, sandbox, runtime, adapter, operation or implementation. |
| `docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` | active support doctrine | documented non-implemented | Generic boundary for external runtime memory, checkpoint, graph recall and observability adapters. No memory backend, MCP server, checkpoint engine, observability backend or approval/memory engine implemented. |
| `docs/governance/HERMES_KANBAN_EXECUTION_PATTERNS.md` | candidate / to verify | documented non-implemented | Tool-specific Hermes Kanban execution-pattern note only. Coordinates runtime patterns only; does not grant approval, memory, scheduling or governance authority. |
| `docs/governance/HERMES_PAGE_AGENT_INTEGRATION.md` | active support doctrine | documented non-implemented | Hermes-side Page-Agent / Chrome / MCP browser-control adapter framing. Raw Page-Agent commands are not exposed; P0 is status + observe only; final effects require explicit human gates. No Page-Agent dependency, Chrome extension, Hermes skill, MCP service, browser automation, approval engine, memory engine or external action is implemented. |
| `docs/governance/MCP_POLICY_SERVER_CANDIDATE.md` | candidate / to verify | documented non-implemented | Candidate-only MCP policy plane for read-only governance resources, validation-only policy checks and MCP capability passporting. It does not create an MCP runtime, host, gateway, approval engine or memory engine. |
| `docs/governance/TRIPARTITE_INTERFACE_SPEC.md` | candidate support doctrine | documented non-implemented | Interface grammar for exposure surface, execution runtime, Pantheon governance and optional MCP policy surface. Defines data objects and trace spine only; no API, endpoint, queue, scheduler, OpenWebUI extension, Hermes skill, MCP tool, approval engine, memory engine or external action. |
| `docs/governance/MCP_PANTHEON_MINIMAL_V0.md` | candidate support doctrine | documented non-implemented | Minimal MCP Pantheon posture: read-only resources, validation-only tools, candidate skeletons and reports. Refuses runtime, connector gateway, provider router, scheduler, queue, approval engine, memory promotion and external action server. |
| `docs/governance/REFUSAL_FIXTURES.md` | candidate support doctrine | documented non-implemented | Refusal fixture catalog for future MCP, Hermes adapter and OpenWebUI gate tests. Documentation only; no tests, CI, runtime behavior, MCP tools, OpenWebUI actions, Hermes skills, external actions, approval behavior or memory promotion. |
| `docs/governance/NANGO_HERMES_CONNECTOR_GATEWAY.md` | candidate support doctrine | documented non-implemented | How Nango may be considered a bounded Hermes-side connector gateway for third-party APIs. Does not install Nango; no runtime. |
| `docs/governance/PADDLEOCR_HERMES_SKILL_NOTE.md` | candidate / to verify | documented non-implemented | Placement note for PaddleOCR as a possible document-extraction adapter. Does not implement PaddleOCR. |
| `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` | candidate / to verify | documented non-implemented | Development sequence for a future Pantheon MCP Policy Server. No MCP server, Docker service, installer, dashboard, gateway, connector runtime, scheduler, queue, approval engine, memory engine, router or plugin manager. Partially superseded by the implemented read-only `mcp-server/` artifact; remains useful as development history and must not contradict `WHAT_RUNS.md` or `MODULES.md`. |
| `docs/governance/UNDERSTAND_ANYTHING_HERMES_ADAPTER.md` | candidate support doctrine | documented non-implemented | How Understand-Anything may be considered a bounded Hermes-side structural-analysis capability. Does not install it; no runtime. |
| `docs/governance/PADDLEOCR_DASHBOARD_INSTALL_CANDIDATE.md` | candidate / to verify | documented non-implemented | Dashboard-installable, Hermes-managed OCR placement note. Governs status, scope, evidence and memory boundaries only; no install, runtime, skill, MCP host, OCR pipeline, approval engine or memory promotion. |

## Boundary

This file moves rows; it decides nothing. Authority classes and repo states are copied verbatim from the master index at migration time. Any class change routes through its own reviewed PR against the master index rules.
