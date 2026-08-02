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
                "revision": 1,
                "concepts": [
                    {
                        "id": "project_claim",
                        "label": "ProjectClaim",
                        "canonical_owner": "Pantheon-Next",
                        "patterns": [r"\bproject[_ -]?claim\b"],
                        "max_active_implementations": 1,
                        "max_authority_definitions": 2,
                    },
                    {
                        "id": "evidence",
                        "label": "Evidence",
                        "canonical_owner": "Pantheon-Next",
                        "patterns": [r"\bevidence\b"],
                    },
                ],
            }
        ),
        encoding="utf-8",
    )
    return tool.load_registry(path)


def test_cross_repository_audit_prioritizes_authority_runtime_and_generation(
    tmp_path: Path,
) -> None:
    tool = _load_tool()
    registry = _registry(tool, tmp_path)
    next_root = tmp_path / "Pantheon-Next"
    mvp_root = tmp_path / "pantheon-mvp"
    (next_root / "schemas").mkdir(parents=True)
    (mvp_root / "contracts").mkdir(parents=True)

    (next_root / "schemas" / "project_claim.schema.yaml").write_text(
        "project_claim evidence canonical schema\n",
        encoding="utf-8",
    )
    (mvp_root / "contracts" / "project_claim_contract.py").write_text(
        'PROJECT_CLAIM = "project_claim"\n',
        encoding="utf-8",
    )
    (mvp_root / "v2_adapter.py").write_text(
        'URL = "/v1/items"\nqueue = []\nproject_claim = True\n',
        encoding="utf-8",
    )

    specs = [
        tool.RepositorySpec("Pantheon-Next", "governance", next_root),
        tool.RepositorySpec("pantheon-mvp", "implementation", mvp_root),
    ]
    records = tool.build_inventory(specs, registry)
    findings = tool.build_findings(specs, records, registry)
    categories = {(finding.priority, finding.category) for finding in findings}

    assert ("P0", "authority_collision") in categories
    assert ("P0", "runtime_boundary") in categories
    assert ("P1", "generation_name") in categories
    assert ("P1", "generation_identity") in categories
    assert all(len(finding.finding_id) == 12 for finding in findings)


def test_historical_generation_names_are_reported_at_low_priority(tmp_path: Path) -> None:
    tool = _load_tool()
    registry = _registry(tool, tmp_path)
    next_root = tmp_path / "Pantheon-Next"
    mvp_root = tmp_path / "pantheon-mvp"
    (next_root / "ai_logs").mkdir(parents=True)
    mvp_root.mkdir()
    (next_root / "ai_logs" / "adapter_v0.md").write_text(
        "historical /v1 route\n",
        encoding="utf-8",
    )

    specs = [
        tool.RepositorySpec("Pantheon-Next", "governance", next_root),
        tool.RepositorySpec("pantheon-mvp", "implementation", mvp_root),
    ]
    records = tool.build_inventory(specs, registry)
    findings = tool.build_findings(specs, records, registry)

    version_findings = [
        finding
        for finding in findings
        if finding.category in {"generation_name", "generation_identity"}
    ]
    assert version_findings
    assert {finding.priority for finding in version_findings} == {"P5"}


def test_empty_duplicates_are_ignored_and_report_is_deterministic(tmp_path: Path) -> None:
    tool = _load_tool()
    registry = _registry(tool, tmp_path)
    next_root = tmp_path / "Pantheon-Next"
    mvp_root = tmp_path / "pantheon-mvp"
    next_root.mkdir()
    mvp_root.mkdir()

    (next_root / "empty.py").write_text("", encoding="utf-8")
    (mvp_root / "empty.py").write_text("", encoding="utf-8")
    (next_root / "shared.md").write_text("same\n", encoding="utf-8")
    (mvp_root / "shared.md").write_text("same\n", encoding="utf-8")

    specs = [
        tool.RepositorySpec("Pantheon-Next", "governance", next_root),
        tool.RepositorySpec("pantheon-mvp", "implementation", mvp_root),
    ]
    records = tool.build_inventory(specs, registry)
    findings = tool.build_findings(specs, records, registry)

    assert len(tool.exact_duplicates(records)) == 1
    first = tool.render_markdown(specs, records, registry, findings)
    second = tool.render_markdown(specs, records, registry, findings)
    assert first == second
    assert "Pantheon architecture convergence inventory" in first
    assert "Decision vocabulary" in first


def test_registry_rejects_duplicate_concept_ids(tmp_path: Path) -> None:
    tool = _load_tool()
    path = tmp_path / "ownership.json"
    path.write_text(
        json.dumps(
            {
                "registry_id": "pantheon.system_ownership",
                "revision": 1,
                "concepts": [
                    {
                        "id": "evidence",
                        "canonical_owner": "Pantheon-Next",
                        "patterns": [r"\bevidence\b"],
                    },
                    {
                        "id": "evidence",
                        "canonical_owner": "Pantheon-Next",
                        "patterns": [r"\bevidence\b"],
                    },
                ],
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
