"""Capability passport validation (validation-only).

Mirrors templates/mcp_capability_passport.yaml. A valid passport is not an
authorized capability: validation reports shape and governance gaps; the
gate and the human decide. `visible != admitted`, `valid != authorized`.
"""

from __future__ import annotations

from typing import Any

APPROVAL_LEVELS = ["C0", "C1", "C2", "C3", "C4", "C5"]

ENUMS: dict[str, list[str]] = {
    "mcp_capability_passport.status": ["candidate", "reviewed", "suspended", "rejected"],
    "mcp_capability_passport.mcp_server.transport": ["stdio", "http", "other", ""],
    "mcp_capability_passport.mcp_server.trust_level": ["trusted", "internal", "external", "unknown"],
    "mcp_capability_passport.capability.primitive": ["resource", "prompt", "tool"],
    "mcp_capability_passport.governance.task_authorization": ["unauthorized", "task_authorized"],
    "mcp_capability_passport.governance.risk_level": ["low", "medium", "high", "critical"],
    "mcp_capability_passport.governance.approval_required": APPROVAL_LEVELS,
    "mcp_capability_passport.governance.memory_behavior": ["none", "candidate_only", "never_canonical"],
    "mcp_capability_passport.result_handling.default_output_status": ["draft", "candidate", "to_verify", "blocked"],
    "mcp_capability_passport.revocation.status": ["active", "suspended", "revoked"],
}

TRISTATE = ["true", "false", "unknown", True, False]

REQUIRED_PATHS = [
    "mcp_capability_passport.passport_id",
    "mcp_capability_passport.status",
    "mcp_capability_passport.mcp_server.server_id",
    "mcp_capability_passport.capability.primitive",
    "mcp_capability_passport.capability.name",
    "mcp_capability_passport.operation.reads_private_data",
    "mcp_capability_passport.operation.writes_external_state",
    "mcp_capability_passport.operation.can_send_to_external_party",
    "mcp_capability_passport.operation.can_change_memory",
    "mcp_capability_passport.governance.task_authorization",
    "mcp_capability_passport.governance.risk_level",
    "mcp_capability_passport.governance.approval_required",
    "mcp_capability_passport.governance.memory_behavior",
]

TRISTATE_PATHS = [
    "mcp_capability_passport.operation.reads_private_data",
    "mcp_capability_passport.operation.writes_external_state",
    "mcp_capability_passport.operation.can_execute_code",
    "mcp_capability_passport.operation.can_send_to_external_party",
    "mcp_capability_passport.operation.can_modify_dossier",
    "mcp_capability_passport.operation.can_change_memory",
]


def _get(data: dict, dotted: str) -> Any:
    cur: Any = data
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def _approval_at_least(value: Any, floor: str) -> bool:
    try:
        return APPROVAL_LEVELS.index(str(value)) >= APPROVAL_LEVELS.index(floor)
    except ValueError:
        return False


def validate_passport(data: dict) -> dict:
    """Validate one passport document. Returns a report, never a permission."""
    problems: list[str] = []
    gaps: list[str] = []

    if not isinstance(data, dict) or "mcp_capability_passport" not in data:
        return {
            "valid": False,
            "problems": ["top-level key 'mcp_capability_passport' is missing"],
            "governance_gaps": [],
            "authority_note": _AUTHORITY_NOTE,
        }

    for path in REQUIRED_PATHS:
        value = _get(data, path)
        if value in (None, ""):
            problems.append(f"required field missing or empty: {path}")

    for path, allowed in ENUMS.items():
        value = _get(data, path)
        if value is not None and value not in allowed:
            problems.append(f"{path}: '{value}' not in {allowed}")

    for path in TRISTATE_PATHS:
        value = _get(data, path)
        if value is not None and value not in TRISTATE:
            problems.append(f"{path}: '{value}' must be true/false/unknown")

    # Governance gap rules — shape may be valid while governance is not ready.
    op = lambda name: _get(data, f"mcp_capability_passport.operation.{name}")
    gov = lambda name: _get(data, f"mcp_capability_passport.governance.{name}")

    external = op("can_send_to_external_party") in (True, "true")
    writes = op("writes_external_state") in (True, "true")
    memory = op("can_change_memory") in (True, "true")
    unknowns = [p for p in TRISTATE_PATHS if op(p.rsplit(".", 1)[-1]) == "unknown"]

    if external and not _approval_at_least(gov("approval_required"), "C3"):
        gaps.append("can_send_to_external_party=true requires approval_required >= C3")
    if external and gov("user_decision_gate_required") is not True:
        gaps.append("can_send_to_external_party=true requires user_decision_gate_required: true")
    if writes and not _approval_at_least(gov("approval_required"), "C2"):
        gaps.append("writes_external_state=true requires approval_required >= C2")
    if memory and gov("memory_behavior") not in ("candidate_only", "never_canonical"):
        gaps.append("can_change_memory=true requires memory_behavior candidate_only or never_canonical")
    if unknowns:
        gaps.append(
            "operation flags still 'unknown' (review before any task authorization): "
            + ", ".join(unknowns)
        )
    if _get(data, "mcp_capability_passport.status") == "candidate" and gov("task_authorization") == "task_authorized":
        gaps.append("a candidate passport must not be task_authorized (visible != admitted)")

    return {
        "valid": not problems,
        "ready_for_review": not problems and not gaps,
        "problems": problems,
        "governance_gaps": gaps,
        "next_human_decision": (
            "review the passport and decide admission at the gate"
            if not problems
            else "fix the passport shape, then resubmit for review"
        ),
        "doctrine_refs": [
            "templates/mcp_capability_passport.yaml",
            "docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md",
            "docs/governance/APPROVALS.md",
        ],
        "authority_note": _AUTHORITY_NOTE,
    }


_AUTHORITY_NOTE = (
    "Validation is not authorization. The policy decision is data; "
    "the gate decides; the human decides."
)
