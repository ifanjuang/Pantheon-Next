from __future__ import annotations

import json

import pytest

from mvp_vertical.hermes_contradictory_review_runtime import (
    BINDING_ID,
    HermesContradictoryReviewRuntimeError,
    REVIEW_FINDINGS_SCHEMA,
    build_delegate_task,
    compile_delegate_result,
)


CLAIMS = [
    {
        "claim_id": "claim-1",
        "statement": "The candidate is complete.",
        "kind": "fact",
        "source_refs": ["artifact:abc"],
    }
]


def _findings() -> dict:
    return {
        "observations": [
            {
                "observation_id": "obs-1",
                "claim_id": "claim-1",
                "support_status": "partially_supported",
                "severity": "warning",
                "method": "independent bounded review",
                "detail": "One expected section is absent.",
                "artifact_refs": ["artifact:abc"],
                "fresh_observation": True,
            }
        ],
        "analogous_occurrences": [],
        "limits": ["No source beyond the admitted artifact was consulted."],
    }


def test_delegate_contract_uses_one_tasks_item_and_per_task_output_schema() -> None:
    payload = build_delegate_task(
        claims=CLAIMS,
        candidate_id="artifact:abc",
        candidate_digest="sha256:candidate",
        review_context="Check the declared completion claim only.",
    )

    assert set(payload) == {"tasks"}
    assert len(payload["tasks"]) == 1
    task = payload["tasks"][0]
    assert task["output_schema"] == REVIEW_FINDINGS_SCHEMA
    assert "role" not in task
    assert "agent" not in task
    assert "output_schema" not in payload
    context = json.loads(task["context"])
    assert context["claims"] == CLAIMS
    assert "do not repair or mutate" in " ".join(context["constraints"])
    assert "Pantheon Role authority" in task["goal"]


def test_schema_contains_findings_only_not_governed_authority_fields() -> None:
    properties = REVIEW_FINDINGS_SCHEMA["properties"]
    assert set(properties) == {"observations", "analogous_occurrences", "limits"}
    for forbidden in (
        "task_contract_ref",
        "authorized_by",
        "candidate_digest",
        "binding_id",
        "execution_id",
        "is_evidence",
        "is_approval",
    ):
        assert forbidden not in properties


def test_schema_valid_child_result_compiles_through_existing_rite_contract() -> None:
    report = compile_delegate_result(
        delegate_entry={
            "status": "completed",
            "schema_valid": True,
            "summary": json.dumps(_findings()),
        },
        claims=CLAIMS,
        task_contract_ref="task-contract:42",
        trigger_reason="material completion claim",
        proposed_by="ATHENA",
        authorized_by="ZEUS-candidate",
        review_mode="mode_standard",
        candidate_id="artifact:abc",
        candidate_digest="sha256:candidate",
        execution_id="sa-0-abcd1234",
    )

    assert report["status"] == "review_completed_with_reserve"
    assert report["produced_by"]["binding_id"] == BINDING_ID
    assert report["produced_by"]["execution_id"] == "sa-0-abcd1234"
    assert report["authority"] == {
        "is_evidence": False,
        "is_approval": False,
        "is_zeus_closure": False,
        "is_task_authorization": False,
        "requires_zeus_closure": True,
    }
    assert "runtime_binding" not in report


def test_child_cannot_inject_governed_fields_or_bypass_schema_failure() -> None:
    findings = _findings()
    findings["authorized_by"] = "worker-self-approved"
    with pytest.raises(HermesContradictoryReviewRuntimeError, match="unsupported fields"):
        compile_delegate_result(
            delegate_entry={
                "status": "completed",
                "schema_valid": True,
                "summary": json.dumps(findings),
            },
            claims=CLAIMS,
            task_contract_ref="task-contract:42",
            trigger_reason="material completion claim",
            proposed_by="ATHENA",
            authorized_by="ZEUS-candidate",
            review_mode="mode_standard",
            candidate_id="artifact:abc",
            candidate_digest="sha256:candidate",
            execution_id="sa-0-abcd1234",
        )

    with pytest.raises(HermesContradictoryReviewRuntimeError, match="output_schema"):
        compile_delegate_result(
            delegate_entry={
                "status": "completed",
                "schema_valid": False,
                "summary": "{}",
            },
            claims=CLAIMS,
            task_contract_ref="task-contract:42",
            trigger_reason="material completion claim",
            proposed_by="ATHENA",
            authorized_by="ZEUS-candidate",
            review_mode="mode_standard",
            candidate_id="artifact:abc",
            candidate_digest="sha256:candidate",
            execution_id="sa-0-abcd1234",
        )
