"""Temporary #827 diagnostic: observe raw retrieval before runner usefulness filtering."""

from __future__ import annotations

import json
import runpy
from pathlib import Path

from mvp_vertical import retrieval_scope


BASELINE = runpy.run_path(
    str(Path(__file__).with_name("test_professional_quote_review_baseline.py"))
)
ORACLE = BASELINE["ORACLE"]
_connect_or_skip = BASELINE["_connect_or_skip"]
_qualification_contract = BASELINE["_qualification_contract"]
_prepare_project_review_scope = BASELINE["_prepare_project_review_scope"]


def test_observe_raw_quote_review_hits_before_runner_filter() -> None:
    conn = _connect_or_skip()
    contract, project_id = _qualification_contract()
    try:
        principal, requested_documents = _prepare_project_review_scope(
            conn,
            contract,
            project_id,
        )
        _resolution, hits = retrieval_scope.retrieve_accessible_applicable_hybrid(
            conn,
            principal,
            contract=contract,
            project_id=project_id,
            requested_documents=requested_documents,
            query=ORACLE["review_request"],
            top_k=4,
            candidate_k=12,
            rrf_k=60,
        )
        observation = [
            {
                "source_ref": hit.chunk.source_ref,
                "chunk_no": hit.chunk.chunk_no,
                "distance": hit.chunk.distance,
                "semantic_rank": hit.semantic_rank,
                "lexical_rank": hit.lexical_rank,
                "hybrid_score": hit.hybrid_score,
            }
            for hit in hits
        ]
        print(
            "PROFESSIONAL_QUOTE_REVIEW_RAW_HITS="
            + json.dumps(observation, ensure_ascii=False, sort_keys=True)
        )
        assert hits
    finally:
        conn.close()
