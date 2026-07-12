"""Block 3 — Register Candidate (issue #13). All DB-free: builds a real
approved decision_record via the gate, then proposes/refuses retention."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]

from mvp_vertical.register import RegisterRefusal, propose_register_candidate
from mvp_vertical.terminal_gate_standin import record_decision

SCHEMA = yaml.safe_load((ROOT / "vendor/pantheon/mvp_governed_loop_objects.schema.yaml").read_text())


def _candidates() -> list:
    return [
        {"object_type": "result_candidate", "object_id": "mvp.test.tc.rc-001",
         "result_candidate_id": "mvp.test.tc.rc-001", "applies_to": "mvp.test.tc",
         "status": "draft_to_review", "body": "…", "external_action_authorized": False},
        {"object_type": "evidence_pack_candidate", "object_id": "mvp.test.tc.ep-001",
         "evidence_pack_id": "mvp.test.tc.ep-001", "status": "candidate",
         "possible_decisions": ["approve", "refuse", "request_revision", "request_more_evidence"]},
    ]


def _approved() -> dict:
    return record_decision(_candidates(), decision="approve", decided_by="Camille")


def test_approved_decision_can_propose_a_register_candidate():
    import jsonschema
    reg = propose_register_candidate(_approved(), retention_authorized=True,
                                     statement="Le lot 06 est limité à la terrasse T2.",
                                     scope="dossier devis_reprise")
    assert reg["object_type"] == "register_candidate"
    assert reg["status"] == "candidate"
    assert reg["not_memory_until_admitted"] is True
    jsonschema.validate(reg, SCHEMA)


def test_register_candidate_links_to_the_exact_reviewed_content():
    decision = _approved()
    reg = propose_register_candidate(decision, retention_authorized=True,
                                     statement="x", scope="y")
    assert reg["created_because_of"] == decision["decision_id"]
    # the candidate digest the human reviewed is carried in the basis
    joined = " ".join(reg["basis"])
    assert decision["candidate_digest"]["value"] in joined
    assert decision["evidence_pack_digest"]["value"] in joined


def test_refuses_when_decision_is_not_approve():
    revision = record_decision(_candidates(), decision="request_revision", decided_by="Camille")
    with pytest.raises(RegisterRefusal):
        propose_register_candidate(revision, retention_authorized=True, statement="x", scope="y")


def test_refuses_without_explicit_retention_authorization():
    for value in (False, None, "true", 1):
        with pytest.raises(RegisterRefusal):
            propose_register_candidate(_approved(), retention_authorized=value, statement="x", scope="y")


def test_refuses_missing_statement_or_scope():
    with pytest.raises(RegisterRefusal):
        propose_register_candidate(_approved(), retention_authorized=True, statement="  ", scope="y")
    with pytest.raises(RegisterRefusal):
        propose_register_candidate(_approved(), retention_authorized=True, statement="x", scope="")


def test_refuses_non_decision_record_input():
    with pytest.raises(RegisterRefusal):
        propose_register_candidate({"object_type": "result_candidate"},
                                   retention_authorized=True, statement="x", scope="y")


def test_candidate_promotes_no_memory_and_authorizes_nothing():
    reg = propose_register_candidate(_approved(), retention_authorized=True, statement="x", scope="y")
    assert reg["not_memory_until_admitted"] is True
    assert "memory_promotion" in reg["forbidden_reuse"]
    assert "external_send" in reg["forbidden_reuse"]
    # it never asserts an external authorization…
    assert reg.get("external_action_authorized", False) is False
    # …and it is a candidate, never an admitted register entry
    assert reg["status"] == "candidate"
