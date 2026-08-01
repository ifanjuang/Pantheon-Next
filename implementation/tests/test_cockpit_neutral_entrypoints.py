from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


def test_canonical_page_uses_responsibility_named_entrypoint() -> None:
    html = (COCKPIT / "index.html").read_text(encoding="utf-8")
    assert 'src="cockpit_bootstrap.js"' in html
    assert 'src="v3_bootstrap.js"' not in html


def test_neutral_entrypoint_chain_is_complete() -> None:
    cockpit = (COCKPIT / "cockpit_bootstrap.js").read_text(encoding="utf-8")
    live = (COCKPIT / "live_bootstrap.js").read_text(encoding="utf-8")
    assert 'import("./live_bootstrap.js")' in cockpit
    assert 'import("./shell_controls.js")' in cockpit
    assert 'import("./live_collection_adapter.js")' in live


def test_generation_named_entrypoint_files_are_retired() -> None:
    for filename in ("v3_bootstrap.js", "v2_bootstrap.js", "v3_swiper.js", "v2_shell_controls.js"):
        assert not (COCKPIT / filename).exists(), filename
