"""FastAPI route installer for native PostgreSQL Agency Data.

The HTTP surface is deliberately narrow: normalized reads plus explicit human
Project create/update commands with actor identity, idempotency and expected
revision. Hermes must use an admitted scoped capability instead of these global
Agency Data routes.
"""

from __future__ import annotations

import hmac
from typing import Callable, Literal

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

from . import agency_data, agency_directory


class ProjectCreateBody(BaseModel):
    project_id: str = Field(min_length=1, max_length=200)
    code: str = Field(min_length=1, max_length=200)
    display_name: str = Field(min_length=1, max_length=300)
    description: str = Field(default="", max_length=10_000)
    status: str | None = Field(default=None, max_length=200)
    phase: str | None = Field(default=None, max_length=200)
    location: str | None = Field(default=None, max_length=500)
    primary_client: str | None = Field(default=None, max_length=500)
    tags: list[str] = Field(default_factory=list, max_length=50)
    idempotency_key: str = Field(min_length=8, max_length=200)


class ProjectUpdateBody(BaseModel):
    expected_revision: int = Field(ge=1)
    idempotency_key: str = Field(min_length=8, max_length=200)
    code: str | None = Field(default=None, min_length=1, max_length=200)
    display_name: str | None = Field(default=None, min_length=1, max_length=300)
    description: str | None = Field(default=None, max_length=10_000)
    status: str | None = Field(default=None, max_length=200)
    phase: str | None = Field(default=None, max_length=200)
    location: str | None = Field(default=None, max_length=500)
    primary_client: str | None = Field(default=None, max_length=500)
    tags: list[str] | None = Field(default=None, max_length=50)


def _bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        return ""
    return authorization.removeprefix("Bearer ").strip()


def install_agency_data_routes(
    app: FastAPI,
    *,
    with_connection: Callable,
    require_read_key: Callable,
    require_writer_kind: Callable,
    require_actor: Callable,
) -> None:
    def agency_operation(operation):
        try:
            return with_connection(operation)
        except (
            agency_data.ProjectNotFound,
            agency_directory.PersonNotFound,
            agency_directory.OrganizationNotFound,
        ) as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except agency_data.GovernanceGateRequired as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        except (agency_data.StaleProjectWrite, agency_data.IdempotencyConflict) as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        except (agency_data.AgencyDataError, agency_directory.AgencyDirectoryError) as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    def require_global_agency_read(
        authorization: str | None = Header(default=None),
    ) -> None:
        supplied = _bearer_token(authorization)
        hermes_key = getattr(app.state, "hermes_api_key", "")
        if hermes_key and hmac.compare_digest(supplied, hermes_key):
            raise HTTPException(
                status_code=403,
                detail=(
                    "Hermes global Agency Data reads are disabled; "
                    "use an admitted scoped execution envelope"
                ),
            )
        require_read_key(authorization)

    def require_human_agency_writer(
        authorization: str | None = Header(default=None),
    ) -> Literal["human"]:
        supplied = _bearer_token(authorization)
        hermes_key = getattr(app.state, "hermes_api_key", "")
        editor_key = getattr(app.state, "editor_api_key", "")
        hermes_match = bool(hermes_key and hmac.compare_digest(supplied, hermes_key))
        editor_match = bool(editor_key and hmac.compare_digest(supplied, editor_key))
        if hermes_match and editor_match:
            raise HTTPException(
                status_code=503,
                detail="editor and Hermes Agency Data keys must be distinct",
            )
        if hermes_match:
            raise HTTPException(
                status_code=403,
                detail=(
                    "Hermes direct Agency Data writes are disabled; "
                    "use an admitted bounded capability"
                ),
            )
        writer_kind = require_writer_kind(authorization)
        if writer_kind != "human":
            raise HTTPException(
                status_code=403,
                detail="global Agency Data writes require a human editor credential",
            )
        return "human"

    @app.get("/v1/agency/projects")
    def list_projects(
        q: str | None = None,
        limit: int = 100,
        _authorized: None = Depends(require_global_agency_read),
    ) -> dict:
        projects = agency_operation(
            lambda conn: agency_data.list_projects(conn, query=q, limit=limit)
        )
        return {
            "system_of_record": "postgres",
            "scope_match": "agency_projects",
            "projects": projects,
        }

    @app.get("/v1/agency/projects/{project_id}")
    def get_project(
        project_id: str,
        _authorized: None = Depends(require_global_agency_read),
    ) -> dict:
        project = agency_operation(lambda conn: agency_data.get_project(conn, project_id))
        return {"system_of_record": "postgres", "project": project}

    @app.get("/v1/agency/projects/{project_id}/participations")
    def get_project_participations(
        project_id: str,
        _authorized: None = Depends(require_global_agency_read),
    ) -> dict:
        participations = agency_operation(
            lambda conn: agency_directory.list_project_participations(conn, project_id)
        )
        return {
            "system_of_record": "postgres",
            "project_id": project_id,
            "participations": participations,
        }

    @app.get("/v1/agency/participations")
    def list_participations(
        q: str | None = None,
        project_id: str | None = None,
        limit: int = 100,
        _authorized: None = Depends(require_global_agency_read),
    ) -> dict:
        participations = agency_operation(
            lambda conn: agency_directory.list_participations(
                conn,
                query=q,
                project_id=project_id,
                limit=limit,
            )
        )
        return {
            "system_of_record": "postgres",
            "scope_match": "agency_project_participations",
            "participations": participations,
        }

    @app.get("/v1/agency/people")
    def list_people(
        q: str | None = None,
        limit: int = 100,
        _authorized: None = Depends(require_global_agency_read),
    ) -> dict:
        people = agency_operation(
            lambda conn: agency_directory.list_people(conn, query=q, limit=limit)
        )
        return {
            "system_of_record": "postgres",
            "scope_match": "agency_people",
            "people": people,
        }

    @app.get("/v1/agency/people/{person_id}")
    def get_person(
        person_id: str,
        _authorized: None = Depends(require_global_agency_read),
    ) -> dict:
        person = agency_operation(lambda conn: agency_directory.get_person(conn, person_id))
        return {"system_of_record": "postgres", "person": person}

    @app.get("/v1/agency/organizations")
    def list_organizations(
        q: str | None = None,
        limit: int = 100,
        _authorized: None = Depends(require_global_agency_read),
    ) -> dict:
        organizations = agency_operation(
            lambda conn: agency_directory.list_organizations(conn, query=q, limit=limit)
        )
        return {
            "system_of_record": "postgres",
            "scope_match": "agency_organizations",
            "organizations": organizations,
        }

    @app.get("/v1/agency/organizations/{organization_id}")
    def get_organization(
        organization_id: str,
        _authorized: None = Depends(require_global_agency_read),
    ) -> dict:
        organization = agency_operation(
            lambda conn: agency_directory.get_organization(conn, organization_id)
        )
        return {"system_of_record": "postgres", "organization": organization}

    @app.post("/v1/agency/projects", status_code=201)
    def create_project(
        body: ProjectCreateBody,
        writer_kind: Literal["human"] = Depends(require_human_agency_writer),
        actor: str = Depends(require_actor),
    ) -> dict:
        values = body.model_dump()
        idempotency_key = values.pop("idempotency_key")
        project = agency_operation(
            lambda conn: agency_data.create_project(
                conn,
                actor=actor,
                actor_kind=writer_kind,
                idempotency_key=idempotency_key,
                **values,
            )
        )
        return {
            "system_of_record": "postgres",
            "effect": "internal_agency_data_write",
            "approval_inferred": False,
            "project": project,
        }

    @app.patch("/v1/agency/projects/{project_id}")
    def update_project(
        project_id: str,
        body: ProjectUpdateBody,
        writer_kind: Literal["human"] = Depends(require_human_agency_writer),
        actor: str = Depends(require_actor),
    ) -> dict:
        supplied = body.model_dump(exclude_unset=True)
        expected_revision = supplied.pop("expected_revision")
        idempotency_key = supplied.pop("idempotency_key")
        project = agency_operation(
            lambda conn: agency_data.update_project(
                conn,
                project_id=project_id,
                changes=supplied,
                actor=actor,
                actor_kind=writer_kind,
                expected_revision=expected_revision,
                idempotency_key=idempotency_key,
            )
        )
        return {
            "system_of_record": "postgres",
            "effect": "internal_agency_data_write",
            "approval_inferred": False,
            "project": project,
        }
