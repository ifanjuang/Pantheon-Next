from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


def test_contacts_editor_is_dedicated_and_project_owned() -> None:
    source = (COCKPIT / "contacts_editor.js").read_text(encoding="utf-8")

    assert 'const GROUPS = Object.freeze([' in source
    assert '"Maîtrise d’ouvrage"' in source
    assert '"Bureaux d’études"' in source
    assert '"Entreprises de travaux"' in source
    assert 'expected_revision: state.project.revision' in source
    assert 'contacts,' in source
    assert 'method: "PATCH"' in source
    assert 'project:(.+):contacts' in source
    assert "participation" not in source.lower()


def test_contacts_editor_keeps_optional_connector_provenance_as_data_only() -> None:
    source = (COCKPIT / "contacts_editor.js").read_text(encoding="utf-8")

    assert '"source_ref", "Source / Google Contact"' in source
    assert "googleapis" not in source.lower()
    assert "fetch('https://" not in source.lower()
    assert "browser_sync_execution" not in source


def test_contacts_editor_is_loaded_as_an_independent_module() -> None:
    html = (COCKPIT / "v2.html").read_text(encoding="utf-8")

    assert '<script src="contacts_editor.js" defer></script>' in html
    assert '<link rel="stylesheet" href="styles/contacts_editor.css">' in html
    assert "PantheonContactsEditor" not in (COCKPIT / "v2_app_schema.js").read_text(encoding="utf-8")
    assert "PantheonContactsEditor" not in (COCKPIT / "schema_editor.js").read_text(encoding="utf-8")
