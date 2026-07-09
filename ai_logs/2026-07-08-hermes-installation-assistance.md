# Hermes installation assistance

Date: 2026-07-08

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added: `docs/governance/HERMES_INSTALLATION_ASSISTANCE.md`.
- Updated: `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`.
- Updated: `docs/governance/WHAT_RUNS.md`.
- Removed: none.

## Why

After adding Hermes runtime governance, the missing adjacent piece was installation help and checks.

The change defines how Pantheon may assist a human installation without becoming the installer: preflight readiness, command candidates, redacted output review, post-install classification, activation checks, stop conditions, rollback readiness and evidence expectations.

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
install_plan != install_authorization
command_candidate != command_executed
command_executed != approved_installation
health_probe != safe_runtime
setup_complete != activation_authorized
api_key_present != secret_governed
rollback_path_known != rollback_decided
trace != doctrine
```
