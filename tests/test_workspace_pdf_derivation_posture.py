"""Regression checks for the converged PDF/Markdown/Hindsight workspace posture."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OCR_PIPELINE = ROOT / "docs" / "governance" / "DOCUMENT_OCR_DERIVATION_PIPELINE.md"
OBSIDIAN = ROOT / "docs" / "governance" / "OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md"
APU_READ = ROOT / "implementation" / "mvp_vertical" / "apu_object_read.py"


def test_manual_marker_workspace_path_does_not_become_second_structural_owner() -> None:
    text = OCR_PIPELINE.read_text(encoding="utf-8")

    for invariant in (
        "OCR-AI / L3-N0X/obsidian-marker = selected optional/manual workspace PDF-to-Markdown convenience surface",
        "Docling = preferred document_structural_analysis candidate under #662",
        "Marker workspace selection != structural-analysis qualification",
        "Marker Markdown != original source",
        "no Markdown derivative != source unavailable",
    ):
        assert invariant in text

    assert "SourceDown = selected workspace conversion surface" not in text
    assert "SourceDown = historical prior workspace choice, not the current selected daily conversion surface" in text


def test_hindsight_keeps_one_markdown_producer_and_does_not_require_native_pdf_ingestion() -> None:
    ocr = OCR_PIPELINE.read_text(encoding="utf-8")
    obsidian = OBSIDIAN.read_text(encoding="utf-8")

    for invariant in (
        "Hindsight native file retain = not selected in the current qualified workspace producer path",
        "Do not simultaneously activate a second native-PDF Hindsight producer for the same source",
        "Obsidian Markdown\n-> designated hindsight-obsidian-sync producer\n-> Hindsight derived bank",
    ):
        assert invariant in ocr

    assert "hindsight-obsidian-sync  = qualified designated ingestion producer" in obsidian
    assert "Hindsight\n= derived retrieval / associative memory" in obsidian


def test_workspace_metadata_remains_distinct_from_document_authority() -> None:
    text = OCR_PIPELINE.read_text(encoding="utf-8")

    for invariant in (
        "detected index != admitted Document version",
        "highest-looking index != purpose-specific currentness",
        "date printed in document != receipt date",
        "date printed in document != effective date",
        "human note != extracted fact",
        "derived summary != Evidence",
        "No new production `document.yaml` or workspace-metadata schema is adopted by this posture.",
    ):
        assert invariant in text

    assert "index_candidates:" in text
    assert "date_candidates:" in text
    assert "based_on_digest:" in text


def test_project_anatomy_is_not_mirrored_into_markdown_for_hindsight() -> None:
    text = OCR_PIPELINE.read_text(encoding="utf-8")
    apu_read = APU_READ.read_text(encoding="utf-8")

    for invariant in (
        "Do not make Markdown or Hindsight the universal interchange format for structured project state.",
        "Observation Bundle",
        "Project Anatomy stable_objects",
        "Project Anatomy attribute_claims",
        "Project Anatomy relation_claims",
        "Projet.md != Project Anatomy",
        "projection != persistence",
    ):
        assert invariant in text

    assert "canonical Observation Bundle" in text
    assert "Hermes may read admitted Project Anatomy through its bounded Project Anatomy context seam." in text
    assert '"projection_only": True' in apu_read
    assert '"is_memory": False' in apu_read
