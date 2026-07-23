"""Gate-validation slice: validate a caller-provided human decision reference.

The preflight (`service.evaluate_preflight`) only checks that a
`human_decision_ref` is *present*; it reports `gate_signal_validation_performed:
false`. This module performs the missing content check: given a caller-asserted
decision reference and the requirement the consequential effect must satisfy, it
validates scope, approval level, expiry, object identity and digest, and refuses
a non-human signer.

Read-only and side-effect free. It validates the fields the caller supplies; it
does not fetch, persist or cryptographically authenticate the decision, and a
`valid` verdict is not an approval or an authorization. The human decision
remains external to this service (see HTTP_API_CONTRACT.md, Human decision
boundary).
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


# Signer identities that may never stand in for a human decision. A decision is
# a recorded human determination; a runtime, service account or bot cannot make
# one. Matched case-insensitively as a whole token or a prefix.
_SYSTEM_SIGNER_TOKENS = (
    "system",
    "service",
    "service-account",
    "serviceaccount",
    "bot",
    "agent",
    "runtime",
    "hermes",
    "openwebui",
    "pantheon",
    "pantheon-mcp",
    "mcp",
    "root",
    "automation",
    "cron",
    "scheduler",
)


def _rank(value: Any) -> int:
    """Approval ceiling rank C0..C5, or -1 when malformed."""
    if not isinstance(value, str) or len(value) != 2 or not value.startswith("C"):
        return -1
    try:
        return int(value[1])
    except ValueError:
        return -1


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def _is_system_signer(decided_by: Any) -> bool:
    if not isinstance(decided_by, str) or not decided_by.strip():
        return True  # an empty signer is not a human
    token = decided_by.strip().lower()
    head = token.replace("_", "-").split(":", 1)[0].split("@", 1)[0]
    for marker in _SYSTEM_SIGNER_TOKENS:
        if head == marker or head.startswith(marker + "-") or token.startswith(marker + ":"):
            return True
    return False


def _scope_of(value: Any) -> tuple[Any, Any] | None:
    if not isinstance(value, dict):
        return None
    scope_type = value.get("scope_type")
    scope_id = value.get("scope_id")
    if not scope_type or not scope_id:
        return None
    return (scope_type, scope_id)


def validate_decision(payload: dict[str, Any], now: datetime | None = None) -> dict[str, Any]:
    """Validate a caller-provided decision reference against a requirement.

    ``payload`` carries ``decision`` (the asserted human decision reference) and
    ``expectation`` (what the consequential effect requires). Returns a verdict
    as data. A ``valid`` verdict means the asserted fields are internally
    consistent with the requirement — never that the effect is approved.
    """
    now = now or datetime.now(timezone.utc)
    decision = payload.get("decision")
    expectation = payload.get("expectation")
    decision = decision if isinstance(decision, dict) else {}
    expectation = expectation if isinstance(expectation, dict) else {}

    checks: dict[str, str] = {}
    findings: list[str] = []

    # 1. Structural completeness.
    required_fields = ("decision_id", "decided_by", "approval_level", "scope")
    missing = [f for f in required_fields if not decision.get(f)]
    if missing:
        checks["structural"] = "fail"
        findings.append(f"decision is missing required fields: {sorted(missing)}")
    else:
        checks["structural"] = "ok"

    # 2. Signer must be human.
    if _is_system_signer(decision.get("decided_by")):
        checks["signer"] = "fail"
        findings.append(
            "decided_by is empty or a non-human (system/service/runtime) identity; "
            "only a human may make a decision"
        )
    else:
        checks["signer"] = "ok"

    # 3. Expiry.
    expires_at = decision.get("expires_at")
    if expires_at is None or expires_at == "":
        checks["expiry"] = "not_checked"
        findings.append("decision has no expires_at; expiry could not be verified")
    else:
        parsed = _parse_time(expires_at)
        if parsed is None:
            checks["expiry"] = "fail"
            findings.append(f"decision expires_at is not a valid timestamp: {expires_at!r}")
        elif parsed < now:
            checks["expiry"] = "fail"
            findings.append(f"decision expired at {parsed.isoformat()} (as of {now.isoformat()})")
        else:
            checks["expiry"] = "ok"

    # 4. Scope match.
    required_scope = _scope_of(expectation.get("required_scope"))
    decision_scope = _scope_of(decision.get("scope"))
    if required_scope is None:
        checks["scope"] = "not_checked"
    elif decision_scope is None:
        checks["scope"] = "fail"
        findings.append("decision scope is missing scope_type/scope_id")
    elif decision_scope != required_scope:
        checks["scope"] = "fail"
        findings.append(
            f"decision scope {decision_scope} does not match required scope {required_scope}"
        )
    else:
        checks["scope"] = "ok"

    # 5. Approval level sufficiency.
    required_ceiling = expectation.get("required_ceiling")
    if required_ceiling is None:
        checks["level"] = "not_checked"
    else:
        have, need = _rank(decision.get("approval_level")), _rank(required_ceiling)
        if have < 0 or need < 0:
            checks["level"] = "fail"
            findings.append(
                f"approval level malformed (decision={decision.get('approval_level')!r}, "
                f"required={required_ceiling!r}); expected C0..C5"
            )
        elif have < need:
            checks["level"] = "fail"
            findings.append(
                f"decision approval level {decision.get('approval_level')} is below the "
                f"required ceiling {required_ceiling}"
            )
        else:
            checks["level"] = "ok"

    # 6. Object identity.
    expected_identity = expectation.get("object_identity")
    if expected_identity in (None, ""):
        checks["object_identity"] = "not_checked"
    elif decision.get("object_identity") != expected_identity:
        checks["object_identity"] = "fail"
        findings.append(
            "decision object_identity does not match the effect it is asked to gate"
        )
    else:
        checks["object_identity"] = "ok"

    # 7. Digest.
    expected_digest = expectation.get("expected_digest")
    if expected_digest in (None, ""):
        checks["digest"] = "not_checked"
        findings.append("no expected_digest supplied; the decision content was not verified")
    elif decision.get("content_digest") != expected_digest:
        checks["digest"] = "fail"
        findings.append("decision content_digest does not match the expected digest")
    else:
        checks["digest"] = "ok"

    verdict = "valid" if not any(state == "fail" for state in checks.values()) else "invalid"

    return {
        "result": "validated",
        "verdict": verdict,
        "gate_signal_validation_performed": True,
        "checks": checks,
        "findings": findings,
        "limits": [
            "Validation checks the caller-provided decision fields only; it does "
            "not fetch, persist or cryptographically authenticate the decision.",
            "A valid verdict is not an approval or an authorization; it does not "
            "execute, send, write or promote memory. The human decision remains "
            "external to this service.",
        ],
    }
