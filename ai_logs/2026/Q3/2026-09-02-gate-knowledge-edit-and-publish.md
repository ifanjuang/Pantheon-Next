# Routing Knowledge publication and edit-application through the chokepoint

Date: 2026-09-02

Status: implemented — `publish_knowledge` (conditionally, on the
reviewed claim only) and `apply_edit_request` (unconditionally) now route
through `enforce_consequential`; `complete_edit_request` is closed by a
local status guard, not by wiring the chokepoint. Third and fourth of the
five originally pending gates; `complete_edit_request` was recorded as a
sixth line item in the same inventory entry but never needed the PDP.
Boundary profile: bounded_implementation_change.

## Change

- Added: `knowledge.KnowledgeGateRefused`, `knowledge.KnowledgeGatePolicyUnavailable`,
  `knowledge._gate_knowledge_write`; `cockpit_api.require_policy_client`;
  a matching `require_policy_client` closure inside
  `install_knowledge_edit_variant_routes`; `human_decision_ref` fields on
  `PublishKnowledgeBody`, `ApplyEditBody`, `ApplySelectedVariantBody`;
  `tests/test_knowledge_edit_and_publish_gate.py`.
- Updated: `publish_knowledge` and `apply_edit_request` gained
  `policy_client`, `decision_payload`, `required_ceiling` parameters;
  `complete_edit_request` gained a status guard rejecting a request that
  is not `queued_for_hermes`; `knowledge_edit_variants.apply_selected_variant`
  threads the same three parameters through both of its internal
  `apply_edit_request` calls; `cockpit_api.create_app` resolves its own
  policy client/enforcement mode (mirroring `cockpit_shell.py`, kept
  separate rather than shared — see Why); the `apply_intelligent_edit` and
  `apply_selected_edit_variant` routes require a policy client whenever
  enforcement is active; the `publish_knowledge` route requires one only
  when the request claims `review_status="reviewed"`; the inventory's
  three matching entries move off `gate_required_not_wired`; the pending
  ceiling 4 → 1; `test_knowledge_edit_variant_routes.py`'s fixture now
  states explicitly that it disables policy enforcement because it mocks
  the underlying functions and isn't exercising this gate.
- Removed: nothing.

## Why

The inventory's finding for `apply_edit_request` named it directly: "the
point where the chokepoint belongs." `publish_knowledge`'s finding was
narrower — only a caller-supplied `review_status="reviewed"` claim commits
Knowledge as reviewed without anything behind that claim; the far more
common `generated_unreviewed` write was never the problem, and gating it
unconditionally would have been a real regression, not a fix.
`complete_edit_request`'s finding was different in kind: a request already
decided (`rejected`, `applied`) could still be silently overwritten by a
fresh Hermes proposal landing late, because nothing checked `status` before
writing. That is a missing guard on an internal handoff step, not a
missing decision — Hermes filling in a proposal it was queued for is not
itself the consequential act; applying that proposal already routes
through this same gate.

## What the gates bind to

`publish_knowledge`: scope is the parent Project; the object reference is
`knowledge_item:{knowledge_id}`; the expected digest is the same
`_payload_digest` already computed for the write, so a decision cannot be
replayed against a different document body under the same publication
claim.

`apply_edit_request`: scope is the parent Project (read off the document
row, inside the transaction, after the existing staleness re-check);
the object reference is `knowledge_edit_request:{request_id}`; the
expected digest binds `{request_id, knowledge_id, base_version,
selected_text_digest, replacement_markdown}` as one unit, so a decision
taken over one proposed replacement cannot be replayed against a
different one, a different base version, or a different request.

Both routes fold the caller-supplied `human_decision_ref` into the bound
decision's `decision_id`; `_gate_knowledge_write` refuses to proceed if
that reference is missing or too short to be real, closing the same gap
`store_reviewed_dossier` (#938) and `bind_oidc_identity` (#935) closed:
a `policy_client` present with no real decision reference behind it does
not silently pass.

## A caught bypass, before it shipped

`apply_edit_request` is not called from one place. `knowledge_edit_variants.
apply_selected_variant` calls it directly, twice — once on the "already
applied" replay branch, once on the main apply branch — and that function
is itself reachable through a third, separately composed route
(`apply_selected_edit_variant` in `knowledge_edit_variant_api.py`, mounted
through `cockpit_composed.py`, not through `cockpit_api.py`). Grepping for
all direct callers of `apply_edit_request` found this before any test did;
wiring only the direct `apply_intelligent_edit` route would have left a
trivial, uninstrumented path to apply the same edit without a decision
point. All three call sites — the direct route, and both calls inside
`apply_selected_variant` — now thread the same `policy_client`.

## What is still not verified

`publish_knowledge`'s gate binds the publication claim to its exact
content; it does not verify `created_by` or `actor_kind` on the candidate
path. A holder of the editor key can still attribute an unreviewed
publication to anyone. That is outside what this repair was scoped to
close — the inventory finding was about the reviewed claim specifically,
not about caller identity.

## Where the enforcement actually lives

`cockpit_api.create_app` now resolves its own `policy_client` and
`policy_enforcement` from the same environment variables
`cockpit_shell.py` reads (`MVP_POLICY_API_URL`, `MVP_POLICY_API_KEY`,
`MVP_POLICY_ENFORCEMENT`), rather than reusing `cockpit_shell.py`'s
resolution. `cockpit_api.create_app` is wrapped by `cockpit_shell.
create_cockpit_app`, which is wrapped again by `cockpit_composed.
create_composed_cockpit_app` — all three share one `FastAPI` app instance
and its `app.state`, so `cockpit_shell`'s resolution runs after
`cockpit_api`'s and overwrites it harmlessly whenever the composition
chain is used in full. The duplication is deliberate: refactoring
`cockpit_shell.py`'s already-tested resolution to be shared risked
touching a lower-level module this task did not need to change, for a
gate that is only reachable through the full composition chain in
practice. `install_knowledge_edit_variant_routes` reads `app.state`
defensively (`getattr(..., "required")`) rather than assuming those
attributes exist, because that installer is also unit-tested against a
bare app that never goes through `cockpit_api.create_app` at all.

## Boundary

Boundary profile applies: `bounded_implementation_change`.

Protected paths touched: no.
Runtime impact: publishing Knowledge as already reviewed, and applying a
decided edit-request replacement (through either the direct route or the
variant-selection route), now fail closed on every production path when
no decision point is configured. Publishing an unreviewed Knowledge item,
and every read path, is unchanged. Existing callers that pass no
`policy_client` (all prior test modules exercising these functions
directly) are unchanged.
Authority impact: this is the point. Claiming a Knowledge publication as
reviewed, and applying a decided edit to Knowledge content, now route
through the governance check, each bound to the exact content being
committed.
Schema/test/CI impact: no schema change; one test module added; one
existing test module's fixture updated to state explicitly that it
disables enforcement because it is out of this gate's scope, not because
the gate is wrong.
External action: none.
Memory behavior: none.

## Verification

```text
implementation/tests   1303 passed, 380 skipped
tests/                  595 passed
```

The eleven DB-dependent tests in `test_knowledge_edit_and_publish_gate.py`
skip locally (no reachable PostgreSQL/pgvector in this execution
environment, same as #938); the three no-DB isolation tests exercising
`_gate_knowledge_write` directly ran and passed locally, and were also
run against a deliberately broken `publish_knowledge` gate condition
(`if False:` in place of the real check) to confirm sensitivity before
being restored — they did not move, because they test the shared helper
directly rather than the call site, which is the known, pre-existing
limitation of that check (see Local distinctions). GitHub CI runs the full
pgvector integration lane and is the authoritative execution check for the
eleven DB-dependent tests.

## Local distinctions

```text
conditional gate on a specific claim   != unconditional gate on the write
missing status guard                    != missing decision point
digest binds proposed content as a unit != digest verifies the proposal is sound
AST-reachable call                      != a live call on every branch
```

The last line names a real, pre-existing limit in
`test_a_coverage_claim_is_backed_by_a_real_call`: it verifies
`enforce_consequential` is statically reachable from a claimed-gated
function, not that the specific branch reaching it is live at runtime.
Wrapping a real gate call in `if False:` still passes that test, because
dead code is still reachable in AST terms. This was confirmed by hand
during this change and left unfixed — it is a gap in the coverage-claim
test's method, not in this gate, and is out of this task's scope.
