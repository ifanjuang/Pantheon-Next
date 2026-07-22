# Pantheon Next — Obsolete and Absent Index

Status: candidate refusal/absence map — populated; awaiting review.

This sub-index records obsolete, superseded, refused and voluntarily absent material, per `docs/governance/AUTHORITY_INDEX_DECOMPOSITION_PLAN.md`. An entry here is an active decision, not a forgotten gap.

It does not override the authority vocabulary, promotion rule, placement test, tool naming rule, terminology boundary rule or sensitive-path guardrail of `docs/governance/AUTHORITY_INDEX.md`. The master index defines how to read authority; this file only lists where refused or superseded material sits. Listing an item here does not reinstate it; removing an item from here does not promote it.

## Obsolete documents and artifacts

Removed material remains available through Git history. Retained obsolete documents carry their own status and must not be cited as active doctrine.

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `docs/governance/CAPABILITY_RESOURCE_PRESET_MODEL.md` (removed; git history) | obsolete | superseded | Superseded by `COMMON_INSTALLATION_BASELINE.md` and the module-only `INSTALL_MODULE_CATALOG.md`. |
| `catalog/presets/` (removed; git history) | obsolete declarative artifacts | superseded | Historical installation-composition examples. They must not determine, render or install a Pantheon environment. |
| `catalog/schemas/preset.schema.json` (removed; git history) | obsolete schema artifact | superseded | Historical schema for the retired installation-composition model. It is not the common installation contract. |
| `docs/governance/CARD_STACK_HARDENING_NOTE.md` | obsolete | superseded | Superseded by the reconciled `CARD_STACK_MODEL.md`. Retained only as historical record; not active doctrine. |
| `CHANGELOG_ADDENDUM_EVIDENCE_TOPOLOGY_SCHEMA_D2.md` (removed; git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EPISTEMIC_CONTROL.md` (removed; git history) | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md` after reviewing the historical source. |
| `EPISTEMIC_CONTROL_PROPAGATION.md` (removed; git history) | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md` with `EPISTEMIC_CONTROL.md`. |
| `EVIDENCE_TOPOLOGY_BRIDGES.md` (removed; git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EVIDENCE_TOPOLOGY_CHECKLIST.md` (removed; git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EVIDENCE_TOPOLOGY_GATE.md` (removed; git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EVIDENCE_TOPOLOGY_RECONCILIATION.md` (removed; git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EVIDENCE_TOPOLOGY_ROADMAP.md` (removed; git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md` (removed; git history) | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `EXTERNAL_RUNTIME_OPTIONS.md` (removed; git history) | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md`. |
| `MEMORY_EVENT_SCHEMA.md` (removed; git history) | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md`. |
| `docs/governance/MIGRATION_PLAYBOOK.md` | obsolete | completed | Historical migration procedure retained at its expected path for link and repository-check compatibility. It must not restart migration or create an external source dependency. |
| `MODEL_ROUTING_POLICY.md` (removed; git history) | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md`. |
| `OPENWEBUI_DOMAIN_MAPPING.md` (removed; git history) | obsolete | superseded | Merged into `OPENWEBUI_INTEGRATION.md`; resolved per `STUB_RESOLUTION_PLAN.md`. |
| `OPENWEBUI_PLUGIN_POLICY.md` (removed; git history) | obsolete | superseded | Merged into `OPENWEBUI_INTEGRATION.md`; resolved per `STUB_RESOLUTION_PLAN.md`. |
| `ROLE_SIGNAL_PROFILES.md` (removed; git history) | obsolete | superseded | Merged into `ROLE_SIGNALS.md`; resolved per `STUB_RESOLUTION_PLAN.md`. |
| `ROUTING_FOUNDATION.md` (removed; git history) | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md`. |
| `WORKFLOW_ADAPTATION.md` (removed; git history) | obsolete | superseded | Merged into `WORKFLOW_LIFECYCLE.md`; resolved per `STUB_RESOLUTION_PLAN.md`. |

## Voluntarily absent

A voluntarily absent item is excluded by doctrine, per the master index vocabulary. Its absence is a decision.

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `dashboard/` | voluntarily absent | non implemented (by doctrine) | A real dashboard module is voluntarily absent until actually built (`CLAUDE.md`, repository structure). The current exposure surface is the static prototype under `docs/assets/pantheon-control/`; bounded read-only verification, where implemented, lives in protected implementation artifacts such as `mcp-server/`, not in a dashboard module. A future dashboard must display or request qualification only under the governed boundary and must not execute, approve, send, schedule, route providers, install, update or promote memory. |

## Historical bootstrap stubs

Row migrated from the Current authority map of `docs/governance/AUTHORITY_INDEX.md`; the Bootstrap stub rule remains defined there.

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| Historical bootstrap stubs formerly listed in roadmap/status materials, including `MODEL_ROUTING_POLICY.md`, `MEMORY_EVENT_SCHEMA.md`, `EPISTEMIC_CONTROL.md` and equivalent declared stubs | candidate / stub reference | documented non-implemented | Not canonical, not implemented and not active support doctrine unless a future row in the master index promotes a concrete file. Roadmap mentions are historical signals, not authority. The three named files have since been resolved to `Status: obsolete` (see above). |

## Boundary

This file records decisions already made elsewhere. It creates no runtime, promotes nothing and reinstates nothing.
