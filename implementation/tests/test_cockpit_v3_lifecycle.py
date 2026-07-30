"""Architecture budgets for the cockpit navigation core.

These are static guards, not runtime measurements: they pin the contracts so a
later edit cannot quietly reintroduce a Swiper-shaped cockpit or mount a whole
collection into the DOM again.

Contracts:
  - Swiper exists in exactly one module (the MotionAdapter);
  - the cockpit never calls Swiper's slide APIs directly;
  - the mounted DOM window is bounded and does not grow with the collection;
  - an already-resident array is applied at once, never faked as a stream;
  - a superseded async load cannot append into the replacement collection.
"""

from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
ADAPTER = "v3/collection/motion_adapter.js"
COLLECTION_PROVIDER = COCKPIT / "v3" / "collection" / "collection_provider.js"

# Every cockpit module that must stay free of Swiper.
SWIPER_FREE = (
    "v3/collection/navigation_state.js",
    "v3/collection/collection_provider.js",
    "v3/collection/collection_controller.js",
    "v3/collection/level_controller.js",
    "v3/collection/card_renderer.js",
    "v3/demo_collection_app.js",
)


def _read(rel: str) -> str:
    return (COCKPIT / rel).read_text(encoding="utf-8")


def _run_module(body: str) -> subprocess.CompletedProcess[str]:
    node = shutil.which("node")
    if node is None:  # pragma: no cover - depends on the runner image
        pytest.skip("Node.js is unavailable; JavaScript behavior check skipped")
    return subprocess.run(
        [node, "--input-type=module", "-e", body],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def test_swiper_is_confined_to_the_motion_adapter() -> None:
    adapter = _read(ADAPTER)
    assert "new window.Swiper" in adapter

    for rel in SWIPER_FREE:
        source = _read(rel)
        assert "new window.Swiper" not in source, rel
        assert "new Swiper(" not in source, rel


def test_cockpit_never_drives_swiper_slide_apis_directly() -> None:
    # These belong to the adapter alone, so the engine stays replaceable.
    for rel in SWIPER_FREE + ("v3_swiper.js",):
        source = _read(rel)
        for forbidden in ("appendSlide", "removeAllSlides", "updateSlides", "slideTo(", "slidePrev(", "slideNext("):
            assert forbidden not in source, f"{rel} calls {forbidden}"


def test_mounted_window_is_bounded_independently_of_collection_size() -> None:
    adapter = _read(ADAPTER)

    # Swiper Virtual keeps a windowed slice of the collection in the DOM instead
    # of mounting every sibling. Measured in Chromium on a 43-item collection:
    # the DOM window peaks at 5 slides and does not grow with the collection
    # (see docs/architecture/cockpit-navigation-lifecycle.md).
    assert "virtual" in adapter
    assert "addSlidesBefore: 1" in adapter
    assert "addSlidesAfter: 1" in adapter
    assert "cache: false" in adapter


def test_resident_arrays_are_not_fake_streamed() -> None:
    provider = _read("v3/collection/collection_provider.js")

    assert "isAsyncIterable" in provider
    assert "Symbol.asyncIterator" in provider
    # An array must be applied in one go, with no per-frame drip.
    assert "requestAnimationFrame" not in provider


def test_superseded_async_load_cannot_pollute_replacement_collection() -> None:
    result = _run_module(
        f"""
        import {{ loadCollection }} from {json.dumps(COLLECTION_PROVIDER.as_uri())};

        const model = {{ collectionId: null, items: [], loading: false }};
        const state = {{
          setCollection(next) {{
            model.collectionId = next.collectionId;
            model.items = [...next.items];
            model.loading = next.loading;
          }},
          appendItems(items) {{ model.items.push(...items); }},
          setLoading(value) {{ model.loading = value; }},
        }};

        async function* staleStream() {{
          yield {{ id: "stale-first" }};
          await new Promise(resolve => setTimeout(resolve, 25));
          yield {{ id: "stale-late" }};
        }}

        const cancel = loadCollection(
          state,
          {{ spaceId: "agency", id: "stale" }},
          staleStream(),
          0,
        );

        await new Promise(resolve => setTimeout(resolve, 5));
        cancel();
        loadCollection(
          state,
          {{ spaceId: "agency", id: "current" }},
          [{{ id: "current-only" }}],
          0,
        );
        await new Promise(resolve => setTimeout(resolve, 50));

        if (model.collectionId !== "current") throw new Error("stale collection replaced the current identity");
        if (model.loading) throw new Error("cancelled stream changed the current loading state");
        if (model.items.length !== 1 || model.items[0].id !== "current-only") {{
          throw new Error(`stale stream polluted replacement collection: ${{JSON.stringify(model.items)}}`);
        }}
        """
    )
    assert result.returncode == 0, result.stderr


def test_new_card_stays_swipeable() -> None:
    renderer = _read("v3/collection/card_renderer.js")
    adapter = _read(ADAPTER)

    # The synthetic `New` card fills its whole slide. Rendering it as a <button>
    # (matched by noSwipingSelector) or tagging it `swiper-no-swiping` makes
    # Swiper refuse every gesture starting on it, trapping the user on that card
    # with no way back. It must navigate like any other card.
    new_card = renderer[renderer.index("export function renderNewSlide"):]
    new_card = new_card[: new_card.index("\nexport function")] if "\nexport function" in new_card else new_card
    code = "\n".join(line for line in new_card.splitlines() if not line.lstrip().startswith("//"))

    assert 'createElement("button")' not in code
    assert "swiper-no-swiping" not in code
    assert 'role", "button"' in code  # still announced as activatable
    assert "noSwipingSelector" in adapter  # the selector that made <button> fatal


def test_demo_html_targets_the_single_cockpit_page() -> None:
    demo_html = _read("demo.html")
    assert "index.html?mode=demo" in demo_html
    assert "v2.html?mode=demo" not in demo_html
