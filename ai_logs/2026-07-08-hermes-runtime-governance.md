# Hermes runtime governance

Date: 2026-07-08

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added: `docs/governance/HERMES_RUNTIME_GOVERNANCE.md`.
- Updated: `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`.
- Updated: `docs/governance/reference_reviews/README.md`.
- Updated: `docs/governance/WHAT_RUNS.md`.
- Removed: none.

## Why

A user-supplied Hermes Agent beginner setup guide is useful as a field report, but it must not become a Pantheon install procedure.

The change distills the guide into a governed Hermes runtime Capability Slot and cockpit runtime-card grammar: installation status, health signal, update signal, activation state, provider/model/tool/gateway gates, evidence references and rollback visibility.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none.
Authority impact: candidate support doctrine indexed; no promotion to canonical doctrine.
Schema/test/CI impact: none.
External action: none.
Memory behavior: none.

## Local distinctions

```text
external_reference != adopted_dependency
installed != approved
healthy != safe
update_available != update_authorized
runtime_success != evidence
gateway_running != gateway_exposed_safely
trace != doctrine
```
