"""Steps 4-5 of the governed loop: scoped retrieval → candidate return.

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

from .contract import TaskContract, ContractError
from .drafting import (
    Drafter,
    DeterministicDrafter,
    duty_of_care_flags,
    grounding_review,
    review_flags,
    verify_draft,
)
from .store import RetrievedChunk, retrieve_scoped


class RunnerInvariantError(RuntimeError):
    """The runner was about to emit an object that breaks a governance
    invariant (e.g. authorizing an external action). Raised as a hard stop,
    never returned as data — a broken cage is a bug, not a candidate."""


# Phrases that would commit the practitioner if sent as-is. Flagging is
# advisory display material for the gate — never an auto-block or auto-fix.
COMMITMENT_PATTERNS = (
    r"nous acceptons",
    r"nous validons",
    r"vous pouvez (lancer|démarrer)",
    r"bon pour accord",
    r"nous confirmons",
)

# Advisory only. Matching one of these merely routes the request to a clearer
# refusal message when the contract forbids external_send. It is NOT the
# boundary and must never be mistaken for it: the boundary is structural — the
# runner has no transport, so it cannot send regardless of phrasing. Paraphrase
# evades the message, not the cage. (Adoption review, Gate 6.)
SEND_INTENT_TERMS = (
    "envoie", "envoyer", "envoi",
    "transmet", "transmiss",
    "expédi",
    "diffus",          # diffuser/diffusion d'un DCE aux entreprises = un envoi externe
    "fais suivre",
    "send", "forward",
)

# Below this cosine-distance quality, the perimeter is judged unable to
# support an answer and the runner reports a capability gap instead of
# improvising one. Calibrated on the devis_reprise fixtures (2026-07-09):
# in-perimeter questions score <= 0.66, off-topic questions >= 0.95 with
# the stopword-filtered hashing embedder; 0.85 keeps a margin both ways.
# Recalibrate whenever the embedder changes — that is a reviewed decision.
MAX_USEFUL_DISTANCE = 0.85


@dataclass(frozen=True)
class RunOutput:
    kind: str  # "candidates" | "refusal"
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
        for m in re.finditer(pattern, text, re.IGNORECASE):
            flags.append({"phrase": m.group(0), "risk": "external commitment if sent as-is"})
    return flags


# Statuses a candidate may never carry on the way out of the runner: they
# would assert an outcome only the human gate can grant.
_FORBIDDEN_STATUSES = frozenset({"sent", "approved", "authorized", "validated"})


def _assert_no_external_authorization(documents: list) -> None:
    """Post-condition on every runner output, on every path.

    The cage is structural — there is no transport in this package — but this
    guard makes the invariant explicit and testable so a later change (the
    Block 2 LLM slot, above all) cannot quietly emit an object that authorizes
    an external action or claims an outcome the gate alone may grant.
    """
    for doc in documents:
        if doc.get("external_action_authorized", False):
            raise RunnerInvariantError(
                f"runner emitted external_action_authorized=True on {doc.get('object_id')!r}"
            )
        status = str(doc.get("status", ""))
        if status in _FORBIDDEN_STATUSES:
            raise RunnerInvariantError(
                f"runner emitted forbidden status {status!r} on {doc.get('object_id')!r}"
            )


def run(
    conn,
    contract: TaskContract,
    question: str,
    drafter: Drafter | None = None,
) -> RunOutput:
    """Public entry point. Every path funnels through the post-condition guard
    so no output can break the no-external-authorization invariant.

    `drafter` is the Block 2 seam: pass a Hermes-side LLM drafter to fill the
    slot; omit it to use the deterministic, dossier-general default.
    """
    output = _run(conn, contract, question, drafter or DeterministicDrafter())
    _assert_no_external_authorization(output.documents)
    return output


def _run(
    conn,
    contract: TaskContract,
    question: str,
    drafter: Drafter,
) -> RunOutput:
    # forbidden-scope refusal path: an explicitly forbidden ask is refused
    # before any retrieval happens. The match is advisory routing to a clearer
    # message (see SEND_INTENT_TERMS); the actual guarantee is the absence of a
    # transport, enforced structurally and by _assert_no_external_authorization.
    lowered = question.lower()
    if "external_send" in contract.forbidden and any(term in lowered for term in SEND_INTENT_TERMS):
        return _refusal(contract, question, "forbidden_scope",
                        "external_send is forbidden by the contract; transmission is a human decision")

    chunks = retrieve_scoped(conn, contract, question)
    useful = [c for c in chunks if c.distance <= MAX_USEFUL_DISTANCE]
    if not useful:
        return _refusal(contract, question, "outside_perimeter",
                        "no declared source supports this question; widening the perimeter is a contract revision, not a runner decision")

    draft = drafter.draft(intent=contract.intent, question=question, chunks=useful)
    # Structural guard on the drafter's output before it can become a candidate:
    # an (untrusted, e.g. LLM) drafter may not cite evidence it was not given.
    # Raises DraftRejected — a bad draft is a bug, not a candidate.
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
        # Honest claim: verify_draft proved only that every citation refers to a
        # retrieved chunk — citation integrity, NOT that the prose is grounded or
        # true. Naming it grounding_verified overclaimed (review #4).
        "citation_integrity_verified": True,
        "commitment_flags": _detect_commitments(draft),
        # Advisory, non-blocking signals for the human gate — never enforcement:
        # - professional_assertion_flags: prose that reads like a professional
        #   verdict, detected ANYWHERE in the draft (with or without a citation),
        #   so a *cited* conclusion is still surfaced (review #3 regression fix).
        # - grounding_review: citation counts + assertive prose that carries no
        #   citation in its own sentence (issue #13 P5). The two are complementary
        #   and neither is a truth verdict: citation présente != conclusion validée.
        "professional_assertion_flags": review_flags(draft),
        # - duty_of_care_flags: prose that judges or retains an entreprise, where
        #   objectivité/équité and the MAF duty-of-conseil verifications apply.
        #   The cage never asserts those checks done; it surfaces them for the
        #   human MOE (docs/governance/PROFESSIONAL_DUTY_OF_CARE.md).
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
                "evidence_id": f"ei-{c.source_ref.rsplit('/', 1)[-1].split('.')[0]}-{c.chunk_no}",
                "claim": c.body[:160],
                "source_ref": c.source_ref,
                "retrieval_trace": c.retrieval_trace,
                "support_status": "sourced_not_verified",
            }
            for c in useful
        ],
        "assumptions": ["aucune hypothèse ajoutée par le runner ; toute hypothèse relève de la décision humaine"],
        "limitations": ["seuls les extraits déclarés au contrat ont été lus"],
        "contradictions_preserved": [
            "le runner restitue les passages sans arbitrer entre eux ; toute contradiction entre sources est conservée pour la décision humaine, non résolue"
        ],
        "open_risks": ["toute formulation d'accord engagerait le praticien si envoyée"],
        "possible_decisions": ["approve", "refuse", "request_revision", "request_more_evidence"],
        "governance_refs": ["docs/governance/MVP_GOVERNED_TASK_LOOP.md"],
    }
    return RunOutput(kind="candidates", documents=[result_candidate, evidence_pack])
