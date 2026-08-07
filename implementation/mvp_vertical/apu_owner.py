"""Project-scoped executable owner for reviewed Architecture Project Understanding data.

H1 stores an already reviewed V0.1 bootstrap dossier. H2 adds only the bounded
``add_match_to_existing_object`` mutation. H4c evolves the same owner to the
Project Anatomy V0.2 core without rewriting H1/H2 history or creating a parallel
identity store. The owner does not create stable objects automatically, admit
Evidence, canonize claims, resolve Decisions or authorize tasks.
"""

from __future__ import annotations

import hashlib
import json
import uuid
from functools import lru_cache
from pathlib import Path
from typing import Any

import jsonschema
import psycopg
import yaml
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012


MIGRATION = Path(__file__).resolve().parent / "sql" / "021_project_anatomy_owner.sql"
V02_MIGRATION = Path(__file__).resolve().parent / "sql" / "024_project_anatomy_v02_owner.sql"
VENDOR = Path(__file__).resolve().parent / "vendor" / "pantheon"
V02_AUTHORITY_REF = "ifanjuang/Pantheon-Next@98be3a1dd07be6b6ee2847127d698618f6ff703a"
AUTHORITY = {
    "is_projection": True,
    "is_evidence": False,
    "is_decision": False,
    "is_memory": False,
    "canonizes_claims": False,
    "authorizes_tasks": False,
    "permits_runtime_writes": False,
}
APPLICATION_AUTHORITY = {
    "match_recorded": True,
    "stable_identity_professionally_validated": False,
    "is_evidence": False,
    "is_decision": False,
    "is_memory": False,
    "canonizes_claims": False,
    "closes_work_issue": False,
    "resolves_decision_request": False,
    "authorizes_external_effect": False,
}


class ApuOwnerError(ValueError):
    pass


class ApuOwnerNotFound(ApuOwnerError):
    pass


class ApuOwnerConflict(ApuOwnerError):
    pass


@lru_cache(maxsize=1)
def _registry() -> Registry:
    shared = yaml.safe_load((VENDOR / "apu_shared.schema.yaml").read_text(encoding="utf-8"))
    resource = Resource.from_contents(shared, default_specification=DRAFT202012)
    return Registry().with_resource(uri="shared.schema.yaml", resource=resource)


@lru_cache(maxsize=None)
def _validator(name: str) -> jsonschema.Draft202012Validator:
    path = VENDOR / f"apu_{name}.schema.yaml"
    try:
        schema = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise ApuOwnerError(f"unable to load governed APU schema: {name}") from exc
    if not isinstance(schema, dict):
        raise ApuOwnerError(f"governed APU schema must be an object: {name}")
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
        registry=_registry(),
    )


def _validate(name: str, payload: dict[str, Any]) -> None:
    errors = sorted(
        _validator(name).iter_errors(payload),
        key=lambda error: (tuple(str(part) for part in error.absolute_path), error.message),
    )
    if errors:
        rendered = "; ".join(
            f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
            for error in errors
        )
        raise ApuOwnerError(f"{name} violates its governed contract: {rendered}")


@lru_cache(maxsize=1)
def _v02_registry() -> Registry:
    shared = yaml.safe_load(
        (VENDOR / "apu_v02_shared.schema.yaml").read_text(encoding="utf-8")
    )
    resource = Resource.from_contents(shared, default_specification=DRAFT202012)
    return Registry().with_resource(uri="shared.schema.yaml", resource=resource)


@lru_cache(maxsize=None)
def _v02_validator(name: str) -> jsonschema.Draft202012Validator:
    path = VENDOR / f"apu_v02_{name}.schema.yaml"
    try:
        schema = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise ApuOwnerError(f"unable to load governed APU V0.2 schema: {name}") from exc
    if not isinstance(schema, dict):
        raise ApuOwnerError(f"governed APU V0.2 schema must be an object: {name}")
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
        registry=_v02_registry(),
    )


def _validate_v02(name: str, payload: dict[str, Any]) -> None:
    errors = sorted(
        _v02_validator(name).iter_errors(payload),
        key=lambda error: (tuple(str(part) for part in error.absolute_path), error.message),
    )
    if errors:
        rendered = "; ".join(
            f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
            for error in errors
        )
        raise ApuOwnerError(f"V0.2 {name} violates its governed contract: {rendered}")


def ensure_schema(conn: psycopg.Connection) -> None:
    conn.execute(MIGRATION.read_text(encoding="utf-8"))
    conn.commit()


def ensure_v02_schema(conn: psycopg.Connection) -> None:
    conn.execute(MIGRATION.read_text(encoding="utf-8"))
    conn.execute(V02_MIGRATION.read_text(encoding="utf-8"))
    conn.commit()


def _required(value: Any, field: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise ApuOwnerError(f"{field} is required")
    return text


def _digest(value: Any) -> str:
    rendered = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(rendered.encode("utf-8")).hexdigest()


def _project_exists(conn: psycopg.Connection, project_id: str) -> bool:
    with conn.cursor() as cur:
        cur.execute("SELECT 1 FROM agency_projects WHERE project_id = %s", (project_id,))
        return cur.fetchone() is not None


def _normalize_dossier(
    *,
    project_id: str,
    objects: list[dict[str, Any]],
    relations: list[dict[str, Any]],
    review_ref: str,
) -> dict[str, Any]:
    if not isinstance(objects, list) or not objects:
        raise ApuOwnerError("objects must be a non-empty array")
    if not isinstance(relations, list):
        raise ApuOwnerError("relations must be an array")

    normalized_objects: list[dict[str, Any]] = []
    object_ids: set[str] = set()
    for item in objects:
        if not isinstance(item, dict):
            raise ApuOwnerError("every APU object entry must be an object")
        unknown = set(item) - {"stable_object", "object_identity"}
        if unknown:
            raise ApuOwnerError(
                "unsupported APU object entry field(s): " + ", ".join(sorted(unknown))
            )
        stable_object = item.get("stable_object")
        if not isinstance(stable_object, dict):
            raise ApuOwnerError("stable_object must be an object")
        _validate("stable_object", stable_object)
        object_id = _required(stable_object.get("stable_object_id"), "stable_object_id")
        if object_id in object_ids:
            raise ApuOwnerError(f"duplicate stable_object_id: {object_id}")
        object_ids.add(object_id)
        if stable_object.get("scope_type") != "project" or stable_object.get("scope_id") != project_id:
            raise ApuOwnerError(
                f"stable object {object_id} must carry the exact Project scope"
            )

        identity = item.get("object_identity")
        if identity is not None:
            if not isinstance(identity, dict):
                raise ApuOwnerError("object_identity must be an object")
            _validate("object_identity", identity)
            if identity.get("stable_id") != object_id:
                raise ApuOwnerError("object_identity.stable_id must equal stable_object_id")
            if identity.get("object_kind") != stable_object.get("kind"):
                raise ApuOwnerError("object identity kind must equal stable object kind")

        normalized_objects.append(
            {"stable_object": stable_object, "object_identity": identity}
        )

    normalized_relations: list[dict[str, Any]] = []
    relation_ids: set[str] = set()
    for relation in relations:
        if not isinstance(relation, dict):
            raise ApuOwnerError("every APU relation must be an object")
        _validate("object_relation", relation)
        relation_id = _required(relation.get("relation_id"), "relation_id")
        if relation_id in relation_ids:
            raise ApuOwnerError(f"duplicate relation_id: {relation_id}")
        relation_ids.add(relation_id)
        origin = _required(relation.get("from"), "relation.from")
        target = _required(relation.get("to"), "relation.to")
        if origin == target:
            raise ApuOwnerError("APU relation cannot target the same object")
        if origin not in object_ids or target not in object_ids:
            raise ApuOwnerError("APU relation references an object outside the dossier")
        normalized_relations.append(relation)

    normalized_objects.sort(key=lambda item: item["stable_object"]["stable_object_id"])
    normalized_relations.sort(key=lambda item: item["relation_id"])
    return {
        "project_ref": project_id,
        "review_ref": review_ref,
        "objects": normalized_objects,
        "relations": normalized_relations,
    }


def _project_state(
    conn: psycopg.Connection,
    project_id: str,
    *,
    lock: bool = False,
) -> dict[str, Any] | None:
    suffix = " FOR UPDATE" if lock else ""
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT * FROM agency_apu_project_state WHERE project_id = %s" + suffix,
            (project_id,),
        )
        row = cur.fetchone()
    return dict(row) if row is not None else None


def get_apu_object(
    conn: psycopg.Connection,
    *,
    project_id: str,
    object_id: str,
    lock: bool = False,
) -> dict[str, Any]:
    suffix = " FOR UPDATE" if lock else ""
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT * FROM agency_apu_objects WHERE project_id = %s AND object_id = %s" + suffix,
            (project_id, object_id),
        )
        row = cur.fetchone()
    if row is None:
        raise ApuOwnerNotFound(f"unknown APU object in Project {project_id}: {object_id}")
    value = dict(row)
    return {
        "object_id": value["object_id"],
        "project_ref": value["project_id"],
        "object_kind": value.get("object_kind"),
        "proof_status": value.get("proof_status"),
        "stable_object": value.get("stable_object"),
        "object_identity": value.get("object_identity"),
        "canonical_stable_object": value.get("canonical_stable_object"),
        "object_family": value.get("object_family"),
        "revision": value["revision"],
        "retired_at": value.get("retired_at"),
        "retired_by": value.get("retired_by"),
    }


def get_project_anatomy(conn: psycopg.Connection, *, project_id: str) -> dict[str, Any]:
    project_id = _required(project_id, "project_id")
    state = _project_state(conn, project_id)
    if state is None:
        raise ApuOwnerNotFound(f"Project has no executable APU owner state: {project_id}")
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT * FROM agency_apu_objects WHERE project_id = %s AND retired_at IS NULL "
            "ORDER BY object_id",
            (project_id,),
        )
        objects = [dict(row) for row in cur.fetchall()]
        cur.execute(
            "SELECT * FROM agency_apu_object_relations WHERE project_id = %s AND retired_at IS NULL "
            "ORDER BY relation_id",
            (project_id,),
        )
        relations = [dict(row) for row in cur.fetchall()]
    return {
        "project_ref": project_id,
        "model_version": int(state.get("model_version") or 1),
        "model_authority_ref": state.get("model_authority_ref"),
        "owner_revision": state["revision"],
        "objects": [
            {
                "object_id": row["object_id"],
                "object_kind": row.get("object_kind"),
                "proof_status": row.get("proof_status"),
                "stable_object": row.get("stable_object"),
                "object_identity": row.get("object_identity"),
                "canonical_stable_object": row.get("canonical_stable_object"),
                "object_family": row.get("object_family"),
                "revision": row["revision"],
            }
            for row in objects
        ],
        "relations": [
            row["relation_payload"] | {"revision": row["revision"]}
            for row in relations
        ],
        "authority": dict(AUTHORITY),
    }


def list_apu_events(conn: psycopg.Connection, *, project_id: str) -> list[dict[str, Any]]:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT * FROM agency_apu_events WHERE project_id = %s ORDER BY occurred_at, event_id",
            (project_id,),
        )
        rows = cur.fetchall()
    return [dict(row) for row in rows]


def apply_source_match(
    conn: psycopg.Connection,
    *,
    command: dict[str, Any],
    authorization_id: str,
    actor: str,
    idempotency_key: str,
) -> dict[str, Any]:
    """Apply one already-validated bounded legacy source match to a V0.1 owner."""
    if command.get("operation") != "add_match_to_existing_object":
        raise ApuOwnerError("unsupported APU owner application operation")
    project_id = _required(command.get("project_ref"), "command.project_ref")
    object_id = _required(
        command.get("target_stable_object_ref"), "command.target_stable_object_ref"
    )
    candidate_ref = _required(command.get("source_candidate_ref"), "command.source_candidate_ref")
    command_id = _required(command.get("command_id"), "command.command_id")
    command_digest = _required(command.get("payload_digest"), "command.payload_digest")
    authorization_id = _required(authorization_id, "authorization_id")
    actor = _required(actor, "actor")
    key = _required(idempotency_key, "idempotency_key")
    try:
        expected_owner_revision = int(command["expected_owner_revision"])
        expected_object_revision = int(command["expected_object_revision"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ApuOwnerError("command target revisions are required") from exc
    if expected_owner_revision < 1 or expected_object_revision < 1:
        raise ApuOwnerError("command target revisions must be positive")

    match: dict[str, Any] = {
        "source_candidate_id": candidate_ref,
        "status": "candidate",
        "match_evidence": [
            f"execution_result:{command.get('source_execution_result_ref')}",
            f"mapping:{command.get('source_mapping_ref')}",
            f"review:{command.get('source_review_ref')}",
            f"authorization:{authorization_id}",
        ],
    }
    if command.get("source_artifact_ref"):
        match["source_artifact_id"] = command["source_artifact_ref"]
    if command.get("certainty"):
        match["certainty"] = command["certainty"]
    if command.get("match_axis"):
        match["match_axis"] = command["match_axis"]

    event_payload = {
        "command_ref": command_id,
        "command_payload_digest": command_digest,
        "authorization_ref": authorization_id,
        "target_stable_object_ref": object_id,
        "source_candidate_ref": candidate_ref,
        "source_artifact_ref": command.get("source_artifact_ref"),
        "source_execution_result_ref": command.get("source_execution_result_ref"),
        "source_mapping_result_ref": command.get("source_mapping_result_ref"),
        "source_mapping_ref": command.get("source_mapping_ref"),
        "source_review_ref": command.get("source_review_ref"),
        "match_status": "candidate",
        "stable_identity_professionally_validated": False,
        "evidence_admitted": False,
        "work_issue_closed": False,
        "decision_request_resolved": False,
    }
    event_digest = _digest(event_payload)

    with conn.transaction():
        state = _project_state(conn, project_id, lock=True)
        if state is None:
            raise ApuOwnerNotFound(f"Project has no executable APU owner state: {project_id}")
        model_version = int(state.get("model_version") or 1)
        if model_version == 2:
            raise ApuOwnerConflict(
                "legacy add_match_to_existing_object is closed after Project Anatomy V0.2 migration"
            )
        if model_version != 1:
            raise ApuOwnerConflict(
                f"unsupported Project Anatomy model_version: {model_version}"
            )

        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "SELECT * FROM agency_apu_events WHERE idempotency_key = %s",
                (key,),
            )
            replay = cur.fetchone()
            if replay is not None:
                if (
                    replay["event_type"] != "source_match_applied"
                    or replay.get("command_ref") != command_id
                    or replay["payload_digest"] != event_digest
                ):
                    raise ApuOwnerConflict(
                        "APU application idempotency key belongs to another effect"
                    )
                return {
                    "status": "replayed",
                    "event": dict(replay),
                    "object": get_apu_object(
                        conn,
                        project_id=project_id,
                        object_id=object_id,
                    ),
                    "authority": dict(APPLICATION_AUTHORITY),
                }
            cur.execute(
                "SELECT event_id FROM agency_apu_events "
                "WHERE event_type = 'source_match_applied' AND command_ref = %s",
                (command_id,),
            )
            if cur.fetchone() is not None:
                raise ApuOwnerConflict("APU write command was already applied")

        if state["revision"] != expected_owner_revision:
            raise ApuOwnerConflict(
                f"stale APU owner revision: expected {expected_owner_revision}, found {state['revision']}"
            )
        target = get_apu_object(
            conn,
            project_id=project_id,
            object_id=object_id,
            lock=True,
        )
        if target.get("retired_at") is not None:
            raise ApuOwnerConflict("target APU object is retired")
        if target["revision"] != expected_object_revision:
            raise ApuOwnerConflict(
                f"stale APU object revision: expected {expected_object_revision}, found {target['revision']}"
            )

        stable_object = dict(target["stable_object"])
        matches = list(stable_object.get("matches") or [])
        if any(item.get("source_candidate_id") == candidate_ref for item in matches):
            raise ApuOwnerConflict("source candidate is already matched to the target object")
        matches.append(match)
        stable_object["matches"] = matches
        _validate("stable_object", stable_object)
        object_payload = {
            "stable_object": stable_object,
            "object_identity": target.get("object_identity"),
        }
        next_object_revision = target["revision"] + 1
        next_owner_revision = state["revision"] + 1
        conn.execute(
            """
            UPDATE agency_apu_objects
               SET stable_object = %s,
                   payload_digest = %s,
                   revision = %s,
                   updated_at = clock_timestamp()
             WHERE project_id = %s AND object_id = %s AND revision = %s
            """,
            (
                Jsonb(stable_object),
                _digest(object_payload),
                next_object_revision,
                project_id,
                object_id,
                expected_object_revision,
            ),
        )
        conn.execute(
            """
            UPDATE agency_apu_project_state
               SET revision = %s, updated_at = clock_timestamp()
             WHERE project_id = %s AND revision = %s
            """,
            (next_owner_revision, project_id, expected_owner_revision),
        )
        event_id = f"apu-event-{uuid.uuid4().hex}"
        conn.execute(
            """
            INSERT INTO agency_apu_events (
                event_id, project_id, event_type, expected_revision,
                resulting_revision, actor, idempotency_key, payload_digest, payload,
                command_ref, authorization_ref
            ) VALUES (%s, %s, 'source_match_applied', %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                event_id,
                project_id,
                expected_owner_revision,
                next_owner_revision,
                actor,
                key,
                event_digest,
                Jsonb(event_payload),
                command_id,
                authorization_id,
            ),
        )
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "SELECT * FROM agency_apu_events WHERE event_id = %s",
                (event_id,),
            )
            event = dict(cur.fetchone())

    return {
        "status": "applied",
        "event": event,
        "object": get_apu_object(conn, project_id=project_id, object_id=object_id),
        "owner_revision": next_owner_revision,
        "authority": dict(APPLICATION_AUTHORITY),
    }


def store_reviewed_dossier(
    conn: psycopg.Connection,
    *,
    project_id: str,
    objects: list[dict[str, Any]],
    relations: list[dict[str, Any]],
    review_ref: str,
    actor: str,
    idempotency_key: str,
) -> dict[str, Any]:
    """Bootstrap one reviewed V0.1 APU dossier; this is not a runtime create-object API."""
    project_id = _required(project_id, "project_id")
    actor = _required(actor, "actor")
    review_ref = _required(review_ref, "review_ref")
    key = _required(idempotency_key, "idempotency_key")
    dossier = _normalize_dossier(
        project_id=project_id,
        objects=objects,
        relations=relations,
        review_ref=review_ref,
    )
    payload_digest = _digest(dossier)

    with conn.transaction():
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "SELECT project_id, event_type, payload_digest FROM agency_apu_events "
                "WHERE idempotency_key = %s",
                (key,),
            )
            replay = cur.fetchone()
        if replay is not None:
            if (
                replay["project_id"] != project_id
                or replay["event_type"] != "reviewed_dossier_imported"
                or replay["payload_digest"] != payload_digest
            ):
                raise ApuOwnerConflict("APU idempotency key belongs to another effect")
            return get_project_anatomy(conn, project_id=project_id)

        if not _project_exists(conn, project_id):
            raise ApuOwnerNotFound(f"unknown Project: {project_id}")
        if _project_state(conn, project_id) is not None:
            raise ApuOwnerConflict(
                "Project APU owner is already initialized; H1 exposes no create/update command"
            )

        conn.execute(
            "INSERT INTO agency_apu_project_state (project_id, revision, created_by) "
            "VALUES (%s, 1, %s)",
            (project_id, actor),
        )
        for item in dossier["objects"]:
            stable_object = item["stable_object"]
            identity = item.get("object_identity")
            object_id = stable_object["stable_object_id"]
            object_payload = {"stable_object": stable_object, "object_identity": identity}
            conn.execute(
                """
                INSERT INTO agency_apu_objects (
                    object_id, project_id, object_kind, proof_status,
                    stable_object, object_identity, payload_digest, created_by
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    object_id,
                    project_id,
                    stable_object["kind"],
                    stable_object["proof_status"],
                    Jsonb(stable_object),
                    Jsonb(identity) if identity is not None else None,
                    _digest(object_payload),
                    actor,
                ),
            )
        for relation in dossier["relations"]:
            conn.execute(
                """
                INSERT INTO agency_apu_object_relations (
                    relation_id, project_id, relation_type, from_object_id,
                    to_object_id, relation_payload, payload_digest, created_by
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    relation["relation_id"],
                    project_id,
                    relation["type"],
                    relation["from"],
                    relation["to"],
                    Jsonb(relation),
                    _digest(relation),
                    actor,
                ),
            )
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
                        "object_refs": [
                            item["stable_object"]["stable_object_id"]
                            for item in dossier["objects"]
                        ],
                        "relation_refs": [item["relation_id"] for item in dossier["relations"]],
                        "automatic_creation": False,
                        "runtime_write": False,
                    }
                ),
            ),
        )
    return get_project_anatomy(conn, project_id=project_id)


def migrate_project_to_v02(
    conn: psycopg.Connection,
    *,
    project_id: str,
    actor: str,
    idempotency_key: str,
) -> dict[str, Any]:
    from . import apu_v02_support

    return apu_v02_support.migrate_project_to_v02(
        conn,
        project_id=project_id,
        actor=actor,
        idempotency_key=idempotency_key,
    )


def list_v02_owner_migrations(
    conn: psycopg.Connection,
    *,
    project_id: str,
) -> list[dict[str, Any]]:
    from . import apu_v02_support

    return apu_v02_support.list_v02_owner_migrations(conn, project_id=project_id)


def get_project_anatomy_v02(
    conn: psycopg.Connection,
    *,
    project_id: str,
) -> dict[str, Any]:
    from . import apu_v02_support

    return apu_v02_support.get_project_anatomy_v02(conn, project_id=project_id)


def store_reviewed_v02_dossier(
    conn: psycopg.Connection,
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
    from . import apu_v02_support

    return apu_v02_support.store_reviewed_v02_dossier(
        conn,
        project_id=project_id,
        stable_objects=stable_objects,
        source_representations=source_representations,
        attribute_claims=attribute_claims,
        relation_claims=relation_claims,
        review_ref=review_ref,
        actor=actor,
        idempotency_key=idempotency_key,
    )