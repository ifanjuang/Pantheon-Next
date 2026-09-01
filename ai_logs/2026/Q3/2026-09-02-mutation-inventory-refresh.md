# Refreshing a governance record the code had left behind

Date: 2026-09-02

Status: validation-only trace — governance record refresh, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Added: `ai_logs/2026/Q3/2026-09-02-mutation-inventory-refresh.md`; an
  `unguarded_body` field on every `gate_required_not_wired` entry; the
  `_gate_closure` and `_normalized_function` helpers; and
  `test_a_pending_gate_is_still_absent_from_the_code_it_names`.
- Updated: three verdicts from `gate_required_not_wired` to `none` after their
  gaps were repaired; three Information projection entries and the
  `suggest_projects` entry, whose recorded defects were fixed; the
  `apu_write_preparation.apply_authorized_write_command` entry, which cited the
  projection race as a live sibling; required-gate ceiling 9 → 6.
- Removed: the `evidence` field this log's first version proposed, and the test
  built on it. Both had the polarity wrong; see below.

## Why

The mutation inventory went stale within a day of being written.

Five findings it recorded were repaired in `main` between 2026-08-31 and
2026-09-01 — the manager lockout (2f9fcfbd), the self-asserted `verified` Claim
status (b201a019), the self-chosen identity assurance (#916), the implicit
unlink in `suggest_projects` (2222a020) and the projection first-write race
(552e67e7). **None of those commits touched the inventory.**

So the record read three gates as open that were closed, and described two
defects that no longer existed, while every test in the file passed.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — this changes a test module and a log; no executable
behaviour changes.
Authority impact: none — the verdicts are review records, not approvals.
Schema/test/CI impact: the inventory test gains one check and lowers one
ceiling; no schema or workflow changes.
External action: none.
Memory behavior: none.

## Why the existing tests could not catch it

They check that every discovered entry point is **declared**, and that a
declared entry names a guard regime and a reason. Nothing checks that the reason
is still true. A verdict, once written, was permanent until someone re-read it.

That is precisely the failure the inventory exists to record — a record
describing a state its subject has left — committed by the inventory itself. It
joins the list the review has been keeping, and it is the first entry on that
list that is structural rather than an error of reading.

## The repair, and why this shape

Each `gate_required_not_wired` entry is checked on two axes, and both of them
assert an **absence**:

- `_gate_closure` is the mirror of `_writer_closure` — seeded on
  `enforce_consequential` and followed through the same call graph. A pending
  verdict is exactly the claim that an entry point is in the writer closure and
  not in the gate closure, so this is what makes the claim checkable. The gate
  closure currently reaches three functions (`policy_gate.governed_effect`,
  `capability_manager.governed_execute`,
  `knowledge_update.apply_knowledge_update`) and none of the six pending ones.
- `unguarded_body` is the sha256 of the function as `ast.unparse` renders it,
  pinning the body that was read when the verdict was taken. It catches a repair
  made by any means other than the gate — validating the `review_ref`, guarding
  the status, taking an actor. Going through the parser is deliberate: a rewrap
  or a comment leaves the digest alone; a change in what the function does does
  not.

This is deliberately the pattern the review recommended everywhere else, and the
one `apu_write_preparation.append_authorization` already uses: **bind the record
to the content it describes, not to a name.** Having spent thirteen batches
recording where the repository does not do that, the inventory had no business
not doing it either.

Verified by injecting each repair shape rather than by reading the test:
`enforce_consequential(...)` in `bind_oidc_identity` fails the closure
assertion; a `review_ref` format check in `store_reviewed_dossier` fails the
digest assertion; a comment-only edit to the same function fails neither.

## The first version of this repair had the polarity wrong

Recorded because it is the same error one more time, and because the log claimed
the repair worked before review found otherwise.

The first version bound each verdict to a literal fragment of the module — a
`def` line, a parameter name, a check the function already performs — and
asserted the fragment was still **present**. But `gate_required_not_wired` is a
claim about what the code does *not* do, and every one of those fragments
survives the repair. Wiring the gate into `bind_oidc_identity` would have left
`def bind_oidc_identity(` exactly where it was and the test green.

The verification claimed above was equally hollow: renaming the function proved
the anchor detects a rename. Nobody had asked whether the function still existed.
The one scenario the test named — a repair leaving the verdict stale — was the
one it could not see.

That is the failure shape this whole review has been cataloguing, a guard
asserted from what a check is named rather than from what it composes to,
committed in the test written to stop it. It was caught by review on the pull
request, not by anything in this repository.

A second finding from the same review: the three Information projection guard
lists were refreshed to record the compare-and-swap while the `reviewed`
explanations beside them still described the first-write race as live. A record
can rot toward either verdict, and only the entry's own text says which reading
is current. All three now say they were wrong in both directions in turn.

## The cost, accepted

A body can move for a reason unrelated to the gate, and the test will then ask
for a verdict that has not changed. That is the intended trade: a false alarm
asks a question, and a stale governance record answers one wrongly. Six
known-defective functions are cheap to re-read.

## Local distinctions

```text
declared             != still true
verdict written      != verdict valid
passes its own tests != describes its subject
bound to a name      != bound to a content
present code         != absent guard
verified by breaking != verified against the scenario it names
```
