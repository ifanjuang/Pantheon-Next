# Phase C Migration Mapping

This file tracks the migration of governance Markdown from Pantheon-OS into Pantheon-Next during Phase C.

## Snapshot reference

```text
Source archive : legacy/Pantheon-OS-main.zip
Captured in    : Pantheon-Next commit 9c2354b
Snapshot date  : 2026-05-12
```

The archive is the single Phase C snapshot. Later OS evolution is out of scope for Phase C and is handled in a delta pass after Phase C closure (playbook rule D5=a).

OS files referenced below resolve to `<archive root>/Pantheon-OS-main/<path>` inside the snapshot archive.

## Mapping table

| Next path | OS source path | Lot | Migration PR | Status | Notes |
|---|---|---|---|---|---|
| `docs/governance/ARCHITECTURE.md` | `docs/governance/ARCHITECTURE.md` | 1 | `claude/migrate-lot1-architecture` | migrated | 509 → ~250 lines, condensed under D3=a; OS-specific domain identifiers and runtime/install detail dropped; Pantheon OS → Pantheon Next renaming applied; HEPHAISTOS spelling enforced |
| `docs/governance/MODULES.md` | `docs/governance/MODULES.md` | 1 | pending | pending | |
| `docs/governance/GLOSSARY.md` | none | 1 | pending | pending — likely `no-op` per playbook special rule (OS snapshot has no `GLOSSARY.md` under `docs/governance/`) | |
| `docs/governance/APPROVALS.md` | `docs/governance/APPROVALS.md` | 2 | pending | pending | |
| `docs/governance/TASK_CONTRACTS.md` | `docs/governance/TASK_CONTRACTS.md` | 2 | pending | pending | |
| `docs/governance/TASK_CONTRACT_REVISIONS.md` | `docs/governance/TASK_CONTRACT_REVISIONS.md` | 2 | pending | pending | |
| `docs/governance/EVIDENCE_PACK.md` | `docs/governance/EVIDENCE_PACK.md` | 2 | pending | pending | |
| `docs/governance/MEMORY.md` | `docs/governance/MEMORY.md` | 3 | pending | pending | |
| `docs/governance/MEMORY_EVENT_SCHEMA.md` | `docs/governance/MEMORY_EVENT_SCHEMA.md` | 3 | pending | pending | |
| `docs/governance/KNOWLEDGE_TAXONOMY.md` | `docs/governance/KNOWLEDGE_TAXONOMY.md` | 3 | pending | pending | |
| `docs/governance/EPISTEMIC_CONTROL.md` | `docs/governance/EPISTEMIC_CONTROL.md` | 3 | pending | pending | |
| `docs/governance/EPISTEMIC_CONTROL_PROPAGATION.md` | `docs/governance/EPISTEMIC_CONTROL_PROPAGATION.md` | 3 | pending | pending | |
| `docs/governance/ROLE_SIGNALS.md` | `docs/governance/ROLE_SIGNALS.md` | 4 | pending | pending | |
| `docs/governance/ROLE_SIGNAL_PROFILES.md` | `docs/governance/ROLE_SIGNAL_PROFILES.md` | 4 | pending | pending | |
| `docs/governance/WORKFLOW_SCHEMA.md` | `docs/governance/WORKFLOW_SCHEMA.md` | 4 | pending | pending | |
| `docs/governance/WORKFLOW_ADAPTATION.md` | `docs/governance/WORKFLOW_ADAPTATION.md` | 4 | pending | pending | |
| `docs/governance/RUN_GRAPH.md` | `docs/governance/RUN_GRAPH.md` | 4 | pending | pending | |
| `docs/governance/REQUEST_ORCHESTRATION.md` | `docs/governance/REQUEST_ORCHESTRATION.md` | 4 | pending | pending | |
| `docs/governance/EXECUTION_DISCIPLINE.md` | `docs/governance/EXECUTION_DISCIPLINE.md` | 4 | pending | pending | |
| `docs/governance/ROUTING_FOUNDATION.md` | `docs/governance/ROUTING_FOUNDATION.md` | 5 | pending | pending | |
| `docs/governance/MODEL_ROUTING_POLICY.md` | `docs/governance/MODEL_ROUTING_POLICY.md` | 5 | pending | pending | |
| `docs/governance/HERMES_INTEGRATION.md` | `docs/governance/HERMES_INTEGRATION.md` | 6 | pending | pending | |
| `docs/governance/OPENWEBUI_INTEGRATION.md` | `docs/governance/OPENWEBUI_INTEGRATION.md` | 6 | pending | pending | |
| `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md` | `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md` | 6 | pending | pending | |
| `docs/governance/OPENWEBUI_PLUGIN_POLICY.md` | `docs/governance/OPENWEBUI_PLUGIN_POLICY.md` | 6 | pending | pending | |
| `docs/governance/EXTERNAL_TOOLS_POLICY.md` | `docs/governance/EXTERNAL_TOOLS_POLICY.md` | 7 | pending | pending | |
| `docs/governance/EXTERNAL_RUNTIME_OPTIONS.md` | `docs/governance/EXTERNAL_RUNTIME_OPTIONS.md` | 7 | pending | pending | |
| `docs/governance/CODE_AUDIT_POST_PIVOT.md` | `docs/governance/CODE_AUDIT_POST_PIVOT.md` | 7 | pending | pending | |
| `docs/governance/SKILL_LIFECYCLE.md` | `docs/governance/SKILL_LIFECYCLE.md` | 7 | pending | pending | |
| `docs/assets/README.md` | `docs/assets/` (registry) | 8 | pending | pending | |

## OS files not yet bound to a Next stub

The OS snapshot contains additional governance Markdown files that do not have a corresponding Pantheon-Next stub. They are not migrated by default in Phase C. Each will require arbitration before any migration:

- `AI_LOG.md`
- `DELIVERABLE_OPERATING_MODEL.md`
- `DEVELOPMENT_PHASES.md`
- `EVALUATION.md`
- `EXTERNAL_AI_OPTION_REVIEWS.md` (Next already has an active document by the same name)
- `EXTERNAL_ECOSYSTEM_REVIEWS.md`
- `EXTERNAL_HERMES_UI_OPTION_REVIEWS.md`
- `EXTERNAL_MEMORY_RUNTIME_REVIEWS_OPENCONCHO_HONCHO.md`
- `EXTERNAL_RUNTIME_OPTION_REVIEWS_KANWAS_AKS_AGENTRQ_OPENCODE_SIX_HATS.md`
- `EXTERNAL_RUNTIME_REVIEW_TEMPLATE.md`
- `EXTERNAL_WATCHLIST.md`
- `GOVERNANCE_ENHANCEMENT_BACKLOG.md`
- `GOVERNANCE_METHODS.md`
- `HERMES_CAPABILITY_MAP.md`
- `HERMES_EXECUTION_MODEL.md`
- `MEMORY_STORAGE_MODEL.md`
- `PRE_REFACTOR_ARCHITECTURE_FINDINGS.md`
- `VERSIONS.md`

Arbitration outcomes will be recorded here as `Voluntarily not migrated`, `migrated under <new path>` or `condensed into <existing doc>` with a short justification.

## Update policy

This file is updated at every Phase C migration PR. Each PR appends or rewrites the row of the file it migrates and may append a row under `OS files not yet bound to a Next stub` if needed.

The file is not touched by Phase D schema PRs or by post-merge reconciliations.
