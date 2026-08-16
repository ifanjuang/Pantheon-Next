"""Contract checks for the historical O3 Hindsight/Obsidian/Hermes fixture.

The O3 lab intentionally preserves its exact Hindsight 0.8.5 and
hindsight-obsidian 0.2.0-era pins so the original qualification remains
reproducible. It is not the current deployed-version baseline. The newer
Windows + Synology qualification is recorded in Pantheon-Next #655 and its
2026-08-16 Q3 AI log.
"""

from __future__ import annotations

import ast
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "hindsight-obsidian-hermes-o3-lab.yml"
SEQUENCE = ROOT / "tools" / "run_hindsight_obsidian_hermes_o3.sh"
HERMES_CONFIG = ROOT / "tools" / "run_hindsight_hermes_o1.py"
FIXTURE = ROOT / "tools" / "hindsight_hermes_o1_fixture.py"


def test_o3_reuses_exact_historical_upstreams_and_existing_harnesses() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8")
    workflow = yaml.safe_load(raw)
    assert workflow["name"] == "Hindsight Obsidian Hermes O3 Shared Bank"
    assert "pull_request" in workflow[True]
    assert "workflow_dispatch" in workflow[True]
    assert "Historical O3 regression fixture" in raw
    assert "Current Windows + Synology qualification" in raw
    assert "b627aa6fa02f8516d4af402ebceca4a5beed3ec9" in raw
    assert "3c27eb6234bf91b8ceee9e9071591b31e9b148cb" in raw
    assert 'HINDSIGHT_VERSION: "0.8.5"' in raw
    assert "vectorize-io/hindsight-obsidian" in raw
    assert "NousResearch/hermes-agent" in raw
    assert "secrets." not in raw


def test_o3_has_one_ingestion_path_and_scoped_hermes_recall() -> None:
    raw = SEQUENCE.read_text(encoding="utf-8")
    assert raw.startswith("#!/usr/bin/env bash\nset -euo pipefail")
    assert "node \"$CLI\" reconcile" in raw
    assert "client.retain" not in raw
    assert "hindsight_client import Hindsight" not in raw
    assert "--recall-tag vault:Vault-A" in raw
    assert "--recall-tag folder:Projects/Alpha" in raw
    assert "--recall-tags-match all_strict" in raw
    assert "PANTHEON_O3_OBSIDIAN_TARGET" in raw
    assert "PANTHEON_O3_OBSIDIAN_STALE" in raw
    assert "PANTHEON_O3_VAULT_B_OTHER" in raw
    assert "forbid-marker" in raw
    assert "retain-count-before" in raw and "retain-count-after" in raw
    assert "hermes -p assistant-personal chat -q" in raw
    assert "capture-memory-status --profile pantheon-governed" in raw
    assert "profile delete assistant-personal --yes" in raw


def test_shared_hindsight_config_supports_strict_provider_scope_without_breaking_o1() -> None:
    raw = HERMES_CONFIG.read_text(encoding="utf-8")
    ast.parse(raw)
    assert 'cfg.add_argument("--recall-tag", action="append", default=[])' in raw
    assert 'cfg.add_argument("--recall-tags-match", default="all_strict")' in raw
    assert 'hindsight_config["recall_tags"] = recall_tags' in raw
    assert 'hindsight_config["recall_tags_match"] = recall_tags_match' in raw
    assert '"auto_retain": False' in raw
    assert '"auto_recall": False' in raw


def test_shared_fixture_can_require_target_and_exclude_stale_or_cross_vault_results() -> None:
    raw = FIXTURE.read_text(encoding="utf-8")
    ast.parse(raw)
    assert "DEFAULT_MARKER = \"PANTHEON_O1_SYNTHETIC_MEMORY_MARKER\"" in raw
    assert "DEFAULT_SUCCESS_TOKEN = \"O1_HINDSIGHT_RECALL_COMPLETED\"" in raw
    assert 'parser.add_argument("--forbid-marker", action="append", default=[])' in raw
    assert "forbidden_marker_seen_in_tool_result" in raw
    assert "hindsight_recall" in raw


def test_o3_preserves_authority_boundaries() -> None:
    raw = SEQUENCE.read_text(encoding="utf-8") + WORKFLOW.read_text(encoding="utf-8")
    assert "pantheon_state_mutated':False" in raw
    assert "evidence_admitted':False" in raw
    assert "production_activated':False" in raw
    assert "LangChain" not in raw
    assert "LangGraph" not in raw
    assert "Project Anatomy" not in raw
