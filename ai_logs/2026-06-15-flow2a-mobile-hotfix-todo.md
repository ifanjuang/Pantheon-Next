# AI Log — flow2a mobile hotfix todo

Date: 2026-06-15

## Status

A mobile rendering regression remains open in issue #131 after PR #136.

## Required hotfix

Patch `docs/index.html` so the mobile version of `flow2a` no longer overlaps text.

Preferred approach:

- replace the compressed mobile `card(...)` helper with explicit mobile helpers;
- increase card heights and/or mobile viewBox height;
- keep the inner frame narrower and the lateral arrows visible;
- keep all doctrinal wording already accepted.

## Scope

Expected future diff:

- `docs/index.html`
- one follow-up `ai_logs/...` entry

No protected path.
No runtime.
