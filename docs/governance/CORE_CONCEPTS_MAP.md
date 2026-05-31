# Core Concepts Map

Status: active navigation doctrine — concept map only.

This document gives a compact map of the core Pantheon Next concepts and their relationships.

It is a reading aid.

It is not a schema.

It is not a runtime model.

It is not a workflow engine.

It is not a module registry.

It is not a plugin manager.

It does not authorize execution, approval, memory promotion, tool use or external transmission.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon now contains several governance layers:

- Task Contracts;
- Context Packs;
- Evidence Packs;
- Memory Candidates;
- Pantheon Roles;
- Rites;
- Domain Packs;
- Skill Candidates;
- Modules;
- Effective Policy;
- OpenWebUI Templates;
- User Decision Gates;
- External Tool Candidates;
- Reference Reviews.

Each layer is useful only if it remains distinct.

This map prevents doctrine sprawl by showing what each concept does and what it must never become.

For where each concept lives across layers, and how a profession's methodology is defined once in Pantheon and projected outward, see `MODULAR_DOMAIN_REORIENTATION.md`. It reconciles `MODULE_ACTIVATION.md`, `DOMAIN_PACK_SPEC.md`, `CAPABILITY_PLACEMENT.md` and `TASK_CONTRACTS.md` under one placement and projection model.

## One-line doctrine

```text
Task Contract bounds work.
Context Pack prepares context.
Hermes executes externally.
Evidence Pack makes results reviewable.
Approvals decide legitimacy.
Memory keeps only what was validated.
OpenWebUI exposes the process.
Pantheon governs the status.
```

## Minimal dossier flow

```text
User request
→ Task Contract Candidate
→ scoped sources and Knowledge selection
→ Context Pack
→ external execution by Hermes when authorized
→ Output Candidate
→ Evidence Pack Candidate
→ review and approval
→ delivery or User Decision Gate
→ optional Memory Candidate
→ Canonical Memory only after approval
```

Nothing in this flow executes inside Pantheon.

## Core object map

| Concept | Function | Must not become |
|---|---|---|
| Raw Source | available material | proof |
| Knowledge Item | organized reference | truth |
| Retrieved Knowledge | surfaced candidate support | evidence by itself |
| Context Pack | bounded task context | memory or proof |
| Task Contract | governed execution boundary | runtime task |
| Hermes execution | external work under contract | approval |
| Output Candidate | proposed result | deliverable by default |
| Evidence Pack | reviewable proof package | runtime log or approval |
| Approval | explicit governance decision | execution permission engine |
| Memory Candidate | proposed durable claim | Canonical Memory |
| Canonical Memory | approved scoped memory | raw database dump |
| Pantheon Role | governance viewpoint | autonomous agent |
| Rite | bounded shared method | workflow runtime |
| Domain Pack | professional constraints | professional authority |
| Skill Candidate | eligible external capability | installed skill |
| Module | governable capability area | plugin |
| Effective Policy | computed governance posture | enforcement engine |
| OpenWebUI Template | cockpit display pattern | runtime UI authority |
| User Decision Gate | exposed human decision point | automatic approval |
| Reference Review | external inspiration analysis | adoption decision |

## Authority ladder

Authority increases only through governance.

```text
Raw Source
→ Source Reference
→ Evidence Item
→ Evidence Pack
→ Approval
→ Memory Candidate if durable claim exists
→ Canonical Memory if approved
```

Shortcuts are forbidden:

```text
retrieved ≠ evidence
chunked ≠ validated
scored ≠ approved
clear ≠ verified
produced ≠ deliverable
repeated ≠ memory
```

## Execution ladder

Pantheon does not execute.

```text
Task Contract
→ Context Pack
→ Hermes executes externally
→ Hermes returns candidates and evidence
→ Pantheon reviews status
→ OpenWebUI exposes result and decisions
```

Forbidden collapse:

```text
Task Contract ≠ runtime task
Context Pack ≠ prompt authority
Hermes done ≠ approved
run trace ≠ Evidence Pack
OpenWebUI display ≠ validation
```

## Role and rite map

Roles and rites are governance devices.

```text
Roles judge.
Rites coordinate.
Agora may expose deliberation.
ZEUS arbitrates status and procedure.
The human decides.
```

A role is a stable responsibility of judgment.

A rite is a bounded method used when a recurring methodological tension appears.

A Role Signal may request review or escalation.

A Role Signal must not activate, execute, approve or promote memory.

## Domain and skill map

Domain Packs and Skill Candidates support professional workflows without becoming professional authority.

```text
Domain Pack enabled
→ professional constraints apply
→ relevant roles become active or mandatory
→ skill candidates may become eligible
→ Task Contract may authorize a specific skill
→ Hermes may execute the task-bound skill externally
→ Evidence Pack returns
→ human review remains required
```

Forbidden collapse:

```text
domain enabled ≠ professional validation
legal domain ≠ legal advice authority
architecture domain ≠ architectural compliance approval
skill eligible ≠ installed skill
skill installed ≠ task-authorized
skill output ≠ approved deliverable
```

## Module and Effective Policy map

Module Activation defines whether a capability is detected, enabled or task-authorized.

```text
detected
→ enabled by governed scope
→ task-authorized through Task Contract
→ exposed by OpenWebUI
→ executed externally only when allowed
```

Core distinction:

```text
Detected does not mean enabled.
Enabled does not mean authorized for a task.
Authorized for a task does not mean sovereign.
```

Effective Policy is the visible answer to:

```text
Given what is detected, enabled, scoped and requested, what is actually allowed now?
```

Effective Policy is not a runtime engine.

## OpenWebUI map

OpenWebUI is the cockpit.

It may expose:

- Task Contract status;
- Context Pack state;
- Evidence Pack state;
- Output Candidate;
- approval prompts;
- Memory Candidate review;
- role readiness;
- domain activation;
- skill eligibility;
- module status;
- dependency blockers;
- User Decision Gates.

It must not:

- execute Pantheon doctrine;
- approve by display;
- promote memory;
- install skills;
- run LangGraph for Pantheon;
- grant Hermes broad Knowledge access;
- hide unresolved risk behind a smooth UI.

## Hermes map

Hermes is the external execution runtime.

Pantheon may provide Hermes:

- Task Contract;
- Context Pack;
- role viewpoint request;
- approval expectation;
- tool policy excerpt;
- Evidence Pack expectation;
- memory rule;
- output format expectation.

Hermes may return:

- Result Candidate;
- Evidence Pack Candidate;
- Patch Candidate;
- Memory Candidate;
- Capability Gap;
- Risk Escalation;
- Review Note.

Hermes must not:

- canonize evidence;
- approve itself;
- promote memory;
- expand scope silently;
- bypass User Decision Gates;
- become Pantheon doctrine.

## User Decision Gate map

When governed tension exceeds procedural arbitration, Pantheon must expose the conflict and ask the user.

Typical triggers:

- source conflict;
- scope conflict;
- professional risk;
- external effect;
- delivery ambiguity;
- memory risk;
- approval uncertainty;
- role conflict.

The gate is not approval by itself.

It is the visible place where the user decides when the system must not decide alone.

## External reference map

External systems are reviewed before any use.

```text
Watch
→ Reference Review
→ Boundary classification
→ Distillation or rejection
→ Candidate only if useful
→ Task Contract before execution
```

Reference reviews may inspire:

- vocabulary;
- boundary rules;
- evidence expectations;
- risk registers;
- Hermes candidate constraints;
- OpenWebUI exposure patterns.

They do not approve:

- dependency adoption;
- runtime migration;
- plugin installation;
- skill installation;
- provider routing;
- MCP server creation;
- observability backend creation;
- automatic memory promotion;
- automatic approval.

## High-risk shortcut list

Reject these equations:

```text
OpenWebUI Function = Pantheon runtime
Hermes profile = Pantheon Role
LangGraph state = memory
Nango connection = authorized external action
Understand-Anything graph = architecture truth
RAG score = evidence
benchmark pass = professional validation
role agreement = approval
rite completion = approval
pre-execution simulation = safe execution
schema valid = governance approved
```

## Current stable reading path

For repo work, use this short path before diving deeper:

```text
1. STATUS.md
2. CORE_CONCEPTS_MAP.md
3. README.md
4. AGENTS.md
5. TASK_CONTRACTS.md
6. CONTEXT_PACKS.md
7. EVIDENCE_PACK.md
8. APPROVALS.md
9. MEMORY.md
10. OPENWEBUI_INTEGRATION.md
11. HERMES_INTEGRATION.md
12. EXTERNAL_TOOLS_POLICY.md
```

Then read the specific doctrine for the task:

```text
roles or college      -> GOVERNANCE_COLLEGE.md, ROLE_ACTIVATION.md, ROLE_SIGNALS.md
modules and UI        -> MODULE_ACTIVATION.md, OPENWEBUI_TEMPLATES.md
professional domains  -> ROLE_ACTIVATION.md, examples/
rites                 -> rites/README.md
RAG                   -> RAG_INGESTION_PIPELINE.md, RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md
external references   -> reference_reviews/, WATCHLIST.md, REJECTED_PATTERNS.md
```

## Final rule

```text
Every concept has one job.
Every promotion requires governance.
Every external action requires a boundary.
Every unresolved tension must remain visible.
```