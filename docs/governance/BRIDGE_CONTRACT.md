# Bridge Contract

Status: active support doctrine — future bridge boundary and non-runtime adapter contract.

This document defines the governance boundary for a future non-authoritative Pantheon Bridge between the Pantheon policy service, Hermes Agent / the external runtime, optional compatible runtime clients, Pantheon Cockpit projections and optional external systems such as Langflow, LangGraph, Langfuse or a provenance graph.

It does not implement a bridge.

It does not create an API, endpoint, scheduler, queue, message bus, provider router, tool runtime, workflow runtime, Policy Decision Point, Policy Enforcement Point, approval engine, memory engine, runtime-client component, Hermes skill, Langflow flow, LangGraph runtime, Langfuse backend or GraphRAG runtime.

Runtime/client/authority placement is inherited from `HERMES_INTEGRATION.md`: the Pantheon policy service is the bounded PDP, Hermes/the external runtime is the executor and PEP, optional runtime clients expose interaction only, Pantheon Cockpit projects governed state, and Pantheon retains governance authority.

## Purpose

A bridge may later be needed to adapt governed requests and policy decisions between Pantheon and external execution systems without making any client, adapter or transport layer authoritative.

The bridge exists to preserve boundary discipline.

It adapts a governed request into an external execution request, conveys the applicable Pantheon policy decision to the runtime/PEP, and translates returned material back into reviewable candidates.

It does not execute the work itself.

It does not decide whether a consequential effect is authorized.

## Core rule

```text
The bridge may adapt and convey a contract or policy decision.
The bridge must not become a runtime, PDP or PEP.
```

A bridge may perform non-authorizing structural preflight such as checking that required request fields and references are present before consulting policy. It may refuse to forward a malformed or structurally incomplete adapter request.

Only the Pantheon policy service may issue the bounded PDP disposition for a consequential effect. The bridge may report that disposition unchanged and must never widen it. If policy is unavailable or invalid, the bridge reports that state; the external runtime/PEP remains responsible for fail-closed enforcement of the consequential effect.

A bridge must not decide truth, grant approval, promote memory, broaden scope or authorize external effect by itself.

## Allowed bridge responsibilities

A future bridge may:

```text
receive a bounded execution request from an authorized caller or optional runtime client
verify required request fields and governance references are present
refuse to forward a malformed or structurally incomplete adapter request
prepare a deterministic Pantheon policy-service request
report policy unavailable or invalid without converting that state into allow
convey the Pantheon PDP disposition without widening it
select an executor class only within the returned policy constraints
prepare a bounded Hermes request
prepare a bounded Langflow request when explicitly allowed
attach trace metadata for observability
normalize returned candidates
return runtime-interaction status to the requesting client when applicable
provide governed status material for Pantheon Cockpit projection
surface Capability Gap
surface User Decision Gate need
```

These are boundary checks and adapter operations.

They are not autonomous execution, policy decision or consequential-effect enforcement.

## Forbidden bridge responsibilities

A bridge must not:

```text
act as a second Policy Decision Point
widen a Pantheon policy disposition
claim fail-closed enforcement of the consequential effect
execute agent loops
run tools directly
perform the consequential effect as Policy Enforcement Point
route providers as a sovereign layer
schedule jobs by itself
own queues
own workflow state
own memory
approve output
promote a Registre Probatoire entry
merge code
deploy systems
send external communications
auto-install skills
auto-enable plugins
resolve role disagreement silently
```

If the bridge independently decides that an effect may proceed, a competing PDP has been created.

If the bridge claims responsibility for enforcing the consequential effect, a competing PEP has been created.

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

This envelope is not a runtime task or an authorization decision.

It is a boundary declaration supplied to the Pantheon policy check and external execution adapter.

## Authorized executor classes

Candidate executor classes may include:

```text
hermes_profile
hermes_skill_candidate
langflow_flow_candidate
langgraph_runtime_candidate
read_only_provenance_query
observability_trace_sink
```

An executor class is not authorized merely because it is installed or named in this document.

Task-bound eligibility comes from the applicable Pantheon PDP disposition and is enforced by the external runtime/PEP.

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
adapter_status
outcome_observation_candidate
```

Returned material remains candidate until governed review.

A technically successful bridge/runtime return is not Evidence, approval or professional acceptance.

## Status vocabulary

Recommended bridge-facing statuses:

```text
policy_check_required
policy_unavailable
policy_invalid
request_not_forwarded_structural_invalid
pdp_disposition_received
eligible_for_executor_handoff
eligible_with_gate
returned_candidate
returned_with_risk
returned_capability_gap
human_decision_required
```

These statuses report adapter or policy-observation state.

They are not execution commands, they do not replace the canonical PDP disposition vocabulary, and they do not claim PEP enforcement. Detailed deny, revision, evidence or gate reasons should be conveyed from the Pantheon policy result rather than reinvented by the bridge.

## Runtime-client relationship

An optional compatible runtime client may request a bounded bridge operation or display runtime-interaction state when a deployed binding supports it.

The client may expose:

```text
request candidate execution
show policy or adapter reason
show runtime status label
show returned candidate references
show Capability Gap
```

A runtime client must not use the bridge to bypass Pantheon policy or turn UI state into approval.

Governed Evidence gaps, approval state and User Decision Gates belong to Pantheon Cockpit projection, not to client authority.

## Pantheon Cockpit relationship

Pantheon Cockpit may project governed Cards, policy/gate reasons, Evidence gaps, policy/gate state and human decision surfaces derived from governed artifacts.

Cockpit projection does not execute the bridge, persist authority by itself or replace the Pantheon policy decision.

## Hermes relationship

Hermes/the external runtime may receive bounded requests after the applicable Pantheon policy disposition permits the execution opportunity or required gate path.

The runtime/PEP is responsible for fail-closed behavior when required policy is unavailable or invalid, enforcing consequential-effect policy, and performing the effect only when allowed.

Hermes may return candidates, evidence notes, patch candidates, memory candidates, gaps, risks and truthful technical outcome observations.

Hermes completion does not equal approval or Evidence.

## Langflow relationship

Langflow may be called by a future bridge only for deterministic preparation or extraction flows explicitly admitted by the applicable policy and Task Contract.

Langflow output must remain candidate material.

## LangGraph relationship

LangGraph may be used only for durable external execution when interruption, checkpoint or resume are explicitly required and admitted.

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
Pantheon policy service decides the bounded policy disposition as PDP.
The bridge adapts, reports and conveys without widening authority.
Hermes or another admitted external runtime fail-closes, enforces and executes as PEP.
Optional runtime clients expose interaction only.
Pantheon Cockpit projects governed state.
The human decides consequential effects when required.
```
