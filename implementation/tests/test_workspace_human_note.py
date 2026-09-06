from __future__ import annotations

import hashlib
import os
from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from mvp_vertical import workspace_human_note
from mvp_vertical.workspace_qualification_api import install_workspace_qualification_routes


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _source(root: Path, name: str = "Plan-RDC-D.pdf") -> Path:
    path = root / name
    path.write_bytes(b"%PDF-1.7\nworkspace-note-test\n")
    return path


def test_human_note_creates_minimal_managed_fragment_and_roundtrips(tmp_path: Path) -> None:
    source = _source(tmp_path)

    initial = workspace_human_note.read_workspace_human_note(
        {"vault": tmp_path}, "vault", source.name
    )
    assert initial["manifest_state"] == "absent"
    assert initial["manifest_digest"] is None
    assert initial["human_note"] == ""
    assert initial["governed_identity"] is False

    saved = workspace_human_note.write_workspace_human_note(
        {"vault": tmp_path},
        "vault",
        source.name,
        human_note="À comparer avec le plan BET avant validation.",
        expected_manifest_digest=None,
    )

    sidecar = tmp_path / "document.yaml"
    raw = sidecar.read_text(encoding="utf-8")
    assert raw.startswith("# >>> Pantheon workspace note\n")
    assert "source_path: Plan-RDC-D.pdf" in raw
    assert "human_note: À comparer avec le plan BET avant validation." in raw
    assert raw.endswith("# <<< Pantheon workspace note\n")
    assert saved["manifest_digest"] == _digest(sidecar)
    assert saved["binding_state"] == "bound"
    assert saved["human_note"] == "À comparer avec le plan BET avant validation."


def test_human_note_preserves_unowned_manifest_bytes_and_comments(tmp_path: Path) -> None:
    source = _source(tmp_path)
    sidecar = tmp_path / "document.yaml"
    original = (
        "display:\n"
        "  full_name: Plan du rez-de-chaussée\n"
        "# commentaire humain à conserver exactement\n"
    )
    sidecar.write_text(original, encoding="utf-8")

    observed = workspace_human_note.read_workspace_human_note(
        {"vault": tmp_path}, "vault", source.name
    )
    saved = workspace_human_note.write_workspace_human_note(
        {"vault": tmp_path},
        "vault",
        source.name,
        human_note="Note locale",
        expected_manifest_digest=observed["manifest_digest"],
    )

    after = sidecar.read_text(encoding="utf-8")
    assert after.startswith(original)
    assert "# commentaire humain à conserver exactement" in after
    assert saved["human_note"] == "Note locale"

    updated = workspace_human_note.write_workspace_human_note(
        {"vault": tmp_path},
        "vault",
        source.name,
        human_note="Note locale corrigée",
        expected_manifest_digest=saved["manifest_digest"],
    )
    final = sidecar.read_text(encoding="utf-8")
    assert final.startswith(original)
    assert final.count("# >>> Pantheon workspace note") == 1
    assert updated["human_note"] == "Note locale corrigée"


def test_human_note_refuses_stale_manifest_digest(tmp_path: Path) -> None:
    source = _source(tmp_path)
    first = workspace_human_note.write_workspace_human_note(
        {"vault": tmp_path},
        "vault",
        source.name,
        human_note="Première note",
        expected_manifest_digest=None,
    )
    sidecar = tmp_path / "document.yaml"
    sidecar.write_text(sidecar.read_text(encoding="utf-8") + "external: edit\n", encoding="utf-8")

    with pytest.raises(workspace_human_note.WorkspaceHumanNoteConflict, match="changed"):
        workspace_human_note.write_workspace_human_note(
            {"vault": tmp_path},
            "vault",
            source.name,
            human_note="Écrasement interdit",
            expected_manifest_digest=first["manifest_digest"],
        )

    assert "external: edit" in sidecar.read_text(encoding="utf-8")


def test_human_note_binding_prevents_another_file_reusing_same_sidecar(tmp_path: Path) -> None:
    first_source = _source(tmp_path, "Plan-A.pdf")
    second_source = _source(tmp_path, "Plan-B.pdf")
    saved = workspace_human_note.write_workspace_human_note(
        {"vault": tmp_path},
        "vault",
        first_source.name,
        human_note="Concerne uniquement le plan A",
        expected_manifest_digest=None,
    )

    observed_second = workspace_human_note.read_workspace_human_note(
        {"vault": tmp_path}, "vault", second_source.name
    )
    assert observed_second["binding_state"] == "mismatch"
    assert observed_second["human_note"] == "Concerne uniquement le plan A"

    with pytest.raises(workspace_human_note.WorkspaceHumanNoteConflict, match="another workspace source"):
        workspace_human_note.write_workspace_human_note(
            {"vault": tmp_path},
            "vault",
            second_source.name,
            human_note="Ne doit pas remplacer la note A",
            expected_manifest_digest=saved["manifest_digest"],
        )


def test_clearing_only_managed_note_removes_empty_sidecar(tmp_path: Path) -> None:
    source = _source(tmp_path)
    saved = workspace_human_note.write_workspace_human_note(
        {"vault": tmp_path},
        "vault",
        source.name,
        human_note="Temporaire",
        expected_manifest_digest=None,
    )
    cleared = workspace_human_note.write_workspace_human_note(
        {"vault": tmp_path},
        "vault",
        source.name,
        human_note="",
        expected_manifest_digest=saved["manifest_digest"],
    )
    assert not (tmp_path / "document.yaml").exists()
    assert cleared["manifest_state"] == "absent"
    assert cleared["human_note"] == ""


def test_human_note_refuses_symlink_sidecar(tmp_path: Path) -> None:
    source = _source(tmp_path)
    outside = tmp_path / "outside.yaml"
    outside.write_text("secret: keep\n", encoding="utf-8")
    os.symlink(outside, tmp_path / "document.yaml")

    with pytest.raises(workspace_human_note.WorkspaceHumanNoteError, match="symlink"):
        workspace_human_note.read_workspace_human_note(
            {"vault": tmp_path}, "vault", source.name
        )
    assert outside.read_text(encoding="utf-8") == "secret: keep\n"


def _note_api(root: Path) -> TestClient:
    app = FastAPI()
    install_workspace_qualification_routes(
        app,
        workspace_roots={"vault": root},
        with_connection=lambda operation: operation(None),
        require_read_key=lambda: None,
        require_editor_key=lambda: None,
        require_human_actor=lambda: "ifan",
    )
    return TestClient(app)


def test_note_api_requires_explicit_write_and_returns_non_authority_boundaries(tmp_path: Path) -> None:
    source = _source(tmp_path)
    client = _note_api(tmp_path)

    read = client.post(
        "/cockpit/workspace-notes/read",
        json={"workspace_ref": "vault", "relative_path": source.name},
    )
    assert read.status_code == 200
    assert read.json()["manifest_digest"] is None

    write = client.post(
        "/cockpit/workspace-notes/write",
        json={
            "workspace_ref": "vault",
            "relative_path": source.name,
            "human_note": "Note humaine",
            "expected_manifest_digest": None,
        },
    )
    assert write.status_code == 200
    payload = write.json()
    assert payload["written_by"] == "ifan"
    assert payload["workspace_write"] is True
    assert payload["automatic_document_admission"] is False
    assert payload["is_evidence"] is False
    assert payload["human_note"] == "Note humaine"
