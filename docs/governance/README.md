# Governance Index

This directory contains the canonical governance references for Pantheon Next.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next is governance-first.

Pantheon Next is not an autonomous runtime.

## Repository state

This repository is under controlled bootstrap, conceptual stabilization and selective distillation from Pantheon-OS.

Some documents are active doctrine.

Some documents are migrated doctrine.

Some documents are narrative, visual, product, editorial or inspiration support doctrine.

Some documents are stub placeholders only.

Some implementation areas are still absent.

Always verify `STATUS.md` before treating a document as canonical migrated doctrine.

---

# Read order

For repository work, read in this order.

## Core bootstrap

1. `ai_logs/README.md`
2. `docs/governance/STATUS.md`
3. `README.md`
4. `CHANGELOG.md`
5. `docs/governance/ARCHITECTURE.md`
6. `docs/governance/MODULES.md`
7. `docs/governance/AGENTS.md`
8. `docs/governance/MEMORY.md`
9. `docs/governance/APPROVALS.md`
10. `docs/governance/TASK_CONTRACTS.md`
11. `docs/governance/TASK_CONTRACT_REVISIONS.md`
12. `docs/governance/EXECUTION_DISCIPLINE.md`
13. `docs/governance/EVIDENCE_PACK.md`
14. `docs/governance/HERMES_INTEGRATION.md`
15. `docs/governance/OPENWEBUI_INTEGRATION.md`
16. `docs/governance/EXTERNAL_TOOLS_POLICY.md`
17. `docs/governance/KNOWLEDGE_TAXONOMY.md`
18. `docs/governance/CODE_AUDIT_POST_PIVOT.md`
19. `docs/assets/README.md`

## Conceptual stabilization support

After the core bootstrap order, read:

- `docs/governance/CONCEPTUAL_STABILIZATION.md`;
- `docs/governance/NARRATIVE.md`;
- `docs/governance/VISUAL_LANGUAGE.md`;
- `docs/governance/SCOPE_ISOLATION.md`;
- `docs/governance/GOVERNANCE_COLLEGE.md`;
- `docs/governance/USER_DECISION_GATE.md`.

These documents clarify Phase S doctrine, the non-runtime narrative layer, scope compartmentalization, role separation, governed tensions and human decision escalation.

## Product and editorial positioning support

For product differentiation, market positioning and public-facing language, also read:

- `docs/governance/PRODUCT_DIFFERENTIATION.md`;
- `docs/governance/EDITORIAL_LANGUAGE.md`.

These documents define product and editorial support doctrine only.

They do not define implementation, runtime behavior, a plugin, a provider router, a scheduler, a queue or an execution system.

## Document workflow support

For governed professional document production, also read:

- `docs/governance/MARKDOWN_DOSSIER_WORKFLOW.md`.

This document defines a Markdown dossier workflow proposal.

It is documentation-level governance only.

It does not implement an editor, runtime, plugin, OpenWebUI extension or Hermes tool.

## RAG ingestion support

For governed PDF and document preparation for RAG, also read:

- `docs/governance/RAG_INGESTION_PIPELINE.md`.

This document defines a RAG ingestion governance proposal.

It is documentation-level governance only.

It does not implement PDF parsing, OCR, chunking, indexing, an OpenWebUI plugin, a Hermes tool, a scheduler, a queue or an ingestion runtime.

## Inspiration support

For external repository inspiration, agentic pattern distillation and skill watchlist posture, also read:

- `docs/governance/EXTERNAL_REPO_INSPIRATIONS.md`;
- `docs/governance/EXTERNAL_AGENTIC_INSPIRATIONS.md`;
- `docs/governance/SKILL_WATCHLIST.md`.

These documents map external projects, agentic systems and skill ecosystems that may inspire Pantheon design.

They are support doctrine only.

They do not add dependencies, approve integrations, approve skills or define runtime implementation.

---

# Documents present

## Migrated from Pantheon-OS

- `ARCHITECTURE.md`;
- `MODULES.md`;
- `CODE_AUDIT_POST_PIVOT.md`;
- `TASK_CONTRACT_REVISIONS.md`;
- `EXECUTION_DISCIPLINE.md`.

These documents have been distilled into Pantheon Next governance doctrine.

They do not introduce runtime behavior.

## Active governance documents

- `STATUS.md`;
- `ROADMAP.md`;
- `MIGRATION_PLAYBOOK.md`;
- `ARCHITECTURE.md`;
- `MODULES.md`;
- `CODE_AUDIT_POST_PIVOT.md`;
- `TASK_CONTRACTS.md`;
- `TASK_CONTRACT_REVISIONS.md`;
- `EXECUTION_DISCIPLINE.md`;
- `AGENTS.md`;
- `GOVERNANCE_COLLEGE.md` (`Governance College`);
- `USER_DECISION_GATE.md` (`User Decision Gate`);
- `GLOSSARY.md`;
- `REPOSITORY_SIMPLIFICATION_PLAN.md`;
- `EXTERNAL_AI_OPTION_REVIEWS.md`;
- `CONCEPTUAL_STABILIZATION.md`;
- `EVIDENCE_PACK.md`;
- `MEMORY.md`;
- `APPROVALS.md`;
- `WORKFLOW_SCHEMA.md` (`Workflow Manifest`);
- `RUN_GRAPH.md` (`Run Trace View`);
- `REQUEST_ORCHESTRATION.md` (`Request Coordination`);
- `HERMES_INTEGRATION.md`;
- `OPENWEBUI_INTEGRATION.md`;
- `EXTERNAL_TOOLS_POLICY.md`;
- `KNOWLEDGE_TAXONOMY.md`;
- `SCOPE_ISOLATION.md`;
- `MARKDOWN_DOSSIER_WORKFLOW.md` (`Markdown Dossier Workflow`);
- `RAG_INGESTION_PIPELINE.md` (`RAG Ingestion Pipeline`).

## Active product, editorial, narrative, visual and inspiration support documents

These documents explain, position, stabilize or support Pantheon Next without defining runtime behavior.

- `PRODUCT_DIFFERENTIATION.md`;
- `EDITORIAL_LANGUAGE.md`;
- `NARRATIVE.md`;
- `VISUAL_LANGUAGE.md`;
- `EXTERNAL_REPO_INSPIRATIONS.md`;
- `EXTERNAL_AGENTIC_INSPIRATIONS.md`;
- `SKILL_WATCHLIST.md`.

## Stub present — non implemented

These files exist only as migration placeholders or unreconciled migration targets.

They are not canonical migrated doctrine yet.

- `MODEL_ROUTING_POLICY.md`;
- `ROUTING_FOUNDATION.md`;
- `MEMORY_EVENT_SCHEMA.md`;
- `ROLE_SIGNALS.md`;
- `WORKFLOW_ADAPTATION.md`;
- `SKILL_LIFECYCLE.md`;
- `ROLE_SIGNAL_PROFILES.md`;
- `OPENWEBUI_DOMAIN_MAPPING.md`;
- `OPENWEBUI_PLUGIN_POLICY.md`;
- `EPISTEMIC_CONTROL.md`;
- `EPISTEMIC_CONTROL_PROPAGATION.md`;
- `EXTERNAL_RUNTIME_OPTIONS.md`;
- `docs/assets/README.md`.

---

# Implementation areas

Schemas are present as an initial baseline but are not yet backed by repository tests.

Operations tooling is not implemented.

Tests are not implemented.

---

# Boundary rule

No governance document may introduce:

- autonomous execution runtime;
- hidden scheduler;
- queue system;
- provider router runtime;
- automatic memory promotion;
- hidden workflow execution;
- automatic Hermes profile installation;
- automatic skill installation;
- agent self-approval.

Any proposal introducing these patterns must be classified as runtime-drift risk.

---

# Execution discipline boundary

`EXECUTION_DISCIPLINE.md` defines smallest-safe-path and contribution discipline.

It does not implement execution, scheduling, queueing, provider routing, workflow running, automatic retries or self-healing.

Hermes executes externally under a bounded frame.

Pantheon governs status, evidence, scope and procedure.

---

# Task Contract revision boundary

`TASK_CONTRACT_REVISIONS.md` defines how a Task Contract may be revised, paused, resumed, reset or closed.

It does not implement workflow execution, automatic retries, automatic resume, approval automation or hidden runtime mutation.

Hermes may execute only inside an approved current frame.

OpenWebUI may expose the decision.

Pantheon governs the status and procedure.

---

# Role and decision boundary

`AGENTS.md` defines Pantheon Roles as canonical governance roles, not executable agents.

`GOVERNANCE_COLLEGE.md` defines how Pantheon Roles operate as separated governance viewpoints, useful tensions, negative powers and procedural arbitration.

`USER_DECISION_GATE.md` defines when Pantheon must expose discord and request human decision.

None of these documents defines a runtime, multi-agent execution, autonomous debate system, message bus, hidden orchestration or automatic approval loop.

---

# Editorial boundary

`EDITORIAL_LANGUAGE.md` defines public-facing vocabulary, syntax and title guidance.

It is an editorial support document.

It does not redefine governance doctrine, implementation status, runtime architecture or approval rules.

Public-facing text should start from professional risks, dossier status and decision consequences before technical architecture.

---

# Narrative boundary

The city-game metaphor is allowed only as an explanatory layer.

It must not redefine Pantheon Next as a game engine, execution engine, autonomous city, hidden workflow runner or self-governing agent system.

The narrative sentence remains:

```text
L'IA ouvre les possibles.
Pantheon les organise.
L'humain décide.
Le validé reste.
```

---

# Product boundary

`PRODUCT_DIFFERENTIATION.md` defines product doctrine.

It positions Pantheon Next as a governed configuration, evidence and decision-memory layer around OpenWebUI and Hermes.

It must not be read as a mandate to build a runtime, plugin marketplace, provider router, scheduler, queue, autonomous agent system or OpenWebUI/Hermes replacement.

---

# Workflow boundary

Workflow vocabulary is allowed only as governance vocabulary.

`WORKFLOW_SCHEMA.md` defines a Workflow Manifest.

`RUN_GRAPH.md` defines a Run Trace View.

`REQUEST_ORCHESTRATION.md` defines Request Coordination.

`MARKDOWN_DOSSIER_WORKFLOW.md` defines a governed professional document workflow for Markdown dossiers.

`RAG_INGESTION_PIPELINE.md` defines governed source preparation for RAG-ready documents.

None of these documents defines execution, scheduling, queueing, provider routing or hidden orchestration.

---

# Code audit boundary

`CODE_AUDIT_POST_PIVOT.md` defines legacy code and runtime-surface audit doctrine.

It is a classification register and migration safety document.

It does not mean the listed historical routes, apps, workers, queues, Docker files or CI details exist in Pantheon Next.

It does not authorize their reuse.

It does not implement a Doctor.

---

# Integration, tools, knowledge and scope boundary

`HERMES_INTEGRATION.md` defines the external execution boundary.

`OPENWEBUI_INTEGRATION.md` defines the cockpit and exposure boundary.

`EXTERNAL_TOOLS_POLICY.md` defines external capability governance.

`KNOWLEDGE_TAXONOMY.md` defines the categories of source, knowledge, context, evidence, memory, doctrine and runtime state.

`SCOPE_ISOLATION.md` defines compartmentalization across session, task, dossier, project, domain, user, organization, repository, governance and system scope.

None of these documents defines runtime ownership, provider routing, a plugin manager, automatic memory promotion or OpenWebUI as source of truth.

---

# Inspiration boundary

`EXTERNAL_REPO_INSPIRATIONS.md`, `EXTERNAL_AGENTIC_INSPIRATIONS.md` and `SKILL_WATCHLIST.md` record external repositories, agentic systems and skills that may inspire Pantheon design.

They must not be treated as:

- dependency list;
- skill approval list;
- integration approval;
- implementation roadmap;
- runtime architecture;
- plugin registry;
- vendor selection;
- external tooling mandate.

External repositories and skills remain inspirations until a separate governed adoption decision exists.
