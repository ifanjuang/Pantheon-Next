from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = ROOT / "tools" / "check_architecture_debt_baseline.py"


def _load_tool():
    name = "check_architecture_debt_baseline"
    spec = importlib.util.spec_from_file_location(name, TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _route() -> str:
    return "/" + "v1" + "/items"


def _inventory(*, generation: bool = True, route: bool = True):
    return {
        "artifacts": [
            {
                "repository": "pantheon-mvp",
                "path": "pkg/feature.py",
                "posture": "implementation",
                "generation_named": generation,
                "routes": [f"GET {_route()}"] if route else [],
                "versioned_routes": [_route()] if route else [],
            },
            {
                "repository": "Pantheon-Next",
                "path": "ai_logs/history-v2.md",
                "posture": "history",
                "generation_named": True,
                "routes": [],
                "versioned_routes": [],
            },
        ]
    }


def _baseline(tmp_path: Path, *, generation: bool = True, route: bool = True) -> Path:
    path = tmp_path / "baseline.json"
    path.write_text(
        json.dumps(
            {
                "baseline_id": "pantheon.architecture_debt",
                "revision": 1,
                "status": "active_decreasing_baseline",
                "allowed": {
                    "generation_named_artifacts": (
                        ["pantheon-mvp:pkg/feature.py"] if generation else []
                    ),
                    "internal_versioned_routes": (
                        {
                            "pantheon-mvp:pkg/feature.py": [
                                ["v1", "items"]
                            ]
                        }
                        if route
                        else {}
                    ),
                },
            }
        ),
        encoding="utf-8",
    )
    return path


def test_matching_baseline_passes_and_excludes_history(tmp_path: Path) -> None:
    tool = _load_tool()
    current = tool.collect_debt(_inventory())
    baseline = tool.load_baseline(_baseline(tmp_path))

    assert tool.compare(current, baseline) == []
    assert current.generation_named_artifacts == ("pantheon-mvp:pkg/feature.py",)


def test_new_debt_fails_even_inside_known_file(tmp_path: Path) -> None:
    tool = _load_tool()
    inventory = _inventory()
    inventory["artifacts"][0]["versioned_routes"].append(
        "/" + "v1" + "/items/{item_id}"
    )
    current = tool.collect_debt(inventory)
    baseline = tool.load_baseline(_baseline(tmp_path))

    errors = tool.compare(current, baseline)
    assert any("new internal versioned routes" in error for error in errors)


def test_resolved_debt_requires_baseline_reduction(tmp_path: Path) -> None:
    tool = _load_tool()
    current = tool.collect_debt(_inventory(generation=False, route=False))
    baseline = tool.load_baseline(_baseline(tmp_path))

    errors = tool.compare(current, baseline)
    assert any("resolved generation debt" in error for error in errors)
    assert any("resolved versioned routes" in error for error in errors)


def test_route_catalogue_is_deterministic() -> None:
    tool = _load_tool()
    first = tool.route_catalogue(_inventory())
    second = tool.route_catalogue(_inventory())

    assert first == second
    assert first["route_declarations"] == 1
