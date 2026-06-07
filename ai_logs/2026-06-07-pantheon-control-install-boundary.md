# AI Log — Pantheon Control installation boundary

Date: 2026-06-07

## Context

The user clarified that installer work will continue in a separate discussion and that the current discussion should focus only on the MCP Policy Server.

They also clarified that installation belongs inside the broader Pantheon Control / dashboard / install track, not as an isolated installer concern.

Known current local path:

```text
/volume3/docker/Pantheon-Next
```

This path is treated as a current deployment fact, not a portable default.

## Action

Created documentation-only boundary note:

```text
docs/governance/PANTHEON_CONTROL_INSTALLATION.md
```

The document separates:

```text
Pantheon Control installation work
MCP Policy Server validation / candidate-preparation work
Hermes execution
Pantheon governance status
```

## Decision classification

Accepted:

```text
Installation belongs under Pantheon Control.
Installer work should be handled separately from the MCP thread.
MCP work should continue as validation + preparation only.
```

Refused:

```text
Treating the installer as part of the MCP Policy Server.
Treating the MCP Policy Server as a runtime, scheduler, queue, approval engine or memory engine.
Hard-coding /volume3 as a universal NAS path.
Giving MCP Docker socket access or write access to the repo.
```

To verify:

```text
Final Pantheon Control repository layout.
Whether installation implementation lives under pantheon-control/ or another candidate implementation area.
Whether PR #67 absorbs or supersedes this boundary note.
```

To arbitrate:

```text
Whether future installer implementation may touch Docker files, operations/, platform/ or .env templates.
Which preflight failures suspend a module automatically.
```

## Repo state

```text
documented non-implemented
```

No installer, Docker stack, `.env`, platform component, operations procedure, dashboard, MCP server, scheduler, queue, approval engine, memory engine or external action was implemented.

## Next

Continue the present discussion on MCP Policy Server scope only:

```text
validation
scope classification
approval-level classification
Task Contract Candidate preparation
Evidence Pack Candidate skeleton preparation
Result Candidate format preparation
Memory Candidate review framing
```
