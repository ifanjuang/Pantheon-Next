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
- `docs/governance/MODULES.md`.

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
- `docs/governance/EVIDENCE_PACK.md`;
- `docs/governance/MEMORY.md`;
- `docs/governance/WORKFLOW_SCHEMA.md`;
- `docs/governance/RUN_GRAPH.md`;
- `docs/governance/REQUEST_ORCHESTRATION.md`;
- `docs/governance/HERMES_INTEGRATION.md`;
- `docs/governance/OPENWEBUI_INTEGRATION.md`;
- `docs/governance/EXTERNAL_TOOLS_POLICY.md`;
- `docs/governance/KNOWLEDGE_TAXONOMY.md`;
- `docs/governance/SCOPE_ISOLATION.md`.

Implemented support doctrine includes:

- `docs/governance/PRODUCT_DIFFERENTIATION.md`;
- `docs/governance/EDITORIAL_LANGUAGE.md`;
- `docs/governance/NARRATIVE.md`;
- `docs/governance/VISUAL_LANGUAGE.md`;
- `docs/governance/EXTERNAL_REPO_INSPIRATIONS.md`;
- `docs/governance/EXTERNAL_AGENTIC_INSPIRATIONS.md`;
- `docs/governance/SKILL_WATCHLIST.md`;
- `docs/examples/README.md`.

Still to migrate or reconcile from stubs:

- `docs/governance/TASK_CONTRACT_REVISIONS.md`;
- `docs/governance/EXECUTION_DISCIPLINE.md`;
- `docs/governance/MODEL_ROUTING_POLICY.md`;
- `docs/governance/ROUTING_FOUNDATION.md`;
- `docs/governance/CODE_AUDIT_POST_PIVOT.md`;
- `docs/governance/MEMORY_EVENT_SCHEMA.md`;
- `docs/governance/ROLE_SIGNALS.md`;
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
- forbidden-runtime surface checks.

Forbidden scope:

- runtime execution;
- workflow start;
- tool invocation;
- provider routing;
- memory promotion;
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
- schema read.

It must not expose:

- execution;
- workflow start;
- provider routing;
- tool dispatch;
- memory promotion;
- scheduling;
- queueing.

## Current risks

- governance migration remains incomplete;
- stubs may be mistaken for migrated doctrine;
- schema presence may be mistaken for tested validation coverage;
- examples may be mistaken for implemented workflows or professional advice;
- active integration doctrine may be mistaken for runtime integration;
- Hermes profile templates may be mistaken for installed agents;
- future migrations may accidentally reintroduce runtime-oriented architecture.

## Next recommended sequence

1. Review `CODE_AUDIT_POST_PIVOT.md` against post-pivot doctrine.
2. Continue controlled migration one file at a time under `MIGRATION_PLAYBOOK.md`.
3. Reconcile schemas against active Markdown doctrine.
4. Add read-only schema and governance tests.
5. Add read-only Doctor tooling only after the target checks are stable.
