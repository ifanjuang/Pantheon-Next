"""Canonical Capability Passport validation and eligibility qualification.

This module validates the current flat Capability Passport schema from the
repository. It is read-only: validation and eligibility qualification are data,
not admission persistence, activation or task authorization.
"""

from __future__ import annotations

from typing import Any

import yaml
from jsonschema import Draft202012Validator

from .repo import find_repo_root, read_repo_text


APPROVED_REVIEW_STATUS = "reviewed"
IMMUTABLE_ANCHORS = ("commit_ref", "content_digest", "package_digest")


def _schema() -> dict[str, Any]:
    root = find_repo_root()
    loaded = yaml.safe_load(read_repo_text("schemas/capability_passport.schema.yaml", root))
    if not isinstance(loaded, dict):
        raise ValueError("Capability Passport schema must be a mapping")
    return loaded


def _path(error: Any) -> str:
    return ".".join(str(part) for part in error.absolute_path)


def _immutable_anchor(candidate: dict[str, Any]) -> dict[str, str] | None:
    provenance = candidate.get("implementation_provenance")
    if not isinstance(provenance, dict):
        return None
    for kind in IMMUTABLE_ANCHORS:
        value = provenance.get(kind)
        if isinstance(value, str) and value.strip():
            return {"kind": kind, "value": value.strip()}
    return None


def validate_passport(candidate: dict[str, Any] | None) -> dict[str, Any]:
    """Validate one current Capability Passport and qualify review eligibility.

    A reviewed Passport is eligible for governance review only when it pins an
    exact implementation release. This function never authorizes task use.
    """

    candidate = candidate if isinstance(candidate, dict) else {}
    schema = _schema()
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(candidate), key=_path)
    problems = [
        {"path": _path(error), "message": error.message}
        for error in errors
    ]

    gaps: list[str] = []
    status = candidate.get("status")
    anchor = _immutable_anchor(candidate)
    governance = candidate.get("governance")
    governance = governance if isinstance(governance, dict) else {}
    task_authorization = governance.get("task_authorization")

    if status == APPROVED_REVIEW_STATUS and anchor is None:
        gaps.append(
            "reviewed Capability Passport requires exact implementation provenance "
            "with commit_ref, content_digest or package_digest"
        )
    if status == "candidate" and task_authorization == "task_authorized":
        gaps.append("candidate Capability Passport must not be task-authorized")
    if status == APPROVED_REVIEW_STATUS and task_authorization == "task_authorized":
        gaps.append(
            "reviewed Capability eligibility does not itself establish task authorization"
        )

    valid = not problems
    exact_release_qualified = valid and status == APPROVED_REVIEW_STATUS and anchor is not None
    eligibility_posture = (
        "invalid"
        if not valid
        else "reviewed_exact_release"
        if exact_release_qualified and not gaps
        else "reviewed_with_governance_gaps"
        if status == APPROVED_REVIEW_STATUS
        else "candidate_or_nonreviewed"
    )

    return {
        "valid": valid,
        "ready_for_review": valid and not gaps,
        "passport_id": candidate.get("passport_id"),
        "status": status,
        "implementation_anchor": anchor,
        "exact_release_qualified": exact_release_qualified,
        "eligibility_posture": eligibility_posture,
        "problems": problems,
        "governance_gaps": gaps,
        "task_authorization": task_authorization,
        "authorization_effect": "none",
        "activation_effect": "none",
        "write_effect": False,
        "runtime_probe_performed": False,
        "next_human_decision": (
            "review exact release eligibility and any remaining governance gaps"
            if valid
            else "fix the Passport shape against the canonical schema"
        ),
        "non_equivalences": [
            "schema valid != admitted",
            "reviewed != task-authorized",
            "exact release known != safe",
            "eligibility != activation",
            "eligibility != task authorization",
            "runtime success != Evidence",
        ],
        "doctrine_refs": [
            "schemas/capability_passport.schema.yaml",
            "docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md",
            "docs/governance/CAPABILITY_REGISTRY.md",
            "docs/governance/TASK_CONTRACTS.md",
        ],
        "authority_note": (
            "Validation and eligibility qualification are data. The policy gate and human "
            "review consequential use; Task Contract / Execution Admission remains separate."
        ),
    }
