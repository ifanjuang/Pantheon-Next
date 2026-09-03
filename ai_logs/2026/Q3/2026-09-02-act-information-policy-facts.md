# The act gate told the decision point it reached outside Pantheon

Date: 2026-09-02

Status: implemented — `act_working_information`'s policy candidate now
declares its own request facts instead of leaving them to the transport's
defaults. Corrects a defect introduced by #940.
Boundary profile: bounded_implementation_change.

## Change

- Updated: the candidate `act_working_information` builds for
  `enforce_consequential` — `request` now carries the policy facts
  (`intent`, `external_effect`, `writes_state`, `transmission_requested`,
  `memory_promotion_requested`, `professional_position`,
  `financial_or_contractual_effect`, `scope`) rather than domain
  identifiers.
- Added: `test_the_act_is_declared_to_the_decision_point_as_a_local_state_write`.
- Removed: nothing.

## Why

#940 put `{information_id, series_id, expected_revision}` in the
candidate's `request`. `policy_request.build_preflight_payload` keeps only
the fields the policy transport declares, so all three were dropped — and
it then applies `request.setdefault("external_effect", bool(candidate.get(
"external_effect", True)))`. The default is **True**: a candidate that
says nothing about its external effect is assumed to have one.

So the gate told the PDP that acting an Information version reaches
outside Pantheon. It does not: it supersedes one row and promotes
another, both in the local store, and sends nothing anywhere.

The consequence is not cosmetic. `pantheon_mcp.policy.classify_request`
branches on that flag first (`if external is True ... consequence = "K4"`),
so the write classified as **K4 at ceiling C3** instead of **K3 at C2**.
The gate supplies `approval_level = required_ceiling = "C2"`, so the PDP
additionally reported `human_decision_level_at_required_ceiling` as a
missing requirement — a third refusal reason on top of the two every
gated write currently carries.

`human_access.bind_oidc_identity` (#935), `apu_owner.store_reviewed_dossier`
(#938) and `knowledge._gate_knowledge_write` (#939) all state these facts
explicitly and were never affected. This gate was the only one that did
not, and it was the newest.

## How it was found, and what it does not fix

Found while answering a different question — whether a real Policy
Decision Point exists behind `enforce_consequential`. It does:
`mcp-server/` serves both endpoints `HttpPolicyClient` calls, with real
classification rules. Running the real `PantheonPolicyService` against the
exact candidate each gated module builds showed this one classifying K4
where its three siblings classify K3.

That audit surfaced a second, larger finding this change deliberately does
**not** address: every `writes_state: True` request classifies K3, and K3
requires `task_contract_ref` and `evidence_pack_candidate_ref` as well as
`human_decision_ref`. All five gates wired in #935/#938/#939/#940 supply
only the third, so all five are refused by the real PDP with
`blocked_pending_task_contract`. Only the pre-existing
`knowledge_update.apply_knowledge_update` supplies all three.

That is not a missing parameter to be patched here. A Task Contract
governs delegated work; these five are human-originated Cockpit and CLI
writes, which have a decision reference and structurally have no Task
Contract. Whether the classifier should distinguish human-originated from
delegated writes is a doctrine question, recorded for review rather than
resolved by an implementation change.

## Boundary

Boundary profile applies: `bounded_implementation_change`.

Protected paths touched: no.
Runtime impact: none today — no deployment configures a decision point, so
the gate is unreachable either way. Against a configured PDP the write is
now classified and refused as what it is (K3/C2) rather than as an
external effect (K4/C3).
Authority impact: none gained. The write remains refused by the real PDP
for the unrelated reason above; this change only stops it misdeclaring
itself.
Schema/test/CI impact: no schema change; one test added.
External action: none.
Memory behavior: none.

## Verification

```text
implementation/tests   1303 passed, 387 skipped
tests/                  595 passed
```

Against the real `PantheonPolicyService`, same candidate, before and after:

```text
before  K4 | ceiling C3 | missing: reviewed_task_contract_ref,
                                   evidence_pack_candidate_ref,
                                   human_decision_level_at_required_ceiling
after   K3 | ceiling C2 | missing: reviewed_task_contract_ref,
                                   evidence_pack_candidate_ref
```

The new test skips locally (no PostgreSQL here) and runs in the CI
pgvector lane.

## Local distinctions

```text
field omitted        != field defaulted safely
gate wired           != gate payload correct
gate payload correct != gate accepted by the real PDP
```
