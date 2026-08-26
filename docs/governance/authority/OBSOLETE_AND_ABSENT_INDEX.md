# Pantheon Next — Obsolete and Absent Index

Status: candidate refusal/absence map — populated; awaiting review.

This sub-index records obsolete, superseded, refused and voluntarily absent material. An entry here is an active decision, not a forgotten gap.

It does not override the authority vocabulary, promotion rule, placement test, tool naming rule, terminology boundary rule or sensitive-path guardrail of `docs/governance/AUTHORITY_INDEX.md`. The master index defines how to read authority; this file only lists where refused or superseded material sits. Listing an item here does not reinstate it; removing an item from here does not promote it.

## Obsolete documents and artifacts

Removed material remains available through Git history. Retained obsolete documents carry their own status and must not be cited as active doctrine.

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| Former local Pantheon Control dashboard assets under `docs/assets/pantheon-control/` (removed; Git history) | obsolete static prototype | superseded by co-located candidate cockpit | The former multipage dashboard, navigation, project fixtures, interactive controls and duplicate renderers are removed. `README.md` and `index.html` remain as an orientation point to `implementation/mvp_vertical/cockpit/`. A synthetic Hermes renderer preview and six read-only classifier mirrors remain only as protected validation support and must not be read as the retired Pantheon dashboard. |
| Former architecture MVP static page and fictional product scenario (removed after implementation migration) | obsolete local demonstration | transformed into implementation demo fixture | The product-facing synthetic corpus moved in transformed form to the implementation history that is now co-located under `implementation/`. Verbose manual-run and duplicate HTML outputs remain only in Git history. This migration does not adopt or activate the implementation. |
| Former capability/resource installation-composition model (removed; Git history) | obsolete | superseded | Superseded by `COMMON_INSTALLATION_BASELINE.md` and the module-only `INSTALL_MODULE_CATALOG.md`. |
| Former installation-composition manifests under `catalog/` (removed; Git history) | obsolete declarative artifacts | superseded | Historical examples must not determine, render or install a Pantheon environment. Only those former manifests were removed: the `catalog/` directory itself is active and now hosts the candidate capability/resource and decision-projection records (see `WHAT_RUNS.md` and `MODULES.md`). |
| Former installation-composition schema under `catalog/schemas/` (removed; Git history) | obsolete schema artifact | superseded | It is not the common installation contract. The current `catalog/schemas/` hold the candidate capability, resource, handoff-decision, provisioner-handoff and current-decision-projection contracts, not the removed composition schema. |
| Former `CARD_STACK_HARDENING_NOTE.md` (removed; Git history) | obsolete | superseded | Superseded by the reconciled `CARD_STACK_MODEL.md`. Its accepted rules are owned by the current model. |
| Former `STUB_RESOLUTION_PLAN.md` (removed; Git history) | obsolete validation plan | completed | The one-shot dispositions were executed. Current authority and obsolete-placement indexes now carry the resulting state. |
| `PADDLEOCR_DASHBOARD_INSTALL_CANDIDATE.md` (removed; Git history) | obsolete candidate support note | superseded by single-slot document structural-analysis convergence | The removed note described dashboard-driven installation, multiple parser modules and capability routing. Current convergence keeps one replaceable `document_structural_analysis` responsibility and forbids a parallel parser/provider router merely to expose alternatives; parser comparison remains under #662 and the existing document-analysis owners. |
| `MCP_POLICY_SERVER_CANDIDATE.md` (removed; Git history) | obsolete candidate support doctrine | superseded by implemented bounded policy service | The old document described a future/non-implemented MCP Policy Server. The current boundary is implemented under `mcp-server/`; `mcp-server/docs/HTTP_API_CONTRACT.md` defines the transport-neutral PDP projection and the existing MCP consultation surface. |
| `PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` (removed; Git history) | obsolete development roadmap | completed/superseded | The future-development sequence is no longer an active architecture owner. Current implementation, tests and operator contracts under `mcp-server/` own the implemented policy surface; Git history and `ai_logs` preserve development provenance. |
| `PANTHEON_MVP_VERTICAL_BINDING.md` (removed; Git history) | obsolete external-binding baseline | superseded by monorepo placement and co-located implementation | The document classified `ifanjuang/pantheon-mvp` as a current external executable candidate, pinned July 2026 commits/runs and described a future Hermes-side execution owner. The repository placement decision now makes `implementation/` the active Pantheon implementation responsibility; `NEXT_MVP_REPOSITORY_PLACEMENT.md`, current Document/Knowledge contracts and implementation tests carry the surviving invariants. Historical external PRs, commits and CI remain provenance only. |
| `PANTHEON_MVP_COCKPIT_RECONCILIATION.md` (removed; Git history) | obsolete validation-only cockpit reconciliation | superseded by current lifecycle doctrine and co-located implementation | The document pinned the July 2026 external `pantheon-mvp` cockpit and recorded implementation and activation posture. Its surviving rules are now owned by `DOCUMENT_LIFECYCLE_GOVERNANCE.md`, `NEXT_MVP_REPOSITORY_PLACEMENT.md`, current cockpit/document contracts and `implementation/`. Historical commits, CI observations and demo provenance remain in Git and dated `ai_logs`; the removed file is no longer an active adapter owner. |
| `HERMES_CODE_HOSTING_BOUNDARY.md` (removed; Git history) | obsolete hosting decision | superseded by current monorepo placement and Hermes integration boundary | The July 2026 Option A decision placed executable candidate code in a sibling repository. Current placement is owned by `NEXT_MVP_REPOSITORY_PLACEMENT.md`: bounded Pantheon implementation and adapters live under `implementation/`, while Hermes remains the external execution runtime under `HERMES_INTEGRATION.md`. The historical arbitration remains in Git and dated `ai_logs`. |
| `MVP_VERTICAL_IMPLEMENTATION_PLAN.md` (removed; Git history) | obsolete implementation plan | hosting assumption and delivery sequence superseded | The plan sequenced a future external MVP vertical before the co-located implementation existed. The surviving governed-loop contract remains in `MVP_GOVERNED_TASK_LOOP.md` and `schemas/mvp_governed_loop_objects.schema.yaml`; current executable candidate work lives under `implementation/`. Historical planning and arbitration context remain in Git and `ai_logs`. |
| `MONOREPO_INTEGRATION_PROPOSAL.md` (removed; Git history) | obsolete integration proposal | realized/superseded by current repository rules and placement | The proposal justified admitting bounded MCP/dashboard surfaces behind a one-way repository boundary. The current module boundary is now carried by root `CLAUDE.md`, `NEXT_MVP_REPOSITORY_PLACEMENT.md`, `PANTHEON_CONTROL_BOUNDARY.md` and the implemented protected surfaces. The original proposal remains historical provenance in Git and `ai_logs`. |
| `REGISTER_LINK_CASCADE_SCHEMA_PROPOSAL.md` (removed; Git history) | obsolete validation-only proposal | applied/superseded by canonical dependency doctrine and validation schemas | The proposal was applied after review. `EVIDENCE_MEMORY_CANONICALIZATION.md` owns dependency, impact-review, conflict and critical-impact semantics; `schemas/register_link.schema.yaml` and `schemas/impact_review.schema.yaml` carry the machine-checkable contracts. Historical proposal context remains in Git and dated `ai_logs`. No automatic cascade resolution, memory promotion or human-decision substitution is introduced. |
| `REGISTRE_PROBATOIRE_SCHEMA_PROPOSAL.md` (removed; Git history) | obsolete validation-only proposal | E6 applied; superseded by current Register Candidate schema and doctrine | The approved E6 rename was completed on 2026-06-12: the old `memory_candidate` schema/example were removed, `schemas/register_candidate.schema.yaml` and its example/tests became the current contract, and Registre Probatoire doctrine was aligned. `ai_logs/2026-06-12-registre-e6-applied.md` preserves the application proof. The deprecated `confidence` alias remains allowed only when explicitly marked legacy/deprecated; no memory promotion or runtime is introduced. |
| `CHANGELOG_ADDENDUM_EVIDENCE_TOPOLOGY_SCHEMA_D2.md` (removed; Git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EPISTEMIC_CONTROL.md` (removed; Git history) | obsolete | superseded | Resolved during the completed stub cleanup after review of the historical source. |
| `EPISTEMIC_CONTROL_PROPAGATION.md` (removed; Git history) | obsolete | superseded | Resolved with `EPISTEMIC_CONTROL.md` during the completed stub cleanup. |
| `EVIDENCE_TOPOLOGY_BRIDGES.md` (removed; Git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EVIDENCE_TOPOLOGY_CHECKLIST.md` (removed; Git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EVIDENCE_TOPOLOGY_GATE.md` (removed; Git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EVIDENCE_TOPOLOGY_RECONCILIATION.md` (removed; Git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EVIDENCE_TOPOLOGY_ROADMAP.md` (removed; Git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md` (removed; Git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EXTERNAL_RUNTIME_OPTIONS.md` (removed; Git history) | obsolete | superseded | Resolved during the completed stub cleanup. |
| `MEMORY_EVENT_SCHEMA.md` (removed; Git history) | obsolete | superseded | Resolved during the completed stub cleanup. |
| Former `MIGRATION_PLAYBOOK.md` (removed; Git history) | obsolete | completed | The historical migration is closed. Current work starts from `STATUS.md`, `WHAT_RUNS.md`, `AUTHORITY_INDEX.md`, `MODULES.md` and `CONTRIBUTING.md`; no active workflow depends on the former playbook. |
| `MODEL_ROUTING_POLICY.md` (removed; Git history) | obsolete | superseded | Resolved during the completed stub cleanup. |
| `OPENWEBUI_DOMAIN_MAPPING.md` (removed; Git history) | obsolete | superseded | Merged into `OPENWEBUI_INTEGRATION.md` during the completed stub cleanup. |
| `OPENWEBUI_PLUGIN_POLICY.md` (removed; Git history) | obsolete | superseded | Merged into `OPENWEBUI_INTEGRATION.md` during the completed stub cleanup. |
| `ROLE_SIGNAL_PROFILES.md` (removed; Git history) | obsolete | superseded | Merged into `ROLE_SIGNALS.md` during the completed stub cleanup. |
| `ROUTING_FOUNDATION.md` (removed; Git history) | obsolete | superseded | Resolved during the completed stub cleanup. |
| `WORKFLOW_ADAPTATION.md` (removed; Git history) | obsolete | superseded | Merged into `WORKFLOW_LIFECYCLE.md` during the completed stub cleanup. |

## Voluntarily absent

A voluntarily absent item is excluded by doctrine, per the master index vocabulary. Its absence is a decision.

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `dashboard/` | voluntarily absent | non implemented (by doctrine) | A real dashboard module is voluntarily absent until actually built (`CLAUDE.md`, repository structure). The current public path under `docs/assets/pantheon-control/` is an orientation pointer with bounded validation-support artifacts, not a local exposure implementation. Bounded read-only verification, where implemented, lives in protected implementation artifacts such as `mcp-server/`, not in a dashboard module. A future dashboard must display or request qualification only under the governed boundary and must not execute, approve, send, schedule, route providers, install, update or promote memory. |

## Historical bootstrap stubs

Row migrated from the Current authority map of `docs/governance/AUTHORITY_INDEX.md`; the Bootstrap stub rule remains defined there.

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| Historical bootstrap stubs formerly listed in roadmap/status materials, including `MODEL_ROUTING_POLICY.md`, `MEMORY_EVENT_SCHEMA.md`, `EPISTEMIC_CONTROL.md` and equivalent declared stubs | candidate / stub reference | documented non-implemented | Not canonical, not implemented and not active support doctrine unless a future row in the master index promotes a concrete file. Roadmap mentions are historical signals, not authority. The named files were resolved and removed during the completed stub cleanup; their history remains in Git. |

## Boundary

This file records decisions already made elsewhere. It creates no runtime, promotes nothing and reinstates nothing.
