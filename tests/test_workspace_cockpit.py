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


def test_workspace_projection_distinguishes_package_health(tmp_path: Path) -> None:
    module = _module()
    coherent = tmp_path / "CCTP"
    coherent.mkdir()
    (coherent / "CCTP.md").write_text("# CCTP\n", encoding="utf-8")
    (coherent / "document.yaml").write_text(
        "display:\n  full_name: Cahier des clauses techniques\n",
        encoding="utf-8",
    )
    (coherent / "assets").mkdir()
    (coherent / "assets" / "coupe.png").write_bytes(b"fixture")

    qualifiable = tmp_path / "Notice"
    qualifiable.mkdir()
    (qualifiable / "Notice.md").write_text("# Notice\n", encoding="utf-8")

    invalid = tmp_path / "DPGF"
    invalid.mkdir()
    (invalid / "DPGF.md").write_text("# DPGF\n", encoding="utf-8")
    (invalid / "document.yaml").write_text("display: [\n", encoding="utf-8")

    result = module.scan_workspaces([("Affaires", tmp_path)], max_depth=2)
    cards = {card["name"]: card for card in result["workspaces"][0]["cards"]}
    assert cards["CCTP"]["status"] == "COHERENT"
    assert cards["CCTP"]["subtitle"] == "Cahier des clauses techniques"
    assert cards["CCTP"]["resources"]["images"] == 1
    assert cards["Notice"]["status"] == "QUALIFIABLE"
    assert cards["DPGF"]["status"] == "INVALID"


def test_package_boundary_does_not_project_assets_as_cards(tmp_path: Path) -> None:
    module = _module()
    package = tmp_path / "Rapport"
    package.mkdir()
    (package / "Rapport.md").write_text("# Rapport\n", encoding="utf-8")
    (package / "assets").mkdir()
    (package / "assets" / "photo.jpg").write_bytes(b"fixture")
    result = module.scan_workspaces([("IFJA", tmp_path)], max_depth=3)
    assert [card["name"] for card in result["workspaces"][0]["cards"]] == ["Rapport"]


def test_declared_representation_cannot_escape_its_package(tmp_path: Path) -> None:
    module = _module()
    outside = tmp_path / "outside.md"
    outside.write_text("# Outside\n", encoding="utf-8")
    package = tmp_path / "Rapport"
    package.mkdir()
    (package / "Rapport.md").write_text("# Rapport\n", encoding="utf-8")
    (package / "document.yaml").write_text(
        "representation:\n  markdown:\n    file: ../outside.md\n",
        encoding="utf-8",
    )

    card = module.inspect_package("IFJA", tmp_path, package)
    assert "La représentation Markdown déclarée est introuvable" in card["warnings"]


def test_check_mode_returns_json_without_database(tmp_path: Path) -> None:
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
    assert payload["totals"]["FREE"] == 1


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
    assert "setfacl" in text
    assert "pgvector" not in text.lower()
    compose = COMPOSE.read_text(encoding="utf-8")
    assert "read_only: true" in compose
    assert compose.count(":ro") == 3
    assert "127.0.0.1" in compose
