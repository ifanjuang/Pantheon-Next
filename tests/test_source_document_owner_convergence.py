from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_document_knowledge_contract_keeps_machine_boundary_and_drops_client_owner():
    text = _read("docs/governance/DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md")
    schema = _read("schemas/document_knowledge_slice.schema.yaml")

    assert "OpenWebUI" not in text
    assert "schemas/document_knowledge_slice.schema.yaml" in text
    for family in (
        "source_document",
        "extraction",
        "document_structure",
        "chunk[]",
        "project_document_card",
        "knowledge_publication[]",
        "version_event[]",
    ):
        assert family in text
    assert "Pantheon Cockpit" in text
    assert "runtime success != approval" in text
    assert "automatic_evidence_admission: false" in schema
    assert "memory_promotion: false" in schema
    assert "automatic_approval: false" in schema


def test_source_ingestion_model_is_provider_and_client_agnostic():
    text = _read("docs/governance/SOURCE_INGESTION_RETRIEVAL_MODEL.md")
    assert "OpenWebUI" not in text
    assert "ifanjuang/pantheon-mvp" not in text
    assert "linked != approved" in text
    assert "cached != retained" in text
    assert "ingested != Evidence" in text
    assert "retrieved != true" in text
    assert "provider selected != authority transfer" in text
    assert "Direct source/context access is valid when sufficient" in text
    assert "Pantheon Cockpit" in text


def test_layered_record_model_preserves_seven_distinct_layers():
    text = _read("docs/governance/RAW_DERIVED_GOVERNED_RECORDS.md")
    assert "OpenWebUI" not in text
    for label in (
        "1. Raw content",
        "2. Derived content",
        "3. Governed records",
        "4. Retrieval objects",
        "5. Provenance objects",
        "6. Evidence objects",
        "7. Approval and decision records",
    ):
        assert label in text
    assert "projection != persistence" in text
    assert "retrieval score != authority" in text
    assert "runtime completion != authorization" in text
