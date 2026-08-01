from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
RENDERER = COCKPIT / "v2_app_schema.js"
CREATE_INFORMATION = COCKPIT / "information_create.js"
FAMILIES_CSS = COCKPIT / "styles" / "families.css"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_contacts_remain_one_grouped_card_with_scrollable_back() -> None:
    renderer = _text(RENDERER)
    css = _text(FAMILIES_CSS)

    assert 'entity_type: "project_contacts"' in renderer
    assert 'title: "Contacts"' in renderer
    assert 'values.map(contactDisplay).join("\\n")' in renderer
    assert '[data-family="contact"] .card-back-body {' in css
    assert 'overflow-y: auto;' in css


def test_change_candidate_decision_exposes_review_context() -> None:
    renderer = _text(RENDERER)

    assert 'category: "Décision · Modification"' in renderer
    assert '["Proposition", changes.map(candidateChangeLine).join("\\n")' in renderer
    assert '["Proposé par",' in renderer
    assert '["Révision de base",' in renderer
    assert '["Sources", (item.source_refs || []).join("\\n")' in renderer
    assert 'available_actions: item.status === "pending_review" ? ["Refuser", "Valider"] : []' in renderer


def test_tool_card_keeps_runtime_and_governance_axes_separate() -> None:
    renderer = _text(RENDERER)

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
        assert f'["{label}",' in renderer
    assert 'Catalogue absent ≠ outil absent · runtime non observé ≠ non installé.' in renderer


def test_known_gap_new_information_is_not_yet_a_spatial_child() -> None:
    renderer = _text(RENDERER)
    creator = _text(CREATE_INFORMATION)

    # Known UX gap tracked in #94: creation exists but is injected in the Project
    # back instead of participating in the Project child collection.
    assert 'body.append(blankCard())' in creator
    selected_children = 'setChildren(selectedCardId, [contactsId, ...informationIds, ...legacyIds, ...workIds]);'
    assert selected_children in renderer
    assert "new-information" not in selected_children


def test_known_gap_project_claim_provenance_is_stored_but_not_rendered() -> None:
    renderer = _text(RENDERER)

    # Known UX/projection gap tracked in #95. Project values already come from
    # claim_values, while claim_refs are not yet consumed by the Project renderer.
    assert 'item.claim_values?.[field.key]' in renderer
    project_rows = renderer[renderer.index("function projectSchemaRows"):renderer.index("function normalizeProject")]
    assert "claim_refs" not in project_rows
