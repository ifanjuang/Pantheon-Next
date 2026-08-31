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

Twenty-eight of the seventy-two entry points have been read individually; 44 have
not. The first batches were chosen because nothing in production reached them —
answerable without unwinding a call graph, and the cheapest end of the backlog
rather than the most urgent one. The `knowledge.py` batch is the first that is
live on both sides: every one of its four entry points is behind a route a key
holder can call today.

Six entry points are now recorded as `gate_required_not_wired` rather than
softened into `none`. `bind_oidc_identity` is where an external identity becomes
able to act as a governed principal. `store_reviewed_dossier` installs canonical
APU state on the strength of a `review_ref` that nothing validates. `revoke_grant`
lets one access manager lock another one out. `publish_knowledge` accepts
`review_status="reviewed"` as a caller assertion. `complete_edit_request` can
return a human-rejected request to `proposed`. `apply_edit_request` acts on that
status as though it were a decision.

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
    ("agency_information.py", "act_working_information"): _UNREVIEWED,
    ("agency_information.py", "create_information"): _UNREVIEWED,
    ("agency_information.py", "derive_working_version"): _UNREVIEWED,
    ("agency_information.py", "update_working_information"): _UNREVIEWED,
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
    ("decision_requests.py", "cancel_request"): _UNREVIEWED,
    ("decision_requests.py", "create_request"): _UNREVIEWED,
    ("decision_requests.py", "resolve_request"): _UNREVIEWED,
    ("document_revision_discussion.py", "create_comment"): _UNREVIEWED,
    ("entity_relations.py", "propose_relation"): _UNREVIEWED,
    ("execution_results.py", "append_review_disposition"): _UNREVIEWED,
    ("execution_results.py", "store_execution_result"): _UNREVIEWED,
    ("hermes_execution.py", "admit_handoff"): {
        "gate": "none",
        "local_guards": ("human actor", "read_only effect only", "Task Contract and Context Pack identity", "TTL bounds", "idempotency"),
        "reviewed": (
            "Admits an external execution handoff bounded to a read_only effect, tied to a Task Contract and Context Pack identity and a TTL. Admission of a read_only effect is not authorization of a consequential one."
        ),
    },
    ("hermes_execution.py", "record_external_runtime_start"): _UNREVIEWED,
    ("hermes_execution.py", "revoke_admission"): _UNREVIEWED,
    ("hermes_handoff_store.py", "submit_handoff"): _UNREVIEWED,
    ("hermes_launch_context.py", "reserve_launch"): _UNREVIEWED,
    ("hermes_result_candidate.py", "create_result_candidate"): _UNREVIEWED,
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
    ("information_projection.py", "add_document_link"): _UNREVIEWED,
    ("information_projection.py", "remove_document_link"): _UNREVIEWED,
    ("information_projection.py", "update_projection_metadata"): _UNREVIEWED,
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
        "local_guards": ("status", "variant ownership", "audit inside apply transaction"),
        "reviewed": (
            "Applies a variant the request already selected; ownership is checked so a variant cannot be applied to a request it does not belong to."
        ),
    },
    ("knowledge_edit_variants.py", "create_variant_request"): _UNREVIEWED,
    ("knowledge_edit_variants.py", "project_execution_result_variant"): _UNREVIEWED,
    ("knowledge_edit_variants.py", "reject_request"): _UNREVIEWED,
    ("knowledge_edit_variants.py", "select_variant"): _UNREVIEWED,
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
    ("work_issue_scopes.py", "add_scope"): _UNREVIEWED,
    ("work_issue_scopes.py", "replace_primary_scope"): _UNREVIEWED,
    ("work_issue_scopes.py", "retire_scope"): _UNREVIEWED,
    ("work_issues.py", "add_comment"): {
        "gate": "none",
        "local_guards": ("idempotency replay", "row lock", "optimistic expected_version check", "event trail recording the author"),
        "reviewed": "A comment on a Work Issue is not a professional effect; the concurrency and trail guarantees are the right level for it.",
    },
    ("work_issues.py", "create_issue"): _UNREVIEWED,
    ("work_issues.py", "record_hermes_return"): _UNREVIEWED,
    ("work_issues.py", "start_hermes_run"): _UNREVIEWED,
}


def _writes_durable_state(node: ast.AST) -> bool:
    return any(
        isinstance(child, ast.Constant)
        and isinstance(child.value, str)
        and SQL_WRITE.search(child.value)
        for child in ast.walk(node)
    )


def _discovered() -> set[tuple[str, str]]:
    """Return every public mutation entry point the net can see under mvp_vertical."""
    found: set[tuple[str, str]] = set()
    for path in sorted(MVP.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name.startswith("_"):
                continue
            by_verb = node.name.split("_")[0] in MUTATION_PREFIXES
            if by_verb or _writes_durable_state(node):
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
    assert len(pending) <= 6, (
        f"{len(pending)} entry points are known to need the chokepoint and do not reach "
        "it; the ceiling is 6. Wire one, or move the ceiling deliberately and say why."
    )


def test_the_unreviewed_debt_is_visible_and_does_not_grow() -> None:
    """Enumerated is not reviewed, and the gap is recorded rather than implied.

    The widened net enumerated 64 entry points that had not been read
    individually. Twenty have now been reviewed, leaving 44. Reviewing one means
    replacing `_UNREVIEWED` with its real guard regime and the reasoning behind
    it. This bound exists so the debt shrinks deliberately and cannot quietly
    grow.
    """
    unreviewed = [key for key, record in INVENTORY.items() if record["gate"] == "unreviewed"]
    assert len(unreviewed) <= 44, (
        f"{len(unreviewed)} entry points are unreviewed; the ceiling is 44. A new "
        "mutation entry point must be reviewed, not added to the backlog."
    )


def test_discovery_is_not_vacuous() -> None:
    assert len(_discovered()) >= 70


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
