# Pantheon Next Roadmap

Pantheon Next is a governance-first repository with minimal read-only tooling planned.

This roadmap defines controlled migration and stabilization phases. It must not be interpreted as a runtime implementation plan.

## Doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next must not recreate an autonomous execution engine, agent runtime, tool runtime, scheduler, queue, provider router, hidden workflow runtime, plugin manager, module runtime, automatic skill installer or automatic memory promoter.

## Phase 0 — Clean repository bootstrap

Status: implemented.

Implemented:

- repository baseline;
- root README and French README;
- license, version and changelog;
- AI log directory and rules;
- legacy area marker;
- initial governance entry points.

## Phase 1 — Canonical governance baseline

Status: partial but coherent.

Goals:

- migrate or distill governance Markdown from Pantheon-OS selectively;
- keep `docs/governance/AGENTS.md` as the canonical Pantheon Role registry;
- avoid governance duplication in Hermes profile folders;
- preserve the OpenWebUI / Hermes / Pantheon boundary;
- keep stubs clearly marked until migrated or closed;
- preserve future modularity without creating a plugin manager or runtime registry.

Migrated from Pantheon-OS:

- `docs/governance/ARCHITECTURE.md`;
- `docs/governance/MODULES.md`;
- `docs/governance/CODE_AUDIT_POST_PIVOT.md`;
- `docs/governance/TASK_CONTRACT_REVISIONS.md`;
- `docs/governance/EXECUTION_DISCIPLINE.md`;
- `docs/governance/ROLE_SIGNALS.md`.

Implemented active doctrine includes:

- `docs/governance/README.md`;
- `docs/governance/STATUS.md`;
- `docs/governance/ROADMAP.md`;
- `docs/governance/MIGRATION_PLAYBOOK.md`;
- `docs/governance/AGENTS.md`;
- `docs/governance/GOVERNANCE_COLLEGE.md`;
- `docs/governance/USER_DECISION_GATE.md`;
- `docs/governance/APPROVALS.md`;
- `docs/governance/TASK_CONTRACTS.md`;
- `docs/governance/TASK_CONTRACT_REVISIONS.md`;
- `docs/governance/EXECUTION_DISCIPLINE.md`;
- `docs/governance/ROLE_SIGNALS.md`;
- `docs/governance/EVIDENCE_PACK.md`;
- `docs/governance/MEMORY.md`;
- `docs/governance/MODULES.md`;
- `docs/governance/MODULE_ACTIVATION.md`;
- `docs/governance/WORKFLOW_SCHEMA.md`;
- `docs/governance/RUN_GRAPH.md`;
- `docs/governance/REQUEST_ORCHESTRATION.md`;
- `docs/governance/MARKDOWN_DOSSIER_WORKFLOW.md`;
- `docs/governance/RAG_INGESTION_PIPELINE.md`;
- `docs/governance/HERMES_INTEGRATION.md`;
- `docs/governance/OPENWEBUI_INTEGRATION.md`;
- `docs/governance/EXTERNAL_TOOLS_POLICY.md`;
- `docs/governance/KNOWLEDGE_TAXONOMY.md`;
- `docs/governance/SCOPE_ISOLATION.md`;
- `docs/governance/CONTEXT_PACKS.md`.

Implemented support doctrine includes:

- `docs/governance/PRODUCT_DIFFERENTIATION.md`;
- `docs/governance/EDITORIAL_LANGUAGE.md`;
- `docs/governance/NARRATIVE.md`;
- `docs/governance/VISUAL_LANGUAGE.md`;
- `docs/governance/EXTERNAL_REPO_INSPIRATIONS.md`;
- `docs/governance/EXTERNAL_AGENTIC_INSPIRATIONS.md`;
- `docs/governance/reference_reviews/README.md`;
- `docs/governance/reference_reviews/LANGGRAPH.md`;
- `docs/governance/WATCHLIST.md`;
- `docs/governance/REFERENCE_BOUNDARIES.md`;
- `docs/governance/ECOSYSTEM_MAP.md`;
- `docs/governance/DISTILLATION_REGISTRY.md`;
- `docs/governance/REJECTED_PATTERNS.md`;
- `docs/governance/EXTERNAL_METHOD_REVIEWS.md`;
- `docs/governance/TENSIONS_AND_RISKS.md`;
- `docs/governance/SKILL_WATCHLIST.md`;
- `docs/examples/README.md`.

### Module activation chain

Status: documented at support-doctrine level, not implemented.

Purpose:

```text
detect capability availability
activate governed capability by scope
authorize capability per Task Contract
compute Effective Policy for review and future UI exposure
```

Core distinction:

```text
Detected does not mean enabled.
Enabled does not mean authorized for a task.
Authorized for a task does not mean sovereign.
```

`MODULE_ACTIVATION.md` defines:

- detection records;
- activation records;
- task authorization records;
- status vocabulary;
- scope levels;
- mandatory rules;
- optional rules;
- Effective Policy examples;
- UI control boundaries;
- LangGraph as first example of a Hermes runtime candidate.

This is not a module registry implementation.

It is not a UI implementation.

It is not a plugin manager.

It is not an execution runtime.

### External reference governance chain

Status: documented at support-doctrine level, not implemented.

Purpose:

```text
observe external references
understand their boundaries
decide what can be distilled or rejected
preserve recurring tensions
```

Documents:

| Function | Documents |
|---|---|
| Observe | `WATCHLIST.md`, `SKILL_WATCHLIST.md` |
| Understand | `REFERENCE_BOUNDARIES.md`, `ECOSYSTEM_MAP.md`, `reference_reviews/` |
| Decide | `DISTILLATION_REGISTRY.md`, `REJECTED_PATTERNS.md`, `EXTERNAL_METHOD_REVIEWS.md` |
| Preserve | `TENSIONS_AND_RISKS.md` |

This chain is not an adoption workflow, dependency system or runtime roadmap.

It does not approve integrations, tools, plugins, MCP servers, observability platforms, GraphRAG runtimes, LangGraph runtimes, skills or provider gateways.

The governing rule is:

```text
Pattern distillation is allowed.
Runtime migration is not.
```

### External agent pattern keepers

Status: roadmap distillation only.

Keep only patterns that strengthen governance:

- constitution over prompt;
- negative scope definition;
- capability map before component map;
- reversibility-based approval;
- cache, context, source, evidence and memory separation;
- Memory Candidate discipline;
- skill specification with `FOR` and `NOT FOR`;
- mandatory dissent and contradiction preservation;
- freshness disclosure;
- correction as specification debt;
- regression review for governance behavior;
- periodic governance audit.

Rejected:

- persistent personal agent as the system center;
- proactive headless jobs, schedulers or autonomous routines inside Pantheon;
- unrestricted email, calendar, business-data or private-data access;
- self-learning loops, auto-save behavior or auto-promoted memory;
- automatic skill installation, marketplace adoption or plugin import;
- hidden council, swarm intelligence or autonomous debate runtime;
- direct OpenWebUI storage browsing by Hermes without bounded scope;
- any architecture where Pantheon executes instead of governing.

### External tool and professional verticalization keepers

Status: roadmap distillation only.

Keep from verified tool-factory patterns:

- verified external tool candidates before exposure;
- proof artifacts for generated or discovered capabilities;
- dry-run defaults before write-capable tool use;
- lockfile, hash and semantic drift detection for external specifications;
- deterministic snapshot and replay for tool behavior tests;
- tool scorecards that separate technical readiness from governance approval;
- explicit non-goals for anti-bot bypass, CAPTCHA solving and terms-of-service violations;
- distinction between generated tool, verification proof, installation state, allowed use and governed approval.

Rejected from tool-factory patterns:

- internal Pantheon tool factory;
- MCP server or MCP router inside Pantheon;
- automatic tool generation, installation or exposure;
- automatic skill installation;
- catalog or registry treated as marketplace;
- tool availability treated as authorization;
- technical proof treated as business, professional or governance approval.

Keep from professional verticalization patterns:

- domain-specific playbooks and practice profiles;
- cold-start interview to capture professional context, house style, escalation rules and seed documents;
- draft-only output posture for regulated or liability-sensitive domains;
- explicit professional review gate before reliance, filing, publication, transmission or external effect;
- source attribution and citation verification posture;
- visible jurisdiction, scope and assumption declarations;
- conservative handling of privilege, confidentiality and subjective professional judgment;
- connector trust layer with restrictive default allowlist;
- skill QA before use or recommendation;
- install or capability log for auditability;
- freshness gate for bundled references, procedures, regulations and playbooks.

Rejected from professional verticalization patterns:

- legal or professional agents as autonomous authorities;
- scheduled agents inside Pantheon;
- managed-agent orchestration inside Pantheon;
- connector access without Task Contract scope;
- community skill marketplace;
- skill installer, recommender or auto-updater;
- professional outputs treated as advice without review;
- playbook drift promoted into doctrine or memory without governed review.

Still to migrate or reconcile from stubs:

- `docs/governance/MODEL_ROUTING_POLICY.md`;
- `docs/governance/ROUTING_FOUNDATION.md`;
- `docs/governance/MEMORY_EVENT_SCHEMA.md`;
- `docs/governance/WORKFLOW_ADAPTATION.md`;
- `docs/governance/SKILL_LIFECYCLE.md`;
- `docs/governance/ROLE_SIGNAL_PROFILES.md`;
- `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`;
- `docs/governance/OPENWEBUI_PLUGIN_POLICY.md`;
- `docs/governance/EPISTEMIC_CONTROL.md`;
- `docs/governance/EPISTEMIC_CONTROL_PROPAGATION.md`;
- `docs/governance/EXTERNAL_RUNTIME_OPTIONS.md`;
- `docs/assets/README.md`.

## Phase 2 — Hermes profile templates

Status: implemented as candidate-only templates.

Implemented profiles:

- `athena-agent`;
- `argos-agent`;
- `themis-agent`;
- `apollo-agent`;
- `zeus-agent`;
- `iris-agent`;
- `hephaistos-agent`.

Implemented base and candidate files:

- `hermes/profiles/_base/base-soul-rules.md`;
- `hermes/profiles/_base/LANGGRAPH_RUNTIME_CANDIDATE.md`.

These are profile or runtime-candidate templates only.

They are not installed, deployed, executed or granted governance authority by Pantheon Next.

## Phase 3 — Schemas and examples

Status: initial baseline present, not fully reconciled or tested.

Implemented schema files:

- `schemas/README.md`;
- `schemas/task_contract.schema.yaml`;
- `schemas/task_contract_revision.schema.yaml`;
- `schemas/evidence_pack.schema.yaml`;
- `schemas/memory_candidate.schema.yaml`;
- `schemas/role_signal.schema.yaml`;
- `schemas/workflow_manifest.schema.yaml`;
- `schemas/skill_manifest.schema.yaml`;
- `schemas/examples/`.

Implemented example area:

- `docs/examples/README.md`;
- `docs/examples/architecture_devis_reprise/`;
- `docs/examples/regulatory_watch_conflict/`;
- `docs/examples/legal_note/`;
- `docs/examples/medical_letter/`;
- `docs/examples/PRACTITIONER_HOOKS.md`.

Remaining work:

- reconcile schema fields against active Markdown doctrine;
- add tests for schema validation;
- keep examples fictional, non-advisory and clearly marked as educational support;
- review legal and medical examples with relevant professionals before treating them as stable use-case doctrine.

## Phase 4 — Read-only tooling

Status: not implemented.

Allowed future scope:

- read-only Doctor checks;
- governance reference validation;
- schema validation command;
- stub/migration status checks;
- forbidden-runtime surface checks;
- external-reference boundary checks;
- module-activation consistency checks.

Forbidden scope:

- runtime execution;
- workflow start;
- tool invocation;
- provider routing;
- memory promotion;
- external-reference adoption;
- skill installation;
- module activation by automation;
- scheduler or queue behavior;
- automatic remediation.

## Phase 5 — Context packs, module controls and integration specs

Status: documented at doctrine level, not implemented.

Current documents define the boundary for:

- OpenWebUI as cockpit and exposure surface;
- Hermes Agent as external execution runtime;
- Context Pack handoff;
- Evidence Pack return;
- Memory Candidate discipline;
- future read-only scoped knowledge gateway;
- future module-control UI semantics.

Remaining work:

- design a sample Context Pack;
- design a sample Evidence Pack returned from Hermes;
- design a visible User Decision Gate example for OpenWebUI exposure;
- design a non-executable module Effective Policy display mock;
- avoid direct Hermes access to raw OpenWebUI storage.

## Phase 6 — Optional read-only Domain API

Status: deferred.

A future API may expose governance-only read surfaces such as:

- governance snapshot;
- role registry read;
- policy read;
- context-pack export;
- module effective policy read;
- schema read;
- support-doctrine index read.

It must not expose:

- execution;
- workflow start;
- provider routing;
- tool dispatch;
- memory promotion;
- external-reference adoption;
- module activation;
- scheduling;
- queueing.

## Current risks

- governance migration remains incomplete;
- stubs may be mistaken for migrated doctrine;
- schema presence may be mistaken for tested validation coverage;
- examples may be mistaken for implemented workflows or professional advice;
- active integration doctrine may be mistaken for runtime integration;
- Hermes profile templates may be mistaken for installed agents;
- LangGraph runtime candidate template may be mistaken for approved installation;
- Module Activation doctrine may be mistaken for implemented UI, plugin manager, module registry or runtime policy engine;
- Effective Policy examples may be mistaken for executable enforcement;
- external personal-agent patterns may be mistaken for approved Pantheon architecture;
- pattern keepers may be mistaken for authorization to create autonomous timing loops, auto-learning, auto-memory or skill marketplace behavior;
- external-reference support documents may be mistaken for dependency adoption, vendor endorsement, runtime migration, implementation backlog or automatic enforcement;
- verified tool-factory patterns may be mistaken for authorization to build a Pantheon tool factory or MCP runtime;
- professional verticalization patterns may be mistaken for authorization to create autonomous legal, medical or regulated-profession agents;
- Task Contract revision doctrine may be mistaken for automatic workflow resume;
- Execution Discipline may be mistaken for internal execution capability;
- Role Signals may be mistaken for an agent message bus or hidden debate runtime;
- future migrations may accidentally reintroduce runtime-oriented architecture.

## Next recommended sequence

1. Continue controlled migration one file at a time under `MIGRATION_PLAYBOOK.md`.
2. Reconcile schemas against active Markdown doctrine.
3. Add read-only schema and governance tests.
4. Add read-only Doctor tooling only after the target checks are stable.
5. Distill external agent patterns only into governed pattern cards, checklist items or Hermes candidate constraints, never into Pantheon runtime behavior.
6. Distill external tool-factory and professional verticalization patterns only into governed pattern cards, example constraints, skill QA checklists or Hermes candidate constraints, never into Pantheon execution behavior.
7. Use the external-reference support chain before adding any new external inspiration: watch, bound, map, distill or reject, then preserve the tension when it remains useful.
8. Use `MODULE_ACTIVATION.md` before designing future UI controls for detected, enabled or task-authorized capabilities.