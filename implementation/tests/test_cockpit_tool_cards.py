from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
PROJECTION = COCKPIT / "projection" / "cockpit_projection.js"
TOOL_GOVERNANCE = COCKPIT / "projection" / "tool_governance_projection.js"
ASSEMBLER = COCKPIT / "projection" / "child_collection_assembler.js"
DATA_LOADER = COCKPIT / "data" / "cockpit_data_loader.js"
BOOTSTRAP = COCKPIT / "live_bootstrap.js"


def test_tool_space_is_driven_by_catalogue_not_legacy_static_containers():
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
    exact_projection = TOOL_GOVERNANCE.read_text(encoding="utf-8")

    for label in (
        "Installation",
        "État natif",
        "Santé observée",
        "Gouvernance",
        "Mise à jour",
        "Permissions",
        "Evidence attendue",
        "Rollback",
        "Prochaine décision humaine",
    ):
        assert label in renderer

    for label in (
        "Binding exact",
        "Release immuable",
        "Activation",
        "Scope d’activation",
        "Compatibilité observée",
        "Sécurité qualifiée",
        "Fraîcheur observation",
        "Source observation",
    ):
        assert label in exact_projection

    assert 'item.governance_state === "candidate"' in renderer
    assert 'item.health_state === "observed_ready"' in renderer
    assert "runtime non observé ≠ non installé" in renderer


def test_exact_capability_projection_never_infers_authority():
    exact_projection = TOOL_GOVERNANCE.read_text(encoding="utf-8")
    bootstrap = BOOTSTRAP.read_text(encoding="utf-8")

    assert '"projection/tool_governance_projection.js"' in bootstrap
    assert "item.binding_id" in exact_projection
    assert "item.implementation_anchor" in exact_projection
    assert "item.activation_scope" in exact_projection
    assert "item.compatibility_status" in exact_projection
    assert "item.safety_status" in exact_projection
    assert "item.freshness_status" in exact_projection
    assert '"not_observed"' in exact_projection
    assert "binding sélectionné ≠ dépendance adoptée" in exact_projection
    assert "compatible ≠ activé" in exact_projection
    assert "UI projetée ≠ autorisation" in exact_projection


def test_tool_catalog_failure_does_not_invent_runtime_absence():
    renderer = PROJECTION.read_text(encoding="utf-8")
    data_loader = DATA_LOADER.read_text(encoding="utf-8")

    assert 'title: "Catalogue indisponible"' in renderer
    assert "Catalogue absent ≠ outil absent" in renderer
    assert "state.toolCatalog = await dataLoader.loadToolCatalog()" in renderer
    assert "return []" in data_loader
