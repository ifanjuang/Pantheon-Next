# 2026-07-08 — Doctrine boundary dedup pass

Status: validation-only intervention trace.

## Context

User review flagged that repeating the line below everywhere was becoming redundant and low-value:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Decision applied

The line remains useful as a canonical architecture boundary, but not as repeated document decoration.

Repository wording should now prefer:

```text
exposed_by
executed_by
governed_by
approved_by
forbidden
```

when reviewing a concrete capability, repo, skill, connector, workflow, runtime or operational status claim.

## Files changed

- `README.md`
  - Keeps the doctrine line as canonical boundary.
  - Adds instruction that operational documents should use explicit boundary fields rather than repeating the slogan mechanically.

- `docs/governance/WHAT_RUNS.md`
  - Replaces the repeated slogan block with operational boundary fields.
  - Keeps the runtime-status honesty map unchanged.

- `CONTRIBUTING.md`
  - Removes the repeated slogan block.
  - Adds a contribution rule to use explicit boundary fields for concrete changes.

## Boundary

This change is documentation-only.

It does not modify:

```text
schemas/
tests/
pyproject.toml
operations/
platform/
Docker files
.env files
CLAUDE.md
mcp-server/
GitHub Actions / CI scripts
```

It does not change runtime status, approval behavior, memory behavior, tool installation, scheduling, queueing, provider routing or external actions.

## Status

Implemented as documentation.

Authority class: active support wording cleanup.
