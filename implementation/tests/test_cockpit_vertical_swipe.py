"""Regression guards for compact vertical level navigation in the Cockpit."""

from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
MOTION = COCKPIT / "collection" / "motion_adapter.js"
CONTROLLER = COCKPIT / "collection" / "collection_controller.js"
LIVE_ADAPTER = COCKPIT / "live_collection_adapter.js"


def _run_module(body: str) -> subprocess.CompletedProcess[str]:
    node = shutil.which("node")
    if node is None:  # pragma: no cover - runner dependent
        pytest.skip("Node.js is unavailable; vertical swipe behavior check skipped")
    return subprocess.run(
        [node, "--input-type=module", "-e", body],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def test_compact_motion_emits_only_dominant_vertical_level_swipes() -> None:
    result = _run_module(
        f"""
        import {{ createWindowedMotion }} from {json.dumps(MOTION.as_uri())};

        class FakeElement {{
          constructor() {{
            this.children = [];
            this.className = "";
            this.dataset = {{}};
          }}
          append(...nodes) {{ this.children.push(...nodes); }}
          setAttribute() {{}}
          remove() {{}}
        }}

        let swiper = null;
        let callbacks = null;
        class FakeSwiper {{
          constructor(_shell, options) {{
            callbacks = options.on;
            swiper = this;
            this.activeIndex = 0;
            this.animating = false;
            this.slides = [];
            this.allowTouchMove = true;
            this.virtual = {{
              slides: [],
              update() {{}},
              appendSlide() {{}},
            }};
          }}
          slideTo(index) {{ this.activeIndex = index; }}
          slidePrev() {{ this.activeIndex = Math.max(0, this.activeIndex - 1); }}
          slideNext() {{ this.activeIndex += 1; }}
          destroy() {{}}
        }}

        globalThis.document = {{ createElement() {{ return new FakeElement(); }} }};
        globalThis.window = {{ Swiper: FakeSwiper }};

        const mount = new FakeElement();
        const levelMoves = [];
        const motion = createWindowedMotion({{
          mount,
          renderAt() {{ return null; }},
          onCrossAxisMove(delta, meta) {{ levelMoves.push([delta, meta.presentation]); }},
        }});
        motion.mount(3, 1);

        function gesture(startX, startY, endX, endY) {{
          callbacks.touchStart(swiper, {{ clientX: startX, clientY: startY }});
          callbacks.touchMoveOpposite(swiper, {{ clientX: endX, clientY: endY }});
          callbacks.touchEnd(swiper, {{ clientX: endX, clientY: endY }});
        }}

        gesture(100, 260, 104, 160); // finger up -> child
        gesture(100, 160, 96, 265);  // finger down -> parent
        gesture(100, 200, 210, 208); // horizontal -> sibling motion only
        gesture(100, 200, 102, 170); // vertical but below the level threshold

        const expected = JSON.stringify([[1, "compact"], [-1, "compact"]]);
        if (JSON.stringify(levelMoves) !== expected) {{
          throw new Error(`unexpected level moves: ${{JSON.stringify(levelMoves)}}`);
        }}
        """
    )
    assert result.returncode == 0, result.stderr


def test_vertical_swipe_reuses_projection_commands_without_second_navigation_state() -> None:
    motion = MOTION.read_text(encoding="utf-8")
    controller = CONTROLLER.read_text(encoding="utf-8")
    adapter = LIVE_ADAPTER.read_text(encoding="utf-8")

    assert "onCrossAxisMove" in motion
    assert "touchMoveOpposite" in motion
    assert 'presentation: "compact"' in motion

    assert "onCrossAxisMove" in controller
    assert "onCrossAxisMove(delta, { collection, ...meta })" in controller

    assert 'delta < 0 ? "v2-ascend" : "v2-descend"' in adapter
    assert "control.click()" in adapter
    assert "PantheonSpatialNavigation" not in adapter
    assert ".descend(" not in adapter
    assert ".ascend(" not in adapter


def test_demo_and_live_share_the_same_vertical_swipe_adapter() -> None:
    bootstrap = (COCKPIT / "live_bootstrap.js").read_text(encoding="utf-8")
    demo = (COCKPIT / "demo_bootstrap.js").read_text(encoding="utf-8")

    assert 'if (isDemo) await import("./demo_bootstrap.js")' in bootstrap
    assert 'await import("./live_collection_adapter.js")' in bootstrap
    assert "live_collection_adapter" not in demo
    assert "createWindowedMotion" not in demo
