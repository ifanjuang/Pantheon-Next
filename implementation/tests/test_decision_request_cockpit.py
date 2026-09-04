from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "pantheon_app" / "cockpit"
PROJECTION = COCKPIT / "projection" / "decision_request_projection.js"
ACTIONS = COCKPIT / "actions" / "decision_request_actions.js"
ASSEMBLER = COCKPIT / "projection" / "child_collection_assembler.js"
LOADER = COCKPIT / "data" / "cockpit_data_loader.js"
DEFINITIONS = COCKPIT / "registries" / "card_projection_definitions.json"


def test_decision_request_projection_preserves_one_stable_identity() -> None:
    source = PROJECTION.read_text(encoding="utf-8")
    assembler = ASSEMBLER.read_text(encoding="utf-8")
    loader = LOADER.read_text(encoding="utf-8")

    assert "decision-request:${requestId}" in source
    assert "request_is_not_decision: true" in source
    assert 'available_actions: request.status === "pending" ? ["Décider"] : []' in source
    assert "PantheonGlobalDecisionRequests" in loader
    assert "PantheonProjectDecisionRequests" in loader
    assert "PantheonGlobalDecisionRequests" in assembler
    assert "PantheonProjectDecisionRequests" in assembler
    assert ".map(decisionProjection().normalize)" in assembler


def test_decisions_root_metadata_is_definition_driven() -> None:
    definitions = json.loads(DEFINITIONS.read_text(encoding="utf-8"))["definitions"]
    decision = next(item for item in definitions if item["entity_id"] == "space:decisions")
    assert decision["presentation_family"] == "decision"
    assert decision["children_source"] == "navigation_registry"
    assert "n’est pas une Décision" in decision["detail_rows"][0][1]

    projection = PROJECTION.read_text(encoding="utf-8")
    assert 'entity_id: "space:decisions"' in projection
    assert 'entity_type: "cockpit_space"' in projection
    assert 'title: "Décisions"' not in projection


def test_decision_action_records_only_a_human_determination() -> None:
    source = ACTIONS.read_text(encoding="utf-8")
    assert "../decision-requests/${encodeURIComponent(requestId)}" in source
    assert "decision-requests/${encodeURIComponent(requestId)}/resolve" in source
    assert 'identity_assurance: "declared"' in source
    assert 'X-Pantheon-Human-Actor' in source
    assert "Cette opération crée un Decision record immuable" in source

    for forbidden in (
        "handoff-submit",
        "handoff-admit",
        "runtime_continuation_authorized: true",
        "work_issue_transitioned: true",
        "action_executed: true",
        "evidence_admitted",
        "setInterval(",
        "setTimeout(",
    ):
        assert forbidden not in source


@pytest.mark.parametrize("path", [PROJECTION, ACTIONS, ASSEMBLER, LOADER])
def test_decision_cockpit_javascript_parses(path: Path) -> None:
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js unavailable")
    result = subprocess.run([node, "--check", str(path)], check=False, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
