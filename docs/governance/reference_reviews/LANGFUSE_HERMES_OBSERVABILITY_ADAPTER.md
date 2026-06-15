# Langfuse / Hermes Observability Adapter

Status: external reference / support review — candidate observability placement, documented non-implemented.

This document records how Langfuse may be used with Hermes and the Pantheon Dashboard.

It does not install Langfuse, add Docker Compose, modify `operations/`, create a platform service, create a trace collector, add SDK code, add a schema, create an approval engine, create a memory engine, create an Evidence Pack authority, create a workflow builder or authorize external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## External reference

Langfuse is an open-source AI engineering and LLM observability platform. Its repository describes support for observability, metrics, prompt management, playgrounds, datasets and evaluations, with integrations including OpenTelemetry, LangChain, OpenAI SDK and LiteLLM.

The official Langfuse self-hosting documentation states that Docker Compose is the simplest way to run Langfuse locally or on a VM for a first deployment, while high-availability and high-throughput deployments should use Kubernetes/Helm or another production deployment route.

Reference URLs:

```text
https://langfuse.com/self-hosting/deployment/docker-compose
https://github.com/langfuse/langfuse
https://github.com/langfuse/langfuse/blob/main/docker-compose.yml
```

## Placement

Langfuse belongs to the observability layer.

Hermes remains the execution runtime.

The Dashboard may expose links, status cards or read-only embedded views.

Pantheon governs status, evidence, approval, scope and memory.

```text
Hermes executes.
Langfuse observes.
The Dashboard exposes.
Pantheon governs what may be believed, approved, remembered or acted on.
```

## Accepted

Accepted as a candidate external adapter pattern:

- Hermes may emit traces to Langfuse for model calls, tool calls, latency, cost, errors and sessions.
- Hermes may attach governance metadata to traces when available.
- The Dashboard may show a Langfuse connection status, health indication and link to the Langfuse UI.
- The Dashboard may show read-only trace summaries linked to a Task Contract, Result Candidate, Evidence Pack Candidate or User Decision Gate.
- Langfuse traces may support audit review and Evidence Pack Candidate construction.

Recommended metadata keys:

```text
task_contract_id
dossier_id
case_id
run_id
result_candidate_id
evidence_pack_candidate_id
approval_gate_id
requested_effect
approval_ceiling
memory_behavior
scope
```

## Refused

Refused as Pantheon authority or runtime:

- Langfuse trace = proof;
- Langfuse score = validation;
- Langfuse dataset = canonical memory;
- Langfuse prompt = doctrine;
- Langfuse success = approval;
- Langfuse experiment = professional decision;
- Langfuse UI action = external-action authorization;
- Langfuse service = Pantheon runtime.

A trace may help review a candidate. It must not become the Evidence Pack, the Registre Probatoire entry, the approval record or the source of truth.

## Dashboard projection

The Dashboard may expose a module such as:

```text
Observability
  Langfuse
    configured: true | false
    health: unknown | reachable | degraded | unavailable
    ui_url:
    last_trace_refs:
    open_ui_action: external_link
```

For a dossier or task, the Dashboard may show:

```text
Trace available
Execution completed / partial / failed / blocked
Result Candidate produced
Evidence Pack Candidate available / missing
Validation required
External action not authorized unless explicitly approved
Canonical memory unchanged unless validated
```

The Dashboard must not collapse runtime success and governance status.

Minimum distinction:

```text
handoff_delivery_status: not_sent | sent | refused | failed | timeout
runtime_task_status: not_started | success | partial | failed | blocked | unknown
governance_result_status: candidate | to_verify | approved | rejected | blocked
```

## Installation posture

A practical deployment may install Langfuse beside Hermes or on the same internal host, but that deployment belongs outside this governance document.

Permitted future implementation package, subject to separate approval:

```text
Hermes / external runtime configuration
Langfuse service deployment
Dashboard external link / health card
trace metadata adapter
```

Not permitted in this document:

```text
Docker changes
operations runbook
platform service
.env secrets
schema changes
tests
runtime code
```

Those paths require a separate work package and explicit approval.

## Relationship with AgentCanvas / Evidence Canvas

AgentCanvas-style views and Langfuse traces answer different parts of the same need.

```text
Langfuse stores and displays observability traces.
AgentCanvas-style views may visualize a run graph.
Evidence Canvas, if created later, qualifies the governance status of candidates and evidence.
```

None of these replaces Pantheon authority.

## To verify

- Which Hermes execution path will emit Langfuse traces first.
- Whether traces should be emitted through OpenTelemetry, SDK integration or an adapter wrapper.
- Which metadata keys are stable enough to require across all traces.
- Which trace fields must be redacted before Dashboard display.
- Whether Dashboard access should be link-only first, before any embedded read-only view.
- Whether a generic Trace Candidate contract is needed before deeper Evidence Canvas work.

## To arbitrate

- Deployment mode for the first internal test: Docker Compose beside Hermes, standalone VM, or existing service host.
- Authentication and access policy for the Langfuse UI.
- Retention period for traces that may contain professional or client-sensitive data.
- Whether prompt management and datasets stay unused initially to avoid confusing observability with doctrine or memory.

## Boundary phrase

```text
Langfuse observes the run.
Hermes carries the work.
The Dashboard exposes the trace.
Pantheon qualifies the status.
The human decides.
```
