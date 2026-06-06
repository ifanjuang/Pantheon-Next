# Sub-Agent-MCP Reference Review

Status: external runtime / adapter reference review — candidate only.

Date: 2026-06-06

This document reviews `stormaref/Sub-Agent-MCP` as an external inspiration for Pantheon Next.

It does not add a dependency.

It does not approve installation.

It does not implement Sub-Agent-MCP.

It does not authorize a Pantheon MCP runtime, sub-agent runtime, orchestration server, provider router, plugin manager, hidden workflow runner, automatic approval system, automatic memory promotion or external-action engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Source reviewed

Primary source:

```text
https://github.com/stormaref/Sub-Agent-MCP
```

Reviewed repository posture:

```text
A Python MCP server exposes one tool per YAML-defined sub-agent.
A parent LLM calls an agent tool with a prompt.
The server builds a LangChain agent with its own OpenAI-compatible model, system prompt and optional downstream MCP servers.
The sub-agent returns a final response object.
```

Implementation areas reviewed:

```text
README.md
config/agents.example.yaml
src/sub_agent_mcp/main.py
src/sub_agent_mcp/server/tools.py
src/sub_agent_mcp/server/openapi.py
src/sub_agent_mcp/agent/builder.py
src/sub_agent_mcp/agent/executor.py
src/sub_agent_mcp/mcp_client/manager.py
src/sub_agent_mcp/config/schema.py
```

## Pantheon classification

| Axis | Classification |
|---|---|
| Reference type | external runtime / adapter / delegation layer |
| Pantheon use | boundary stress-test and adapter vocabulary only |
| Hermes use | optional sub-agent delegation candidate behind Task Contract |
| OpenWebUI use | optional thin tool exposure of bounded agent capabilities only |
| Installation status | not installed |
| Adoption status | not approved |
| Doctrine status | support review only |

## What Sub-Agent-MCP solves

Sub-Agent-MCP is useful because it separates a parent LLM from specialized sub-agents.

Relevant capability families:

- parent-to-sub-agent delegation;
- per-agent prompt and model selection;
- per-agent downstream MCP server configuration;
- per-agent tool allowlisting;
- MCP tool exposure from YAML agent declarations;
- OpenAPI-compatible tool routes for OpenWebUI-style exposure;
- local or containerized runtime operation.

These capabilities are valuable.

They are also exactly why Sub-Agent-MCP must remain outside Pantheon core.

## Boundary decision

```text
Sub-Agent-MCP may structure external execution.
Hermes may call it as an adapter candidate.
OpenWebUI may expose bounded agent tools.
Pantheon must never treat its agent registry, responses or tool availability as governance authority.
```

## Allowed Pantheon distillation

Pantheon may distill the following patterns:

| Sub-Agent-MCP pattern | Pantheon distillation |
|---|---|
| one YAML agent -> one MCP tool | capability exposure candidate, not authorization |
| per-agent system prompt | role-scoped execution prompt candidate, not Pantheon Role authority |
| per-agent MCP servers | scoped tool perimeter candidate |
| `tool_allowlist` | execution-runtime tool budget signal |
| parent agent delegation | external decomposition pattern under Task Contract |
| OpenAPI tool route | exposure-surface adapter pattern, not cockpit authority |
| returned `{ response }` | raw result requiring Pantheon envelope before governance use |
| returned `{ error }` | runtime failure signal, not governance status |

## Forbidden imports

Pantheon must not import:

- Sub-Agent-MCP as a Pantheon runtime;
- YAML agent configuration as doctrine;
- MCP tool availability as capability authorization;
- a sub-agent answer as validated truth;
- a sub-agent completion as approval;
- a sub-agent prompt as Pantheon Role authority;
- a downstream MCP allowlist as sufficient governance scope;
- OpenAPI route exposure as delivery approval;
- LangChain agent state as Evidence Pack;
- runtime logs as proof by themselves;
- tool response text as Canonical Memory;
- automatic selection of sub-agents as hidden Governance College procedure;
- any external-action tool call without an explicit approval gate.

## Risk analysis

### Runtime drift

High risk.

Sub-Agent-MCP is a real runtime. Installing or embedding it inside Pantheon would make Pantheon run sub-agents, manage MCP tool exposure and orchestrate execution.

Safe posture:

```text
Sub-Agent-MCP belongs only behind Hermes or another approved execution runtime boundary.
```

### Authorization drift

High risk.

The repository registers one MCP tool per configured agent. In Pantheon terms, registration is not authorization.

Safe posture:

```text
MCP availability != task authorization.
Configured agent != approved capability.
```

A Sub-Agent-MCP agent may be `detected`, `candidate` or `sandbox_enabled`. It is never `task_authorized` merely because it exists in YAML.

### Evidence drift

Medium risk.

The current success response shape is essentially raw text.

Safe posture:

```text
{ response } -> Result Candidate
selected sources / logs / traces -> Evidence Pack Candidate
```

Sub-Agent-MCP output requires a Pantheon-compatible envelope before it can be reviewed as governed work.

### Approval drift

High risk.

A parent LLM may call a specialized sub-agent and receive a confident answer. That answer is not an approval.

Safe posture:

```text
Sub-agent completion may trigger review.
It does not grant approval.
```

### Memory drift

High risk.

A sub-agent may infer reusable facts, preferences, dossier assumptions or operational lessons.

Safe posture:

```text
Sub-agent output may propose Memory Candidates.
It cannot create Canonical Memory.
```

### Scope drift

Medium risk.

Downstream MCP servers can expose filesystem, search or other tools. Without a Task Contract and Context Pack, the sub-agent may over-read, over-send or cross dossier boundaries.

Safe posture:

```text
Every call must be bound by Task Contract, Context Pack, allowed tools, forbidden tools, approval ceiling and memory rule.
```

## Pantheon / Hermes / OpenWebUI split

| Layer | Allowed | Forbidden |
|---|---|---|
| Pantheon | boundary doctrine, manifest expectations, envelope requirement, approval and memory rules | MCP server, sub-agent runtime, YAML runtime registry, plugin manager, provider router |
| Hermes | optional caller of Sub-Agent-MCP under Task Contract | approval authority, memory promotion, doctrine mutation, uncontrolled external action |
| OpenWebUI | thin tool exposure, status display, Evidence Pack Candidate display, User Decision Gate capture | hidden sub-agent orchestration, automatic sending, automatic approval, automatic memory promotion |

## Minimum compatibility envelope

A Pantheon-compatible adapter around Sub-Agent-MCP must not return raw text as the only review object.

Minimum output shape:

```text
Task Contract in
-> Sub-Agent-MCP adapter
-> Result Candidate + Evidence Pack Candidate out
```

Minimum governed fields:

```yaml
result_candidate:
  status: candidate
  agent_id:
  task_contract_id:
  response:
  assumptions: []
  open_questions: []
  limitations: []

evidence_pack_candidate:
  sources: []
  tool_calls: []
  traces: []
  contradictions: []
  missing_evidence: []

governance:
  approval_required: C0-C5
  memory_behavior: none | candidate_only | never_canonical
  scope:
  forbidden_actions_attempted: []
```

This shape is documentary only. It is not an executable schema.

## Candidate use cases

### Source auditor

Purpose:

```text
Check whether cited sources are current, relevant and sufficient.
```

Required posture:

```text
no final truth
no delivery
Evidence Pack Candidate only
```

### Evidence builder

Purpose:

```text
Assemble source excerpts, assumptions, contradictions and missing proof for review.
```

Required posture:

```text
candidate pack only
no proof status by itself
```

### Architecture domain reviewer

Purpose:

```text
Apply architecture-domain review angles to a dossier output candidate.
```

Required posture:

```text
professional method projection only
no professional advice authority
human architect decides
```

### Memory candidate reviewer

Purpose:

```text
Identify what might be worth remembering, under which scope and review horizon.
```

Required posture:

```text
Memory Candidate only
no Canonical Memory creation
```

## Adoption posture

Current recommendation:

```text
watch + distill + test externally only
```

Do not install in Pantheon.

If tested, test outside this repository as an adapter candidate with one low-risk agent first:

```text
source_auditor
```

The test must prove:

- Task Contract input is mandatory;
- raw prompt-only calls are rejected or wrapped;
- allowed and forbidden tools are explicit;
- response is downgraded to Result Candidate;
- Evidence Pack Candidate is returned or missing evidence is declared;
- no external action can occur without approval;
- no memory can be promoted.

## Boundary phrase

```text
Sub-Agent-MCP may delegate execution.
It does not authorize capability, truth, memory, approval or action.
Runtime may propose.
Pantheon governs eligibility, proof, status and approval.
The human decides.
```
