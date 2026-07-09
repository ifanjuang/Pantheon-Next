# Pantheon Control — single boundary document

Status: candidate support doctrine — to verify. Consolidates the Pantheon Control family into one slim boundary note. Candidate until reviewed.

This document is the boundary reference for the Pantheon Control concept and future dashboard-facing verification surface. It does not mean a real `dashboard/` module currently exists.

It absorbs and supersedes the larger Pantheon Control drafts proposed in PR #67 and PR #72, which remain readable in their closed PRs as background material.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Current repository placement

Current repository state distinguishes three things:

```text
dashboard/                     = voluntarily absent real dashboard module
docs/assets/pantheon-control/  = static prototype / partial read-only mirror
mcp-server/                    = protected read-only verification / policy artifact, where implemented
```

Therefore, this document governs the Pantheon Control boundary and future dashboard-facing behavior, but it does not promote `dashboard/` from voluntarily absent to implemented.

Bounded read-only verification may be displayed by a future dashboard, but the protected verification artifact remains outside the dashboard module unless a later reviewed implementation says otherwise.

## What Pantheon Control is

Pantheon Control is a thin, light governed control surface concept:

- it may display install, adoption, configuration, liveness and health observations as qualified status data;
- it may show gate decisions, blockers, risks and next required human decisions;
- it may let the user view evidence logs and prepare proposed Registre Probatoire edits.

A proposed evidence edit is a governed candidate routed through the consequential chokepoint and the User Decision Gate — never a direct write.

## What Pantheon Control is not

It runs no agent and decides nothing; the gate decides. It must not become:

```text
a heavy dashboard
an automatic skill installer
an orchestrator
an approval engine
a memory promotion engine
a scheduler or queue
a provider router
a connector gateway
a hidden workflow runtime
```

## Required status distinctions

The surface must never collapse these states:

```text
listed != installed != connected != authorized != validated
observed != adopted
healthy != safe
runtime_success != evidence
```

A component may be listed but not installed, installed but not connected, connected but not authorized, authorized for one scope but not another, technically valid but not yet validated for professional use.

## NAS / install posture

- No hard-coded volume. Candidate Docker roots are detected (for example `/volume*/docker`); when several exist, the human chooses.
- The current known deployment path (`/volume3/docker/Pantheon-Next`) is a local fact, not a portable default.
- Installation preparation stays readable, explicit, local-first and reversible; planned changes are shown and confirmed by the human before they are applied.
- Installation work is separate from the MCP thread: `mcp-server/` may later be installed and displayed by a Pantheon Control surface, but it stays read-only / validation / candidate-preparation per `CLAUDE.md`.
- A read-only repository mount (for example `…/Pantheon-Next:/repo:ro`) is the expected posture for any local verification surface; the surface receives no Docker socket access, no write access to the repository or to professional dossiers, no external-action credentials, and no approval or memory authority.

## Forbidden behavior

The surface must not silently modify access or exposure, install or update skills globally, promote a capability from available to authorized, turn a preflight pass into professional validation, write Registre Probatoire entries, approve outputs, trigger external actions, merge code, or schedule hidden jobs.

## Relationship to other doctrine

| Concern | Where it lives |
|---|---|
| Absence of real `dashboard/` module | `docs/governance/authority/OBSOLETE_AND_ABSENT_INDEX.md` |
| Static Pantheon Control prototype | `docs/assets/pantheon-control/` |
| Protected read-only verification / policy artifact | `mcp-server/`, `PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` |
| Module boundary (`dashboard/`, `mcp-server/`) | `CLAUDE.md`, `MONOREPO_INTEGRATION_PROPOSAL.md` |
| Invocation and connectivity preflight | `MODULE_INVOCATION_PREFLIGHT.md` |
| Capability passports and the chokepoint | `UNIFORM_CAPABILITY_GOVERNANCE.md` |
| Registre Probatoire | `MEMORY.md`, `EVIDENCE_MEMORY_CANONICALIZATION.md` |

Feature-level material from the former drafts (document/media stack, observability and voice, mobile-first UX, implementation phasing) is intentionally not carried into this boundary note. Any of it may return later as its own governed candidate, one scoped proposal at a time, if the thin boundary above is preserved.

## Boundary phrase

```text
Pantheon Control may display and prepare the room.
Protected verification artifacts check the frame.
Hermes performs the work.
Pantheon governs status.
The human decides.
```
