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
entry point defended itself with its own local checks — signed previews,
confirmation phrases, optimistic concurrency, idempotency keys, admission state
machines — and no two of them shared a guard.

Local defence was never the problem. The problem was that a ninth entry point
could be added tomorrow inheriting none of it, and no check in this repository
would notice.

The Cockpit's Knowledge write is now wired to the chokepoint and enforcement
defaults to required, so one entry point below records real coverage. Seven still
do not, and that is the current honest state rather than a defect list.

This test makes the surface enumerable: every public `apply_*` / `admit_*` /
`promote_*` / `approve_*` / `commit_*` function in `mvp_vertical` must appear
below with its actual current guard regime. Adding one without declaring it fails
closed, so the decision about its guard becomes explicit and reviewable rather
than implicit.

```text
import edge != call path
module reachable != gate invoked
local guard != central chokepoint
declared inventory != wired chokepoint
```

Updating `INVENTORY` is the intended way to add an entry point. Recording
`gate: "none"` is a permitted, honest answer — recording nothing is not.
"""

from __future__ import annotations

import ast
from pathlib import Path

MVP = Path(__file__).resolve().parents[1] / "mvp_vertical"

# Prefixes that name a function producing or admitting a durable effect.
MUTATION_PREFIXES = frozenset({"apply", "admit", "promote", "approve", "commit"})

# Every declared entry point carries the guard it actually performs today.
#
#   gate = "enforce_consequential"  -> calls the Pantheon chokepoint
#   gate = "optional"               -> chokepoint reachable but opt-in, default off
#   gate = "none"                   -> defends itself with module-local checks only
#
# A claim of "enforce_consequential" is verified below in both directions: it is
# refused while no client can exist, and it must be backed by a real call.
#
# `local_guards` records what genuinely protects the path, so that "none" is
# never mistaken for "unprotected".
INVENTORY: dict[tuple[str, str], dict[str, object]] = {
    ("agency_change_candidates.py", "apply_project_candidate"): {
        "gate": "none",
        "local_guards": ("human actor", "status", "base revision staleness", "idempotency"),
    },
    ("apu_owner.py", "apply_source_match"): {
        "gate": "none",
        "local_guards": ("prior authorization id", "exact command shape", "idempotency"),
    },
    ("apu_write_preparation.py", "apply_authorized_write_command"): {
        "gate": "none",
        "local_guards": (
            "reviewed command chain",
            "stored index vs embedded effect",
            "owner and object revision freshness",
            "idempotency",
        ),
    },
    ("hermes_execution.py", "admit_handoff"): {
        "gate": "none",
        "local_guards": (
            "human actor",
            "read_only effect only",
            "Task Contract and Context Pack identity",
            "TTL bounds",
            "idempotency",
        ),
    },
    ("knowledge.py", "apply_edit_request"): {
        "gate": "none",
        "local_guards": ("request status", "single transaction with audit", "idempotency"),
    },
    ("knowledge_edit_variants.py", "apply_selected_variant"): {
        "gate": "none",
        "local_guards": ("status", "variant ownership", "audit inside apply transaction"),
    },
    ("knowledge_update.py", "apply_knowledge_update"): {
        "gate": "enforce_consequential",
        "local_guards": (
            "signed preview",
            "exact confirmation phrase",
            "expected_version and base digest",
            "idempotency",
        ),
    },
    ("project_document_admission.py", "admit_source_as_revision"): {
        "gate": "none",
        "local_guards": ("explicit target document", "exact capture identity", "idempotency"),
    },
}


def _discovered() -> set[tuple[str, str]]:
    """Return every public module-level mutation entry point under mvp_vertical."""
    found: set[tuple[str, str]] = set()
    for path in sorted(MVP.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name.startswith("_"):
                continue
            if node.name.split("_")[0] in MUTATION_PREFIXES:
                found.add((str(path.relative_to(MVP)), node.name))
    return found


def test_every_mutation_entry_point_is_declared() -> None:
    undeclared = sorted(_discovered() - set(INVENTORY))
    assert not undeclared, (
        "a consequential mutation entry point exists without a declared guard "
        "regime; add it to INVENTORY with the guard it actually performs "
        f"(\"none\" is an honest answer, silence is not): {undeclared}"
    )


def test_the_inventory_does_not_describe_functions_that_no_longer_exist() -> None:
    stale = sorted(set(INVENTORY) - _discovered())
    assert not stale, f"INVENTORY describes entry points that were removed or renamed: {stale}"


def test_discovery_is_not_vacuous() -> None:
    # A refactor that renamed every entry point would make the guard above
    # trivially satisfied.
    assert len(_discovered()) >= 8


def test_every_declared_entry_point_states_a_real_local_guard() -> None:
    """No entry point may be recorded as both ungated and unguarded."""
    for key, record in INVENTORY.items():
        assert record["gate"] in {"enforce_consequential", "optional", "none"}, key
        assert record["local_guards"], (
            f"{key} declares no guard at all; a mutation path must state what "
            "protects it, even when the central chokepoint is not invoked"
        )


def _claimed_covered() -> set[tuple[str, str]]:
    return {key for key, record in INVENTORY.items() if record["gate"] == "enforce_consequential"}


def test_a_coverage_claim_requires_a_client_that_can_exist() -> None:
    """No entry point may claim a call that nothing can reach.

    Before the application factory built one, `HttpPolicyClient` had no non-test
    instantiation, so a claim of `enforce_consequential` described a call that
    could not happen. Removing the wiring must make that claim fail again rather
    than leave the inventory asserting coverage the deployment lost.
    """
    sources = "\n".join(path.read_text(encoding="utf-8") for path in MVP.rglob("*.py"))
    if "HttpPolicyClient(" not in sources:
        assert not _claimed_covered(), (
            "an entry point claims it routes through the chokepoint while "
            f"HttpPolicyClient is never instantiated: {sorted(_claimed_covered())}"
        )


def test_a_coverage_claim_is_backed_by_a_real_call() -> None:
    """A declared claim must be visible in the module that makes it."""
    for module, function in sorted(_claimed_covered()):
        source = (MVP / module).read_text(encoding="utf-8")
        assert "enforce_consequential(" in source, (
            f"{module}::{function} is recorded as routing through the chokepoint, "
            "but the module contains no call to enforce_consequential"
        )


def test_the_wired_entry_point_is_reachable_only_with_a_decision_point() -> None:
    """The claim must hold at the application boundary, not only in the module.

    A module that calls the gate when handed a client still bypasses it when the
    application hands it None. Enforcement therefore defaults to required, and
    `test_policy_client_assembly.py` covers the refusal paths in full.
    """
    shell = (MVP / "cockpit_shell.py").read_text(encoding="utf-8")
    assert "require_policy_client" in shell
    assert 'os.getenv("MVP_POLICY_ENFORCEMENT", "required")' in shell
