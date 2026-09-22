from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / "implementation" / "workspace_cockpit" / "server.py"
INSTALLER = ROOT / "deployment" / "ubuntu" / "configure-workspace-cockpit-local"
COMPOSE = ROOT / "deployment" / "ubuntu" / "compose.workspace-cockpit-local.yaml"


def _module():
    spec = importlib.util.spec_from_file_location("workspace_cockpit_server", SERVER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _cards(result: dict) -> list[dict]:
    return result["workspaces"][0]["cards"]


def test_complete_source_cartouche_bundle_projects_rich_card(tmp_path: Path) -> None:
    module = _module()
    dce = tmp_path / "DCE"
    dce.mkdir()
    (dce / "CCTP_IND_C.pdf").write_bytes(b"%PDF-fixture")
    (dce / "CCTP_IND_C.md").write_text(
        """---
document_id: doc-cctp-c
source: CCTP_IND_C.pdf
project: LIEUREY
phase: DCE
type: CCTP
index: C
document_date: 2026-09-12
issuer: FRONTSign
tags:
  - structure
  - ossature-bois
---
# CCTP — Lot 03 Ossature bois

## Résumé
CCTP du lot structure pour la consultation DCE.

## Limites / incertitudes
À vérifier avec les plans structure.
""",
        encoding="utf-8",
    )

    result = module.scan_workspaces([("Affaires", tmp_path)], max_depth=2)
    cards = _cards(result)
    document = next(card for card in cards if card["kind"] == "document")
    folder = next(card for card in cards if card["kind"] == "folder")

    assert result["projection"] == "affaires_source_cartouche_v1"
    assert document["status"] == "COMPLETE"
    assert document["document_id"] == "doc-cctp-c"
    assert document["source"] == "CCTP_IND_C.pdf"
    assert document["source_present"] is True
    assert document["cartouche"] == "CCTP_IND_C.md"
    assert document["cartouche_present"] is True
    assert document["title"] == "CCTP — Lot 03 Ossature bois"
    assert document["document_type"] == "CCTP"
    assert document["phase"] == "DCE"
    assert document["index"] == "C"
    assert document["tags"] == ["structure", "ossature-bois"]
    assert "CCTP du lot structure" in document["summary"]
    assert document["hindsight_eligible"] is True
    assert document["warnings"] == []
    assert folder["status"] == "FOLDER"
    assert folder["folder_context_present"] is False
    assert folder["can_generate_folder_context"] is True
    assert result["document_count"] == 1
    assert result["folder_count"] == 1


def test_source_without_cartouche_is_visible_with_generate_affordance(tmp_path: Path) -> None:
    module = _module()
    (tmp_path / "Notice.pdf").write_bytes(b"%PDF-fixture")

    result = module.scan_workspaces([("Affaires", tmp_path)], max_depth=1)
    card = _cards(result)[0]

    assert card["kind"] == "document"
    assert card["name"] == "Notice.pdf"
    assert card["status"] == "CARTOUCHE_MISSING"
    assert card["source_present"] is True
    assert card["cartouche_present"] is False
    assert card["can_generate_cartouche"] is True
    assert card["hindsight_eligible"] is True


def test_cartouche_without_source_is_explicitly_missing(tmp_path: Path) -> None:
    module = _module()
    (tmp_path / "DPGF.md").write_text(
        """---
document_id: doc-dpgf
source: DPGF.xlsx
type: DPGF
---
# DPGF

## Résumé
Décomposition du prix global et forfaitaire.
""",
        encoding="utf-8",
    )

    result = module.scan_workspaces([("Affaires", tmp_path)], max_depth=1)
    card = _cards(result)[0]

    assert card["status"] == "SOURCE_MISSING"
    assert card["source"] == "DPGF.xlsx"
    assert card["source_present"] is False
    assert card["cartouche_present"] is True
    assert card["document_id"] == "doc-dpgf"


def test_folder_context_is_projected_without_creating_identity(tmp_path: Path) -> None:
    module = _module()
    dce = tmp_path / "DCE"
    dce.mkdir()
    (dce / "_folder.md").write_text(
        """---
project: LIEUREY
phase: DCE
tags:
  - consultation
---
# Consultation des entreprises

Pièces utilisées pour la consultation.
""",
        encoding="utf-8",
    )

    result = module.scan_workspaces([("Affaires", tmp_path)], max_depth=2)
    folder = next(card for card in _cards(result) if card["kind"] == "folder")

    assert folder["status"] == "FOLDER"
    assert folder["title"] == "Consultation des entreprises"
    assert folder["project"] == "LIEUREY"
    assert folder["phase"] == "DCE"
    assert folder["tags"] == ["consultation"]
    assert folder["folder_context"] == "_folder.md"
    assert folder["folder_context_present"] is True
    assert folder["can_generate_folder_context"] is False
    assert "document_id" not in folder



def test_folder_without_folder_md_is_explicitly_detected_but_not_invalid(tmp_path: Path) -> None:
    module = _module()
    dossier = tmp_path / "CHANTIER"
    dossier.mkdir()
    (dossier / "Photo.pdf").write_bytes(b"%PDF-fixture")

    result = module.scan_workspaces([("Affaires", tmp_path)], max_depth=2)
    folder = next(card for card in _cards(result) if card["kind"] == "folder")

    assert folder["status"] == "FOLDER"
    assert folder["folder_context"] is None
    assert folder["folder_context_present"] is False
    assert folder["can_generate_folder_context"] is True
    assert folder["warnings"] == []


def test_workspace_index_persists_reconstructible_snapshot_and_detects_changes(tmp_path: Path) -> None:
    module = _module()
    affaires = tmp_path / "affaires"
    state = tmp_path / "state" / "index.sqlite3"
    affaires.mkdir()
    dce = affaires / "DCE"
    dce.mkdir()
    (dce / "CCTP.pdf").write_bytes(b"%PDF-v1")

    index = module.WorkspaceIndex(
        [("Affaires", affaires)],
        2,
        state,
        reconcile_seconds=60,
        debounce_seconds=0.01,
        enable_watcher=False,
    )

    first = index.reconcile("test-initial")
    assert state.is_file()
    first_doc = next(card for card in first["workspaces"][0]["cards"] if card["kind"] == "document")
    first_folder = next(card for card in first["workspaces"][0]["cards"] if card["kind"] == "folder")
    assert first_doc["status"] == "CARTOUCHE_MISSING"
    assert first_folder["folder_context_present"] is False
    assert first["index_state"]["last_reconcile_reason"] == "test-initial"

    (dce / "CCTP.md").write_text(
        """---
document_id: doc-cctp
source: CCTP.pdf
type: CCTP
---
# CCTP
""",
        encoding="utf-8",
    )
    (dce / "_folder.md").write_text("# DCE\n", encoding="utf-8")

    second = index.reconcile("test-change")
    second_doc = next(card for card in second["workspaces"][0]["cards"] if card["kind"] == "document")
    second_folder = next(card for card in second["workspaces"][0]["cards"] if card["kind"] == "folder")
    assert second_doc["status"] == "COMPLETE"
    assert second_doc["document_id"] == "doc-cctp"
    assert second_folder["folder_context_present"] is True
    assert second["index_state"]["last_reconcile_reason"] == "test-change"

    state.unlink()
    rebuilt = index.reconcile("test-rebuild")
    assert state.is_file()
    assert rebuilt["item_count"] == second["item_count"]
    assert rebuilt["index_state"]["last_reconcile_reason"] == "test-rebuild"


def test_workspace_index_dirty_signal_reconciles_without_ui_scan(tmp_path: Path) -> None:
    module = _module()
    affaires = tmp_path / "affaires"
    state = tmp_path / "state" / "index.sqlite3"
    affaires.mkdir()

    index = module.WorkspaceIndex(
        [("Affaires", affaires)],
        2,
        state,
        reconcile_seconds=60,
        debounce_seconds=0.01,
        enable_watcher=False,
    )
    index.start()
    try:
        assert index.snapshot()["item_count"] == 0
        (affaires / "Notice.pdf").write_bytes(b"%PDF")
        index.mark_dirty()

        deadline = module.time.monotonic() + 3
        while module.time.monotonic() < deadline:
            if index.snapshot()["item_count"] == 1:
                break
            module.time.sleep(0.02)

        snapshot = index.snapshot()
        assert snapshot["item_count"] == 1
        assert snapshot["index_state"]["last_reconcile_reason"] == "watch"
        assert snapshot["workspaces"][0]["cards"][0]["status"] == "CARTOUCHE_MISSING"
    finally:
        index.stop()


def test_index_state_must_remain_outside_workspace_root(tmp_path: Path) -> None:
    module = _module()
    root = tmp_path / "AFFAIRES"
    root.mkdir()
    assert module._path_is_within(root / ".state" / "index.sqlite3", root) is True
    assert module._path_is_within(tmp_path / "state" / "index.sqlite3", root) is False



def test_reconcile_move_preserves_cartouche_identity_when_pair_moves_together(tmp_path: Path) -> None:
    module = _module()
    affaires = tmp_path / "AFFAIRES"
    state = tmp_path / "state" / "index.sqlite3"
    source_dir = affaires / "DCE"
    target_dir = affaires / "MARCHE"
    source_dir.mkdir(parents=True)
    target_dir.mkdir()

    (source_dir / "CCTP_IND_C.pdf").write_bytes(b"%PDF")
    (source_dir / "CCTP_IND_C.md").write_text(
        """---
document_id: doc-cctp-c
source: CCTP_IND_C.pdf
---
# CCTP
""",
        encoding="utf-8",
    )

    index = module.WorkspaceIndex(
        [("Affaires", affaires)],
        3,
        state,
        reconcile_seconds=60,
        debounce_seconds=0.01,
        enable_watcher=False,
    )
    before = index.reconcile("before-move")
    before_doc = next(
        card
        for card in before["workspaces"][0]["cards"]
        if card["kind"] == "document" and card["document_id"] == "doc-cctp-c"
    )
    assert before_doc["path"] == "DCE/CCTP_IND_C.pdf"
    assert before_doc["status"] == "COMPLETE"

    (source_dir / "CCTP_IND_C.pdf").rename(target_dir / "CCTP_IND_C.pdf")
    (source_dir / "CCTP_IND_C.md").rename(target_dir / "CCTP_IND_C.md")

    after = index.reconcile("after-move")
    after_doc = next(
        card
        for card in after["workspaces"][0]["cards"]
        if card["kind"] == "document" and card["document_id"] == "doc-cctp-c"
    )
    assert after_doc["path"] == "MARCHE/CCTP_IND_C.pdf"
    assert after_doc["status"] == "COMPLETE"
    assert after_doc["document_id"] == before_doc["document_id"]


def test_linux_inotify_accelerates_change_detection_when_available(tmp_path: Path) -> None:
    module = _module()
    if not module.sys.platform.startswith("linux"):
        return

    root = tmp_path / "AFFAIRES"
    root.mkdir()
    observed = module.threading.Event()
    watcher = module._InotifyWatcher([("Affaires", root)], 2, observed.set)
    assert watcher.start() is True
    try:
        (root / "Notice.pdf").write_bytes(b"%PDF")
        assert observed.wait(2.0) is True
        assert watcher.mode == "inotify"
    finally:
        watcher.stop()


def test_declared_source_cannot_escape_cartouche_directory(tmp_path: Path) -> None:
    module = _module()
    (tmp_path / "outside.pdf").write_bytes(b"%PDF-outside")
    package = tmp_path / "Rapport"
    package.mkdir()
    (package / "Rapport.pdf").write_bytes(b"%PDF-report")
    (package / "Rapport.md").write_text(
        """---
document_id: doc-rapport
source: ../outside.pdf
---
# Rapport
""",
        encoding="utf-8",
    )

    result = module.scan_workspaces([("Affaires", tmp_path)], max_depth=2)
    card = next(card for card in _cards(result) if card["name"] == "Rapport.pdf")

    assert card["status"] == "CHECK"
    assert card["source"] == "Rapport.pdf"
    assert any("même dossier" in warning for warning in card["warnings"])


def test_heavy_sources_stay_visible_and_temp_backups_are_ignored(tmp_path: Path) -> None:
    module = _module()
    (tmp_path / "Maquette.rvt").write_bytes(b"revit")
    (tmp_path / "Maquette.0001.rvt").write_bytes(b"revit-backup")
    (tmp_path / "Perspective.psd").write_bytes(b"photoshop")
    (tmp_path / "~$Notice.docx").write_bytes(b"office-lock")
    (tmp_path / "cache.tmp").write_bytes(b"temp")

    result = module.scan_workspaces([("Affaires", tmp_path)], max_depth=1)
    documents = [card for card in _cards(result) if card["kind"] == "document"]

    assert {card["name"] for card in documents} == {"Maquette.rvt", "Perspective.psd"}
    assert all(card["status"] == "CARTOUCHE_MISSING" for card in documents)
    assert all(card["heavy_binary"] is True for card in documents)
    assert all(card["hindsight_eligible"] is False for card in documents)


def test_malformed_cartouche_is_check_not_source_loss(tmp_path: Path) -> None:
    module = _module()
    (tmp_path / "Notice.pdf").write_bytes(b"%PDF-fixture")
    (tmp_path / "Notice.md").write_text(
        """---
document_id: [
---
# Notice
""",
        encoding="utf-8",
    )

    result = module.scan_workspaces([("Affaires", tmp_path)], max_depth=1)
    card = _cards(result)[0]

    assert card["status"] == "CHECK"
    assert card["source_present"] is True
    assert card["cartouche_present"] is True
    assert any("YAML" in warning for warning in card["warnings"])


def test_check_mode_returns_affaires_projection_without_database(tmp_path: Path) -> None:
    dossier = tmp_path / "Libre"
    dossier.mkdir()
    result = subprocess.run(
        ["python3", str(SERVER), "--root", f"Test={tmp_path}", "--check"],
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["read_only"] is True
    assert payload["projection"] == "affaires_source_cartouche_v1"
    assert payload["totals"]["FOLDER"] == 1
    assert payload["item_count"] == 1


def test_linux_installer_and_browser_assets_are_syntax_valid() -> None:
    subprocess.run(["bash", "-n", str(INSTALLER)], check=True)
    subprocess.run(
        ["node", "--check", str(ROOT / "implementation" / "workspace_cockpit" / "static" / "app.js")],
        check=True,
    )
    text = INSTALLER.read_text(encoding="utf-8")
    assert "127.0.0.1" in text
    assert "NoNewPrivileges=true" in text
    assert "ProtectSystem=strict" in text
    assert "StateDirectory=pantheon-workspace-cockpit" in text
    assert "--state-db /var/lib/pantheon-workspace-cockpit/index.sqlite3" in text
    assert "--reconcile-seconds 60" in text
    assert "setfacl" in text
    assert "pgvector" not in text.lower()
    compose = COMPOSE.read_text(encoding="utf-8")
    # Slice 1 keeps the historical read-only mounts; deployment convergence is #660 Slice 4.
    assert "read_only: true" in compose
    assert compose.count(":ro") == 3
    assert "workspace-cockpit-state:/state" in compose
    assert "WORKSPACE_INDEX_DB: /state/index.sqlite3" in compose
    assert "WORKSPACE_RECONCILE_SECONDS" in compose
    assert "WORKSPACE_WATCH_DEBOUNCE_MS" in compose
    assert "127.0.0.1" in compose
    assert "role-trace:" in compose
    assert "ROLE_TRACE_ATTACH_KEY" in compose
    assert "ROLE_TRACE_READ_KEY" in compose
    assert "HERMES_ROLE_TRACE_API_KEY" in compose

    html = (ROOT / "implementation" / "workspace_cockpit" / "static" / "index.html").read_text(encoding="utf-8")
    javascript = (ROOT / "implementation" / "workspace_cockpit" / "static" / "app.js").read_text(encoding="utf-8")
    graph_css = (ROOT / "implementation" / "workspace_cockpit" / "static" / "role_trace_graph.css").read_text(encoding="utf-8")

    assert "AFFAIRES" in html
    assert "CARTOUCHE_MISSING" in javascript
    assert "SOURCE_MISSING" in javascript
    assert "Générer le cartouche" in javascript
    assert "Action visible, écriture non activée" in javascript
    assert "Cartouche dossier" in javascript
    assert "Sans _folder.md" in javascript
    assert 'href="role_trace_graph.css"' in html
    assert 'id="role-dialogue-events"' in html
    assert 'id="role-view-graph"' in html
    assert 'id="role-graph"' in html
    assert 'id="role-graph-lanes"' in html
    assert "Ordre observable" in html
    assert "/api/role-traces/latest" in javascript
    assert "Last-Event-ID" in javascript
    assert 'roleView.stageEvents.set(event.stage_id, { ...event });' in javascript
    assert 'button.dataset.roleTraceView === roleView.activeView' in javascript
    assert 'parent_stage_id' not in javascript
    assert 'caused_by' not in javascript
    assert '.role-graph-lane' in graph_css
    assert '.role-graph-node[data-projection="derived_transient"]' in graph_css
