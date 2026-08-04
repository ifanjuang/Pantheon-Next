from __future__ import annotations

from copy import deepcopy
import importlib.util
from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "hermes" / "distribution" / "pantheon-standard.lock.yaml"
TOOL = ROOT / "tools" / "check_hermes_distribution_lock.py"


def _load_tool():
    name = "pantheon_hermes_distribution_lock_checker"
    spec = importlib.util.spec_from_file_location(name, TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


CHECKER = _load_tool()


def _manifest() -> dict:
    value = yaml.safe_load(LOCK.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _fake_next_root(tmp_path: Path, manifest: dict) -> Path:
    root = tmp_path / "Pantheon-Next"
    for component in manifest["components"]:
        if component["source_repository"] != "Pantheon-Next":
            continue
        path = root / component["path"]
        if Path(component["path"]).suffix:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("candidate fixture\n", encoding="utf-8")
        else:
            path.mkdir(parents=True, exist_ok=True)
    return root


def test_distribution_lock_keeps_required_components_separate_and_default_off(tmp_path) -> None:
    manifest = _manifest()
    next_root = _fake_next_root(tmp_path, manifest)

    assert CHECKER.evaluate(
        manifest,
        repository_roots={"pantheon-mvp": ROOT, "Pantheon-Next": next_root},
    ) == []

    required_kinds = {
        item["kind"] for item in manifest["components"] if item["required"] is True
    }
    assert required_kinds == {"run_binding", "context_bridge", "runtime_observer"}
    assert all(item["enabled_by_default"] is False for item in manifest["components"])
    assert manifest["state"]["activation_state"] == "not_activated"
    assert manifest["state"]["task_authorization_state"] == "not_authorized"
    assert set(manifest["authority"].values()) == {False}


def test_distribution_route_contract_matches_current_adapter_sources(tmp_path) -> None:
    manifest = _manifest()
    next_root = _fake_next_root(tmp_path, manifest)

    assert CHECKER._route_contract(
        manifest,
        {"pantheon-mvp": ROOT, "Pantheon-Next": next_root},
    ) == []


def test_distribution_validator_rejects_authority_and_default_enablement(tmp_path) -> None:
    manifest = _manifest()
    next_root = _fake_next_root(tmp_path, manifest)
    invalid = deepcopy(manifest)
    invalid["components"][0]["enabled_by_default"] = True
    invalid["state"]["activation_state"] = "activated"
    invalid["authority"]["dispatches_runs"] = True

    errors = CHECKER.evaluate(
        invalid,
        repository_roots={"pantheon-mvp": ROOT, "Pantheon-Next": next_root},
    )

    assert "component must remain default-off: run-binding" in errors
    assert "distribution lock must not activate a binding" in errors
    assert "distribution lock claims authority: dispatches_runs" in errors
