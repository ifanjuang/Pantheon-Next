"""Decision-record identity (issue #13, P1). All DB-free — the gate records a
decision on a candidate stream, no pgvector involved."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

from mvp_vertical.terminal_gate_standin import record_decision


def _candidates(status: str = "draft_to_review") -> list:
    return [
        {
            "object_type": "result_candidate",
            "object_id": "mvp.test.tc.rc-001",
            "result_candidate_id": "mvp.test.tc.rc-001",
            "applies_to": "mvp.test.tc",
            "status": status,
            "body": "…",
            "external_action_authorized": False,
        },
        {
            "object_type": "evidence_pack_candidate",
            "object_id": "mvp.test.tc.ep-001",
            "evidence_pack_id": "mvp.test.tc.ep-001",
            "status": "candidate",
            "possible_decisions": ["approve", "refuse", "request_revision", "request_more_evidence"],
        },
    ]


def test_two_decisions_on_the_same_candidate_are_distinct_events():
    first = record_decision(_candidates(), decision="request_revision", decided_by="Camille",
                            recorded_at="2026-07-12T10:00:00.000001Z")
    second = record_decision(_candidates(), decision="approve", decided_by="Camille",
                             recorded_at="2026-07-12T10:05:00.000002Z")
    assert first["decision_id"] != second["decision_id"]
    assert first["object_id"] != second["object_id"]
    # both still apply to the same candidate
    assert first["applies_to"] == second["applies_to"] == "mvp.test.tc.rc-001"


def test_even_identical_decisions_differ_by_timestamp():
    a = record_decision(_candidates(), decision="approve", decided_by="Camille",
                        recorded_at="2026-07-12T10:00:00.000001Z")
    b = record_decision(_candidates(), decision="approve", decided_by="Camille",
                        recorded_at="2026-07-12T10:00:00.000002Z")
    assert a["decision_id"] != b["decision_id"]


def test_decision_id_is_deterministic_for_pinned_inputs():
    kw = dict(decision="approve", decided_by="Camille", rationale="ok",
              recorded_at="2026-07-12T10:00:00.000000Z")
    assert record_decision(_candidates(), **kw)["decision_id"] == \
           record_decision(_candidates(), **kw)["decision_id"]


def test_recorded_at_is_present_and_microsecond():
    rec = record_decision(_candidates(), decision="approve", decided_by="Camille")
    assert rec["recorded_at"].endswith("Z")
    # "…:SS.ffffff Z" — a dot-separated microsecond fraction is present
    assert "." in rec["recorded_at"].split("T", 1)[1]


def test_supersession_is_recorded_without_rewriting():
    first = record_decision(_candidates(), decision="request_revision", decided_by="Camille",
                            recorded_at="2026-07-12T10:00:00.000001Z")
    revised = record_decision(_candidates(), decision="approve", decided_by="Camille",
                              recorded_at="2026-07-12T10:05:00.000000Z",
                              supersedes_decision_id=first["decision_id"])
    assert revised["supersedes_decision_id"] == first["decision_id"]
    # the superseding record is its own event, not a mutation of the first
    assert revised["decision_id"] != first["decision_id"]
    # a decision that supersedes nothing carries no such field
    assert "supersedes_decision_id" not in first


def test_decision_record_still_authorizes_nothing_and_conforms():
    import jsonschema
    schema = yaml.safe_load((ROOT / "vendor/pantheon/mvp_governed_loop_objects.schema.yaml").read_text())
    rec = record_decision(_candidates(), decision="approve", decided_by="Camille",
                          supersedes_decision_id="mvp.test.tc.rc-001.decision.deadbeef0000")
    assert rec["external_action_authorized"] is False
    jsonschema.validate(rec, schema)  # unique id + recorded_at + supersedes all schema-valid
