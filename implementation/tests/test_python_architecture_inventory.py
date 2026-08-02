from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = ROOT / "tools" / "audit_python_architecture.py"


def _load_tool():
    module_name = "audit_python_architecture"
    spec = importlib.util.spec_from_file_location(module_name, TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def test_inventory_detects_imports_routes_and_version_named_paths(tmp_path: Path) -> None:
    tool = _load_tool()
    package = tmp_path / "sample"
    package.mkdir()
    (package / "service.py").write_text(
        "from fastapi import APIRouter\n"
        "router = APIRouter()\n"
        "@router.get('/items')\n"
        "def list_items():\n"
        "    return []\n",
        encoding="utf-8",
    )
    versioned = package / "v2_adapter.py"
    versioned.write_text("import sample.service\n", encoding="utf-8")

    records = [tool.inspect_file(tmp_path, path) for path in tool.iter_python_files(tmp_path, ("sample",))]
    by_path = {record.path: record for record in records}

    assert by_path["sample/service.py"].routes == ("GET /items",)
    assert by_path["sample/v2_adapter.py"].imports == ("sample.service",)
    assert by_path["sample/v2_adapter.py"].version_named is True


def test_inventory_markdown_is_deterministic_and_report_only(tmp_path: Path) -> None:
    tool = _load_tool()
    package = tmp_path / "sample"
    package.mkdir()
    (package / "alpha.py").write_text("def public():\n    return 1\n", encoding="utf-8")
    (package / "beta.py").write_text("from sample import alpha\n", encoding="utf-8")

    records = [tool.inspect_file(tmp_path, path) for path in tool.iter_python_files(tmp_path, ("sample",))]
    first = tool.render_markdown(records)
    second = tool.render_markdown(records)

    assert first == second
    assert "Report-only" in first
    assert "sample/alpha.py" in first
    assert "sample/beta.py" in first


def test_repository_python_paths_do_not_use_generation_names() -> None:
    tool = _load_tool()
    records = tool.build_inventory(ROOT)
    version_named = [record.path for record in records if record.version_named]

    assert version_named == [], (
        "Python architecture paths must be responsibility-named, not generation-named: "
        + ", ".join(version_named)
    )
