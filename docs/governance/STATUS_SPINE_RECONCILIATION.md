# Status Spine Reconciliation

Status: validation-only / status-spine reconciliation — partially resolved.

Date: 2026-06-30

This document records the current reconciliation position between:

- `STATUS.md`;
- `AUTHORITY_INDEX.md`;
- `MODULES.md`;
- `WHAT_RUNS.md`;
- `REPOSITORY_CONSOLIDATION_LANDING_PLAN.md`.

It does not create doctrine by itself, implement runtime behavior, approve a protected-path change, create a dashboard, approve a PR, execute Hermes, send anything externally or promote memory.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Why this note exists

`WHAT_RUNS.md` states the repository's runtime-status posture.

Before PR #239, the safe position was to keep `mcp-server/` in:

```text
partial / to verify / protected review required
```

because some existing `MODULES.md` wording described the MCP policy server as an active read-only policy / validation surface while the status spine still treated it as unresolved.

PR #239 has now been:

```text
reviewed as protected-path work;
target-tested locally on the changed update verifier;
merged into main as a read-only fix.
```

Therefore, `mcp-server/` is no longer only a future candidate in repository terms. It is a bounded read-only verification artifact, still partial / to verify as a whole.

## Current reconciliation position

### Accepted

```text
WHAT_RUNS.md is an active support status-honesty map.
It does not replace AUTHORITY_INDEX.md or MODULES.md.
It constrains runtime-language interpretation.
mcp-server/ may be described as implemented read-only / partial / protected path.
```

### Still to verify

```text
broader mcp-server/ suite and coverage;
dashboard boundary;
Pantheon Control static prototype language;
AUTHORITY_INDEX.md grouped rows;
MODULES.md row wording.
```

### Still to arbitrate

```text
Whether AUTHORITY_INDEX.md should add a grouped row for mcp-server/ as implementation artifact / read-only verification surface.
Whether MODULES.md should keep active_support wording exactly or qualify it as implemented read-only / partial.
How to classify docs/assets/pantheon-control/: static prototype, partial read-only mirror, or cockpit candidate.
```

## Temporary rule

Until `AUTHORITY_INDEX.md` and `MODULES.md` are explicitly aligned:

```text
If runtime availability wording differs,
use the following status for mcp-server/:
implemented read-only / partial / protected path.
```

This rule does not promote the server into a runtime. It recognizes the read-only verification artifact while preventing accidental authority expansion.

## Current target classification

```text
Path or area: mcp-server/
Authority class: implementation artifact / read-only verification surface
Repo state: implemented read-only / partial / protected path
Boundary: may validate structure/status and return status data only; must not execute, approve, send, schedule, route providers, install, update, write external systems or promote memory.
```

`docs/assets/pantheon-control/` should remain:

```text
static prototype / partial read-only mirror / to verify
```

because the static UI may mirror read-only verifier logic, but it is not a live cockpit, approval engine, memory engine or runtime.

## Required follow-up edits

After maintainer review, update:

1. `AUTHORITY_INDEX.md` — add or revise rows for `WHAT_RUNS.md`, `STATUS_SPINE_RECONCILIATION.md`, `REPOSITORY_CONSOLIDATION_LANDING_PLAN.md`, `docs/assets/pantheon-control/` and `mcp-server/`.
2. `MODULES.md` — align MCP policy server row with the implemented read-only / partial status.
3. `WHAT_RUNS.md` — already updated after PR #239; keep aligned with future MCP changes.
4. `STATUS.md` — already updated after PR #239; keep only posture and live exceptions, not the full implementation argument.

## Boundary

This reconciliation is a safety brake.

It does not authorize additional protected-path modification. It does not create a dashboard. It does not allow runtime claims in public copy.

```text
Status first.
Evidence before promotion.
Protected review before implementation claims.
Human decision before authority change.
```
