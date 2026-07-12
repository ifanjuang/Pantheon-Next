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

from typing import Protocol, Sequence

from .store import RetrievedChunk


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
