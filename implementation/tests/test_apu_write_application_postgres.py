"""PostgreSQL acceptance tests for H2 bounded APU match application."""

from __future__ import annotations

import json
import uuid

import pytest

from mvp_vertical import agency_data, apu_owner, apu_write_preparation


@pytest.fixture
def conn():
    try:
        connection = agency_data.connect()
        connection.execute(apu_owner.MIGRATION.read_text(encoding="utf-8"))
        connection.execute(apu_write_preparation.MIGRATION.read_text(encoding="utf-8"))
        connection.execute(
            apu_write_preparation.APPLICATION_MIGRATION.read_text(encoding="utf-8")
        )
        connection.commit()
    except Exception as exc:  # pragma: no cover - local unit-only environment
        pytest.skip(f"PostgreSQL unreachable: {exc}")
    connection.execute("BEGIN")
    try:
        yield connection
    finally:
        connection.rollback()
        connection.close()


def _id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex}"


def _project(conn, label: str) -> str:
    project_id = _id("project")
    conn.execute(
        "INSERT INTO agency_projects "
        "(project_id, code, display_name, created_by, updated_by) "
        "VALUES (%s, %s, %s, 'test', 'test')",
        (project_id, _id(label), f"Projet {label}"),
    )
    return project_id


def _bootstrap_object(conn, project_id: str, object_id: str) -> None:
    apu_owner.store_reviewed_dossier(
        conn,
        project_id=project_id,
        objects=[
            {
                "stable_object": {
                    "stable_object_id": object_id,
                    "human_ref": object_id,
                    "kind": "space",
                    "proof_status": "accepted_as_support",
                    "scope_type": "project",
                    "scope_id": project_id,
                    "matches": [],
                },
                "object_identity": {
                    "stable_id": object_id,
                    "object_kind": "space",
                    "current_display_name": "Pièce test",
                    "source_refs": [],
                    "aliases": [],
                },
            }
        ],
        relations=[],
        review_ref="review:h2-bootstrap",
        actor="human:architect",
        idempotency_key=_id("apu-bootstrap"),
    )


def _command(
    *,
    project_id: str,
    object_id: str,
    candidate_ref: str,
    expected_owner_revision: int = 1,
    expected_object_revision: int = 1,
) -> dict:
    command = {
        "command_id": _id("apu-write-command"),
        "operation": "add_match_to_existing_object",
        "project_ref": project_id,
        "source_execution_result_ref": _id("execution"),
        "source_mapping_result_ref": _id("result"),
        "source_mapping_ref": _id("mapping"),
        "source_review_ref": _id("review"),
        "target_stable_object_ref": object_id,
        "source_candidate_ref": candidate_ref,
        "source_artifact_ref": _id("document"),
        "certainty": "E3",
        "expected_owner_revision": expected_owner_revision,
        "expected_object_revision": expected_object_revision,
        "rationale": "Le mapping revu rattache ce fragment à l'objet existant.",
        "prepared_by": "human:architect",
        "limitations": ["Application bornée à ce match et à cette révision."],
        "authority": dict(apu_write_preparation.COMMAND_AUTHORITY),
    }
    command["payload_digest"] = apu_write_preparation._digest(command)
    return command


def _persist_command_and_authorization(conn, command: dict) -> str:
    conn.execute(
        """
        INSERT INTO apu_write_command_candidates (
            command_id, execution_result_id, result_ref, mapping_ref, source_review_ref,
            operation, project_ref, target_stable_object_ref, source_candidate_ref,
            source_artifact_ref, certainty, rationale, command_payload, payload_digest,
            expected_owner_revision, expected_object_revision,
            prepared_by, idempotency_key
        ) VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s::jsonb, %s,
            %s, %s,
            %s, %s
        )
        """,
        (
            command["command_id"],
            command["source_execution_result_ref"],
            command["source_mapping_result_ref"],
            command["source_mapping_ref"],
            command["source_review_ref"],
            command["operation"],
            command["project_ref"],
            command["target_stable_object_ref"],
            command["source_candidate_ref"],
            command.get("source_artifact_ref"),
            command.get("certainty"),
            command["rationale"],
            json.dumps(command, sort_keys=True, separators=(",", ":")),
            command["payload_digest"],
            command["expected_owner_revision"],
            command["expected_object_revision"],
            command["prepared_by"],
            _id("prepare-key"),
        ),
    )
    authorization_id = _id("apu-write-authorization")
    authorization_payload = {
        "command_ref": command["command_id"],
        "command_payload_digest": command["payload_digest"],
        "action": "authorize_application",
        "authorized_by": "human:architect",
    }
    conn.execute(
        """
        INSERT INTO apu_write_authorization_events (
            authorization_id, command_ref, command_payload_digest, action,
            authorized_by, idempotency_key, payload_digest
        ) VALUES (%s, %s, %s, 'authorize_application', %s, %s, %s)
        """,
        (
            authorization_id,
            command["command_id"],
            command["payload_digest"],
            "human:architect",
            _id("authorize-key"),
            apu_write_preparation._digest(authorization_payload),
        ),
    )
    return authorization_id


def _setup_application(conn, *, label: str = "apply") -> tuple[str, str, dict, str]:
    project_id = _project(conn, label)
    object_id = _id("space")
    _bootstrap_object(conn, project_id, object_id)
    command = _command(
        project_id=project_id,
        object_id=object_id,
        candidate_ref=_id("candidate"),
    )
    authorization_id = _persist_command_and_authorization(conn, command)
    return project_id, object_id, command, authorization_id


def test_application_mutates_only_the_existing_match_and_records_provenance(conn) -> None:
    project_id, object_id, command, authorization_id = _setup_application(conn)

    receipt = apu_owner.apply_source_match(
        conn,
        command=command,
        authorization_id=authorization_id,
        actor="human:architect",
        idempotency_key=_id("apply-key"),
    )

    assert receipt["status"] == "applied"
    assert receipt["owner_revision"] == 2
    assert receipt["authority"] == apu_owner.APPLICATION_AUTHORITY
    assert receipt["authority"]["match_recorded"] is True
    assert receipt["authority"]["stable_identity_professionally_validated"] is False
    assert receipt["authority"]["is_evidence"] is False
    assert receipt["authority"]["is_decision"] is False
    assert receipt["authority"]["closes_work_issue"] is False
    assert receipt["authority"]["authorizes_external_effect"] is False

    stored = apu_owner.get_apu_object(
        conn,
        project_id=project_id,
        object_id=object_id,
    )
    assert stored["revision"] == 2
    assert len(stored["stable_object"]["matches"]) == 1
    match = stored["stable_object"]["matches"][0]
    assert match["source_candidate_id"] == command["source_candidate_ref"]
    assert match["source_artifact_id"] == command["source_artifact_ref"]
    assert match["certainty"] == "E3"
    assert match["status"] == "candidate"
    assert f"authorization:{authorization_id}" in match["match_evidence"]

    events = apu_owner.list_apu_events(conn, project_id=project_id)
    assert [item["event_type"] for item in events] == [
        "reviewed_dossier_imported",
        "source_match_applied",
    ]
    event = events[-1]
    assert event["expected_revision"] == 1
    assert event["resulting_revision"] == 2
    assert event["command_ref"] == command["command_id"]
    assert event["authorization_ref"] == authorization_id
    assert event["payload"]["stable_identity_professionally_validated"] is False
    assert event["payload"]["evidence_admitted"] is False
    assert event["payload"]["work_issue_closed"] is False
    assert event["payload"]["decision_request_resolved"] is False


def test_exact_application_replay_is_idempotent(conn) -> None:
    project_id, object_id, command, authorization_id = _setup_application(
        conn, label="replay"
    )
    key = _id("apply-replay")

    first = apu_owner.apply_source_match(
        conn,
        command=command,
        authorization_id=authorization_id,
        actor="human:architect",
        idempotency_key=key,
    )
    second = apu_owner.apply_source_match(
        conn,
        command=command,
        authorization_id=authorization_id,
        actor="human:architect",
        idempotency_key=key,
    )

    assert first["status"] == "applied"
    assert second["status"] == "replayed"
    assert apu_owner.get_apu_object(
        conn,
        project_id=project_id,
        object_id=object_id,
    )["revision"] == 2
    assert sum(
        item["event_type"] == "source_match_applied"
        for item in apu_owner.list_apu_events(conn, project_id=project_id)
    ) == 1


def test_same_command_cannot_be_applied_again_under_another_idempotency_key(conn) -> None:
    _project_id, _object_id, command, authorization_id = _setup_application(
        conn, label="command-once"
    )
    apu_owner.apply_source_match(
        conn,
        command=command,
        authorization_id=authorization_id,
        actor="human:architect",
        idempotency_key=_id("apply-first"),
    )

    with pytest.raises(apu_owner.ApuOwnerConflict, match="already applied"):
        apu_owner.apply_source_match(
            conn,
            command=command,
            authorization_id=authorization_id,
            actor="human:architect",
            idempotency_key=_id("apply-second"),
        )


def test_stale_owner_revision_is_refused_without_match_mutation(conn) -> None:
    project_id, object_id, command, authorization_id = _setup_application(
        conn, label="stale-owner"
    )
    conn.execute(
        "UPDATE agency_apu_project_state SET revision = 2 WHERE project_id = %s",
        (project_id,),
    )

    with pytest.raises(apu_owner.ApuOwnerConflict, match="stale APU owner revision"):
        apu_owner.apply_source_match(
            conn,
            command=command,
            authorization_id=authorization_id,
            actor="human:architect",
            idempotency_key=_id("apply-stale-owner"),
        )

    stored = apu_owner.get_apu_object(conn, project_id=project_id, object_id=object_id)
    assert stored["revision"] == 1
    assert stored["stable_object"]["matches"] == []


def test_stale_object_revision_is_refused_without_match_mutation(conn) -> None:
    project_id, object_id, command, authorization_id = _setup_application(
        conn, label="stale-object"
    )
    conn.execute(
        "UPDATE agency_apu_objects SET revision = 2 "
        "WHERE project_id = %s AND object_id = %s",
        (project_id, object_id),
    )

    with pytest.raises(apu_owner.ApuOwnerConflict, match="stale APU object revision"):
        apu_owner.apply_source_match(
            conn,
            command=command,
            authorization_id=authorization_id,
            actor="human:architect",
            idempotency_key=_id("apply-stale-object"),
        )

    stored = apu_owner.get_apu_object(conn, project_id=project_id, object_id=object_id)
    assert stored["revision"] == 2
    assert stored["stable_object"]["matches"] == []


def test_application_event_remains_append_only(conn) -> None:
    project_id, _object_id, command, authorization_id = _setup_application(
        conn, label="history"
    )
    receipt = apu_owner.apply_source_match(
        conn,
        command=command,
        authorization_id=authorization_id,
        actor="human:architect",
        idempotency_key=_id("apply-history"),
    )
    event_id = receipt["event"]["event_id"]

    with pytest.raises(Exception, match="append-only"):
        with conn.transaction():
            conn.execute(
                "UPDATE agency_apu_events SET actor = 'other' WHERE event_id = %s",
                (event_id,),
            )


def test_h2_migration_is_catalog_guarded_for_composed_startup() -> None:
    sql = apu_write_preparation.APPLICATION_MIGRATION.read_text(encoding="utf-8")
    assert "ADD COLUMN IF NOT EXISTS" not in sql
    assert "information_schema.columns" in sql
    assert "pg_constraint" in sql
    assert "NOT VALID" in sql
    assert "VALIDATE CONSTRAINT" in sql
