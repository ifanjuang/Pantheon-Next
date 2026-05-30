# Capability Placement

Status: active support doctrine — capability placement, future integration boundaries and non-runtime architecture.

This document defines where a capability should live when Pantheon Next integrates or references OpenWebUI, Hermes Agent, Langflow, LangGraph, Langfuse, GraphRAG or another external system.

It does not implement an integration, install a dependency or create runtime behavior.

It does not create a bridge, endpoint, queue, scheduler, provider router, plugin registry, MCP runtime, observability backend, GraphRAG runtime, LangGraph runtime, Langflow runtime, OpenWebUI Function, OpenWebUI Tool, OpenWebUI Pipe, OpenWebUI Filter, OpenWebUI Action, OpenWebUI Pipeline or Hermes skill.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Next needs a placement rule before executable integration begins.

The same capability can look legitimate in several places.

Example:

```text
source audit
```

It may appear as:

- a Pantheon governance rule;
- an OpenWebUI display panel;
- a Hermes skill;
- a Langflow extraction flow;
- a GraphRAG provenance query;
- a Langfuse trace span.

Those are not equivalent.

Placement defines authority.

## Core rule

```text
A capability belongs where its primary effect belongs.
```

If the primary effect is governance, the capability belongs in Pantheon doctrine.

If the primary effect is user visibility or decision capture, the capability belongs in OpenWebUI.

If the primary effect is external execution, the capability belongs in Hermes or another external runtime under Task Contract.

If the primary effect is deterministic transformation, the capability may belong in Langflow as an external flow candidate.

If the primary effect is durable interruptible execution, the capability may belong in LangGraph behind Hermes or a governed bridge.

If the primary effect is trace observation, the capability belongs in Langfuse or another observability layer.

If the primary effect is relationship discovery or provenance linking, the capability may belong in a GraphRAG or provenance graph layer.

If the capability changes legitimacy, memory, approval, scope, doctrine or external effect, Pantheon governance must remain the authority.

## Layer placement

### Pantheon Next

Pantheon owns:

```text
doctrine
role definitions
Task Contract rules
Context Pack rules
Evidence Pack rules
approval rules
memory promotion rules
scope isolation rules
external tools policy
capability placement rules
prompt placement rules
integration boundaries
reference reviews
rejected patterns
persistent tensions
```

Pantheon must not own:

```text
agent runtime
tool runtime
workflow runtime
provider router
scheduler
queue
message bus
plugin manager
skill installer
MCP runtime
observability backend
GraphRAG runtime
LangGraph central runtime
Langflow runtime
OpenWebUI plugin execution
Hermes internal runtime state
automatic approval
automatic memory promotion
```

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

OpenWebUI must not become:

```text
canonical memory
source of truth
governance authority
runtime authority
unrestricted knowledge gateway
free plugin manager
provider router
scheduler
hidden workflow runner
automatic approval surface
automatic memory promoter
```

OpenWebUI Functions, Tools, Pipes, Filters, Actions and Pipelines are capability surfaces.

They are not authorized merely because OpenWebUI can host them.

### Pantheon Bridge candidate

A future Pantheon Bridge may translate governed user intent into bounded execution requests.

It may validate that required governance artifacts exist.

It may adapt a Task Contract and Context Pack into a Hermes request.

It may normalize a returned candidate into a reviewable envelope.

It must not become:

```text
agent runtime
workflow runtime
tool runtime
provider router
queue
scheduler
approval engine
memory promotion engine
hidden orchestrator
```

The bridge is a boundary adapter.

It is not Pantheon execution.

### Hermes Agent

Hermes owns external execution.

Hermes may host:

```text
profiles
skills
tools
toolsets
workers
controlled terminal operations
repository read and patch candidates
source audit work
file conversion work
PDF and document extraction work
browser or search work
Evidence Pack candidate preparation
Memory Candidate proposal
Capability Gap signaling
```

Hermes must return candidates.

Hermes must not approve, canonize, promote memory, mutate doctrine, merge code directly or bypass approvals.

### Langflow candidate

Langflow may be used as an external deterministic flow engine for bounded preparation tasks.

Good fits:

```text
source extraction
redaction preparation
Context Pack skeleton generation
Evidence Pack skeleton generation
document chunking review
format normalization
repeatable preprocessing
```

Bad fits:

```text
approval
canonical memory
Pantheon role execution
Governance College runtime
hidden workflow authority
autonomous dossier resolution
```

Langflow flows are external capabilities.

They require Task Contract, scope and evidence boundaries when used for governed work.

### LangGraph runtime candidate

LangGraph may be considered only for external long-running, interruptible or checkpoint-heavy execution behind Hermes or a governed bridge.

Good fits:

```text
long-running repository review
interruptible evidence construction
human-in-the-loop execution
checkpoint and resume under unchanged Task Contract
multi-step extraction with recoverable state
```

Bad fits:

```text
Pantheon central runtime
Governance College
role debate engine
automatic approval
automatic memory promotion
provider routing authority
```

LangGraph state is runtime state.

It is not Evidence Pack, Canonical Memory, approval or doctrine.

### Langfuse candidate

Langfuse may observe model, tool and execution traces.

It may record technical metadata useful for audit support.

It must not become:

```text
Evidence Pack
Canonical Memory
approval record
doctrine source
runtime authority
```

Langfuse traces can support review.

They do not replace Evidence Packs.

### GraphRAG or provenance graph candidate

A graph layer may support relationship discovery, provenance linking and contradiction review.

It may represent links between:

```text
source
claim
chunk
entity
Task Contract
Context Pack
Evidence Item
Evidence Pack
Output Candidate
Memory Candidate
Canonical Memory
approval
contradiction
run reference
```

The graph must not decide truth.

Connectivity is not approval.

Retrieval from a graph is not evidence until selected and represented in an Evidence Pack.

## Placement matrix

| Capability | Pantheon | OpenWebUI | Hermes | Langflow | LangGraph | Langfuse | Graph / GraphRAG |
|---|---|---|---|---|---|---|---|
| Doctrine | owns | displays excerpts | receives constraints | receives constraints | receives constraints | observes refs | links refs |
| Task Contract | owns | displays / captures candidate | consumes | consumes | consumes | traces id | links id |
| Context Pack | owns rules | selects / displays | consumes | may prepare candidate | consumes | traces id | links scope |
| Evidence Pack | owns rules | displays | produces candidate | may skeletonize | may support long run | observes traces | links evidence |
| Approval | owns rules | captures explicit action | reports need | never grants | may interrupt | observes | links decision |
| User Decision Gate | owns format | exposes | reports conflict | never resolves | may pause before gate | observes | links conflict |
| Memory Candidate | owns rules | displays / review surface | may propose | may propose candidate | may pause | observes | links claim |
| Canonical Memory | owns | displays scoped excerpt | consumes approved excerpt | never owns | never owns | observes ref | may link approved item |
| Source audit | defines rules | displays result | executes | may preprocess | only if long | observes | enriches provenance |
| Repository patch candidate | defines rules | requests / displays | executes candidate | not default | if long / interruptible | observes | links change |
| RAG ingestion candidate | defines boundaries | selects sources | executes or delegates | may run deterministic flow | if long | observes | indexes / links |
| UI action | defines legitimacy | hosts thin action | receives request | no | no | observes | no |
| Workflow long run | defines boundary | displays status | executes | may be subflow | checkpoint runtime | observes | links milestones |
| Provider routing | forbids Pantheon ownership | not authority | possible Hermes concern | no | no | observes only | no |
| Plugin marketplace | rejects by default | not used for Pantheon | not automatic | no | no | no | no |

## Default placements

Use these defaults unless a Task Contract, Evidence Pack expectation and approval path justify otherwise.

```text
OpenWebUI: cockpit actions and display only
Hermes: execution, skills, tools and candidate production
Langflow: deterministic external preparation flows only
LangGraph: long-running external runtime candidate only
Langfuse: observability only
GraphRAG: provenance and retrieval support only
Pantheon: governance authority only
```

## Rejected placements

Reject these collapses:

```text
OpenWebUI Function = Pantheon runtime
OpenWebUI Knowledge = Canonical Memory
Hermes profile = Pantheon Role authority
Hermes completion = approval
Langflow flow = governed decision
LangGraph checkpoint = memory
Langfuse trace = Evidence Pack
GraphRAG relation = proof
MCP availability = tool authorization
plugin installed = capability approved
```

## Evolution phases

### Phase 1 — Documentation and templates

Allowed now:

```text
governance placement documents
prompt placement documents
bridge contract doctrine
non-executable templates
ai_logs
```

Not allowed by this phase:

```text
runtime bridge
OpenWebUI executable extension
Hermes skill installation
Langflow deployment
LangGraph runtime
Langfuse backend
GraphRAG runtime
Docker or operations changes
```

### Phase 2 — Thin cockpit to Hermes

Future candidate:

```text
OpenWebUI thin Action
Pantheon Bridge candidate
Hermes profile and skill under Task Contract
Evidence Pack Candidate return
User Decision Gate display
```

This phase still must not create hidden execution inside Pantheon.

### Phase 3 — External preparation and observability

Future candidate:

```text
Langflow headless preparation flows
Langfuse trace metadata
read-only provenance graph
Hermes skill candidates for source audit and evidence building
```

All returned material remains candidate until governed review.

### Phase 4 — Durable interruptible external execution

Future candidate:

```text
LangGraph behind Hermes or bridge
human interrupt exposure in OpenWebUI
checkpoint / resume under unchanged Task Contract
Evidence Pack Candidate return
```

LangGraph must not become Pantheon core.

## Final rule

```text
Pantheon does not own the engines.
Pantheon owns the rules that decide what an engine may do,
what its output is worth,
and what may remain.
```
