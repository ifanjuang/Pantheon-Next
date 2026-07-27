from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


def test_v2_tool_space_is_driven_by_catalogue_not_legacy_static_containers():
    renderer = (COCKPIT / "v2_app_schema.js").read_text(encoding="utf-8")

    assert 'fetch("tool_catalog.json", { cache: "no-store" })' in renderer
    assert "state.toolCatalog" in renderer
    assert "state.toolCatalog.map(normalizeTool)" in renderer
    assert 'entity_id: `tool:${item.tool_id}`' in renderer
    assert 'setChildren("space:outils", tools.map(item => item.entity_id))' in renderer
    assert 'entity_id: "tools:capabilities"' not in renderer
    assert 'entity_id: "tools:hosts"' not in renderer


def test_tool_cards_keep_governance_axes_visibly_separate():
    renderer = (COCKPIT / "v2_app_schema.js").read_text(encoding="utf-8")

    for label in (
        "Installation",
        "État natif",
        "Santé observée",
        "Gouvernance",
        "Activation scope",
        "Mise à jour",
        "Permissions",
        "Evidence attendue",
        "Rollback",
        "Prochaine décision humaine",
    ):
        assert label in renderer

    assert "item.governance_state === \"candidate\"" in renderer
    assert "item.health_state === \"observed_ready\"" in renderer
    assert "runtime non observé ≠ non installé" in renderer


def test_tool_catalog_failure_does_not_invent_runtime_absence():
    renderer = (COCKPIT / "v2_app_schema.js").read_text(encoding="utf-8")

    assert 'title: "Catalogue indisponible"' in renderer
    assert "Catalogue absent ≠ outil absent" in renderer
    assert "state.toolCatalog = []" in renderer
