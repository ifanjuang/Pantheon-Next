"""Controlled NAS intake and strict project-document naming."""

from __future__ import annotations

import uuid
from pathlib import Path

import pytest

from mvp_vertical import store
from mvp_vertical.contract import TaskContract
from mvp_vertical.naming import DocumentNameError, parse_document_name


def test_parse_strict_project_document_name() -> None:
    parsed = parse_document_name(
        "Projects/MAISON-A/30_DCE/"
        "MAISON-A_A1_DCE_IFJ_CCTP_LOT-06_2026-07-20.pdf"
    )
    assert parsed.project_code == "MAISON-A"
    assert parsed.revision_index == "A1"
    assert parsed.phase_folder == "30_DCE"
    assert parsed.distributor == "IFJ"
    assert parsed.document_type == "CCTP"
    assert parsed.object_name == "LOT-06"
    assert parsed.document_date.isoformat() == "2026-07-20"
    assert parsed.extension == "pdf"


@pytest.mark.parametrize(
    ("source_ref", "message"),
    [
        (
            "Projects/MAISON-A/50_Chantier/"
            "MAISON-A_A1_DCE_IFJ_CCTP_LOT-06_2026-07-20.pdf",
            "must be stored directly in 30_DCE",
        ),
        (
            "Projects/MAISON-A/30_DCE/"
            "MAISON-A_1_DCE_IFJ_CCTP_LOT-06_2026-07-20.pdf",
            "revision index",
        ),
        (
            "Projects/MAISON-A/30_DCE/"
            "MAISON-A_A1_DCE_IFJ_CCTP_LOT_06_2026-07-20.pdf",
            "use hyphens inside fields",
        ),
        (
            "Projects/MAISON-A/30_DCE/"
            "MAISON-A_A1_DCE_IFJ_CCTP_LOT-06_2026-02-30.pdf",
            "valid YYYY-MM-DD",
        ),
    ],
)
def test_reject_non_conforming_document_name(source_ref: str, message: str) -> None:
    with pytest.raises(DocumentNameError, match=message):
        parse_document_name(source_ref)


@pytest.fixture
def conn():
    try:
        connection = store.connect()
    except Exception as exc:  # pragma: no cover - unit-only local environment
        pytest.skip(f"PostgreSQL/pgvector unreachable: {exc}")
    yield connection
    connection.close()


def _contract(tmp_path: Path, dossier: str, sources: tuple[str, ...]) -> TaskContract:
    raw = {
        "object_type": "task_contract",
        "object_id": f"tc.{dossier}",
        "contract_id": f"tc.{dossier}",
        "scope": {
            "dossier": dossier,
            "parent_project_id": "project-card-maison-a",
            "declared_sources": [{"source_ref": source} for source in sources],
        },
    }
    return TaskContract(raw=raw, path=tmp_path / "tc.yaml", dossier=dossier, sources=sources)


def test_incremental_intake_preserves_other_documents_and_enriches_card(conn, tmp_path) -> None:
    dossier = f"nas-intake-{uuid.uuid4().hex}"
    cctp = (
        "Projects/MAISON-A/30_DCE/"
        "MAISON-A_A1_DCE_IFJ_CCTP_LOT-06_2026-07-20.md"
    )
    courrier = (
        "Projects/MAISON-A/50_Chantier/"
        "MAISON-A_B1_CHANTIER_ENTREPRISE-X_COURRIER_REPRISE-FACADE_2026-07-21.md"
    )
    for source, body in ((cctp, "# CCTP\n\nLot 06."), (courrier, "# Courrier\n\nReprise façade.")):
        path = tmp_path / source
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
    contract = _contract(tmp_path, dossier, (cctp, courrier))

    assert store.intake_document(conn, contract, tmp_path, cctp, ingestion_id="cctp") == 1
    assert store.intake_document(
        conn, contract, tmp_path, courrier, ingestion_id="courrier"
    ) == 1

    card = store.get_document_card(conn, dossier, cctp)
    assert card["parent_project_id"] == "project-card-maison-a"
    assert card["naming"] == {
        "project_code": "MAISON-A",
        "revision_index": "A1",
        "phase_code": "DCE",
        "phase_folder": "30_DCE",
        "distributor": "IFJ",
        "document_type": "CCTP",
        "object_name": "LOT-06",
        "document_date": "2026-07-20",
        "extension": "md",
        "validated": True,
    }

    (tmp_path / cctp).write_text("# CCTP\n\nLot 06 révisé.", encoding="utf-8")
    assert store.intake_document(conn, contract, tmp_path, cctp, ingestion_id="cctp-revised") == 1
    with conn.cursor() as cur:
        cur.execute(
            "SELECT source_ref, count(*) FROM chunks WHERE dossier = %s "
            "GROUP BY source_ref ORDER BY source_ref",
            (dossier,),
        )
        assert cur.fetchall() == [(cctp, 1), (courrier, 1)]
