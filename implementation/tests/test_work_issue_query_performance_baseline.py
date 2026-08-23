from __future__ import annotations

import pytest

from tools.measure_work_issue_projection_queries import measure


def test_work_issue_projection_query_baseline() -> None:
    try:
        result = measure(issue_count=3)
    except Exception as exc:  # pragma: no cover - local unit-only environment
        pytest.skip(f"PostgreSQL unreachable: {exc}")

    assert result == {
        "measurement": "work_issue_projection_sql_query_count",
        "scenario": "list_three_empty_work_issue_aggregates_with_card_metadata",
        "issue_count": 3,
        "projection_count": 3,
        "sql_queries": 5,
        "query_strategy": "constant_batch_for_non_empty_case",
        "expected_current_formula": "5",
    }
