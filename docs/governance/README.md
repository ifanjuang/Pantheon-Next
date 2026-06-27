# Governance Index

This directory contains the governance references for Pantheon Next.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next is governance-first. It is not an autonomous runtime.

## How this index works

This file is the **entry point and read path**. It does not re-list or re-classify every document — that would duplicate three authoritative files:

- `STATUS.md` — current posture and live exceptions (candidate / to verify).
- `AUTHORITY_INDEX.md` — authority class and status of each item.
- `MODULES.md` — module map (authority document + boundary per governance area).

```text
For "what state is this in?" → STATUS.md
For "what authority does this have?" → AUTHORITY_INDEX.md
For "which area owns this?" → MODULES.md
For "what do I read, in what order?" → this file
```

Always verify `STATUS.md` before treating a document as canonical.

---

# Read order

## Short stable path

1. `ai_logs/README.md`
2. `docs/governance/STATUS.md`
3. `docs/governance/CORE_CONCEPTS_MAP.md`
4. `docs/governance/TERMINOLOGY_BOUNDARIES.md`
5. `docs/governance/COMPETENCE_MODEL.md`
6. `README.md`
7. `CHANGELOG.md`
8. `docs/governance/AGENTS.md`
9. `docs/governance/TASK_CONTRACTS.md`
10. `docs/governance/DOSSIER_SITUATION_INTAKE.md`
11. `docs/governance/WORKFLOW_FORGING_PROTOCOL.md`
12. `docs/governance/CONTEXT_PACKS.md`
13. `docs/governance/CONTEXT_STACK.md`
14. `docs/governance/CARD_STACK_MODEL.md`
15. `docs/governance/CARD_STACK_ROLE_QUALITY_ALIGNMENT.md`
16. `docs/governance/CARD_STACK_KNOWLEDGE_CORPUS_ALIGNMENT.md`
17. `docs/governance/EVIDENCE_PACK.md`
18. `docs/governance/EVIDENCE_TOPOLOGY_GATE.md`
19. `docs/governance/APPROVALS.md`
20. `docs/governance/MEMORY.md`
21. `docs/governance/OPENWEBUI_INTEGRATION.md`
22. `docs/governance/HERMES_INTEGRATION.md`
23. `docs/governance/EXTERNAL_TOOLS_POLICY.md`

## Core bootstrap

For full repository work:

1. `ai_logs/README.md`
2. `docs/governance/STATUS.md`
3. `docs/governance/CORE_CONCEPTS_MAP.md`
4. `docs/governance/TERMINOLOGY_BOUNDARIES.md`
5. `docs/governance/COMPETENCE_MODEL.md`
6. `README.md`
7. `CHANGELOG.md`
8. `docs/governance/ARCHITECTURE.md`
9. `docs/governance/MODULES.md`
10. `docs/governance/MODULE_ACTIVATION.md`
11. `docs/governance/ROLE_ACTIVATION.md`
12. `docs/governance/AGENTS.md`
13. `docs/governance/ROLE_SIGNALS.md`
14. `docs/governance/MEMORY.md`
15. `docs/governance/APPROVALS.md`
16. `docs/governance/TASK_CONTRACTS.md`
17. `docs/governance/DOSSIER_SITUATION_INTAKE.md`
18. `docs/governance/WORKFLOW_FORGING_PROTOCOL.md`
19. `docs/governance/WORKFLOW_LIFECYCLE.md`
20. `docs/governance/TASK_CONTRACT_REVISIONS.md`
21. `docs/governance/EXECUTION_DISCIPLINE.md`
22. `docs/governance/EVIDENCE_PACK.md`
23. `docs/governance/EVIDENCE_TOPOLOGY_GATE.md`
24. `docs/governance/HERMES_INTEGRATION.md`
25. `docs/governance/OPENWEBUI_INTEGRATION.md`
26. `docs/governance/OPENWEBUI_TEMPLATES.md`
27. `docs/governance/EXTERNAL_TOOLS_POLICY.md`
28. `docs/governance/KNOWLEDGE_TAXONOMY.md`
29. `docs/governance/SCOPE_ISOLATION.md`
30. `docs/governance/CONTEXT_PACKS.md`
31. `docs/governance/CONTEXT_STACK.md`
32. `docs/governance/CARD_STACK_MODEL.md`
33. `docs/governance/CARD_STACK_ROLE_QUALITY_ALIGNMENT.md`
34. `docs/governance/CARD_STACK_KNOWLEDGE_CORPUS_ALIGNMENT.md`
35. `docs/governance/CODE_AUDIT_POST_PIVOT.md`
36. `docs/assets/README.md`

## Terminology boundaries

Before vocabulary cleanup, document naming, UI labels, schema naming proposals or external tool placement work, read:

- `TERMINOLOGY_BOUNDARIES.md` — controlled vocabulary, reserved runtime terms, aliases and migration rules.
- `COMPETENCE_MODEL.md` — candidate model separating Connaissance, Guide/Ressource de compétence, Compétence, Template, Hermes Skill, Tool, Evidence, Action and Gate.
- `EDITORIAL_LANGUAGE.md` — public-facing wording and professional language.
- `CORE_CONCEPTS_MAP.md` — compact relationship map for core governance concepts.

```text
Use Case / Affaire for the professional unit.
Use Approach / Démarche for the governed reusable handling of a Situation.
Use Capability / Capacité for abstract governable effect classes.
Use Competence / Compétence for governed reusable abilities.
Use Connaissance for non-project documentary corpus such as PLU, MAF recommendations, CCTP guides, lexicons, professional references and agency doctrine.
Use Guide/Ressource de compétence for documentation, manuals, wiki pages, examples or files used to learn or operate a competence.
Reserve Workflow, Skill, Tool, Job, Action and State for execution.
Reserve Recall for runtime memory output and Register for validated memory.
```

## Placement and modular orientation

Before capability, domain or module placement work, read:

- `CAPABILITY_PLACEMENT.md`, `MODULAR_DOMAIN_REORIENTATION.md`, `ADAPTERS_AND_BINDINGS.md` — where capabilities live, the tool-agnostic body, the manifest/envelope and the blueprint-in-Pantheon / adapter-outside model.
- `EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` — generic boundary for external runtime memory, checkpoint, graph recall and observability adapters.
- `MODULE_ACTIVATION.md`, `DOMAIN_PACK_SPEC.md` — activation semantics and domain-pack specification.

`MODULAR_DOMAIN_REORIENTATION.md` reconciles `MODULE_ACTIVATION`, `DOMAIN_PACK_SPEC`, `CAPABILITY_PLACEMENT` and `TASK_CONTRACTS` under one placement model.

## Workflow, intake and role-forged candidates

- `DOSSIER_SITUATION_INTAKE.md` — clarifies the real professional situation before the workflow is forged: request, phase, geography, contract scope, source/version state, relation tension, risk triggers and questions.
- `WORKFLOW_FORGING_PROTOCOL.md` — defines how a Workflow Candidate may be generated on the flow without becoming authorized, durable or externally effective by default.
- `WORKFLOW_LIFECYCLE.md` — candidate lifecycle for workflow modes, authority levels, proposal-before-execution and durable operation boundaries.
- `docs/assets/workflow-under-hood/README.md` and `docs/examples/architecture_erp_effectif_impact_workflow/README.md` — visual and fictional examples only.

```text
Clarify the situation before forging the workflow.
A workflow may be forged automatically.
Its authority is never automatic.
```

## Context composition

- `CONTEXT_PACKS.md` — governed context bundles prepared for a target surface, assistant, runtime or review surface.
- `CONTEXT_STACK.md` — candidate cockpit-facing dynamic context-card stack. It governs visible context composition and HESTIA as a candidate context-watch role; it does not implement a UI, context engine, retrieval engine, approval engine, memory engine or canonical role promotion.

```text
Context prepares work.
Evidence supports review.
Approval legitimizes consequential change.
Memory preserves what was validated.
```

## Card stack and cockpit UX model

- `CARD_STACK_MODEL.md` — candidate, explicitly revisable model for card-based cockpit UX: unique cards, scenes, Workflow Scene, Evidence Scene, Competence Scene, recto/verso card display, constellation navigation, role/rite/place cards and gate visibility.
- `CARD_STACK_ROLE_QUALITY_ALIGNMENT.md` — candidate alignment note for reading role/god cards through the corrected role-quality vocabulary: cards show useful quality expressions, not activated agents or character panels.
- `CARD_STACK_KNOWLEDGE_CORPUS_ALIGNMENT.md` — candidate alignment note defining Connaissance as reusable non-project documentary corpus; project-specific material remains Document/Source, Context, Evidence, Memory Candidate or Register depending on use.

```text
Cards are unique objects.
Scenes are filtered and ordered presentations.
Workflow Scene is exhaustive for cards used in a treatment.
Evidence Scene is scoped by project and subject.
Competence Scene is global and neutral.
Connaissance is documentary corpus outside projects.
Constellation changes project and reveals the graph.
Gates expose decision status.
Role / God cards show expressed qualities, not autonomous roles.
```

This model is documented non-implemented and remains open for Claude, ChatGPT and human review before any promotion.

## Architecture method and role-quality cluster

The following architecture-domain documents are candidate support doctrine. They stabilize vocabulary and response discipline for professional architecture methods, but do not implement role executors, workflow engines, UI, approval engines, senders, memory engines or runtime behavior:

- `ARCHITECTURE_METHOD_TAXONOMY.md` — method, approach, discipline, strategy, procedure, tactic and reflex vocabulary.
- `ARCHITECTURE_ROLE_REFLEX_COORDINATION.md` — role-owned reflexes, consultations, rites and Zeus arbitration without agent loops.
- `ARCHITECTURE_ROLE_FACETS.md` — role-quality model: jurisdictions are protected fields, facets are qualities.
- `ARCHITECTURE_ROLE_ACTIVATION_MODEL.md` — historical filename for the current Role Expression Model; roles are permanent guardians and qualities express contextually.

```text
The method advances.
The role guards.
The quality expresses.
The reflex alerts.
The gate exposes.
The human decides.
```

## Evidence topology

- `EVIDENCE_TOPOLOGY_GATE.md`, `EVIDENCE_TOPOLOGY_CHECKLIST.md`, `EVIDENCE_TOPOLOGY_ROADMAP.md`, `EVIDENCE_TOPOLOGY_RECONCILIATION.md`, `EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md`, `EVIDENCE_TOPOLOGY_BRIDGES.md`, `evidence_topology_antipatterns/README.md`, `docs/examples/evidence_topology/README.md`.

```text
The unit of reasoning is not the agent.
The unit of reasoning is the proof chain.
```

## Conceptual, rites and human decision

- `CONCEPTUAL_STABILIZATION.md`, `GOVERNANCE_COLLEGE.md`, `USER_DECISION_GATE.md`, `DECISION_SURFACE_SPEC.md`, `SCOPE_ISOLATION.md`, `CONTEXT_PACKS.md`, `CONTEXT_STACK.md`, `CARD_STACK_MODEL.md`, `CARD_STACK_ROLE_QUALITY_ALIGNMENT.md`, `CARD_STACK_KNOWLEDGE_CORPUS_ALIGNMENT.md`, `DOMAIN_PACK_SPEC.md`, `ARCHITECTURE_METHOD_TAXONOMY.md`, `ARCHITECTURE_ROLE_REFLEX_COORDINATION.md`, `ARCHITECTURE_ROLE_FACETS.md`, `ARCHITECTURE_ROLE_ACTIVATION_MODEL.md`, and `rites/` (`RITE_DIVERGENCE_CONTROLEE`, `AUTOCRITIQUE_CONTRADICTOIRE`, `CONCORDANCE_DES_SOURCES`, `PREMISSES_CACHEES`, `REFONDATION_DE_SESSION`).

```text
Roles judge. Rites coordinate. Task Contracts bound.
Evidence Packs prove. ZEUS states procedure. The human decides.
```

## Dossier, RAG and document workflow

- `MARKDOWN_DOSSIER_WORKFLOW.md`, `RAG_INGESTION_PIPELINE.md`, `RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md`, `DOSSIER_SITUATION_INTAKE.md`, `WORKFLOW_FORGING_PROTOCOL.md`.

## Product, editorial and external references

- Product / editorial: `PRODUCT_DIFFERENTIATION.md`, `EDITORIAL_LANGUAGE.md`, `NARRATIVE.md`, `VISUAL_LANGUAGE.md`.
- External references and boundaries: `EXTERNAL_REPO_INSPIRATIONS.md`, `EXTERNAL_AGENTIC_INSPIRATIONS.md`, `EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md`, `SPICE_REFERENCE_DISTILLATION.md`, `reference_reviews/` (LANGGRAPH, UNDERSTAND_ANYTHING, NANGO, FUTURE_AGI, AGENTOS, …), `UNDERSTAND_ANYTHING_HERMES_ADAPTER.md`, `NANGO_HERMES_CONNECTOR_GATEWAY.md`, `WATCHLIST.md`, `REFERENCE_BOUNDARIES.md`, `ECOSYSTEM_MAP.md`, `DISTILLATION_REGISTRY.md`, `REJECTED_PATTERNS.md`, `EXTERNAL_METHOD_REVIEWS.md`, `TENSIONS_AND_RISKS.md`, `SKILL_WATCHLIST.md`.

```text
observe -> understand -> decide -> preserve
Pattern distillation is allowed. Runtime migration is not.
```

---

# Boundary rule

This is the single boundary statement for the whole directory. Individual documents restate it only where it aids reading.

No governance document may introduce an autonomous execution runtime, hidden scheduler, message/job/agent queue or queue system, provider router runtime, message bus, automatic memory promotion, hidden workflow execution, automatic Hermes profile or skill installation, agent self-approval, topology dispatcher or swarm controller.

External references may inspire vocabulary, pattern cards, evidence expectations, approval thresholds, memory discipline, scope boundaries and candidate constraints. They must not authorize dependency adoption, runtime migration, plugin or skill installation, provider routing, MCP/observability/GraphRAG/LangGraph runtime creation, automatic memory promotion, automatic approval or hidden workflow execution.

Any proposal introducing these patterns is a runtime-drift risk and must be classified as such.

```text
Pantheon defines the contract.
The tools carry the work.
The validated remains.
```

---

# Implementation areas
