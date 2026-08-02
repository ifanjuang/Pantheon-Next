"""The existing Document card exposes structured diagnostics without a new card family."""

from pathlib import Path


def test_document_verso_projects_structured_extraction_diagnostics() -> None:
    renderer = (
        Path(__file__).resolve().parents[1]
        / "mvp_vertical"
        / "cockpit"
        / "projection"
        / "cockpit_projection.js"
    ).read_text(encoding="utf-8")

    assert "const structured = item.structured_extraction || {};" in renderer
    assert '["Extraction structurée", text(structured.status' in renderer
    assert '["Pages / tableaux"' in renderer
    assert '["Anomalies", text(structured.anomaly_count' in renderer
    assert "subject_tags: item.subject_tags || item.tags || []" in renderer
    assert 'entity_type: "document"' in renderer
