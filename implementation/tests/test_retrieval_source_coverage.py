"""Opt-in comparative source coverage stays inside the existing retrieval owner."""

from __future__ import annotations

from pathlib import Path

import pytest

from mvp_vertical import human_access, retrieval, retrieval_scope
from mvp_vertical.contract import TaskContract
from mvp_vertical.retrieval import HybridRetrievedChunk
from mvp_vertical.store import RetrievedChunk


def _chunk(source_ref: str, digest: str, number: int) -> RetrievedChunk:
    return RetrievedChunk(
        source_ref=source_ref,
        source_digest=digest,
        chunk_no=number,
        body=f"candidate {source_ref} {number}",
        distance=0.1,
    )


def _hit(source_ref: str, digest: str, number: int, score: float) -> HybridRetrievedChunk:
    return HybridRetrievedChunk(
        chunk=_chunk(source_ref, digest, number),
        hybrid_score=score,
        semantic_rank=number + 1,
        lexical_rank=None,
    )


def _contract(*, minimum_hits_per_source: object = 0) -> TaskContract:
    raw = {
        "object_id": "task-source-coverage",
        "contract_id": "task-source-coverage",
        "scope": {
            "parent_project_id": "project-a",
            "declared_sources": [
                "sources/a.md",
                "sources/b.md",
                "sources/c.md",
            ],
        },
    }
    if minimum_hits_per_source is not None:
        raw["retrieval_boundary"] = {
            "minimum_hits_per_source": minimum_hits_per_source,
        }
    return TaskContract(
        raw=raw,
        path=Path("task.yaml"),
        dossier="dossier-a",
        sources=("sources/a.md", "sources/b.md", "sources/c.md"),
        forbidden=(),
    )


def _principal() -> human_access.PrincipalContext:
    return human_access.PrincipalContext(
        principal_ref="human:test",
        issuer="test",
        subject="subject",
    )


def test_source_floor_is_opt_in_and_default_keeps_global_top_k() -> None:
    hits = [
        _hit("sources/a.md", "a", 0, 1.0),
        _hit("sources/a.md", "a", 1, 0.9),
        _hit("sources/a.md", "a", 2, 0.8),
        _hit("sources/b.md", "b", 0, 0.7),
        _hit("sources/c.md", "c", 0, 0.6),
    ]
    sources = (("sources/a.md", "a"), ("sources/b.md", "b"), ("sources/c.md", "c"))

    selected = retrieval.select_minimum_source_hits(
        hits,
        sources=sources,
        top_k=4,
        minimum_hits_per_source=0,
    )

    assert selected == hits[:4]
    assert {hit.chunk.source_ref for hit in selected} == {"sources/a.md", "sources/b.md"}


def test_source_floor_represents_each_available_exact_source_without_rewriting_rrf_order() -> None:
    hits = [
        _hit("sources/a.md", "a", 0, 1.0),
        _hit("sources/a.md", "a", 1, 0.9),
        _hit("sources/a.md", "a", 2, 0.8),
        _hit("sources/b.md", "b", 0, 0.7),
        _hit("sources/c.md", "c", 0, 0.6),
    ]
    sources = (("sources/a.md", "a"), ("sources/b.md", "b"), ("sources/c.md", "c"))

    selected = retrieval.select_minimum_source_hits(
        hits,
        sources=sources,
        top_k=4,
        minimum_hits_per_source=1,
    )

    assert [(hit.chunk.source_ref, hit.chunk.chunk_no) for hit in selected] == [
        ("sources/a.md", 0),
        ("sources/a.md", 1),
        ("sources/b.md", 0),
        ("sources/c.md", 0),
    ]
    assert [hit.hybrid_score for hit in selected] == [1.0, 0.9, 0.7, 0.6]


def test_source_floor_never_fabricates_a_missing_source_candidate() -> None:
    hits = [
        _hit("sources/a.md", "a", 0, 1.0),
        _hit("sources/a.md", "a", 1, 0.9),
        _hit("sources/b.md", "b", 0, 0.8),
    ]
    sources = (("sources/a.md", "a"), ("sources/b.md", "b"), ("sources/c.md", "c"))

    selected = retrieval.select_minimum_source_hits(
        hits,
        sources=sources,
        top_k=3,
        minimum_hits_per_source=1,
    )

    assert selected == hits
    assert all(hit.chunk.source_ref != "sources/c.md" for hit in selected)


def test_source_floor_rejects_an_impossible_slot_requirement() -> None:
    with pytest.raises(ValueError, match="more source slots than top_k"):
        retrieval.select_minimum_source_hits(
            [],
            sources=(("sources/a.md", "a"), ("sources/b.md", "b")),
            top_k=1,
            minimum_hits_per_source=1,
        )


def test_scope_seam_passes_only_declared_floor_to_existing_retrieval_owner(monkeypatch) -> None:
    resolution = retrieval_scope.RetrievalScopeResolution(
        project_id="project-a",
        principal_ref="human:test",
        sources=(
            retrieval_scope.ResolvedRetrievalSource(
                document_id="doc-a",
                purpose="current_working",
                document_version_id="version-a",
                dossier="dossier-a",
                source_ref="sources/a.md",
                source_digest="a",
                source_version=1,
            ),
        ),
    )
    monkeypatch.setattr(
        retrieval_scope,
        "resolve_accessible_applicable_sources",
        lambda *args, **kwargs: resolution,
    )
    captured = {}

    def retrieve(*args, **kwargs):
        captured.update(kwargs)
        return []

    monkeypatch.setattr(retrieval_scope.retrieval, "retrieve_hybrid_exact_scoped", retrieve)

    returned_resolution, hits = retrieval_scope.retrieve_accessible_applicable_hybrid(
        object(),
        _principal(),
        contract=_contract(minimum_hits_per_source=1),
        project_id="project-a",
        requested_documents=(("doc-a", "current_working"),),
        query="compare",
    )

    assert returned_resolution is resolution
    assert hits == []
    assert captured["minimum_hits_per_source"] == 1
    assert captured["sources"] == (("sources/a.md", "a"),)


def test_invalid_declared_source_floor_fails_closed_before_ranking(monkeypatch) -> None:
    resolution = retrieval_scope.RetrievalScopeResolution(
        project_id="project-a",
        principal_ref="human:test",
        sources=(),
    )
    monkeypatch.setattr(
        retrieval_scope,
        "resolve_accessible_applicable_sources",
        lambda *args, **kwargs: resolution,
    )
    touched = []
    monkeypatch.setattr(
        retrieval_scope.retrieval,
        "retrieve_hybrid_exact_scoped",
        lambda *args, **kwargs: touched.append(True),
    )

    with pytest.raises(retrieval_scope.RetrievalScopeError, match="non-negative integer"):
        retrieval_scope.retrieve_accessible_applicable_hybrid(
            object(),
            _principal(),
            contract=_contract(minimum_hits_per_source=True),
            project_id="project-a",
            requested_documents=(),
            query="compare",
        )

    assert touched == []
