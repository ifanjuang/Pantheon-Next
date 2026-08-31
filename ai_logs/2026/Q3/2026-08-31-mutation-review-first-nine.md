# First nine consequential-mutation entry points reviewed

Date: 2026-08-31

Status: validation-only trace — governance review record, no runtime change.
Boundary profile: validation_only_trace.

## Objective

The widened discovery net in #877 enumerated 72 mutation entry points and left 64
carrying `_UNREVIEWED` — enumerated but never read. Reviewing one means deciding
whether its effect is consequential in the doctrine's sense, or whether its local
guard chain suffices and should be declared as such.

## Why these nine first

Cross-referencing the inventory against the symbol layer separates the backlog by
whether anything in production reaches the point at all:

```text
entry_reachable    55
test_called_only    8
never_called        1
```

The nine non-live points were taken first for cost, not urgency: with no runtime
caller, the question is answerable without unwinding a call graph. This is the
cheap end of the backlog and it is stated as such.

## What the review found

Seven were cleared as `none` — meaning a human read the path and judged its local
chain sufficient, which is a conclusion and not an absence. Two were not:

```text
human_access.py::bind_oidc_identity      gate_required_not_wired
apu_owner.py::store_reviewed_dossier     gate_required_not_wired
```

That is the moment an external identity becomes able to act as a governed
principal. Its local chain is the strongest in its module — a disabled principal
is refused, issuer/subject/bound_by are required, a conflicting binding to
another principal is refused — and it is still an authorization boundary rather
than a bookkeeping write. Nothing routes it through the governance check.

The vocabulary had no way to say that. It could express "calls the chokepoint",
"can call it, off by default" and "local guards only"; it could not express
"reviewed, and this one needs the gate it does not have". Collapsing that into
`none` would have lost the only record that the decision was ever taken, so the
regime was added, with a ceiling of one so it cannot become a parking space.

## Two findings that are not classifications

**Revocation leaves no trace of who performed it.** `create_principal` records
`created_by`. `disable_principal` and `revoke_oidc_binding` record no actor at
all. The direction is safety-increasing, which is why neither is recorded as
needing the gate, but an access withdrawal that cannot be attributed is a gap in
the trail rather than a property of a thin path.

**The human-access lifecycle is half-wired.** Four of its six mutation points are
not reached from production — creating a principal, binding an OIDC identity and
revoking that binding are exercised only by tests, and disabling a principal is
called by nothing anywhere. The two that are live are `grant_access` and
`revoke_grant`, both still unreviewed. So the surface that decides who may act
exists in code and is not in service.

## The eight earlier entries gained their reasoning

Requiring a rationale on every reviewed entry caught the eight cleared in #877:
they carried a verdict and a guard list with no recorded reasoning. `none` is the
easiest value to write and the hardest to audit later. Their reasoning is now
written down rather than the requirement being relaxed to accommodate them.

## Boundary

Protected paths touched: `implementation/tests/` — one inventory file.
Runtime impact: none. No mutation path is changed, wired or unwired by this.
Authority impact: none. Each verdict is a proposal for arbitration; by doctrine
the human decides what is consequential.
Schema/test/CI impact: one new gate regime, two new guards, one lowered ceiling.
External action: none.
Memory behavior: none.

## Local distinctions

```text
reviewed as none    != unreviewed
reviewed as none    != unprotected
enumerated          != read
verdict             != reasoning
needs the gate      != reaches the gate
not in service      != safe
```

## Next decision

The 55 live entry points. They cannot be answered this cheaply: each has a
production caller whose context decides whether the effect is consequential. The
natural next batch is `human_access.py::grant_access` and `revoke_grant`, because
the module's other four are now on record and those two are what actually decide
who may act.


## Amendment, 2026-08-31 — one verdict was wrong, and a review caught it

`store_reviewed_dossier` was first recorded as `none`, on the reasoning that
`review_ref` carries a review that already happened, so the consequence gate
belonged at that review rather than at its recording. This log even called it the
closest call of the nine.

It was still wrong. `review_ref` passes through `_required` only — a check that
the string is non-empty. There is no lookup, no foreign key, no signature, and no
table of governed reviews to point at; `source_review_ref` in the write-
preparation schema is likewise plain text. The verdict therefore rested on an
unverified caller assertion while the function installs canonical APU state.

That is the distinction this repository makes everywhere else, and one this same
session wrote down when observing the policy service report
`gate_signal_validation_performed: false`:

```text
provided reference != validated decision
caller asserts     != repository verified
closest call       != call it either way
```

Reclassified as `gate_required_not_wired`. The ceiling for that regime moves from
1 to 2 — deliberately, which is the mechanism the ceiling exists for, rather than
by softening the verdict to keep the number.

Worth recording plainly: this is the fifth finding from the same reviewer in this
session and the first to catch a *judgment* rather than a coding slip. Flagging an
entry as the closest call and then still deciding it the easy way is exactly the
failure mode the `reviewed` field was added to expose.
