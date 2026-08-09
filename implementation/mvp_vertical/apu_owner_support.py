"""Internal implementation support for the single executable APU owner.

This module is not a second authority or API surface. ``apu_owner`` remains the
only owner-facing module and delegates its H4c V0.2 migration/projection helpers
here to keep the legacy H1/H2 implementation readable.
"""

from __future__ import annotations

import uuid
from typing import Any

from psycopg.rows import dict_row
from psycopg.types.json import Jsonb


V02_AUTHORITY_REF = "ifanjuang/Pantheon-Next@98be3a1dd07be6b6ee2847127d698618f6ff703a"
LEGACY_KIND_TO_FAMILY = {
    "space": "spatial",
    "level": "spatial",
    "path": "spatial",
    "vertical_connection": "spatial",
    "boundary": "element",
    "opening": "element",
    "grid": "datum",
}
SUPPORTED_OWNER_ENTITY_TYPES = {"stable_object", "source_representation"}


def _owner():
    # Lazy import prevents an import cycle while keeping apu_owner as the public
    # authority surface.
    from . import apu_owner

    return apu_owner


def _required(value: Any, field: str) -> str:
    owner = _owner()
    return owner._required(value, field)


def _digest(value: Any) -> str:
    return _owner()._digest(value)


def _v02_source_match_effect(
    command: dict[str, Any],
    *,
    project_id: str,
    object_id: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    owner = _owner()
    if command.get("target_model_version") != 2:
        raise owner.ApuOwnerConflict(
            "legacy add_match_to_existing_object is closed after Project Anatomy V0.2 migration"
        )
    representation = command.get("source_representation")
    relation = command.get("identity_relation_claim")
    if not isinstance(representation, dict) or not isinstance(relation, dict):
        raise owner.ApuOwnerError(
            "V0.2 source match requires exact source representation and identity relation payloads"
        )
    owner._validate_v02("source_representation", representation)
    owner._validate_v02("relation_claim", relation)

    representation_id = _required(
        representation.get("representation_id"), "source_representation.representation_id"
    )
    if representation_id != command.get("source_candidate_ref"):
        raise owner.ApuOwnerError(
            "V0.2 source representation must equal source_candidate_ref"
        )
    if representation.get("project_ref") != project_id:
        raise owner.ApuOwnerError(
            "V0.2 source representation must carry the exact Project"
        )
    if representation.get("source_artifact_ref") != command.get("source_artifact_ref"):
        raise owner.ApuOwnerError(
            "V0.2 source representation must carry the exact source artifact"
        )
    if representation.get("proof_status") != "candidate":
        raise owner.ApuOwnerError("V0.2 applied source representation must remain candidate")

    if relation.get("relation_type") != "identity.represents":
        raise owner.ApuOwnerError("V0.2 source match must use identity.represents")
    if relation.get("assertion_mode") != "proposed":
        raise owner.ApuOwnerError("V0.2 source match assertion must remain proposed")
    if relation.get("source_authority") != "model_interpretation_candidate":
        raise owner.ApuOwnerError(
            "V0.2 source match must retain candidate source authority"
        )
    if relation.get("proof_status") != "candidate":
        raise owner.ApuOwnerError("V0.2 source match relation must remain candidate")
    if relation.get("subject_ref") != {
        "entity_type": "source_representation",
        "entity_id": representation_id,
    }:
        raise owner.ApuOwnerError(
            "V0.2 identity relation must start from the exact source representation"
        )
    if relation.get("object_ref") != {
        "entity_type": "stable_object",
        "entity_id": object_id,
    }:
        raise owner.ApuOwnerError(
            "V0.2 identity relation must target the selected stable object"
        )
    if relation.get("source_representation_refs") != [representation_id]:
        raise owner.ApuOwnerError(
            "V0.2 identity relation must retain its exact source representation"
        )
    if command.get("certainty") and relation.get("certainty") != command.get("certainty"):
        raise owner.ApuOwnerError(
            "V0.2 identity relation certainty must equal the reviewed mapping"
        )
    return dict(representation), dict(relation)


def store_v02_source_match_effect(
    conn,
    *,
    command: dict[str, Any],
    project_id: str,
    object_id: str,
    actor: str,
) -> dict[str, Any]:
    """Append the exact V0.2 source and candidate identity relation effect."""
    owner = _owner()
    representation, relation = _v02_source_match_effect(
        command,
        project_id=project_id,
        object_id=object_id,
    )
    representation_id = representation["representation_id"]
    representation_digest = _digest(representation)
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT * FROM agency_apu_source_representations "
            "WHERE representation_id = %s FOR UPDATE",
            (representation_id,),
        )
        existing_representation = cur.fetchone()
    if existing_representation is None:
        conn.execute(
            """
            INSERT INTO agency_apu_source_representations (
                representation_id, project_id, source_kind, proof_status,
                representation_payload, payload_digest, revision, created_by
            ) VALUES (%s, %s, %s, %s, %s, %s, 1, %s)
            """,
            (
                representation_id,
                project_id,
                representation["source_kind"],
                representation["proof_status"],
                Jsonb(representation),
                representation_digest,
                actor,
            ),
        )
        representation_revision = 1
        representation_reused = False
    else:
        existing = dict(existing_representation)
        if (
            existing["project_id"] != project_id
            or existing["payload_digest"] != representation_digest
            or existing["representation_payload"] != representation
        ):
            raise owner.ApuOwnerConflict(
                "V0.2 source representation identity belongs to different content"
            )
        representation_revision = int(existing["revision"])
        representation_reused = True

    relation_id = _required(
        relation.get("relation_claim_id"), "identity_relation_claim.relation_claim_id"
    )
    with conn.cursor() as cur:
        cur.execute(
            "SELECT 1 FROM agency_apu_relation_claims WHERE claim_id = %s",
            (relation_id,),
        )
        if cur.fetchone() is not None:
            raise owner.ApuOwnerConflict("V0.2 identity relation claim already exists")
    conn.execute(
        """
        INSERT INTO agency_apu_relation_claims (
            claim_id, project_id, subject_entity_type, subject_entity_id,
            relation_type, object_entity_type, object_entity_id, assertion_mode,
            source_authority, proof_status, claim_payload, payload_digest, created_by
        ) VALUES (%s, %s, 'source_representation', %s, 'identity.represents',
                  'stable_object', %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            relation_id,
            project_id,
            representation_id,
            object_id,
            relation["assertion_mode"],
            relation["source_authority"],
            relation["proof_status"],
            Jsonb(relation),
            _digest(relation),
            actor,
        ),
    )
    return {
        "source_representation": representation | {"revision": representation_revision},
        "identity_relation_claim": relation,
        "source_representation_reused": representation_reused,
    }


def get_v02_source_match_effect(
    conn,
    *,
    command: dict[str, Any],
    project_id: str,
    object_id: str,
) -> dict[str, Any]:
    representation, relation = _v02_source_match_effect(
        command,
        project_id=project_id,
        object_id=object_id,
    )
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT representation_payload, revision "
            "FROM agency_apu_source_representations WHERE representation_id = %s",
            (representation["representation_id"],),
        )
        representation_row = cur.fetchone()
        cur.execute(
            "SELECT claim_payload FROM agency_apu_relation_claims WHERE claim_id = %s",
            (relation["relation_claim_id"],),
        )
        relation_row = cur.fetchone()
    if representation_row is None or relation_row is None:
        raise _owner().ApuOwnerConflict("V0.2 source match event has incomplete canonical effect")
    return {
        "source_representation": dict(representation_row["representation_payload"])
        | {"revision": int(representation_row["revision"])},
        "identity_relation_claim": dict(relation_row["claim_payload"]),
        "source_representation_reused": True,
    }


def _legacy_stable_to_v02(row: dict[str, Any]) -> dict[str, Any]:
    owner = _owner()
    legacy = row.get("stable_object") or {}
    object_id = _required(row.get("object_id"), "object_id")
    project_id = _required(row.get("project_id"), "project_id")
    kind = _required(row.get("object_kind") or legacy.get("kind"), "object_kind")
    family = LEGACY_KIND_TO_FAMILY.get(kind)
    if family is None:
        raise owner.ApuOwnerError(
            f"legacy APU object {object_id} has no reviewed V0.2 family mapping: {kind}"
        )

    identity = row.get("object_identity") or {}
    nomenclature: dict[str, Any] = {}
    internal_code = str(identity.get("internal_code") or "").strip()
    display_name = str(identity.get("current_display_name") or legacy.get("human_ref") or "").strip()
    aliases = [
        str(value).strip()
        for value in (identity.get("aliases") or [])
        if str(value).strip()
    ]
    if internal_code:
        nomenclature["internal_code"] = internal_code
    if display_name:
        nomenclature["display_name"] = display_name
    if aliases:
        nomenclature["aliases"] = list(dict.fromkeys(aliases))

    canonical: dict[str, Any] = {
        "stable_object_id": object_id,
        "project_ref": project_id,
        "object_family": family,
    }
    if nomenclature:
        canonical["nomenclature"] = nomenclature
    owner._validate_v02("stable_object", canonical)
    return canonical


def _legacy_inline_match_count(rows: list[dict[str, Any]]) -> int:
    return sum(len((row.get("stable_object") or {}).get("matches") or []) for row in rows)


def _migration_result(conn, migration_row: dict[str, Any]) -> dict[str, Any]:
    return {
        "status": "migrated",
        "migration": dict(migration_row),
        "projection": get_project_anatomy_v02(
            conn,
            project_id=migration_row["project_id"],
        ),
    }


def list_v02_owner_migrations(conn, *, project_id: str) -> list[dict[str, Any]]:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT *
              FROM agency_apu_v02_owner_migrations
             WHERE project_id = %s
             ORDER BY occurred_at, migration_id
            """,
            (project_id,),
        )
        return [dict(row) for row in cur.fetchall()]


def migrate_project_to_v02(
    conn,
    *,
    project_id: str,
    actor: str,
    idempotency_key: str,
) -> dict[str, Any]:
    owner = _owner()
    project_id = _required(project_id, "project_id")
    actor = _required(actor, "actor")
    key = _required(idempotency_key, "idempotency_key")

    with conn.transaction():
        state = owner._project_state(conn, project_id, lock=True)
        if state is None:
            raise owner.ApuOwnerNotFound(
                f"Project has no executable APU owner state: {project_id}"
            )

        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "SELECT * FROM agency_apu_v02_owner_migrations WHERE idempotency_key = %s",
                (key,),
            )
            replay = cur.fetchone()
            if replay is not None:
                if replay["project_id"] != project_id:
                    raise owner.ApuOwnerConflict(
                        "V0.2 owner migration idempotency key belongs to another Project"
                    )
                return _migration_result(conn, dict(replay))

        if int(state.get("model_version") or 1) == 2:
            raise owner.ApuOwnerConflict(
                "Project Anatomy owner is already migrated to V0.2"
            )
        if int(state.get("model_version") or 1) != 1:
            raise owner.ApuOwnerConflict("unsupported Project Anatomy owner model version")

        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                """
                SELECT *
                  FROM agency_apu_objects
                 WHERE project_id = %s
                 ORDER BY object_id
                 FOR UPDATE
                """,
                (project_id,),
            )
            object_rows = [dict(row) for row in cur.fetchall()]
            cur.execute(
                "SELECT COUNT(*) AS count FROM agency_apu_object_relations WHERE project_id = %s",
                (project_id,),
            )
            legacy_relation_count = int(cur.fetchone()["count"])

        canonical_objects: list[dict[str, Any]] = []
        for row in object_rows:
            if row.get("canonical_stable_object") is not None:
                raise owner.ApuOwnerConflict(
                    "legacy Project already contains V0.2 canonical object payloads"
                )
            canonical = _legacy_stable_to_v02(row)
            canonical_objects.append(canonical)
            conn.execute(
                """
                UPDATE agency_apu_objects
                   SET object_family = %s,
                       canonical_stable_object = %s,
                       canonical_payload_digest = %s
                 WHERE project_id = %s AND object_id = %s
                """,
                (
                    canonical["object_family"],
                    Jsonb(canonical),
                    _digest(canonical),
                    project_id,
                    row["object_id"],
                ),
            )

        compatibility_report = {
            "legacy_inline_match_count": _legacy_inline_match_count(object_rows),
            "legacy_relation_count": legacy_relation_count,
            "canonicalized_legacy_matches": 0,
            "canonicalized_legacy_relations": 0,
            "canonical_emission_allowed_for_legacy": False,
            "stable_identity_rows_migrated": len(canonical_objects),
            "source_representations_created": 0,
            "attribute_claims_created": 0,
            "relation_claims_created": 0,
            "owner_revision_preserved": int(state["revision"]),
            "object_revisions_preserved": {
                row["object_id"]: int(row["revision"]) for row in object_rows
            },
            "legacy_events_preserved": True,
            "authority_transfer": False,
        }
        migration_payload = {
            "project_ref": project_id,
            "from_version": 1,
            "to_version": 2,
            "owner_revision": int(state["revision"]),
            "source_authority_ref": V02_AUTHORITY_REF,
            "compatibility": compatibility_report,
        }
        migration_id = f"apu-v02-migration.{_digest(migration_payload)[:24]}"
        payload_digest = _digest(migration_payload)

        conn.execute(
            """
            UPDATE agency_apu_project_state
               SET model_version = 2,
                   model_authority_ref = %s
             WHERE project_id = %s AND model_version = 1
            """,
            (V02_AUTHORITY_REF, project_id),
        )
        conn.execute(
            """
            INSERT INTO agency_apu_v02_owner_migrations (
                migration_id, project_id, from_version, to_version,
                owner_revision, source_authority_ref, compatibility_report,
                payload_digest, actor, idempotency_key
            ) VALUES (%s, %s, 1, 2, %s, %s, %s, %s, %s, %s)
            """,
            (
                migration_id,
                project_id,
                int(state["revision"]),
                V02_AUTHORITY_REF,
                Jsonb(compatibility_report),
                payload_digest,
                actor,
                key,
            ),
        )
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "SELECT * FROM agency_apu_v02_owner_migrations WHERE migration_id = %s",
                (migration_id,),
            )
            stored = dict(cur.fetchone())

    return _migration_result(conn, stored)


def _normalize_v02_dossier(
    *,
    project_id: str,
    stable_objects: list[dict[str, Any]],
    source_representations: list[dict[str, Any]],
    attribute_claims: list[dict[str, Any]],
    relation_claims: list[dict[str, Any]],
    review_ref: str,
) -> dict[str, Any]:
    owner = _owner()
    if not isinstance(stable_objects, list) or not stable_objects:
        raise owner.ApuOwnerError("stable_objects must be a non-empty array")
    for name, value in (
        ("source_representations", source_representations),
        ("attribute_claims", attribute_claims),
        ("relation_claims", relation_claims),
    ):
        if not isinstance(value, list):
            raise owner.ApuOwnerError(f"{name} must be an array")

    object_ids: set[str] = set()
    representations: set[str] = set()
    attribute_ids: set[str] = set()
    relation_ids: set[str] = set()

    normalized_stable: list[dict[str, Any]] = []
    for item in stable_objects:
        if not isinstance(item, dict):
            raise owner.ApuOwnerError("every V0.2 stable object must be an object")
        owner._validate_v02("stable_object", item)
        object_id = _required(item.get("stable_object_id"), "stable_object_id")
        if item.get("project_ref") != project_id:
            raise owner.ApuOwnerError(
                f"V0.2 stable object {object_id} must carry the exact Project"
            )
        if object_id in object_ids:
            raise owner.ApuOwnerError(f"duplicate V0.2 stable_object_id: {object_id}")
        object_ids.add(object_id)
        normalized_stable.append(dict(item))

    normalized_representations: list[dict[str, Any]] = []
    for item in source_representations:
        if not isinstance(item, dict):
            raise owner.ApuOwnerError("every V0.2 source representation must be an object")
        owner._validate_v02("source_representation", item)
        representation_id = _required(item.get("representation_id"), "representation_id")
        if item.get("project_ref") != project_id:
            raise owner.ApuOwnerError(
                f"V0.2 source representation {representation_id} must carry the exact Project"
            )
        if representation_id in representations:
            raise owner.ApuOwnerError(
                f"duplicate V0.2 source representation id: {representation_id}"
            )
        representations.add(representation_id)
        normalized_representations.append(dict(item))

    def check_entity(ref: Any, label: str) -> None:
        if not isinstance(ref, dict):
            raise owner.ApuOwnerError(f"{label} must be an APU entity ref")
        entity_type = _required(ref.get("entity_type"), f"{label}.entity_type")
        entity_id = _required(ref.get("entity_id"), f"{label}.entity_id")
        if entity_type not in SUPPORTED_OWNER_ENTITY_TYPES:
            raise owner.ApuOwnerError(
                f"H4c executable owner does not yet persist {entity_type} entities"
            )
        if entity_type == "stable_object" and entity_id not in object_ids:
            raise owner.ApuOwnerError(f"{label} references an unknown stable object")
        if entity_type == "source_representation" and entity_id not in representations:
            raise owner.ApuOwnerError(f"{label} references an unknown source representation")

    normalized_attributes: list[dict[str, Any]] = []
    for item in attribute_claims:
        if not isinstance(item, dict):
            raise owner.ApuOwnerError("every V0.2 attribute claim must be an object")
        owner._validate_v02("attribute_claim", item)
        claim_id = _required(item.get("attribute_claim_id"), "attribute_claim_id")
        if claim_id in attribute_ids:
            raise owner.ApuOwnerError(f"duplicate V0.2 attribute claim id: {claim_id}")
        attribute_ids.add(claim_id)
        check_entity(item.get("subject_ref"), "attribute_claim.subject_ref")
        for representation_ref in item.get("source_representation_refs") or []:
            if representation_ref not in representations:
                raise owner.ApuOwnerError(
                    "attribute_claim source_representation_ref is outside the reviewed dossier"
                )
        normalized_attributes.append(dict(item))

    normalized_relations: list[dict[str, Any]] = []
    for item in relation_claims:
        if not isinstance(item, dict):
            raise owner.ApuOwnerError("every V0.2 relation claim must be an object")
        owner._validate_v02("relation_claim", item)
        claim_id = _required(item.get("relation_claim_id"), "relation_claim_id")
        if claim_id in relation_ids:
            raise owner.ApuOwnerError(f"duplicate V0.2 relation claim id: {claim_id}")
        relation_ids.add(claim_id)
        check_entity(item.get("subject_ref"), "relation_claim.subject_ref")
        check_entity(item.get("object_ref"), "relation_claim.object_ref")
        for representation_ref in item.get("source_representation_refs") or []:
            if representation_ref not in representations:
                raise owner.ApuOwnerError(
                    "relation_claim source_representation_ref is outside the reviewed dossier"
                )
        normalized_relations.append(dict(item))

    normalized_stable.sort(key=lambda item: item["stable_object_id"])
    normalized_representations.sort(key=lambda item: item["representation_id"])
    normalized_attributes.sort(key=lambda item: item["attribute_claim_id"])
    normalized_relations.sort(key=lambda item: item["relation_claim_id"])
    return {
        "project_ref": project_id,
        "review_ref": review_ref,
        "stable_objects": normalized_stable,
        "source_representations": normalized_representations,
        "attribute_claims": normalized_attributes,
        "relation_claims": normalized_relations,
    }


def _insert_v02_dossier(conn, dossier: dict[str, Any], *, actor: str) -> None:
    for stable in dossier["stable_objects"]:
        digest = _digest(stable)
        conn.execute(
            """
            INSERT INTO agency_apu_objects (
                object_id, project_id, object_family,
                canonical_stable_object, canonical_payload_digest,
                payload_digest, created_by
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                stable["stable_object_id"],
                stable["project_ref"],
                stable["object_family"],
                Jsonb(stable),
                digest,
                digest,
                actor,
            ),
        )

    for representation in dossier["source_representations"]:
        conn.execute(
            """
            INSERT INTO agency_apu_source_representations (
                representation_id, project_id, source_kind, proof_status,
                representation_payload, payload_digest, created_by
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                representation["representation_id"],
                representation["project_ref"],
                representation["source_kind"],
                representation["proof_status"],
                Jsonb(representation),
                _digest(representation),
                actor,
            ),
        )

    for claim in dossier["attribute_claims"]:
        subject = claim["subject_ref"]
        conn.execute(
            """
            INSERT INTO agency_apu_attribute_claims (
                claim_id, project_id, subject_entity_type, subject_entity_id,
                attribute_key, assertion_mode, source_authority, proof_status,
                claim_payload, payload_digest, created_by
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                claim["attribute_claim_id"],
                dossier["project_ref"],
                subject["entity_type"],
                subject["entity_id"],
                claim["attribute_key"],
                claim["assertion_mode"],
                claim["source_authority"],
                claim["proof_status"],
                Jsonb(claim),
                _digest(claim),
                actor,
            ),
        )

    for claim in dossier["relation_claims"]:
        subject = claim["subject_ref"]
        target = claim["object_ref"]
        conn.execute(
            """
            INSERT INTO agency_apu_relation_claims (
                claim_id, project_id, subject_entity_type, subject_entity_id,
                relation_type, object_entity_type, object_entity_id,
                assertion_mode, source_authority, proof_status,
                claim_payload, payload_digest, created_by
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                claim["relation_claim_id"],
                dossier["project_ref"],
                subject["entity_type"],
                subject["entity_id"],
                claim["relation_type"],
                target["entity_type"],
                target["entity_id"],
                claim["assertion_mode"],
                claim["source_authority"],
                claim["proof_status"],
                Jsonb(claim),
                _digest(claim),
                actor,
            ),
        )


def store_reviewed_v02_dossier(
    conn,
    *,
    project_id: str,
    stable_objects: list[dict[str, Any]],
    source_representations: list[dict[str, Any]],
    attribute_claims: list[dict[str, Any]],
    relation_claims: list[dict[str, Any]],
    review_ref: str,
    actor: str,
    idempotency_key: str,
) -> dict[str, Any]:
    owner = _owner()
    project_id = _required(project_id, "project_id")
    review_ref = _required(review_ref, "review_ref")
    actor = _required(actor, "actor")
    key = _required(idempotency_key, "idempotency_key")
    dossier = _normalize_v02_dossier(
        project_id=project_id,
        stable_objects=stable_objects,
        source_representations=source_representations,
        attribute_claims=attribute_claims,
        relation_claims=relation_claims,
        review_ref=review_ref,
    )
    payload_digest = _digest(dossier)

    with conn.transaction():
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "SELECT project_id, event_type, payload_digest FROM agency_apu_events WHERE idempotency_key = %s",
                (key,),
            )
            replay = cur.fetchone()
        if replay is not None:
            if (
                replay["project_id"] != project_id
                or replay["event_type"] != "reviewed_dossier_imported"
                or replay["payload_digest"] != payload_digest
            ):
                raise owner.ApuOwnerConflict("APU idempotency key belongs to another effect")
            return get_project_anatomy_v02(conn, project_id=project_id)

        if not owner._project_exists(conn, project_id):
            raise owner.ApuOwnerNotFound(f"unknown Project: {project_id}")
        if owner._project_state(conn, project_id) is not None:
            raise owner.ApuOwnerConflict("Project APU owner is already initialized")

        conn.execute(
            """
            INSERT INTO agency_apu_project_state (
                project_id, revision, created_by, model_version, model_authority_ref
            ) VALUES (%s, 1, %s, 2, %s)
            """,
            (project_id, actor, V02_AUTHORITY_REF),
        )
        _insert_v02_dossier(conn, dossier, actor=actor)
        conn.execute(
            """
            INSERT INTO agency_apu_events (
                event_id, project_id, event_type, expected_revision,
                resulting_revision, actor, idempotency_key, payload_digest, payload
            ) VALUES (%s, %s, 'reviewed_dossier_imported', 0, 1, %s, %s, %s, %s)
            """,
            (
                f"apu-event-{uuid.uuid4().hex}",
                project_id,
                actor,
                key,
                payload_digest,
                Jsonb(
                    {
                        "review_ref": review_ref,
                        "model_version": 2,
                        "stable_object_refs": [
                            item["stable_object_id"] for item in dossier["stable_objects"]
                        ],
                        "source_representation_refs": [
                            item["representation_id"]
                            for item in dossier["source_representations"]
                        ],
                        "attribute_claim_refs": [
                            item["attribute_claim_id"] for item in dossier["attribute_claims"]
                        ],
                        "relation_claim_refs": [
                            item["relation_claim_id"] for item in dossier["relation_claims"]
                        ],
                        "automatic_creation": False,
                        "runtime_write": False,
                    }
                ),
            ),
        )
    return get_project_anatomy_v02(conn, project_id=project_id)


def get_project_anatomy_v02(conn, *, project_id: str) -> dict[str, Any]:
    owner = _owner()
    project_id = _required(project_id, "project_id")
    state = owner._project_state(conn, project_id)
    if state is None:
        raise owner.ApuOwnerNotFound(f"Project has no executable APU owner state: {project_id}")
    if int(state.get("model_version") or 1) != 2:
        raise owner.ApuOwnerConflict("Project Anatomy owner is not migrated to V0.2")

    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT * FROM agency_apu_objects
             WHERE project_id = %s
               AND canonical_stable_object IS NOT NULL
               AND retired_at IS NULL
             ORDER BY object_id
            """,
            (project_id,),
        )
        object_rows = [dict(row) for row in cur.fetchall()]
        cur.execute(
            "SELECT * FROM agency_apu_source_representations WHERE project_id = %s ORDER BY representation_id",
            (project_id,),
        )
        representation_rows = [dict(row) for row in cur.fetchall()]
        cur.execute(
            "SELECT * FROM agency_apu_attribute_claims WHERE project_id = %s ORDER BY claim_id",
            (project_id,),
        )
        attribute_rows = [dict(row) for row in cur.fetchall()]
        cur.execute(
            "SELECT * FROM agency_apu_relation_claims WHERE project_id = %s ORDER BY claim_id",
            (project_id,),
        )
        relation_rows = [dict(row) for row in cur.fetchall()]
        cur.execute(
            "SELECT COUNT(*) AS count FROM agency_apu_object_relations WHERE project_id = %s",
            (project_id,),
        )
        legacy_relation_count = int(cur.fetchone()["count"])

    legacy_inline_match_count = _legacy_inline_match_count(object_rows)
    return {
        "project_ref": project_id,
        "model_version": 2,
        "model_authority_ref": state.get("model_authority_ref"),
        "owner_revision": int(state["revision"]),
        "stable_objects": [
            {
                "object_id": row["object_id"],
                "stable_object": row["canonical_stable_object"],
                "revision": int(row["revision"]),
                "retired_at": row.get("retired_at"),
            }
            for row in object_rows
        ],
        "source_representations": [
            dict(row["representation_payload"]) | {"revision": int(row["revision"])}
            for row in representation_rows
        ],
        "attribute_claims": [dict(row["claim_payload"]) for row in attribute_rows],
        "relation_claims": [dict(row["claim_payload"]) for row in relation_rows],
        "compatibility": {
            "legacy_inline_match_count": legacy_inline_match_count,
            "legacy_relation_count": legacy_relation_count,
            "canonicalized_legacy_matches": 0,
            "canonicalized_legacy_relations": 0,
            "canonical_emission_allowed_for_legacy": False,
        },
        "authority": {
            "is_projection": True,
            "is_evidence": False,
            "is_decision": False,
            "is_memory": False,
            "canonizes_claims": False,
            "authorizes_tasks": False,
            "permits_runtime_writes": False,
            "legacy_payload_is_canonical": False,
        },
    }
