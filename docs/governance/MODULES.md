# Modules

Status: active doctrine — migrated and distilled from Pantheon-OS @ `fd0beba83528bd5c92244d76a5643646dfae2d87`.

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
| Decision surfaces | `DECISION_SURFACE_SPEC.md`, `USER_DECISION_GATE.md`, `EVIDENCE_PACK.md` | to_verify | OpenWebUI-facing display/capture pattern only. It does not approve, execute, validate, promote memory, send, or become an Evidence Pack. |
| Approvals | `APPROVALS.md` | active_doctrine | Approval is governance, not execution. |
| Task Contracts | `TASK_CONTRACTS.md` | active_doctrine | Contracts frame execution but do not execute. |
| Evidence | `EVIDENCE_PACK.md` | active_doctrine | Evidence is review material, not runtime log. |
| Memory | `MEMORY.md`, `SCOPE_ISOLATION.md` | active_doctrine | No automatic memory promotion. |
| Knowledge | `KNOWLEDGE_TAXONOMY.md` | active_doctrine | Knowledge is not memory or proof by default. |
| Workflows | `WORKFLOW_SCHEMA.md`, `RUN_GRAPH.md`, `REQUEST_ORCHESTRATION.md` | active_doctrine | Workflow vocabulary is governance vocabulary only. |
| Governed composition | `CAPABILITY_REGISTRY.md`, `WORKFLOW_SCHEMA.md` | to_verify | Candidate: HÉPHAÏSTOS forges a Workflow Manifest candidate from declared capabilities, gated by two evidence gates. forged != authorized. No forge engine or runtime; promotes no memory. |
| Repository review watcher | `REPOSITORY_REVIEW_WATCHER.md` | to_verify | Candidate Workflow Manifest only. It may frame repository activity review, but does not implement cron, webhook, queue, dashboard writes, Hermes skill, approval or memory promotion. |
| Doctor audit | `DOCTOR_MODULE_SPEC.md` | active_support | Audit-only support. Verifies, cites, classifies and flags; does not edit, fix, promote or decide. |
| OpenWebUI integration | `OPENWEBUI_INTEGRATION.md` | active_doctrine | OpenWebUI exposes, it does not govern or execute. |
| Hermes integration | `HERMES_INTEGRATION.md` | active_doctrine | Hermes executes externally under Task Contract. |
| Hermes Kanban execution patterns | `HERMES_KANBAN_EXECUTION_PATTERNS.md` | to_verify | Tool-specific execution coordination note only. Kanban tasks, swarms and scheduled reviews remain external runtime behavior; returned outputs stay candidates. |
| MCP policy server | `PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`, `mcp-server/` | active_support | Bounded read-only policy / validation MCP surface centered on the capability passport; also validates candidate Architecture Project Understanding dossiers. It serves doctrine and returns decisions as data; it does not execute, send, write, approve, schedule, queue, route providers or promote memory. The gate decides; the human decides. |
| External tools | `EXTERNAL_TOOLS_POLICY.md` | active_doctrine | Tools are capabilities, not authority. |
| External runtime threat review | `EXTERNAL_RUNTIME_THREAT_MODEL_REVIEW.md` | active_support | Review method for external runtimes, mixed AI workspaces and privileged capability surfaces. It classifies power, exposure, host-control, untrusted content and gates; it does not scan, sandbox, install, execute, approve or configure. |
| Model capability passport | `MODEL_CAPABILITY_PASSPORT.md`, `UNIFORM_CAPABILITY_GOVERNANCE.md` | active_support | Model-specific passport declaration under the uniform capability rule. It governs admissibility, data exposure, task-family suitability, evidence and approval ceiling; it does not route, serve, benchmark or select models at runtime. |
| Capability placement | `CAPABILITY_PLACEMENT.md`, `MODULAR_DOMAIN_REORIENTATION.md`, `ADAPTERS_AND_BINDINGS.md` | active_support | Governs modular capability placement and domain-pack projection. Tool-agnostic body, no runtime. |
| External runtime memory adapters | `EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` | active_support | Governs external runtime memory, checkpoint, graph recall and observability adapters. No memory backend, graph runtime, checkpoint engine, MCP server, approval engine or automatic memory promotion. |
| Domain pack spec | `DOMAIN_PACK_SPEC.md` | active_support | Governed methodology configuration, not a runtime module. |
| Request lifecycle | `REQUEST_LIFECYCLE.md` | active_support | Lifecycle of a request: MÈTIS (situated comprehension, keeper of the cap) + Zeus cap arbitration + Cerbère/Charon memory gates. Governance moments, not a runtime. |
| Answer verification gate | `ANSWER_VERIFICATION_GATE.md` | to_verify | Candidate doctrine for memory-first answers, evidence escalation and consequential response status. No classifier, schema, COP, approval engine or memory engine. |
| Governed form filling | `GOVERNED_FORM_FILLING.md` | to_verify | Field-as-claim filling of any form/CERFA with per-field resolution + fallback, guardrails and a modular skill decomposition. Method only; connectors/PDF are adapters. Candidate until reviewed. |
| Architecture agency pack | `ARCHITECTURE_AGENCY_DOMAIN_PACK.md` | to_verify | Candidate domain pack; pending boundary review (#30). |
| Knowledge ingestion and memory | `KNOWLEDGE_INGESTION_AND_MEMORY.md` | to_verify | Candidate; pending boundary review (#30). |
| Workflow lifecycle | `WORKFLOW_LIFECYCLE.md` | to_verify | Candidate; pending boundary review (#30). |
| Data platform | `DATA_PLATFORM_ARCHITECTURE.md`, `DATA_PLATFORM_INDEX.md`, `DATA_PLATFORM_STATUS.md`, `DATA_PLATFORM_RECONCILIATION.md` | to_verify | Pending boundary review against `CLAUDE.md`; a data platform must not become a runtime. `DATA_PLATFORM_RECONCILIATION.md` records the boundary reconciliation. |
| Product positioning | `PRODUCT_DIFFERENTIATION.md`, `EDITORIAL_LANGUAGE.md` | active_support | Product doctrine only. |
| Narrative and visual language | `NARRATIVE.md`, `VISUAL_LANGUAGE.md` | active_support | Explanatory layer only. |
| External inspirations | `EXTERNAL_REPO_INSPIRATIONS.md`, `EXTERNAL_AGENTIC_INSPIRATIONS.md`, `SKILL_WATCHLIST.md`, `SPICE_REFERENCE_DISTILLATION.md` | active_support | Inspiration and reference distillation only, no dependency or approval. |
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

## External runtime threat review module

Pantheon Next may define review methods for external runtimes, tool hosts, AI workspaces, connector hosts and model-serving surfaces.

Such review methods may classify:

- system role;
- exposure posture;
- privileged capability surface;
- data access;
- external effects;
- memory effects;
- model effects;
- scheduling effects;
- host-control surface;
- untrusted content paths;
- evidence and approval expectations.

They must not scan, sandbox, install, configure, execute, approve, promote memory or become an operations tool.

## Model capability passport module

Pantheon Next may define model-specific capability passport fields.

A model passport may classify:

- model identity;
- provider or runtime;
- local, external or hybrid processing posture;
- modality and context limits;
- input and output classes;
- data exposure;
- task-family suitability;
- professional-use ceiling;
- evidence expectations;
- known failure modes;
- approval ceiling;
- memory behavior.

A model passport must not route, serve, download, benchmark, select or execute a model. Those behaviors belong to an external runtime or adapter.

## External runtime memory adapter module

Pantheon Next may define adapter boundaries for external runtime memory tools.

Such tools may support:

- semantic recall;
- temporal graph memory;
- conversation or dossier memory;
- agent runtime state;
- checkpoint and resume;
- trace observation;
- loop detection;
- context assembly.

They remain external.

They may return Register Candidates, Evidence Pack Candidates, Trace References, Runtime State References or Review Queue signals.

They must not approve, validate, promote a Registre Probatoire entry, decide scope, authorize external effects or become a Pantheon runtime.

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
