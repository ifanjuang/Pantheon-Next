from __future__ import annotations

import uuid

import pytest

from mvp_vertical import agency_claims, agency_data


def _id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex}"


@pytest.fixture
def conn():
    try:
        connection = agency_data.connect()
    except Exception as exc:  # pragma: no cover
        pytest.skip(f"PostgreSQL unreachable: {exc}")
    connection.execute(
        "TRUNCATE agency_project_claims, agency_change_candidate_events, agency_change_candidates, "
        "agency_project_events, agency_projects RESTART IDENTITY CASCADE"
    )
    connection.commit()
    yield connection
    connection.close()


def _project(conn) -> dict:
    return agency_data.create_project(
        conn,
        project_id=_id("project"),
        code=_id("CLAIM")[:24],
        display_name="Projet claims",
        actor="human",
        actor_kind="human",
        idempotency_key=_id("create"),
        attributes={"programme_summary": "Maison individuelle"},
    )


def test_claim_updates_derived_project_projection_without_bumping_project_revision(conn) -> None:
    project = _project(conn)
    first = agency_claims.record_claim(
        conn,
        project_id=project["project_id"],
        claim_type="budget",
        value=350000,
        actor="human:test",
        source_kind="human_assertion",
        status="asserted",
    )

    after_first = agency_data.get_project(conn, project["project_id"])
    assert after_first["revision"] == project["revision"]
    assert after_first["attributes"] == {"programme_summary": "Maison individuelle"}
    assert after_first["claim_values"]["budget"] == 350000
    assert after_first["claim_refs"]["budget"]["claim_id"] == first["claim_id"]
    assert after_first["claim_refs"]["budget"]["status"] == "asserted"

    second = agency_claims.record_claim(
        conn,
        project_id=project["project_id"],
        claim_type="budget",
        value=375000,
        actor="human:test",
        source_kind="information",
        source_ref="information-budget-a01",
        backing_ref={
            "entity_type": "information",
            "entity_id": "information-budget-a01",
            "observed_status": "acted",
        },
        status="source_backed",
        supersedes=first["claim_id"],
    )

    current = agency_data.get_project(conn, project["project_id"])
    assert current["revision"] == project["revision"]
    assert current["claim_values"]["budget"] == 375000
    assert current["claim_refs"]["budget"]["claim_id"] == second["claim_id"]
    assert current["claim_refs"]["budget"]["backing_ref"] == {
        "entity_type": "information",
        "entity_id": "information-budget-a01",
        "observed_status": "acted",
    }
    assert [claim["claim_id"] for claim in agency_claims.list_project_claims(conn, project["project_id"])] == [
        second["claim_id"],
        first["claim_id"],
    ]


def test_scalar_parcel_claims_are_aggregated_into_project_list_projection(conn) -> None:
    project = _project(conn)
    for value in ("AD-85", "AD-86"):
        agency_claims.record_claim(
            conn,
            project_id=project["project_id"],
            claim_type="parcelle",
            value=value,
            actor="human:test",
            source_kind="human_assertion",
            status="asserted",
        )

    current = agency_data.get_project(conn, project["project_id"])
    assert current["claim_values"]["parcelle"] == ["AD-86", "AD-85"]
    assert len(current["claim_refs"]["parcelle"]) == 2


def test_project_claim_rows_are_append_only(conn) -> None:
    project = _project(conn)
    claim = agency_claims.record_claim(
        conn,
        project_id=project["project_id"],
        claim_type="plu_zone",
        value="UDb",
        actor="human:test",
        source_kind="human_assertion",
        status="asserted",
    )

    with pytest.raises(Exception, match="append-only"):
        conn.execute(
            "UPDATE agency_project_claims SET value='\"UC0\"'::jsonb WHERE claim_id=%s",
            (claim["claim_id"],),
        )
    conn.rollback()

    with pytest.raises(Exception, match="append-only"):
        conn.execute("DELETE FROM agency_project_claims WHERE claim_id=%s", (claim["claim_id"],))
    conn.rollback()
