"""Make the consequential-mutation surface enumerable instead of assumed.

`CLAUDE.md` states the invariant in the present tense:

```text
A consequential effect still routes through the governance check (the
chokepoint). No module or implementation path bypasses it.
```

Nothing verified that. `policy_gate.enforce_consequential` was imported by two
modules, so an import-graph audit reported the module as reachable and healthy,
while the parameter that triggers the call (`policy_client`) had no non-test
caller and `HttpPolicyClient` was never instantiated outside tests. Each mutation
entry point defends itself with its own local checks — signed previews,
confirmation phrases, optimistic concurrency, idempotency keys, admission state
machines — and no two of them share a guard.

Local defence is not the problem. The problem is that a new entry point can be
added tomorrow inheriting none of it, with no check noticing.

## Where the review stands

Sixty of the eighty-five entry points have been read individually; 25 have
not. The first batches were chosen because nothing in production reached them —
answerable without unwinding a call graph, and the cheapest end of the backlog
rather than the most urgent one. From `knowledge.py` onward every entry point is
live: each sits behind a route a key holder can call today.

Seven entry points are now recorded as `gate_required_not_wired` rather than
softened into `none`. `bind_oidc_identity` is where an external identity becomes
able to act as a governed principal. `store_reviewed_dossier` installs canonical
APU state on the strength of a `review_ref` that nothing validates. `revoke_grant`
lets one access manager lock another one out. `publish_knowledge` accepts
`review_status="reviewed"` as a caller assertion. `complete_edit_request` can
return a human-rejected request to `proposed`. `apply_edit_request` acts on that
status as though it were a decision. `act_working_information` supersedes the
acted version of a governed Information series and records no actor.

## The first write of a projection is not serialised

Recorded because all three `information_projection` entries share it, and
because the first version of those records named the row lock and
`expected_revision` as effective guards without qualification.

`_metadata_row(..., lock=True)` runs `SELECT ... FOR UPDATE` and, when no
projection-metadata row exists yet, returns a synthetic dictionary carrying
`revision: 0`. `FOR UPDATE` locks rows, not keys: a row that does not exist
cannot be locked. So two concurrent first mutations both read revision 0, both
pass the `expected_revision` check, and both compute `resulting_revision = 1`.

For `update_projection_metadata` that is a lost update — the second
`ON CONFLICT DO UPDATE` overwrites every field the first wrote. For the link
paths the metadata survives, but the event log gains two events both declaring
`0 -> 1`, describing a linear history that did not happen.

The pattern is used correctly everywhere else: eleven other modules raise a
not-found error when the locked row is missing. This is the one place where the
row is optional by design, and the optional case is where the token is invented.

A minimal repair, for the owner: carry the expected revision into the upsert's
conflict clause — `ON CONFLICT ... DO UPDATE SET ... WHERE
agency_information_projection_metadata.revision = <expected_revision>` — and
require `rowcount == 1`. On a genuine first write exactly one racer's INSERT
succeeds; the loser conflicts, its guarded UPDATE matches nothing, and it fails
as stale instead of overwriting.

## Where the actor label is strongest, and what that still is not

Six modules record an actor nobody verified. `entity_relations` is where this
codebase pushes hardest against that, and reading it clarifies the whole axis.

```text
agency_classification   _validate_actor, defaulted        a caller omits it and passes
agency_information      actor_kind literal at the route   body-proof, module still trusts it
execution_results       trigger: claim needs a human      a second Python caller cannot pass
entity_relations        CHECK: only a proposal may be     no row can say Hermes canonized
                        attributed to a non-human
```

The last is the strongest form available, and it is worth being exact about
what it buys. None of these verifies that the label is true: a caller
presenting `human` passes every one of them. What the constraint guarantees is
that the audit trail can never hold the contradiction — no stored row can say
Hermes canonized a relation.

That is internal consistency of the record. It is real, it is rare, and it is
not the same as knowing who acted. `canonize_relation`'s docstring says "Hermes
cannot reach this"; what holds is "no record can say Hermes reached this".

## The net was under-counting, and it under-counted the worst cases

The tenth batch found this by accident, reading `work_issues.py`:
`transition_issue` was not in this inventory at all. Nor were twelve others.

Discovery saw a public function only if its name began with one of five verbs
or its own body contained a literal SQL write. Neither signal sees a public
function that delegates its write to a private helper in the same module —
which is a normal way to write this codebase, and is how the following are
written:

```text
work_issues.transition_issue          the only general status move
work_issues.close_issue               the only path to done
entity_relations.canonize_relation    canonization, by name
entity_relations.reject_relation      entity_relations.retire_relation
source_intake.exclude_source          restore_source, link_project,
                                      unlink_project, update_metadata,
                                      suggest_projects
hermes_runtime_return.record_external_runtime_return
apu_cross_family.create_decision_request
```

Thirteen entry points, and the miss was not random: it fell on functions whose
names are verbs of consequence. A third signal now catches them — a public
function that calls a private same-module helper whose body writes.

Worth being precise about how this instrument failed, because it is the same
failure it exists to find. Two tests guarded discovery: one asserts every
discovered entry point is declared, the other that discovery is not vacuous.
Both passed throughout. Neither could fail for something the net never saw.
**The control verified its output and never its coverage.**

## Attribution is a separate axis from authorization

Four modules now show the same split, and it is not the gate's to fix. The
authorization is verified — a key comparison, a principal lookup, a dependency
that cannot be reached from a request body. The attribution is not.

```text
agency_classification     X-Pantheon-Human-Actor   asserted, persisted as updated_by
agency_information        X-Pantheon-Actor         asserted, required, then discarded
knowledge                 created_by               a body field, persisted verbatim
knowledge_edit_variants   X-Pantheon-Human-Actor   asserted, persisted; kind is a literal
decision_requests         X-Pantheon-Human-Actor   asserted — and so is its assurance level
information_projection    X-Pantheon-Actor         asserted, persisted into the event log
hermes_execution          X-Pantheon-Human-Actor   asserted — but the key decides the side
```

The last line is the one exception found so far, and it is an exception of
authorization rather than attribution. Admission and revocation take the editor
key with a human actor; launch reservation, runtime start and result return take
the Hermes key with a Hermes actor. The name in the header is still unverified,
but no key can play both sides: Hermes cannot admit its own handoff, and a human
editor cannot forge the runtime callback.

The last line is the one that settles the question. `decision_requests` is the
only module that models the distinction: `identity_assurance` is mandatory and
takes `declared` or `authenticated`, and `authenticated` requires an
`authenticated_principal` with `user_id` and `identity_provider`. Both arrive in
the request body. So the party asserting the name also chooses the assurance
level describing that assertion, and supplies the principal said to back it.
Nothing authenticates any of it.

The concept the other four modules lack already exists here. What it lacks is a
source of truth: an assurance level is only worth what produced it.

Two are worth reading twice. All four Information routes refuse a request
without `X-Pantheon-Actor` and none of them uses the value: the parameter is
named `_actor`, and `agency_information_cards` has no actor column to put it in.
The header is enforced as though it mattered and stored nowhere.

And in `knowledge_edit_variants` the review event log — the record of who chose,
who refused and who applied — takes its `actor` from that header and its
`actor_kind` from a literal written at each of its four `_insert_event` sites,
one `system` and three `human`. Both halves of the attribution are decided by the
code path rather than observed from the caller.

## What keeps being wrong

Four of those six were first recorded as `none`, and each correction had the same
shape: a guard was believed on the strength of what it is called rather than what
it composes to.

```text
review_ref                     reads as a reference to a review
"cannot revoke access.manage"  reads as protection of the administrator
_validate_actor                reads as a refusal of Hermes
status == "proposed"           reads as a decision already taken
```

None of the four was a slip. Each was a verdict written after reading the
function, and each was wrong one call away from where the reading stopped. The
question that finds them is not "what does this check" but "who controls each
input" — asked of every link, including the ones that look settled.

## How the surface is discovered, and why not by name

A first version of this test recognised entry points by five verb prefixes —
`apply`, `admit`, `promote`, `approve`, `commit`. A review pointed out that the
docstring then claimed far more than the code delivered, and it was right: that
net caught **8** functions while **64** other public functions write to the
database directly. Widening the verb list is not the fix either — it drags in
`create_app` and `resolve_case_ref`, which mutate nothing.

Discovery is therefore the union of two signals, neither sufficient alone:

```text
structural  a public function whose body contains an INSERT / UPDATE / DELETE
            statement — catches writers whatever they are called
verb        a public apply_/admit_/promote_/approve_/commit_ function — catches
            entry points that delegate their write and contain no SQL of their
            own, which the structural signal alone misses (two of the eight
            reviewed entries are exactly that)
```

This is a net, not a proof. It still cannot see a delegating entry point that is
named outside the verb list, and it does not follow the call graph. What it does
guarantee is that the surface it names is enumerated and cannot grow silently.

## What a declaration means

```text
gate = "enforce_consequential"    -> calls the Pantheon chokepoint
gate = "optional"                 -> chokepoint reachable but opt-in, default off
gate = "none"                     -> reviewed; module-local checks judged sufficient
gate = "gate_required_not_wired"  -> reviewed; the effect needs the chokepoint and
                                     does not reach it. A decision, not a defect
                                     list, and a debt that may not grow.
```

`none` is a conclusion, not an absence: it records that a human read the path and
judged its local chain sufficient. `unreviewed` is the absence. Keeping the two
apart is the whole point of this file — without the distinction, a path nobody
has looked at is indistinguishable from one that was cleared.

`local_guards` records what genuinely protects the path, so `"none"` is never
mistaken for `"unprotected"`. Entries carrying `_UNREVIEWED` are enumerated but
not yet individually read: their guard regime is *unknown*, which is recorded
honestly rather than assumed to be `"none"`. A test counts them, so the debt is
visible and shrinks deliberately.

## Two attribution mechanisms, and only one of them verifies

Reading the `agency_classification` cluster surfaced a repository-wide split that
no single entry owns.

```text
principal.principal_ref     35 sites   an authenticated principal context
X-Pantheon-Human-Actor      19 route dependencies across 8 modules
```

The second is a request header. `require_human_actor` is named like an
authentication check and composes to: read the header, require it non-empty.
Nothing ties the named human to a governed principal or to the party presenting
the bearer key — and the value is persisted into governed rows as `updated_by`.

So on those routes the *authorization* is verified (the bearer key) while the
*attribution* is asserted. The chokepoint would not repair that; binding the
actor to an authenticated identity would. It is recorded here because it is the
third instance in this file of the same failure shape, and the one with the
widest reach.

```text
import edge != call path
module reachable != gate invoked
local guard != central chokepoint
enumerated != reviewed
declared inventory != wired chokepoint
```

Adding an entry point without declaring it fails closed. Recording `_UNREVIEWED`
is a permitted, honest answer; recording nothing is not.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path

MVP = Path(__file__).resolve().parents[1] / "mvp_vertical"

# Verb prefixes that name an entry point which may delegate its write.
MUTATION_PREFIXES = frozenset({"apply", "admit", "promote", "approve", "commit"})

# A statement that changes durable state, found in the function's own body.
SQL_WRITE = re.compile(r"\b(INSERT\s+INTO|UPDATE\s+[\w.\"]+\s+SET|DELETE\s+FROM)\b", re.IGNORECASE)

# Enumerated by the net below, but not yet individually read. Its guard regime is
# unknown — not assumed absent.
_UNREVIEWED = {"gate": "unreviewed", "local_guards": None}

INVENTORY: dict[tuple[str, str], dict[str, object]] = {
    ("agency_change_candidate_review.py", "request_project_candidate_revision"): _UNREVIEWED,
    ("agency_change_candidates.py", "apply_project_candidate"): {
        "gate": "none",
        "local_guards": ("human actor", "status", "base revision staleness", "idempotency"),
        "reviewed": (
            "A reviewed candidate is applied to a project only from a declared human actor, against the base revision it was prepared on. Staleness is refused rather than merged."
        ),
    },
    ("agency_change_candidates.py", "create_project_candidate"): _UNREVIEWED,
    ("agency_change_candidates.py", "reject_project_candidate"): _UNREVIEWED,
    ("agency_claims.py", "record_claim"): _UNREVIEWED,
    ("agency_classification.py", "archive_category"): {
        "gate": "none",
        "local_guards": (
            "route rejects the Hermes bearer key outright, and 503s if the editor and Hermes keys are identical — the only verified refusal of Hermes on this path",
            "_validate_actor rejects an actor_kind outside human or system, but the label is caller-supplied and defaults to human, so it refuses nothing on a direct call",
            "expected_revision optimistic concurrency, StaleCategoryWrite on mismatch",
            "refuses an already archived Category",
        ),
        "reviewed": (
            "Classification, not a professional act: it approves nothing, admits no Evidence and reaches nothing external. The protection is route-borne, not module-borne: the API route is the sole production caller and rejects the Hermes bearer key, "
            "while _validate_actor only checks a label the caller supplies and which defaults to human. A first review of this entry called those two independent layers; they are not, and the correction matters because a second production caller would inherit none of the route's refusal. Attribution is the module's other weak point: see the docstring."
        ),
    },
    ("agency_classification.py", "assign_category"): {
        "gate": "none",
        "local_guards": (
            "route rejects the Hermes bearer key outright, and 503s if the editor and Hermes keys are identical — the only verified refusal of Hermes on this path",
            "_validate_actor rejects an actor_kind outside human or system, but the label is caller-supplied and defaults to human, so it refuses nothing on a direct call",
            "required assignment, category and entity identifiers",
            "entity_type checked against a controlled set",
        ),
        "reviewed": (
            "Classification, not a professional act: it approves nothing, admits no Evidence and reaches nothing external. The protection is route-borne, not module-borne: the API route is the sole production caller and rejects the Hermes bearer key, "
            "while _validate_actor only checks a label the caller supplies and which defaults to human. A first review of this entry called those two independent layers; they are not, and the correction matters because a second production caller would inherit none of the route's refusal. Attribution is the module's other weak point: see the docstring."
        ),
    },
    ("agency_classification.py", "create_category"): {
        "gate": "none",
        "local_guards": (
            "route rejects the Hermes bearer key outright, and 503s if the editor and Hermes keys are identical — the only verified refusal of Hermes on this path",
            "the sole production caller passes actor_kind as a literal, so a request body cannot set it",
            "_validate_actor rejects an actor_kind outside human or system, but the label is caller-supplied and defaults to human, so it refuses nothing on a direct call",
            "required category_id and title, non-negative sort_order",
        ),
        "reviewed": (
            "Classification, not a professional act: it approves nothing, admits no Evidence and reaches nothing external. The protection is route-borne, not module-borne: the API route is the sole production caller and rejects the Hermes bearer key, "
            "while _validate_actor only checks a label the caller supplies and which defaults to human. A first review of this entry called those two independent layers; they are not, and the correction matters because a second production caller would inherit none of the route's refusal. Attribution is the module's other weak point: see the docstring."
        ),
    },
    ("agency_classification.py", "retire_category_assignment"): {
        "gate": "none",
        "local_guards": (
            "route rejects the Hermes bearer key outright, and 503s if the editor and Hermes keys are identical — the only verified refusal of Hermes on this path",
            "_validate_actor rejects an actor_kind outside human or system, but the label is caller-supplied and defaults to human, so it refuses nothing on a direct call",
            "expected_revision optimistic concurrency, StaleCategoryAssignmentWrite on mismatch",
            "refuses an already retired CategoryAssignment",
        ),
        "reviewed": (
            "Classification, not a professional act: it approves nothing, admits no Evidence and reaches nothing external. The protection is route-borne, not module-borne: the API route is the sole production caller and rejects the Hermes bearer key, "
            "while _validate_actor only checks a label the caller supplies and which defaults to human. A first review of this entry called those two independent layers; they are not, and the correction matters because a second production caller would inherit none of the route's refusal. Attribution is the module's other weak point: see the docstring."
        ),
    },
    ("agency_classification.py", "update_category"): {
        "gate": "none",
        "local_guards": (
            "route rejects the Hermes bearer key outright, and 503s if the editor and Hermes keys are identical — the only verified refusal of Hermes on this path",
            "the sole production caller passes actor_kind as a literal",
            "_validate_actor rejects an actor_kind outside human or system, but the label is caller-supplied and defaults to human, so it refuses nothing on a direct call",
            "expected_revision optimistic concurrency, StaleCategoryWrite on mismatch",
            "refuses an empty change set",
        ),
        "reviewed": (
            "Classification, not a professional act: it approves nothing, admits no Evidence and reaches nothing external. The protection is route-borne, not module-borne: the API route is the sole production caller and rejects the Hermes bearer key, "
            "while _validate_actor only checks a label the caller supplies and which defaults to human. A first review of this entry called those two independent layers; they are not, and the correction matters because a second production caller would inherit none of the route's refusal. Attribution is the module's other weak point: see the docstring."
        ),
    },
    ("agency_data.py", "create_project"): _UNREVIEWED,
    ("agency_data.py", "update_project"): _UNREVIEWED,
    ("agency_information.py", "act_working_information"): {
        "gate": "gate_required_not_wired",
        "local_guards": ("actor_kind must be human, no default", "row lock", "working status only", "expected_revision", "supersede and install in one transaction"),
        "reviewed": (
            "This is the act. It supersedes the currently acted version of a "
            "governed Information series and installs a new one, in one "
            "transaction, and the acted row is what `card_scope` and "
            "`hermes_scoped_context` read. The module states its own gravity — "
            "'only a human may act an Information version' — and enforces it by "
            "comparing a string the caller passes. The route passes it correctly "
            "today, from a dependency rather than the body. Two things make it a "
            "gate requirement anyway: the effect is a change to canonical agency "
            "state, and nothing records who performed it. `acted_at` is written; "
            "the acting party is not, because the table has no actor column."
        ),
    },
    ("agency_information.py", "create_information"): {
        "gate": "none",
        "local_guards": ("actor_kind human or system, no default", "new rows must start draft or in_progress", "source ref/note validation", "handwritten allowlist, validated against the field registry"),
        "reviewed": (
            "Creates a draft, which approves nothing and supersedes nothing, and "
            "`actor_kind` carries no default, so a direct caller has to state its "
            "claim rather than inherit one. Corrected on review: this record said "
            "the field allowlist was derived from the schema rather than written "
            "out twice. Neither half was true. The set passed to `_schema_values` "
            "is seventeen names spelled out at the call site, duplicating the keys "
            "of the dict directly above it, and `_schema_values` only forwards "
            "whatever allowlist its caller hands it to `normalize_declared_fields`, "
            "which checks the field registry — not any declared view. A `create` "
            "view does exist and today matches the handwritten set exactly, minus "
            "`project_id`, which is a path parameter; nothing holds them in step. "
            "`update_working_information` next door does derive its allowlist, via "
            "`_editable_fields()` and the `edit` view, so the two paths differ in "
            "kind and only one of them was read correctly the first time."
        ),
    },
    ("agency_information.py", "derive_working_version"): {
        "gate": "none",
        "local_guards": ("row lock", "base must be the acted version", "source ref/note validation", "new row forced to draft"),
        "reviewed": (
            "Derives a new draft from the acted version; the status is a literal in "
            "the INSERT, so the caller cannot ask for anything else. One "
            "inconsistency worth naming rather than filing: `actor_kind` defaults "
            "to `human` here while the other three in this module require it. That "
            "is the shape corrected in the classification cluster — a default "
            "turning a claim into an inheritance — and it is the one entry point "
            "here where a future direct caller would pass the check by omission."
        ),
    },
    ("agency_information.py", "update_working_information"): {
        "gate": "none",
        "local_guards": ("hermes requires hermes_admitted, never passed by any route", "working status only", "expected_revision plus a rowcount check", "editable-field allowlist", "status restricted to working values"),
        "reviewed": (
            "Edits a working version only: an acted or superseded row is refused "
            "outright. Concurrency is checked twice — the locked read compares "
            "`expected_revision`, and the UPDATE carries the revision in its WHERE "
            "clause and asserts `rowcount == 1`, so a race that slips past the "
            "first check still cannot write. Hermes is refused unconditionally in "
            "production because `hermes_admitted` is a parameter no route passes."
        ),
    },
    ("apu_mapping_reviews.py", "append_mapping_review"): _UNREVIEWED,
    ("apu_owner.py", "apply_source_match"): {
        "gate": "none",
        "local_guards": ("prior authorization id", "exact command shape", "idempotency"),
        "reviewed": (
            "Applies a match that a prior authorization already decided; the command shape is checked exactly, so this records a decision rather than taking one."
        ),
    },
    ("apu_owner.py", "store_reviewed_dossier"): {
        "gate": "gate_required_not_wired",
        "local_guards": (
            "required project_id, review_ref, actor and idempotency_key",
            "payload digest compared on replay, refusing a reused key with different content",
            "normalization before write",
        ),
        "reviewed": (
            "Installs canonical APU state. First reviewed as none on the reasoning that "
            "review_ref carries a review that already happened, so the consequence gate "
            "belonged at that review rather than at its recording. That was wrong, and a "
            "review caught it: review_ref passes through _required only — a non-empty "
            "string. No lookup, foreign key, signature or any other check ties it to a "
            "completed governed review, and no table of such reviews exists to point at. "
            "The verdict therefore rested on an unverified caller assertion, which is the "
            "distinction this repository makes everywhere else: a provided reference is "
            "not a validated decision. Recorded as needing the chokepoint until either "
            "the prior review is verifiable or the write is routed through the gate."
        ),
    },
    ("apu_write_preparation.py", "append_authorization"): _UNREVIEWED,
    ("apu_write_preparation.py", "apply_authorized_write_command"): {
        "gate": "none",
        "local_guards": ("reviewed command chain", "stored index vs embedded effect", "owner and object revision freshness", "idempotency"),
        "reviewed": (
            "The strongest local chain in the inventory: the command must already be reviewed, its stored index must agree with the embedded effect, and both owner and object revision must still be fresh. Freshness is what makes replay safe here."
        ),
    },
    ("apu_write_preparation.py", "prepare_write_command"): _UNREVIEWED,
    ("contradictory_review_store.py", "persist_candidate"): _UNREVIEWED,
    ("decision_requests.py", "cancel_request"): {
        "gate": "none",
        "local_guards": ("rationale required", "row lock", "status must be pending", "expected_revision in the WHERE clause", "idempotency with payload digest", "event records the actor"),
        "reviewed": (
            "Withdraws a pending request, which decides nothing and is "
            "safety-decreasing only in the sense that a question goes unanswered. "
            "It insists on a rationale, refuses a request that is no longer "
            "pending, and records the cancelling actor and an event. The actor is "
            "the `X-Pantheon-Human-Actor` header value, as everywhere else."
        ),
    },
    ("decision_requests.py", "create_request"): {
        "gate": "none",
        "local_guards": ("status is a literal in the INSERT", "decision_type, priority and response_mode checked against frozensets", "blocking requires a WorkIssue", "evidence ref and digest required together", "projection validated against the decision_request contract", "idempotency with payload digest"),
        "reviewed": (
            "Creates a pending request: it asks for a decision, it does not take "
            "one. The INSERT writes `status` as a literal `'pending'`, so no "
            "caller can create a request that arrives already resolved — the same "
            "shape `create_variant_request` uses and `knowledge.create_edit_request` "
            "does not. The projection is validated against the `decision_request` "
            "contract on read."
        ),
    },
    ("decision_requests.py", "resolve_request"): {
        "gate": "gate_required_not_wired",
        "local_guards": ("row lock", "status must be pending", "expected_revision in the WHERE clause", "response validated against the request's mode and options", "unique decision identity", "idempotency with payload digest", "decision record and status transition in one transaction"),
        "reviewed": (
            "This is the decision. It writes an `agency_decision_records` row "
            "carrying `approve`, `refuse`, `request_revision` or "
            "`request_more_evidence` against a candidate digest, and the "
            "concurrency and idempotency around it are the most careful in the "
            "codebase. The finding is what it records about who decided. This "
            "module is the only one that models the distinction the rest of the "
            "review keeps missing: `identity_assurance` is mandatory and takes "
            "`declared` or `authenticated`, and `authenticated` requires an "
            "`authenticated_principal` carrying `user_id` and `identity_provider`. "
            "Both come from the request body. The route supplies `decided_by` from "
            "the `X-Pantheon-Human-Actor` header and forwards the rest with "
            "`**values`, so the party asserting the name also chooses the assurance "
            "level describing that assertion, and supplies the principal that is "
            "said to back it. Nothing authenticates it; the checks are that the "
            "dict has two non-empty keys. A governed decision record can therefore "
            "read `identity_assurance: authenticated` on a decision nothing "
            "authenticated. The contract validation on the projection constrains "
            "the value, not its truth."
        ),
    },
    ("document_revision_discussion.py", "create_comment"): _UNREVIEWED,
    ("entity_relations.py", "propose_relation"): _UNREVIEWED,
    ("execution_results.py", "append_review_disposition"): {
        "gate": "none",
        "local_guards": ("disposition vocabulary", "result row locked FOR UPDATE across checks and replay", "result_kind must match the disposition family", "claim-bearing dispositions require reviewer_kind human", "a database trigger enforces the same", "idempotency with payload digest"),
        "reviewed": (
            "The first guard in this review enforced below Python. "
            "`accepted_for_claim` and `selected_for_change_candidate` are refused "
            "for a non-human reviewer by this function *and* by "
            "`validate_execution_result_review_disposition`, a trigger on the "
            "table. That answers the weakness recorded against "
            "`agency_classification._validate_actor`, which was not a second "
            "layer because a direct caller inherited its default: a trigger is a "
            "second layer, because a second Python caller cannot route around it. "
            "The route passes `reviewer_kind=\"human\"` as a literal behind the "
            "editor key. The immutable result row is locked before the checks and "
            "kept locked through the replay lookup, so a replay cannot bypass the "
            "semantic checks for its family."
        ),
    },
    ("execution_results.py", "store_execution_result"): {
        "gate": "none",
        "local_guards": ("Hermes bearer key on the route", "authority block must equal the module constant exactly", "producer, results and refs required", "idempotency with payload digest"),
        "reviewed": (
            "Stores a returned execution result as a candidate. The record is "
            "refused unless its `authority` block equals the module's own "
            "constant, so a runtime cannot return a result that describes its own "
            "authority differently from the one the store recognises — the "
            "boundary is compared, not read from the payload."
        ),
    },
    ("hermes_execution.py", "admit_handoff"): {
        "gate": "none",
        "local_guards": ("human actor", "read_only effect only", "Task Contract and Context Pack identity", "TTL bounds", "idempotency"),
        "reviewed": (
            "Admits an external execution handoff bounded to a read_only effect, tied to a Task Contract and Context Pack identity and a TTL. Admission of a read_only effect is not authorization of a consequential one."
        ),
    },
    ("hermes_execution.py", "record_external_runtime_start"): {
        "gate": "none",
        "local_guards": ("Hermes key and Hermes actor on the route", "admission locked", "state must be admitted or launch_reserved", "exact launch reservation match", "work-issue version pinned to the admitted or reserved version", "run linkage asserts rowcount == 1", "idempotent on the same run_id"),
        "reviewed": (
            "Records that an external runtime started against an admission. It "
            "is reached with a different key from admission: the route takes "
            "`require_hermes_key` and `require_hermes_actor`, while admission and "
            "revocation take the editor key and a human actor. Corrected on "
            "review: that separation is a configuration property, not an enforced "
            "one. Both dependencies compare the bearer against their own key and "
            "nothing else, and `create_app` accepts an editor key equal to the "
            "Hermes key, so one credential can admit a handoff and record its "
            "runtime start. The `editor_match and hermes_match` refusal exists "
            "three times in this codebase — `agency_data_api`, "
            "`agency_classification_api`, `cockpit_shell` — and covers none of the "
            "execution routes, which is where the doctrine needs it most. The "
            "regime stays `none`: what collapses is segregation of duties, not the "
            "read_only bound on the effect, and the collapsed holder is the editor "
            "key holder who could already admit. The repair is one place — refuse "
            "equal keys when the app is constructed. "
            "The callback's `expected_issue_version` must equal the version the "
            "admission or reservation pinned. Worth quoting: the response carries "
            "its own non-equivalences as data — `runtime start recorded != "
            "Evidence`, `launch reservation != dispatch`, `running != task "
            "success`. The code states what it does not mean."
        ),
    },
    ("hermes_execution.py", "revoke_admission"): {
        "gate": "none",
        "local_guards": ("editor key and human actor on the route", "human actor and reason required", "admission locked", "state must be admitted", "idempotency checked across admission, actor and reason"),
        "reviewed": (
            "Withdraws an admission, which is safety-increasing, and records the "
            "reason as an event rather than mutating the admission row. The "
            "replay check compares admission, actor and reason together, so one "
            "idempotency key cannot carry a different revocation."
        ),
    },
    ("hermes_handoff_store.py", "submit_handoff"): {
        "gate": "none",
        "local_guards": ("human actor required", "preview must carry execution_authorized false", "requested_effect must be read_only", "immutable basis assembled and stored", "owner reads inside the write transaction", "idempotency with request digest"),
        "reviewed": (
            "Submits a handoff request. Two refusals are structural rather than "
            "advisory: the preview must say `execution_authorized: false`, and the "
            "effect must be `read_only`. Owner reads run inside the same explicit "
            "transaction as the write, which the source comment explains. On "
            "`preview_digest` the protection is route-borne, not module-borne, "
            "and this record first overstated that. `submit_handoff` does not "
            "recompute the digest from the preview it is handed, so a direct "
            "Python caller could fabricate one — but the sole production caller "
            "rebuilds the preview server-side with `prepare()`, and "
            "`hermes_handoff_preview.build_preview` sets "
            "`preview[\"preview_digest\"] = _digest(preview)` over that "
            "server-built content. The client's `expected_preview_digest` is only "
            "compared, to reject a stale scope with 409. So the chain every later "
            "stage relies on — the immutable basis at admission, the re-derivation "
            "in `get_execution_envelope` — is anchored to a computed value on the "
            "one path that exists today, and to an argument if a second caller is "
            "ever added."
        ),
    },
    ("hermes_launch_context.py", "reserve_launch"): {
        "gate": "none",
        "local_guards": ("Hermes key and actor on the route", "REPEATABLE READ isolation", "admission locked FOR UPDATE", "one reservation per admission", "idempotency checked across admission and actor"),
        "reviewed": (
            "Reserves exactly one launch against an admission and freezes its "
            "bootstrap context. It raises the transaction isolation to REPEATABLE "
            "READ and locks the admission, so two runtimes cannot both reserve. "
            "The docstring names the thing a caller would otherwise assume: a "
            "replay of the same idempotency key returns the same immutable "
            "reservation and is not permission to submit Hermes again."
        ),
    },
    ("hermes_result_candidate.py", "create_result_candidate"): {
        "gate": "none",
        "local_guards": ("Hermes key and actor on the route", "candidate payload normalized", "at least one trace_ref required", "summary bounded", "result digest over the whole material", "idempotency"),
        "reviewed": (
            "Persists what the runtime returned as a candidate. Nothing here "
            "admits Evidence, validates Knowledge or authorizes a task; the "
            "requirement of at least one `trace_ref` means a candidate cannot "
            "arrive with nothing to check it against."
        ),
    },
    ("human_access.py", "bind_oidc_identity"): {
        "gate": "gate_required_not_wired",
        "local_guards": ("refuses a disabled principal", "required issuer, subject and bound_by", "BindingConflict when the identity is bound to another principal", "idempotent within the same principal"),
        "reviewed": "The moment an external identity becomes able to act as a governed principal. The local chain is the strongest in this module and still not the same thing as the governance check: this is an authorization boundary, not a bookkeeping write. Reviewed as needing the chokepoint; nothing routes it there today.",
    },
    ("human_access.py", "create_principal"): {
        "gate": "none",
        "local_guards": ("required principal_ref", "recorded created_by actor", "idempotent ON CONFLICT insert"),
        "reviewed": "Creates a governed identity; it authorizes nothing on its own — grant_access does. The actor who created it is recorded. No runtime caller at review time.",
    },
    ("human_access.py", "disable_principal"): {
        "gate": "none",
        "local_guards": ("existence check", "idempotent when already disabled"),
        "reviewed": "Withdraws the ability to act, so the direction is safety-increasing and the local chain is thin by design. Recorded as reviewed with one finding: unlike create_principal it records no actor, so a disabling leaves no trace of who did it.",
    },
    ("human_access.py", "grant_access"): {
        "gate": "none",
        "local_guards": (
            "route requires an authenticated principal holding project.access.manage",
            "granted_by is taken from the authenticated session, never from the request body",
            "route refuses to delegate project.access.manage, so a grant cannot escalate",
            "a document grant requires the target to already hold active project.read",
            "refuses a disabled principal",
            "resource_type and action checked against controlled vocabularies",
            "project existence and document-belongs-to-project checked",
            "idempotent on an identical active grant",
        ),
        "reviewed": (
            "An authorization boundary, and the reflex after the store_reviewed_dossier "
            "correction is to escalate it too. The distinguishing fact is that the actor "
            "here is verified rather than asserted: granted_by comes from the "
            "authenticated session and the caller must already hold project.access.manage, "
            "checked against the database. store_reviewed_dossier failed on exactly the "
            "opposite — a review_ref nothing verifies. The route also caps escalation by "
            "refusing to delegate the manage right at all, and the codebase names the "
            "effect technical_project_access_granted, distinguishing it from a "
            "professional one. Cleared on the chain, not on the category."
        ),
    },
    ("human_access.py", "revoke_grant"): {
        "gate": "gate_required_not_wired",
        "local_guards": (
            "route requires an authenticated principal holding project.access.manage",
            "grant must belong to the named project, AccessDenied otherwise",
            "route refuses to revoke a grant whose own action is project.access.manage",
            "idempotent when already revoked",
        ),
        "reviewed": (
            "First reviewed as none, on the claim that the one escalation it could enable — "
            "stripping a project administrator — was refused by the route outright. A review "
            "caught that this is false, and the guard list said so too. "
            "require_project_access_manager checks project.read first and project.access.manage "
            "second, while the route refuses only a grant whose own action is "
            "project.access.manage. A manager can therefore revoke another manager's paired "
            "project.read grant: the victim keeps the manage row and fails every management "
            "endpoint. project.read is remotely grantable and revocation carries no "
            "REMOTE_MANAGEABLE_ACTIONS restriction at all, so the path needs no special access. "
            "An administrator lockout reachable by an ordinary manager is consequential, and "
            "nothing routes this through the governance check. The durable remedy is a code "
            "fix — protect a manager's paired read grant — which is a behavioural change and "
            "not this record's to make."
        ),
    },
    ("human_access.py", "revoke_oidc_binding"): {
        "gate": "none",
        "local_guards": ("required binding_id", "raises on unknown binding", "idempotent when already revoked"),
        "reviewed": "Withdraws an ability, so it is safety-increasing. Same finding as disable_principal: no actor is recorded on the revocation.",
    },
    ("information_projection.py", "add_document_link"): {
        "gate": "none",
        "local_guards": ("actor_kind human or system, no default", "Information and Document existence checked", "link role vocabulary", "row lock once the metadata row exists", "expected_revision, unserialised on the first write", "idempotency with payload digest", "event derived from the write's own result"),
        "reviewed": (
            "Links a Document to an Information card: metadata about what backs a "
            "card, not a change to what the card says. Both endpoints are checked "
            "to exist before the write. `observed_version` and `observed_digest` "
            "are caller-supplied and unverified against the Document, which the "
            "names say plainly — they record what the linker saw, not a validated "
            "fact, and this review has recorded the opposite naming twice. "
            "Notable in the other direction: the upsert returns `(xmax = 0)` and "
            "the event type is chosen from that, so `document_link_added` versus "
            "`document_link_updated` reflects what the statement did rather than "
            "what a preceding SELECT predicted. The comment says a prior version "
            "got this wrong and left the history describing a creation that never "
            "happened. That is a record derived from an effect instead of "
            "asserted beside it. Corrected on review: see the first-write race "
            "recorded in this module's docstring section; the row lock and "
            "`expected_revision` above hold only once the metadata row exists."
        ),
    },
    ("information_projection.py", "remove_document_link"): {
        "gate": "none",
        "local_guards": ("actor_kind human or system, no default", "row lock once the metadata row exists", "expected_revision, unserialised on the first write", "rowcount == 1 or the link did not exist", "idempotency with payload digest"),
        "reviewed": (
            "Unlinks a Document from an Information card, withdrawing a "
            "projection rather than changing governed content. The DELETE asserts "
            "`rowcount == 1`, so removing a link that was not there is an error "
            "rather than a silent success — the event log cannot record a removal "
            "that removed nothing. Corrected on review: the row lock and "
            "`expected_revision` hold only once the metadata row exists — see the "
            "first-write race in this module's docstring section."
        ),
    },
    ("information_projection.py", "update_projection_metadata"): {
        "gate": "none",
        "local_guards": ("actor_kind human or system, no default", "media-type vocabulary", "contact refs resolved against their tables", "row lock once the metadata row exists", "expected_revision, unserialised on the first write", "idempotency with payload digest"),
        "reviewed": (
            "Edits projection metadata — dates, media types, contact references. "
            "`projection != persistence` and `projection != governed identity` "
            "both apply: none of this changes what the Information says or who "
            "may act on it. Contact references are resolved against their tables "
            "rather than stored as free strings. Corrected on review: this is the "
            "path where the first-write race recorded below costs a lost update, "
            "not just a false history line."
        ),
    },
    ("knowledge.py", "apply_edit_request"): {
        "gate": "gate_required_not_wired",
        "local_guards": ("request status", "re-read under lock", "version and selection digest", "single transaction with audit", "idempotency"),
        "reviewed": (
            "Corrected. This entry read `none` on the reasoning that the request "
            "status already carried the decision. Reading the two functions that "
            "write that status shows nothing has to decide anything for it to say "
            "`proposed`: `create_edit_request` accepts `replacement_markdown` from "
            "its caller and sets `proposed` on the spot, and `complete_edit_request` "
            "sets `proposed` with no status guard. The transactional audit and the "
            "concurrency checks are real and unchanged; what is not real is the "
            "decision they are recorded against. This is the point where the "
            "Knowledge Markdown changes, so it is where the chokepoint belongs."
        ),
    },
    ("knowledge.py", "complete_edit_request"): {
        "gate": "gate_required_not_wired",
        "local_guards": ("non-empty replacement", "Hermes bearer key on the route", "version comparison against base_version"),
        "reviewed": (
            "Reads as Hermes filling in the proposal it was queued for. It takes no "
            "actor, no idempotency key, writes no event, and guards no status: it "
            "sets `replacement_markdown` and a status on whatever request_id it is "
            "given. `knowledge_edit_variants.reject_request` moves a request to "
            "`rejected` and records a human rejection event; that rejection does not "
            "revise the Knowledge item, so the version still equals base_version, so "
            "this function returns the request to `proposed` — and the editor-keyed "
            "apply route then applies it. The party whose proposal was rejected can "
            "un-reject it, leaving no trace beside the rejection event. An applied "
            "request is safe here only by accident of the same version comparison."
        ),
    },
    ("knowledge.py", "create_edit_request"): {
        "gate": "none",
        "local_guards": ("instruction kind and non-empty instruction", "row lock", "base_version equality", "selected text matched against the live snapshot", "idempotency with payload digest"),
        "reviewed": (
            "Writes a request row, which is a candidate and not itself consequential, "
            "and its concurrency guards are unusually tight — the selection range and "
            "the selected text are both checked against the locked snapshot. The "
            "finding is what it can set that row to: passing `replacement_markdown` "
            "on creation skips `queued_for_hermes` and writes `proposed` directly, so "
            "the editor key alone produces the text, the status that reads as a "
            "decision, and then the apply. `requested_by` is an unverified body "
            "string. Recorded at the apply, which is where the Knowledge changes, "
            "rather than duplicated here."
        ),
    },
    ("knowledge.py", "publish_knowledge"): {
        "gate": "gate_required_not_wired",
        "local_guards": ("non-empty knowledge_id, title and Markdown", "family membership", "expected_version must be 0", "idempotency"),
        "reviewed": (
            "The route guard is a bearer-token comparison, and the body is passed "
            "through with `**body.model_dump()`. Three of those fields are claims "
            "about people: `created_by`, `actor_kind` — which accepts `hermes` — and "
            "`review_status`, which accepts `reviewed`. The function checks each "
            "against a set of permitted strings and nothing else. A holder of the "
            "editor key can therefore publish a Knowledge item that already reads as "
            "professionally reviewed, attributed to anyone. `schema conformance != "
            "professional approval` is the invariant, and membership in "
            "REVIEW_STATUSES is exactly the conformance being mistaken for it."
        ),
    },
    ("knowledge.py", "revise_knowledge"): {
        "gate": "none",
        "local_guards": ("expected_version optimistic concurrency", "actor_kind membership", "idempotency with payload digest"),
        "reviewed": (
            "The revision primitive, not an entry point: its own route, "
            "`PUT /knowledge/{knowledge_id}`, is retired and raises 410. It holds as "
            "`none` only because both live callers are themselves recorded — "
            "`knowledge_update.apply_knowledge_update`, behind the signed preview and "
            "confirmation phrase, and `apply_edit_request`, recorded above as needing "
            "the gate. Worth naming plainly: the 410 says direct revision is retired "
            "in favour of the signed routes, and the edit-request pair reaches this "
            "same function on the same editor key with no signature, no confirmation "
            "phrase and no project scope. The retirement is a property of the route, "
            "not of the module."
        ),
    },
    ("knowledge_edit_variants.py", "apply_selected_variant"): {
        "gate": "none",
        "local_guards": ("status re-checked under lock", "selection unchanged under lock", "variant ownership", "audit inside the apply transaction", "idempotent replay when already applied"),
        "reviewed": (
            "Reasoning rewritten, regime unchanged. It said the request had "
            "already selected the variant, and selection is genuinely recorded "
            "here — `selected_by`, an event, an idempotency key. What the "
            "selection does not survive is a rejection: `reject_request` does not "
            "clear `selected_variant_id`, and `knowledge.complete_edit_request` "
            "returns a rejected request to `proposed`, after which this function "
            "finds a `proposed` status and an intact selection and applies the "
            "variant a human refused. The gate stays recorded at "
            "`knowledge.apply_edit_request`, which this delegates to and which is "
            "where the Knowledge changes; wiring it there covers this path, so "
            "recording it twice would overstate what has to be wired. One caveat: "
            "the `replacement_markdown` write here commits in its own transaction "
            "before the delegation, so it would survive a refusal downstream."
        ),
    },
    ("knowledge_edit_variants.py", "create_variant_request"): {
        "gate": "none",
        "local_guards": ("status and replacement_markdown are literals in the INSERT", "locked snapshot with base_version equality", "selection range and text matched against the snapshot", "idempotency with payload digest"),
        "reviewed": (
            "The same table as `knowledge.create_edit_request`, and the "
            "instructive contrast with it: here the INSERT writes "
            "`replacement_markdown` as a literal NULL and the status as a literal "
            "`queued_for_hermes`, so this creation path cannot manufacture a "
            "`proposed` request. The shortcut recorded against the other path is "
            "not a shape the codebase lacks a fix for; it is one this module "
            "already closes."
        ),
    },
    ("knowledge_edit_variants.py", "project_execution_result_variant"): {
        "gate": "none",
        "local_guards": ("status must be queued_for_hermes or proposed", "scope currency re-checked under lock", "candidate payload validated against the contract", "conflict persisted after the rollback", "idempotency with projection digest"),
        "reviewed": (
            "Projects a Hermes candidate and declares its authority as data: "
            "CANDIDATE_AUTHORITY sets selects_variant, applies_edit, "
            "validates_knowledge, admits_evidence, promotes_memory and "
            "authorizes_task all False. It refuses any status outside "
            "`{queued_for_hermes, proposed}` — the guard `complete_edit_request` "
            "lacks — so a rejected request cannot receive a projection. The "
            "staleness conflict is written in its own transaction after the "
            "attempt unwinds, so discovering it does not depend on the attempt "
            "committing."
        ),
    },
    ("knowledge_edit_variants.py", "reject_request"): {
        "gate": "none",
        "local_guards": ("status must be queued_for_hermes or proposed", "row lock", "non-empty reason", "idempotency with payload digest", "event records the refusal"),
        "reviewed": (
            "Refuses an edit, which is safety-increasing, and records why. The "
            "finding is not in this function but in what happens after it: the "
            "rejection it writes is reversible by `complete_edit_request`, and "
            "this function clears no selection, so a rejected request can arrive "
            "back at `proposed` with its selection intact. Recorded here so the "
            "reversal is findable from the function that is supposed to be "
            "terminal."
        ),
    },
    ("knowledge_edit_variants.py", "select_variant"): {
        "gate": "none",
        "local_guards": ("status must be proposed", "row lock", "variant ownership", "idempotency with payload digest", "event records the selection"),
        "reviewed": (
            "Records the human choice between two candidates; it mutates no "
            "Knowledge and the event says so explicitly "
            "(`knowledge_mutated: False`). Both halves of the attribution it "
            "writes are unverified, though: `actor` is the "
            "`X-Pantheon-Human-Actor` header value, and `actor_kind` is a literal "
            "at the call site — as it is at every site in this module. Corrected "
            "on review: that was first written as six event writes, five `human` "
            "and one `system`, which counted `actor_kind=` matches rather than "
            "reading what each call was to. There are four `_insert_event` sites, "
            "one `system` for the projection and three `human` for selection, "
            "rejection and application; the remaining two literals are passed into "
            "`knowledge.apply_edit_request`. Six literals, four of them in the "
            "audit log. The point is unchanged and the count was not checked: the "
            "column records the kind the code path intends, never the kind of the "
            "caller observed."
        ),
    },
    ("knowledge_update.py", "apply_knowledge_update"): {
        "gate": "optional",
        "local_guards": ("signed preview", "exact confirmation phrase", "expected_version and base digest", "idempotency"),
        "reviewed": (
            "The one path with the chokepoint reachable. Its local chain is a signed preview, an exact confirmation phrase, optimistic concurrency and idempotency; the gate is opt-in and off by default, which is why the regime is optional rather than covered."
        ),
    },
    ("project_document_admission.py", "admit_source_as_revision"): {
        "gate": "none",
        "local_guards": ("explicit target document", "exact capture identity", "idempotency"),
        "reviewed": (
            "Admits a captured source as a revision of an explicitly named target document, keyed on the exact capture identity. Admission is not a currentness or authority claim, which are owned elsewhere."
        ),
    },
    ("project_document_currentness.py", "record_version_event"): {
        "gate": "none",
        "local_guards": ("refuses hermes actors outright", "refuses any consequential authority status", "refuses a system actor setting anything authoritative", "controlled vocabulary on event type, status, effect class and authority", "required actor and idempotency_key"),
        "reviewed": "The clearest case in the codebase of a path that enforces the doctrine without calling the chokepoint: it raises GovernanceGateRequired rather than deciding, so a consequential authority transition cannot pass through it at all.",
    },
    ("project_documents.py", "create_document"): {
        "gate": "none",
        "local_guards": ("_validate_actor refuses hermes with GovernanceGateRequired", "required parent project, type, title and idempotency_key", "payload digest with idempotent replay"),
        "reviewed": "Creates a document shell; authority and currentness are owned elsewhere and refused here. No runtime caller at review time.",
    },
    ("project_documents.py", "link_revision"): _UNREVIEWED,
    ("project_documents.py", "record_issuer_reference"): {
        "gate": "none",
        "local_guards": ("_validate_actor refuses hermes with GovernanceGateRequired", "basis_kind checked against a controlled vocabulary", "opaque reference validation", "revision existence check", "payload digest with idempotent replay"),
        "reviewed": "Records an observation about a revision, not an authority claim about it.",
    },
    ("source_intake.py", "create_source"): _UNREVIEWED,
    ("source_intake.py", "relate_contained_source"): _UNREVIEWED,
    ("storage_retention.py", "retain_document_version"): _UNREVIEWED,
    ("store.py", "ingest"): _UNREVIEWED,
    ("apu_cross_family.py", "create_decision_request"): _UNREVIEWED,
    ("entity_relations.py", "canonize_relation"): {
        "gate": "none",
        "local_guards": ("separate route with the editor key and a human actor", "actor_kind literal at the route", "_actor refuses any kind but human, no default", "relation locked", "status must be proposed", "expected_revision", "idempotency with payload digest", "a CHECK constraint refuses a non-human actor_kind on any event that is not a proposal"),
        "reviewed": (
            "The act the doctrine names, and the most layered guard in this "
            "codebase. The route is separate from the Hermes proposal route and "
            "passes `actor_kind=\"human\"` as a literal; `_actor(..., "
            "proposing=False)` accepts only `human` and has no default; and "
            "`agency_entity_relation_events_hermes_proposes_only` — "
            "`CHECK (actor_kind = 'human' OR event_type = 'relation_proposed')` — "
            "refuses to store any other event kind attributed to Hermes. "
            "Worth being exact about what that buys, because the docstring says "
            "'Hermes cannot reach this' and that is not quite the property. None "
            "of the three layers verifies that the label is true; a caller "
            "presenting `human` passes all of them. What the constraint "
            "guarantees is that the audit trail can never contain the "
            "contradiction: no row can say Hermes canonized anything. That is "
            "internal consistency of the record, which is real and rare — and it "
            "is not the same as knowing who acted."
        ),
    },
    ("entity_relations.py", "reject_relation"): {
        "gate": "none",
        "local_guards": ("same three layers as canonize_relation", "status must be proposed", "closes the relation and frees the edge", "expected_revision", "idempotency with payload digest"),
        "reviewed": (
            "Refuses a proposal, which is safety-increasing, and shares "
            "`_decide` with canonization and retirement so the optimistic lock, "
            "the replay check and the audit record are identical across all "
            "three. The source says why that matters: a reader of the history is "
            "entitled to assume the three decisions were recorded the same way."
        ),
    },
    ("entity_relations.py", "retire_relation"): {
        "gate": "none",
        "local_guards": ("same three layers as canonize_relation", "status must be canonical", "retires rather than deletes", "records retired_by and retired_at", "expected_revision", "idempotency with payload digest"),
        "reviewed": (
            "Withdraws a relation that had been made canonical. It moves the row "
            "to `retired` and stamps `retired_by`, rather than deleting: the "
            "relation that was once true stays readable as having been true and "
            "withdrawn."
        ),
    },
    ("hermes_runtime_return.py", "record_external_runtime_return"): _UNREVIEWED,
    ("source_intake.py", "exclude_source"): _UNREVIEWED,
    ("source_intake.py", "link_project"): _UNREVIEWED,
    ("source_intake.py", "restore_source"): _UNREVIEWED,
    ("source_intake.py", "suggest_projects"): _UNREVIEWED,
    ("source_intake.py", "unlink_project"): _UNREVIEWED,
    ("source_intake.py", "update_metadata"): _UNREVIEWED,
    ("work_issue_scopes.py", "add_scope"): {
        "gate": "none",
        "local_guards": ("scope type and role vocabularies", "issue locked", "expected_version", "idempotency keyed on event type and payload", "event records the link"),
        "reviewed": (
            "Records which entities a Work Issue concerns. A scope link says what "
            "the issue is about; it grants nothing and admits nothing. The "
            "entity_type and scope_role vocabularies are closed frozensets and the "
            "endpoint is validated by a database trigger — "
            "`validate_work_issue_scope_endpoint` refuses an unknown project or "
            "decision reference, so a dangling scope cannot be stored even by a "
            "caller that skips this module."
        ),
    },
    ("work_issue_scopes.py", "replace_primary_scope"): {
        "gate": "none",
        "local_guards": ("replacement normalized to the primary role", "issue locked", "expected_version", "retire and add in one transaction", "idempotency with payload digest"),
        "reviewed": (
            "Swaps the primary scope in one transaction, so an issue is never left "
            "without one or holding two. The replacement's role is a literal "
            "`primary` inside the function, not a caller argument."
        ),
    },
    ("work_issue_scopes.py", "retire_scope"): {
        "gate": "none",
        "local_guards": ("issue locked", "expected_version", "idempotency keyed on event type and payload", "retirement rather than deletion, enforced by a trigger"),
        "reviewed": (
            "Withdraws a scope link. It retires rather than deletes, and that is "
            "not a convention this function is trusted to keep: "
            "`guard_work_issue_scope_link_mutation` refuses the DELETE outright — "
            "'WorkIssue scope links are retained; retire instead of deleting'. "
            "Third guard in this review enforced below Python."
        ),
    },
    ("work_issues.py", "add_comment"): {
        "gate": "none",
        "local_guards": ("idempotency replay", "row lock", "optimistic expected_version check", "event trail recording the author"),
        "reviewed": "A comment on a Work Issue is not a professional effect; the concurrency and trail guarantees are the right level for it.",
    },
    ("work_issues.py", "close_issue"): {
        "gate": "none",
        "local_guards": ("to_status and actor_kind are literals inside the function", "issue locked", "expected_version", "ALLOWED_TRANSITIONS confines done to review", "close_reason required", "idempotency"),
        "reviewed": (
            "Newly discovered by the delegation signal added in this batch. It is "
            "the only path to `done`, and it does not take the target from its "
            "caller: `to_status=\"done\"` and `actor_kind=\"human\"` are literals in "
            "the body, and `ALLOWED_TRANSITIONS` permits `done` only out of "
            "`review`. Its route adds the editor key and a human actor."
        ),
    },
    ("work_issues.py", "create_issue"): {
        "gate": "none",
        "local_guards": ("origin and status are literals in the INSERT", "requested_effect constrained by a SQL CHECK", "idempotency", "event records the creator"),
        "reviewed": (
            "Creates an open issue: `origin` is a literal `'human'` and `status` a "
            "literal `'open'` in the INSERT, so neither can be asked for. "
            "`requested_effect` is caller-supplied and this module does not check "
            "it — the column's CHECK constraint does, against the five permitted "
            "effects. That matters more than it looks: `hermes_execution."
            "admit_handoff` refuses anything but `read_only`, reading this column, "
            "so the constraint that bounds the whole Hermes boundary is enforced "
            "in SQL rather than here."
        ),
    },
    ("work_issues.py", "record_hermes_return"): {
        "gate": "none",
        "local_guards": ("outcome vocabulary", "summary and trace_refs required", "run must be the issue's own running run, locked", "target status derived from a table, not from the caller", "expected_version", "idempotency"),
        "reviewed": (
            "Where Hermes reports what it produced — and the clearest expression "
            "in this codebase of what Hermes may not do. The caller names an "
            "outcome; the resulting issue status is looked up in "
            "`RETURN_TO_ISSUE_STATUS`, whose whole range is `review` and "
            "`waiting`. Hermes cannot name `done` because it never names a status "
            "at all. The run must exist, belong to this issue and be `running`, "
            "read `FOR UPDATE`."
        ),
    },
    ("work_issues.py", "start_hermes_run"): {
        "gate": "none",
        "local_guards": ("issue must be assigned to hermes", "Task Contract and Context Pack must match the issue's", "status must be open or waiting", "requested_effect copied from the governed row", "expected_version", "idempotency"),
        "reviewed": (
            "The counterpart to `hermes_execution.record_external_runtime_start`. "
            "Its refusals compare the caller's Task Contract and Context Pack refs "
            "against the issue's own, and the run's `requested_effect` is copied "
            "from `issue[\"requested_effect\"]` rather than taken as an argument — "
            "so the bound on what the run may do comes from the governed row, not "
            "from whoever starts it. `actor_kind` is a literal `hermes`."
        ),
    },
    ("work_issues.py", "transition_issue"): {
        "gate": "none",
        "local_guards": ("issue locked", "ALLOWED_TRANSITIONS", "expected_version", "idempotency"),
        "reviewed": (
            "Newly discovered by the delegation signal added in this batch, and "
            "the one that most deserved finding: it takes both `to_status` and "
            "`actor_kind` from its caller, and it is how an issue moves. Its sole "
            "production route passes `to_status=\"in_progress\"` and "
            "`actor_kind=\"human\"` as literals behind the editor key and a human "
            "actor, and `ALLOWED_TRANSITIONS` refuses any move the state machine "
            "does not permit. Route-borne again: a second caller would choose both "
            "values freely, within the state machine."
        ),
    },
}


def _writes_durable_state(node: ast.AST) -> bool:
    return any(
        isinstance(child, ast.Constant)
        and isinstance(child.value, str)
        and SQL_WRITE.search(child.value)
        for child in ast.walk(node)
    )


def _private_writers(tree: ast.Module) -> set[str]:
    """Names of same-module helpers whose own body writes durable state."""
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name.startswith("_")
        and _writes_durable_state(node)
    }


def _calls(node: ast.AST) -> set[str]:
    return {
        child.func.id
        for child in ast.walk(node)
        if isinstance(child, ast.Call) and isinstance(child.func, ast.Name)
    }


def _discovered() -> set[tuple[str, str]]:
    """Return every public mutation entry point the net can see under mvp_vertical."""
    found: set[tuple[str, str]] = set()
    for path in sorted(MVP.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        writers = _private_writers(tree)
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name.startswith("_"):
                continue
            by_verb = node.name.split("_")[0] in MUTATION_PREFIXES
            by_delegation = bool(_calls(node) & writers)
            if by_verb or _writes_durable_state(node) or by_delegation:
                found.add((str(path.relative_to(MVP)), node.name))
    return found


def test_every_mutation_entry_point_is_declared() -> None:
    undeclared = sorted(_discovered() - set(INVENTORY))
    assert not undeclared, (
        "a consequential mutation entry point exists without a declared guard "
        "regime; add it to INVENTORY with the guard it actually performs "
        f"(_UNREVIEWED is an honest answer, silence is not): {undeclared}"
    )


def test_the_inventory_does_not_describe_functions_that_no_longer_exist() -> None:
    stale = sorted(set(INVENTORY) - _discovered())
    assert not stale, f"INVENTORY describes entry points that were removed or renamed: {stale}"


def test_both_discovery_signals_carry_weight() -> None:
    """Neither signal alone would enumerate the surface.

    The structural signal misses entry points that delegate their write; the verb
    signal misses writers named outside the verb list. Dropping either would
    silently shrink what this guard sees, so both are asserted to still matter.
    """
    verb_only, sql_only = set(), set()
    for path in sorted(MVP.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name.startswith("_"):
                continue
            key = (str(path.relative_to(MVP)), node.name)
            by_verb = node.name.split("_")[0] in MUTATION_PREFIXES
            by_sql = _writes_durable_state(node)
            if by_verb and not by_sql:
                verb_only.add(key)
            elif by_sql and not by_verb:
                sql_only.add(key)

    assert verb_only, "no delegating entry point found; the verb signal has stopped earning its place"
    assert sql_only, "no direct writer found outside the verb list; the structural signal has stopped earning its place"


GATE_REGIMES = {
    "enforce_consequential",
    "optional",
    "none",
    "gate_required_not_wired",
    "unreviewed",
}


def test_every_declared_entry_point_states_a_guard_regime() -> None:
    for key, record in INVENTORY.items():
        assert record["gate"] in GATE_REGIMES, key
        if record["gate"] == "unreviewed":
            assert record["local_guards"] is None, (
                f"{key} is recorded as unreviewed but names local guards; either it was "
                "reviewed, or the guards are a guess"
            )
        else:
            assert record["local_guards"], (
                f"{key} declares no guard at all; a reviewed mutation path must state what "
                "protects it, even when the central chokepoint is not invoked"
            )


def test_a_reviewed_entry_records_why_it_was_cleared() -> None:
    """A verdict without a reason is not a review.

    `none` is the easiest value to write and the hardest to audit later. Requiring
    the reasoning keeps it from becoming the default a future reader cannot
    distinguish from a shrug.
    """
    for key, record in INVENTORY.items():
        if record["gate"] == "unreviewed":
            continue
        assert record.get("reviewed"), (
            f"{key} carries a verdict with no recorded reasoning; say what was read "
            "and why the regime is right"
        )


def test_a_required_gate_that_is_not_wired_stays_visible_and_does_not_grow() -> None:
    """A path known to need the chokepoint, recorded rather than quietly deferred.

    This is the honest state for an effect whose review concluded it is
    consequential while nothing routes it through the gate. It is not the same as
    `none`, and collapsing the two would lose the only record that the decision
    was ever taken.
    """
    pending = [key for key, record in INVENTORY.items() if record["gate"] == "gate_required_not_wired"]
    assert len(pending) <= 8, (
        f"{len(pending)} entry points are known to need the chokepoint and do not reach "
        "it; the ceiling is 8. Wire one, or move the ceiling deliberately and say why."
    )


def test_the_unreviewed_debt_is_visible_and_does_not_grow() -> None:
    """Enumerated is not reviewed, and the gap is recorded rather than implied.

    The widened net enumerated 64 entry points that had not been read
    individually. The net was widened in the tenth batch and found 13 more, so
    the enumerated total is 85; 60 are read and 25 are not. Reviewing one means
    replacing `_UNREVIEWED` with its real guard regime and the reasoning behind
    it. This bound exists so the debt shrinks deliberately and cannot quietly
    grow.
    """
    unreviewed = [key for key, record in INVENTORY.items() if record["gate"] == "unreviewed"]
    assert len(unreviewed) <= 25, (
        f"{len(unreviewed)} entry points are unreviewed; the ceiling is 25. A new "
        "mutation entry point must be reviewed, not added to the backlog."
    )


def test_discovery_is_not_vacuous() -> None:
    assert len(_discovered()) >= 84


def _claimed_covered() -> set[tuple[str, str]]:
    return {key for key, record in INVENTORY.items() if record["gate"] == "enforce_consequential"}


def test_a_coverage_claim_requires_a_client_that_can_exist() -> None:
    """No entry point may claim a call that nothing can reach."""
    sources = "\n".join(path.read_text(encoding="utf-8") for path in MVP.rglob("*.py"))
    if "HttpPolicyClient(" not in sources:
        assert not _claimed_covered(), (
            "an entry point claims it routes through the chokepoint while "
            f"HttpPolicyClient is never instantiated: {sorted(_claimed_covered())}"
        )


def test_a_coverage_claim_is_backed_by_a_real_call() -> None:
    for module, function in sorted(_claimed_covered()):
        source = (MVP / module).read_text(encoding="utf-8")
        assert "enforce_consequential(" in source, (
            f"{module}::{function} is recorded as routing through the chokepoint, "
            "but the module contains no call to enforce_consequential"
        )
