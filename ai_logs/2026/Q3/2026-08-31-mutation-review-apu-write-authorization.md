# Mutation review: APU write authorization and governed Claims

Date: 2026-08-31

Status: validation-only trace — governance review record, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Added: `ai_logs/2026/Q3/2026-08-31-mutation-review-apu-write-authorization.md`.
- Updated: four inventory verdicts across `apu_write_preparation.py`,
  `apu_mapping_reviews.py` and `agency_claims.py`; one existing verdict
  enriched; unreviewed ceiling 25 → 21.
- Removed: nothing.

## Why

The eight entries recorded as `gate_required_not_wired` across this review all
fail the same way: they accept a claim that a decision happened. This batch went
looking at the APU write path because it is where the repository models a
decision as an object, and the question worth answering was whether that object
is consulted or merely stored.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — no executable behaviour changes.
Authority impact: none — the verdicts are review records, not approvals.
Schema/test/CI impact: the inventory test's unreviewed ceiling moves; no schema
or workflow changes.
External action: none.
Memory behavior: none.

## The finding: the missing pattern already exists here

`append_authorization` writes a row carrying `command_payload_digest`, taken
from the stored command rather than from its caller. `apply_authorized_write_command`
then refuses to act unless two things hold:

```python
if not items or items[-1]["action"] != "authorize_application":
    raise ApuWritePreparationError("latest write authorization must authorize_application")
if authorization["command_payload_digest"] != command["payload_digest"]:
    raise ApuWriteApplicationConflict(
        "latest authorization does not cover the exact command payload digest")
```

**An authorization here covers a specific content, not a name.** A later
rejection blocks the apply, and an authorization that no longer matches the
bytes being applied is refused.

Set that beside the eight:

```text
store_reviewed_dossier    a review_ref that is a bare non-empty string
publish_knowledge         review_status="reviewed" asserted in the body
resolve_request           identity_assurance="authenticated" asserted in the body
apply_edit_request        a status two functions can write with no decision behind it
...
append_authorization      a digest computed from the thing being approved
```

This is not a design the repository lacks. It is a design the repository has,
in one place, and does not apply where it records approvals elsewhere.

## And I nearly got this one backwards

A first grep for consumers of `append_authorization` returned the writing route
and a read-back route, and I was about to record that nothing consults the
authorization. A second grep for `authorize_application` found
`_latest_application_authorization`, which is the enforcement.

That would have been the eighth instance of this review's own recurring failure
— asserting from a search result taken for the search. It was caught before it
was written, which is the first time in this session that has happened.

## The other verdicts

`prepare_write_command` does not accept its target. It reads the latest selected
mapping review, takes `selected_stable_object_ref` from there, and refuses if
that object has left the mapping's candidates or been retired.

`append_mapping_review` refuses a `mapping_ref` that is not present in the
execution result it names, so a review cannot exist against a mapping that was
never produced.

`record_claim` says of itself that it "records an assertion; it approves
nothing", and its `status` and `certainty` arrive from the caller with defaults.
What holds them is below Python and stronger than anything else this review has
found there: triggers on `agency_project_claims` check that a claim derived from
a candidate carries **the reviewed candidate's value**, that its `backing_ref`
is one of that candidate's `basis_refs`, and that an APU backing belongs to the
Claim's own Project.

Everywhere else in this review, the below-Python guards check a vocabulary. Here
they check that the assertion matches what it claims to be derived from.

## Local distinctions

```text
approval stored     != approval consulted
covers a name       != covers a content
checks a vocabulary != checks a derivation
records an assertion != approves it
```
