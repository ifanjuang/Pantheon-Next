# OpenWebUI Integration

Status: active doctrine — optional external exposure integration boundary.
Boundary profile: active_support_doctrine.

## Purpose

This document owns the governance boundary for OpenWebUI when it is separately installed and selected as an external exposure, communication or Knowledge-integration surface.

It does not own Pantheon Cockpit product composition or root navigation. The current executable Cockpit candidate is co-located under `implementation/mvp_vertical/cockpit/`; product composition is owned by `PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md` and executable root identity/order by the Navigation Registry.

```text
OpenWebUI integration != Pantheon Cockpit authority
exposure != governance
user action captured != consequential effect authorized
Knowledge available != task-scoped Knowledge
```

This document is not an OpenWebUI installation guide, plugin implementation specification, provider configuration guide or deployment authority.

## Allowed role

When selected, OpenWebUI may expose or collect bounded interaction around governed Pantheon objects, for example:

- chat or request interaction;
- user intent and clarification;
- source upload or source reference;
- Knowledge Base consultation or selection;
- Task Contract display;
- Context Pack display;
- Evidence Pack Candidate display;
- Output Candidate display;
- Gate or Decision request display;
- approval/rejection/revision intent capture;
- Register Candidate or durable-entry excerpt display;
- runtime observations returned by an external executor;
- bounded escalation or request-for-more-evidence actions.

The underlying object owner remains authoritative for identity, status, Evidence, approval, retention and permitted actions.

```text
UI display != object creation
UI label != lifecycle state authority
UI action != approval by itself
UI visibility != scope authorization
```

## User decision capture

OpenWebUI may capture a user decision or review intent only as input to the relevant governed decision path.

For consequential decisions, the record must be sufficiently specific to bind at least the applicable object/version, scope, action or decision meaning and the required human identity/authentication context where the owner contract requires it.

A generic click, chat affirmation or interface state must not silently become a high-consequence approval.

Exact decision validity and ceilings remain owned by `APPROVALS.md`, `USER_DECISION_GATE.md` and the applicable decision contracts.

## Knowledge and source boundary

OpenWebUI may organize or expose user-side files, Notes, folders and Knowledge Bases. That organization is an exposure convenience, not Pantheon Knowledge authority or task scope by itself.

Preserve the sequence:

```text
available material
→ explicitly selected or owner-scoped material
→ bounded retrieval
→ candidate support
→ Evidence only through the Evidence owner
→ durable retention only through the retention owner
```

And the distinctions:

```text
available != selected
selected != retrieved
retrieved != Evidence
Knowledge Base item != governed memory
folder != Case
folder != governed identity
```

A user-visible folder or Knowledge Base must not grant an execution runtime global access to all underlying content.

## Governed handoff to Hermes or another runtime

OpenWebUI may help the user select inputs, but the execution boundary must be expressed through existing governed artifacts rather than direct UI-to-runtime authority.

Preferred shape:

```text
user selection / request
→ Task Contract and bounded context
→ authorized source or Knowledge references
→ external execution when admitted
→ candidate result + evidence/observation return
```

A bounded Context Pack or equivalent owner-defined task context is preferred over coupling Hermes to OpenWebUI internals.

OpenWebUI must not imply unrestricted Hermes access to every file, Note, Knowledge Base, vector index or database object visible to the user.

Direct runtime access to OpenWebUI internal storage is not a normal governance path. Any exceptional diagnostic integration must be explicitly scoped, read-only where possible and unable to bypass Evidence, approval or retention boundaries.

## OpenWebUI extension surfaces

OpenWebUI Functions, Tools, Pipes, Filters, Actions, Pipelines or comparable extension mechanisms are external capability surfaces when they can call services, transform consequential data, execute code, write state, publish externally or influence retained content.

They therefore compose existing Capability owners rather than creating an OpenWebUI-specific governance lifecycle:

```text
Capability placement
→ Binding qualification
→ installation / health observations
→ activation where governed
→ task-specific admission
→ bounded execution
```

Relevant owners include:

- `CAPABILITY_PLACEMENT.md`;
- `UNIFORM_CAPABILITY_GOVERNANCE.md`;
- `ADAPTERS_AND_BINDINGS.md`;
- `EXTERNAL_TOOLS_POLICY.md`;
- `TASK_CONTRACTS.md`;
- `APPROVALS.md`;
- `EVIDENCE_PACK.md`.

```text
extension installed != approved
extension visible != task-authorized
extension output != Evidence
plugin convenience != Pantheon runtime
```

This document does not create a plugin registry, installation lifecycle, execution engine or provider-routing authority.

## Events and observations

OpenWebUI events or webhooks may be consumed as bounded observations where an approved integration exists.

An event can support traceability, diagnostics or candidate evidence collection. It does not decide governance state and is not a durable governed entry by itself.

```text
event received != action approved
event recorded != Evidence accepted
event history != Registre Probatoire
```

## Candidate outputs and Evidence display

OpenWebUI may display candidate outputs and Evidence Pack Candidates, including source references, assumptions, limitations, contradictions and unresolved gaps.

The presentation must not erase the owner-defined status or make partial evidence appear complete.

```text
candidate displayed != deliverable approved
Evidence Pack displayed != Evidence accepted
runtime receipt displayed != Evidence
```

## Memory and retention display

OpenWebUI may display retention candidates or excerpts of governed durable records when authorized for the user and scope.

It must not infer promotion from repeated chat content, retrieval success, model confidence, interface convenience or Knowledge Base indexing.

Retention remains owned by `MEMORY.md` and the applicable Register contracts.

## Relationship to the Pantheon Cockpit

The co-located Pantheon Cockpit and OpenWebUI are separate exposure responsibilities.

- Pantheon Cockpit: current executable candidate product projection under `implementation/`, with governed root/product composition.
- OpenWebUI: optional external interaction and Knowledge-integration channel when separately selected and installed.

They may expose some of the same governed objects without duplicating those objects or creating competing status/lifecycle authority.

```text
same object in two surfaces != two identities
surface-specific projection != persistence fork
channel choice != governance choice
```

## Deployment and implementation status

Repository doctrine does not pin an OpenWebUI operational version or installation procedure. Any deployment or extension configuration must be checked against the current external OpenWebUI documentation and the actual target environment before use.

The co-located `implementation/` subtree may contain OpenWebUI-facing adapters or integration candidates. Their presence and tests establish implementation evidence only.

```text
adapter present != installed
installed != adopted
adopted != activated
activated != task-authorized
CI green != production authorization
```

Use `WHAT_RUNS.md` for current repository/runtime status.

## Forbidden authority drift

OpenWebUI integration must not become:

- governance source of truth;
- owner of Pantheon Cockpit root topology;
- execution authority merely through UI interaction;
- automatic approval path;
- automatic durable-memory promotion path;
- unrestricted Knowledge gateway to an execution runtime;
- hidden provider or capability authority;
- doctrine mutation authority.

## Final rule

OpenWebUI can make governed work accessible through an optional external channel. It does not make the displayed state true, authorized, executed, evidenced or durable by itself.
