from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "templates/hermes/skills/ifja-project-context/SKILL.md"
REGISTRY = ROOT / "templates/TEMPLATE_REGISTRY.md"


def test_ifja_project_context_routes_existing_sources_without_new_authority():
    assert SKILL.is_file()

    text = SKILL.read_text(encoding="utf-8")
    assert "name: ifja-project-context" in text
    assert "status: candidate_template_only" in text
    assert "governed_by: docs/governance/HERMES_INTEGRATION.md" in text

    assert "Hindsight recall != source authority" in text
    assert "Use `AFFAIRES` for dossier-specific material" in text
    assert "Use `DOCUMENTAIRES` for transversal professional references" in text
    assert "consult `AFFAIRES` and `DOCUMENTAIRES` in parallel" in text
    assert "Prefer the professional workspace before external research" in text
    assert "reuse the existing `source-research` skill/capability" in text
    assert "Prefer an abstracted query" in text

    assert "using `classify_request` when that remains the exposed contract" in text
    assert "Do not derive K/V/C" in text
    assert "Do not call Pantheon mechanically for trivial consultation" in text

    assert "Do not hard-code filesystem paths, Hindsight bank IDs or provider-specific names" in text
    assert "retrieved != truth" in text
    assert "Hindsight != Evidence" in text
    assert "runtime success != authorization" in text
    assert "projection != persistence" in text

    registry = REGISTRY.read_text(encoding="utf-8")
    skill_path = "templates/hermes/skills/ifja-project-context/SKILL.md"
    assert registry.count(skill_path) == 1
