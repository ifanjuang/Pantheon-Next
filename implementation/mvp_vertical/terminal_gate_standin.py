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

Decision identity (issue #13, P1): every recorded decision is a distinct event
with a unique ``decision_id`` (a content digest) and a microsecond
``recorded_at``; ``supersedes_decision_id`` links a revising decision to the
one it replaces. This stand-in *emits* distinct events; it does NOT persist
them, so it cannot itself guarantee an append-only history — that is a property
of the future decision store, not of this repository:

    distinct_events_emitted != append_only_history_guaranteed
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import json
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


def _now_micro() -> str:
    """UTC timestamp with microsecond precision — fine enough that two distinct
    decisions never share a recorded_at, so their content digests differ."""
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def _canonical(obj) -> str:
    """Stable serialization for hashing: sorted keys, no incidental whitespace."""
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _decision_digest(payload: dict) -> str:
    """Deterministic sha256 over a canonical serialization of the decision's
    identifying content. Same inputs (incl. recorded_at) -> same id; any
    difference -> a different id."""
    return hashlib.sha256(_canonical(payload).encode("utf-8")).hexdigest()


def _content_digest(obj: dict) -> dict:
    """A schema-shaped integrity reference proving exactly what content was
    reviewed. Any change to the object changes the digest (issue #13, P2)."""
    return {
        "algorithm": "sha256",
        "value": hashlib.sha256(_canonical(obj).encode("utf-8")).hexdigest(),
    }


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
    recorded_at: str | None = None,
    supersedes_decision_id: str | None = None,
) -> dict:
    """Record a human decision on a runner candidate stream as a decision_record.

    Raises GateRefusal on an unknown decision, a non-reviewable candidate, or a
    missing/system signer. Returns a schema-conforming decision_record that
    authorizes nothing external.

    Each call is a distinct event: decision_id is a content digest and
    recorded_at is microsecond-precise, so two decisions on the same candidate
    never collide. Pass supersedes_decision_id to link a revising decision to
    the one it replaces; pass recorded_at to pin the timestamp (tests, replay).
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
    now = recorded_at or _now_micro()
    # The id derives from the decision's identifying content, so distinct
    # decisions get distinct ids and a superseding decision is its own event.
    digest = _decision_digest({
        "applies_to": applies_to,
        "decision": decision,
        "decided_by": signer,
        "rationale": rationale,
        "recorded_at": now,
        "supersedes_decision_id": supersedes_decision_id,
    })[:12]
    decision_id = f"{applies_to}.decision.{digest}"
    record = {
        "object_type": "decision_record",
        "object_id": decision_id,
        "decision_id": decision_id,
        "status": "recorded",
        "applies_to": applies_to,
        "decision": decision,
        "decided_by": signer,
        "decision_surface": DECISION_SURFACE,
        "recorded_at": now,
        "rationale": rationale,
        # Integrity: prove exactly what content the human reviewed. Any change
        # to the candidate (or evidence pack) changes its digest (issue #13, P2).
        "candidate_digest": _content_digest(result_candidate),
        "consequences": _consequences(decision),
        "external_action_authorized": False,
        "governance_refs": [
            "docs/governance/USER_DECISION_GATE.md",
            "docs/governance/MVP_GOVERNED_TASK_LOOP.md",
        ],
    }
    if supersedes_decision_id is not None:
        record["supersedes_decision_id"] = supersedes_decision_id
    if evidence_pack is not None:
        record["related_evidence_pack"] = (
            evidence_pack.get("evidence_pack_id") or evidence_pack.get("object_id")
        )
        record["evidence_pack_digest"] = _content_digest(evidence_pack)

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
