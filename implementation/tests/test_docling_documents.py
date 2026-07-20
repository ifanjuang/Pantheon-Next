"""Docling document vertical: bounded conversion, persistence and card projection."""

from __future__ import annotations

import base64
import json
import uuid
from pathlib import Path

import pytest

from mvp_vertical import store
from mvp_vertical.contract import TaskContract
from mvp_vertical.documents import (
    ConvertedDocument,
    DoclingServeClient,
    DocumentConversionError,
    converter_for,
)


class _Response:
    def __init__(self, payload: dict) -> None:
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self) -> bytes:
        return json.dumps(self.payload).encode("utf-8")


def test_docling_client_sends_one_contained_file_and_parses_v1_response(tmp_path) -> None:
    source = tmp_path / "contrat.pdf"
    source.write_bytes(b"fictional-pdf")
    observed = {}

    def opener(request, *, timeout):
        observed["url"] = request.full_url
        observed["headers"] = dict(request.header_items())
        observed["payload"] = json.loads(request.data)
        observed["timeout"] = timeout
        return _Response(
            {
                "status": "success",
                "processing_time": 1.25,
                "document": {
                    "md_content": "# Contrat\n\nClause 1",
                    "json_content": {"schema_name": "DoclingDocument", "texts": []},
                },
                "errors": [],
            }
        )

    client = DoclingServeClient(
        "http://docling.internal:5001",
        api_key="secret",
        opener=opener,
    )
    converted = client.convert(source)

    assert observed["url"] == "http://docling.internal:5001/v1/convert/source"
    assert observed["headers"]["X-api-key"] == "secret"
    sent = observed["payload"]
    assert len(sent["file_sources"]) == 1
    assert sent["file_sources"][0]["filename"] == "contrat.pdf"
    assert base64.b64decode(sent["file_sources"][0]["base64_string"]) == b"fictional-pdf"
    assert sent["options"]["to_formats"] == ["md", "json"]
    assert converted.markdown.startswith("# Contrat")
    assert converted.document_json["schema_name"] == "DoclingDocument"
    assert converted.status == "ready"


def test_docling_partial_success_is_visible_for_review(tmp_path) -> None:
    source = tmp_path / "scan.pdf"
    source.write_bytes(b"scan")
    client = DoclingServeClient(
        "http://127.0.0.1:5001",
        opener=lambda *_args, **_kwargs: _Response(
            {
                "status": "partial_success",
                "document": {"md_content": "Texte OCR", "json_content": {}},
            }
        ),
    )
    converted = client.convert(source)
    assert converted.status == "needs_review"
    assert converted.quality_flags == ("docling_partial_success",)


def test_binary_source_refuses_without_docling_adapter(tmp_path) -> None:
    source = tmp_path / "etude.pdf"
    source.write_bytes(b"pdf")
    with pytest.raises(DocumentConversionError, match="requires.*Docling"):
        converter_for(source, None)


class _FakeDocling:
    converter = "docling_serve"
    converter_version = "test-1"
    config_digest = "config-test"

    def __init__(self) -> None:
        self.calls = 0

    def convert(self, path: Path) -> ConvertedDocument:
        self.calls += 1
        return ConvertedDocument(
            markdown="# Etude structure\n\nPréconisation de reprise en sous-œuvre.",
            document_json={"schema_name": "DoclingDocument", "name": path.name},
            converter=self.converter,
            converter_version=self.converter_version,
            config_digest=self.config_digest,
        )


@pytest.fixture
def conn():
    try:
        connection = store.connect()
    except Exception as exc:  # pragma: no cover - unit-only local environment
        pytest.skip(f"PostgreSQL/pgvector unreachable: {exc}")
    yield connection
    connection.close()


def _contract(tmp_path: Path, source_ref: str, dossier: str) -> TaskContract:
    raw = {
        "object_type": "task_contract",
        "object_id": f"tc.{dossier}",
        "contract_id": f"tc.{dossier}",
        "scope": {"dossier": dossier, "declared_sources": [{"source_ref": source_ref}]},
    }
    return TaskContract(raw=raw, path=tmp_path / "tc.yaml", dossier=dossier, sources=(source_ref,))


def test_pdf_ingestion_persists_extraction_reuses_cache_and_projects_card(conn, tmp_path) -> None:
    dossier = f"project-{uuid.uuid4().hex}"
    source_ref = "nas/30_DCE/PROJET_A1_DCE_IFJ_ETUDE_STRUCTURE.pdf"
    path = tmp_path / source_ref
    path.parent.mkdir(parents=True)
    path.write_bytes(b"fictional-pdf-content")
    contract = _contract(tmp_path, source_ref, dossier)
    docling = _FakeDocling()

    assert store.ingest(
        conn, contract, tmp_path, ingestion_id="docling-first", docling=docling
    ) == 1
    assert docling.calls == 1

    # Same bytes + converter/version/config reuses the structured extraction,
    # while creating a new auditable ingestion run and chunk identity.
    assert store.ingest(
        conn, contract, tmp_path, ingestion_id="docling-second", docling=docling
    ) == 1
    assert docling.calls == 1

    card = store.get_document_card(conn, dossier, source_ref)
    assert card["card_type"] == "project_document"
    assert card["parent_project_id"] == dossier
    assert card["source_ref"] == source_ref
    assert card["analysis_status"] == "ready"
    assert card["extraction"]["converter"] == "docling_serve"
    assert card["extraction"]["chunk_count"] == 1
    assert "cache_reused" in card["extraction"]["quality_flags"]
    assert card["authority"] == {
        "is_source": False,
        "is_evidence": False,
        "is_memory": False,
    }

    with conn.cursor() as cur:
        cur.execute(
            "SELECT document_json FROM extraction_runs WHERE extraction_id = %s",
            (card["extraction"]["extraction_id"],),
        )
        assert cur.fetchone()[0]["schema_name"] == "DoclingDocument"


def test_failed_conversion_is_visible_without_deleting_previous_chunks(conn, tmp_path) -> None:
    dossier = f"project-{uuid.uuid4().hex}"
    source_ref = "nas/10_CONCEPTION/scan.pdf"
    path = tmp_path / source_ref
    path.parent.mkdir(parents=True)
    path.write_bytes(b"scan")
    contract = _contract(tmp_path, source_ref, dossier)

    class Failing(_FakeDocling):
        def convert(self, path: Path) -> ConvertedDocument:
            raise DocumentConversionError("OCR failed loudly")

    with pytest.raises(DocumentConversionError, match="OCR failed loudly"):
        store.ingest(conn, contract, tmp_path, ingestion_id="docling-failed", docling=Failing())

    card = store.get_document_card(conn, dossier, source_ref)
    assert card["analysis_status"] == "failed"
    assert "OCR failed loudly" in card["extraction"]["error"]
