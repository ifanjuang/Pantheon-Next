# The boundary-profile vocabulary had an owner, a rule and no check

Date: 2026-09-06

Status: implemented — a seeded ratchet now requires every `Boundary profile:`
declaration in a live document to name a profile `BOUNDARY_PROFILES.md` actually
defines. No document changed; CI stays green. The vocabulary decision itself is
#1000's.
Boundary profile: validation_only_trace.

## Change

- Added: `tests/test_boundary_profile_vocabulary_conformance.py` — two tests, a
  10-entry seeded allowlist, and a parser that reads the defined set from the
  owner document instead of restating it.
- Removed: nothing. No document, no check, no existing test touched.
- Opened: #1000, the vocabulary reconciliation decision.

## Why

Sizing #996's next slice — the 49 `docs/governance/` root documents — required
knowing what to migrate them *to*. Checking that first turned up the problem:

```text
BOUNDARY_PROFILES.md   active support doctrine   defines the vocabulary   7 names
STATUS_HEADER_RULES.md active support doctrine   defines the line syntax
enforcement                                      none
```

```text
$ grep -rl 'Boundary profile' tests/ .github/scripts/
(nothing)
```

Two owners, both active support doctrine, and nothing anywhere compared a
declared profile against the defined set. So the vocabulary drifted:

```text
 7  names defined by the owner   (2 of them never used)
19  names in use it does not define
37  declarations carrying one    (10 live documents, 27 ai_logs)
```

The drift is not exotic. It includes two near-misses of defined names
(`validation_only` for `validation_only_trace`, `candidate_support_doctrine` for
`candidate_support_note`) — both mine, in `ai_logs/` entries written this
quarter — and six free-form phrases in a slot the owner specifies as a single
identifier.

It also includes two real gaps rather than sloppiness. Every defined profile
asserts `implementation: false` / `runtime: false`, so a change under
`implementation/` has no admissible profile at all; 14 declarations invented
one. And the owner defines `active_support_doctrine` for documents that
*support* accepted doctrine, with nothing for a document that **is** it.

## Why this had to come before #996's next slice

#996 migrates 112 documents onto this vocabulary. Migrating onto an unenforced
vocabulary is how the drift arrived; doing it 112 more times would multiply it.
The 49-document `docs/governance/` slice is therefore held, not abandoned — it
resumes once #1000 settles the target set, and two of its files
(`GLOSSARY.md`, *canonical*; and the four `validation-only` checklists) sit
exactly on the gaps #1000 has to close.

## Why a ratchet again, and what makes this one different

Same mechanism as #995 and for the same reason — seed what exists, refuse what
is new, force delisting on repair — with one addition that matters:

```text
the defined set is parsed from BOUNDARY_PROFILES.md, not restated in the test
```

So defining a profile in the owner admits it repository-wide with no test
change. The test enforces the owner's decision; it does not hold a second copy
of it. That was proven, not assumed — see the second mutation below.

## What is deliberately not governed

`ai_logs/` is excluded. A past entry's declared profile is part of what that
intervention recorded about itself, and rewriting it edits the trace. Its 27
non-conforming declarations are counted in #1000 and left alone. Whether traces
should be normalized to a later vocabulary is a maintainer decision, and it is
the same class as `docs/audits/` in #996's non-goals.

## Verification

```text
tests/                                    675 passed
check_status_headers.py                   OK
check_internal_links.py                   OK
check_no_truncation.py                    OK
check_obsolete_authority_consistency.py   OK
```

Both directions were mutated and observed to fail before the mutations were
reverted and the tree confirmed clean:

```text
a live document declares `invented_thing`
  -> failed, naming ('docs/governance/MODULES.md', 'invented_thing')

the owner is given a `### `external_reference_review`` section
  -> failed, demanding the now-admitted name leave the allowlist
```

The second mutation is the one worth recording: it proves the owner-driven
admission path works, so #1000 can be resolved by editing doctrine rather than
by editing this test.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none. Test-only; no document, schema or runtime changed.
Authority impact: none. The test grants nothing and defines no profile; it
enforces an existing active-support-doctrine vocabulary against its own owner.
It cannot widen what a profile means.
Schema/test/CI impact: one new test file, two tests. No existing test modified,
weakened, skipped or removed.
External action: none.
Memory behavior: none.

## Local distinctions

```text
rule owned          != rule enforced
vocabulary defined  != vocabulary used
name drift          != naming gap
ratchet             != decision
```
