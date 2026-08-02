from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
LOADER = COCKPIT / "navigation" / "swiper_loader.js"
BOOTSTRAP = COCKPIT / "live_bootstrap.js"
MOTION = COCKPIT / "v3" / "collection" / "motion_adapter.js"


def test_swiper_acquisition_is_isolated_from_live_bootstrap() -> None:
    loader = LOADER.read_text(encoding="utf-8")
    bootstrap = BOOTSTRAP.read_text(encoding="utf-8")

    assert 'const SWIPER_VERSION = "14.0.7"' in loader
    assert "cdn.jsdelivr.net/npm/swiper" in loader
    assert "unpkg.com/swiper" in loader
    assert "export async function ensureSwiper" in loader
    assert 'import("./navigation/swiper_loader.js")' in bootstrap
    assert "await ensureSwiper()" in bootstrap

    for acquisition_detail in ("cdn.jsdelivr.net/npm/swiper", "unpkg.com/swiper", "SWIPER_VERSION", "loadExternalScript"):
        assert acquisition_detail not in bootstrap


def test_swiper_loader_acquires_library_but_never_constructs_navigation() -> None:
    loader = LOADER.read_text(encoding="utf-8")
    motion = MOTION.read_text(encoding="utf-8")

    assert "new window.Swiper" not in loader
    assert "new Swiper" not in loader
    assert "slideNext(" not in loader
    assert "slidePrev(" not in loader
    assert "new window.Swiper" in motion or "new Swiper" in motion


def test_swiper_loader_javascript_parses() -> None:
    node = shutil.which("node")
    if node is None:  # pragma: no cover
        pytest.skip("Node.js is unavailable")

    result = subprocess.run(
        [node, "--check", str(LOADER)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
