# Core Concepts Map

Status: active support — navigation concept map only.
Boundary profile: active_support_doctrine.

This document is the compact conceptual entry point for Pantheon Next. It points to existing owners; it does not create a schema, lifecycle, runtime, registry, workflow engine, approval engine or memory engine.

For exact terminology use `TERMINOLOGY_BOUNDARIES.md` and `GLOSSARY.md`. For repository/runtime posture use `STATUS.md` and `WHAT_RUNS.md`. If this map conflicts with an owner document, the owner wins.

## Responsibility map

```text
Pantheon governance core
= contracts, doctrine, status, evidence/approval/memory boundaries

mcp-server/
= bounded read-only policy and verification projection

implementation/
= bounded executable candidate implementation, including the current Cockpit candidate

OpenWebUI
= optional external exposure / communication / Knowledge integration surface when separately installed

Hermes Agent or another approved external runtime
= bounded execution under governed contracts

Human
= consequential decision and professional responsibility
```

Repository co-location does not transfer authority. An installed or healthy external surface does not become authorized by that fact alone.

## Core object map

| Concept | Function | Current owner family | Must not become |
|---|---|---|---|
| Case / Situation | governed professional scope and situated problem | `TASK_CONTRACTS.md`, relevant domain owners | folder identity or runtime task |
| Source | received, retrieved or observed material | `RAW_DERIVED_GOVERNED_RECORDS.md`, source-specific owners | truth or Evidence by ingestion alone |
| Knowledge | organized reusable or project reference material | `KNOWLEDGE_TAXONOMY.md` and Knowledge owners | Evidence or memory by retrieval alone |
| Context Pack | bounded context for one governed task/review | `CONTEXT_PACKS.md` | canonical memory or proof |
| Task Contract | governed boundary for delegated work | `TASK_CONTRACTS.md` | execution or authorization by itself |
| Capability | abstract governable function | `UNIFORM_CAPABILITY_GOVERNANCE.md`, `CAPABILITY_PLACEMENT.md` | installed Tool or task permission |
| Binding | selected technical realization candidate | `ADAPTERS_AND_BINDINGS.md` and capability contracts | adoption or activation by selection alone |
| Output Candidate | proposed result of work | task/domain owner | approved deliverable by production alone |
| Evidence Pack Candidate | reviewable support package | `EVIDENCE_PACK.md`, `EVIDENCE_TOPOLOGY.md` | runtime log or automatic proof |
| Gate / Decision | consequential threshold and scoped human determination | `APPROVALS.md`, `USER_DECISION_GATE.md`, decision contracts | hidden runtime approval |
| Register Candidate / Entry | proposed then approved durable governed retention | `MEMORY.md` and Register owners | raw storage dump or runtime memory |
| Pantheon Role | governance viewpoint/responsibility | `AGENTS.md`, `GOVERNANCE_COLLEGE.md` | autonomous agent |
| Rite | bounded recurring governance method | `rites/` owners | workflow runtime |
| Domain Pack | professional constraints and methodology projection | `DOMAIN_PACK_SPEC.md` and domain owners | professional authority by configuration |
| Card | presentation of an already-owned object | `CARD_STACK_MODEL.md`, `CARD_PROJECTION_DEFINITION_MODEL.md` | object schema, lifecycle or authority |
| Workspace projection | ephemeral read-only view of configured filesystem roots | co-located Workspace reader + Structured Agency Interface | Project, Category, Knowledge or governed identity |

## Minimal governed flow

```text
user request
→ Case / Situation clarification
→ Task Contract Candidate
→ scoped Sources and Knowledge
→ Context Pack
→ external execution when admitted and authorized
→ Output Candidate + Evidence Pack Candidate
→ review / Gate / human Decision
→ optional Register Candidate
→ governed durable entry only after its own admission
```

Shortcuts remain invalid:

```text
retrieved != truth
source != Evidence
runtime success != Evidence
schema valid != approved
installed != approved
healthy != safe
projection != persistence
folder != governed identity
Decision recorded != external effect executed
memory != Evidence
```

## Product and exposure surfaces

### Pantheon Cockpit

The current executable product candidate is co-located under `implementation/mvp_vertical/cockpit/`.

Its product composition is governed by `PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md`. Executable root identity and order are owned by the Navigation Registry. `CARD_STACK_MODEL.md` owns generic Card / Scene / Deck / Constellation projection grammar only.

```text
Cockpit projection != governed object
UI intent != authorization
root placement != object identity
implementation present != adopted or production-authorized
```

### OpenWebUI

OpenWebUI is an optional external exposure, communication and Knowledge-integration surface when separately installed. `OPENWEBUI_INTEGRATION.md` owns that integration boundary.

OpenWebUI may expose governed artifacts and capture bounded user intent. It is not the owner of Pantheon Cockpit root topology, governance truth, execution authority or durable memory.

### Hermes and other external runtimes

Hermes Agent is the principal external execution runtime described by current integration doctrine. Other approved bindings remain possible where the Capability owners allow them.

```text
runtime available != binding adopted
binding adopted != task-authorized
execution complete != approved result
```

### MCP policy / verification surface

`mcp-server/` projects bounded read-only governance validation and policy data. It does not execute professional work, approve effects or become the Cockpit.

## Authority ladder

Authority increases only through the relevant owner and governance path.

```text
material observed or retrieved
→ scoped candidate
→ qualified support / Evidence Candidate where applicable
→ human review or Decision where consequential
→ durable governed retention only through its own admission
```

Presence, repetition, UI visibility, model confidence, test success or storage location do not advance an object on this ladder.

## Stable reading path

For significant repository work:

```text
STATUS.md
→ WHAT_RUNS.md
→ AUTHORITY_INDEX.md
→ CORE_CONCEPTS_MAP.md
→ TERMINOLOGY_BOUNDARIES.md
→ relevant owner document
```

Then use the narrow task path:

```text
Cockpit product      → PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md → CARD_STACK_MODEL.md → implementation/mvp_vertical/cockpit/README.md
OpenWebUI integration → OPENWEBUI_INTEGRATION.md
Capabilities          → CAPABILITY_PLACEMENT.md → UNIFORM_CAPABILITY_GOVERNANCE.md → ADAPTERS_AND_BINDINGS.md
Governed execution    → TASK_CONTRACTS.md → HERMES_INTEGRATION.md → EVIDENCE_PACK.md → APPROVALS.md
Knowledge / Evidence  → KNOWLEDGE_TAXONOMY.md → EVIDENCE_PACK.md → EVIDENCE_TOPOLOGY.md
Memory / Register     → MEMORY.md
Roles / Rites         → AGENTS.md → GOVERNANCE_COLLEGE.md → rites/README.md
Professional domains  → DOMAIN_PACK_SPEC.md → relevant domain-pack owner
```

Do not read the whole governance corpus by default and do not create another concept/ownership map to solve a local ambiguity. Extend or simplify the existing owner first.

## Final rule

```text
Every concept has one job.
Every durable identity has an owner.
Every consequential effect has a gate.
Every external execution has a bounded contract.
Every projection remains downstream of authority.
The human decides what is consequential.
```
