from __future__ import annotations

from pathlib import Path
import shutil
import subprocess

import pytest


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
MOTION = COCKPIT / "collection" / "motion_adapter.js"
BOOTSTRAP = COCKPIT / "live_bootstrap.js"
ADAPTER = COCKPIT / "live_collection_adapter.js"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_mobile_swiper_motion_javascript_parses() -> None:
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is unavailable; JavaScript syntax check skipped")
    result = subprocess.run(
        [node, "--input-type=module", "--check"],
        input=_read(MOTION),
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr


def test_compact_mobile_cards_use_existing_swiper_owner_with_fraction_position() -> None:
    motion = _read(MOTION)
    adapter = _read(ADAPTER)

    assert 'const MOBILE_QUERY = "(max-width: 620px)";' in motion
    assert 'pagination.className = "swiper-pagination swiper-pagination-fraction v3-mobile-card-pagination"' in motion
    assert 'type: "fraction"' in motion
    assert "pagination.hidden = !mobile.matches || count < 2" in motion
    assert "threshold: 6" in motion
    assert "resistanceRatio: .62" in motion
    assert "watchOverflow: true" in motion
    assert "mobile.addEventListener?.(\"change\", onMobileChange)" in motion
    assert "mobile.removeEventListener?.(\"change\", onMobileChange)" in motion

    assert "createResponsiveMotion({" in adapter
    assert "new window.Swiper" not in adapter
    assert "swiper-pagination" not in adapter


def test_mobile_swiper_preserves_windowing_vertical_navigation_and_fail_closed_fallback() -> None:
    motion = _read(MOTION)
    bootstrap = _read(BOOTSTRAP)

    assert "addSlidesBefore: 1" in motion
    assert "addSlidesAfter: 1" in motion
    assert "cache: false" in motion
    assert 'direction: "vertical"' in motion
    assert 'document.documentElement.dataset.cockpitNavigation = swiperReady ? "swiper" : "fallback"' in bootstrap
    assert 'for (const id of ["v2-previous", "v2-next"])' in bootstrap
    assert "control.hidden = false" in bootstrap


def test_workspace_inventory_is_not_reinterpreted_as_the_governed_card_carousel() -> None:
    workspace = ROOT / "workspace_cockpit" / "static"
    index = (workspace / "index.html").read_text(encoding="utf-8")
    app = (workspace / "app.js").read_text(encoding="utf-8")

    assert "swiper" not in index.lower()
    assert "new window.Swiper" not in app
    assert "workspace-tabs" in index
    assert "status-filters" in index
