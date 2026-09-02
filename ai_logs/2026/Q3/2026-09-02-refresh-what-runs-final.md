# WHAT_RUNS.md went stale within the hour, again

Date: 2026-09-02

Status: implemented — the chokepoint row in `docs/governance/WHAT_RUNS.md`
now reflects all six wired write paths and a `gate_required_not_wired`
ceiling of 0.
Boundary profile: active_support_doctrine.

## Change

- Updated: the "Internal consequential-write chokepoint" row.

## Why

`#937` refreshed this row against the state after `bind_oidc_identity`
(#935) was wired, when four gates (`store_reviewed_dossier`,
`publish_knowledge`, `complete_edit_request`, `apply_edit_request`) were
still pending and a fifth (`act_working_information`) hadn't been named
as reviewed yet in the row's own text. #938, #939 and #940 then wired or
closed all five before #937 merged — so the refresh was already behind
its own subject by the time it landed. Same failure mode the founding
paragraph of the mutation inventory names about itself: a record rots at
its premises, and this row's premise (two boundaries wired, five pending)
stopped being true within the hour.

This pass writes the row against the actually-merged state on `main`:
six write paths wired, zero pending. It also adds one sentence the prior
version didn't have — that none of this establishes a real Policy
Decision Point is configured and reachable anywhere, or what such a PDP's
rules would actually decide beyond the shape `enforce_consequential`
requires. That gap was raised in conversation as the next open question
for this repository and belongs in the status row, not only in chat.

## Boundary

Boundary profile applies: `active_support_doctrine`.

Protected paths touched: no.
Runtime impact: none — documentation only.
Authority impact: none.
Schema/test/CI impact: none.
External action: none.
Memory behavior: none.

## Verification

Read against `main` at the six gated call sites (`knowledge_update.py`,
`human_access.py`, `apu_owner.py`, `knowledge.py` ×2, `agency_information.py`)
and the mutation inventory's own pending-gate assertion
(`test_a_required_gate_that_is_not_wired_stays_visible_and_does_not_grow`,
ceiling 0). No code changed; nothing to run beyond confirming the claims
against the source they describe.

## Local distinctions

```text
gate wired  != Policy Decision Point configured
gate wired  != PDP has real rules behind it
doc refreshed once != doc stays true
```
