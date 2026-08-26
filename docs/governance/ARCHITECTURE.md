# Architecture

Status: active doctrine — independently maintained in Pantheon Next.
Boundary profile: active_support_doctrine.

Historical provenance is preserved in git history; this file has no external source dependency.

## Purpose

Pantheon Next is a governance-first monorepo. It separates authority, verification, product projection and external execution so that implementation success cannot silently become governance truth.

```text
Pantheon governance core
        ↓ consumed by
mcp-server/ and implementation/
        ↓ integrated with
external runtimes and optional external exposure surfaces
```

Authority flows downward only through explicit contracts. Repository co-location does not reverse that direction.

## Current layers

### Governance core

Owns doctrine, canonical contracts, status, evidence rules, approval boundaries, memory/retention rules, capability governance and professional/domain constraints.

Key owners include:

- `TASK_CONTRACTS.md`;
- `EVIDENCE_PACK.md` and `EVIDENCE_TOPOLOGY.md`;
- `APPROVALS.md` and `USER_DECISION_GATE.md`;
- `MEMORY.md`;
- `CAPABILITY_PLACEMENT.md` and `UNIFORM_CAPABILITY_GOVERNANCE.md`;
- `DOMAIN_PACK_SPEC.md`;
- `PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md` for Cockpit product composition.

The governance core does not gain execution authority from implementation code.

### Read-only policy / verification surface

`mcp-server/` projects bounded governance validation and policy data. It can verify or classify within its declared contracts; it does not become the UI, execute professional work, approve consequences or promote durable memory.

### Co-located implementation

`implementation/` contains bounded executable candidate behavior: persistence, APIs, Cockpit projections and integration adapters.

The current Cockpit candidate lives under `implementation/mvp_vertical/cockpit/`.

```text
Structured Agency Interface
= product composition and Space meaning

Navigation Registry
= executable root identity and order

Card Stack
= generic projection grammar

Card Projection Definitions
= machine-readable presentation mapping

owner records
= remain outside the renderer
```

The Cockpit may expose projections and capture bounded intent. It does not own the underlying business identity, Evidence status, authorization or persistence merely because it renders them.

### External execution runtimes

Hermes Agent is the principal external execution runtime described by current doctrine. Other separately approved bindings remain possible through the Capability owners.

External runtimes may perform bounded work only through the applicable Task Contract, capability, policy and approval boundaries. Their results return as candidates or observations until the relevant governance owner admits them.

### Optional external exposure surfaces

OpenWebUI is an optional external exposure, communication and Knowledge-integration surface when separately installed. Its boundary is owned by `OPENWEBUI_INTEGRATION.md`.

OpenWebUI may expose governed artifacts or capture user intent, but it is not the owner of Pantheon Cockpit root topology, governance truth, execution authority or durable memory.

Other communication or document surfaces may be integrated under the same principle: channel != authority.

### Human responsibility

Consequential decisions remain human. Neither a UI action, policy verdict, runtime receipt nor successful test substitutes for the required scoped human decision or professional responsibility.

## Governed work spine

```text
request
→ Case / Situation clarification
→ Task Contract Candidate
→ scoped Sources and Knowledge
→ Context Pack
→ admitted external execution when required
→ Output Candidate + Evidence Pack Candidate
→ review / Gate / human Decision
→ optional durable retention through its own admission
```

The relevant object owners define exact states and transitions. This architecture document does not create a parallel lifecycle.

## Capability placement

A technical capability remains replaceable behind governed placement and binding contracts.

```text
Capability
→ eligible Binding
→ observed installation / health / compatibility
→ governed activation where applicable
→ task-specific admission
→ bounded execution
```

These axes remain independent:

```text
available != adopted
installed != approved
healthy != safe
activated != task-authorized
runtime success != Evidence
```

Pantheon should reuse an existing external technical capability rather than recode it merely to centralize control.

## Evidence, memory and persistence

Storage, retrieval, execution and governance remain distinct.

```text
stored != governed
retrieved != truth
runtime trace != Evidence
memory != Evidence
Register Candidate != durable governed entry
projection != persistence
```

Exact Evidence and retention rules are owned by `EVIDENCE_PACK.md`, `EVIDENCE_TOPOLOGY.md` and `MEMORY.md`.

## Knowledge and Workspace

Knowledge identity and filesystem location are not interchangeable.

The Cockpit Workspace projection is a bounded read-only technical view over explicitly configured filesystem roots. It must not infer Project, Category, Knowledge, Evidence or governed identity from a folder or path.

```text
folder != Case
folder != Category
file present != Knowledge
retrieved file != Evidence
```

## Integration rule

An integration must identify separately:

```text
exposed_by
executed_by
governed_by
approved_by
persisted_by, when persistence exists
```

No adapter, UI or external runtime acquires another layer's authority by convenience.

## Privacy and professional data

Real professional data, secrets, credentials and environment-specific deployment authority remain outside the public repository. Repository fixtures and examples must remain fictional, neutral and non-identifying.

Private deployment may bind real storage and runtimes only through separately governed configuration and authorization.

## Current status source

Do not infer deployment or adoption from this architecture map.

- `STATUS.md` owns repository posture;
- `WHAT_RUNS.md` owns runtime-status honesty;
- `AUTHORITY_INDEX.md` owns authority classification;
- `MODULES.md` maps governance areas;
- `implementation/mvp_vertical/cockpit/README.md` describes the current co-located Cockpit candidate.

## Final invariants

```text
repository co-location != authority transfer
implementation present != adopted
projection != persistence
runtime success != authorization
runtime success != Evidence
retrieved data != truth
memory != Evidence
folder != governed identity
Decision recorded != external effect executed
```

Pantheon Next should remain simpler than the runtimes and products it governs. When an existing owner or replaceable external capability already covers a responsibility, converge on it instead of creating a parallel path.
