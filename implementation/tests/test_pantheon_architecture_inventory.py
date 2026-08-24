from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = ROOT / "tools" / "audit_pantheon_architecture.py"


def _load_tool():
    name = "audit_pantheon_architecture"
    spec = importlib.util.spec_from_file_location(name, TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _registry(tool, tmp_path: Path):
    path = tmp_path / "ownership.json"
    path.write_text(
        json.dumps(
            {
                "registry_id": "pantheon.system_ownership",
                "revision": 2,
                "concepts": [
                    {
                        "id": "project_claim",
                        "label": "ProjectClaim",
                        "semantic_owner": "Pantheon-Next",
                        "implementation_owner": "pantheon-mvp",
                        "patterns": [r"\bproject[_ -]?claim\b"],
                        "max_identity_implementations": 1,
                    },
                    {
                        "id": "hermes_execution",
                        "label": "Hermes execution",
                        "semantic_owner": "Pantheon-Next",
                        "implementation_owner": "pantheon-mvp",
                        "runtime_owner": "Hermes/external runtime",
                        "patterns": [r"\bhermes[_ -]?(?:execution|run|runtime|tool)\b"],
                        "max_identity_implementations": 2,
                    },
                ],
            }
        ),
        encoding="utf-8",
    )
    return tool.load_registry(path)


def test_audit_distinguishes_internal_routes_runtime_constructs_and_semantics(
    tmp_path: Path,
) -> None:
    tool = _load_tool()
    registry = _registry(tool, tmp_path)
    next_root = tmp_path / "Pantheon-Next"
    mvp_root = tmp_path / "pantheon-mvp"
    (next_root / "docs" / "governance").mkdir(parents=True)
    (mvp_root / "pkg").mkdir(parents=True)

    (next_root / "docs" / "governance" / "PROJECT_CLAIM.md").write_text(
        "project_claim lifecycle\n",
        encoding="utf-8",
    )
    (mvp_root / "pkg" / "project_claim.py").write_text(
        "from fastapi import APIRouter\n"
        "router = APIRouter(prefix='/v1')\n"
        "class ProjectClaim:\n"
        "    pass\n",
        encoding="utf-8",
    )
    (mvp_root / "pkg" / "runner.py").write_text(
        "import queue\n"
        "def enqueue():\n"
        "    return queue.Queue()\n",
        encoding="utf-8",
    )

    specs = [
        tool.ZoneSpec("governance-core", "governance", "Pantheon-Next", next_root),
        tool.ZoneSpec("implementation", "implementation", "pantheon-mvp", mvp_root),
    ]
    records = tool.build_inventory(specs, registry)
    findings = tool.build_findings(specs, records, registry)
    categories = {(finding.priority, finding.category) for finding in findings}

    assert ("P1", "internal_versioned_routes") in categories
    assert ("P0", "runtime_constructs") in categories
    assert not any(
        finding.category == "semantic_owner_conflict" for finding in findings
    )


def test_guard_vocabulary_is_not_treated_as_runtime_implementation(
    tmp_path: Path,
) -> None:
    tool = _load_tool()
    registry = _registry(tool, tmp_path)
    next_root = tmp_path / "Pantheon-Next"
    mvp_root = tmp_path / "pantheon-mvp"
    (next_root / ".github" / "scripts").mkdir(parents=True)
    mvp_root.mkdir()
    (next_root / ".github" / "scripts" / "check_boundaries.py").write_text(
        'FORBIDDEN = ["scheduler", "queue", "automatic_approval"]\n',
        encoding="utf-8",
    )

    specs = [
        tool.ZoneSpec("governance-core", "governance", "Pantheon-Next", next_root),
        tool.ZoneSpec("implementation", "implementation", "pantheon-mvp", mvp_root),
    ]
    records = tool.build_inventory(specs, registry)
    findings = tool.build_findings(specs, records, registry)

    assert not any(finding.category == "runtime_constructs" for finding in findings)


def test_external_version_reference_is_not_an_internal_route(tmp_path: Path) -> None:
    tool = _load_tool()
    registry = _registry(tool, tmp_path)
    next_root = tmp_path / "Pantheon-Next"
    mvp_root = tmp_path / "pantheon-mvp"
    next_root.mkdir()
    (mvp_root / "hermes" / "client").mkdir(parents=True)
    (mvp_root / "hermes" / "client" / "runs.py").write_text(
        "HERMES_RUNS_URL = 'http://hermes:8642/v1/runs'\n",
        encoding="utf-8",
    )

    specs = [
        tool.ZoneSpec("governance-core", "governance", "Pantheon-Next", next_root),
        tool.ZoneSpec("implementation", "implementation", "pantheon-mvp", mvp_root),
    ]
    records = tool.build_inventory(specs, registry)
    findings = tool.build_findings(specs, records, registry)

    assert any(finding.category == "version_references" for finding in findings)
    assert not any(
        finding.category == "internal_versioned_routes" for finding in findings
    )


def test_empty_duplicates_are_ignored_and_report_is_deterministic(
    tmp_path: Path,
) -> None:
    tool = _load_tool()
    registry = _registry(tool, tmp_path)
    next_root = tmp_path / "Pantheon-Next"
    mvp_root = tmp_path / "pantheon-mvp"
    next_root.mkdir()
    mvp_root.mkdir()
    (next_root / "empty.py").write_text("", encoding="utf-8")
    (mvp_root / "empty.py").write_text("", encoding="utf-8")
    (next_root / "project_claim.schema.yaml").write_text(
        "same\n", encoding="utf-8"
    )
    (mvp_root / "project_claim.schema.yaml").write_text(
        "same\n", encoding="utf-8"
    )

    specs = [
        tool.ZoneSpec("governance-core", "governance", "Pantheon-Next", next_root),
        tool.ZoneSpec("implementation", "implementation", "pantheon-mvp", mvp_root),
    ]
    records = tool.build_inventory(specs, registry)
    findings = tool.build_findings(specs, records, registry)

    assert len(tool.exact_duplicates(records)) == 1
    first = tool.render_markdown(specs, records, registry, findings)
    second = tool.render_markdown(specs, records, registry, findings)
    assert first == second
    assert "Pantheon architecture convergence inventory" in first
    assert "semantic `Pantheon-Next`" in first
    assert "**governance-core**" in first
    assert "**implementation**" in first


def test_nested_monorepo_zones_assign_each_artifact_once(tmp_path: Path) -> None:
    tool = _load_tool()
    registry = _registry(tool, tmp_path)
    repo_root = tmp_path / "repo"
    implementation_root = repo_root / "implementation"
    (repo_root / "docs" / "governance").mkdir(parents=True)
    (implementation_root / "pkg").mkdir(parents=True)
    (repo_root / "docs" / "governance" / "PROJECT_CLAIM.md").write_text(
        "project_claim lifecycle\n", encoding="utf-8"
    )
    (implementation_root / "pkg" / "project_claim.py").write_text(
        "class ProjectClaim:\n    pass\n", encoding="utf-8"
    )
    specs = [
        tool.ZoneSpec("governance-core", "governance", "Pantheon-Next", repo_root),
        tool.ZoneSpec("implementation", "implementation", "pantheon-mvp", implementation_root),
    ]
    records = tool.build_inventory(specs, registry)
    assert len(records) == 2
    assert {(record.zone, record.path) for record in records} == {
        ("governance-core", "docs/governance/PROJECT_CLAIM.md"),
        ("implementation", "pkg/project_claim.py"),
    }
    assert next(record for record in records if record.zone == "implementation").owner_identity == "pantheon-mvp"


def test_registry_rejects_duplicate_concept_ids(tmp_path: Path) -> None:
    tool = _load_tool()
    path = tmp_path / "ownership.json"
    concept = {
        "id": "project_claim",
        "semantic_owner": "Pantheon-Next",
        "patterns": [r"\bproject[_ -]?claim\b"],
    }
    path.write_text(
        json.dumps(
            {
                "registry_id": "pantheon.system_ownership",
                "revision": 2,
                "concepts": [concept, concept],
            }
        ),
        encoding="utf-8",
    )

    try:
        tool.load_registry(path)
    except ValueError as exc:
        assert "duplicate concept id" in str(exc)
    else:
        raise AssertionError("duplicate concept ids must be rejected")
