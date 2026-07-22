"""Cards-first cockpit static composition boundaries."""

from __future__ import annotations

from fastapi.testclient import TestClient

from mvp_vertical import effect_preview, resource_profiles, work_issue_read
from mvp_vertical.cockpit_shell import create_cockpit_app


class _Connection:
    def close(self) -> None:
        pass


def test_cards_first_cockpit_shell_is_available() -> None:
    client = TestClient(create_cockpit_app(connect_fn=_Connection, api_key="read-key"))

    response = client.get("/cockpit/")
    assert response.status_code == 200
    assert "Pantheon Cockpit" in response.text
    assert "Le cockpit affiche des projections" in response.text
    assert 'data-scene="work"' in response.text
    assert 'src="resources.js"' in response.text
    assert 'src="effects.js"' in response.text
    assert 'src="knowledge_updates.js"' in response.text

    assert client.get("/cockpit/app.js").status_code == 200
    assert client.get("/cockpit/resources.js").status_code == 200
    assert client.get("/cockpit/effects.js").status_code == 200
    assert client.get("/cockpit/knowledge_updates.js").status_code == 200
    assert client.get("/cockpit/styles/index.css").status_code == 200
    assert client.get("/cockpit/styles/resources.css").status_code == 200
    assert client.get("/cockpit/styles/effects.css").status_code == 200
    assert client.get("/cockpit/styles/knowledge_updates.css").status_code == 200
    assert client.get("/editor/").status_code == 200


def test_composed_shell_keeps_existing_api_boundary() -> None:
    client = TestClient(create_cockpit_app(connect_fn=_Connection, api_key="read-key"))

    assert client.get("/health").status_code == 200
    assert client.get("/v1/projects/project-a/documents").status_code == 401
    assert client.get("/v1/projects/project-a/work-issues").status_code == 401
    assert client.get("/v1/projects/project-a/resource-profiles").status_code == 401
    assert client.post(
        "/v1/projects/project-a/effects/preview",
        json={"information": "Préciser le choix de couverture."},
    ).status_code == 401


def test_health_reports_effective_service_posture() -> None:
    read_client = TestClient(
        create_cockpit_app(connect_fn=_Connection, api_key="read-key")
    )
    read_health = read_client.get("/health").json()
    assert read_health["mode"] == "read_only"
    assert read_health["preview_effect"] == "none"
    assert read_health["write_surface"] == "disabled"
    assert read_health["signed_knowledge_update_gate"] == "not_configured"

    editor_client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            editor_api_key="editor-key",
            update_signing_secret="signing-secret",
        )
    )
    editor_health = editor_client.get("/health").json()
    assert editor_health["mode"] == "bounded_read_write"
    assert editor_health["preview_effect"] == "none"
    assert editor_health["write_surface"] == "bounded_document_knowledge_writes"
    assert editor_health["signed_knowledge_update_gate"] == "configured"


def test_schema_initializer_runs_once_at_service_startup() -> None:
    calls: list[str] = []
    app = create_cockpit_app(
        connect_fn=_Connection,
        initialize_fn=lambda: calls.append("initialized"),
        api_key="read-key",
    )

    with TestClient(app) as client:
        assert calls == ["initialized"]
        assert client.get("/health").status_code == 200
        assert client.get("/health").status_code == 200

    assert calls == ["initialized"]


def test_work_issue_route_is_read_only_and_exact_case_scoped(monkeypatch) -> None:
    observed = {}

    def list_projections(_conn, case_ref, *, include_terminal, limit):
        observed.update(
            case_ref=case_ref,
            include_terminal=include_terminal,
            limit=limit,
        )
        return [
            {
                "work_issue": {
                    "issue_id": "issue-1",
                    "case_ref": case_ref,
                    "title": "Review one bounded matter",
                    "status": "review",
                },
                "comments": [],
                "hermes_runs": [],
                "events": [],
                "governance_refs": [],
            }
        ]

    monkeypatch.setattr(work_issue_read, "list_issue_projections", list_projections)
    client = TestClient(create_cockpit_app(connect_fn=_Connection, api_key="read-key"))

    response = client.get(
        "/v1/projects/project-a/work-issues",
        params={"include_terminal": "false", "limit": 25},
        headers={"Authorization": "Bearer read-key"},
    )

    assert response.status_code == 200
    assert response.json()["scope_match"] == "exact_case_ref"
    assert response.json()["work_issues"][0]["work_issue"]["case_ref"] == "project-a"
    assert observed == {
        "case_ref": "project-a",
        "include_terminal": False,
        "limit": 25,
    }


def test_resource_profile_route_is_read_only_and_exact_project_scoped(monkeypatch) -> None:
    observed = {}

    def list_profiles(_conn, parent_project_id):
        observed["parent_project_id"] = parent_project_id
        return {
            "parent_project_id": parent_project_id,
            "scope_match": "exact_parent_project_id",
            "documents": [],
            "knowledge_sites": [
                {
                    "knowledge_id": "knowledge.rules",
                    "sites": [
                        {
                            "url": "https://www.legifrance.gouv.fr/",
                            "host": "www.legifrance.gouv.fr",
                            "site_kind": "legal_reference",
                            "retrieval_profile": {
                                "mode": "address_only",
                                "crawl_status": "not_authorized",
                                "vector_status": "not_indexed",
                                "structure_indexed": False,
                            },
                        }
                    ],
                }
            ],
            "crawl_capability": {
                "status": "documented_not_implemented",
                "default_mode": "address_only",
                "requires_human_scope_approval": True,
            },
        }

    monkeypatch.setattr(resource_profiles, "list_project_resource_profiles", list_profiles)
    client = TestClient(create_cockpit_app(connect_fn=_Connection, api_key="read-key"))
    response = client.get(
        "/v1/projects/project-a/resource-profiles",
        headers={"Authorization": "Bearer read-key"},
    )

    assert response.status_code == 200
    assert response.json()["scope_match"] == "exact_parent_project_id"
    assert response.json()["knowledge_sites"][0]["sites"][0]["retrieval_profile"]["mode"] == "address_only"
    assert observed == {"parent_project_id": "project-a"}


def test_effect_preview_route_is_authenticated_and_proposal_only(monkeypatch) -> None:
    observed = {}

    def preview(_conn, **values):
        observed.update(values)
        return {
            "parent_project_id": values["parent_project_id"],
            "status": "proposal_only",
            "matching_mode": "exact_project_then_deterministic_lexical",
            "information_digest": "sha256:fictional",
            "explicit_object_refs": values["explicit_object_refs"],
            "ambiguous": False,
            "proposals": [
                {
                    "proposal_id": "proposal-1",
                    "effect": "UPDATE",
                    "effect_source": "matched_object_default",
                    "target": {
                        "object_type": "knowledge",
                        "object_id": "knowledge.coverage",
                        "card_id": "card-knowledge.coverage",
                        "title": "Couverture zinc",
                        "current_status": "needs_review",
                    },
                    "candidate_object_type": "knowledge",
                    "score": 0.8,
                    "confidence": "high",
                    "reasons": ["Titre rapproché."],
                    "requires_human_confirmation": True,
                    "apply_route": None,
                }
            ],
            "limits": ["No proposal is persisted."],
        }

    monkeypatch.setattr(effect_preview, "preview_project_effects", preview)
    client = TestClient(create_cockpit_app(connect_fn=_Connection, api_key="read-key"))
    response = client.post(
        "/v1/projects/project-a/effects/preview",
        headers={"Authorization": "Bearer read-key"},
        json={
            "information": "Le client confirme la couverture zinc.",
            "explicit_object_refs": ["knowledge.coverage"],
            "effect_hint": "UPDATE",
            "max_proposals": 3,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "proposal_only"
    assert payload["proposals"][0]["apply_route"] is None
    assert payload["proposals"][0]["requires_human_confirmation"] is True
    assert observed == {
        "parent_project_id": "project-a",
        "information": "Le client confirme la couverture zinc.",
        "explicit_object_refs": ["knowledge.coverage"],
        "effect_hint": "UPDATE",
        "max_proposals": 3,
    }
