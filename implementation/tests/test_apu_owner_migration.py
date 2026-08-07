"""PostgreSQL acceptance contract for the H4c Project Anatomy V0.2 owner.

These tests deliberately define the owner migration before implementation. H4c
must preserve H1/H2/H3 history and stable ids while making V0.2 primitives the
only canonical projection for migrated/new V0.2 projects.
"""

from __future__ import annotations

import uuid

import psycopg
import pytest

from mvp_vertical import agency_data, apu_owner, store


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


def _legacy_object(project_id: str, object_id: str, *, kind: str = "opening") -> dict:
    return {
        "stable_object": {
            "stable_object_id": object_id,
            "human_ref": f"Legacy {object_id}",
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
                    "match_evidence": ["historical-reviewed-match"],
                }
            ],
        },
        "object_identity": {
            "stable_id": object_id,
            "object_kind": kind,
            "internal_code": f"CODE-{object_id[-6:]}",
            "current_display_name": f"Objet {object_id}",
            "aliases": [f"alias-{object_id}"],
            "source_refs": [
                {"source": "legacy-plan-A", "value": f"ref-{object_id}"}
            ],
        },
    }


def _legacy_relation(origin: str, target: str) -> dict:
    return {
        "relation_id": _id("legacy-relation"),
        "type": "hosted_by",
        "from": origin,
        "to": target,
        "source_refs": ["legacy-plan-A"],
    }


def _bootstrap_legacy(conn, project_id: str) -> tuple[str, str]:
    opening = _id("apu-opening")
    boundary = _id("apu-boundary")
    apu_owner.store_reviewed_dossier(
        conn,
        project_id=project_id,
        objects=[
            _legacy_object(project_id, opening, kind="opening"),
            _legacy_object(project_id, boundary, kind="boundary"),
        ],
        relations=[_legacy_relation(opening, boundary)],
        review_ref="review:architect:legacy",
        actor="human:architect",
        idempotency_key=_id("legacy-bootstrap"),
    )
    return opening, boundary


def _v02_stable(project_id: str, object_id: str) -> dict:
    return {
        "stable_object_id": object_id,
        "project_ref": project_id,
        "object_family": "element",
        "nomenclature": {
            "internal_code": "PORTE-01",
            "display_name": "Porte 01",
            "aliases": ["P01"],
        },
    }


def _v02_representation(project_id: str, representation_id: str) -> dict:
    return {
        "representation_id": representation_id,
        "project_ref": project_id,
        "source_artifact_ref": "SRC-DRAWING-001",
        "source_kind": "drawing",
        "identifiers": [
            {"scheme": "drawing.fragment", "value": "door-polygon-01"}
        ],
        "observed_at": "2026-08-07T12:00:00Z",
        "binding_ref": "binding.drawing.reviewed",
        "adapter_version": "0.2-fixture",
        "freshness_token": "drawing-revision-A",
        "proof_status": "candidate",
    }


def _v02_attribute_claim(object_id: str, claim_id: str) -> dict:
    return {
        "attribute_claim_id": claim_id,
        "subject_ref": {"entity_type": "stable_object", "entity_id": object_id},
        "attribute_key": "geometry.width",
        "value": {"value_type": "number", "value": 900, "unit": "mm"},
        "assertion_mode": "human_asserted",
        "source_authority": "project_working_document",
        "proof_status": "candidate",
    }


def _v02_identity_relation(representation_id: str, object_id: str, claim_id: str) -> dict:
    return {
        "relation_claim_id": claim_id,
        "subject_ref": {
            "entity_type": "source_representation",
            "entity_id": representation_id,
        },
        "relation_type": "identity.represents",
        "object_ref": {"entity_type": "stable_object", "entity_id": object_id},
        "assertion_mode": "proposed",
        "source_authority": "model_interpretation_candidate",
        "proof_status": "candidate",
        "source_representation_refs": [representation_id],
    }


def test_legacy_owner_migrates_to_v02_without_rewriting_history_or_revisions(conn) -> None:
    project_id = _project(conn, "migration")
    opening, boundary = _bootstrap_legacy(conn, project_id)

    before = apu_owner.get_project_anatomy(conn, project_id=project_id)
    before_objects = {
        item["object_id"]: item["revision"] for item in before["objects"]
    }
    event_ids_before = [
        item["event_id"] for item in apu_owner.list_apu_events(conn, project_id=project_id)
    ]

    migrated = apu_owner.migrate_project_to_v02(
        conn,
        project_id=project_id,
        actor="human:architect",
        idempotency_key="migrate-project-to-v02",
    )
    projection = apu_owner.get_project_anatomy_v02(conn, project_id=project_id)

    assert migrated["status"] == "migrated"
    assert projection["model_version"] == 2
    assert projection["owner_revision"] == before["owner_revision"]
    assert {
        item["stable_object"]["stable_object_id"]: item["revision"]
        for item in projection["stable_objects"]
    } == before_objects
    assert {item["stable_object"]["stable_object_id"] for item in projection["stable_objects"]} == {
        opening,
        boundary,
    }
    assert all(item["stable_object"]["project_ref"] == project_id for item in projection["stable_objects"])
    assert all(item["stable_object"]["object_family"] == "element" for item in projection["stable_objects"])

    # V0.1 inline matches and object_relation rows remain compatibility history;
    # migration cannot invent V0.2 source observations or claims.
    assert projection["source_representations"] == []
    assert projection["attribute_claims"] == []
    assert projection["relation_claims"] == []
    assert projection["compatibility"]["legacy_inline_match_count"] == 2
    assert projection["compatibility"]["legacy_relation_count"] == 1
    assert projection["compatibility"]["canonicalized_legacy_matches"] == 0
    assert projection["compatibility"]["canonicalized_legacy_relations"] == 0
    assert projection["compatibility"]["canonical_emission_allowed_for_legacy"] is False

    assert [
        item["event_id"] for item in apu_owner.list_apu_events(conn, project_id=project_id)
    ] == event_ids_before
    migration_rows = apu_owner.list_v02_owner_migrations(conn, project_id=project_id)
    assert len(migration_rows) == 1
    assert migration_rows[0]["owner_revision"] == before["owner_revision"]
    assert migration_rows[0]["from_version"] == 1
    assert migration_rows[0]["to_version"] == 2


def test_v02_migration_replay_is_exact_and_different_key_conflicts(conn) -> None:
    project_id = _project(conn, "migration-replay")
    _bootstrap_legacy(conn, project_id)

    first = apu_owner.migrate_project_to_v02(
        conn,
        project_id=project_id,
        actor="human:architect",
        idempotency_key="same-migration-key",
    )
    replay = apu_owner.migrate_project_to_v02(
        conn,
        project_id=project_id,
        actor="human:architect",
        idempotency_key="same-migration-key",
    )
    assert replay == first

    with pytest.raises(apu_owner.ApuOwnerConflict, match="already migrated"):
        apu_owner.migrate_project_to_v02(
            conn,
            project_id=project_id,
            actor="human:architect",
            idempotency_key="different-migration-key",
        )


def test_reviewed_v02_bootstrap_uses_same_stable_identity_owner(conn) -> None:
    project_id = _project(conn, "v02-bootstrap")
    object_id = _id("apu-door")
    representation_id = _id("representation")
    attribute_claim_id = _id("attribute-claim")
    relation_claim_id = _id("relation-claim")

    projection = apu_owner.store_reviewed_v02_dossier(
        conn,
        project_id=project_id,
        stable_objects=[_v02_stable(project_id, object_id)],
        source_representations=[
            _v02_representation(project_id, representation_id)
        ],
        attribute_claims=[_v02_attribute_claim(object_id, attribute_claim_id)],
        relation_claims=[
            _v02_identity_relation(representation_id, object_id, relation_claim_id)
        ],
        review_ref="review:architect:v02-bootstrap",
        actor="human:architect",
        idempotency_key="v02-bootstrap-key",
    )

    assert projection["model_version"] == 2
    assert projection["owner_revision"] == 1
    assert projection["stable_objects"][0]["object_id"] == object_id
    assert projection["stable_objects"][0]["stable_object"] == _v02_stable(project_id, object_id)
    assert projection["source_representations"][0]["representation_id"] == representation_id
    assert projection["attribute_claims"][0]["attribute_claim_id"] == attribute_claim_id
    assert projection["relation_claims"][0]["relation_claim_id"] == relation_claim_id

    # H3 keeps resolving the exact same stable identity table/key.
    row = conn.execute(
        "SELECT project_id, object_id FROM agency_apu_objects WHERE object_id = %s",
        (object_id,),
    ).fetchone()
    assert row == (project_id, object_id)


def test_v02_bootstrap_refuses_cross_project_source_and_claim_refs(conn) -> None:
    project_a = _project(conn, "v02-a")
    project_b = _project(conn, "v02-b")
    object_id = _id("apu-door")
    representation_id = _id("representation")

    foreign_representation = _v02_representation(project_b, representation_id)
    with pytest.raises(apu_owner.ApuOwnerError, match="exact Project"):
        apu_owner.store_reviewed_v02_dossier(
            conn,
            project_id=project_a,
            stable_objects=[_v02_stable(project_a, object_id)],
            source_representations=[foreign_representation],
            attribute_claims=[],
            relation_claims=[],
            review_ref="review:cross-project",
            actor="human:architect",
            idempotency_key="v02-cross-project",
        )


def test_v02_claim_tables_are_append_only(conn) -> None:
    project_id = _project(conn, "append-only")
    object_id = _id("apu-door")
    claim_id = _id("attribute-claim")
    apu_owner.store_reviewed_v02_dossier(
        conn,
        project_id=project_id,
        stable_objects=[_v02_stable(project_id, object_id)],
        source_representations=[],
        attribute_claims=[_v02_attribute_claim(object_id, claim_id)],
        relation_claims=[],
        review_ref="review:append-only",
        actor="human:architect",
        idempotency_key="v02-append-only",
    )

    with pytest.raises(psycopg.errors.RaiseException, match="append-only"):
        with conn.transaction():
            conn.execute(
                "UPDATE agency_apu_attribute_claims SET created_by = 'other' WHERE claim_id = %s",
                (claim_id,),
            )


def test_legacy_h2_match_write_is_closed_after_v02_migration(conn) -> None:
    project_id = _project(conn, "h2-close")
    object_id, _ = _bootstrap_legacy(conn, project_id)
    apu_owner.migrate_project_to_v02(
        conn,
        project_id=project_id,
        actor="human:architect",
        idempotency_key="migrate-before-h2",
    )

    with pytest.raises(apu_owner.ApuOwnerConflict, match="V0.2"):
        apu_owner.apply_source_match(
            conn,
            command={
                "operation": "add_match_to_existing_object",
                "project_ref": project_id,
                "target_stable_object_ref": object_id,
                "source_candidate_ref": "candidate-new",
                "command_id": "legacy-command-after-v02",
                "payload_digest": "a" * 64,
                "expected_owner_revision": 1,
                "expected_object_revision": 1,
            },
            authorization_id="authorization-legacy",
            actor="human:architect",
            idempotency_key="legacy-apply-after-v02",
        )
