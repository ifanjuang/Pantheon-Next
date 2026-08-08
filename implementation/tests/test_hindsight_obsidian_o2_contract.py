from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "hindsight-obsidian-o2-sync.yml"
SEQUENCE = ROOT / "tools" / "run_hindsight_obsidian_o2.sh"


def test_o2_uses_exact_official_headless_sync_release() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8")
    workflow = yaml.safe_load(raw)
    assert workflow["name"] == "Hindsight Obsidian O2 Sync"
    assert "pull_request" in workflow[True]
    assert "workflow_dispatch" in workflow[True]
    assert "b627aa6fa02f8516d4af402ebceca4a5beed3ec9" in raw
    assert "vectorize-io/hindsight-obsidian" in raw
    assert "p.version!=='0.2.0'" in raw
    assert "hindsight-obsidian-sync" in raw
    assert "npm run lint" in raw
    assert "npm test" in raw
    assert "npm run build" in raw


def test_o2_live_lab_is_local_synthetic_and_no_llm() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8")
    assert 'HINDSIGHT_VERSION: "0.8.5"' in raw
    assert "HINDSIGHT_API_RETAIN_EXTRACTION_MODE=chunks" in raw
    assert "HINDSIGHT_API_ENABLE_AUTO_CONSOLIDATION=false" in raw
    assert "HINDSIGHT_API_ENABLE_OBSERVATIONS=false" in raw
    assert "secrets." not in raw
    assert "pantheon-o2-synthetic" in raw
    assert "docker stop pantheon-o2-hindsight" in raw


def test_o2_exercises_real_reconcile_lifecycle_and_scope() -> None:
    raw = SEQUENCE.read_text(encoding="utf-8")
    assert raw.startswith("#!/usr/bin/env bash\nset -euo pipefail")
    assert 'VAULT_A="$LAB_ROOT/Vault-A"' in raw
    assert 'VAULT_B="$LAB_ROOT/Vault-B"' in raw
    assert '"$VAULT_A/Projects/Alpha"' in raw
    assert '"$VAULT_A/Projects/Beta"' in raw
    assert '"$VAULT_B/Projects/Alpha"' in raw
    assert raw.count('node "$CLI" reconcile') == 1  # centralized helper, invoked repeatedly
    assert "=2 unchanged" in raw
    assert "~1 updated" in raw
    assert "-1 deleted" in raw
    assert 'mv "$VAULT_A/Projects/Alpha/note.md"' in raw
    assert "tags_match': 'all_strict'" in raw
    assert "vault:Vault-A" in raw
    assert "vault:Vault-B" in raw
    assert "folder:Projects/Alpha" in raw
    assert "document_id" in raw
    assert "metadata" in raw and "path" in raw
    assert "pantheon_state_mutated':False" in raw
    assert "evidence_admitted':False" in raw


def test_o2_does_not_create_pantheon_memory_or_sync_authority() -> None:
    raw = SEQUENCE.read_text(encoding="utf-8") + WORKFLOW.read_text(encoding="utf-8")
    assert "Project Anatomy" not in raw
    assert "Registre Probatoire" not in raw
    assert "LangChain" not in raw
    assert "LangGraph" not in raw
    assert "bidirectional" not in raw.lower()
