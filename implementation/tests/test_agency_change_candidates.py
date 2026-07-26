from __future__ import annotations

import uuid

import pytest

from mvp_vertical import agency_change_candidates, agency_data


def _id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex}"


@pytest.fixture
def conn():
    try:
        connection = agency_data.connect()
    except Exception as exc:  # pragma: no cover
        pytest.skip(f"PostgreSQL unreachable: {exc}")
    connection.execute(
        "TRUNCATE agency_change_candidate_events, agency_change_candidates, "
        "agency_project_events, agency_projects RESTART IDENTITY CASCADE"
    )
    connection.commit()
    yield connection
    connection.execute(
        "TRUNCATE agency_change_candidate_events, agency_change_candidates, "
        "agency_project_events, agency_projects RESTART IDENTITY CASCADE"
    )
    connection.commit()
    connection.close()


def _project(conn) -> dict:
    return agency_data.create_project(
        conn,
        project_id=_id("project"),
        code=_id("CAND")[:24],
        display_name="Projet candidate",
        actor="human",
        actor_kind="human",
        idempotency_key=_id("project-create"),
        attributes={"budget": 350000, "plu_zone": "UC0"},
    )


def test_candidate_is_separate_then_human_apply_updates_exact_project_revision(conn) -> None:
    project = _project(conn)
    candidate = agency_change_candidates.create_project_candidate(
        conn,
        project_id=project["project_id"],
        base_revision=project["revision"],
        proposed_attributes={"budget": 375000, "surface_terrain": 950},
        proposer="reviewer",
        proposer_kind="human",
        reason="Mise à jour programme",
        source_refs=["note://programme/2026-07-26"],
        idempotency_key=_id("candidate"),
    )

    assert candidate["status"] == "pending_review"
    assert candidate["entity_type"] == "project"
    assert candidate["base_revision"] == project["revision"]
    assert candidate["changes"] == [
        {"field": "budget", "before": 350000, "proposed": 375000},
        {"field": "surface_terrain", "before": None, "proposed": 950},
    ]

    unchanged = agency_data.get_project(conn, project["project_id"])
    assert unchanged["revision"] == project["revision"]
    assert unchanged["attributes"] == project["attributes"]

    applied = agency_change_candidates.apply_project_candidate(
        conn,
        candidate_id=candidate["candidate_id"],
        actor="human-approver",
        idempotency_key=_id("apply"),
    )
    assert applied["status"] == "applied"
    assert applied["applied_revision"] == project["revision"] + 1

    updated = agency_data.get_project(conn, project["project_id"])
    assert updated["revision"] == project["revision"] + 1
    assert updated["attributes"] == {
        "budget": 375000,
        "plu_zone": "UC0",
        "surface_terrain": 950,
    }


def test_rejected_candidate_never_changes_project(conn) -> None:
    project = _project(conn)
    candidate = agency_change_candidates.create_project_candidate(
        conn,
        project_id=project["project_id"],
        base_revision=project["revision"],
        proposed_attributes={"budget": 400000},
        proposer="reviewer",
        proposer_kind="human",
        idempotency_key=_id("candidate"),
    )
    rejected = agency_change_candidates.reject_project_candidate(
        conn,
        candidate_id=candidate["candidate_id"],
        actor="human-approver",
        reason="Budget non confirmé",
        idempotency_key=_id("reject"),
    )
    assert rejected["status"] == "rejected"
    unchanged = agency_data.get_project(conn, project["project_id"])
    assert unchanged["revision"] == project["revision"]
    assert unchanged["attributes"]["budget"] == 350000


def test_candidate_becomes_stale_when_project_revision_moves(conn) -> None:
    project = _project(conn)
    candidate = agency_change_candidates.create_project_candidate(
        conn,
        project_id=project["project_id"],
        base_revision=project["revision"],
        proposed_attributes={"budget": 400000},
        proposer="reviewer",
        proposer_kind="human",
        idempotency_key=_id("candidate"),
    )

    concurrent = agency_data.update_project(
        conn,
        project_id=project["project_id"],
        changes={"attributes": {"budget": 360000, "plu_zone": "UC0"}},
        actor="other-human",
        actor_kind="human",
        expected_revision=project["revision"],
        idempotency_key=_id("concurrent"),
    )
    assert concurrent["revision"] == project["revision"] + 1

    stale = agency_change_candidates.apply_project_candidate(
        conn,
        candidate_id=candidate["candidate_id"],
        actor="human-approver",
        idempotency_key=_id("apply-stale"),
    )
    assert stale["status"] == "stale"
    current = agency_data.get_project(conn, project["project_id"])
    assert current["revision"] == concurrent["revision"]
    assert current["attributes"]["budget"] == 360000


def test_candidate_event_log_is_append_only(conn) -> None:
    project = _project(conn)
    candidate = agency_change_candidates.create_project_candidate(
        conn,
        project_id=project["project_id"],
        base_revision=project["revision"],
        proposed_attributes={"budget": 365000},
        proposer="reviewer",
        proposer_kind="human",
        idempotency_key=_id("candidate"),
    )
    event_id = conn.execute(
        "SELECT event_id FROM agency_change_candidate_events WHERE candidate_id=%s",
        (candidate["candidate_id"],),
    ).fetchone()[0]
    with pytest.raises(Exception, match="append-only"):
        conn.execute(
            "UPDATE agency_change_candidate_events SET actor='x' WHERE event_id=%s",
            (event_id,),
        )
    conn.rollback()


def test_candidate_api_is_installed_but_does_not_expose_hermes_creation() -> None:
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    api = (root / "mvp_vertical" / "agency_change_candidate_api.py").read_text(encoding="utf-8")
    installer = (root / "mvp_vertical" / "agency_data_api.py").read_text(encoding="utf-8")
    assert '/v1/agency/projects/{project_id}/change-candidates' in api
    assert '/v1/agency/change-candidates/{candidate_id}/apply' in api
    assert '/v1/agency/change-candidates/{candidate_id}/reject' in api
    assert 'proposer_kind="human"' in api
    assert "install_agency_change_candidate_routes" in installer
