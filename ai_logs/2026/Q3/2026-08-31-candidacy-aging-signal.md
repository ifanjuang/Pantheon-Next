# Candidacy aging signal

Date: 2026-08-31

Status: validation-only trace — documented and implemented as a read-only CI signal.
Boundary profile: validation_only_trace.

## Objective

Make the difference visible between a candidate deliberately kept as a candidate
and a candidate nobody has revisited since it was written. Today those two states
are indistinguishable, so the absence of a decision reads exactly like an
oversight.

## Repository baseline

```text
main = c4958c3
99 candidate documents out of 209 governance documents
```

Existing owners were read before adding anything. `AUTHORITY_INDEX.md` already
owns the authority vocabulary and the promotion rule (B-5), including its
explicit statement that a candidate does not become active doctrine by age. The
signal is documented there rather than in a new governance document.

## Change

- Added: `.github/scripts/check_candidacy_aging.py` — a read-only report.
- Added: `tests/test_candidacy_aging.py`.
- Updated: `docs/governance/AUTHORITY_INDEX.md` — a subsection under the
  promotion rule describing the signal and the optional `Candidacy reviewed:`
  header line.
- Updated: `.github/workflows/governance-ci.yml` — one step.

## Why the start date is derived, not written

A written start date is a claim that goes stale silently; the commit history is
a fact. The check walks each candidate's commits backwards to find when the
document last entered the candidate state.

This repository's history begins at its own import commit and the predecessor
repository is retired. For a document that arrived with that import, the real
candidacy start is not observable here, so the check reports it as `imported`
rather than giving it a fabricated age. All 99 current candidates are in that
state today; the observable clock starts now.

## What the check refuses

A document may restart its own clock with `Candidacy reviewed: <date> (<record>)`
in its header block. The check fails when that marker is malformed, dated in the
future, points outside `ai_logs/`, or cites a record that does not exist. An
aging reset backed by a missing record is worse than no reset.

Both directions were verified against the real corpus before commit: a valid
marker moves a row out of `imported`; a dangling one exits non-zero and names the
document.

## Boundary

Protected paths touched: `.github/scripts/`, `.github/workflows/` — read-only
validation only.
Runtime impact: none.
Authority impact: none. The signal promotes, demotes and archives nothing.
Schema/test/CI impact: one new CI step that reports and does not fail on age.
External action: none.
Memory behavior: none.

## Local distinctions

```text
age != referent
aging signal != promotion
unresolved != forgotten
written date != observed fact
import date != candidacy start
CI report != decision
```

## Next decision

The report is empty of aged rows today by construction. It becomes informative
at the first threshold crossing, at which point each row needs one of three
outcomes: promotion with a referent, archival, or a dated review. Nothing in
this change makes any of those automatic.
