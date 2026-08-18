"""Lifecycle guards for the live Cockpit map binding."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BINDING = ROOT / "mvp_vertical" / "cockpit" / "map_binding.js"
RENDERER = ROOT / "mvp_vertical" / "cockpit" / "rendering" / "card_renderer.js"
INDEX = ROOT / "mvp_vertical" / "cockpit" / "index.html"
CSS = ROOT / "mvp_vertical" / "cockpit" / "styles" / "cockpit.css"


def test_live_map_mounts_only_into_pantheon_verso_hosts_and_cleans_removed_hosts() -> None:
    source = BINDING.read_text(encoding="utf-8")

    assert '.card[data-family="pantheon"] [data-pantheon-map-lens]' in source
    assert "new MutationObserver(sync)" in source
    assert "window.PantheonMapMount.mountLive(svg, opts)" in source
    assert "state.mount.destroy();" in source
    assert "mounts.delete(lens);" in source


def test_canonical_pantheon_back_owns_the_map_lens() -> None:
    source = RENDERER.read_text(encoding="utf-8")

    assert "function renderPantheonMapLens()" in source
    assert 'lens.dataset.pantheonMapLens = "true"' in source
    assert 'svg.dataset.pantheonMap = "true"' in source
    assert '(model.presentation_family || model.family) === "pantheon"' in source
    assert "body.append(renderPantheonMapLens());" in source


def test_global_map_toggle_and_overlay_are_retired_from_the_shell() -> None:
    html = INDEX.read_text(encoding="utf-8")
    binding = BINDING.read_text(encoding="utf-8")

    for token in ("v2-map-toggle", "v2-map-panel", "v2-map-close"):
        assert token not in html
        assert token not in binding


def test_mobile_shell_hides_header_location_and_navigation_controls() -> None:
    source = CSS.read_text(encoding="utf-8")

    assert "@media (max-width: 620px)" in source
    assert ".v3-header,\n    .v2-location,\n    .v3-navigation-bridge { display: none; }" in source
    assert ".v3-shell {\n      grid-template-rows: minmax(0, 1fr);\n      gap: 0;\n    }" in source
    assert ".v3-stage { grid-row: 1; }" in source
