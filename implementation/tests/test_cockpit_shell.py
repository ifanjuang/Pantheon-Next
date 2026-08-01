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
    # The single cockpit page is Cockpit V3, loaded through its module bootstrap.
    assert 'id="v2-stage"' in response.text
    assert 'src="v3_bootstrap.js"' in response.text

    assert client.get("/cockpit/v3_bootstrap.js").status_code == 200
    assert client.get("/cockpit/v2_bootstrap.js").status_code == 200
    assert client.get("/cockpit/v3_swiper.js").status_code == 200
    assert client.get("/cockpit/v3/collection/collection_controller.js").status_code == 200
    for stylesheet in ("cockpit.css", "cards.css", "families.css", "editors.css"):
        assert client.get(f"/cockpit/styles/{stylesheet}").status_code == 200
    assert client.get("/cockpit/styles/index.css").status_code == 404
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
        )
    )
    editor_health = editor_client.get("/health").json()
    assert editor_health["mode"] == "editor"
    assert editor_health["preview_effect"] == "proposal_only"
    assert editor_health["write_surface"] == "change_candidate_only"
    assert editor_health["signed_knowledge_update_gate"] == "not_configured"


def test_preview_effect_contract_is_proposal_only(monkeypatch) -> None:
    monkeypatch.setattr(effect_preview, "preview_effect", lambda **_: {"effect": "preview"})
    client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            editor_api_key="editor-key",
        )
    )

    response = client.post(
        "/v1/projects/project-a/effects/preview",
        headers={"Authorization": "Bearer editor-key"},
        json={"information": "Préciser le choix de couverture."},
    )
    assert response.status_code == 200
    assert response.json() == {"effect": "preview"}


def test_resource_profile_contract(monkeypatch) -> None:
    monkeypatch.setattr(resource_profiles, "list_resource_profiles", lambda *_: [])
    client = TestClient(create_cockpit_app(connect_fn=_Connection, api_key="read-key"))

    response = client.get(
        "/v1/projects/project-a/resource-profiles",
        headers={"Authorization": "Bearer read-key"},
    )
    assert response.status_code == 200
    assert response.json() == {"resource_profiles": []}


def test_work_issue_read_contract(monkeypatch) -> None:
    monkeypatch.setattr(work_issue_read, "list_work_issues", lambda *_: [])
    client = TestClient(create_cockpit_app(connect_fn=_Connection, api_key="read-key"))

    response = client.get(
        "/v1/projects/project-a/work-issues",
        headers={"Authorization": "Bearer read-key"},
    )
    assert response.status_code == 200
    assert response.json() == {"work_issues": []}
