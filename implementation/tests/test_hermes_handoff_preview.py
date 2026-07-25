"""Tests for preview-only Cockpit -> Hermes handoff candidates."""

from __future__ import annotations

from fastapi.testclient import TestClient

from mvp_vertical import card_scope, hermes_handoff_preview
from mvp_vertical.cockpit_shell import create_cockpit_app


class _Connection:
    def close(self) -> None:
        pass


def test_handoff_preview_is_deterministic_read_only_and_not_authorized() -> None:
    request = {
        "question": "Quels points structurels dois-je vérifier ?",
        "card_context_envelope": {
            "root_entity": {"entity_id": "project:lieurey", "entity_type": "project"},
            "descendants": [
                {"entity_id": "document:cctp", "entity_type": "document"},
            ],
            "source_refs": ["source:cctp.pdf", "source:cctp.pdf"],
            "explicit_additions": [],
            "explicit_exclusions": [],
            "scope_widened_implicitly": False,
        },
        "selected_context": [
            {"entity_id": "person:bet", "entity_type": "person"},
        ],
    }
    first = hermes_handoff_preview.build_preview(**request)
    second = hermes_handoff_preview.build_preview(**request)

    assert first == second
    assert first["requested_effect"] == "read_only"
    assert first["execution_authorized"] is False
    assert first["task_contract"]["task_contract_ref"].startswith("task-contract-candidate:")
    assert first["context_pack"]["context_pack_ref"].startswith("context-pack-candidate:")
    assert first["context_pack"]["scope_widened_implicitly"] is False
    assert len(first["context_pack"]["source_refs"]) == 1
    assert first["task_contract"]["forbidden_outputs"] == [
        "external_effect",
        "canonical_effect",
        "memory_promotion",
        "agency_data_mutation",
    ]


def test_handoff_preview_exclusions_win_over_selected_context() -> None:
    preview = hermes_handoff_preview.build_preview(
        question="Résume le dossier",
        card_context_envelope={
            "root_entity": {"entity_id": "project:lieurey", "entity_type": "project"},
            "descendants": [],
            "source_refs": [],
            "explicit_additions": [],
            "explicit_exclusions": [
                {"entity_id": "person:private", "entity_type": "person"},
            ],
        },
        selected_context=[
            {"entity_id": "person:private", "entity_type": "person"},
            {"entity_id": "org:bet", "entity_type": "organization"},
        ],
    )
    included = preview["context_pack"]["included_entities"]
    assert {"entity_id": "person:private", "entity_type": "person"} not in included
    assert {"entity_id": "org:bet", "entity_type": "organization"} in included


def _preview_body() -> dict:
    return {
        "question": "Que faut-il examiner ?",
        "card_context_envelope": {
            "root_entity": {"entity_id": "project:lieurey", "entity_type": "project"},
            "descendants": [],
            "source_refs": [],
            "explicit_additions": [],
            "explicit_exclusions": [],
            "scope_widened_implicitly": False,
        },
        "selected_context": [],
    }


def _patch_scope_validation(monkeypatch) -> None:
    monkeypatch.setattr(
        card_scope,
        "validate_entity_ref",
        lambda _conn, *, entity_ref: {**entity_ref, "source_refs": []},
    )
    monkeypatch.setattr(
        card_scope,
        "resolve_explicit_context",
        lambda _conn, *, entity_refs: {
            "entities": list(entity_refs),
            "source_refs": [
                "source:selected.pdf"
                for item in entity_refs
                if item.get("entity_type") == "document"
            ],
        },
    )


def test_handoff_preview_api_requires_read_key_and_refuses_implicit_scope_widening(monkeypatch) -> None:
    _patch_scope_validation(monkeypatch)
    client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            api_key="read-key",
        )
    )
    body = _preview_body()

    denied = client.post("/v1/cockpit/hermes-handoffs/preview", json=body)
    assert denied.status_code == 401

    accepted = client.post(
        "/v1/cockpit/hermes-handoffs/preview",
        headers={"Authorization": "Bearer read-key"},
        json=body,
    )
    assert accepted.status_code == 200
    assert accepted.json()["execution_authorized"] is False
    assert accepted.json()["scope_resolution"]["requested"] is False

    body["card_context_envelope"]["scope_widened_implicitly"] = True
    widened = client.post(
        "/v1/cockpit/hermes-handoffs/preview",
        headers={"Authorization": "Bearer read-key"},
        json=body,
    )
    assert widened.status_code == 422
    assert "may not widen scope implicitly" in widened.json()["detail"]


def test_handoff_preview_api_rejects_client_supplied_scope_material(monkeypatch) -> None:
    _patch_scope_validation(monkeypatch)
    client = TestClient(create_cockpit_app(connect_fn=_Connection, api_key="read-key"))
    headers = {"Authorization": "Bearer read-key"}

    for field, value in (
        ("descendants", [{"entity_id": "document:forged", "entity_type": "document"}]),
        ("source_refs", ["file:///forged-secret"]),
        ("explicit_additions", [{"entity_id": "person:forged", "entity_type": "person"}]),
    ):
        body = _preview_body()
        body["card_context_envelope"][field] = value
        response = client.post(
            "/v1/cockpit/hermes-handoffs/preview",
            headers=headers,
            json=body,
        )
        assert response.status_code == 422
        assert "server-controlled" in response.json()["detail"]


def test_selected_context_is_server_validated_and_can_add_resolved_sources(monkeypatch) -> None:
    calls = []
    _patch_scope_validation(monkeypatch)

    def resolve_explicit_context(_conn, *, entity_refs):
        calls.append(list(entity_refs))
        return {
            "entities": list(entity_refs),
            "source_refs": ["nas://lieurey/selected.pdf"] if entity_refs else [],
        }

    monkeypatch.setattr(card_scope, "resolve_explicit_context", resolve_explicit_context)
    client = TestClient(create_cockpit_app(connect_fn=_Connection, api_key="read-key"))
    body = _preview_body()
    body["selected_context"] = [
        {"entity_id": "document:selected", "entity_type": "document"}
    ]
    response = client.post(
        "/v1/cockpit/hermes-handoffs/preview",
        headers={"Authorization": "Bearer read-key"},
        json=body,
    )
    assert response.status_code == 200
    payload = response.json()
    assert calls[0] == [{"entity_id": "document:selected", "entity_type": "document"}]
    assert payload["scope_resolution"]["selected_entities_validated"] == 1
    assert payload["context_pack"]["source_refs"] == ["nas://lieurey/selected.pdf"]


def test_declared_descendants_are_added_only_when_explicitly_requested(monkeypatch) -> None:
    calls = []
    _patch_scope_validation(monkeypatch)

    def resolve_declared_descendants(_conn, *, root_entity):
        calls.append(root_entity)
        return {
            "policy": "project_declared_children",
            "root_owner_id": "lieurey",
            "descendants": [
                {"entity_id": "participation:bet", "entity_type": "project_participation"},
                {"entity_id": "document:cctp", "entity_type": "document"},
            ],
            "source_refs": ["source:cctp.pdf"],
            "counts": {"project_participations": 1, "documents": 1},
        }

    monkeypatch.setattr(card_scope, "resolve_declared_descendants", resolve_declared_descendants)
    client = TestClient(create_cockpit_app(connect_fn=_Connection, api_key="read-key"))
    headers = {"Authorization": "Bearer read-key"}

    root_only = client.post(
        "/v1/cockpit/hermes-handoffs/preview",
        headers=headers,
        json=_preview_body(),
    )
    assert root_only.status_code == 200
    assert calls == []
    assert root_only.json()["scope_resolution"]["policy"] == "root_only"
    assert len(root_only.json()["context_pack"]["included_entities"]) == 1

    expanded_body = _preview_body()
    expanded_body["include_declared_descendants"] = True
    expanded = client.post(
        "/v1/cockpit/hermes-handoffs/preview",
        headers=headers,
        json=expanded_body,
    )
    assert expanded.status_code == 200
    assert calls == [{"entity_id": "project:lieurey", "entity_type": "project"}]
    payload = expanded.json()
    assert payload["scope_resolution"]["policy"] == "project_declared_children"
    assert payload["scope_resolution"]["descendants_added"] == 2
    assert payload["scope_resolution"]["source_refs_added"] == 1
    assert len(payload["context_pack"]["included_entities"]) == 3
    assert payload["context_pack"]["source_refs"] == ["source:cctp.pdf"]
