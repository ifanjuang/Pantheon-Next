"""Block 3 — Register Candidate proposal (issue #13).

The only transition into the register is:

    Decision Record + decision == approve + retention_authorized == true
        -> Register Candidate

A Register Candidate is NOT a Register Entry, and retention_authorized is NOT
memory promotion. This module produces a schema-valid ``register_candidate`` as
DATA, linked to the exact decision record and to the digests of the content the
human reviewed. It writes nothing durable and promotes no memory:

    register_candidate != register_entry
    retention_authorized != memory_promoted
    decision_recorded != consequence_executed

``statement`` (what is retained), ``scope`` (where it applies) and
``retention_authorized`` (a human authorization, distinct from the approve
decision) are supplied by the human — never fabricated here.
"""

from __future__ import annotations

import hashlib
import json

from .contract import _schema
from .runner import _assert_no_external_authorization


class RegisterRefusal(ValueError):
    """The register transition preconditions are not met — not an approved
    decision, retention not authorized, or a missing statement/scope."""


def _canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _validate(candidate: dict) -> None:
    try:
        import jsonschema
    except ImportError as exc:  # pragma: no cover - runtime dep, guard only
        raise RegisterRefusal("cannot validate register_candidate — jsonschema not installed") from exc
    try:
        jsonschema.validate(candidate, _schema())
    except jsonschema.ValidationError as exc:
        raise RegisterRefusal(
            f"register_candidate does not conform to the vendored schema: {exc.message}"
        ) from exc


def propose_register_candidate(
    decision_record: dict,
    *,
    retention_authorized: bool,
    statement: str,
    scope: str,
) -> dict:
    """Propose a register candidate from an approved decision — or refuse.

    Refuses unless the input is a decision_record whose decision is ``approve``
    and ``retention_authorized`` is exactly ``True``, with a human-authored
    ``statement`` and ``scope``. Returns a schema-valid register_candidate that
    is not memory until admitted, writes nothing durable, and authorizes
    nothing external.
    """
    if not isinstance(decision_record, dict) or decision_record.get("object_type") != "decision_record":
        raise RegisterRefusal("input is not a decision_record")
    if decision_record.get("decision") != "approve":
        raise RegisterRefusal(
            f"only an approved decision may propose retention (decision="
            f"{decision_record.get('decision')!r})"
        )
    if retention_authorized is not True:
        raise RegisterRefusal(
            "retention_authorized must be explicitly true — retention is a human "
            "authorization, separate from the approve decision"
        )
    statement = (statement or "").strip()
    scope = (scope or "").strip()
    if not statement:
        raise RegisterRefusal("statement is required: what is being registered must be human-authored")
    if not scope:
        raise RegisterRefusal("scope is required: where the statement applies")

    decision_id = decision_record.get("decision_id") or decision_record["object_id"]
    applies_to = decision_record.get("applies_to", decision_id)

    # basis links the candidate to the exact reviewed content — the decision and
    # the digests the decision recorded (integrity chain, not a memory write).
    basis = [f"decision:{decision_id}"]
    for key, label in (("candidate_digest", "candidate_digest"),
                       ("evidence_pack_digest", "evidence_pack_digest")):
        digest = decision_record.get(key)
        if isinstance(digest, dict) and digest.get("value"):
            basis.append(f"{label}:{digest.get('algorithm', 'sha256')}:{digest['value']}")

    id_digest = hashlib.sha256(
        _canonical({"created_because_of": decision_id, "statement": statement, "scope": scope}).encode("utf-8")
    ).hexdigest()[:12]
    object_id = f"{applies_to}.register.{id_digest}"

    candidate = {
        "object_type": "register_candidate",
        "object_id": object_id,
        "candidate_id": object_id,
        "status": "candidate",
        "created_because_of": decision_id,
        "statement": statement,
        "scope": scope,
        "basis": basis,
        "not_memory_until_admitted": True,
        "forbidden_reuse": ["memory_promotion", "external_send", "durable_write"],
        "governance_refs": [
            "docs/governance/MVP_GOVERNED_TASK_LOOP.md",
            "docs/governance/USER_DECISION_GATE.md",
        ],
    }
    # A register candidate authorizes no external action either, and it is only
    # a candidate — never an admitted entry, never durable memory.
    _assert_no_external_authorization([candidate])
    _validate(candidate)
    return candidate
