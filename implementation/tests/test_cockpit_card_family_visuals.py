from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


def test_project_card_visual_is_family_scoped_and_loaded_after_shared_cards() -> None:
    html = (COCKPIT / "index.html").read_text(encoding="utf-8")
    css = (COCKPIT / "styles" / "v3_card_project.css").read_text(encoding="utf-8")

    shared = 'href="styles/v3_living_cards.css"'
    project = 'href="styles/v3_card_project.css"'
    geometry = 'href="styles/v3_geometry.css"'

    assert shared in html
    assert project in html
    assert geometry in html
    assert html.index(shared) < html.index(project) < html.index(geometry)

    selector = '[data-cockpit-v3="living-card"][data-family="project"]'
    assert selector in css
    assert "data-family=\"information\"" not in css
    assert "data-family=\"tool\"" not in css
    assert "data-family=\"decision\"" not in css


def test_project_visual_does_not_change_card_dom_or_business_model() -> None:
    renderer = (COCKPIT / "v3" / "collection" / "card_renderer.js").read_text(encoding="utf-8")
    provider = (COCKPIT / "v3" / "providers" / "demo_provider.js").read_text(encoding="utf-8")

    assert "article.dataset.family = item.family" in renderer
    assert '"project"' in provider
    assert "v3_card_project" not in renderer
    assert "v3_card_project" not in provider
