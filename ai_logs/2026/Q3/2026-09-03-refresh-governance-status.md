# implementation/GOVERNANCE_STATUS.md went stale the same way WHAT_RUNS.md did

Date: 2026-09-03

Status: implemented — `implementation/GOVERNANCE_STATUS.md` now lists all
six wired chokepoints and states, as fact rather than silence, that five
of them are refused by a real Policy Decision Point today.
Boundary profile: active_support_doctrine.

## Change

- Updated: "Current executable owners" adds the four newer chokepoints
  (human OIDC identity binding, APU reviewed-dossier import, Knowledge
  publish/edit-application, Agency Information act); "Selected
  implementation status" adds one `wired_not_connected` line per new
  chokepoint; a new paragraph states the real-PDP classification finding
  as verified fact with a citation; "Adoption gates still open" adds the
  Task Contract / Evidence Pack doctrine question raised earlier today.
- Removed: nothing.

## Why

`GOVERNANCE_STATUS.md` was last touched 2026-08-29 (PR #812), before
`bind_oidc_identity` (#935), `store_reviewed_dossier` (#938),
`publish_knowledge`/`apply_edit_request` (#939) and
`act_working_information` (#940, #942) all merged. It named exactly one
chokepoint, `knowledge_update_chokepoint`, and said nothing about the
other five now live on `main`.

Found by a repo-wide audit run today across four parallel zones
(governance docs, `mcp-server/`, `implementation/`, everything else). The
`implementation/` audit read this file at face value and reported "the
chokepoint is wired into only one write path" — an accurate reading of a
stale document, which is exactly how staleness propagates: a correct
report about the wrong ground truth. Cross-checking against `main`'s
actual `mvp_vertical/` source (not this doc) found five more.

This is the third instance of the same failure mode this session
(`WHAT_RUNS.md` twice, #937 and #941; `test_consequential_mutation_
inventory.py`'s own founding paragraph once). A status document is not
self-updating; every one of these needed a human or an audit to notice
before the mismatch was ever visible.

## What this update adds beyond the miss count

Section 3 of this repository's own doctrine (Task Contracts govern
delegated work) collides with what was actually built: the five newer
chokepoints gate writes a human makes directly — publishing Knowledge as
reviewed, acting an Information version, importing a reviewed APU
dossier, binding an OIDC identity, applying a decided edit — none of
which are delegated work with a Task Contract behind them. Run against
`mcp-server`'s real `PantheonPolicyService`, all five classify K3 (because
they declare `writes_state: true`) and K3 requires `task_contract_ref`
and `evidence_pack_candidate_ref`, which none of the five supply. Only
`knowledge_update_chokepoint` supplies both, which is why it alone is
admitted.

This was verified empirically, not inferred: running the real service
against each gate's exact candidate payload returns
`blocked_pending_task_contract` for all five. The finding and the
verification are in `ai_logs/2026/Q3/2026-09-02-act-information-policy-
facts.md`; this update makes the fact visible in the status document a
deploying reader would actually consult, rather than leaving it buried in
a narrower fix's log entry.

The doctrine question itself — whether the classifier should distinguish
human-originated writes from delegated ones — is recorded as an open
adoption gate, not resolved here. Resolving it is a governance decision,
not a documentation update.

## Boundary

Boundary profile applies: `active_support_doctrine`.

Protected paths touched: no.
Runtime impact: none — documentation only.
Authority impact: none.
Schema/test/CI impact: none.
External action: none.
Memory behavior: none.

## Verification

```text
check_status_headers.py    OK
check_internal_links.py    OK
check_no_truncation.py     OK
```

No code changed; the six chokepoint claims were each read against the
`mvp_vertical/` source that implements them, and the real-PDP refusal
claim was read against the verification already recorded in
`2026-09-02-act-information-policy-facts.md`.

## Local distinctions

```text
chokepoint wired      != chokepoint admitted by a real decision point
status doc accurate   != status doc current
one correct reading   != the ground truth it read was current
```
