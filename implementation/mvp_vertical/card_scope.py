"""Server-side resolution and validation of Cockpit Card scope.

DOM nesting and browser-supplied references are not security boundaries. The
server verifies stable identities, resolves declared descendants itself and
returns source references only from records it has resolved.
"""

from __future__ import annotations

from typing import Any

import psycopg

from . import agency_data, agency_directory, knowledge, store, work_issue_read, work_issues


class CardScopeError(ValueError):
    pass


_COCKPIT_SPACES = {
    "space:pantheon",
    "space:decisions",
    "space:affaires",
    "space:connaissances",
    "space:outils",
}


def _strip_prefix(value: str, prefix: str) -> str:
    return value[len(prefix):] if value.startswith(prefix) else value


def _root_identity(root_entity: dict[str, Any]) -> tuple[str, str]:
    entity_id = str(root_entity.get("entity_id") or "").strip()
    entity_type = str(root_entity.get("entity_type") or "").strip()
    if not entity_id or not entity_type:
        raise CardScopeError("root entity requires stable entity_id and entity_type")
    return entity_id, entity_type


def _participation_project_id(conn: psycopg.Connection, participation_id: str) -> str:
    row = conn.execute(
        "SELECT project_id FROM agency_project_participations WHERE participation_id = %s",
        (participation_id,),
    ).fetchone()
    if row is None:
        raise CardScopeError(f"unknown Agency ProjectParticipation: {participation_id}")
    return str(row[0])


def validate_entity_ref(
    conn: psycopg.Connection,
    *,
    entity_ref: dict[str, Any],
) -> dict:
    """Verify one client-requested entity against its authoritative store.

    The returned entity identity preserves the client-visible stable identifier,
    but existence and source references are established server-side.
    """
    entity_id, entity_type = _root_identity(entity_ref)
    source_refs: list[str] = []

    try:
        if entity_type == "project":
            agency_data.get_project(conn, _strip_prefix(entity_id, "project:"))
        elif entity_type == "person":
            person_id = _strip_prefix(entity_id, "person:")
            agency_directory.get_person(conn, person_id)
        elif entity_type == "organization":
            organization_id = _strip_prefix(entity_id, "organization:")
            organization_id = _strip_prefix(organization_id, "org:")
            agency_directory.get_organization(conn, organization_id)
        elif entity_type == "project_participation":
            participation_id = _strip_prefix(entity_id, "participation:")
            _participation_project_id(conn, participation_id)
        elif entity_type == "document":
            document_id = _strip_prefix(entity_id, "document:")
            document = store.get_document_card_by_id(conn, document_id)
            if document.get("source_ref"):
                source_refs.append(str(document["source_ref"]))
        elif entity_type == "knowledge":
            knowledge_id = _strip_prefix(entity_id, "knowledge:")
            item = knowledge.get_knowledge_card(conn, knowledge_id)
            source_refs.extend(str(ref) for ref in item.get("source_chunk_refs", []) if ref)
        elif entity_type == "work_issue":
            issue_id = _strip_prefix(entity_id, "work:")
            work_issue_read.get_issue_record(conn, issue_id)
        elif entity_type == "cockpit_space":
            if entity_id not in _COCKPIT_SPACES:
                raise CardScopeError(f"unknown Cockpit space: {entity_id}")
        else:
            raise CardScopeError(f"unsupported Cockpit context entity type: {entity_type}")
    except (
        agency_data.ProjectNotFound,
        agency_directory.PersonNotFound,
        agency_directory.OrganizationNotFound,
        agency_directory.AgencyDirectoryError,
        knowledge.KnowledgeNotFound,
        work_issues.WorkIssueError,
        KeyError,
    ) as exc:
        raise CardScopeError(str(exc)) from exc

    return {
        "entity_id": entity_id,
        "entity_type": entity_type,
        "source_refs": source_refs,
    }


def resolve_explicit_context(
    conn: psycopg.Connection,
    *,
    entity_refs: list[dict[str, Any]],
) -> dict:
    """Validate explicit Context Resolver selections and derive their sources."""
    entities: list[dict[str, str]] = []
    source_refs: list[str] = []
    seen_entities: set[tuple[str, str]] = set()
    seen_sources: set[str] = set()

    for raw in entity_refs:
        validated = validate_entity_ref(conn, entity_ref=raw)
        key = (validated["entity_type"], validated["entity_id"])
        if key not in seen_entities:
            seen_entities.add(key)
            entities.append(
                {
                    "entity_id": validated["entity_id"],
                    "entity_type": validated["entity_type"],
                }
            )
        for source_ref in validated["source_refs"]:
            if source_ref not in seen_sources:
                seen_sources.add(source_ref)
                source_refs.append(source_ref)

    return {"entities": entities, "source_refs": source_refs}


def resolve_declared_descendants(
    conn: psycopg.Connection,
    *,
    root_entity: dict[str, Any],
) -> dict:
    entity_id, entity_type = _root_identity(root_entity)

    if entity_type == "project":
        project_id = _strip_prefix(entity_id, "project:")
        try:
            agency_data.get_project(conn, project_id)
        except agency_data.ProjectNotFound as exc:
            raise CardScopeError(str(exc)) from exc

        participations = agency_directory.list_project_participations(conn, project_id)
        documents = store.list_document_cards(conn, project_id)
        descendants = [
            {
                "entity_id": f"participation:{item['participation_id']}",
                "entity_type": "project_participation",
            }
            for item in participations
        ]
        descendants.extend(
            {
                "entity_id": f"document:{item['document_id']}",
                "entity_type": "document",
            }
            for item in documents
        )
        return {
            "policy": "project_declared_children",
            "root_owner_id": project_id,
            "descendants": descendants,
            "source_refs": [item["source_ref"] for item in documents if item.get("source_ref")],
            "counts": {
                "project_participations": len(participations),
                "documents": len(documents),
            },
        }

    if entity_type == "document":
        document_id = _strip_prefix(entity_id, "document:")
        try:
            document = store.get_document_card_by_id(conn, document_id)
        except KeyError as exc:
            raise CardScopeError(str(exc)) from exc
        return {
            "policy": "document_source_only",
            "root_owner_id": document_id,
            "descendants": [],
            "source_refs": [document["source_ref"]] if document.get("source_ref") else [],
            "counts": {"documents": 1},
        }

    validate_entity_ref(conn, entity_ref=root_entity)
    return {
        "policy": "root_only",
        "root_owner_id": entity_id,
        "descendants": [],
        "source_refs": [],
        "counts": {},
    }


def resolve_case_ref(
    conn: psycopg.Connection,
    *,
    root_entity: dict[str, Any],
) -> str:
    """Resolve the owning project/case before an internal Work Issue is created."""
    entity_id, entity_type = _root_identity(root_entity)

    if entity_type == "project":
        project_id = _strip_prefix(entity_id, "project:")
        try:
            agency_data.get_project(conn, project_id)
        except agency_data.ProjectNotFound as exc:
            raise CardScopeError(str(exc)) from exc
        return project_id

    if entity_type == "document":
        document_id = _strip_prefix(entity_id, "document:")
        try:
            return str(store.get_document_card_by_id(conn, document_id)["parent_project_id"])
        except KeyError as exc:
            raise CardScopeError(str(exc)) from exc

    if entity_type == "knowledge":
        knowledge_id = _strip_prefix(entity_id, "knowledge:")
        try:
            return str(knowledge.get_knowledge_card(conn, knowledge_id)["parent_project_id"])
        except knowledge.KnowledgeNotFound as exc:
            raise CardScopeError(str(exc)) from exc

    if entity_type == "work_issue":
        issue_id = _strip_prefix(entity_id, "work:")
        try:
            return str(work_issue_read.get_issue_record(conn, issue_id)["case_ref"])
        except work_issues.WorkIssueError as exc:
            raise CardScopeError(str(exc)) from exc

    if entity_type == "project_participation":
        participation_id = _strip_prefix(entity_id, "participation:")
        return _participation_project_id(conn, participation_id)

    raise CardScopeError(
        f"Hermes handoff submission requires a project-scoped root; unsupported root type: {entity_type}"
    )
