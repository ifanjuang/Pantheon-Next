"""OIDC-authenticated, server-scoped human collaboration projection.

The `/me` surface exposes only resources granted to the verified local principal.
It does not replace professional owners and does not make UI visibility an
authorization source.
"""

from __future__ import annotations

from typing import Callable

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

from . import agency_data, human_access, project_document_admission, project_documents


class RevisionAdmissionBody(BaseModel):
    source_id: str = Field(min_length=1, max_length=300)
    source_document_id: str = Field(min_length=1, max_length=300)
    source_version: int = Field(ge=1)
    revision_label: str | None = Field(default=None, max_length=200)
    supersedes_version_id: str | None = Field(default=None, max_length=300)
    idempotency_key: str = Field(min_length=8, max_length=300)


def _bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        return ""
    return authorization.removeprefix("Bearer ").strip()


def install_human_access_routes(
    app: FastAPI,
    *,
    with_connection: Callable,
    oidc_verifier: human_access.TokenVerifier | None = None,
) -> None:
    """Install the first principal-scoped human surface.

    Existing shared API keys remain a compatibility path on their existing
    internal routes. They are not accepted by this OIDC-only surface.
    """
    if oidc_verifier is None:
        try:
            oidc_verifier = human_access.OidcJwtVerifier.from_env_optional()
        except human_access.AccessConfigurationError as exc:
            raise RuntimeError(str(exc)) from exc
    app.state.oidc_human_verifier = oidc_verifier

    def require_principal(
        authorization: str | None = Header(default=None),
    ) -> human_access.PrincipalContext:
        token = _bearer_token(authorization)
        if not token:
            raise HTTPException(status_code=401, detail="OIDC bearer token is required")
        verifier = app.state.oidc_human_verifier
        if verifier is None:
            raise HTTPException(status_code=503, detail="OIDC human access is not configured")
        try:
            claims = verifier.verify(token)
        except human_access.AuthenticationFailed as exc:
            raise HTTPException(status_code=401, detail=str(exc)) from exc
        except human_access.AccessConfigurationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        try:
            return with_connection(
                lambda conn: human_access.resolve_principal_context(conn, claims)
            )
        except human_access.PrincipalNotBound as exc:
            raise HTTPException(status_code=403, detail=str(exc)) from exc
        except human_access.PrincipalDisabled as exc:
            raise HTTPException(status_code=403, detail=str(exc)) from exc
        except human_access.HumanAccessError as exc:
            raise HTTPException(status_code=401, detail=str(exc)) from exc

    def scoped(operation):
        try:
            return with_connection(operation)
        except human_access.AccessDenied as exc:
            raise HTTPException(status_code=403, detail=str(exc)) from exc
        except (
            agency_data.ProjectNotFound,
            project_documents.ProjectDocumentNotFound,
            project_document_admission.SourceNotAdmissible,
        ) as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except (
            project_documents.IdempotencyConflict,
            project_documents.DuplicateCaptureConflict,
            project_documents.SupersessionConflict,
            project_document_admission.SourceAlreadyAdmitted,
            project_document_admission.AdmissionIdempotencyConflict,
        ) as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        except (
            human_access.HumanAccessError,
            project_documents.ProjectDocumentError,
            project_document_admission.ProjectDocumentAdmissionError,
        ) as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.get("/me")
    def me(
        principal: human_access.PrincipalContext = Depends(require_principal),
    ) -> dict:
        return {
            "principal": principal.as_dict(),
            "authority": dict(human_access.AUTHORITY),
        }

    @app.get("/me/projects")
    def my_projects(
        principal: human_access.PrincipalContext = Depends(require_principal),
    ) -> dict:
        projects = scoped(
            lambda conn: human_access.list_accessible_projects(conn, principal.principal_ref)
        )
        return {
            "principal_ref": principal.principal_ref,
            "scope_match": "direct_project_read_grants",
            "projects": projects,
            "authority": dict(human_access.AUTHORITY),
        }

    @app.get("/me/projects/{project_id}")
    def my_project(
        project_id: str,
        principal: human_access.PrincipalContext = Depends(require_principal),
    ) -> dict:
        def operation(conn):
            human_access.require_access(
                conn,
                principal_ref=principal.principal_ref,
                project_id=project_id,
                resource_type="project",
                resource_id=project_id,
                action="project.read",
            )
            return agency_data.get_project(conn, project_id)

        project = scoped(operation)
        return {
            "principal_ref": principal.principal_ref,
            "project": project,
            "authority": dict(human_access.AUTHORITY),
        }

    @app.get("/me/projects/{project_id}/documents")
    def my_project_documents(
        project_id: str,
        principal: human_access.PrincipalContext = Depends(require_principal),
    ) -> dict:
        documents = scoped(
            lambda conn: human_access.list_accessible_documents(
                conn,
                principal_ref=principal.principal_ref,
                project_id=project_id,
            )
        )
        return {
            "principal_ref": principal.principal_ref,
            "project_id": project_id,
            "scope_match": "exact_document_read_grants",
            "documents": documents,
            "authority": dict(human_access.AUTHORITY),
        }

    @app.get("/me/projects/{project_id}/documents/{document_id}")
    def my_project_document(
        project_id: str,
        document_id: str,
        principal: human_access.PrincipalContext = Depends(require_principal),
    ) -> dict:
        def operation(conn):
            human_access.require_access(
                conn,
                principal_ref=principal.principal_ref,
                project_id=project_id,
                resource_type="project",
                resource_id=project_id,
                action="project.read",
            )
            human_access.require_access(
                conn,
                principal_ref=principal.principal_ref,
                project_id=project_id,
                resource_type="project_document",
                resource_id=document_id,
                action="document.read",
            )
            document = project_documents.get_document(conn, document_id)
            if document["parent_project_id"] != project_id:
                raise human_access.AccessDenied("Project Document is outside the requested Project scope")
            revisions = project_documents.list_revisions(conn, document_id)
            return document, revisions

        document, revisions = scoped(operation)
        return {
            "principal_ref": principal.principal_ref,
            "project_id": project_id,
            "document": document,
            "revisions": revisions,
            "authority": dict(human_access.AUTHORITY),
        }

    @app.post("/me/projects/{project_id}/documents/{document_id}/revisions", status_code=201)
    def submit_project_document_revision(
        project_id: str,
        document_id: str,
        body: RevisionAdmissionBody,
        principal: human_access.PrincipalContext = Depends(require_principal),
    ) -> dict:
        def operation(conn):
            # Access checks are reads and therefore start a psycopg transaction.
            # Own the outer transaction here so the nested A2 owner savepoints
            # cannot be rolled back merely because with_connection closes later.
            with conn.transaction():
                human_access.require_access(
                    conn,
                    principal_ref=principal.principal_ref,
                    project_id=project_id,
                    resource_type="project",
                    resource_id=project_id,
                    action="project.read",
                )
                human_access.require_access(
                    conn,
                    principal_ref=principal.principal_ref,
                    project_id=project_id,
                    resource_type="project_document",
                    resource_id=document_id,
                    action="document.read",
                )
                human_access.require_access(
                    conn,
                    principal_ref=principal.principal_ref,
                    project_id=project_id,
                    resource_type="project_document",
                    resource_id=document_id,
                    action="document.revision.submit",
                )
                document = project_documents.get_document(conn, document_id)
                if document["parent_project_id"] != project_id:
                    raise human_access.AccessDenied("Project Document is outside the requested Project scope")
                return project_document_admission.admit_source_as_revision(
                    conn,
                    source_id=body.source_id,
                    document_id=document_id,
                    source_document_id=body.source_document_id,
                    source_version=body.source_version,
                    revision_label=body.revision_label,
                    supersedes_version_id=body.supersedes_version_id,
                    actor=principal.principal_ref,
                    actor_kind="human",
                    idempotency_key=body.idempotency_key,
                )

        result = scoped(operation)
        return {
            "principal_ref": principal.principal_ref,
            "project_id": project_id,
            "effect": "project_document_revision_admission",
            "access_authority": dict(human_access.AUTHORITY),
            "result": result,
        }
