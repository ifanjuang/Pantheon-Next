"""Temporary #827 diagnostic: expose the post-#874 baseline and fusion ranking.

This file deliberately reuses the existing professional baseline harness and the
existing project-aware retrieval seam. It fails after capturing observations so
the exact post-#874 result is visible in GitHub Actions. It is diagnostic-only
and must not be merged.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from mvp_vertical import retrieval_scope, runner


BASELINE_PATH = Path(__file__).with_name("test_professional_quote_review_baseline.py")


def _load_baseline_module():
    spec = importlib.util.spec_from_file_location("q827_professional_baseline", BASELINE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _hit_snapshot(hit) -> dict:
    return {
        "source_ref": hit.chunk.source_ref,
        "chunk_no": hit.chunk.chunk_no,
        "distance": hit.chunk.distance,
        "semantic_rank": hit.semantic_rank,
        "lexical_rank": hit.lexical_rank,
        "hybrid_score": hit.hybrid_score,
        "useful": runner._is_useful(hit),
    }


def test_expose_post874_professional_baseline_observation(capsys) -> None:
    baseline = _load_baseline_module()
    baseline.test_current_project_aware_professional_review_baseline_is_observed_not_assumed()
    captured = capsys.readouterr().out
    marker = "PROFESSIONAL_QUOTE_REVIEW_BASELINE="
    observation = next(
        (line for line in captured.splitlines() if line.startswith(marker)),
        None,
    )
    assert observation is not None

    conn = baseline._connect_or_skip()
    contract, project_id = baseline._qualification_contract()
    try:
        principal, requested_documents = baseline._prepare_project_review_scope(
            conn,
            contract,
            project_id,
        )
        _resolution, top4 = retrieval_scope.retrieve_accessible_applicable_hybrid(
            conn,
            principal,
            contract=contract,
            project_id=project_id,
            requested_documents=requested_documents,
            query=baseline.ORACLE["review_request"],
            top_k=4,
            candidate_k=12,
            rrf_k=60,
        )
        _resolution, full_pool = retrieval_scope.retrieve_accessible_applicable_hybrid(
            conn,
            principal,
            contract=contract,
            project_id=project_id,
            requested_documents=requested_documents,
            query=baseline.ORACLE["review_request"],
            top_k=12,
            candidate_k=12,
            rrf_k=60,
        )
    finally:
        conn.close()

    ranking = {
        "top4": [_hit_snapshot(hit) for hit in top4],
        "full_pool": [_hit_snapshot(hit) for hit in full_pool],
    }
    pytest.fail(
        observation
        + "\nPOST874_HYBRID_RANKING="
        + json.dumps(ranking, ensure_ascii=False, sort_keys=True),
        pytrace=False,
    )
