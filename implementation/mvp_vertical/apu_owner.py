"""Project-scoped executable owner for reviewed Architecture Project Understanding data.

H1 stores an already reviewed bootstrap dossier and exposes a server-owned read
projection. It does not expose automatic stable-object creation, apply APU write
commands, admit Evidence, canonize claims, resolve Decisions or authorize tasks.
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
VENDOR = Path(__file__).resolve().parent / "vendor" / "pantheon"
AUTHORITY = {
    "is_projection": True,
    "is_evidence": False,
    "is_decision": False,
    "is_memory": False,
    "canonizes_claims": False,
    "authorizes_tasks": False,
    "permits_runtime_writes": False,
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


def ensure_schema(conn: psycopg.Connection) -> None:
    conn.execute(MIGRATION.read_text(encoding="utf-8"))
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


def _project_state(conn: psycopg.Connection, project_id: str) -> dict[str, Any] | None:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM agency_apu_project_state WHERE project_id = %s", (project_id,))
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
        "object_kind": value["object_kind"],
        "proof_status": value["proof_status"],
        "stable_object": value["stable_object"],
        "object_identity": value.get("object_identity"),
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
        "owner_revision": state["revision"],
        "objects": [
            {
                "object_id": row["object_id"],
                "object_kind": row["object_kind"],
                "proof_status": row["proof_status"],
                "stable_object": row["stable_object"],
                "object_identity": row.get("object_identity"),
                "revision": row["revision"],
            }
            for row in objects
        ],
        "relations": [row["relation_payload"] | {"revision": row["revision"]} for row in relations],
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
    """Bootstrap one reviewed APU dossier; this is not a runtime create-object API."""
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
