"""Emitted payloads conform to the vendored Pantheon-Next contracts.

Pantheon-Next defines the shape; this repository implements it. Until now the
join between the two was a *name*: `sql/013_information_card_projection.sql`
carried the contract's filename and nothing checked that what it produced
matched. Where a payload was checked at all — the Knowledge edit variant — it was
against a hand-copied `required` set with nothing keeping the two equal.

These tests exercise the real projections against the real vendored schemas, and
assert the provenance sidecars still describe the files on disk.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import uuid

import pytest

from mvp_vertical import vendor_contracts

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "mvp_vertical" / "vendor" / "pantheon"

CONTRACTS = (
    "source_intake_admission",
    "information_card_projection",
    "knowledge_edit_variant_candidate",
)


@pytest.mark.parametrize("name", CONTRACTS)
def test_vendored_contract_is_a_valid_schema(name: str) -> None:
    # Loading compiles and checks the schema; an invalid one raises here.
    assert vendor_contracts.problems(name, {}) is not None


@pytest.mark.parametrize("name", CONTRACTS)
def test_vendored_contract_matches_its_recorded_provenance(name: str) -> None:
    source = vendor_contracts.provenance(name)
    digest = sha256((VENDOR / f"{name}.schema.yaml").read_bytes()).hexdigest()

    assert source["source_repository"] == "ifanjuang/Pantheon-Next"
    assert source["source_path"] == f"schemas/{name}.schema.yaml"
    assert len(source["source_commit"]) == 40
    assert source["posture"] == "vendored-reference"
    assert source["authority_transfer"] is False, "vendoring transfers no authority"
    assert digest == source["sha256"], (
        "the vendored file no longer matches its recorded digest; re-vendor "
        "deliberately rather than editing a pinned snapshot in place"
    )


@pytest.mark.parametrize("name", CONTRACTS)
def test_every_vendored_contract_has_a_sidecar(name: str) -> None:
    assert (VENDOR / f"{name}.schema.yaml").is_file()
    assert (VENDOR / f"{name}.source.json").is_file()


def test_vendor_directory_declares_provenance_for_every_schema() -> None:
    """A schema vendored without a sidecar has no recorded origin at all."""
    schemas = {path.name[: -len(".schema.yaml")] for path in VENDOR.glob("*.schema.yaml")}
    sidecars = {path.name[: -len(".source.json")] for path in VENDOR.glob("*.source.json")}
    missing = sorted(schemas - sidecars)
    assert not missing, (
        "vendored schema(s) without a provenance sidecar: " + ", ".join(missing)
    )


def test_a_non_conforming_payload_is_refused() -> None:
    """The validator must bite, not pass everything through."""
    with pytest.raises(vendor_contracts.ContractViolation):
        vendor_contracts.validate("source_intake_admission", {"source_id": "x"})

    with pytest.raises(vendor_contracts.ContractViolation) as excinfo:
        vendor_contracts.validate(
            "information_card_projection", {"information_id": "i", "project_id": "p"}
        )
    assert "does not conform" in str(excinfo.value)


def test_unknown_contract_is_reported_as_unavailable() -> None:
    with pytest.raises(vendor_contracts.ContractUnavailable):
        vendor_contracts.validate("no_such_contract", {})


# ---- the real projections ---------------------------------------------------


@pytest.fixture
def conn():
    from mvp_vertical import agency_data, information_projection, source_intake

    try:
        connection = agency_data.connect()
        relations = connection.execute(
            "SELECT to_regclass('agency_sources'), "
            "to_regclass('agency_information_projection_metadata')"
        ).fetchone()
        connection.rollback()
        if relations[0] is None:
            source_intake.initialize(connection)
        if relations[1] is None:
            information_projection.initialize(connection)
    except Exception as exc:  # pragma: no cover - unit-only environment
        pytest.skip(f"PostgreSQL unreachable: {exc}")

    connection.execute("BEGIN")
    try:
        yield connection
    finally:
        connection.rollback()
        connection.close()


def _id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex}"


def test_source_projection_conforms(conn) -> None:
    from mvp_vertical import source_intake

    record = source_intake.create_source(
        conn,
        source_id=_id("source"),
        source_kind="email",
        origin_system="gmail",
        origin_external_ref=_id("msg"),
        raw_source_ref=f"gmail://{_id('raw')}",
        received_at="2026-08-06T10:00:00+00:00",
        actor="reviewer",
        actor_kind="human",
        idempotency_key=_id("create"),
        declared_project_name="Maison Blanc",
    )
    payload = source_intake.contract_projection(record)

    assert payload["origin"]["system"] == "gmail"
    assert payload["project_ref"] is None
    assert payload["project_link_status"] == "unassigned"
    # The stored row is flat; the contract nests origin. Both stay legible.
    assert "origin_system" not in payload


def test_information_projection_conforms_before_and_after_metadata(conn) -> None:
    from datetime import date

    from mvp_vertical import agency_data, agency_information, information_projection

    project = agency_data.create_project(
        conn,
        project_id=_id("project"),
        code=f"CONF-{uuid.uuid4().hex[:8].upper()}",
        display_name="Projet Conformité",
        actor="reviewer",
        actor_kind="human",
        idempotency_key=_id("project"),
    )
    info = agency_information.create_information(
        conn,
        project_id=project["project_id"],
        title="CCTP couverture",
        category="CCTP",
        source_type="native",
        source_note="Brouillon natif",
        index_label="B",
        information_date=date(2026, 8, 5),
        actor_kind="human",
    )

    # No projection metadata yet. This repository stores revision 0 to mean
    # "absent"; the contract's revision starts at 1 and is optional, so the
    # absence is projected as an omission rather than a non-conforming zero.
    before = information_projection.contract_projection(conn, info["information_id"])
    assert "revision" not in before
    assert before["backing_mode"] == "native"
    assert before["media_types"] == ["text"]

    information_projection.update_projection_metadata(
        conn,
        information_id=info["information_id"],
        source_date=date(2026, 8, 1),
        received_at=None,
        issued_at=None,
        media_types=["pdf"],
        contact_refs=[],
        expected_revision=0,
        actor="reviewer",
        actor_kind="human",
        idempotency_key=_id("metadata"),
    )
    after = information_projection.contract_projection(conn, info["information_id"])
    assert after["revision"] == 1
    assert after["media_types"] == ["pdf"]
    assert after["dates"]["source_date"] == "2026-08-01"
