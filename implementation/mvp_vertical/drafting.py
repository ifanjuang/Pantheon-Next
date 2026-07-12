"""The drafting seam (Block 2).

Block 1 hardcoded a draft specific to the devis_reprise fixture — it produced
the wrong text for any other dossier (proven by the adversarial dossier's
xfail). Block 2 replaces the hardcode with a *seam*: the runner takes a
``Drafter`` and this module ships a deterministic, dossier-general default.

The LLM slot — a Hermes-side ``Drafter`` — plugs in here, but this repository
does NOT wire or route any provider. Provider routing is forbidden to this
external candidate (`GOVERNANCE_STATUS.md`), and the live LLM call belongs to
the governed Hermes profile:

    route_providers            -> forbidden here; belongs to Hermes
    deterministic_default      -> keeps this block offline and testable

The deterministic drafter **asserts nothing**. It assembles the retrieved
passages as the basis for a human decision and draws no domain conclusion — a
runner that authored analysis would be validating professional truth, which is
forbidden. Contradictions are preserved by restating passages verbatim, not by
detecting or resolving them.
"""

from __future__ import annotations

import re
from typing import Protocol, Sequence

from .store import RetrievedChunk


class DraftRejected(ValueError):
    """The verifier rejected a draft before it could become a candidate.

    A structural failure — the drafter cited evidence it was not given — is a
    bug in the drafter, not a candidate. The runner raises rather than emit it.
    This is the guard that lets an untrusted (LLM) Drafter fill the seam.
    """


_CITATION_RE = re.compile(r"\[([^\]#]+)#chunk-(\d+)\]")

# Heuristic proxy for a draft asserting a professional conclusion — the runner
# must not validate professional truth. Advisory only (keyword-based, so
# false-positive-prone): surfaced to the gate, NEVER an auto-reject. The real
# semantic check is the human gate (or, later, a Hermes-side LLM judge). Do not
# mistake this list for the guarantee — that lesson is Gate 6.
_VERDICT_PATTERNS = (
    r"est conforme", r"n'est pas conforme", r"est valide", r"est invalide",
    r"doit être (accepté|rejeté|refusé|validé|approuvé)",
    r"je conclus", r"nous concluons", r"il est établi",
)


def verify_draft(draft: str, chunks: Sequence[RetrievedChunk]) -> None:
    """Structural safety check on a drafter's output, before it becomes a
    candidate. Raises DraftRejected on failure.

    Enforced (structural, complete): every source reference in the draft must
    correspond to a chunk actually retrieved in-perimeter — no fabricated
    citations, no citing a source outside the declared scope. This is what
    lets an untrusted Drafter fill the seam: it cannot invent evidence.

    NOT enforced here: whether the prose asserts a professional conclusion or
    resolves a contradiction. Those are semantic and remain the human gate's
    job (see review_flags for advisory, non-blocking detection). This is a
    sourcing check, not a truth check — do not conflate the two.
    """
    provided = {(c.source_ref, c.chunk_no) for c in chunks}
    provided_refs = {c.source_ref for c in chunks}
    for match in _CITATION_RE.finditer(draft):
        ref, chunk_no = match.group(1), int(match.group(2))
        if ref not in provided_refs:
            raise DraftRejected(
                f"draft cites a source outside the retrieved perimeter: {ref!r}"
            )
        if (ref, chunk_no) not in provided:
            raise DraftRejected(
                f"draft cites {ref}#chunk-{chunk_no}, which was not among the retrieved chunks"
            )


def review_flags(draft: str) -> list[dict]:
    """Advisory, non-blocking flags for the gate: prose that reads like a
    professional conclusion. Heuristic — for human attention, not enforcement."""
    flags = []
    for pattern in _VERDICT_PATTERNS:
        for match in re.finditer(pattern, draft, re.IGNORECASE):
            flags.append({
                "phrase": match.group(0),
                "risk": "reads as a professional conclusion; the runner may not validate truth",
            })
    return flags


class Drafter(Protocol):
    """The seam a Hermes-side LLM drafter implements. Given the contract's
    intent, the question, and the in-perimeter chunks, return a draft body.
    It receives only already-scoped material and returns text — it cannot
    widen the perimeter, send, or approve."""

    def draft(
        self,
        *,
        intent: str,
        question: str,
        chunks: Sequence[RetrievedChunk],
    ) -> str:
        ...


class DeterministicDrafter:
    """Dossier-general, offline, deterministic default (no LLM, no provider).

    Assembles the retrieved passages and defers every judgement to the human
    gate. Works for any dossier because it authors no domain content.
    """

    def draft(
        self,
        *,
        intent: str,
        question: str,
        chunks: Sequence[RetrievedChunk],
    ) -> str:
        citations = "\n".join(
            f"- [{c.source_ref}#chunk-{c.chunk_no}] {c.body[:160].strip()}…"
            for c in chunks
        )
        request = (intent or question or "").strip()
        return (
            "Bonjour,\n\n"
            "Cette réponse est un candidat soumis à votre décision. Elle ne "
            "valide, n'accepte ni n'approuve aucun périmètre par elle-même.\n\n"
            f"Votre demande : {request}\n\n"
            "Éléments retenus dans le périmètre déclaré du dossier, à l'appui "
            "de votre décision :\n"
            f"{citations}\n\n"
            "Aucune conclusion n'est tirée à votre place. Les passages ci-dessus "
            "sont restitués tels quels, sans arbitrage entre eux ; toute "
            "contradiction éventuelle est conservée pour votre appréciation.\n\n"
            "Cordialement,\nL'agence"
        )
