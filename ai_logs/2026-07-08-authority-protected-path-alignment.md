# 2026-07-08 — Authority protected-path alignment

## Status

Validation-only trace.

This log records an authority-index alignment. It does not create doctrine, runtime behavior, approval, memory promotion, provider routing, scheduling, installation, update execution or external action.

## Scope

Files changed:

```text
docs/governance/AUTHORITY_INDEX.md
docs/governance/authority/IMPLEMENTATION_ARTIFACTS_AUTHORITY_INDEX.md
```

## What changed

- `docs/governance/authority/IMPLEMENTATION_ARTIFACTS_AUTHORITY_INDEX.md` now classifies `tests/` as `implemented read-only / partial / protected path`, matching `WHAT_RUNS.md` and `MODULES.md`.
- `schemas/` is clarified as validation contracts, partial / protected review required.
- `CLAUDE.md` and GitHub Actions / CI scripts are explicitly listed in the implementation-artifacts sub-index as protected paths.
- `docs/governance/AUTHORITY_INDEX.md` sensitive-path guardrail now includes `CLAUDE.md`, `mcp-server/` and GitHub Actions / CI scripts, matching the broader protected-path discipline already stated elsewhere.

## Why

After the status-runtime read-path reconciliation, the authority spine still had two residual mismatches:

```text
IMPLEMENTATION_ARTIFACTS_AUTHORITY_INDEX.md listed tests/ only as protected path.
AUTHORITY_INDEX.md had a shorter sensitive-path list than STATUS.md / WHAT_RUNS.md / CONTRIBUTING.md.
```

The change makes the authority layer consistent with the current status spine without relaxing any protected path.

## Boundary kept

This intervention did not modify protected implementation paths themselves.

It did not add or authorize:

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

## Risks and limitations

- No CI or full link checker was run in this intervention.
- The implementation-artifacts sub-index remains a candidate support map awaiting review.
- Listing a protected path is status visibility only. It does not authorize modification of that path.

## Result

The authority layer now matches the current protected-path discipline:

```text
schemas/
tests/
pyproject.toml
operations/
platform/
CLAUDE.md
mcp-server/
GitHub Actions / CI scripts
Docker files
.env files
```
