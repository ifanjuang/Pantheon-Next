# 2026-07-08 — Specialized boundary dedup pass A

Status: validation-only intervention trace.

## Context

Repository review identified repeated architecture-boundary slogans across specialized doctrine documents.

The canonical boundary remains in the root/status/index layer. Specialized documents should apply the boundary locally rather than repeat the slogan mechanically.

## Change applied

This pass removes the repeated slogan block from `docs/governance/EVIDENCE_PACK.md` and replaces it with a direct reference to the canonical boundary.

The local doctrine remains unchanged:

- Evidence Pack remains governed proof material.
- Evidence Pack remains not runtime log, chain-of-thought, runtime state or execution replay.
- Pantheon still receives and governs evidence without owning or replaying execution.

## Deferred work

This is intentionally not a full repository rewrite.

Larger files and more sensitive consolidation candidates remain for later passes:

```text
docs/governance/MODULES.md
docs/governance/AUTHORITY_INDEX.md
docs/governance/TERMINOLOGY_BOUNDARIES.md
docs/governance/COMPETENCE_MODEL.md
docs/governance/CARD_STACK_MODEL.md
docs/governance/OPENWEBUI_INTEGRATION.md
docs/governance/HERMES_INTEGRATION.md
```

`OPENWEBUI_INTEGRATION.md` and `HERMES_INTEGRATION.md` should be handled separately because the connector returned partial content for at least one long integration file during this pass. Avoid full-file replacement unless the complete file is available.

`HERMES_INTEGRATION.md` also contains absorbed material and bridge sections whose compression may affect readability.

## Boundary

Documentation-only change.

No protected paths touched:

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

No runtime status change. No approval, memory, scheduling, queueing, provider-routing, install, update, tool authorization or external-action behavior introduced.

## Status

Implemented as documentation.

Authority class: active support wording cleanup / no doctrine change.
