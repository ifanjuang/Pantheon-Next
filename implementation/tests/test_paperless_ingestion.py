from __future__ import annotations

import hashlib
import uuid
from pathlib import Path

import pytest

from mvp_vertical import store
from mvp_vertical.contract import ContractError, TaskContract
from mvp_vertical.documents import ConvertedDocument
from mvp_vertical.paperless import PaperlessSourceCapture
from mvp_vertical.paperless_ingestion import get_binding, intake_paperless_document


class _FakePaperless:
    def __init__(self, capture: PaperlessSourceCapture) -> None:
        self.capture = capture
        self.calls = []

    def capture_document(self, document_id: int, *, version_id: str):
        self.calls.append((document_id, version_id))
        assert document_id == self.capture.document_id
        assert version_id == self.capture.version_id
        return self.capture


class _FakeDocling:
    converter = "docling_serve"
    converter_version = "paperless-test-1"
    config_digest = "paperless-config"
    observation_kind = "fixture"

    def convert(self, path: Path) -> ConvertedDocument:
        assert path.read_bytes().startswith(b"%PDF")
        return ConvertedDocument(
            markdown="# CCTP charpente\n\nPrescription issue de la version Paperless exacte.",
            document_json={"schema_name": "DoclingDocument", "name": path.name},
            converter=self.converter,
            converter_version=self.converter_version,
            config_digest=self.config_digest,
        )


@pytest.fixture
def conn():
    try:
        connection = store.connect()
    except Exception as exc:  # pragma: no cover - local unit-only environment
        pytest.skip(f"PostgreSQL/pgvector unreachable: {exc}")
    yield connection
    connection.close()


def _capture(document_id: int = 42, version_id: str = "7") -> PaperlessSourceCapture:
    content = b"%PDF-1.7\nfictional-paperless-source"
    digest = hashlib.sha256(content).hexdigest()
    return PaperlessSourceCapture(
        document_id=document_id,
        version_id=version_id,
        original_filename="CCTP-charpente.pdf",
        media_type="application/pdf",
        byte_size=len(content),
        content_hash=f"sha256:{digest}",
        storage_reference=f"paperless://document/{document_id}/version/{version_id}",
        source_ref=f"paperless/{document_id}/versions/{version_id}/CCTP-charpente.pdf",
        content=content,
    )


def _contract(source_ref: str, dossier: str) -> TaskContract:
    return TaskContract(
        raw={
            "object_type": "task_contract",
            "object_id": f"tc.{dossier}",
            "contract_id": f"tc.{dossier}",
            "scope": {
                "dossier": dossier,
                "parent_project_id": dossier,
                "declared_sources": [{"source_ref": source_ref}],
            },
        },
        path=Path("fixture-task-contract.yaml"),
        dossier=dossier,
        sources=(source_ref,),
    )


def test_exact_paperless_version_enters_existing_document_vertical(conn):
    capture = _capture()
    dossier = f"project-paperless-{uuid.uuid4().hex}"
    contract = _contract(capture.source_ref, dossier)
    fake = _FakePaperless(capture)

    result = intake_paperless_document(
        conn,
        contract,
        fake,
        paperless_document_id=42,
        paperless_version_id="7",
        ingestion_id="paperless-intake-1",
        docling=_FakeDocling(),
    )

    assert fake.calls == [(42, "7")]
    assert result["chunks_ingested"] == 1
    assert result["document"]["source_ref"] == capture.source_ref
    assert result["document"]["analysis_status"] == "ready"
    assert result["document"]["extraction"]["converter"] == "docling_serve"
    assert result["source_capture"]["storage_reference"] == capture.storage_reference
    assert result["source_capture"]["content_hash"] == capture.content_hash
    assert result["authority"] == {
        "source": True,
        "knowledge": False,
        "evidence": False,
        "professional_validation": False,
    }

    binding = get_binding(conn, result["document"]["document_id"])
    assert binding["backing_resource"] == "paperless_ngx"
    assert binding["external_document_id"] == 42
    assert binding["external_version_id"] == "7"
    assert binding["storage_reference"] == capture.storage_reference
    assert binding["content_hash"] == capture.content_hash


def test_same_paperless_version_can_back_documents_in_multiple_projects(conn):
    capture = _capture(document_id=55, version_id="3")
    fake = _FakePaperless(capture)
    results = []

    for suffix in ("a", "b"):
        dossier = f"project-paperless-{suffix}-{uuid.uuid4().hex}"
        results.append(
            intake_paperless_document(
                conn,
                _contract(capture.source_ref, dossier),
                fake,
                paperless_document_id=55,
                paperless_version_id="3",
                ingestion_id=f"paperless-multi-{suffix}",
                docling=_FakeDocling(),
            )
        )

    assert results[0]["document"]["document_id"] != results[1]["document"]["document_id"]
    for result in results:
        binding = get_binding(conn, result["document"]["document_id"])
        assert binding["external_document_id"] == 55
        assert binding["external_version_id"] == "3"
        assert binding["storage_reference"] == capture.storage_reference


def test_paperless_capability_does_not_expand_task_contract_scope(conn):
    capture = _capture(document_id=84, version_id="2")
    dossier = f"project-paperless-scope-{uuid.uuid4().hex}"
    contract = _contract("paperless/other/versions/1/declared.pdf", dossier)
    fake = _FakePaperless(capture)

    with pytest.raises(ContractError, match="outside declared perimeter"):
        intake_paperless_document(
            conn,
            contract,
            fake,
            paperless_document_id=84,
            paperless_version_id="2",
            docling=_FakeDocling(),
        )

    with conn.cursor() as cur:
        cur.execute(
            "SELECT COUNT(*) FROM source_documents WHERE dossier = %s",
            (dossier,),
        )
        assert cur.fetchone()[0] == 0
