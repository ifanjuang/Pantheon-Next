from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "check_architecture_convergence_closure.py"


def _load_tool():
    name = "pantheon_architecture_convergence_closure"
    spec = importlib.util.spec_from_file_location(name, TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _clean_payloads() -> tuple[dict, dict]:
    repositories = [
        {"name": "pantheon-mvp"},
        {"name": "Pantheon-Next"},
    ]
    return (
        {
            "repositories": repositories,
            "artifacts": [
                {
                    "repository": "pantheon-mvp",
                    "path": "mvp_vertical/api.py",
                    "posture": "implementation",
                    "generation_named": False,
                    "versioned_routes": [],
                    "parse_error": None,
                }
            ],
        },
        {
            "repositories": repositories,
            "modules": [
                {
                    "repository": "pantheon-mvp",
                    "path": "mvp_vertical/api.py",
                    "usage_state": "active_entrypoint",
                    "removal_candidate": False,
                    "parse_error": None,
                }
            ],
        },
    )


def test_clean_inventories_pass_permanent_closure_guard() -> None:
    guard = _load_tool()
    architecture, usage = _clean_payloads()

    assert guard.evaluate(
        architecture,
        usage,
        expected_repositories=("pantheon-mvp", "Pantheon-Next"),
    ) == []


def test_generation_names_and_versioned_routes_are_permanent_active_violations() -> None:
    guard = _load_tool()
    architecture, usage = _clean_payloads()
    architecture["artifacts"][0]["generation_named"] = True
    architecture["artifacts"][0]["versioned_routes"] = ["/v1/internal"]

    violations = guard.evaluate(architecture, usage)

    assert any("generation-named active artifact" in item for item in violations)
    assert any("versioned internal route" in item for item in violations)


def test_history_and_retired_route_tests_remain_auditable_without_becoming_debt() -> None:
    guard = _load_tool()
    architecture, usage = _clean_payloads()
    architecture["artifacts"].extend(
        [
            {
                "repository": "Pantheon-Next",
                "path": "ai_logs/2026-07-03-hermes-v018-release-review.md",
                "posture": "history",
                "generation_named": True,
                "versioned_routes": [],
                "parse_error": None,
            },
            {
                "repository": "pantheon-mvp",
                "path": "tests/test_retired_routes.py",
                "posture": "test",
                "generation_named": False,
                "versioned_routes": ["/v1/retired"],
                "parse_error": None,
            },
        ]
    )

    assert guard.evaluate(architecture, usage) == []


def test_unreferenced_implementation_candidate_is_a_permanent_violation() -> None:
    guard = _load_tool()
    architecture, usage = _clean_payloads()
    usage["modules"][0]["usage_state"] = "candidate_unreferenced"
    usage["modules"][0]["removal_candidate"] = True

    violations = guard.evaluate(architecture, usage)

    assert any("unreferenced implementation candidate" in item for item in violations)


def test_missing_cross_repository_input_is_refused() -> None:
    guard = _load_tool()
    architecture, usage = _clean_payloads()
    architecture["repositories"] = [{"name": "pantheon-mvp"}]

    violations = guard.evaluate(
        architecture,
        usage,
        expected_repositories=("pantheon-mvp", "Pantheon-Next"),
    )

    assert violations == [
        "architecture inventory is missing expected repository: Pantheon-Next"
    ]


def test_parse_errors_are_refused() -> None:
    guard = _load_tool()
    architecture, usage = _clean_payloads()
    architecture["artifacts"][0]["parse_error"] = "invalid syntax"
    usage["modules"][0]["usage_state"] = "parse_error"
    usage["modules"][0]["parse_error"] = "invalid syntax"

    violations = guard.evaluate(architecture, usage)

    assert any("Python parse error" in item for item in violations)
    assert any("module parse error" in item for item in violations)


def test_temporary_decreasing_debt_baseline_remains_removed() -> None:
    assert not (ROOT / "docs/architecture/ARCHITECTURE_DEBT_BASELINE.json").exists()
    assert not (ROOT / "tools/check_architecture_debt_baseline.py").exists()
    assert not (ROOT / "tests/test_architecture_debt_baseline.py").exists()
