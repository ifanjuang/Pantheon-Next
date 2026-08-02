from __future__ import annotations

import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"


def test_cockpit_runtime_subdirectories_are_packaged() -> None:
    config = tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))
    patterns = set(config["tool"]["setuptools"]["package-data"]["mvp_vertical"])

    required = {
        "cockpit/actions/*",
        "cockpit/boot/*",
        "cockpit/context/*",
        "cockpit/handoff/*",
        "cockpit/interactions/*",
        "cockpit/navigation/*",
        "cockpit/projection/*",
        "cockpit/registries/*",
        "cockpit/rendering/*",
        "cockpit/shell/*",
        "cockpit/styles/*",
        "cockpit/v3/*",
        "cockpit/v3/collection/*",
        "cockpit/v3/providers/*",
    }

    assert required <= patterns
