from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONOREPO = ROOT.parent
WORKFLOW = MONOREPO / ".github" / "workflows" / "implementation-hindsight-obsidian-o2-sync.yml"
ROUTING = ROOT / "tools" / "run_hindsight_obsidian_workspace_routing_o2.sh"


def test_workspace_routing_reuses_current_o2_runtime_matrix() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    assert 'HINDSIGHT_VERSION: "0.9.1"' in workflow
    assert "daf529aacad14a5b8f7db9f34a7f49c9e3629b61" in workflow
    assert "run_hindsight_obsidian_workspace_routing_o2.sh" in workflow


def test_one_human_workspace_routes_affaires_and_documentaires_to_existing_banks() -> None:
    raw = ROUTING.read_text(encoding="utf-8")
    assert 'VAULT="$LAB_ROOT/IFJA"' in raw
    assert 'AFFAIRES_BANK="ifja-projects"' in raw
    assert 'DOCUMENTAIRES_BANK="ifja-agency"' in raw
    assert '--include "$include"' in raw
    assert "Affaires/Lieurey/CR/CR03.md" in raw
    assert "Documentaires/Technique/bardage.md" in raw
    assert "folder:Affaires" in raw
    assert "folder:Documentaires" in raw
    assert "separate_indexes_verified':True" in raw
    assert "cross_bank_leakage_not_observed':True" in raw
    assert "independent_prune_verified':True" in raw


def test_workspace_routing_does_not_migrate_authority_or_live_data() -> None:
    raw = ROUTING.read_text(encoding="utf-8")
    assert "bank_ids_migrated':False" in raw
    assert "real_vaults_changed':False" in raw
    assert "pantheon_state_mutated':False" in raw
    assert "evidence_admitted':False" in raw
    assert "sync_retain" not in raw
    assert "Project Anatomy" not in raw
