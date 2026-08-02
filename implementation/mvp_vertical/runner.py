"""Steps 4-5 of the governed loop: scoped retrieval → candidate return.

STAND-IN (GOVERNANCE_STATUS.md stand-in rule): this module occupies the
Hermes-side execution seat for the proof loop. It is NOT the Hermes Agent:

    stand_in_runner != Hermes Agent

It exists to prove the governance cage end to end; the real runtime actor is
the governed Hermes profile. The LLM slot (a Hermes-side Drafter) plugs into the
Block 2 seam below — this repository never wires or routes a provider.

The runner produces exactly two kinds of output, both as data:

- a Result Candidate + Evidence Pack Candidate (status draft_to_review), or
- a refusal / capability-gap report, when the request falls outside the
  contract's perimeter or the perimeter cannot support an answer.

It approves nothing, sends nothing, remembers nothing. Drafting goes through
a seam (Block 2): run() takes a Drafter, defaulting to a deterministic,
dossier-general one (mvp_vertical/drafting.py). The LLM slot is a Hermes-side
Drafter injected here — this repository never wires or routes a provider.
"""

from __future__ import annotations

import datetime as _dt
import re
from dataclasses import dataclass

import yaml

from .contract import TaskContract, _schema
from .drafting import (
    Drafter,
    DeterministicDrafter,
    duty_of_care_flags,
    grounding_review,
    review_flags,
    verify_draft,
)
from .retrieval import HybridRetrievedChunk, retrieve_hybrid_scoped
from .store import RetrievedChunk, retrieve_scoped


class RunnerInvariantError(RuntimeError):
    """The runner was about to emit an object that breaks a governance
    invariant (e.g. authorizing an external action). Raised as a hard stop,
    never returned as data — a broken cage is a bug, not a candidate."""


COMMITMENT_PATTERNS = (
    r"nous acceptons",
    r"nous validons",
    r"vous pouvez (lancer|démarrer)",
    r"bon pour accord",
    r"nous confirmons",
)

SEND_INTENT_TERMS = (
    "envoie", "envoyer", "envoi",
    "transmet", "transmiss",
    "expédi",
    "diffus",
    "fais suivre",
    "send", "forward",
)

MAX_USEFUL_DISTANCE = 0.85
HYBRID_TOP_K = 4
HYBRID_CANDIDATE_K = 12
HYBRID_RRF_K = 60
_ORIGINAL_RETRIEVE_SCOPED = retrieve_scoped


@dataclass(frozen=True)
class RunOutput:
    kind: str
    documents: list

    def to_yaml(self) -> str:
        return yaml.safe_dump_all(self.documents, sort_keys=False, allow_unicode=True)


def _now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _refusal(contract: TaskContract, question: str, reason: str, detail: str) -> RunOutput:
    return RunOutput(
        kind="refusal",
        documents=[
            {
                "object_type": "result_candidate",
                "object_id": f"{contract.contract_id}.refusal",
                "result_candidate_id": f"{contract.contract_id}.refusal",
                "applies_to": contract.contract_id,
                "status": "refused_capability_gap",
                "created_at": _now(),
                "body": f"Refus : {detail}",
                "external_action_authorized": False,
                "refusal": {
                    "question": question,
                    "reason": reason,
                    "detail": detail,
                    "boundary": "the perimeter decides what can be answered; "
                                "the runner does not improvise beyond it",
                },
                "governance_refs": ["docs/governance/MVP_GOVERNED_TASK_LOOP.md"],
            }
        ],
    )


def _detect_commitments(text: str) -> list[dict]:
    flags = []
    for pattern in COMMITMENT_PATTERNS:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            flags.append(
                {
                    "phrase": match.group(0),
                    "risk": "engagement externe si envoyé tel quel",
                }
            )
    return flags


_FORBIDDEN_STATUSES = frozenset({"sent", "approved", "authorized", "validated"})


def _assert_no_external_authorization(documents: list) -> None:
    for document in documents:
        if document.get("external_action_authorized", False):
            raise RunnerInvariantError(
                f"runner emitted external_action_authorized=True on {document.get('object_id')!r}"
            )
        status = str(document.get("status", ""))
        if status in _FORBIDDEN_STATUSES:
            raise RunnerInvariantError(
                f"runner emitted forbidden status {status!r} on {document.get('object_id')!r}"
            )


def _assert_conforms_to_schema(documents: list) -> None:
    try:
        import jsonschema
    except ImportError as exc:  # pragma: no cover
        raise RunnerInvariantError("cannot validate runner output — jsonschema not installed") from exc
    schema = _schema()
    for document in documents:
        try:
            jsonschema.validate(document, schema)
        except jsonschema.ValidationError as exc:
            raise RunnerInvariantError(
                f"runner emitted a non-conforming {document.get('object_type')!r} "
                f"({document.get('object_id')!r}): {exc.message}"
            ) from exc


def _is_useful(hit: HybridRetrievedChunk) -> bool:
    """Admit a scoped lexical match or a useful semantic match.

    RRF orders candidates. It is not a truth, confidence or Evidence-quality
    threshold.
    """
    if hit.lexical_rank is not None:
        return True
    return hit.semantic_rank is not None and hit.chunk.distance <= MAX_USEFUL_DISTANCE


def _metric_profile(hit: HybridRetrievedChunk) -> str:
    semantic = hit.semantic_rank if hit.semantic_rank is not None else "none"
    lexical = hit.lexical_rank if hit.lexical_rank is not None else "none"
    return (
        "weighted_rrf_v1"
        f";semantic_rank={semantic}"
        f";lexical_rank={lexical}"
        f";hybrid_score={hit.hybrid_score:.12f}"
    )


def _retrieve_hits(conn, contract: TaskContract, question: str) -> list[HybridRetrievedChunk]:
    """Use hybrid retrieval while retaining the former injectable test seam.

    Existing callers and tests may replace ``runner.retrieve_scoped``. When that
    seam is replaced, its scoped semantic results are wrapped as a one-method
    ranking rather than silently ignored. Normal execution always uses the new
    hybrid path.
    """
    if retrieve_scoped is not _ORIGINAL_RETRIEVE_SCOPED:
        chunks = retrieve_scoped(conn, contract, question)
        return [
            HybridRetrievedChunk(
                chunk=chunk,
                hybrid_score=1.0 / (HYBRID_RRF_K + rank),
                semantic_rank=rank,
                lexical_rank=None,
            )
            for rank, chunk in enumerate(chunks, start=1)
        ]
    return retrieve_hybrid_scoped(
        conn,
        contract,
        question,
        top_k=HYBRID_TOP_K,
        candidate_k=HYBRID_CANDIDATE_K,
        rrf_k=HYBRID_RRF_K,
    )


def run(
    conn,
    contract: TaskContract,
    question: str,
    drafter: Drafter | None = None,
) -> RunOutput:
    output = _run(conn, contract, question, drafter or DeterministicDrafter())
    _assert_no_external_authorization(output.documents)
    _assert_conforms_to_schema(output.documents)
    return output


def _run(
    conn,
    contract: TaskContract,
    question: str,
    drafter: Drafter,
) -> RunOutput:
    lowered = question.lower()
    if "external_send" in contract.forbidden and any(
        term in lowered for term in SEND_INTENT_TERMS
    ):
        return _refusal(
            contract,
            question,
            "forbidden_scope",
            "external_send is forbidden by the contract; transmission is a human decision",
        )

    hits = _retrieve_hits(conn, contract, question)
    useful_hits = [hit for hit in hits if _is_useful(hit)]
    useful = [hit.chunk for hit in useful_hits]
    if not useful:
        return _refusal(
            contract,
            question,
            "outside_perimeter",
            "no declared source supports this question; widening the perimeter is a contract revision, not a runner decision",
        )

    draft = drafter.draft(intent=contract.intent, question=question, chunks=useful)
    verify_draft(draft, useful)

    now = _now()
    rc_id = f"{contract.contract_id}.rc-001"
    ep_id = f"{contract.contract_id}.ep-001"
    result_candidate = {
        "object_type": "result_candidate",
        "object_id": rc_id,
        "result_candidate_id": rc_id,
        "applies_to": contract.contract_id,
        "status": "draft_to_review",
        "created_at": now,
        "body": draft,
        "external_action_authorized": False,
        "citation_integrity_verified": True,
        "commitment_flags": _detect_commitments(draft),
        "professional_assertion_flags": review_flags(draft),
        "duty_of_care_flags": duty_of_care_flags(draft),
        "grounding_review": grounding_review(draft, useful),
        "governance_refs": [
            "docs/governance/MVP_GOVERNED_TASK_LOOP.md",
            "docs/governance/PROFESSIONAL_DUTY_OF_CARE.md",
        ],
    }
    evidence_pack = {
        "object_type": "evidence_pack_candidate",
        "object_id": ep_id,
        "evidence_pack_id": ep_id,
        "applies_to": contract.contract_id,
        "supports": rc_id,
        "status": "candidate",
        "created_at": now,
        "evidence_items": [
            {
                "evidence_id": (
                    f"ei-{hit.chunk.source_ref.rsplit('/', 1)[-1].split('.')[0]}-"
                    f"{hit.chunk.chunk_no}"
                ),
                "claim": hit.chunk.body[:160],
                "source_ref": hit.chunk.source_ref,
                "retrieval_trace": hit.chunk.retrieval_trace,
                "retrieval_audit": hit.chunk.retrieval_audit,
                "retrieval_provenance": hit.chunk.retrieval_provenance,
                "retrieval_metrics": {
                    "rank": rank,
                    "distance": hit.chunk.distance,
                    "metric": "cosine_distance",
                    "useful_distance_threshold": MAX_USEFUL_DISTANCE,
                    "profile": _metric_profile(hit),
                    "interpretation": "lower_is_closer_not_truth_probability",
                },
                "support_status": "sourced_not_verified",
            }
            for rank, hit in enumerate(useful_hits, start=1)
        ],
        "assumptions": [
            "aucune hypothèse ajoutée par le runner ; toute hypothèse relève de la décision humaine"
        ],
        "limitations": [
            "seuls les extraits déclarés au contrat ont été lus",
            "le classement hybride combine des rangs lexicaux et sémantiques ; son score ne mesure ni la vérité ni la qualité d'une Evidence",
        ],
        "contradictions_preserved": [
            "le runner restitue les passages sans arbitrer entre eux ; toute contradiction entre sources est conservée pour la décision humaine, non résolue"
        ],
        "open_risks": ["toute formulation d'accord engagerait le praticien si envoyée"],
        "possible_decisions": [
            "approve",
            "refuse",
            "request_revision",
            "request_more_evidence",
        ],
        "governance_refs": ["docs/governance/MVP_GOVERNED_TASK_LOOP.md"],
    }
    return RunOutput(kind="candidates", documents=[result_candidate, evidence_pack])
