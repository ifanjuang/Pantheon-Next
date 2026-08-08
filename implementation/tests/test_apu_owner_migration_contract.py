from __future__ import annotations

import json
from pathlib import Path

from mvp_vertical import apu_owner


ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "mvp_vertical" / "vendor" / "pantheon"


def test_h4c_installs_one_owner_migration_without_replacing_h1_identity_table() -> None:
    assert apu_owner.V02_MIGRATION.name == "024_project_anatomy_v02_owner.sql"
    sql = apu_owner.V02_MIGRATION.read_text(encoding="utf-8")
    assert "ALTER TABLE agency_apu_objects" in sql
    assert "CREATE TABLE IF NOT EXISTS agency_apu_source_representations" in sql
    assert "CREATE TABLE IF NOT EXISTS agency_apu_attribute_claims" in sql
    assert "CREATE TABLE IF NOT EXISTS agency_apu_relation_claims" in sql
    assert "CREATE TABLE IF NOT EXISTS agency_apu_v02_owner_migrations" in sql
    assert "DROP TABLE agency_apu_objects" not in sql
    assert "CREATE TABLE agency_apu_objects" not in sql
    assert "owner_revision" in sql
    assert "append-only" in sql.lower()


def test_v02_vendor_contracts_are_pinned_to_merged_pantheon_next_authority() -> None:
    expected = {
        "apu_v02_stable_object.source.json": (
            "schemas/architecture-project-understanding/stable_object.schema.yaml",
            "d2c9ca39b1cc5a2fef813ea5fbf33a39adc71b71",
        ),
        "apu_v02_source_representation.source.json": (
            "schemas/architecture-project-understanding/source_representation.schema.yaml",
            "00bb375f0d849b59a168223f1b08a2c3e363382c",
        ),
        "apu_v02_attribute_claim.source.json": (
            "schemas/architecture-project-understanding/attribute_claim.schema.yaml",
            "427a86653ce80238233434ac536bd408b9885f77",
        ),
        "apu_v02_relation_claim.source.json": (
            "schemas/architecture-project-understanding/relation_claim.schema.yaml",
            "e594d03647dfc09a5a3d372843cf1cff18ece741",
        ),
    }
    for filename, (source_path, blob_sha) in expected.items():
        source = json.loads((VENDOR / filename).read_text(encoding="utf-8"))
        assert source["source_repository"] == "ifanjuang/Pantheon-Next"
        assert source["source_commit"] == "98be3a1dd07be6b6ee2847127d698618f6ff703a"
        assert source["source_path"] == source_path
        assert source["source_blob_sha"] == blob_sha
        assert source["authority_transfer"] is False


def test_v02_projection_does_not_use_legacy_relation_or_inline_match_as_canonical_channel() -> None:
    owner_source = (ROOT / "mvp_vertical" / "apu_owner.py").read_text(encoding="utf-8")
    support_source = (ROOT / "mvp_vertical" / "apu_owner_support.py").read_text(encoding="utf-8")

    assert '"canonicalized_legacy_matches": 0' in support_source
    assert '"canonicalized_legacy_relations": 0' in support_source
    assert '"canonical_emission_allowed_for_legacy": False' in support_source

    assert "get_project_anatomy_v02" in owner_source
    assert "store_reviewed_v02_dossier" in owner_source
    assert "migrate_project_to_v02" in owner_source
    assert (
        "legacy add_match_to_existing_object is closed after Project Anatomy V0.2 migration"
        in owner_source
    )
