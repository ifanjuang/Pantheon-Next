from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "templates/hermes/skills/ifja-project-context"
SKILL = SKILL_ROOT / "SKILL.md"
PROJECT_RESOLUTION = SKILL_ROOT / "references/project-resolution.md"
DOCUMENT_INSPECTION = SKILL_ROOT / "references/document-inspection.md"
REGISTRY = ROOT / "templates/TEMPLATE_REGISTRY.md"


def test_ifja_project_context_routes_existing_sources_without_new_authority():
    assert SKILL.is_file()
    assert PROJECT_RESOLUTION.is_file()
    assert DOCUMENT_INSPECTION.is_file()

    text = SKILL.read_text(encoding="utf-8")
    assert "name: ifja-project-context" in text
    assert "status: candidate_template_only" in text
    assert "governed_by: docs/governance/HERMES_INTEGRATION.md" in text

    assert "Hindsight recall != source authority" in text
    assert "bounded candidate set" in text
    assert "do not silently merge or select an identity" in text
    assert "conversation-local working referent" in text
    assert "references/project-resolution.md" in text
    assert "`AFFAIRES` -> dossier-specific" in text
    assert "`DOCUMENTAIRES` -> transversal" in text
    assert "consult both in parallel" in text
    assert "### 2. Workspace first" in text
    assert "mentioned != exact source present != relevant content inspected" in text
    assert "references/document-inspection.md" in text
    assert "reuse the existing `source-research` skill/capability" in text
    assert "prefer an abstracted query" in text

    assert "bounded HTTP policy service" in text
    assert "do not assume that the consultation-only MCP binding exposes classification" in text
    assert "return a Capability Gap" in text
    assert "Do not derive K/V/C" in text
    assert "Do not call Pantheon mechanically for trivial consultation" in text

    assert "do not hard-code filesystem paths, Hindsight bank IDs or provider-specific names" in text
    assert "retrieved != truth" in text
    assert "Hindsight != Evidence" in text
    assert "runtime success != authorization" in text
    assert "projection != persistence" in text

    registry = REGISTRY.read_text(encoding="utf-8")
    skill_path = "templates/hermes/skills/ifja-project-context/SKILL.md"
    assert registry.count(skill_path) == 1


def test_project_resolution_keeps_alias_continuity_and_identity_bounded():
    text = PROJECT_RESOLUTION.read_text(encoding="utf-8")

    assert "User statements take precedence over earlier assistant wording" in text
    assert "conversation-local working referent" in text
    assert "Ask for targeted clarification only when choosing between them would materially change" in text
    assert "conversation target != governed identity" in text
    assert "Hindsight lead != source confirmation" in text
    assert "A source-backed or governed identity is stronger confirmation than Hindsight recall" in text
    assert "The third case reopens resolution; it does not authorize an automatic switch" in text
    assert "alias match != governed identity" in text
    assert "folder name != governed identity" in text
    assert "conversation continuity != durable persistence" in text
    assert "confirm it against the admitted `AFFAIRES` source material" in text
    assert "Do not promote it into a permanent alias mapping" in text


def test_document_inspection_separates_reference_presence_and_inspection():
    text = DOCUMENT_INSPECTION.read_text(encoding="utf-8")

    for invariant in (
        "mentioned != exact source present",
        "exact source present != relevant content inspected",
        "Hindsight recall != document inspected",
        "Markdown derivative != exact source",
        "metadata != document content",
        "not retrieved != absent",
        "file listed != content inspected",
        "parser success != professional validation",
        "inspection result != Evidence admission",
    ):
        assert invariant in text

    assert "currently admitted document-analysis capability" in text
    assert "Do not hard-code Docling, Marker, OCR or another provider" in text
    assert "visual/document inspection path" in text
    assert "retain the exact source identity and page, section, anchor or other locator" in text
