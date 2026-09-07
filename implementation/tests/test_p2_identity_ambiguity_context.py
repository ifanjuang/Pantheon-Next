"""P2 repository qualification for determinant stable-object ambiguity.

This proves only the structural half of the behavior: two equally plausible
stable-object identities can be explicitly admitted for the same bounded task
and remain distinct, readable and unresolved. It does not prove that a live
Hermes model will ask the user for clarification; that remains a live cognitive
qualification under #986.
"""

from __future__ import annotations

import uuid

import pytest

from mvp_vertical import (
    agency_data,
    apu_owner,
    hermes_execution,
    hermes_handoff_preview,
    hermes_handoff_store,
    hermes_scoped_context,
    store,
    work_issues,
)
from tools import p2_live_admission_preparer as p2


QUESTION = p2.LIVE_QUESTION


def _id(prefix: str) -> str:
    return f"{prefix}.{uuid.uuid4().hex}"


@pytest.fixture
def conn():
    try:
        connection = store.connect()
    except Exception as exc:  # pragma: no cover - local unit-only environment
        pytest.skip(f"PostgreSQL unreachable: {exc}")
    connection.execute(agency_data.MIGRATION.read_text(encoding="utf-8"))
    connection.execute(apu_owner.MIGRATION.read_text(encoding="utf-8"))
    connection.execute(work_issues.MIGRATION.read_text(encoding="utf-8"))
    connection.execute(hermes_handoff_store.MIGRATION.read_text(encoding="utf-8"))
    for migration in hermes_execution.MIGRATIONS:
        connection.execute(migration.read_text(encoding="utf-8"))
    connection.commit()
    yield connection
    connection.close()


def _admit_and_start(
    conn,
    *,
    project_id: str,
    selected: list[dict[str, str]],
) -> tuple[dict, str, dict]:
    envelope = {
        "root_entity": {
            "entity_id": f"project:{project_id}",
            "entity_type": "project",
        },
        "descendants": [],
        "source_refs": [],
        "explicit_additions": [],
        "explicit_exclusions": [],
        "scope_widened_implicitly": False,
    }
    preview = hermes_handoff_preview.build_preview(
        question=QUESTION,
        card_context_envelope=envelope,
        selected_context=selected,
    )
    handoff = hermes_handoff_store.submit_handoff(
        conn,
        actor="human:p2-ambiguity-test",
        idempotency_key=_id("handoff"),
        question=QUESTION,
        preview=preview,
        card_context_envelope=envelope,
        selected_context=selected,
        include_declared_descendants=False,
    )
    admission = hermes_execution.admit_handoff(
        conn,
        handoff_id=handoff["handoff_id"],
        actor="human:p2-ambiguity-test",
        idempotency_key=_id("admit"),
        ttl_seconds=900,
    )
    run_id = _id("hermes-run")
    hermes_execution.record_external_runtime_start(
        conn,
        admission_id=admission["admission_id"],
        run_id=run_id,
        actor="hermes-runtime",
        expected_issue_version=handoff["work_issue"]["version"],
        idempotency_key=_id("start"),
    )
    return admission, run_id, handoff


def test_determinant_identity_ambiguity_remains_unresolved_before_hermes_reasoning(conn) -> None:
    token = uuid.uuid4().hex
    project = agency_data.create_project(
        conn,
        project_id=f"project.synthetic-p2-ambiguity.{token}",
        code=f"P2C-{token[:10]}".upper(),
        display_name="Qualification synthétique P2 ambiguïté",
        description="Deux cloisons candidates également plausibles pour la même demande.",
        actor="human:p2-ambiguity-test",
        actor_kind="human",
        idempotency_key=f"p2-ambiguity-{token}-project",
    )
    project_id = project["project_id"]
    partition_a = f"apu.synthetic-p2.partition-a.{token}"
    partition_b = f"apu.synthetic-p2.partition-b.{token}"
    representation_id = f"representation.synthetic-p2.ambiguity.{token}"

    apu_owner.store_reviewed_dossier(
        conn,
        project_id=project_id,
        stable_objects=[
            p2._stable(project_id, partition_a, "element", "Cloison P2"),
            p2._stable(project_id, partition_b, "element", "Cloison P2"),
        ],
        source_representations=[p2._representation(project_id, representation_id)],
        attribute_claims=[
            p2._attribute(
                partition_a,
                f"attribute.synthetic-p2.partition-a.{token}",
                representation_id,
                "geometry.thickness",
                120,
                "mm",
            ),
            p2._attribute(
                partition_b,
                f"attribute.synthetic-p2.partition-b.{token}",
                representation_id,
                "geometry.thickness",
                120,
                "mm",
            ),
        ],
        relation_claims=[],
        review_ref=f"fixture:synthetic-p2-ambiguity:{token}",
        actor="system:p2-ambiguity-fixture",
        idempotency_key=f"p2-ambiguity-{token}-apu",
    )

    selected = [
        p2._entity("stable_object", partition_a),
        p2._entity("stable_object", partition_b),
    ]
    admission, run_id, handoff = _admit_and_start(
        conn,
        project_id=project_id,
        selected=selected,
    )

    manifest = hermes_scoped_context.get_context_manifest(
        conn,
        admission_id=admission["admission_id"],
        run_id=run_id,
        actor="hermes-runtime",
    )
    admitted = {(item["entity_type"], item["entity_id"]) for item in manifest["entities"]}
    assert admitted == {
        ("project", f"project:{project_id}"),
        ("stable_object", f"stable_object:{partition_a}"),
        ("stable_object", f"stable_object:{partition_b}"),
    }
    assert manifest["global_search_available"] is False
    assert manifest["global_listing_available"] is False
    assert manifest["source_dereference_available"] is False
    assert manifest["write_effect"] is False
    assert handoff["context_pack"]["scope_widened_implicitly"] is False
    assert handoff["include_declared_descendants"] is False
    assert handoff["question"] == QUESTION

    records = []
    for object_id in (partition_a, partition_b):
        entity = hermes_scoped_context.get_context_entity(
            conn,
            admission_id=admission["admission_id"],
            run_id=run_id,
            entity_type="stable_object",
            entity_id=f"stable_object:{object_id}",
            actor="hermes-runtime",
        )
        record = entity["record"]
        assert record["stable_object"]["nomenclature"]["display_name"] == "Cloison P2"
        assert record["scope"]["relation_traversal_performed"] is False
        assert record["scope"]["neighbour_records_materialized"] is False
        thicknesses = [
            claim["value"]["value"]
            for claim in record["attribute_claims"]
            if claim["attribute_key"] == "geometry.thickness"
        ]
        assert thicknesses == [120]
        records.append(record)

    assert partition_a != partition_b
    assert records[0]["stable_object"] != records[1]["stable_object"]
    assert len(handoff["selected_context"]) == 2
    assert {item["entity_id"] for item in handoff["selected_context"]} == {
        f"stable_object:{partition_a}",
        f"stable_object:{partition_b}",
    }
