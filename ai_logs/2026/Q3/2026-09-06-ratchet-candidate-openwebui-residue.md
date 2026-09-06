# The retirement guard was green because it never looked at candidate doctrine

Date: 2026-09-06

Status: implemented — a second, seeded ratchet now bounds retired-owner
residue in candidate doctrine across `docs/governance/` and
`docs/domain-packs/`. No document was changed; CI stays green.
Boundary profile: validation_only.

## Change

- Added: `FORBIDDEN_OWNERSHIP_PHRASES` and `DOCTRINE_ROOTS` constants,
  `_residue_paths()` (one shared traversal), `KNOWN_CANDIDATE_OPENWEBUI_RESIDUES`
  (67 entries, seeded as-is), and
  `test_candidate_doctrine_openwebui_residue_is_bounded_and_only_shrinks`.
- Updated: `test_active_governance_openwebui_ownership_residue_is_explicitly_bounded`
  now calls the shared traversal instead of carrying its own inline phrase list.
  Its semantics are unchanged: current authority must stay at zero.
- Removed: nothing. No Markdown document was touched.

## Why

`test_openwebui_integration_owner_retirement.py` guards a real decision —
OpenWebUI is retired and must not be named as a current architecture owner.
It was green. It was also, measurably, not looking at the problem.

`_is_current_authority()` admits only documents whose status begins
`canonical doctrine`, `active doctrine` or `active support`. Everything marked
`candidate` is skipped before its content is read. Counted across the two
doctrine roots:

```text
retired-owner phrase present, current authority :  0
retired-owner phrase present, candidate         : 67
```

So the guarantee `KNOWN_CURRENT_AUTHORITY_OPENWEBUI_RESIDUES = set()` is exact
and worth keeping — and it means "zero residue *among documents of authority*",
not "zero residue". Every single offender sits in the class the guard excludes
by construction.

That exclusion is not a bug in the test; it is a deliberate scope that was
written in a six-line helper and stated nowhere else. The cost of leaving it
implicit was measured this morning: `docs/domain-packs/architecture/` sat
outside on two counts at once — wrong directory *and* candidate status — and
accumulated 21 boundary triads naming a retired integration, until #993 swept
them by hand.

## Why a ratchet rather than a sweep

Seeding the list with what exists keeps CI green and forces no document to
change, while making the debt exact and monotonic:

```text
unexpected == set()        -> no new document may introduce the phrase
no_longer_present == set() -> fixing one forces removing its entry
```

The list can only shrink. This is the same mechanism #785 used to drive
current-authority residue to zero, applied one authority class wider.

It is explicitly not the cure. The triad is duplicated boundary boilerplate,
and `BOUNDARY_PROFILES.md` (active support doctrine) already owns the remedy:
`exposed_by` / `executed_by` / `governed_by` are exactly what the triad states
in longhand. 74 documents already declare a `Boundary profile`; 93 still restate
the triad by hand, and only 5 do both — a migration begun and stalled. Finishing
it removes the class of problem, at which point this ratchet and its list can be
deleted outright. That work is #787's, whose own success criterion ("repeated
boundary boilerplate is reduced through existing reusable profiles where safe")
is measurably half-met despite the issue being closed.

## Verification

```text
tests/                     665 passed
check_status_headers.py    OK
check_internal_links.py    OK
check_no_truncation.py     OK
```

The ratchet was proven to bite in both directions before being kept, then the
mutations were reverted and the tree confirmed clean:

```text
appended the phrase to an unlisted candidate  -> failed ("newly states")
fixed a listed file without delisting it      -> failed ("is fixed — remove it")
both reverted, git diff empty                 -> 10 passed
```

## Boundary

Boundary profile applies: `validation_only`.

Protected paths touched: no.
Runtime impact: none. Test-only; no runtime, schema or document changed.
Authority impact: none. The ratchet records debt; it grants nothing and
promotes no document to authority.
Schema/test/CI impact: one test file; one test added, one refactored to share a
traversal so the two phrase lists cannot drift apart.
External action: none.
Memory behavior: none.

## Local distinctions

```text
guard green        != subject clean
scope deliberate   != scope written down
debt bounded       != debt removed
ratchet            != cure
```
