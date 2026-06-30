# Status Spine Reconciliation

Status: validation-only / status-spine reconciliation — to verify.

Date: 2026-06-30

This document records the current reconciliation position between:

- `STATUS.md`;
- `AUTHORITY_INDEX.md`;
- `MODULES.md`;
- `WHAT_RUNS.md`;
- `REPOSITORY_CONSOLIDATION_LANDING_PLAN.md`.

It does not create doctrine by itself, implement runtime behavior, approve a protected-path change, promote `mcp-server/`, create a dashboard, approve a PR, execute Hermes, send anything externally or promote memory.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Why this note exists

`WHAT_RUNS.md` now states the repository's runtime-status posture.

It deliberately keeps `mcp-server/` in:

```text
partial / to verify / protected review required
```

This is more conservative than some existing `MODULES.md` wording, which describes the MCP policy server as an active read-only policy / validation surface.

Until protected-path review verifies the actual code, tests and boundaries, the safe status is:

```text
to verify
```

## Current reconciliation position

### Accepted

```text
WHAT_RUNS.md is an active support status-honesty map.
It does not replace AUTHORITY_INDEX.md or MODULES.md.
It constrains runtime-language interpretation.
```

### To verify

```text
mcp-server/
dashboard boundary
Pantheon Control static prototype language
```

### To arbitrate

```text
Whether mcp-server/ should be promoted from partial/to verify to implementation artifact / read-only verification surface.
Whether MODULES.md should keep active_support wording for MCP policy server or downgrade it pending protected review.
Whether AUTHORITY_INDEX.md needs a grouped row for mcp-server/ as protected-path implementation artifact / to verify.
```

## Temporary rule

Until reconciliation is complete:

```text
If STATUS, MODULES, AUTHORITY_INDEX and WHAT_RUNS disagree about runtime availability,
use the most conservative status:
partial / to verify / protected review required.
```

This rule does not demote canonical doctrine. It prevents accidental runtime promotion by wording.

## Proposed target classification

If protected review confirms the implementation is strictly read-only, the target classification should be:

```text
Path or area: mcp-server/
Authority class: implementation artifact / read-only verification surface
Repo state: partial / protected path / to verify or implemented read-only after review
Boundary: may validate structure/status and return status data only; must not execute, approve, send, schedule, route providers, write external systems or promote memory.
```

If protected review does not confirm that boundary, the target classification should remain:

```text
candidate / to verify / protected path
```

## Required follow-up edits

After review and maintainer decision, update:

1. `AUTHORITY_INDEX.md` — add or revise rows for `WHAT_RUNS.md`, `STATUS_SPINE_RECONCILIATION.md`, `REPOSITORY_CONSOLIDATION_LANDING_PLAN.md`, `docs/assets/pantheon-control/` and `mcp-server/`.
2. `MODULES.md` — align MCP policy server row with the chosen conservative or promoted classification.
3. `WHAT_RUNS.md` — replace `partial / to verify / protected review required` only if review supports promotion.
4. `STATUS.md` — keep only posture and live exceptions, not the full implementation argument.

## Boundary

This reconciliation is a safety brake.

It does not authorize protected-path modification. It does not make `mcp-server/` active. It does not create a dashboard. It does not allow runtime claims in public copy.

```text
Status first.
Evidence before promotion.
Protected review before implementation claims.
Human decision before authority change.
```
