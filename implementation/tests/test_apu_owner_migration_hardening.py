"""Server-side hardening checks for the H4c Project Anatomy owner migration."""

from __future__ import annotations

import uuid

import psycopg
import pytest
from psycopg.types.json import Jsonb

from mvp_vertical import agency_data, apu_owner, store


CONTRACT_AUTHORITY_REF = (
    "ifanjuang/Pantheon-Next@98be3a1dd07be6b6ee2847127d698618f6ff703a"
)
MODEL_DOCTRINE_REF = (
    "ifanjuang/Pantheon-Next@17ce5585445407347ee7b686486857bf713d9172"
    "#docs/domain-packs/architecture/PROJECT_ANATOMY_MODEL.md"
)


def _id(prefix: str) -> str:
    return f"{prefix}.{uuid.uuid4().hex}"


@pytest.fixture
def conn():
    try:
        connection = store.connect()
    except Exception as exc:  # pragma: no cover - local unit-only environment
        pytest.skip(f"PostgreSQL unreachable: {exc}")

    connection.execute(agency_data.MIGRATION.read_text(encoding="utf-8"))
    connection.execute(apu_owner.MIGRATION.read_text(encoding="utf-8"))
    connection.execute(apu_owner.V02_MIGRATION.read_text(encoding="utf-8"))
    connection.execute(
        """
        TRUNCATE agency_apu_v02_owner_migrations,
                 agency_apu_relation_claims,
                 agency_apu_attribute_claims,
                 agency_apu_source_representations,
                 agency_apu_events,
                 agency_apu_object_relations,
                 agency_apu_objects,
                 agency_apu_project_state,
                 agency_project_events,
                 agency_projects
        RESTART IDENTITY CASCADE
        """
    )
    connection.commit()
    yield connection
    connection.close()


def _project(conn, label: str) -> str:
    project_id = _id("project")
    agency_data.create_project(
        conn,
        project_id=project_id,
        code=_id(label)[:24],
        display_name=f"Projet {label}",
        actor="human:test",
        actor_kind="human",
        idempotency_key=_id("project-create"),
        attributes={"programme_summary": "Maison individuelle"},
    )
    return project_id


def _legacy_stable(project_id: str, object_id: str) -> dict:
    return {
        "stable_object_id": object_id,
        "human_ref": "Legacy opening",
        "kind": "opening",
        "proof_status": "accepted_as_support",
        "scope_type": "project",
        "scope_id": project_id,
        "matches": [],
    }


def _canonical_stable(project_id: str, object_id: str) -> dict:
    return {
        "stable_object_id": object_id,
        "project_ref": project_id,
        "object_family": "element",
        "nomenclature": {"display_name": "Porte 01"},
    }


def test_server_rejects_partial_legacy_identity_row_after_not_null_relaxation(conn) -> None:
    project_id = _project(conn, "legacy-partial")
    object_id = _id("legacy-object")

    with pytest.raises(psycopg.errors.CheckViolation):
        with conn.transaction():
            conn.execute(
                """
                INSERT INTO agency_apu_objects (
                    object_id, project_id, object_kind, proof_status,
                    stable_object, payload_digest, created_by
                ) VALUES (%s, %s, NULL, NULL, %s, %s, %s)
                """,
                (
                    object_id,
                    project_id,
                    Jsonb(_legacy_stable(project_id, object_id)),
                    "legacy-partial-digest",
                    "human:test",
                ),
            )


def test_server_rejects_partial_canonical_identity_row(conn) -> None:
    project_id = _project(conn, "canonical-partial")
    object_id = _id("canonical-object")

    with pytest.raises(psycopg.errors.CheckViolation):
        with conn.transaction():
            conn.execute(
                """
                INSERT INTO agency_apu_objects (
                    object_id, project_id, object_family,
                    canonical_stable_object, canonical_payload_digest,
                    payload_digest, created_by
                ) VALUES (%s, %s, NULL, %s, NULL, %s, %s)
                """,
                (
                    object_id,
                    project_id,
                    Jsonb(_canonical_stable(project_id, object_id)),
                    "canonical-partial-digest",
                    "human:test",
                ),
            )


def test_v02_authority_separates_contract_pin_from_conceptual_doctrine(conn) -> None:
    project_id = _project(conn, "authority-migration")
    object_id = _id("legacy-opening")
    apu_owner.store_reviewed_dossier(
        conn,
        project_id=project_id,
        objects=[{"stable_object": _legacy_stable(project_id, object_id)}],
        relations=[],
        review_ref="review:legacy-authority",
        actor="human:architect",
        idempotency_key="legacy-authority-bootstrap",
    )

    legacy_state = conn.execute(
        """
        SELECT model_version, model_authority_ref, model_doctrine_ref
          FROM agency_apu_project_state
         WHERE project_id = %s
        """,
        (project_id,),
    ).fetchone()
    assert legacy_state == (1, None, None)

    apu_owner.migrate_project_to_v02(
        conn,
        project_id=project_id,
        actor="human:architect",
        idempotency_key="authority-migration",
    )
    migrated_state = conn.execute(
        """
        SELECT model_version, model_authority_ref, model_doctrine_ref
          FROM agency_apu_project_state
         WHERE project_id = %s
        """,
        (project_id,),
    ).fetchone()
    assert migrated_state == (2, CONTRACT_AUTHORITY_REF, MODEL_DOCTRINE_REF)


def test_reviewed_v02_bootstrap_gets_both_authority_refs(conn) -> None:
    project_id = _project(conn, "authority-bootstrap")
    object_id = _id("v02-object")
    apu_owner.store_reviewed_v02_dossier(
        conn,
        project_id=project_id,
        stable_objects=[_canonical_stable(project_id, object_id)],
        source_representations=[],
        attribute_claims=[],
        relation_claims=[],
        review_ref="review:v02-authority",
        actor="human:architect",
        idempotency_key="v02-authority-bootstrap",
    )

    state = conn.execute(
        """
        SELECT model_version, model_authority_ref, model_doctrine_ref
          FROM agency_apu_project_state
         WHERE project_id = %s
        """,
        (project_id,),
    ).fetchone()
    assert state == (2, CONTRACT_AUTHORITY_REF, MODEL_DOCTRINE_REF)
