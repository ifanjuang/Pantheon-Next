# Pantheon Control — single boundary document

Status: candidate support doctrine — to verify. Consolidates the Pantheon Control family into one slim boundary note. Candidate until reviewed.

This document is the single boundary reference for the verification surface that `CLAUDE.md` names `dashboard/`. It absorbs and supersedes the larger Pantheon Control drafts proposed in PR #67 and PR #72, which remain readable in their closed PRs as background material.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## What Pantheon Control is

A thin, light verification surface, hosted as the bounded `dashboard/` module of this monorepo (see `CLAUDE.md`, `MONOREPO_INTEGRATION_PROPOSAL.md`):

- it verifies installs from their logs and liveness: is it installed, does it answer, are the checks green — including on a NAS;
- it shows state and gate decisions as data;
- it lets the user view evidence logs and prepare proposed Registre Probatoire edits.

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
installed != connected != authorized != validated
```

A component may be installed but not connected, connected but not authorized, authorized for one scope but not another, technically valid but not yet validated for professional use.

## NAS / install posture

- No hard-coded volume. Candidate Docker roots are detected (for example `/volume*/docker`); when several exist, the human chooses.
- The current known deployment path (`/volume3/docker/Pantheon-Next`) is a local fact, not a portable default.
- Installation preparation stays readable, explicit, local-first and reversible; planned changes are shown and confirmed by the human before they are applied.
- Installation work is separate from the MCP thread: `mcp-server/` may later be installed and displayed by this surface, but it stays read-only / validation / candidate-preparation per `CLAUDE.md`.
- A read-only repository mount (for example `…/Pantheon-Next:/repo:ro`) is the expected posture; the surface receives no Docker socket access, no write access to the repository or to professional dossiers, no external-action credentials, and no approval or memory authority.

## Forbidden behavior

The surface must not silently modify access or exposure, install or update skills globally, promote a capability from available to authorized, turn a preflight pass into professional validation, write Registre Probatoire entries, approve outputs, trigger external actions, merge code, or schedule hidden jobs.

## Relationship to other doctrine

| Concern | Where it lives |
|---|---|
| Module boundary (`dashboard/`, `mcp-server/`) | `CLAUDE.md`, `MONOREPO_INTEGRATION_PROPOSAL.md` |
| Invocation and connectivity preflight | `MODULE_INVOCATION_PREFLIGHT.md` |
| MCP development phases | `PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` |
| Capability passports and the chokepoint | `UNIFORM_CAPABILITY_GOVERNANCE.md` |
| Registre Probatoire | `MEMORY.md`, `EVIDENCE_MEMORY_CANONICALIZATION.md` |

Feature-level material from the former drafts (document/media stack, observability and voice, mobile-first UX, implementation phasing) is intentionally not carried into this boundary note. Any of it may return later as its own governed candidate, one scoped proposal at a time, if the thin boundary above is preserved.

## Boundary phrase

```text
Pantheon Control may prepare and verify the room.
Hermes performs the work.
The mcp-server checks the frame.
Pantheon governs status.
The human decides.
```
