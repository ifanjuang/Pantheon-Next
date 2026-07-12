"""Block 2 — the drafting seam.

The deterministic default drafter must be dossier-general (no devis_reprise
hardcode) and must assert nothing — it assembles evidence and defers to the
human gate. The pure drafter is tested without pgvector; the run()-level
injection is tested against a live pgvector service in CI.
"""

from __future__ import annotations

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

from mvp_vertical import store
from mvp_vertical.contract import load_contract
from mvp_vertical.drafting import DeterministicDrafter
from mvp_vertical.runner import run
from mvp_vertical.store import RetrievedChunk


def _chunk(source_ref: str, body: str, chunk_no: int = 0, distance: float = 0.3) -> RetrievedChunk:
    return RetrievedChunk(source_ref=source_ref, chunk_no=chunk_no, body=body, distance=distance)


# ---- DB-free: the deterministic drafter generalises and asserts nothing ------

def test_deterministic_drafter_speaks_to_the_actual_dossier():
    drafter = DeterministicDrafter()
    chunks = [
        _chunk(
            "dossiers/permis_amenagement/sources/note_plu_hauteurs.md",
            "En zone UB, la hauteur maximale est de 9 m à l'égout. Une surélévation d'un niveau est admise.",
        )
    ]
    body = drafter.draft(
        intent="Vérifier la faisabilité d'une surélévation au regard du PLU.",
        question="quelle hauteur maximale ?",
        chunks=chunks,
    )
    # speaks to THIS dossier via the cited passage…
    assert "surélévation" in body or "PLU" in body
    # …and carries none of the devis_reprise hardcode Block 1 emitted
    assert "Q-2026-041" not in body
    assert "terrasses" not in body


def test_deterministic_drafter_asserts_no_conclusion():
    body = DeterministicDrafter().draft(intent="", question="x", chunks=[_chunk("s.md", "texte source")])
    assert "candidat soumis à votre décision" in body
    assert "aucune conclusion n'est tirée" in body.lower()
    # it must never author an acceptance/commitment on the practitioner's behalf
    for banned in ("nous acceptons", "nous validons", "bon pour accord", "nous confirmons"):
        assert banned not in body.lower()


def test_deterministic_drafter_preserves_contradictions_by_restating():
    # Two conflicting passages both appear verbatim — the drafter neither
    # detects nor resolves the conflict; it is preserved by inclusion.
    chunks = [
        _chunk("a.md", "le poste 4 couvre les terrasses T2 et T3"),
        _chunk("b.md", "le lot 06 est limité à la seule terrasse T2"),
    ]
    body = DeterministicDrafter().draft(intent="", question="x", chunks=chunks)
    assert "T2 et T3" in body
    assert "la seule terrasse T2" in body


def test_deterministic_drafter_satisfies_the_seam():
    # A Hermes-side LLM drafter would satisfy the same Drafter seam; the default
    # is this offline deterministic one (no provider wired in this repo).
    drafter = DeterministicDrafter()
    assert callable(getattr(drafter, "draft", None))
    body = drafter.draft(intent="i", question="q", chunks=[_chunk("s.md", "b")])
    assert isinstance(body, str) and body


# ---- DB-gated: run() uses the injected drafter (CI pgvector) -----------------

@pytest.fixture(scope="module")
def conn():
    try:
        c = store.connect()
    except Exception as exc:  # pragma: no cover
        pytest.skip(f"pgvector unreachable: {exc}")
    yield c
    c.close()


@pytest.fixture(scope="module")
def contract():
    return load_contract(ROOT / "dossiers/devis_reprise/task_contract.yaml")


@pytest.fixture(scope="module")
def ingested(conn, contract):
    return store.ingest(conn, contract, ROOT)


def test_run_uses_the_injected_drafter(conn, contract, ingested):
    class StubDrafter:
        def draft(self, *, intent, question, chunks):
            return f"STUB::{len(chunks)}"

    out = run(conn, contract,
              "le devis de reprise correspond-il au périmètre du CCTP pour le lot 06 ?",
              drafter=StubDrafter())
    assert out.kind == "candidates"
    assert out.documents[0]["body"].startswith("STUB::")


def test_default_run_is_dossier_general_on_devis(conn, contract, ingested):
    out = run(conn, contract, "le devis de reprise correspond-il au périmètre du CCTP pour le lot 06 ?")
    assert out.kind == "candidates"
    body = out.documents[0]["body"]
    # the default drafter no longer authors the hardcoded devis analysis…
    assert "poste 4 du devis" not in body
    # …but the contradiction is still preserved, now by including both passages
    ep = out.documents[1]
    assert ep["contradictions_preserved"]
    assert len(ep["evidence_items"]) >= 2
