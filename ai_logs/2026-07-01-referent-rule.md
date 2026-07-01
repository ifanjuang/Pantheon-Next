# AI log — the referent rule (B-5)

Date: 2026-07-01.

Actor: Claude Code.

## Intent

Arbitration B-5 (accepted, targeted pruning disciplined by a hard rule). The #246
audit found doctrine growing faster than its referent (~20:1 spec/impl, 60 open
candidates). The counterweight is a promotion rule, not a freeze.

## Change

- `docs/governance/AUTHORITY_INDEX.md` gains a "Promotion rule — the referent (B-5)"
  section before the authority map: promoting a `candidate` to `active`/`implemented`
  requires a referent (a schema, a test, an end-to-end example, a read-only
  verification surface, or an explicit dated human decision in `ai_logs/`). Without a
  referent it stays a note/candidate. The rule governs promotion; it demotes nothing
  by itself.

## Boundary

Documentation / doctrine wording only. Adds a promotion discipline; changes no
existing row, schema, test, `mcp-server/` code or runtime.
