# An empty conflict list read as "nothing contradicts"

Date: 2026-09-07

Status: validation-only trace — documented non-implemented.
Boundary profile: bounded_implementation_change.

## Change

- Updated: `implementation/mvp_vertical/project_claim_conflicts.py` — one entry
  added to `LIMITATIONS` naming the scalar-only scope.
- Updated: `implementation/tests/test_project_claim_conflicts.py` — one
  module-level test, plus the same assertion inside the existing candidate test.
- Updated: `README.md`, `README.fr.md`, `docs/index.html`, `docs/index-en.html` —
  one clause each, stating the same restriction publicly.
- Removed: nothing. No schema, contract, classification or detector behavior
  changed.

## Why

`898f2fe0` put the semantic-continuity hypothesis on the READMEs and the public
landing pages: heterogeneous sources converge on governed identities, and
contradictions are preserved rather than resolved. The implementation genuinely
does this — `project_claim_conflicts.py` detects tension and refuses to resolve
it, with `resolves_conflict: False` and `merges_identity: False`.

The detector's reach is narrower than the paragraph:

```text
README spans     drawings, sections, IFC, photos
detector covers  SCAN_SCOPE = active_unsuperseded_scalar_claims
```

`SCAN_SCOPE` already said so, but it reads as configuration. `LIMITATIONS` is
what travels to a consumer with every candidate, and it listed three honest
limitations without this one. So a consumer receiving an empty candidate list had
no way to learn that a geometric or relational contradiction would never have
appeared in it.

```text
no candidates != nothing contradicts
scan scope     != stated limitation
```

## What was deliberately not changed

**The classification was not widened.** `_classification()` keys on
`effective_relation` alone while `basis_relation` and `backing_relation` are
computed and returned in `comparison`. Folding basis into classification was
considered — two Claims sharing a structured basis but disagreeing is likely a
transcription error, while disjoint bases is a genuine document discrepancy — and
rejected: three classification values times four basis relations is twelve labels
where the current design already exposes both axes and leaves the weighing to the
reader. That split is correct; merging it would trade clarity for coverage.

Ranking of candidates was also rejected. Any ordering encodes a judgment about
which contradiction matters more, and that judgment is the architect's.

## Correction to an earlier reading

Presentation was initially assessed as absent. That was wrong. The read API
already returns `conflict_candidates` plus a `conflict_projection` block carrying
scope, count and `absence_of_candidates_inferred`, which distinguishes "we looked
and found none" from "we could not look". Cockpit surfacing is what does not
exist, and `project_claim_status.md` already owns it as planned work.

## Boundary

Boundary profile applies: `bounded_implementation_change`.

Protected paths touched: no.
Runtime impact: none behaviorally. One string is added to a constant that is
already returned with every candidate; no detection, classification, persistence
or contract behavior changes.
Authority impact: none. The change makes an existing restriction legible; it
grants nothing and removes no guarantee.
Schema/test/CI impact: `project_claim_conflict_candidate.schema.yaml` constrains
`limitations` with `minItems: 2` and no maximum, so a fourth entry needs no
contract change. One test added; none weakened or removed.
External action: none.
Memory behavior: none.

## Verification

```text
implementation/tests/                     1368 passed, 408 skipped
tests/                                     675 passed
check_status_headers.py                    OK
check_internal_links.py                    OK
check_no_truncation.py                     OK
check_obsolete_authority_consistency.py    OK
```

The new assertion was first written inside the candidate-level test and found to
be **skipped** there for want of a database, so it proved nothing in this
environment. It was moved to a module-level test that runs without one, then
mutated to confirm it bites:

```text
LIMITATIONS entry removed  -> failed, printing the three remaining limitations
restored                   -> 4 passed
```

## Local distinctions

```text
scan scope        != stated limitation
no candidates     != nothing contradicts
test written      != test executed
computed field    != classification axis
```
