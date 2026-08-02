from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
PROJECTION = COCKPIT / "projection" / "cockpit_projection.js"
ASSEMBLER = COCKPIT / "projection" / "child_collection_assembler.js"
DATA_LOADER = COCKPIT / "data" / "cockpit_data_loader.js"


def test_v2_tool_space_is_driven_by_catalogue_not_legacy_static_containers():
    renderer = PROJECTION.read_text(encoding="utf-8")
    assembler = ASSEMBLER.read_text(encoding="utf-8")
    data_loader = DATA_LOADER.read_text(encoding="utf-8")

    assert 'loadOptionalCollection("tool_catalog.json", "items")' in data_loader
    assert "dataLoader.loadToolCatalog()" in renderer
    assert "state.toolCatalog" in renderer
    assert "state.toolCatalog.map(normalizeTool)" in renderer
    assert 'entity_id: `tool:${item.tool_id}`' in renderer
    assert "tools(context)" in assembler
    assert "return context.buildToolCards();" in assembler
    assert 'entity_id: "tools:capabilities"' not in renderer
    assert 'entity_id: "tools:hosts"' not in renderer


def test_tool_cards_keep_governance_axes_visibly_separate():
    renderer = PROJECTION.read_text(encoding="utf-8")

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

    assert 'item.governance_state === "candidate"' in renderer
    assert 'item.health_state === "observed_ready"' in renderer
    assert "runtime non observé ≠ non installé" in renderer


def test_tool_catalog_failure_does_not_invent_runtime_absence():
    renderer = PROJECTION.read_text(encoding="utf-8")
    data_loader = DATA_LOADER.read_text(encoding="utf-8")

    assert 'title: "Catalogue indisponible"' in renderer
    assert "Catalogue absent ≠ outil absent" in renderer
    assert "state.toolCatalog = await dataLoader.loadToolCatalog()" in renderer
    assert "return []" in data_loader
