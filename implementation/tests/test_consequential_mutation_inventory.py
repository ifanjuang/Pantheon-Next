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

Seventeen of the seventy-two entry points have been read individually; 55 have
not. The nine reviewed most recently were chosen because nothing in production
reaches them yet — eight are exercised only by tests and one, `disable_principal`,
is called by nothing at all. That made the question "is this effect consequential?"
answerable without unwinding a call graph, and it is the cheapest end of the
backlog rather than the most urgent one.

One of the nine came back as needing the chokepoint: `bind_oidc_identity` is the
point where an external identity becomes able to act as a governed principal.
Nothing routes it there, which is recorded as `gate_required_not_wired` rather
than softened into `none`.

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
    ("agency_classification.py", "archive_category"): _UNREVIEWED,
    ("agency_classification.py", "assign_category"): _UNREVIEWED,
    ("agency_classification.py", "create_category"): _UNREVIEWED,
    ("agency_classification.py", "retire_category_assignment"): _UNREVIEWED,
    ("agency_classification.py", "update_category"): _UNREVIEWED,
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
        "gate": "none",
        "local_guards": ("required project_id, review_ref, actor and idempotency_key", "payload digest compared on replay, refusing a reused key with different content", "normalization before write"),
        "reviewed": "Records a review that already happened, carried by review_ref; the consequence gate belongs at that review rather than at its recording. The closest call of the nine — it installs canonical state — and the one most worth re-arbitrating if the review upstream is ever less than governed.",
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
    ("human_access.py", "grant_access"): _UNREVIEWED,
    ("human_access.py", "revoke_grant"): _UNREVIEWED,
    ("human_access.py", "revoke_oidc_binding"): {
        "gate": "none",
        "local_guards": ("required binding_id", "raises on unknown binding", "idempotent when already revoked"),
        "reviewed": "Withdraws an ability, so it is safety-increasing. Same finding as disable_principal: no actor is recorded on the revocation.",
    },
    ("information_projection.py", "add_document_link"): _UNREVIEWED,
    ("information_projection.py", "remove_document_link"): _UNREVIEWED,
    ("information_projection.py", "update_projection_metadata"): _UNREVIEWED,
    ("knowledge.py", "apply_edit_request"): {
        "gate": "none",
        "local_guards": ("request status", "single transaction with audit", "idempotency"),
        "reviewed": (
            "Applies an edit whose request status already carries the decision, with the audit written inside the same transaction so the trail cannot detach from the effect."
        ),
    },
    ("knowledge.py", "complete_edit_request"): _UNREVIEWED,
    ("knowledge.py", "create_edit_request"): _UNREVIEWED,
    ("knowledge.py", "publish_knowledge"): _UNREVIEWED,
    ("knowledge.py", "revise_knowledge"): _UNREVIEWED,
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
    assert len(pending) <= 1, (
        f"{len(pending)} entry points are known to need the chokepoint and do not reach "
        "it; the ceiling is 1. Wire it, or take the decision again deliberately."
    )


def test_the_unreviewed_debt_is_visible_and_does_not_grow() -> None:
    """Enumerated is not reviewed, and the gap is recorded rather than implied.

    The widened net enumerated 64 entry points that had not been read
    individually. Nine have now been reviewed, leaving 55. Reviewing one means
    replacing `_UNREVIEWED` with its real guard regime and the reasoning behind
    it. This bound exists so the debt shrinks deliberately and cannot quietly
    grow.
    """
    unreviewed = [key for key, record in INVENTORY.items() if record["gate"] == "unreviewed"]
    assert len(unreviewed) <= 55, (
        f"{len(unreviewed)} entry points are unreviewed; the ceiling is 55. A new "
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
