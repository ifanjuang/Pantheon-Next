from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "audit_module_usage.py"


def _load_tool():
    name = "pantheon_module_usage_audit"
    spec = importlib.util.spec_from_file_location(name, TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _write(root: Path, relative: str, content: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_relative_imports_are_resolved_before_orphan_classification(tmp_path: Path) -> None:
    audit = _load_tool()
    _write(tmp_path, "pkg/__init__.py", "from . import directory\n")
    _write(
        tmp_path,
        "pkg/api.py",
        "from .lifecycle import install\n"
        "from . import directory\n"
        "def mount(app):\n"
        "    app.get('/items')(lambda: {})\n"
        "    return install(directory)\n",
    )
    _write(tmp_path, "pkg/lifecycle.py", "def install(value):\n    return value\n")
    _write(tmp_path, "pkg/directory.py", "ITEMS = {}\n")
    _write(tmp_path, "pkg/orphan.py", "VALUE = 1\n")

    spec = audit.ZoneSpec("demo", "implementation", "demo-owner", tmp_path)
    records = {item.module: item for item in audit.inspect_zone(spec)}

    assert records["pkg.lifecycle"].usage_state == "active_imported"
    assert records["pkg.directory"].usage_state == "active_imported"
    assert records["pkg.api"].usage_state == "active_entrypoint"
    assert records["pkg.orphan"].usage_state == "candidate_unreferenced"
    assert records["pkg.orphan"].removal_candidate is True


def test_configuration_test_modules_and_test_only_usage_are_distinct(tmp_path: Path) -> None:
    audit = _load_tool()
    _write(tmp_path, "pkg/__init__.py", "")
    _write(tmp_path, "pkg/plugin.py", "def register():\n    return None\n")
    _write(tmp_path, "pkg/helper.py", "VALUE = 1\n")
    _write(tmp_path, "tests/test_consumer.py", "import pkg.helper\n")
    _write(tmp_path, "tests/test_lonely.py", "def test_ok():\n    assert True\n")
    _write(tmp_path, "plugin.yaml", "entrypoint: pkg.plugin\n")
    _write(tmp_path, "pkg/__main__.py", "print('entry')\n")

    spec = audit.ZoneSpec("demo", "implementation", "demo-owner", tmp_path)
    records = {item.module: item for item in audit.inspect_zone(spec)}

    assert records["pkg.plugin"].usage_state == "active_dynamic_or_configured"
    assert records["pkg.plugin"].removal_candidate is False
    assert records["pkg.helper"].usage_state == "test_only"
    assert records["pkg.helper"].removal_candidate is False
    assert records["tests.test_consumer"].usage_state == "test_module"
    assert records["tests.test_lonely"].usage_state == "test_module"
    assert records["tests.test_lonely"].removal_candidate is False
    assert records["pkg.__main__"].usage_state == "active_entrypoint"


def test_tooling_path_reference_is_detected_and_unreferenced_tooling_is_review_only(
    tmp_path: Path,
) -> None:
    audit = _load_tool()
    _write(
        tmp_path,
        ".github/scripts/sync_preview.py",
        "from pathlib import Path\nPath('out').mkdir(exist_ok=True)\n",
    )
    _write(
        tmp_path,
        ".github/scripts/retired_helper.py",
        "VALUE = 1\n",
    )
    _write(
        tmp_path,
        ".github/workflows/preview.yml",
        "steps:\n  - run: python .github/scripts/sync_preview.py\n",
    )

    spec = audit.ZoneSpec("demo", "governance", "demo-owner", tmp_path)
    records = {item.path: item for item in audit.inspect_zone(spec)}

    active = records[".github/scripts/sync_preview.py"]
    review = records[".github/scripts/retired_helper.py"]
    assert active.usage_state == "active_dynamic_or_configured"
    assert active.config_references == [".github/workflows/preview.yml"]
    assert review.usage_state == "tooling_unreferenced_review"
    assert review.removal_candidate is False


def test_markdown_states_that_candidate_is_not_deletion_proof(tmp_path: Path) -> None:
    audit = _load_tool()
    _write(tmp_path, "orphan.py", "VALUE = 1\n")
    spec = audit.ZoneSpec("demo", "implementation", "demo-owner", tmp_path)
    records = audit.inspect_zone(spec)

    report = audit.render_markdown([spec], records)

    assert "candidate_unreferenced" in report
    assert "not deletion proof" in report
    assert "explicit human decision" in report
