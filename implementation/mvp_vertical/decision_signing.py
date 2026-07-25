"""Producer side of human-issuer authentication: sign a decision reference.

The Pantheon PDP (`mcp-server` gate-validation) authenticates the human issuer by
verifying an HMAC-SHA256 signature over the signed decision fields against a
configured issuer key registry. This module is the matching producer: given a
human issuer's shared secret, it computes that signature so the cockpit/operator
can emit an **authenticated** decision reference. Without a signer there is
nothing for the PDP to authenticate; this closes that loop.

The algorithm MUST match Pantheon-Next
`mcp-server/pantheon_mcp/gate_validation.py` (`_SIGNED_FIELDS`, canonical JSON
with sorted keys, HMAC-SHA256). A pinned known-answer test guards this side
against drift; if the PDP algorithm changes, re-sync here.

Signing authenticates *who decided*. It is not an approval and does not
authorize an effect — the PDP still checks scope, ceiling, expiry, object
identity, digest and the V0 effect flags.
"""

from __future__ import annotations

import hashlib
import hmac
import json
from typing import Any

# Must equal gate_validation._SIGNED_FIELDS in Pantheon-Next. Signing binds the
# identity to the authorization envelope, so a signature cannot be replayed for a
# different scope, object, ceiling or expiry.
SIGNED_FIELDS = (
    "decision_id",
    "decided_by",
    "approval_level",
    "scope",
    "object_identity",
    "content_digest",
    "expires_at",
)


def _signing_bytes(decision: dict[str, Any]) -> bytes:
    payload = {field: decision.get(field) for field in SIGNED_FIELDS}
    return json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def sign_decision(decision: dict[str, Any], secret: str) -> str:
    """Return the issuer's HMAC-SHA256 signature over the signed decision fields."""
    if not isinstance(decision, dict):
        raise ValueError("decision must be a mapping")
    if not secret:
        raise ValueError("an issuer signing secret is required")
    return hmac.new(secret.encode("utf-8"), _signing_bytes(decision), hashlib.sha256).hexdigest()


def signed_decision(decision: dict[str, Any], secret: str) -> dict[str, Any]:
    """Return a copy of the decision with its issuer ``signature`` attached."""
    out = dict(decision)
    out["signature"] = sign_decision(decision, secret)
    return out


def signed_decision_payload(decision_payload: dict[str, Any], secret: str) -> dict[str, Any]:
    """Sign the ``decision`` inside a full ``{decision, expectation}`` payload.

    The signature is carried on the decision, so it flows unchanged through
    ``policy_gate.enforce_consequential`` to the PDP's ``validate_decision``."""
    if not isinstance(decision_payload, dict):
        raise ValueError("decision_payload must be a mapping")
    decision = decision_payload.get("decision")
    if not isinstance(decision, dict):
        raise ValueError("decision_payload.decision must be a mapping")
    out = dict(decision_payload)
    out["decision"] = signed_decision(decision, secret)
    return out
