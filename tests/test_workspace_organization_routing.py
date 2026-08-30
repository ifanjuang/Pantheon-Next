"""Regression checks for optional workspace organization and owner routing."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OWNER = ROOT / "docs" / "domain-packs" / "architecture" / "DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md"
INSPECTOR = ROOT / "docs" / "architecture" / "WORKSPACE_MANIFEST_INSPECTOR_CANDIDATE.md"
COCKPIT = ROOT / "docs" / "governance" / "PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md"
OBSIDIAN = ROOT / "docs" / "governance" / "OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md"
AUTHORITY = ROOT / "docs" / "governance" / "authority" / "ARCHITECTURE_AUTHORITY_INDEX.md"
REPOSITORY_INSTRUCTIONS = ROOT / "CLAUDE.md"


def test_workspace_organization_profile_remains_optional() -> None:
    owner = OWNER.read_text(encoding="utf-8")

    for invariant in (
        "recommended structure != mandatory structure",
        "folder/path != governed identity",
        "unclassified folder != invalid folder",
        "Hermes classification proposal != filesystem mutation",
        "Cockpit Space != required physical root folder",
    ):
        assert invariant in owner

    assert "Each project uses one shallow phase hierarchy" not in owner
    assert "Another existing organization remains usable" in owner


def test_workspace_changes_route_through_current_owners() -> None:
    instructions = REPOSITORY_INSTRUCTIONS.read_text(encoding="utf-8")

    for owner in (OWNER, INSPECTOR, COCKPIT, OBSIDIAN):
        assert owner.relative_to(ROOT).as_posix() in instructions

    authority = AUTHORITY.read_text(encoding="utf-8")
    assert OWNER.relative_to(ROOT).as_posix() in authority
    assert "optional recommended IFJA organization profile" in authority


def test_manifest_and_cockpit_consumers_preserve_optional_layout() -> None:
    inspector = INSPECTOR.read_text(encoding="utf-8")
    cockpit = COCKPIT.read_text(encoding="utf-8")
    owner_ref = OWNER.relative_to(ROOT).as_posix()

    assert owner_ref in inspector
    assert "another existing organization as usable" in inspector
    assert owner_ref in cockpit
    assert "not required physical root-folder names" in cockpit


def test_obsidian_second_brain_remains_optional_and_subordinate() -> None:
    obsidian = OBSIDIAN.read_text(encoding="utf-8")
    inspector = INSPECTOR.read_text(encoding="utf-8")
    instructions = REPOSITORY_INSTRUCTIONS.read_text(encoding="utf-8")

    for invariant in (
        "Neither is a Pantheon prerequisite, workspace owner, memory authority or manifest authority.",
        "Each layer is independently optional.",
        "second-brain background manifest mutation        = forbidden",
        "refresh admitted technical observation fields   = deterministic manifest engine only",
        "A missing manifest remains neutral",
    ):
        assert invariant in obsidian

    assert "consumers of this posture, not alternative manifest owners" in inspector
    assert "an Obsidian/second-brain skill is not a workspace prerequisite" in instructions


def test_manifest_write_boundary_is_field_owned_and_read_only_first() -> None:
    owner = OWNER.read_text(encoding="utf-8")
    inspector = INSPECTOR.read_text(encoding="utf-8")
    obsidian = OBSIDIAN.read_text(encoding="utf-8")

    for invariant in (
        "The first executable slice derived from this candidate is read-only.",
        "HUMAN-OWNED WORKSPACE METADATA",
        "MANAGED / DETERMINISTIC",
        "expected current manifest digest",
        "workspace discussion remains distinct from exact-revision comments",
    ):
        assert invariant in inspector

    for invariant in (
        "Until that schema and write contract are admitted, the first implementation",
        "change human or governed fields                  = explicit admitted action only",
        "A link from a",
        "manifest to that discussion is navigation metadata only",
    ):
        assert invariant in obsidian

    assert "one shallow optional `Hermes/` working area" in owner
    assert "Neither optional area adds a required" in owner
