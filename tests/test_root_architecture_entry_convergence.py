from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_root_architecture_entries_match_current_owner_split() -> None:
    claude = _read("CLAUDE.md")
    readme = _read("README.md")
    readme_fr = _read("README.fr.md")

    assert "Hermes Web/dashboard exposes chat, sessions and runtime controls." in claude
    assert "Pantheon Cockpit projects governed Cards, navigation, decisions and status." in claude
    assert "OpenWebUI and Paperless-ngx are refused/retired target integrations" in claude

    assert "Hermes Web/dashboard and compatible clients" in readme
    assert "Pantheon Cockpit" in readme
    assert "OpenWebUI and Paperless-ngx are refused/retired target integrations" in readme

    assert "Hermes Web/dashboard et clients compatibles" in readme_fr
    assert "Pantheon Cockpit" in readme_fr
    assert "OpenWebUI et Paperless-ngx sont des intégrations cibles refusées/retirées" in readme_fr


def test_root_entries_do_not_restore_retired_openwebui_ownership() -> None:
    combined = "\n".join(
        _read(relative) for relative in ("CLAUDE.md", "README.md", "README.fr.md")
    )
    assert "OpenWebUI exposes." not in combined
    assert "OpenWebUI is the cockpit/exposure surface" not in combined
    assert "OpenWebUI owns the cockpit surface" not in combined
    assert "Cockpit / OpenWebUI" not in combined
    assert "OpenWebUI/Paperless/Hermes adapters" not in combined


def test_root_runtime_policy_preserves_non_authority_boundaries() -> None:
    claude = _read("CLAUDE.md")
    assert "client selection does not transfer Pantheon authority" in claude
    assert "projection is not authorization or persistence" in claude
    assert "Repository implementation or client availability does not make them installed, adopted, approved or authorized" in claude
    assert "Historical references remain provenance only" in claude
