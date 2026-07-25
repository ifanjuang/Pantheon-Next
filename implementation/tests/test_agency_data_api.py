"""HTTP boundary tests for the PostgreSQL Agency Data surface."""

from __future__ import annotations

from fastapi.testclient import TestClient

from mvp_vertical import agency_data, agency_directory
from mvp_vertical.cockpit_shell import create_cockpit_app


class _Connection:
    def close(self) -> None:
        pass


def test_agency_project_list_accepts_cockpit_but_refuses_hermes_global_read(monkeypatch) -> None:
    observed = []

    def list_projects(_conn, *, query, limit):
        observed.append((query, limit))
        return [{"project_id": "project-lieurey", "code": "LIEUREY", "revision": 4}]

    monkeypatch.setattr(agency_data, "list_projects", list_projects)
    client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            api_key="read-key",
            hermes_api_key="hermes-key",
        )
    )

    cockpit = client.get(
        "/v1/agency/projects",
        params={"q": "lie", "limit": 20},
        headers={"Authorization": "Bearer read-key"},
    )
    assert cockpit.status_code == 200
    assert cockpit.json()["system_of_record"] == "postgres"

    hermes = client.get(
        "/v1/agency/projects",
        headers={"Authorization": "Bearer hermes-key"},
    )
    assert hermes.status_code == 403
    assert "admitted scoped execution envelope" in hermes.json()["detail"]
    assert observed == [("lie", 20)]


def test_agency_directory_routes_are_normalized_and_read_only(monkeypatch) -> None:
    monkeypatch.setattr(
        agency_directory,
        "list_people",
        lambda _conn, *, query, limit: [
            {"person_id": "person-helene", "display_name": "Hélène Leroux", "revision": 2}
        ],
    )
    monkeypatch.setattr(
        agency_directory,
        "list_organizations",
        lambda _conn, *, query, limit: [
            {"organization_id": "org-bet", "name": "BET Exemple", "revision": 3}
        ],
    )
    monkeypatch.setattr(
        agency_directory,
        "list_project_participations",
        lambda _conn, project_id: [
            {
                "participation_id": "part-1",
                "project_id": project_id,
                "role": "BET STRUCTURE",
                "person_name": "Hélène Leroux",
                "organization_name": "BET Exemple",
            }
        ],
    )
    client = TestClient(create_cockpit_app(connect_fn=_Connection, api_key="read-key"))
    headers = {"Authorization": "Bearer read-key"}

    people = client.get("/v1/agency/people", params={"q": "hel", "limit": 25}, headers=headers)
    organizations = client.get("/v1/agency/organizations", headers=headers)
    participations = client.get("/v1/agency/projects/project-lieurey/participations", headers=headers)

    assert people.status_code == 200
    assert people.json()["scope_match"] == "agency_people"
    assert people.json()["people"][0]["person_id"] == "person-helene"
    assert organizations.status_code == 200
    assert organizations.json()["scope_match"] == "agency_organizations"
    assert participations.status_code == 200
    assert participations.json()["participations"][0]["role"] == "BET STRUCTURE"


def test_hermes_direct_project_update_is_refused_before_adapter_execution(monkeypatch) -> None:
    called = False

    def update_project(_conn, **_values):
        nonlocal called
        called = True
        raise AssertionError("Hermes global write must not reach Agency Data adapter")

    monkeypatch.setattr(agency_data, "update_project", update_project)
    client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            editor_api_key="editor-key",
            hermes_api_key="hermes-key",
        )
    )

    response = client.patch(
        "/v1/agency/projects/project-lieurey",
        headers={
            "Authorization": "Bearer hermes-key",
            "X-Pantheon-Actor": "hermes-agency-adapter",
        },
        json={
            "expected_revision": 4,
            "idempotency_key": "idem-hermes-0001",
            "description": "Description de travail enrichie.",
        },
    )
    assert response.status_code == 403
    assert "admitted bounded capability" in response.json()["detail"]
    assert called is False


def test_hermes_consequential_project_update_is_also_refused_at_global_boundary(monkeypatch) -> None:
    called = False

    def update_project(_conn, **_values):
        nonlocal called
        called = True
        raise AssertionError("Hermes global write must not reach Agency Data adapter")

    monkeypatch.setattr(agency_data, "update_project", update_project)
    client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            editor_api_key="editor-key",
            hermes_api_key="hermes-key",
        )
    )
    response = client.patch(
        "/v1/agency/projects/project-lieurey",
        headers={
            "Authorization": "Bearer hermes-key",
            "X-Pantheon-Actor": "hermes-agency-adapter",
        },
        json={
            "expected_revision": 4,
            "idempotency_key": "idem-hermes-phase",
            "phase": "DCE",
        },
    )
    assert response.status_code == 403
    assert called is False


def test_editor_project_create_is_recorded_as_human_actor(monkeypatch) -> None:
    observed = {}

    def create_project(_conn, **values):
        observed.update(values)
        return {"project_id": values["project_id"], "revision": 1, "owner_system": "postgres"}

    monkeypatch.setattr(agency_data, "create_project", create_project)
    client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            editor_api_key="editor-key",
            hermes_api_key="hermes-key",
        )
    )
    response = client.post(
        "/v1/agency/projects",
        headers={
            "Authorization": "Bearer editor-key",
            "X-Pantheon-Actor": "ifan",
        },
        json={
            "project_id": "project-lieurey",
            "code": "LIEUREY",
            "display_name": "Lieurey",
            "idempotency_key": "idem-human-0001",
        },
    )
    assert response.status_code == 201
    assert observed["actor_kind"] == "human"
    assert observed["actor"] == "ifan"


def test_agency_write_requires_actor_and_writer_key() -> None:
    client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            editor_api_key="editor-key",
            hermes_api_key="hermes-key",
        )
    )
    body = {
        "expected_revision": 1,
        "idempotency_key": "idem-missing-actor",
        "description": "Description bornée",
    }
    missing_actor = client.patch(
        "/v1/agency/projects/project-lieurey",
        headers={"Authorization": "Bearer editor-key"},
        json=body,
    )
    assert missing_actor.status_code == 422

    invalid_key = client.patch(
        "/v1/agency/projects/project-lieurey",
        headers={
            "Authorization": "Bearer wrong-key",
            "X-Pantheon-Actor": "human-editor",
        },
        json=body,
    )
    assert invalid_key.status_code == 401


def test_same_editor_and_hermes_key_is_refused_as_ambiguous() -> None:
    client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            editor_api_key="shared-key",
            hermes_api_key="shared-key",
        )
    )
    response = client.patch(
        "/v1/agency/projects/project-lieurey",
        headers={
            "Authorization": "Bearer shared-key",
            "X-Pantheon-Actor": "ambiguous-actor",
        },
        json={
            "expected_revision": 1,
            "idempotency_key": "idem-ambiguous-key",
            "description": "Description bornée",
        },
    )
    assert response.status_code == 503
