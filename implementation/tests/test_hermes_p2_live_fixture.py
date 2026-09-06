from __future__ import annotations

import pytest

from mvp_vertical import (
    agency_data,
    apu_owner,
    hermes_execution,
    hermes_handoff_store,
    store,
    work_issues,
)
from mvp_vertical.hermes_live_acceptance import CONTEXT_TOOLS, SYNTHETIC_MARKER
from mvp_vertical.hermes_p2_live_fixture import prepare_p2_live_admission


@pytest.fixture
def conn():
    try:
        connection = store.connect()
    except Exception as exc:  # pragma: no cover - local unit-only environment
        pytest.skip(f"PostgreSQL unreachable: {exc}")
    connection.execute(agency_data.MIGRATION.read_text(encoding="utf-8"))
    connection.execute(apu_owner.MIGRATION.read_text(encoding="utf-8"))
    connection.execute(work_issues.MIGRATION.read_text(encoding="utf-8"))
    connection.execute(hermes_handoff_store.MIGRATION.read_text(encoding="utf-8"))
    for migration in hermes_execution.MIGRATIONS:
        connection.execute(migration.read_text(encoding="utf-8"))
    connection.commit()
    yield connection
    connection.close()


def _assert_live_guard_shape(conn, receipt: dict) -> dict:
    assert receipt["synthetic"] is True
    assert receipt["execution_started"] is False
    assert receipt["hermes_run_created"] is False
    assert receipt["technical_receipt_is_evidence"] is False
    assert receipt["production_authorization"] is False
    assert receipt["admission_state"] == "admitted"
    assert "synthetic" in receipt["project_id"]
    assert SYNTHETIC_MARKER in receipt["question"]
    for tool in CONTEXT_TOOLS:
        assert tool in receipt["question"]

    handoff = hermes_handoff_store.get_handoff_snapshot(conn, receipt["handoff_id"])
    assert handoff["question"] == receipt["question"]
    assert handoff["context_pack"]["root_entity"]["entity_type"] == "project"
    assert "synthetic" in handoff["context_pack"]["root_entity"]["entity_id"]

    run_count = conn.execute(
        "SELECT COUNT(*) FROM hermes_runs WHERE admission_ref = %s",
        (receipt["admission_id"],),
    ).fetchone()[0]
    assert run_count == 0
    return handoff


def test_variant_a_prepares_one_unconsumed_local_context_admission(conn) -> None:
    receipt = prepare_p2_live_admission(
        conn,
        variant="A",
        actor="human:p2-test",
        ttl_seconds=900,
    )
    handoff = _assert_live_guard_shape(conn, receipt)

    assert receipt["variant"] == "A"
    assert len(receipt["selected_context"]) == 1
    assert receipt["selected_context"][0]["entity_type"] == "stable_object"
    assert receipt["unrelated_object_ref"] not in receipt["selected_context"]
    assert handoff["include_declared_descendants"] is False
    assert handoff["context_pack"]["scope_widened_implicitly"] is False


def test_variant_b_prepares_composed_context_without_unrelated_object_or_review_claim(conn) -> None:
    receipt = prepare_p2_live_admission(
        conn,
        variant="B",
        actor="human:p2-test",
        ttl_seconds=900,
    )
    handoff = _assert_live_guard_shape(conn, receipt)

    assert receipt["variant"] == "B"
    assert len(receipt["selected_context"]) == 8
    assert {item["entity_type"] for item in receipt["selected_context"]} == {
        "stable_object",
        "information",
        "document",
        "knowledge",
    }
    assert receipt["unrelated_object_ref"] not in receipt["selected_context"]
    assert receipt["knowledge_review_status"] == "generated_unreviewed"
    assert receipt["apu_review_ref_is_synthetic_fixture"] is True
    assert handoff["include_declared_descendants"] is False
    assert handoff["context_pack"]["scope_widened_implicitly"] is False

    knowledge_ref = next(
        item["entity_id"]
        for item in receipt["selected_context"]
        if item["entity_type"] == "knowledge"
    )
    knowledge_id = knowledge_ref.removeprefix("knowledge:")
    status = conn.execute(
        "SELECT review_status FROM knowledge_items WHERE knowledge_id = %s",
        (knowledge_id,),
    ).fetchone()[0]
    assert status == "generated_unreviewed"


def test_each_variant_gets_a_fresh_project_and_admission(conn) -> None:
    a = prepare_p2_live_admission(conn, variant="A", actor="human:p2-test", ttl_seconds=900)
    b = prepare_p2_live_admission(conn, variant="B", actor="human:p2-test", ttl_seconds=900)

    assert a["question"] == b["question"]
    assert a["project_id"] != b["project_id"]
    assert a["handoff_id"] != b["handoff_id"]
    assert a["admission_id"] != b["admission_id"]
    assert a["selected_context"] != b["selected_context"]
