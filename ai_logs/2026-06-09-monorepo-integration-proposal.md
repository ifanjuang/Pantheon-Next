# AI log — Monorepo integration proposal

Date: 2026-06-09.

## Intent

The maintainer decided to host two bounded surfaces inside the Pantheon Next repository:

- an MCP server, as the standard connection surface to Hermes Agent and OpenWebUI;
- a light dashboard, as an install and liveness verification surface, including NAS visibility.

This changes the founding repository boundary, so the documentation amendment is proposed before any module code.

## Decision recorded

```text
Structure: monorepo with a hard internal boundary.
Doctrine: amend CLAUDE.md first.
```

## Boundary

The governance core stays pure and depends on neither module.

`mcp-server/` and `dashboard/` depend on the governance core.

No module may bypass the consequential chokepoint.

## Work performed

- `CLAUDE.md` amended to describe the hard internal boundary.
- `docs/governance/MONOREPO_INTEGRATION_PROPOSAL.md` added as validation-only.
- `docs/governance/AUTHORITY_INDEX.md` indexes the proposal.

## Repo state

Documented non-implemented.

No `mcp-server/` or `dashboard/` code was added.

No schema, test, operations, platform, Docker, pyproject or environment file was changed.
