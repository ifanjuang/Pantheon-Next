# Pantheon Next Roadmap

Pantheon Next is a governance-first repository with minimal read-only tooling planned.

This roadmap defines controlled migration and stabilization phases. It must not be interpreted as a runtime implementation plan.

## Doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next must not recreate an autonomous execution engine, agent runtime, tool runtime, scheduler, queue, provider router, hidden workflow runtime or automatic skill installer.

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
- keep stubs clearly marked until migrated or closed.

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
- `docs/governance/WATCHLIST.md`;
- `docs/governance/REFERENCE_BOUNDARIES.md`;
- `docs/governance/ECOSYSTEM_MAP.md`;
- `docs/governance/DISTILLATION_REGISTRY.md`;
- `docs/governance/REJECTED_PATTERNS.md`;
- `docs/governance/EXTERNAL_METHOD_REVIEWS.md`;
- `docs/governance/TENSIONS_AND_RISKS.md`;
- `docs/governance/SKILL_WATCHLIST.md`;
- `docs/examples/README.md`.

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
| Understand | `REFERENCE_BOUNDARIES.md`, `ECOSYSTEM_MAP.md` |
| Decide | `DISTILLATION_REGISTRY.md`, `REJECTED_PATTERNS.md`, `EXTERNAL_METHOD_REVIEWS.md` |
| Preserve | `TENSIONS_AND_RISKS.md` |

This chain is not an adoption workflow.

It is not a dependency system.

It is not a runtime roadmap.

It does not approve integrations, tools, plugins, MCP servers, observability platforms, GraphRAG runtimes, LangGraph runtimes, skills or provider gateways.

The governing rule is:

```text
Pattern distillation is allowed.
Runtime migration is not.
```

### External agent pattern keepers

Status: roadmap distillation only.

This section records the minimum patterns to preserve from external personal-agent architecture discussions.

It is not an adoption decision.

It is not a runtime plan.

It is not approval to import a personal agent architecture into Pantheon Next.

Keep only these patterns:

- constitution over prompt: keep doctrine, boundaries and decision constraints stronger than assistant-style instructions;
- negative scope definition: keep explicit lists of what Pantheon is not, especially no runtime, scheduler, router, hidden workflow, auto-learning or auto-memory;
- capability map before component map: describe user-visible capabilities and governance boundaries before selecting tools, runtimes or storage;
- reversibility-based approval: map autonomy to C0-C5 and tool risk T0-T5 through reversibility, external effect and durability;
- cache, context, source, evidence and memory separation: no cache, retrieval result, hot context or repeated observation becomes memory;
- Memory Candidate discipline: every durable claim must define claim, scope, source or evidence, confidence, risk, review horizon and approval state;
- skill specification with `FOR` and `NOT FOR`: apply only to Hermes-side candidate skills, never to a Pantheon skill marketplace or installer;
- mandatory dissent and contradiction preservation: roles must expose source, risk, delivery, transmission and memory tensions instead of smoothing them into consensus;
- freshness disclosure: decision-critical sources and candidates must expose date, version, freshness, staleness or limitation;
- correction as specification debt: repeated corrections may become pattern candidates, memory candidates or skill distillation candidates, but never automatic doctrine;
- regression review for governance behavior: future read-only checks should test boundary discipline and forbidden drift, not execute workflows;
- periodic governance audit: review kept, rejected and stale external patterns, and retire inspirations that no longer constrain decisions.

Rejected from this source:

- persistent personal agent as the system center;
- proactive headless jobs, schedulers or autonomous routines inside Pantheon;
- unrestricted email, calendar, business-data or private-data access;
- self-learning loops, auto-save behavior or auto-promoted memory;
- automatic skill installation, marketplace adoption or plugin import;
- hidden council, swarm intelligence or autonomous debate runtime;
- direct OpenWebUI storage browsing by Hermes without bounded scope;
- any architecture where Pantheon executes instead of governing.

These items may become pattern cards, checklist items or Hermes candidate constraints only after separate governed distillation.

### External tool and professional verticalization keepers

Status: roadmap distillation only.

This section records additional patterns to preserve from external tool-factory and legal-verticalization repositories.

It is not an adoption decision.

It is not a dependency list.

It is not approval to import a tool factory, MCP runtime, plugin marketplace, legal agent suite or managed-agent orchestration into Pantheon Next.

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

These items may become pattern cards, checklist items, example constraints or Hermes candidate constraints only after separate governed distillation.

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

These are profile templates only.

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
- external-reference boundary checks.

Forbidden scope:

- runtime execution;
- workflow start;
- tool invocation;
- provider routing;
- memory promotion;
- external-reference adoption;
- skill installation;
- scheduler or queue behavior;
- automatic remediation.

## Phase 5 — Context packs and integration specs

Status: documented at doctrine level, not implemented.

Current documents define the boundary for:

- OpenWebUI as cockpit and exposure surface;
- Hermes Agent as external execution runtime;
- Context Pack handoff;
- Evidence Pack return;
- Memory Candidate discipline;
- future read-only scoped knowledge gateway.

Remaining work:

- design a sample Context Pack;
- design a sample Evidence Pack returned from Hermes;
- design a visible User Decision Gate example for OpenWebUI exposure;
- avoid direct Hermes access to raw OpenWebUI storage.

## Phase 6 — Optional read-only Domain API

Status: deferred.

A future API may expose governance-only read surfaces such as:

- governance snapshot;
- role registry read;
- policy read;
- context-pack export;
- schema read;
- support-doctrine index read.

It must not expose:

- execution;
- workflow start;
- provider routing;
- tool dispatch;
- memory promotion;
- external-reference adoption;
- scheduling;
- queueing.

## Current risks

- governance migration remains incomplete;
- stubs may be mistaken for migrated doctrine;
- schema presence may be mistaken for tested validation coverage;
- examples may be mistaken for implemented workflows or professional advice;
- active integration doctrine may be mistaken for runtime integration;
- Hermes profile templates may be mistaken for installed agents;
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