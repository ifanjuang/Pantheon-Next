# AI log — tripartite interface, MCP V0 and refusal fixtures

Date: 2026-07-02.

Actor: ChatGPT.

## Intent

Document the practical interfaces between OpenWebUI, Hermes Agent, Pantheon governance and the optional Pantheon MCP policy surface after review of OpenWebUI v0.10.0, Hermes Agent v0.17.0/post-release updates and the current Pantheon Next status spine.

The user accepted the proposed improvement set:

```text
1. TRIPARTITE_INTERFACE_SPEC.md
2. MCP_PANTHEON_MINIMAL_V0.md
3. REFUSAL_FIXTURES.md
```

## Sources checked

Active doctrine read before the change:

```text
docs/governance/STATUS.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/DOMAIN_PACK_SPEC.md
docs/governance/ADAPTERS_AND_BINDINGS.md
docs/governance/TASK_CONTRACTS.md
docs/governance/MCP_POLICY_SERVER_CANDIDATE.md
docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md
docs/governance/WHAT_RUNS.md
```

Related PR / discussion signals checked:

```text
#75  MCP policy server roadmap: accepted direction, but candidate / to verify; MCP must not substitute for Task Contract; memory wording must align to Registre Probatoire.
#102 first mcp-server slice: read-only resources and validation tools; refusal posture for send/write/merge/approve/promote/install/schedule/route/execute.
#106 Hermes integration contract and fixtures: Phase 5-6 fixtures, refusal lexicon issue, merged.
#259 B-3 phase 1 vertical slice: accepted / merged as governed dossier and read-only validation, not runtime.
#248 / #251 MCP alignment: mcp-server is read-only verification surface, not UI, runtime or approval engine.
```

## Change

Added three governance documents:

```text
docs/governance/TRIPARTITE_INTERFACE_SPEC.md
docs/governance/MCP_PANTHEON_MINIMAL_V0.md
docs/governance/REFUSAL_FIXTURES.md
```

### `TRIPARTITE_INTERFACE_SPEC.md`

Defines the data objects exchanged between layers:

```text
intent_candidate
context_pack
task_contract
policy_decision
governed_execution_handoff
runtime_return
result_candidate
evidence_pack_candidate
memory_or_register_candidate
user_decision_gate
capability_gap
trace_spine
```

Boundary: interface grammar only. It implements no API, endpoint, bridge, runtime, scheduler, queue, OpenWebUI extension, Hermes skill or MCP tool.

### `MCP_PANTHEON_MINIMAL_V0.md`

Defines the smallest acceptable MCP Pantheon posture:

```text
read-only resources
validation-only tools
candidate skeletons / reports
no external actions
no approval engine
no memory promotion
no provider routing
```

It uses Registre/Evidence-oriented wording rather than canonical-memory language and keeps Hermes as the runtime.

### `REFUSAL_FIXTURES.md`

Defines refusal probes for future MCP, Hermes adapter and OpenWebUI gate tests.

Covered motifs include:

```text
send without approval
write/delete without governed handoff
merge without review
runtime success treated as approval
automatic memory promotion
automatic Registre entry
retrieval treated as proof
cross-project context leakage
unpassport external MCP tool
global skill install
scheduler without scope/expiry
provider routing without minimization
Pantheon running shell
external professional position without evidence
candidate treated as deliverable
health check treated as authorization
runtime approval callback treated as Zeus
```

## Boundary

Documentation only. No protected paths changed.

No changes to:

```text
schemas/
tests/
pyproject.toml
operations/
platform/
Docker
.env
CLAUDE.md
mcp-server/
GitHub Actions
```

The added documents are candidate support doctrine / documented non-implemented.

## Status

```text
Implemented: no.
Documented non-implemented: yes.
Partial: no runtime change.
To verify: adapter mapping to OpenWebUI v0.10.0, Hermes Agent v0.17.0 and existing mcp-server surface.
To arbitrate: promotion status and whether refusal fixtures later become executable tests.
```

## Decision classification

```text
Accepted: interface grammar, minimal MCP profile and refusal fixture catalog.
Refused: Pantheon MCP as runtime, action server, approval engine, memory promotion engine or provider router.
To verify: exact integration with existing mcp-server read-only artifacts.
To arbitrate: final authority status and index promotion.
```
