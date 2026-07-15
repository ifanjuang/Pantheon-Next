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
#
# The legal-qualification tournures were added after the SPS case (a DCE clause
# asserting "le maître d'ouvrage est exempté des obligations SPS … relève de la
# catégorie 3"): asserting a point of law is exactly what objectivité/équité
# forbids the architect from doing lightly (docs/governance/PROFESSIONAL_DUTY_OF_CARE.md).
_VERDICT_PATTERNS = (
    r"est conforme", r"n'est pas conforme", r"est valide", r"est invalide",
    r"doit être (accepté|rejeté|refusé|validé|approuvé)",
    r"je conclus", r"nous concluons", r"il est établi",
    # legal qualification / exemption asserted as settled
    r"est exempté", r"sont exemptés", r"n'est pas soumis", r"ne sont pas soumis",
    r"est soumis à l'article", r"relève de la catégorie", r"est exonéré",
    r"est (conforme|contraire) à la (loi|réglementation|norme)",
)

# A judgment on, or selection of, an ENTREPRISE — the case where objectivité et
# équité (Code de déontologie) and the MAF duty-of-conseil verifications apply.
# Each pattern requires a judgment/selection word near "entreprise"/"offre", so
# neutral restitution of passages that merely mention "les entreprises" does not
# trip it. Advisory only, like every flag here.
_COMPANY_JUDGMENT_PATTERNS = (
    r"\b(retenir|retenue|retenu|écarter|écartée|écarté)\b[^.]*\bentreprise\b",
    r"\bentreprise\b[^.]*\b(retenue|retenu|écartée|écarté|recommandée|recommandé|"
    r"sérieuse|compétente|qualifiée|fiable|la mieux|la moins)\b",
    r"\bje\s+recommande\b", r"\bnous\s+recommandons\b",
    r"\bmeilleure\s+offre\b", r"\bmieux-disant\b", r"\bmoins-disant\b",
    r"\bmeilleur\s+rapport\s+qualité[- ]prix\b",
)

# The duty-of-conseil verifications the cage can never assert from its sources.
_DUTY_OF_CARE_CHECKS = (
    "assurance décennale / RC pro vérifiée",
    "qualifications métier vérifiées",
    "références / visites de chantier",
    "avis (surtout négatif) motivé par écrit",
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


def duty_of_care_flags(draft: str) -> list[dict]:
    """Advisory, non-blocking flags for the gate: prose that judges or selects an
    ENTREPRISE — where objectivité/équité and the MAF duty-of-conseil apply.

    When a draft evaluates or retains a company, the architect's written duty of
    care attaches: verifying insurance (décennale/RC pro), qualifications and
    references, and motivating a negative opinion in writing. The cage has NO
    source for those verifications, so it never asserts them done — it surfaces
    them as unestablished, for the human MOE to carry (and motivate in writing).
    Heuristic and advisory only; absence of a flag proves nothing.

    See docs/governance/PROFESSIONAL_DUTY_OF_CARE.md.
    """
    flags = []
    for pattern in _COMPANY_JUDGMENT_PATTERNS:
        for match in re.finditer(pattern, draft, re.IGNORECASE):
            flags.append({
                "phrase": match.group(0),
                "risk": "jugement/choix d'une entreprise : objectivité et équité "
                        "requises ; l'avis se motive par écrit (MOE humain)",
                "verifications_not_established_here": list(_DUTY_OF_CARE_CHECKS),
                "basis": "docs/governance/PROFESSIONAL_DUTY_OF_CARE.md",
            })
    return flags


def grounding_review(draft: str, chunks: Sequence[RetrievedChunk]) -> dict:
    """Advisory grounding visibility for the gate (issue #13, P5) — before a
    real Hermes-side LLM drafter fills the seam.

    Reports how much of the draft is cited and flags *assertive prose that
    carries no citation in its own sentence*. It is advisory only: NOT a score,
    NOT an approval, and NOT a professional-truth verdict. Crucially, the
    absence of a flag does not mean the draft is grounded or true — that
    remains the human gate's judgement. (This is the Gate 6 discipline: a
    heuristic is never the guarantee.)
    """
    uncited_claim_flags = []
    for sentence in re.split(r"(?<=[.!?])\s+|\n+", draft):
        stripped = sentence.strip()
        if not stripped or _CITATION_RE.search(stripped):
            continue  # empty, or the sentence carries its own citation
        for pattern in _VERDICT_PATTERNS:
            if re.search(pattern, stripped, re.IGNORECASE):
                # The vendored schema's grounding_review def types
                # uncited_claim_flags as an array of strings (upstream dc9068e),
                # so each flag is the offending sentence itself.
                uncited_claim_flags.append(stripped[:200])
                break
    return {
        "citation_count": len(_CITATION_RE.findall(draft)),
        "retrieved_chunk_count": len(chunks),
        "uncited_claim_flags": uncited_claim_flags,
        "note": "advisory only — not a score, not an approval, not a truth "
                "verdict. Absence of flags does not mean the draft is grounded "
                "or true; the human gate decides.",
    }


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
