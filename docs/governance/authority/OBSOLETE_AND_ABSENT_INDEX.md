# Pantheon Next — Obsolete and Absent Index

Status: candidate refusal/absence map — populated with the first migration group; awaiting review.

This sub-index records obsolete, superseded, refused and voluntarily absent material, per `docs/governance/AUTHORITY_INDEX_DECOMPOSITION_PLAN.md`. An entry here is an active decision, not a forgotten gap.

It does not override the authority vocabulary, promotion rule, placement test, tool naming rule, terminology boundary rule or sensitive-path guardrail of `docs/governance/AUTHORITY_INDEX.md`. The master index defines how to read authority; this file only lists where refused or superseded material sits. Listing an item here does not reinstate it; removing an item from here does not promote it.

## Obsolete documents

Each file below carries its own `Status: obsolete` header, which remains the per-file source of truth. The file stays in the repository as historical record; its content must not be cited as active doctrine.

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `docs/governance/CHANGELOG_ADDENDUM_EVIDENCE_TOPOLOGY_SCHEMA_D2.md` | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `docs/governance/EPISTEMIC_CONTROL.md` | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md` after reading the Pantheon-OS source. |
| `docs/governance/EPISTEMIC_CONTROL_PROPAGATION.md` | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md` with `EPISTEMIC_CONTROL.md`. |
| `docs/governance/EVIDENCE_TOPOLOGY_BRIDGES.md` | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `docs/governance/EVIDENCE_TOPOLOGY_CHECKLIST.md` | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `docs/governance/EVIDENCE_TOPOLOGY_GATE.md` | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `docs/governance/EVIDENCE_TOPOLOGY_RECONCILIATION.md` | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `docs/governance/EVIDENCE_TOPOLOGY_ROADMAP.md` | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `docs/governance/EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md` | obsolete | superseded | Superseded by the consolidated evidence topology corpus. |
| `docs/governance/EXTERNAL_RUNTIME_OPTIONS.md` | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md`. |
| `docs/governance/MEMORY_EVENT_SCHEMA.md` | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md`. |
| `docs/governance/MODEL_ROUTING_POLICY.md` | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md`. |
| `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md` | obsolete | superseded | Merged into `OPENWEBUI_INTEGRATION.md`; resolved per `STUB_RESOLUTION_PLAN.md`. |
| `docs/governance/OPENWEBUI_PLUGIN_POLICY.md` | obsolete | superseded | Merged into `OPENWEBUI_INTEGRATION.md`; resolved per `STUB_RESOLUTION_PLAN.md`. |
| `docs/governance/ROLE_SIGNAL_PROFILES.md` | obsolete | superseded | Merged into `ROLE_SIGNALS.md`; resolved per `STUB_RESOLUTION_PLAN.md`. |
| `docs/governance/ROUTING_FOUNDATION.md` | obsolete | superseded | Resolved per `STUB_RESOLUTION_PLAN.md`. |
| `docs/governance/WORKFLOW_ADAPTATION.md` | obsolete | superseded | Merged into `WORKFLOW_LIFECYCLE.md`; resolved per `STUB_RESOLUTION_PLAN.md`. |

## Voluntarily absent

A voluntarily absent item is excluded by doctrine, per the master index vocabulary. Its absence is a decision.

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `dashboard/` | voluntarily absent | non implemented (by doctrine) | A real dashboard module is voluntarily absent until actually built (`CLAUDE.md`, repository structure). The exposure surface exists only as the static prototype under `docs/assets/pantheon-control/`. When it exists it will display, not verify. |

## Historical bootstrap stubs

Row migrated from the Current authority map of `docs/governance/AUTHORITY_INDEX.md`; the Bootstrap stub rule remains defined there.

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| Historical bootstrap stubs formerly listed in roadmap/status materials, including `MODEL_ROUTING_POLICY.md`, `MEMORY_EVENT_SCHEMA.md`, `EPISTEMIC_CONTROL.md` and equivalent declared stubs | candidate / stub reference | documented non-implemented | Not canonical, not implemented and not active support doctrine unless a future row in the master index promotes a concrete file. Roadmap mentions are historical signals, not authority. The three named files have since been resolved to `Status: obsolete` (see above). |

## Boundary

This file records decisions already made elsewhere (per-file Status headers, `STUB_RESOLUTION_PLAN.md`, `REJECTED_PATTERNS.md`, `CLAUDE.md`). It makes no new decision, promotes nothing, reinstates nothing and adds no runtime.
