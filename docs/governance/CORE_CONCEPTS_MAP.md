# Core Concepts Map

Status: active support doctrine — navigation concept map only — implemented as documentation.
Boundary profile: active_support_doctrine.

This is the compact navigation and ownership entry point for Pantheon Next concepts. It is not a schema, runtime, registry, workflow engine, plugin manager or approval engine.

```text
Hermes client surfaces handle conversation and runtime interaction.
Pantheon Cockpit exposes governed projections.
Hermes Agent executes externally.
Pantheon Next governs consequential status.
The human decides.
```

No interface surface becomes authority merely because it displays or captures information.

## Core flow

`Case` is the governed system concept. A filesystem folder, Obsidian folder or UI collection is only a projection or working scope unless an existing owner explicitly binds it to governed identity.

```text
User request
-> Case / Situation clarification
-> Task Contract Candidate
-> scoped Sources / Knowledge selection
-> Context Pack
-> Hermes execution when authorized
-> Output Candidate
-> Evidence Pack Candidate
-> review / approval
-> delivery or User Decision Gate
-> optional Register Candidate
-> Registre Probatoire entry only after governed promotion
```

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
folder != governed identity
```

## Object ownership map

| Concept | Responsibility | Must not become |
|---|---|---|
| Raw Source | available source material | proof |
| Knowledge Item | organized consultable reference | truth |
| Retrieved Knowledge | surfaced candidate support | Evidence by itself |
| Context Pack | bounded task context | memory or proof |
| Task Contract | governed task boundary | runtime task or approval |
| Hermes execution | external execution under contract | governance authority |
| Output Candidate | proposed result | approved deliverable |
| Evidence Pack | reviewable proof package | runtime log or approval |
| Approval | explicit governance decision | runtime success flag |
| Register Candidate | proposed durable Assertion | Registre Probatoire entry |
| Registre Probatoire entry | approved scoped durable Assertion | raw database or runtime memory |
| Pantheon Role | governance viewpoint | autonomous agent |
| Rite | bounded shared method | workflow runtime |
| Domain Pack | professional constraints | professional authority |
| Capability / Skill Candidate | eligible external capability | installed or task-authorized capability |
| Effective Policy | computed governance posture | execution engine |
| Pantheon Cockpit | governed projection and decision surface | source of truth or runtime |
| Hermes client surface | conversation/runtime interaction with Hermes | Pantheon governance surface by implication |
| Obsidian workspace | human-authored Markdown workspace/source projection | Evidence, project identity or canonical memory |
| Hindsight | derived associative memory/index when selected | source truth or Evidence |
| User Decision Gate | visible consequential decision point | automatic approval |

## Authority ladder

```text
Raw Source
-> Source Reference
-> Evidence Item
-> Evidence Pack
-> Approval
-> Register Candidate when a durable Assertion exists
-> Registre Probatoire entry after governed promotion
```

No retrieval score, model confidence, runtime completion, repeated memory or interface state short-circuits this ladder.

## Execution and presentation

Pantheon does not absorb Hermes execution and Hermes clients do not absorb Pantheon governance.

```text
Task Contract / Context Pack
-> Hermes Agent executes externally
-> Hermes returns candidates and observations
-> Pantheon qualifies consequential status
-> Pantheon Cockpit may project governed state
-> Hermes Web/dashboard clients may continue runtime conversation and control
```

The current co-located Cockpit candidate owns governed product projections and navigation semantics through its existing owners. It is not intended to become a second general-purpose chat frontend.

Hermes client implementations remain replaceable. The official Hermes web/dashboard surface is the current baseline; a mobile/PWA client may be selected separately when compatibility and deployment boundaries are verified.

## Knowledge, workspace and memory

Keep three responsibilities separate:

```text
Source / Document owners
  exact professional source identity and provenance

Obsidian workspace
  human-authored Markdown notes, working context and editable projections

Hindsight / Hermes memory
  derived runtime recall where separately selected
```

Pantheon governs Knowledge, Evidence, approval and durable Register promotion. Obsidian does not replace the professional source store, and Hindsight does not become truth because recall succeeds.

## Roles, rites and methods

```text
Roles judge.
Rites structure bounded method.
Agora may expose deliberation.
ZEUS arbitrates governed status and procedure.
The human decides.
```

A Role Signal may request review or escalation. It must not execute, approve or promote memory.

## Capabilities

```text
capability detected
-> binding eligible
-> binding selected / activated where governed
-> task-authorized through existing contract/admission owners
-> Hermes may execute externally
-> result remains candidate until qualified
```

Canonical owners include:

- `CAPABILITY_PLACEMENT.md` and `UNIFORM_CAPABILITY_GOVERNANCE.md` for placement and common governance;
- Capability Passport contracts for exact-release eligibility;
- Binding and Activation contracts for selected runtime bindings;
- `TASK_CONTRACTS.md` and Execution Admission for task legitimacy;
- `HERMES_INTEGRATION.md` for external execution boundary;
- `PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md` for Cockpit product composition;
- `CARD_STACK_MODEL.md` for generic Card / Scene / Deck / Constellation projection grammar.

Detected, installed, activated and task-authorized remain distinct states.

## External systems

External tools are reviewed before becoming a selected binding or client.

```text
Watch
-> Reference Review / placement review
-> distill, reject or retain as candidate
-> select only through an existing owner
-> Task Contract before consequential execution
```

A reviewed UI, runtime, memory system or connector does not become Pantheon architecture merely because it works technically.

OpenWebUI and Paperless are superseded integration candidates, not current target owners. Their historical material remains provenance until incoming references and implementation compatibility code are safely removed.

## Stable reading path

Read this map, then only the owners relevant to the task:

```text
repository state       -> STATUS.md, WHAT_RUNS.md, AUTHORITY_INDEX.md
vocabulary             -> TERMINOLOGY_BOUNDARIES.md, GLOSSARY.md
execution              -> TASK_CONTRACTS.md, HERMES_INTEGRATION.md
context                 -> CONTEXT_PACKS.md, CONTEXT_STACK.md
cockpit product         -> PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md
card grammar            -> CARD_STACK_MODEL.md
knowledge               -> KNOWLEDGE_TAXONOMY.md
workspace / recall      -> OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md
Evidence                -> EVIDENCE_PACK.md
approval                -> APPROVALS.md, USER_DECISION_GATE.md
memory / Register       -> MEMORY.md
external tools          -> EXTERNAL_TOOLS_POLICY.md, EXTERNAL_TOOL_PLACEMENT_REGISTER.md
```

## Final rule

```text
Every concept has one job.
Every durable promotion uses an existing governed owner.
Every external effect keeps an explicit boundary.
Every unresolved consequential tension stays visible.
No superseded product is kept as an architectural owner for historical convenience.
```
