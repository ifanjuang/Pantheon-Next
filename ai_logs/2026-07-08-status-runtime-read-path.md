# 2026-07-08 — Status runtime read-path reconciliation

## Status

Validation-only trace.

This log records a documentation/status-spine reconciliation. It does not create doctrine, runtime behavior, approval, memory promotion, provider routing, scheduling, installation, update execution or external action.

## Scope

Files changed:

```text
docs/governance/WHAT_RUNS.md
docs/governance/MODULES.md
docs/governance/STATUS.md
```

## What changed

- `WHAT_RUNS.md` was updated to use the current repository read path before significant branch merges or closures.
- `WHAT_RUNS.md` date was updated to `2026-07-08`.
- `MODULES.md` now classifies `WHAT_RUNS.md` as part of the Repository status module.
- `MODULES.md` now classifies `tests/` as `implemented_read_only_partial` rather than future-only tooling, matching the runtime-status map and changelog references to existing validation tests.
- `STATUS.md` date was updated to `2026-07-08`.
- `STATUS.md` now distinguishes the governance read path, root repository entry, contribution guardrail, authority index, module map and runtime-status honesty map.
- `STATUS.md` records the README entry refactor and this status-runtime read-path reconciliation as historical reconciliations.

## Why

The previous spine had three tensions:

```text
STATUS.md recognized WHAT_RUNS.md as the runtime-status honesty map.
WHAT_RUNS.md did not yet point to the current repository read path before merge work.
MODULES.md still described tests/ as future tooling even though tests exist where present.
```

The change makes the state spine read consistently:

```text
docs/governance/README.md -> governance read path
README.md                 -> repository entry
CONTRIBUTING.md           -> contribution guardrail
STATUS.md                 -> posture and live exceptions
WHAT_RUNS.md              -> runtime-status honesty
AUTHORITY_INDEX.md        -> authority classification
MODULES.md                -> governance-area map
```

## Boundary kept

This reconciliation did not add or authorize:

```text
runtime
agent loop
scheduler
queue
provider router
MCP host gateway
plugin manager
installer
updater
automatic approval
automatic memory promotion
external sender
```

`tests/` remains validation-only. Its existence does not promote doctrine, approve changes or imply runtime behavior.

## Risks and limitations

- No CI or full link checker was run in this intervention.
- `WHAT_RUNS.md` remains `active support / to verify`; it is a support map, not a canonical implementation registry.
- Protected paths remain protected. This documentation update does not authorize future changes under `tests/`, `schemas/`, `mcp-server/`, GitHub Actions or other protected areas.

## Result

The repository status spine is more coherent:

```text
STATUS records posture.
WHAT_RUNS states operational reality.
MODULES maps governance areas.
AUTHORITY_INDEX classifies authority.
CONTRIBUTING gates changes.
The human decides.
```
