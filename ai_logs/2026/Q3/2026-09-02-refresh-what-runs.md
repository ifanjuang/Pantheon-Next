# Refreshing WHAT_RUNS.md's chokepoint row

Date: 2026-09-02

Status: validation-only trace — governance status-map refresh, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Updated: the `WHAT_RUNS.md` "Internal consequential-write chokepoint" row and
  the file's date header.
- Added: this log.
- Removed: nothing.

## Why

`WHAT_RUNS.md` is the repository's own runtime-status honesty document — the
one it names in `STATUS.md` as the owner of "runtime-status honesty" and the
one `ROADMAP.md` points readers to instead of a release checklist. It had gone
stale the same way the mutation inventory's own founding paragraph did in
#935: it still read "71 have been individually reviewed and 21 remain
explicitly unreviewed" and "Nine reviewed entries are currently
`gate_required_not_wired`" after #932 closed the backlog to 92/92 and #935
wired a second gate, dropping the pending count to five.

A document whose entire purpose is to state current runtime status is the one
document that cannot be allowed to describe a superseded state without saying
so.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — a documentation update.
Authority impact: none.
Schema/test/CI impact: `check_obsolete_authority_consistency.py` and
`check_internal_links.py` verified locally; both pass.
External action: none.
Memory behavior: none.

## Local distinctions

```text
status document       != current status, unless kept current
backlog closed         != the document that said so, updated
gate count changed      != every reader of that count informed
```
