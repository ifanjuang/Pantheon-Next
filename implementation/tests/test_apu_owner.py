"""PostgreSQL acceptance tests for the H1 executable Project Anatomy owner."""

from __future__ import annotations

import uuid

import psycopg
import pytest

from mvp_vertical import agency_data, apu_owner


@pytest.fixture
def conn():
    try:
        connection = agency_data.connect()
        exists = connection.execute(
            "SELECT to_regclass('public.agency_apu_objects')"
        ).fetchone()[0]
        if exists is None:
            apu_owner.ensure_schema(connection)
    except Exception as exc:  # pragma: no cover - local unit-only environment
        pytest.skip(f"PostgreSQL unreachable: {exc}")
    connection.commit()
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


def _object(project_id: str, object_id: str, *, kind: str = "opening") -> dict:
    return {
        "stable_object": {
            "stable_object_id": object_id,
            "human_ref": object_id,
            "kind": kind,
            "proof_status": "accepted_as_support",
            "scope_type": "project",
            "scope_id": project_id,
            "matches": [
                {
                    "source_candidate_id": f"candidate-{object_id}",
                    "source_artifact_id": f"source-{object_id}",
                    "certainty": "E3",
                    "status": "confirmed_by_human",
                    "match_axis": "cross_source",
                    "match_evidence": ["reviewed-source-match"],
                }
            ],
        },
        "object_identity": {
            "stable_id": object_id,
            "object_kind": kind,
            "current_display_name": f"Objet {object_id}",
            "source_refs": [
                {"source": "reviewed-plan-A", "value": f"ref-{object_id}"}
            ],
            "aliases": [f"alias-{object_id}"],
        },
    }


def _relation(origin: str, target: str) -> dict:
    return {
        "relation_id": _id("apu-relation"),
        "type": "hosted_by",
        "from": origin,
        "to": target,
        "source_refs": ["reviewed-plan-A"],
    }


def _store(conn, project_id: str, *, key: str | None = None):
    opening = _id("apu-opening")
    boundary = _id("apu-boundary")
    return apu_owner.store_reviewed_dossier(
        conn,
        project_id=project_id,
        objects=[
            _object(project_id, opening, kind="opening"),
            _object(project_id, boundary, kind="boundary"),
        ],
        relations=[_relation(opening, boundary)],
        review_ref="review:architect:2026-08-07",
        actor="human:architect",
        idempotency_key=key or _id("apu-bootstrap"),
    )


def test_reviewed_dossier_becomes_one_server_owned_project_projection(conn) -> None:
    project_id = _project(conn, "read-owner")
    projection = _store(conn, project_id)

    assert projection["project_ref"] == project_id
    assert projection["owner_revision"] == 1
    assert len(projection["objects"]) == 2
    assert len(projection["relations"]) == 1
    assert projection["relations"][0]["type"] == "hosted_by"
    assert projection["authority"] == apu_owner.AUTHORITY
    assert projection["authority"]["is_evidence"] is False
    assert projection["authority"]["permits_runtime_writes"] is False

    event = apu_owner.list_apu_events(conn, project_id=project_id)
    assert len(event) == 1
    assert event[0]["event_type"] == "reviewed_dossier_imported"
    assert event[0]["expected_revision"] == 0
    assert event[0]["resulting_revision"] == 1
    assert event[0]["payload"]["automatic_creation"] is False
    assert event[0]["payload"]["runtime_write"] is False


def test_bootstrap_is_idempotent_for_the_exact_same_reviewed_dossier(conn) -> None:
    project_id = _project(conn, "idempotent")
    object_a = _id("apu-opening")
    object_b = _id("apu-boundary")
    relation = _relation(object_a, object_b)
    key = _id("apu-key")
    kwargs = {
        "project_id": project_id,
        "objects": [
            _object(project_id, object_a, kind="opening"),
            _object(project_id, object_b, kind="boundary"),
        ],
        "relations": [relation],
        "review_ref": "review:architect:fixed",
        "actor": "human:architect",
        "idempotency_key": key,
    }

    first = apu_owner.store_reviewed_dossier(conn, **kwargs)
    second = apu_owner.store_reviewed_dossier(conn, **kwargs)
    assert second == first
    assert len(apu_owner.list_apu_events(conn, project_id=project_id)) == 1


def test_idempotency_key_cannot_be_reused_for_another_dossier(conn) -> None:
    project_id = _project(conn, "idempotency-conflict")
    key = _id("apu-key")
    object_a = _id("apu-opening")
    apu_owner.store_reviewed_dossier(
        conn,
        project_id=project_id,
        objects=[_object(project_id, object_a)],
        relations=[],
        review_ref="review:one",
        actor="human:architect",
        idempotency_key=key,
    )

    with pytest.raises(apu_owner.ApuOwnerConflict, match="another effect"):
        apu_owner.store_reviewed_dossier(
            conn,
            project_id=project_id,
            objects=[_object(project_id, object_a)],
            relations=[],
            review_ref="review:two",
            actor="human:architect",
            idempotency_key=key,
        )


def test_owner_refuses_cross_project_scope_before_persistence(conn) -> None:
    project_a = _project(conn, "scope-a")
    project_b = _project(conn, "scope-b")
    with pytest.raises(apu_owner.ApuOwnerError, match="exact Project scope"):
        apu_owner.store_reviewed_dossier(
            conn,
            project_id=project_a,
            objects=[_object(project_b, _id("apu-object"))],
            relations=[],
            review_ref="review:scope",
            actor="human:architect",
            idempotency_key=_id("apu-key"),
        )


def test_owner_refuses_invalid_governed_object_shape(conn) -> None:
    project_id = _project(conn, "schema")
    item = _object(project_id, _id("apu-object"))
    item["stable_object"]["kind"] = "imaginary_kind"
    item["object_identity"]["object_kind"] = "imaginary_kind"

    with pytest.raises(apu_owner.ApuOwnerError, match="governed contract"):
        apu_owner.store_reviewed_dossier(
            conn,
            project_id=project_id,
            objects=[item],
            relations=[],
            review_ref="review:schema",
            actor="human:architect",
            idempotency_key=_id("apu-key"),
        )


def test_relation_must_resolve_inside_the_reviewed_dossier(conn) -> None:
    project_id = _project(conn, "relation")
    object_id = _id("apu-object")
    with pytest.raises(apu_owner.ApuOwnerError, match="outside the dossier"):
        apu_owner.store_reviewed_dossier(
            conn,
            project_id=project_id,
            objects=[_object(project_id, object_id)],
            relations=[_relation(object_id, _id("missing-object"))],
            review_ref="review:relation",
            actor="human:architect",
            idempotency_key=_id("apu-key"),
        )


def test_second_bootstrap_without_matching_idempotency_is_refused(conn) -> None:
    project_id = _project(conn, "single-owner")
    _store(conn, project_id)
    with pytest.raises(apu_owner.ApuOwnerConflict, match="already initialized"):
        apu_owner.store_reviewed_dossier(
            conn,
            project_id=project_id,
            objects=[_object(project_id, _id("apu-object"))],
            relations=[],
            review_ref="review:other",
            actor="human:architect",
            idempotency_key=_id("apu-key"),
        )


def test_database_relation_foreign_keys_refuse_cross_project_endpoints(conn) -> None:
    project_a = _project(conn, "fk-a")
    project_b = _project(conn, "fk-b")
    projection_a = _store(conn, project_a)
    projection_b = _store(conn, project_b)
    object_a = projection_a["objects"][0]["object_id"]
    object_b = projection_b["objects"][0]["object_id"]

    with pytest.raises(psycopg.errors.ForeignKeyViolation):
        with conn.transaction():
            conn.execute(
                """
                INSERT INTO agency_apu_object_relations (
                    relation_id, project_id, relation_type, from_object_id,
                    to_object_id, relation_payload, payload_digest, created_by
                ) VALUES (%s, %s, 'hosted_by', %s, %s, '{}'::jsonb, 'digest', 'test')
                """,
                (_id("bad-relation"), project_a, object_a, object_b),
            )


def test_apu_event_history_is_append_only(conn) -> None:
    project_id = _project(conn, "history")
    _store(conn, project_id)
    event_id = apu_owner.list_apu_events(conn, project_id=project_id)[0]["event_id"]

    with pytest.raises(psycopg.errors.RaiseException, match="append-only"):
        with conn.transaction():
            conn.execute(
                "UPDATE agency_apu_events SET actor = 'other' WHERE event_id = %s",
                (event_id,),
            )
