"""Acceptance tests for lazy reconstructible Workspace file observation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from fastapi.testclient import TestClient

from mvp_vertical.cockpit_composed import create_composed_cockpit_app


def _forbidden_connection():
    raise AssertionError("workspace file observation must not open a database connection")


def _client(root: Path) -> TestClient:
    return TestClient(
        create_composed_cockpit_app(
            connect_fn=_forbidden_connection,
            initialize_fn=None,
            api_key="read-key",
            workspace_roots={"ifja-projects": root},
        )
    )


def _authorized_get(client: TestClient, path: str):
    return client.get(path, headers={"Authorization": "Bearer read-key"})


def _write_pdf(path: Path, payload: bytes = b"%PDF-1.4\nsynthetic-pdf\n%%EOF\n") -> None:
    path.write_bytes(payload)


def test_workspace_collection_projects_lightweight_pdf_metadata_and_lazy_detail(
    tmp_path: Path,
) -> None:
    plans = tmp_path / "Plans"
    plans.mkdir()
    pdf = plans / "Plan-RDC-D.pdf"
    _write_pdf(pdf)

    client = _client(tmp_path)
    response = _authorized_get(
        client,
        "/cockpit/workspace-collections/ifja-projects?path=Plans",
    )
    assert response.status_code == 200
    items = response.json()["collection"]["items"]
    assert len(items) == 1

    card = items[0]
    assert card["title"] == "Plan-RDC-D.pdf"
    assert card["category"] == "PDF"
    assert card["workspace_entry_kind"] == "file"
    assert card["workspace_file"] == {
        "filename": "Plan-RDC-D.pdf",
        "extension": ".pdf",
        "media_type": "application/pdf",
        "byte_size": pdf.stat().st_size,
        "file_kind": "pdf",
    }
    assert "digest_sha256" not in card["workspace_file"]
    assert card["entry_detail"]["observation"] == "on_read"
    assert card["entry_detail"]["persisted"] is False
    assert card["entry_detail"]["load_action"]["kind"] == "entry_read"

    serialized = json.dumps(response.json(), ensure_ascii=False)
    assert str(tmp_path) not in serialized
    assert "document_id" not in serialized
    assert "hindsight" not in serialized.casefold()


def test_workspace_pdf_detail_observes_digest_timestamp_and_sidecar_without_admission(
    tmp_path: Path,
) -> None:
    plans = tmp_path / "Plans"
    plans.mkdir()
    pdf = plans / "Plan-RDC-D.pdf"
    _write_pdf(pdf)
    # Presence is observed only. The workspace reader must not parse or trust it.
    (plans / "document.yaml").write_text("not: a production schema\n", encoding="utf-8")

    client = _client(tmp_path)
    collection = _authorized_get(
        client,
        "/cockpit/workspace-collections/ifja-projects?path=Plans",
    ).json()
    pdf_card = next(item for item in collection["collection"]["items"] if item["title"] == pdf.name)

    response = _authorized_get(client, pdf_card["entry_detail"]["load_action"]["href"])
    assert response.status_code == 200
    body = response.json()
    card = body["card"]
    observed = card["workspace_file"]

    assert observed["media_type"] == "application/pdf"
    assert observed["byte_size"] == pdf.stat().st_size
    assert observed["digest_sha256"] == hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert observed["filesystem_modified_at"].endswith("+00:00")
    assert card["adjacent_document_sidecar"] == {
        "state": "present",
        "relative_path": "Plans/document.yaml",
        "parsed": False,
        "identity_mapping_resolved": False,
    }
    assert card["qualification"] == {
        "status": "workspace_observation_only",
        "identity_mapping": "not_resolved_by_workspace_projection",
        "automatic_document_admission": False,
    }
    assert card["authority"] == {
        "governed_identity": False,
        "is_evidence": False,
        "is_memory": False,
        "is_persisted": False,
    }
    assert body["card_is_projection"] is True
    assert body["observation_persisted"] is False
    assert body["source_binary_included"] is False
    assert body["content_parsed"] is False
    assert body["hindsight_required"] is False

    serialized = json.dumps(body, ensure_ascii=False)
    for forbidden in (
        "document_family_id",
        "document_version_id",
        "current_for_execution",
        "current_contractual",
        str(tmp_path),
    ):
        assert forbidden not in serialized


def test_workspace_pdf_detail_recomputes_digest_after_file_change(
    tmp_path: Path,
) -> None:
    pdf = tmp_path / "Etude-G2.pdf"
    _write_pdf(pdf, b"%PDF-1.4\nversion-one\n%%EOF\n")
    client = _client(tmp_path)
    detail = "/cockpit/workspace-entries/ifja-projects?path=Etude-G2.pdf"

    first = _authorized_get(client, detail)
    assert first.status_code == 200
    first_digest = first.json()["card"]["workspace_file"]["digest_sha256"]

    _write_pdf(pdf, b"%PDF-1.4\nversion-two-with-change\n%%EOF\n")
    second = _authorized_get(client, detail)
    assert second.status_code == 200
    second_digest = second.json()["card"]["workspace_file"]["digest_sha256"]

    assert first_digest != second_digest
    assert second_digest == hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert second.json()["observation_persisted"] is False


def test_workspace_file_detail_is_bounded_to_visible_regular_files(tmp_path: Path) -> None:
    folder = tmp_path / "Plans"
    folder.mkdir()
    hidden = tmp_path / ".secret.pdf"
    _write_pdf(hidden)
    client = _client(tmp_path)

    traversal = _authorized_get(
        client,
        "/cockpit/workspace-entries/ifja-projects?path=../outside.pdf",
    )
    assert traversal.status_code == 422

    directory = _authorized_get(
        client,
        "/cockpit/workspace-entries/ifja-projects?path=Plans",
    )
    assert directory.status_code == 422

    hidden_response = _authorized_get(
        client,
        "/cockpit/workspace-entries/ifja-projects?path=.secret.pdf",
    )
    assert hidden_response.status_code == 404

    missing = _authorized_get(
        client,
        "/cockpit/workspace-entries/ifja-projects?path=missing.pdf",
    )
    assert missing.status_code == 404
