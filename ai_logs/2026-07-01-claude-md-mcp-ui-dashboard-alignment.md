# AI log — align CLAUDE.md with the real MCP / UI / dashboard state (B-1)

Date: 2026-07-01.

Actor: Claude Code.

## Intent

Arbitration B-1 (accepted with reformulation) from the maintainer's decision on
the #246 audit. `CLAUDE.md` still described `dashboard/` as an active thin module
that "verifies installs from their logs", while in reality:

- the read-only verifications (`verify_install / observability / backup / exposure /
  update`) live in `mcp-server/`;
- the only UI surface today is the static prototype `docs/assets/pantheon-control/`;
- there is no `dashboard/` module.

The maintainer's rule: `mcp-server/` verifies (read-only), the UI exposes; MCP must
not become the UI; a real `dashboard/` stays **voluntarily absent** until it exists.

## Change (CLAUDE.md, ~4 targeted edits)

- Doctrine intro: "two bounded modules" -> "bounded surfaces" (a `dashboard/`
  module does not yet exist).
- Repository structure: `mcp-server/` is named as the read-only verification
  surface (the `verify_*` checks) and "it verifies; it is not the UI"; the third
  zone becomes "the exposure surface", today only the static
  `docs/assets/pantheon-control/` prototype, with the `dashboard/` module marked
  voluntarily absent until built — the UI exposes, `mcp-server/` verifies.
- Non-negotiable boundaries: the module bullet is reworded from `dashboard/` to
  "the exposure surface (`docs/assets/pantheon-control/` prototype today; a
  `dashboard/` module later)"; `mcp-server/` gains "it does not become the UI".
- Migration policy: reference the exposure-surface prototype instead of a
  `dashboard/` module.

## Boundary

Documentation / doctrine wording only, aligning the working doctrine with the real
tree. `CLAUDE.md` is a protected path; this is the small, explicitly-approved B-1
edit. No schema, test, `mcp-server/` code, runtime or other protected-path change.
The one-way dependency and the chokepoint are unchanged. No new module is created;
a `dashboard/` module remains voluntarily absent.
