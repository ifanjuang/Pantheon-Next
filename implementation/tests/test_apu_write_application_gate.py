"""Unit tests for the H2 command/review/authorization application gate."""

from __future__ import annotations

from contextlib import nullcontext

import pytest

from mvp_vertical import apu_owner, apu_write_preparation, execution_results


EXECUTION = {
    "execution_result": {"execution_result_id": "execution.mapping.001"},
    "results": [
        {
            "result_id": "result.mapping.001",
            "result_kind": "apu_object_mapping",
            "payload": {
                "project_ref": "project-1",
                "document_ref": "document-1",
                "mappings": [
                    {
                        "mapping_id": "mapping.room.001",
                        "candidate_object_ref": "candidate.room.001",
                        "certainty": "E3",
                        "rationale": "Le fragment peut correspondre à l'espace existant.",
                        "match_candidates": [
                            {"stable_object_ref": "space.room-a"},
                            {"stable_object_ref": "space.room-b"},
                        ],
                    }
                ],
            },
        }
    ],
}
REVIEW = {
    "review_id": "review.mapping.001",
    "action": "select_existing_object",
    "selected_stable_object_ref": "space.room-a",
}


class FakeCursor:
    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def execute(self, *_args, **_kwargs):
        return self

    def fetchone(self):
        return None


class FakeConnection:
    def __init__(self):
        self.statements = []

    def transaction(self):
        return nullcontext()

    def cursor(self, **_kwargs):
        return FakeCursor()

    def execute(self, statement, params=None):
        self.statements.append((statement, params))


def _command() -> dict:
    payload = {
        "command_id": "apu-write-command.001",
        "operation": "add_match_to_existing_object",
        "project_ref": "project-1",
        "source_execution_result_ref": "execution.mapping.001",
        "source_mapping_result_ref": "result.mapping.001",
        "source_mapping_ref": "mapping.room.001",
        "source_review_ref": "review.mapping.001",
        "target_stable_object_ref": "space.room-a",
        "source_candidate_ref": "candidate.room.001",
        "source_artifact_ref": "document-1",
        "certainty": "E3",
        "expected_owner_revision": 4,
        "expected_object_revision": 2,
        "rationale": "Le fragment peut correspondre à l'espace existant.",
        "prepared_by": "human:architect",
        "limitations": [
            "Une autorisation humaine distincte est requise avant toute application.",
            "L'application doit refuser une révision APU ou objet devenue obsolète.",
        ],
        "authority": dict(apu_write_preparation.COMMAND_AUTHORITY),
    }
    payload["payload_digest"] = apu_write_preparation._digest(payload)
    return payload


def test_prepare_captures_owner_and_object_revisions(monkeypatch) -> None:
    monkeypatch.setattr(
        execution_results,
        "get_execution_result",
        lambda _conn, _execution_id: EXECUTION,
    )
    monkeypatch.setattr(
        apu_write_preparation,
        "_latest_selected_review",
        lambda *_args, **_kwargs: REVIEW,
    )
    monkeypatch.setattr(
        apu_owner,
        "get_project_anatomy",
        lambda _conn, *, project_id: {"project_ref": project_id, "owner_revision": 4},
    )
    monkeypatch.setattr(
        apu_owner,
        "get_apu_object",
        lambda _conn, *, project_id, object_id: {
            "project_ref": project_id,
            "object_id": object_id,
            "revision": 2,
            "retired_at": None,
        },
    )
    monkeypatch.setattr(
        apu_write_preparation,
        "get_write_command",
        lambda _conn, command_id: {"command_id": command_id},
    )
    conn = FakeConnection()

    apu_write_preparation.prepare_write_command(
        conn,
        execution_result_id="execution.mapping.001",
        result_ref="result.mapping.001",
        mapping_ref="mapping.room.001",
        prepared_by="human:architect",
        idempotency_key="prepare-1",
    )

    insert = next(item for item in conn.statements if "INSERT INTO apu_write_command_candidates" in item[0])
    params = insert[1]
    assert params[14] == 4
    assert params[15] == 2
    command_payload = params[12]
    value = command_payload.obj if hasattr(command_payload, "obj") else command_payload
    assert value["expected_owner_revision"] == 4
    assert value["expected_object_revision"] == 2


def test_application_revalidates_review_authorization_and_candidate_membership(monkeypatch) -> None:
    command = _command()
    command_row = {
        "command_id": command["command_id"],
        "payload_digest": command["payload_digest"],
        "expected_owner_revision": 4,
        "expected_object_revision": 2,
        "command": command,
    }
    monkeypatch.setattr(
        apu_write_preparation,
        "get_write_command",
        lambda _conn, _command_id: command_row,
    )
    monkeypatch.setattr(
        execution_results,
        "get_execution_result",
        lambda _conn, _execution_id: EXECUTION,
    )
    monkeypatch.setattr(
        apu_write_preparation,
        "_latest_selected_review",
        lambda *_args, **_kwargs: REVIEW,
    )
    monkeypatch.setattr(
        apu_write_preparation,
        "_latest_application_authorization",
        lambda _conn, _command: {
            "authorization_id": "authorization-1",
            "action": "authorize_application",
            "command_payload_digest": command["payload_digest"],
        },
    )
    called = {}

    def apply(_conn, **kwargs):
        called.update(kwargs)
        return {"status": "applied", "authority": dict(apu_owner.APPLICATION_AUTHORITY)}

    monkeypatch.setattr(apu_owner, "apply_source_match", apply)
    result = apu_write_preparation.apply_authorized_write_command(
        object(),
        command_id=command["command_id"],
        applied_by="human:architect",
        idempotency_key="apply-1",
    )
    assert result["status"] == "applied"
    assert called["command"] == command
    assert called["authorization_id"] == "authorization-1"
    assert called["actor"] == "human:architect"


def test_application_refuses_superseded_review(monkeypatch) -> None:
    command = _command()
    monkeypatch.setattr(
        apu_write_preparation,
        "get_write_command",
        lambda _conn, _command_id: {
            "command_id": command["command_id"],
            "payload_digest": command["payload_digest"],
            "expected_owner_revision": 4,
            "expected_object_revision": 2,
            "command": command,
        },
    )
    monkeypatch.setattr(
        execution_results,
        "get_execution_result",
        lambda _conn, _execution_id: EXECUTION,
    )
    monkeypatch.setattr(
        apu_write_preparation,
        "_latest_selected_review",
        lambda *_args, **_kwargs: REVIEW | {"review_id": "review.mapping.newer"},
    )
    with pytest.raises(
        apu_write_preparation.ApuWriteApplicationConflict,
        match="newer mapping review",
    ):
        apu_write_preparation.apply_authorized_write_command(
            object(),
            command_id=command["command_id"],
            applied_by="human:architect",
            idempotency_key="apply-stale-review",
        )


def test_application_refuses_tampered_command_digest(monkeypatch) -> None:
    command = _command()
    command["rationale"] = "Contenu modifié après autorisation."
    monkeypatch.setattr(
        apu_write_preparation,
        "get_write_command",
        lambda _conn, _command_id: {
            "command_id": command["command_id"],
            "payload_digest": command["payload_digest"],
            "expected_owner_revision": 4,
            "expected_object_revision": 2,
            "command": command,
        },
    )
    with pytest.raises(
        apu_write_preparation.ApuWriteApplicationConflict,
        match="digest",
    ):
        apu_write_preparation.apply_authorized_write_command(
            object(),
            command_id=command["command_id"],
            applied_by="human:architect",
            idempotency_key="apply-tampered",
        )


def test_latest_rejection_blocks_application(monkeypatch) -> None:
    command = _command()
    monkeypatch.setattr(
        apu_write_preparation,
        "list_authorizations",
        lambda _conn, _command_id: [
            {
                "authorization_id": "authorization-reject",
                "action": "reject_application",
                "command_payload_digest": command["payload_digest"],
            }
        ],
    )
    with pytest.raises(
        apu_write_preparation.ApuWritePreparationError,
        match="authorize_application",
    ):
        apu_write_preparation._latest_application_authorization(object(), command)
