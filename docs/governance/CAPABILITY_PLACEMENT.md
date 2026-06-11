# Capability Placement

Status: active support doctrine — capability placement, future integration boundaries and non-runtime architecture.

This document defines where capabilities should live when Pantheon Next uses OpenWebUI, Hermes Agent, Langflow, LangGraph, Langfuse, GraphRAG or another external system.

It does not implement an integration, install a dependency or create runtime behavior.

It does not create a bridge, endpoint, queue, scheduler, provider router, plugin registry, MCP runtime, observability backend, GraphRAG runtime, LangGraph runtime, Langflow runtime, OpenWebUI Function, OpenWebUI Tool, OpenWebUI Pipe, OpenWebUI Filter, OpenWebUI Action, OpenWebUI Pipeline or Hermes skill.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Core rule

```text
A capability belongs where its primary effect belongs.
```

- governance effect -> Pantheon doctrine;
- user visibility or decision capture -> OpenWebUI;
- external execution -> Hermes or another external runtime under Task Contract;
- deterministic preparation -> Langflow candidate;
- durable interruptible execution -> LangGraph candidate behind Hermes or a governed bridge;
- trace observation -> Langfuse or another observability layer;
- relationship discovery or provenance linking -> GraphRAG / provenance graph candidate.

If a capability changes legitimacy, memory, approval, scope, doctrine or external effect, Pantheon governance remains the authority.

## Placement by layer

### Pantheon Next

Pantheon owns doctrine, role definitions, Task Contract rules, Context Pack rules, Evidence Pack rules, approval rules, memory promotion rules, scope isolation rules, external tools policy, placement rules, prompt placement rules, integration boundaries, reference reviews, rejected patterns and persistent tensions.

Pantheon must not own an agent runtime, tool runtime, workflow runtime, provider router, scheduler, queue, message bus, plugin manager, skill installer, MCP runtime, observability backend, GraphRAG runtime, LangGraph central runtime, Langflow runtime, OpenWebUI plugin execution or Hermes internal runtime state.

### OpenWebUI

OpenWebUI owns the cockpit surface.

Allowed posture:

```text
show
select
label
warn
collect decision
request revision
request more evidence
open User Decision Gate
display Evidence Pack
display Task Contract
display candidate status
display scope warning
request Hermes execution under contract
```

OpenWebUI must not become a Registre Probatoire entry, source of truth, governance authority, runtime authority, unrestricted knowledge gateway, free plugin manager, provider router, scheduler, hidden workflow runner, automatic approval surface or automatic memory promoter.

OpenWebUI Functions, Tools, Pipes, Filters, Actions and Pipelines are capability surfaces only. They are not authorized merely because OpenWebUI can host them.

### Pantheon Bridge candidate

A future bridge may adapt a governed request into bounded external execution. It may check that Task Contract, Context Pack, approval ceiling, memory rule and evidence expectation exist before dispatch.

The bridge is a boundary adapter. It must not become agent runtime, workflow runtime, tool runtime, provider router, queue, scheduler, approval engine, memory promotion engine or hidden orchestrator.

### Governed execution handoff

A governed execution handoff is the boundary object a bridge or exposure surface may prepare before asking an execution runtime to act.

It is not a queue item, worker assignment, scheduler record, provider route, workflow state or executable instruction owned by Pantheon. It is a legitimacy package: the runtime may read it; Pantheon does not run it.

Minimum shape:

```text
governed_execution_handoff:
  handoff_id:
  linked_task_contract:
  linked_context_pack:
  decision_gate:
  approval_ref:
  scope:
  target_runtime: execution_runtime
  requested_effect: read_only | internal_state_change | external_effect | canonical_effect
  action_family:
  target:
    kind:
    ref:
  allowed_inputs:
  forbidden_effects:
  expected_result_candidate:
  expected_evidence_pack_candidate:
  outcome_observation_expected: true
  idempotency_key:
  trace_refs:
```

The handoff is valid only when:

```text
1. the linked Task Contract identifies scope, allowed outputs, forbidden outputs, register rules and approval ceiling;
2. the linked Context Pack exists, or the task explicitly records that no Context Pack is required;
3. the requested effect is classified before dispatch;
4. expected Result Candidate and Evidence Pack Candidate outputs are named;
5. any external effect has an explicit approval path;
6. any canonical effect is refused as runtime work and routed to the governed validation path;
7. an idempotency key and trace references exist for every non-read-only effect.
```

Effect classes:

| Requested effect | Meaning | Pantheon rule |
|---|---|---|
| `read_only` | observe, extract, compare, search, summarize | may proceed when the Task Contract allows it and provenance is preserved |
| `internal_state_change` | create a draft, candidate artifact, candidate status or review item | allowed only as candidate state; not validation |
| `external_effect` | send, publish, file, notify, modify an external system or commit to a third party | requires explicit approval and the User Decision Gate where relevant |
| `canonical_effect` | create or modify doctrine, approval status, a Registre Probatoire entry or another validated state | never executable by the runtime; requires the governed validation path |

The return path must not collapse transport success, task success and governance status. A valid runtime return separates at least:

```text
handoff_delivery_status: not_sent | sent | refused | failed | timeout
runtime_task_status: not_started | success | partial | failed | blocked | unknown
governance_result_status: candidate | to_verify | approved | rejected | blocked
```

A successful runtime response is not proof, approval, professional validation, canonization, transmission authority or memory promotion. It is reviewable evidence and candidate output.

If a bridge or surface cannot produce a valid handoff, the safe result is a visible Capability Gap, not an improvised execution.

### Hermes Agent

Hermes owns external execution. Hermes may host profiles, skills, tools, toolsets, workers, controlled terminal operations, repository read and patch candidates, source audit work, file conversion work, document extraction work, browser or search work, Evidence Pack candidate preparation, Register Candidate proposal and Capability Gap signaling.

Hermes must return candidates. Hermes must not approve, canonize, promote memory, mutate doctrine, merge code directly or bypass approvals.

### Langflow candidate

Langflow may support deterministic preparation: source extraction, redaction preparation, Context Pack skeletons, Evidence Pack skeletons, document chunking review, format normalization and repeatable preprocessing.

Langflow must not grant approval, own a Registre Probatoire entry, execute Pantheon Roles, run the Governance College, hide workflow authority or resolve dossiers autonomously.

### LangGraph runtime candidate

LangGraph may be considered only for external long-running, interruptible or checkpoint-heavy execution behind Hermes or a governed bridge.

LangGraph state is Runtime State. It is not Evidence Pack, a Registre Probatoire entry, approval or doctrine.

### Langfuse candidate

Langfuse may observe model, tool and execution traces. It may record metadata useful for audit support. It must not become Evidence Pack, a Registre Probatoire entry, approval record, doctrine source or runtime authority.

### GraphRAG or provenance graph candidate

A graph layer may support relationship discovery, provenance linking and contradiction review. It may link sources, claims, chunks, entities, Task Contracts, Context Packs, Evidence Items, Evidence Packs, Output Candidates, Register Candidates, a Registre Probatoire entry, approvals, contradictions and run references.

The graph must not decide truth. Connectivity is not approval. Retrieval from a graph is not evidence until selected and represented in an Evidence Pack.

## Placement matrix

| Capability | Pantheon | OpenWebUI | Hermes | Langflow | LangGraph | Langfuse | Graph / GraphRAG |
|---|---|---|---|---|---|---|---|
| Doctrine | owns | displays excerpts | receives constraints | receives constraints | receives constraints | observes refs | links refs |
| Task Contract | owns | displays / captures candidate | consumes | consumes | consumes | traces id | links id |
| Context Pack | owns rules | selects / displays | consumes | may prepare candidate | consumes | traces id | links scope |
| Governed execution handoff | owns rules | prepares / displays / captures approval | consumes under contract | no | may consume only behind runtime | observes refs | links refs |
| Evidence Pack | owns rules | displays | produces candidate | may skeletonize | may support long run | observes traces | links evidence |
| Approval | owns rules | captures explicit action | reports need | never grants | may interrupt | observes | links decision |
| User Decision Gate | owns format | exposes | reports conflict | never resolves | may pause before gate | observes | links conflict |
| Register Candidate | owns rules | displays / review surface | may propose | may propose candidate | may pause | observes | links claim |
| a Registre Probatoire entry | owns | displays scoped excerpt | consumes approved excerpt | never owns | never owns | observes ref | may link approved item |
| Source audit | defines rules | displays result | executes | may preprocess | only if long | observes | enriches provenance |
| Repository patch candidate | defines rules | requests / displays | executes candidate | not default | if long / interruptible | observes | links change |
| RAG ingestion candidate | defines boundaries | selects sources | executes or delegates | may run deterministic flow | if long | observes | indexes / links |
| UI action | defines legitimacy | hosts thin action | receives request | no | no | observes | no |
| Workflow long run | defines boundary | displays status | executes | may be subflow | checkpoint runtime | observes | links milestones |

## Rejected collapses

```text
OpenWebUI Function = Pantheon runtime
OpenWebUI Knowledge = Registre Probatoire entry
Hermes profile = Pantheon Role authority
Hermes completion = approval
Langflow flow = governed decision
LangGraph checkpoint = memory
Langfuse trace = Evidence Pack
GraphRAG relation = proof
MCP availability = tool authorization
plugin installed = capability approved
operations file = governing spec
handoff delivered = task validated
runtime success = governance approval
```

## Operations boundary

```text
Spec first.
Operations second.
Execution elsewhere.
```

No file under `operations/` may be created or modified before a governing documentation spec has been explicitly validated.

The governing spec must define the scope, status, authority, required evidence, approval conditions, external-action limits, human responsibility and exit criteria for the operational procedure.

`operations/` may only translate validated governance into procedural guidance. It must not invent doctrine, promote candidates, define runtime behavior, bypass approval, create hidden workflow authority or become a scheduler, queue, execution engine, approval engine or memory mechanism.

Until a governing spec is validated, any proposed `operations/` content remains a candidate discussion item outside `operations/`.

## Architectural pattern references

External architectural pattern catalogues may be used as vocabulary aids, not as Pantheon doctrine.

They can help name architectural forces such as orchestration, microkernel, plugin systems, middleware, pipelines, gateways, shared repositories, event flows, observability layers or provenance graphs.

Naming a pattern does not authorize Pantheon to implement it.

If a pattern implies execution, routing, scheduling, queueing, plugin loading, durable work, automatic approval, automatic memory promotion or external side effects, it belongs outside Pantheon.

Pantheon may govern the boundary of such a pattern through Task Contracts, manifests, roles, evidence, statuses, approvals, memory rules and action boundaries.

Reference catalogues such as architectural metapatterns are non-normative. They help identify placement risks; they do not override Pantheon governance documents.

## Evolution phases

### Phase 1 — documentation and templates

Allowed now: placement doctrine, prompt placement doctrine, bridge contract doctrine, non-executable templates and AI logs.

Not allowed by this phase: runtime bridge, OpenWebUI executable extension, Hermes skill installation, Langflow deployment, LangGraph runtime, Docker or operations changes.

### Phase 2 — thin cockpit to Hermes

Future candidate: OpenWebUI thin Action, Pantheon Bridge candidate, Hermes profile and skill under Task Contract, Evidence Pack Candidate return and User Decision Gate display.

### Phase 3 — external preparation and observability

Future candidate: Langflow headless preparation flows, Langfuse trace metadata, read-only provenance graph and Hermes skill candidates for source audit and evidence building.

### Phase 4 — durable interruptible external execution

Future candidate: LangGraph behind Hermes or bridge, human interrupt exposure in OpenWebUI, checkpoint / resume under unchanged Task Contract and Evidence Pack Candidate return.

## Final rule

```text
Pantheon does not own the engines.
Pantheon owns the rules that decide what an engine may do,
what its output is worth,
and what may remain.
```
