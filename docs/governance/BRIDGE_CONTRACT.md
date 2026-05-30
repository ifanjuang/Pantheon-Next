# Bridge Contract

Status: active support doctrine — future bridge boundary and non-runtime adapter contract.

This document defines the governance boundary for a future Pantheon Bridge between OpenWebUI, Pantheon doctrine, Hermes Agent and optional external systems such as Langflow, LangGraph, Langfuse or a provenance graph.

It does not implement a bridge.

It does not create an API, endpoint, scheduler, queue, message bus, provider router, tool runtime, workflow runtime, approval engine, memory engine, OpenWebUI Function, Hermes skill, Langflow flow, LangGraph runtime, Langfuse backend or GraphRAG runtime.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A bridge may later be needed because OpenWebUI should not speak directly to every execution system without governance context.

The bridge exists to preserve boundary discipline.

It translates a governed request into an external execution request and translates the returned material back into reviewable candidates.

It does not execute the work itself.

## Core rule

```text
The bridge may adapt a contract.
The bridge must not become a runtime.
```

A bridge may check whether required governance artifacts exist.

A bridge must not decide truth, grant approval, promote memory, broaden scope or authorize external effect by itself.

## Allowed bridge responsibilities

A future bridge may:

```text
receive a request from OpenWebUI
verify Task Contract presence
verify Context Pack presence
verify scope labels
verify approval ceiling
verify memory rule
verify expected evidence
verify allowed output categories
select an authorized external executor class
prepare a bounded Hermes request
prepare a bounded Langflow request when explicitly allowed
attach trace metadata for observability
normalize returned candidates
return status to OpenWebUI
surface Capability Gap
surface User Decision Gate need
```

These are boundary checks and adapter operations.

They are not autonomous execution.

## Forbidden bridge responsibilities

A bridge must not:

```text
execute agent loops
run tools directly
route providers as a sovereign layer
schedule jobs by itself
own queues
own workflow state
own memory
approve output
promote Canonical Memory
merge code
deploy systems
send external communications
auto-install skills
auto-enable plugins
resolve role disagreement silently
```

If the bridge owns durable execution state, governance drift has occurred.

If the bridge is necessary to understand why a result is valid, the Evidence Pack is insufficient.

## Required input envelope

A governed bridge call should include or reference:

```text
request_id
task_contract_id
context_pack_id
requested_executor_class
allowed_outputs
forbidden_outputs
scope
approval_ceiling
memory_rule
expected_evidence
external_effect_policy
user_decision_gate_policy
trace_policy
```

This envelope is not a runtime task.

It is a boundary declaration.

## Authorized executor classes

Allowed executor classes may include:

```text
hermes_profile
hermes_skill_candidate
langflow_flow_candidate
langgraph_runtime_candidate
read_only_provenance_query
observability_trace_sink
```

An executor class is not authorized merely because it is installed.

Authorization remains task-bound.

## Return envelope

A bridge return should normalize external output into:

```text
result_candidate
evidence_pack_candidate
memory_candidate
patch_candidate
capability_gap
risk_escalation
user_decision_gate_needed
trace_reference
blocked_status
```

Returned material remains candidate until governed review.

## Status vocabulary

Recommended bridge statuses:

```text
accepted_for_external_execution
blocked_missing_task_contract
blocked_missing_context_pack
blocked_scope_unclear
blocked_approval_ceiling_unclear
blocked_memory_rule_missing
blocked_executor_not_authorized
blocked_external_effect
blocked_evidence_requirement_missing
returned_candidate
returned_with_risk
returned_capability_gap
human_decision_required
```

These statuses are governance-facing.

They are not execution commands.

## OpenWebUI relationship

OpenWebUI may request bridge action through a thin surface.

The surface may expose:

```text
request execution
show blocked reason
show run status label
show Evidence Pack Candidate
show User Decision Gate
show Capability Gap
```

OpenWebUI must not use the bridge to bypass Pantheon doctrine.

## Hermes relationship

Hermes may receive bounded requests from the bridge.

Hermes may return candidates, evidence notes, patch candidates, memory candidates, gaps and risks.

Hermes completion does not equal approval.

## Langflow relationship

Langflow may be called by a future bridge only for deterministic preparation or extraction flows explicitly authorized by Task Contract.

Langflow output must remain candidate material.

## LangGraph relationship

LangGraph may be used only for durable external execution when interruption, checkpoint or resume are explicitly required.

LangGraph state remains Runtime State.

It is not Evidence Pack, approval or memory.

## Langfuse relationship

Langfuse may receive trace metadata.

Trace metadata can help review, but it does not replace Evidence Pack structure.

## Graph relationship

A graph layer may answer read-only provenance or relationship queries.

Graph output remains Retrieved Knowledge or candidate evidence until selected into an Evidence Pack.

## Final rule

```text
The bridge checks whether execution is allowed.
Hermes or another external runtime performs execution.
Pantheon governs what the result means.
OpenWebUI shows the result and captures the human decision.
```
