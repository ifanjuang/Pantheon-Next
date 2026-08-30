"""Temporary #827 diagnostic: observe the full raw retrieval pool before filtering."""

from __future__ import annotations

import copy
import json
import runpy
from pathlib import Path

from mvp_vertical import retrieval_scope, runner
from mvp_vertical.contract import TaskContract


BASELINE = runpy.run_path(
    str(Path(__file__).with_name("test_professional_quote_review_baseline.py"))
)
ORACLE = BASELINE["ORACLE"]
_connect_or_skip = BASELINE["_connect_or_skip"]
_qualification_contract = BASELINE["_qualification_contract"]
_prepare_project_review_scope = BASELINE["_prepare_project_review_scope"]


def _without_source_floor(contract: TaskContract) -> TaskContract:
    raw = copy.deepcopy(contract.raw)
    raw.setdefault("retrieval_boundary", {})["minimum_hits_per_source"] = 0
    return TaskContract(
        raw=raw,
        path=contract.path,
        dossier=contract.dossier,
        sources=contract.sources,
        forbidden=contract.forbidden,
    )


def test_observe_full_quote_review_pool_before_runner_filter() -> None:
    conn = _connect_or_skip()
    contract, project_id = _qualification_contract()
    try:
        principal, requested_documents = _prepare_project_review_scope(
            conn,
            contract,
            project_id,
        )
        diagnostic_contract = _without_source_floor(contract)
        _resolution, hits = retrieval_scope.retrieve_accessible_applicable_hybrid(
            conn,
            principal,
            contract=diagnostic_contract,
            project_id=project_id,
            requested_documents=requested_documents,
            query=ORACLE["review_request"],
            top_k=12,
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
                "runner_useful": runner._is_useful(hit),
            }
            for hit in hits
        ]
        diagnostic = json.dumps(observation, ensure_ascii=False, sort_keys=True)
        print("PROFESSIONAL_QUOTE_REVIEW_FULL_POOL=" + diagnostic)
        # Intentional temporary failure so GitHub Actions retains the exact raw
        # observation even when pytest would otherwise hide stdout for a pass.
        assert False, "PROFESSIONAL_QUOTE_REVIEW_FULL_POOL=" + diagnostic
    finally:
        conn.close()
