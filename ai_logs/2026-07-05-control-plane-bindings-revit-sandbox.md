# AI log — Control plane, Hermes bindings and Revit sandbox exception

Date: 2026-07-05

Repository: `ifanjuang/Pantheon-Next`

## Summary

Added three candidate support doctrine files to clarify how Pantheon can be less restrictive without becoming runtime:

```text
docs/governance/PANTHEON_CONTROL_PLANE_BOUNDARY.md
docs/governance/HERMES_CAPABILITY_BINDINGS.md
docs/governance/PANTHEON_REVIT_LOCAL_SANDBOX_EXCEPTION.md
```

This log records the intervention as documentation-only.

## Why

The user asked how to free Pantheon development while preserving the Pantheon / Hermes / OpenWebUI boundary, and then asked for a Revit-specific exception.

The goal was to formalize three distinctions:

```text
Knowing status is not executing.
Authorizing a handoff is not executing.
Displaying health is not approving.
Runtime success is not evidence.
```

and to keep the central split:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Documents added

### `PANTHEON_CONTROL_PLANE_BOUNDARY.md`

Defines a bounded control-plane exception:

```text
Pantheon may govern, display and qualify operational state.
Pantheon must not execute, host, schedule, route or self-maintain operational runtime.
```

Adds status vocabulary for:

```text
install_status
health_status
update_status
activation_status
rollback_status
governance_status
capability_gap
runtime_trace_ref
```

Records non-equivalence rules:

```text
installed != approved
healthy != safe
update_available != update_authorized
runtime_success != evidence
binding_selected != dependency_adopted
trace_record != proof
status_display != approval
capability_visible != capability_enabled
sandbox_enabled != production_approved
```

### `HERMES_CAPABILITY_BINDINGS.md`

Defines a first candidate Hermes capability binding registry.

Tier 1 candidate bindings recorded:

```text
web_evidence_intake -> xberg-io/crawlberg
external_connector_gateway -> Nango
observability -> Langfuse
structural_repo_analysis -> Lum1104/Understand-Anything
document_parsing_rag_ingestion -> RAGFlow
revit_local_adapter -> Pantheon Revit Gate local plugin
```

The registry remains a governance-readable classification, not an install queue or dependency registry.

### `PANTHEON_REVIT_LOCAL_SANDBOX_EXCEPTION.md`

Defines a Revit-specific local sandbox exception:

```text
Explore freely in sandbox.
Trace everything.
Promote only what survived real use.
Regulate production later.
```

Allows exploratory read, candidate, preview and `write_light` actions in local disposable Revit sandbox copies, while keeping production, workshared, linked and contractual models governed.

Explicitly blocks:

```text
save model
sync central
purge unused
delete as first-build primitive
write to linked models
execute arbitrary generated code
load unreviewed families into production
silent worksharing mutation
external publication or transmission
professional validation by runtime success
```

## Prior context checked

Before this intervention, the following repository context had already been checked in the conversation:

```text
docs/governance/STATUS.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/DOMAIN_PACK_SPEC.md
docs/governance/WATCHLIST.md
docs/governance/SKILL_WATCHLIST.md
docs/governance/EXTERNAL_REPO_INSPIRATIONS.md
docs/governance/EXTERNAL_AGENTIC_INSPIRATIONS.md
docs/governance/PANTHEON_REVIT_GATE.md
```

Related GitHub items checked:

```text
PR #272 — Revit free exploration V0 posture
PR #274 — Revit V0 capability registry slice
PR #275 — Revit 2027 prototype plan
PR #278 — Revit plugin skeleton
Issue #48 — Request Lifecycle orchestrator outside Pantheon
Issue #146 — Langfuse as Hermes observability adapter candidate
Issue #192 — Intent Candidate log in Pantheon Control
```

## Decision classification

Accepted:

```text
Pantheon may govern and display operational state.
Pantheon Control may expose runtime status, health, update, activation and gaps.
Hermes capability bindings may be listed in a single registry.
Revit may have a local sandbox exception for exploration.
write_light can be treated differently from write_model in Revit sandbox.
Candidate data shapes may appear in docs as non-executable support doctrine.
```

Refused:

```text
Pantheon runtime
Pantheon installer
Pantheon scheduler
Pantheon queue
Pantheon MCP host
Pantheon provider router
Pantheon plugin manager
Pantheon memory engine
Pantheon approval engine
runtime code
schema/test addition
operations/platform/Docker/.env change
real Revit plugin implementation
real Hermes integration
real install/update/rollback execution
```

To verify:

```text
Whether these new governance files should be indexed in AUTHORITY_INDEX.md or future sub-indexes.
Whether the Revit sandbox exception should be folded into PANTHEON_REVIT_GATE.md later.
Whether a separate HERMES_CAPABILITY_INSTALLER_BOUNDARY.md is still needed.
Whether candidate data shapes should later become protected schemas.
Whether Notion tracking should receive one consolidated control-plane card.
```

To arbitrate:

```text
Exact promotion path from documented binding candidate to real Hermes runtime implementation.
Risk levels C0-C5 for install, activation, update and rollback.
Whether Revit production regulation should be a separate file or later section.
Whether operations runbooks belong in this repo or a runtime/operator repo.
```

## Protected paths

No protected path was touched.

```text
schemas/: no
tests/: no
operations/: no
platform/: no
Docker: no
.env: no
pyproject.toml: no
CLAUDE.md: no
runtime code: no
Hermes implementation: no
OpenWebUI implementation: no
Revit plugin implementation: no
```

## Repo state

```text
implemented: no
documented_non_implemented: yes
partial: no runtime; doctrine candidate only
to_verify: indexing and future schema promotion
obsolete: no
non_applicable: runtime implementation in this intervention
```

## Final state

```text
Pantheon does not become the engine.
Pantheon becomes the governed dashboard of the engine.
Hermes executes.
OpenWebUI exposes.
The human decides.
Validated state remains.
```
