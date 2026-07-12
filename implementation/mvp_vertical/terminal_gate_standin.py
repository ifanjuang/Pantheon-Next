"""Terminal decision-gate STAND-IN (adoption review, Gates 4 & 5).

This is NOT the OpenWebUI cockpit and NOT the final decision surface:

    terminal_gate != OpenWebUI cockpit

It stands in for the human decision gate so the governance cage can be proven
end to end. It reads the runner's candidate stream and records a human
decision as a schema-conforming ``decision_record``. It *records* a decision;
it never *executes* the decision's consequence — no send, no register write,
no memory promotion. Even ``approve`` authorizes nothing external:

    draft != external_send_authorization

System-signer refusal (Gate 5): the system may never sign. ``decided_by`` must
be supplied by a human and can neither default to nor be a system identity.
Without a human signer, the gate refuses.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from .contract import _schema
from .runner import _assert_no_external_authorization

# The decision is taken here, at a terminal stand-in — never fabricated as the
# cockpit. Recorded verbatim into every decision_record.
DECISION_SURFACE = "terminal_gate_standin"

# Fallback decision menu, used only if the evidence pack does not carry its own
# possible_decisions. The evidence pack's menu wins when present.
_DEFAULT_DECISIONS = ("approve", "refuse", "request_revision", "request_more_evidence")

# Identities that ARE the system and can never be the human decider. A
# decided_by matching any of these (case-insensitive) is a system-signer
# attempt and is refused — this is Gate 5 made structural.
_SYSTEM_IDENTITIES = frozenset({
    "system", "runner", "hermes", "mvp-vertical", "mvp_vertical", "gate",
    "terminal_gate_standin", "openwebui", "cockpit", "ai", "assistant", "claude",
})


class GateRefusal(ValueError):
    """The gate refuses to record a decision (unknown decision, non-reviewable
    candidate, or — above all — an attempt to have the system sign)."""


def _find(documents: list, object_type: str) -> dict | None:
    for doc in documents:
        if isinstance(doc, dict) and doc.get("object_type") == object_type:
            return doc
    return None


def _consequences(decision: str) -> dict:
    """What the decision *means* and, explicitly, what the gate does NOT do.

    Every consequence is declared not-performed here: the gate records, it does
    not act. Approval in particular never authorizes transmission.
    """
    meaning = {
        "approve": "the human approves the draft as a candidate response, "
                   "not an instruction to send",
        "refuse": "the human rejects the candidate",
        "request_revision": "the human asks for a revised candidate",
        "request_more_evidence": "the human asks for more evidence before deciding",
    }.get(decision, "recorded human decision")
    return {
        "meaning": meaning,
        "executed_by_gate": False,
        "external_send": "forbidden here; a separate human action, never granted by approval",
        "register_write": "not performed by the gate",
        "memory_promotion": "not performed by the gate",
    }


def _validate_record(record: dict) -> None:
    """Self-check: the produced decision_record must conform to the vendored
    schema (Gate 1 discipline) — the gate conforms, it does not invent shape."""
    try:
        import jsonschema
    except ImportError as exc:  # pragma: no cover - runtime dep, guard only
        raise GateRefusal("cannot validate decision_record — jsonschema not installed") from exc
    try:
        jsonschema.validate(record, _schema())
    except jsonschema.ValidationError as exc:
        raise GateRefusal(
            f"decision_record does not conform to the vendored schema: {exc.message}"
        ) from exc


def record_decision(
    documents: list,
    *,
    decision: str,
    decided_by: str,
    rationale: str = "",
) -> dict:
    """Record a human decision on a runner candidate stream as a decision_record.

    Raises GateRefusal on an unknown decision, a non-reviewable candidate, or a
    missing/system signer. Returns a schema-conforming decision_record that
    authorizes nothing external.
    """
    result_candidate = _find(documents, "result_candidate")
    evidence_pack = _find(documents, "evidence_pack_candidate")
    if result_candidate is None:
        raise GateRefusal("no result_candidate in the stream to decide on")
    if result_candidate.get("status") != "draft_to_review":
        raise GateRefusal(
            f"candidate is not reviewable (status={result_candidate.get('status')!r}); "
            "only a draft_to_review candidate can be decided"
        )

    allowed = tuple((evidence_pack or {}).get("possible_decisions", _DEFAULT_DECISIONS))
    if decision not in allowed:
        raise GateRefusal(f"decision {decision!r} is not one of {allowed}")

    # Gate 5 — system-signer refusal. No default, no system identity.
    signer = (decided_by or "").strip()
    if not signer:
        raise GateRefusal(
            "decided_by is required: the system may not sign a decision; a human must"
        )
    if signer.lower() in _SYSTEM_IDENTITIES:
        raise GateRefusal(
            f"decided_by={signer!r} is a system identity; only a human may decide"
        )

    applies_to = result_candidate.get("result_candidate_id") or result_candidate["object_id"]
    record = {
        "object_type": "decision_record",
        "object_id": f"{applies_to}.decision",
        "decision_id": f"{applies_to}.decision",
        "status": "recorded",
        "applies_to": applies_to,
        "decision": decision,
        "decided_by": signer,
        "decision_surface": DECISION_SURFACE,
        "rationale": rationale,
        "consequences": _consequences(decision),
        "external_action_authorized": False,
        "governance_refs": [
            "docs/governance/USER_DECISION_GATE.md",
            "docs/governance/MVP_GOVERNED_TASK_LOOP.md",
        ],
    }
    if evidence_pack is not None:
        record["related_evidence_pack"] = (
            evidence_pack.get("evidence_pack_id") or evidence_pack.get("object_id")
        )

    # Reuse the runner's invariant: a decision_record may not authorize an
    # external action either. Belt-and-suspenders against a future change.
    _assert_no_external_authorization([record])
    _validate_record(record)
    return record


def load_candidates(path: str | Path) -> list:
    """Read a candidate stream (the YAML `run` emits) into a list of documents."""
    text = Path(path).read_text(encoding="utf-8")
    return [doc for doc in yaml.safe_load_all(text) if isinstance(doc, dict)]


def to_yaml(record: dict) -> str:
    return yaml.safe_dump(record, sort_keys=False, allow_unicode=True)
