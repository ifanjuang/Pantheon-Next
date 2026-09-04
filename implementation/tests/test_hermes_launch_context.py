"""PostgreSQL acceptance tests for the admission -> launch reservation junction."""

from __future__ import annotations

import uuid

import pytest

from pantheon_app import (
    agency_data,
    hermes_execution,
    hermes_handoff_preview,
    hermes_handoff_store,
    hermes_launch_context,
    hermes_scoped_context,
    work_issues,
)


def _id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex}"


@pytest.fixture
def conn():
    try:
        connection = agency_data.connect()
    except Exception as exc:  # pragma: no cover
        pytest.skip(f"PostgreSQL unreachable: {exc}")
    connection.execute(work_issues.MIGRATION.read_text(encoding="utf-8"))
    connection.execute(hermes_handoff_store.MIGRATION.read_text(encoding="utf-8"))
    for migration in hermes_execution.MIGRATIONS:
        connection.execute(migration.read_text(encoding="utf-8"))
    connection.commit()
    yield connection
    connection.close()


def _admitted(conn) -> tuple[dict, dict, dict]:
    project = agency_data.create_project(
        conn,
        project_id=_id("project"),
        code=_id("CODE").upper(),
        display_name="Projet launch junction",
        description="Description au moment de la réservation",
        actor="human-reviewer",
        actor_kind="human",
        idempotency_key=_id("project-create"),
    )
    envelope = {
        "root_entity": {
            "entity_id": f"project:{project['project_id']}",
            "entity_type": "project",
        },
        "descendants": [],
        "source_refs": [],
        "explicit_additions": [],
        "explicit_exclusions": [],
        "scope_widened_implicitly": False,
    }
    preview = hermes_handoff_preview.build_preview(
        question="Analyse ce projet sans élargir le périmètre.",
        card_context_envelope=envelope,
        selected_context=[],
    )
    handoff = hermes_handoff_store.submit_handoff(
        conn,
        actor="ifan",
        idempotency_key=_id("handoff"),
        question="Analyse ce projet sans élargir le périmètre.",
        preview=preview,
        card_context_envelope=envelope,
        selected_context=[],
        include_declared_descendants=False,
    )
    admission = hermes_execution.admit_handoff(
        conn,
        handoff_id=handoff["handoff_id"],
        actor="ifan",
        idempotency_key=_id("admit"),
        ttl_seconds=900,
    )
    return project, handoff, admission


def test_launch_reservation_freezes_bounded_snapshot_and_closes_revocation_window(conn) -> None:
    project, _handoff, admission = _admitted(conn)

    reservation = hermes_launch_context.reserve_launch(
        conn,
        admission_id=admission["admission_id"],
        actor="hermes-run-binding",
        idempotency_key=_id("reserve"),
    )

    assert reservation["runtime_submission_performed"] is False
    assert reservation["dispatch_performed"] is False
    assert reservation["snapshot"]["field_projection_version"] == "scoped-context-v1"
    assert reservation["snapshot"]["source_binary_included"] is False
    project_entry = next(
        item for item in reservation["snapshot"]["entities"]
        if item["entity_ref"]["entity_type"] == "project"
    )
    assert project_entry["record"]["project_id"] == project["project_id"]
    assert project_entry["record"]["description"] == "Description au moment de la réservation"
    assert "created_by" not in project_entry["record"]

    state = hermes_execution.get_admission(conn, admission["admission_id"])
    assert state["admission_state"] == "launch_reserved"
    assert state["launch_reservation_id"] == reservation["launch_reservation_id"]
    assert state["ready_for_external_runtime"] is False

    with pytest.raises(hermes_execution.AdmissionConflict, match="cannot be revoked"):
        hermes_execution.revoke_admission(
            conn,
            admission_id=admission["admission_id"],
            actor="ifan",
            reason="too late after reservation",
            idempotency_key=_id("revoke"),
        )


def test_reservation_replay_is_same_object_but_new_key_cannot_reserve_again(conn) -> None:
    _project, _handoff, admission = _admitted(conn)
    key = _id("reserve")
    first = hermes_launch_context.reserve_launch(
        conn,
        admission_id=admission["admission_id"],
        actor="hermes-run-binding",
        idempotency_key=key,
    )
    replay = hermes_launch_context.reserve_launch(
        conn,
        admission_id=admission["admission_id"],
        actor="hermes-run-binding",
        idempotency_key=key,
    )
    assert replay["launch_reservation_id"] == first["launch_reservation_id"]
    assert replay["snapshot_digest"] == first["snapshot_digest"]
    assert replay["replayed"] is True

    with pytest.raises(
        hermes_launch_context.LaunchReservationConflict,
        match="automatic retry is forbidden",
    ):
        hermes_launch_context.reserve_launch(
            conn,
            admission_id=admission["admission_id"],
            actor="hermes-run-binding",
            idempotency_key=_id("different-reserve"),
        )


def test_exact_reservation_links_real_run_and_current_reads_can_diverge_from_snapshot(conn) -> None:
    project, handoff, admission = _admitted(conn)
    reservation = hermes_launch_context.reserve_launch(
        conn,
        admission_id=admission["admission_id"],
        actor="hermes-run-binding",
        idempotency_key=_id("reserve"),
    )

    updated = agency_data.update_project(
        conn,
        project_id=project["project_id"],
        changes={"description": "Description modifiée après snapshot"},
        actor="human-reviewer",
        actor_kind="human",
        expected_revision=1,
        idempotency_key=_id("project-update"),
    )
    assert updated["revision"] == 2

    with pytest.raises(hermes_execution.RuntimeStartConflict, match="exact launch reservation"):
        hermes_execution.record_external_runtime_start(
            conn,
            admission_id=admission["admission_id"],
            run_id=_id("run-bad"),
            actor="hermes-run-binding",
            expected_issue_version=handoff["work_issue"]["version"],
            idempotency_key=_id("start-bad"),
            launch_reservation_id="launch-reservation-wrong",
        )

    run_id = _id("run")
    started = hermes_execution.record_external_runtime_start(
        conn,
        admission_id=admission["admission_id"],
        run_id=run_id,
        actor="hermes-run-binding",
        expected_issue_version=reservation["work_issue_version"],
        idempotency_key=_id("start"),
        launch_reservation_id=reservation["launch_reservation_id"],
    )
    assert started["runtime_start_recorded"] is True
    assert started["launch_reservation_id"] == reservation["launch_reservation_id"]

    row = conn.execute(
        "SELECT admission_ref, launch_reservation_ref FROM hermes_runs WHERE run_id=%s",
        (run_id,),
    ).fetchone()
    assert row[0] == admission["admission_id"]
    assert row[1] == reservation["launch_reservation_id"]

    current = hermes_scoped_context.get_context_entity(
        conn,
        admission_id=admission["admission_id"],
        run_id=run_id,
        entity_type="project",
        entity_id=f"project:{project['project_id']}",
        actor="hermes-runtime",
    )
    snapshot_project = next(
        item for item in reservation["snapshot"]["entities"]
        if item["entity_ref"]["entity_type"] == "project"
    )
    assert snapshot_project["record"]["description"] == "Description au moment de la réservation"
    assert current["record"]["description"] == "Description modifiée après snapshot"
    assert current["current_revision"] == 2
