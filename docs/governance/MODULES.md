# Modules

Status: migrated and distilled from Pantheon-OS @ `fd0beba83528bd5c92244d76a5643646dfae2d87`.

Source: `Pantheon-OS/docs/governance/MODULES.md`.

This document defines Pantheon Next modules as governance areas.

A module is not a runtime package.

A module is not an execution component.

A module is not a plugin, worker, queue, scheduler, provider router, endpoint, Docker service or tool registry.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Core principle

Pantheon Next must remain simpler than the runtime it governs.

Modules help organize governance responsibility.

They do not activate behavior.

They answer three questions:

```text
What governance area exists?
Which document is authoritative for it?
Which external surface may execute or expose it?
```

A module may define doctrine, vocabulary, expected evidence, approval thresholds, memory rules, candidate declarations, examples or future read-only checks.

A module must not define hidden execution.

## Module status vocabulary

Use these statuses when reviewing a module:

```text
active_doctrine
active_support
migrated_doctrine
stub_pending_migration
initial_schema_baseline
candidate_only_template
future_read_only_tooling
external_runtime_surface
voluntarily_not_implemented
```

These are governance statuses.

They are not deployment states.

## Canonical module map

| Module | Authority document | Current status | Runtime boundary |
|---|---|---|---|
| Repository status | `STATUS.md`, `ROADMAP.md` | active_doctrine | No runtime behavior. |
| Migration playbook | `MIGRATION_PLAYBOOK.md` | active_doctrine | Migration doctrine only. |
| Architecture | `ARCHITECTURE.md` | migrated_doctrine | Governance architecture only. |
| Modules | `MODULES.md` | migrated_doctrine | Governance map only. |
| Roles | `AGENTS.md`, `GOVERNANCE_COLLEGE.md`, `USER_DECISION_GATE.md` | active_doctrine | Pantheon Roles are not agents. |
| Approvals | `APPROVALS.md` | active_doctrine | Approval is governance, not execution. |
| Task Contracts | `TASK_CONTRACTS.md` | active_doctrine | Contracts frame execution but do not execute. |
| Evidence | `EVIDENCE_PACK.md` | active_doctrine | Evidence is review material, not runtime log. |
| Memory | `MEMORY.md`, `SCOPE_ISOLATION.md` | active_doctrine | No automatic memory promotion. |
| Knowledge | `KNOWLEDGE_TAXONOMY.md` | active_doctrine | Knowledge is not memory or proof by default. |
| Workflows | `WORKFLOW_SCHEMA.md`, `RUN_GRAPH.md`, `REQUEST_ORCHESTRATION.md` | active_doctrine | Workflow vocabulary is governance vocabulary only. |
| Doctor audit | `DOCTOR_MODULE_SPEC.md` | active_support | Audit-only support. Verifies, cites, classifies and flags; does not edit, fix, promote or decide. |
| OpenWebUI integration | `OPENWEBUI_INTEGRATION.md` | active_doctrine | OpenWebUI exposes, it does not govern or execute. |
| Hermes integration | `HERMES_INTEGRATION.md` | active_doctrine | Hermes executes externally under Task Contract. |
| External tools | `EXTERNAL_TOOLS_POLICY.md` | active_doctrine | Tools are capabilities, not authority. |
| Capability placement | `CAPABILITY_PLACEMENT.md`, `MODULAR_DOMAIN_REORIENTATION.md`, `ADAPTERS_AND_BINDINGS.md` | active_support | Governs modular capability placement and domain-pack projection. Tool-agnostic body, no runtime. |
| Domain pack spec | `DOMAIN_PACK_SPEC.md` | active_support | Governed methodology configuration, not a runtime module. |
| Request lifecycle | `REQUEST_LIFECYCLE.md` | active_support | Lifecycle of a request: MÈTIS (situated comprehension, keeper of the cap) + Zeus cap arbitration + Cerbère/Charon memory gates. Governance moments, not a runtime. |
| Architecture agency pack | `ARCHITECTURE_AGENCY_DOMAIN_PACK.md` | to_verify | Candidate domain pack; pending boundary review (#30). |
| Knowledge ingestion and memory | `KNOWLEDGE_INGESTION_AND_MEMORY.md` | to_verify | Candidate; pending boundary review (#30). |
| Workflow lifecycle | `WORKFLOW_LIFECYCLE.md` | to_verify | Candidate; pending boundary review (#30). |
| Data platform | `DATA_PLATFORM_ARCHITECTURE.md`, `DATA_PLATFORM_INDEX.md`, `DATA_PLATFORM_STATUS.md`, `DATA_PLATFORM_RECONCILIATION.md` | to_verify | Pending boundary review against `CLAUDE.md`; a data platform must not become a runtime. `DATA_PLATFORM_RECONCILIATION.md` records the boundary reconciliation. |
| Product positioning | `PRODUCT_DIFFERENTIATION.md`, `EDITORIAL_LANGUAGE.md` | active_support | Product doctrine only. |
| Narrative and visual language | `NARRATIVE.md`, `VISUAL_LANGUAGE.md` | active_support | Explanatory layer only. |
| External inspirations | `EXTERNAL_REPO_INSPIRATIONS.md`, `EXTERNAL_AGENTIC_INSPIRATIONS.md`, `SKILL_WATCHLIST.md` | active_support | Inspiration only, no dependency or approval. |
| Schemas | `schemas/README.md`, `schemas/*.schema.yaml` | initial_schema_baseline | Validation contracts only. |
| Hermes profile templates | `hermes/profiles/*` | candidate_only_template | Not installed or executed by Pantheon. |
| Examples | `docs/examples/` | active_support | Fictional educational support only. |
| Operations tooling | `operations/` | future_read_only_tooling | Not implemented. Read-only only if added later. |
| Tests | `tests/` | future_read_only_tooling | Not implemented. Validation only if added later. |

## Roles module

Pantheon Roles are governance viewpoints.

They are not autonomous agents.

The canonical registry is `AGENTS.md`.

The college model is defined in `GOVERNANCE_COLLEGE.md`.

Human escalation is defined in `USER_DECISION_GATE.md`.

The roles module may:

- define role responsibilities;
- expose useful disagreement;
- classify tensions;
- request review or escalation;
- define candidate status vocabulary.

It must not:

- spawn agents;
- create a role message bus;
- run autonomous debates;
- self-approve outputs;
- promote memory.

## Domain and dossier module

Pantheon Next may describe domain, dossier and project scopes.

A domain or dossier module is a governance perimeter.

It is not a loaded runtime module.

A domain or dossier module may define:

- scope identity;
- admissible source categories;
- expected output formats;
- risk classes;
- approval thresholds;
- memory and evidence expectations;
- templates or examples.

Domain-specific logic must remain declarative unless executed externally under Task Contract.

Historical Pantheon-OS domain identifiers are not automatically canonical in Pantheon Next.

## Skill governance module

Pantheon Next may define skill governance declarations.

A skill governance declaration is a capability expectation, wrapper or review frame.

It is not an executable skill.

Hermes Skills or other external runtime skills may execute outside Pantheon.

Pantheon may govern:

- purpose;
- allowed inputs;
- allowed outputs;
- forbidden outputs;
- risk class;
- evidence expectation;
- approval level;
- memory impact;
- domain or dossier scope.

Default rule:

```text
candidate until reviewed
```

Pantheon must not become a skill marketplace, plugin manager, automatic installer or capability runtime.

## Workflow governance module

A workflow in Pantheon Next is a governance declaration.

The canonical term is `Workflow Manifest`.

A Workflow Manifest may define:

- scope;
- entry criteria;
- governed phases;
- role viewpoints;
- Task Contract expectations;
- Evidence Pack expectations;
- approval requirements;
- memory rules;
- completion criteria.

It must not define:

- worker scheduling;
- queue progression;
- provider routing;
- runtime retries;
- hidden orchestration;
- tool dispatch.

Execution belongs to Hermes or another external runtime under Task Contract.

## Task Contract module

Task Contracts define the envelope for consequential work.

They may describe:

- objective;
- scope;
- constraints;
- allowed outputs;
- forbidden outputs;
- approval expectations;
- evidence expectations;
- memory rules.

A Task Contract frames execution.

It does not start execution.

It does not authorize broader access by itself.

If the task exceeds the contract, the safe result is a scope gap or User Decision Gate.

## Approval module

Approvals define governance thresholds.

They do not execute actions.

They do not trigger deployment, sending, writing, merging, routing or memory promotion automatically.

Approval levels C0-C5 remain decision thresholds, not runtime permissions.

## Evidence module

Evidence Packs make work reviewable.

They are human-auditable proof packages.

They are not raw runtime logs, hidden chain-of-thought, worker state or execution replay data.

An Evidence Pack may summarize relevant activity, sources, assumptions, risks, outputs, review state and Memory Candidates.

It does not approve itself.

## Memory module

Memory in Pantheon Next is governed continuity.

The memory module separates:

- Knowledge;
- Working Context;
- Session State;
- Runtime State;
- Memory Candidate;
- Canonical Memory.

No runtime may promote memory automatically.

OpenWebUI Knowledge is not Canonical Memory.

Hermes runtime state is not Canonical Memory.

Embeddings are not memory.

Repeated retrieval is not memory.

## Knowledge module

Knowledge is consultable material.

It may include files, Knowledge Bases, uploaded documents, repository documents, web sources and external references.

Knowledge can support a task.

Knowledge does not become proof, output or memory by being retrieved.

A Knowledge Item becomes Evidence only when selected for a specific claim, decision or output and recorded with traceability.

## Integration modules

### OpenWebUI

OpenWebUI is the cockpit.

It may expose:

- chat;
- source selection;
- Knowledge Bases;
- Task Contracts;
- candidate outputs;
- Evidence Packs;
- approval prompts;
- User Decision Gates;
- Memory Candidates.

It must not become Canonical Memory, approval authority, runtime, source of truth or hidden governance store.

### Hermes Agent

Hermes Agent is the external execution runtime.

It may execute technical work under Task Contract.

It may return:

- Result Candidates;
- Evidence Packs;
- Patch Candidates;
- Memory Candidates;
- Capability Gaps;
- Risk Escalations.

Hermes must not approve, canonize, promote memory, bypass scope or mutate doctrine without review.

## External tools module

External tools are capabilities.

They are not authority.

They are governed by `EXTERNAL_TOOLS_POLICY.md`.

The default posture is:

```text
not authorized unless scope, evidence and approval allow it
```

Tool availability does not mean tool authorization.

Tool output is candidate evidence until reviewed.

## Schemas module

Schemas validate structure.

They do not execute anything.

They do not create approval.

They do not promote memory.

They do not define runtime state.

Schemas must keep `governance_refs` aligned with the Markdown doctrine they validate.

## Operations and tests modules

Operations and tests are expected future read-only support areas.

Allowed future operations:

- Doctor checks;
- governance reference validation;
- schema validation;
- stub status checks;
- forbidden-runtime surface checks.

Forbidden operations:

- execution;
- automatic remediation;
- deployment;
- provider routing;
- memory promotion;
- runtime scheduling;
- queue management.

## Legacy module treatment

Historical Pantheon-OS contained runtime-oriented surfaces such as FastAPI applications, registries, workflow loaders, installers, migrations, runtime endpoints and legacy tests.

Pantheon Next does not import those by default.

Legacy components must be classified before reuse:

```text
implemented
documented_but_not_implemented
implemented_but_not_documented
partial
obsolete
contradictory
to_verify
non_implemented
voluntarily_not_migrated
```

No automatic deletion before diagnosis.

No automatic reactivation.

No bulk migration.

## Global governance flow

```text
User intent
→ OpenWebUI exposure
→ Pantheon governance framing
→ Task Contract when needed
→ bounded Context Pack
→ Hermes or external runtime execution when authorized
→ candidate result
→ Evidence Pack
→ review, approval or User Decision Gate
→ optional Memory Candidate
→ Canonical Memory only after explicit promotion
```

## Final rule

A module has value only if it clarifies responsibility, status, evidence, approval, memory or boundary.

If a module starts to execute, schedule, route, install, dispatch, approve itself or promote memory, it has left Pantheon governance scope.
