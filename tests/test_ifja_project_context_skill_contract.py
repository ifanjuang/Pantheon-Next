from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "templates/hermes/skills/ifja-project-context"
SKILL = SKILL_ROOT / "SKILL.md"
PROJECT_RESOLUTION = SKILL_ROOT / "references/project-resolution.md"
DOCUMENT_INSPECTION = SKILL_ROOT / "references/document-inspection.md"
SOURCE_ROUTING = SKILL_ROOT / "references/professional-source-routing.md"
REGISTRY = ROOT / "templates/TEMPLATE_REGISTRY.md"


def test_project_context_is_document_neutral_and_source_first() -> None:
    assert SKILL.is_file()
    assert PROJECT_RESOLUTION.is_file()
    assert DOCUMENT_INSPECTION.is_file()
    assert SOURCE_ROUTING.is_file()

    text = SKILL.read_text(encoding="utf-8")
    routing = SOURCE_ROUTING.read_text(encoding="utf-8")
    assert "name: ifja-project-context" in text
    assert "status: candidate_template_only" in text
    assert "Use one document-neutral route" in text
    assert "Hindsight router first" in text
    assert "do not convert, OCR, inspect images or transcribe media by default" in text
    assert "Hindsight recall != source authority" in text
    assert "memory answer != Evidence" in text
    assert "professional-source-routing.md" in text
    assert "hindsight-kroqi-project:recall_project_memory" in routing
    assert "ifja-vault-read" in routing
    assert "native text or structured data first" in routing
    assert "dossier/client/address/budget/date/status/planning -> AFFAIRES" in routing
    assert "technical/standard/regulatory/legal/method question -> DOCUMENTAIRES" in routing
    assert "mentioned != exact source present != relevant content inspected" in routing

    registry = REGISTRY.read_text(encoding="utf-8")
    assert registry.count("templates/hermes/skills/ifja-project-context/SKILL.md") == 1


def test_project_resolution_keeps_alias_continuity_and_identity_bounded() -> None:
    text = PROJECT_RESOLUTION.read_text(encoding="utf-8")
    for invariant in (
        "User statements take precedence over earlier assistant wording",
        "alias match != governed identity",
        "folder name != governed identity",
        "conversation continuity != durable persistence",
    ):
        assert invariant in text


def test_document_inspection_separates_reference_presence_and_inspection() -> None:
    text = DOCUMENT_INSPECTION.read_text(encoding="utf-8")
    for invariant in (
        "mentioned != exact source present",
        "exact source present != relevant content inspected",
        "Hindsight recall != document inspected",
        "metadata != document content",
        "parser success != professional validation",
    ):
        assert invariant in text
