from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


def test_project_back_uses_authoritative_server_schema() -> None:
    renderer = (COCKPIT / "v2_app_schema.js").read_text(encoding="utf-8")

    assert '../v1/agency/schema/project' in renderer
    assert "state.projectSchema" in renderer
    assert "projectSchemaRows" in renderer
    assert 'field.storage === "attributes"' in renderer
    assert 'field.title || field.label || field.key' in renderer
    assert "const labels = {" not in renderer


def test_pending_change_candidates_are_distinct_decision_cards_under_pantheon() -> None:
    renderer = (COCKPIT / "v2_app_schema.js").read_text(encoding="utf-8")

    assert '/change-candidates?status=pending_review&limit=100' in renderer
    assert 'entity_type: "project_change_candidate"' in renderer
    assert 'entity_id: `decision:change:${item.candidate_id}`' in renderer
    assert 'category: "Décision · Modification"' in renderer
    assert 'entity_type: "work_decision"' in renderer
    assert 'category: "Décision · Travail"' in renderer
    assert 'setChildren("space:pantheon", [...changeDecisionIds, ...workDecisionIds, ...runIds])' in renderer
    assert 'setChildren("space:decisions"' not in renderer
    assert '"decisions"' not in renderer.split("const ROOT_SPACES =", 1)[1].split(";", 1)[0]
    assert "state.changeCandidates" in renderer


def test_change_candidate_buttons_use_human_apply_reject_routes() -> None:
    bootstrap = (COCKPIT / "live_bootstrap.js").read_text(encoding="utf-8")
    actions = (COCKPIT / "actions" / "change_candidate_actions.js").read_text(encoding="utf-8")

    assert '"actions/change_candidate_actions.js"' in bootstrap
    assert 'decision:change:' in actions
    assert '/v1/agency/change-candidates/${encodeURIComponent(candidate.candidateId)}/apply' in actions
    assert '/v1/agency/change-candidates/${encodeURIComponent(candidate.candidateId)}/reject' in actions
    assert 'X-Pantheon-Actor' in actions
    assert "runs/start" not in actions
    assert "execution-admissions" not in actions


def test_change_candidate_javascript_parses() -> None:
    node = shutil.which("node")
    if node is None:  # pragma: no cover
        pytest.skip("node is unavailable")
    path = COCKPIT / "actions" / "change_candidate_actions.js"
    subprocess.run([node, "--check", str(path)], check=True, capture_output=True, text=True)
