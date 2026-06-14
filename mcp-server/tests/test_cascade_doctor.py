"""Read-only tests for the cascade-rule doctor check.

The check flags; it never edits, fixes or decides. These tests validate the
declarative rule and the example instance only.
"""

from __future__ import annotations

from pantheon_mcp.doctor import check_cascade_rule, evaluate_impact_review, run_all


def test_example_impact_review_passes() -> None:
    result = check_cascade_rule()
    assert result["ok"], result
    assert result.get("instances_checked", 0) >= 1


def test_critical_must_route_to_arbitration() -> None:
    bad = {
        "impact_review_id": "x",
        "trigger_id": "P-1",
        "trigger_change": "validated",
        "status": "open",
        "impacted": [
            {"target_id": "P-2", "severity": "critical", "impact_status": "supersede", "decision": "pending"}
        ],
    }
    violations = evaluate_impact_review(bad)
    assert any("critical" in v for v in violations), violations


def test_resolved_requires_recorded_decisions() -> None:
    bad = {
        "status": "resolved",
        "impacted": [
            {"target_id": "P-2", "severity": "high", "impact_status": "revalidate", "decision": "pending"}
        ],
    }
    violations = evaluate_impact_review(bad)
    assert any("resolved" in v for v in violations), violations


def test_well_formed_review_has_no_violation() -> None:
    good = {
        "status": "open",
        "impacted": [
            {"target_id": "P-2", "severity": "critical", "impact_status": "critical_arbitration", "decision": "pending"}
        ],
    }
    assert evaluate_impact_review(good) == []


def test_run_all_includes_cascade_rule() -> None:
    result = run_all()
    assert any(c["check"] == "cascade_rule" for c in result["checks"])
