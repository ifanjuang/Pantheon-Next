# Serialising the APU write application against its own rejection

Date: 2026-09-02

Status: implemented — bounded concurrency repair in the candidate implementation.
Boundary profile: bounded_implementation_change.

## Change

- Added: `_lock_write_command` in `apu_write_preparation.py`;
  `test_appending_an_authorization_takes_the_same_command_row`; a fake
  connection in `tests/test_apu_write_application_gate.py` and
  `tests/test_h5_6_multi_source_closure.py`.
- Updated: `apply_authorized_write_command` now runs its whole verification
  chain inside one transaction, under the command-row lock;
  `append_authorization` takes the same row before writing its event; the two
  inventory entries that recorded the gap as open.
- Removed: nothing.

## Why

The review recorded `apply_authorized_write_command` as the strongest local
guard chain in the codebase, and recorded one hole in it.

`_latest_application_authorization` ran a plain SELECT over
`apu_write_authorization_events`, and the delegation to
`apu_owner.apply_source_match` followed outside any shared transaction. A
`reject_application` committing between that read and that write did not block
the apply. The digest binding — an approval bound to the exact content it
approves, the pattern the rest of the review holds up as the standard — held
under concurrency. The ordering did not.

## What the repair had to be, and why it is two-sided

The obvious reading was "the apply path is missing a `FOR UPDATE`". Reading
`append_authorization` before writing anything showed that is not the shape of
it: that function takes no lock either. It opens its transaction and inserts the
event. So a lock added on the applying side alone would have excluded nothing —
there was no shared row for the two writers to contend on.

`apu_write_command_candidates` is append-only: the trigger in
`012_apu_write_preparation.sql` refuses UPDATE and DELETE on it. That makes the
command row usable as a pure mutex — `FOR UPDATE` never changes it, and both
sides can take it without any risk of one silently rewriting the command.

The authorization events themselves cannot serve as the lock. The row that has
to be seen is a rejection that does not exist yet at the moment the applying
side reads; there is nothing there to lock.

## Boundary

Boundary profile applies: `bounded_implementation_change`.

Protected paths touched: no.
Runtime impact: two writers on one APU write command now serialise. Concurrent
applications of different commands are unaffected; the lock is per command row.
Authority impact: none — this changes when a decision is read, not who may take
it. A rejection that arrives after an application still does not undo it.
Schema/test/CI impact: no schema change; three test modules updated, one test
added.
External action: none.
Memory behavior: none.

## Verification

The unit tests that exercised this chain passed `object()` as the connection,
which held only while nothing in the chain touched it. That is no longer true —
the lock is the first thing the chain does — so they now pass a fake connection
that records the statements, and assert the lock is present and first. That is
a stronger claim than the sentinel allowed.

Both halves were verified by removal, not by reading:

```text
lock removed from append_authorization        → the authorization-side test fails
lock removed from apply_authorized_write_command → the apply-side test fails
```

What is asserted is what the code composes to: both paths issue
`SELECT ... FOR UPDATE` on the same command row before they read or write the
decision. The exclusion that follows is PostgreSQL's, and is not re-tested here.

No concurrency test with two live connections was added. It would have to be
timing-bounded, this container has no PostgreSQL to run it against, and a test
that can hang in CI is worse than the property being argued from row-lock
semantics.

## Local distinctions

```text
lock on one side     != mutual exclusion
digest binding holds != ordering holds
append-only row      != unusable as a mutex
read before the write != read inside the write
```
