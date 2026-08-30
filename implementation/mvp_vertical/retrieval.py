"""Bounded lexical and hybrid retrieval candidates.

This module adds replaceable execution-side retrieval paths without changing
Pantheon authority. Every database query applies the Task Contract perimeter
before ranking. Retrieved material remains candidate context, never Evidence or
truth.
"""

from __future__ import annotations

from dataclasses import dataclass

import psycopg

from .contract import TaskContract, assert_source_in_scope
from .store import RetrievedChunk, retrieve_exact_scoped, retrieve_scoped


@dataclass(frozen=True)
class HybridRetrievedChunk:
    """One source-linked retrieval candidate with transparent fusion metrics."""

    chunk: RetrievedChunk
    hybrid_score: float
    semantic_rank: int | None
    lexical_rank: int | None

    @property
    def retrieval_methods(self) -> tuple[str, ...]:
        methods: list[str] = []
        if self.semantic_rank is not None:
            methods.append("semantic")
        if self.lexical_rank is not None:
            methods.append("lexical")
        return tuple(methods)


def _validate_limits(top_k: int, candidate_k: int) -> None:
    if top_k < 1:
        raise ValueError("top_k must be at least 1")
    if candidate_k < top_k:
        raise ValueError("candidate_k must be greater than or equal to top_k")
    if candidate_k > 100:
        raise ValueError("candidate_k must not exceed 100")


def _exact_scope_columns(
    contract: TaskContract,
    sources: tuple[tuple[str, str], ...],
) -> tuple[list[str], list[str]]:
    source_refs: list[str] = []
    source_digests: list[str] = []
    seen: set[tuple[str, str]] = set()
    for source_ref, source_digest in sources:
        assert_source_in_scope(contract, source_ref)
        digest = str(source_digest or "").strip()
        if not digest:
            raise ValueError("exact retrieval source_digest is required")
        key = (source_ref, digest)
        if key in seen:
            continue
        seen.add(key)
        source_refs.append(source_ref)
        source_digests.append(digest)
    return source_refs, source_digests


def retrieve_lexical_scoped(
    conn: psycopg.Connection,
    contract: TaskContract,
    query: str,
    top_k: int = 8,
) -> list[RetrievedChunk]:
    """Retrieve lexical candidates from current source versions in scope.

    PostgreSQL full-text ranking is used as a replaceable candidate capability.
    The returned ``distance`` is ``1 - normalized lexical rank`` so existing
    consumers can still treat lower values as closer. It is not a probability
    and must not be interpreted as Evidence quality.
    """
    if top_k < 1 or top_k > 100:
        raise ValueError("top_k must be between 1 and 100")
    if not query.strip():
        return []

    with conn.cursor() as cur:
        cur.execute(
            """
            WITH bounded AS (
                SELECT c.*, p.content_type, p.page_start, p.page_end,
                       p.structural_locator, p.parent_heading, p.section_path,
                       p.quality_flags,
                       websearch_to_tsquery('simple', %s) AS lexical_query
                  FROM chunks c
                  JOIN source_documents d
                    ON d.dossier = c.dossier
                   AND d.source_ref = c.source_ref
                   AND d.source_digest = c.source_digest
                  LEFT JOIN retrieval_chunk_projections p
                    ON p.dossier = c.dossier
                   AND p.source_ref = c.source_ref
                   AND p.source_digest = c.source_digest
                   AND p.chunk_no = c.chunk_no
                 WHERE c.dossier = %s
                   AND c.source_ref = ANY(%s)
            ), ranked AS (
                SELECT *,
                       ts_rank_cd(
                           to_tsvector('simple', body), lexical_query, 32
                       ) AS lexical_rank
                  FROM bounded
                 WHERE to_tsvector('simple', body) @@ lexical_query
            )
            SELECT source_ref, chunk_no, body,
                   1.0 - LEAST(1.0, lexical_rank) AS distance,
                   contract_id, contract_digest, ingestion_id, source_digest,
                   COALESCE(content_type, ''), page_start, page_end,
                   COALESCE(structural_locator, ''), parent_heading,
                   COALESCE(section_path, '[]'::jsonb),
                   COALESCE(quality_flags, '[]'::jsonb)
              FROM ranked
             ORDER BY lexical_rank DESC, source_ref ASC, source_digest ASC, chunk_no ASC
             LIMIT %s
            """,
            (query, contract.dossier, list(contract.sources), top_k),
        )
        return [
            RetrievedChunk(
                *row[:-2],
                section_path=tuple(row[-2] or ()),
                quality_flags=tuple(row[-1] or ()),
            )
            for row in cur.fetchall()
        ]


def retrieve_lexical_exact_scoped(
    conn: psycopg.Connection,
    contract: TaskContract,
    query: str,
    *,
    sources: tuple[tuple[str, str], ...],
    top_k: int = 8,
) -> list[RetrievedChunk]:
    """Rank lexical candidates only inside exact source-ref/digest identities."""
    if top_k < 1 or top_k > 100:
        raise ValueError("top_k must be between 1 and 100")
    if not query.strip() or not sources:
        return []
    source_refs, source_digests = _exact_scope_columns(contract, sources)

    with conn.cursor() as cur:
        cur.execute(
            """
            WITH allowed AS (
                SELECT *
                  FROM unnest(%s::text[], %s::text[])
                       AS exact_source(source_ref, source_digest)
            ), bounded AS (
                SELECT c.*, p.content_type, p.page_start, p.page_end,
                       p.structural_locator, p.parent_heading, p.section_path,
                       p.quality_flags,
                       websearch_to_tsquery('simple', %s) AS lexical_query
                  FROM chunks c
                  JOIN allowed a
                    ON a.source_ref = c.source_ref
                   AND a.source_digest = c.source_digest
                  LEFT JOIN retrieval_chunk_projections p
                    ON p.dossier = c.dossier
                   AND p.source_ref = c.source_ref
                   AND p.source_digest = c.source_digest
                   AND p.chunk_no = c.chunk_no
                 WHERE c.dossier = %s
            ), ranked AS (
                SELECT *,
                       ts_rank_cd(
                           to_tsvector('simple', body), lexical_query, 32
                       ) AS lexical_rank
                  FROM bounded
                 WHERE to_tsvector('simple', body) @@ lexical_query
            )
            SELECT source_ref, chunk_no, body,
                   1.0 - LEAST(1.0, lexical_rank) AS distance,
                   contract_id, contract_digest, ingestion_id, source_digest,
                   COALESCE(content_type, ''), page_start, page_end,
                   COALESCE(structural_locator, ''), parent_heading,
                   COALESCE(section_path, '[]'::jsonb),
                   COALESCE(quality_flags, '[]'::jsonb)
              FROM ranked
             ORDER BY lexical_rank DESC, source_ref ASC, source_digest ASC, chunk_no ASC
             LIMIT %s
            """,
            (source_refs, source_digests, query, contract.dossier, top_k),
        )
        return [
            RetrievedChunk(
                *row[:-2],
                section_path=tuple(row[-2] or ()),
                quality_flags=tuple(row[-1] or ()),
            )
            for row in cur.fetchall()
        ]


def reciprocal_rank_fusion(
    semantic: list[RetrievedChunk],
    lexical: list[RetrievedChunk],
    *,
    top_k: int = 4,
    candidate_k: int = 12,
    rrf_k: int = 60,
    semantic_weight: float = 1.0,
    lexical_weight: float = 1.0,
) -> list[HybridRetrievedChunk]:
    """Fuse two bounded rankings deterministically using weighted RRF."""
    _validate_limits(top_k, candidate_k)
    if rrf_k < 1:
        raise ValueError("rrf_k must be at least 1")
    if semantic_weight < 0 or lexical_weight < 0:
        raise ValueError("retrieval weights must be non-negative")
    if semantic_weight == 0 and lexical_weight == 0:
        raise ValueError("at least one retrieval weight must be positive")

    semantic = semantic[:candidate_k]
    lexical = lexical[:candidate_k]
    by_key: dict[tuple[str, str, int], dict] = {}

    for rank, chunk in enumerate(semantic, start=1):
        key = (chunk.source_ref, chunk.source_digest, chunk.chunk_no)
        item = by_key.setdefault(
            key,
            {"chunk": chunk, "score": 0.0, "semantic_rank": None, "lexical_rank": None},
        )
        item["semantic_rank"] = rank
        item["score"] += semantic_weight / (rrf_k + rank)

    for rank, chunk in enumerate(lexical, start=1):
        key = (chunk.source_ref, chunk.source_digest, chunk.chunk_no)
        item = by_key.setdefault(
            key,
            {"chunk": chunk, "score": 0.0, "semantic_rank": None, "lexical_rank": None},
        )
        item["lexical_rank"] = rank
        item["score"] += lexical_weight / (rrf_k + rank)

    fused = [
        HybridRetrievedChunk(
            chunk=item["chunk"],
            hybrid_score=item["score"],
            semantic_rank=item["semantic_rank"],
            lexical_rank=item["lexical_rank"],
        )
        for item in by_key.values()
    ]
    fused.sort(
        key=lambda hit: (
            -hit.hybrid_score,
            hit.semantic_rank if hit.semantic_rank is not None else candidate_k + 1,
            hit.lexical_rank if hit.lexical_rank is not None else candidate_k + 1,
            hit.chunk.source_ref,
            hit.chunk.source_digest,
            hit.chunk.chunk_no,
        )
    )
    return fused[:top_k]


def select_minimum_source_hits(
    hits: list[HybridRetrievedChunk],
    *,
    sources: tuple[tuple[str, str], ...],
    top_k: int,
    minimum_hits_per_source: int = 0,
) -> list[HybridRetrievedChunk]:
    """Apply an opt-in source-representation floor to an already-ranked pool.

    This selector never creates a candidate and never changes RRF scores. For
    each exact source identity it may retain up to ``minimum_hits_per_source``
    candidates that already exist in ``hits``; remaining slots are filled by
    the original global order. The returned list is then restored to that same
    global order.

    A selected source with no candidate in the ranked pool stays absent. Source
    selection is a comparison perimeter, not proof that content is relevant,
    true, or admissible as Evidence.
    """
    if top_k < 1:
        raise ValueError("top_k must be at least 1")
    if minimum_hits_per_source < 0:
        raise ValueError("minimum_hits_per_source must be non-negative")

    source_keys = list(dict.fromkeys((str(ref), str(digest)) for ref, digest in sources))
    if minimum_hits_per_source == 0 or not source_keys:
        return hits[:top_k]
    if minimum_hits_per_source * len(source_keys) > top_k:
        raise ValueError(
            "minimum_hits_per_source cannot require more source slots than top_k"
        )

    def hit_key(hit: HybridRetrievedChunk) -> tuple[str, str, int]:
        return (hit.chunk.source_ref, hit.chunk.source_digest, hit.chunk.chunk_no)

    selected: list[HybridRetrievedChunk] = []
    selected_keys: set[tuple[str, str, int]] = set()

    for source_ref, source_digest in source_keys:
        retained = 0
        for hit in hits:
            if (
                hit.chunk.source_ref == source_ref
                and hit.chunk.source_digest == source_digest
                and hit_key(hit) not in selected_keys
            ):
                selected.append(hit)
                selected_keys.add(hit_key(hit))
                retained += 1
                if retained >= minimum_hits_per_source:
                    break

    for hit in hits:
        if len(selected) >= top_k:
            break
        key = hit_key(hit)
        if key in selected_keys:
            continue
        selected.append(hit)
        selected_keys.add(key)

    global_order = {hit_key(hit): index for index, hit in enumerate(hits)}
    selected.sort(key=lambda hit: global_order[hit_key(hit)])
    return selected[:top_k]


def retrieve_hybrid_scoped(
    conn: psycopg.Connection,
    contract: TaskContract,
    query: str,
    *,
    top_k: int = 4,
    candidate_k: int = 12,
    rrf_k: int = 60,
    semantic_weight: float = 1.0,
    lexical_weight: float = 1.0,
) -> list[HybridRetrievedChunk]:
    """Run current-version scoped semantic and lexical retrieval, then fuse."""
    _validate_limits(top_k, candidate_k)
    semantic = retrieve_scoped(conn, contract, query, top_k=candidate_k)
    lexical = retrieve_lexical_scoped(conn, contract, query, top_k=candidate_k)
    return reciprocal_rank_fusion(
        semantic,
        lexical,
        top_k=top_k,
        candidate_k=candidate_k,
        rrf_k=rrf_k,
        semantic_weight=semantic_weight,
        lexical_weight=lexical_weight,
    )


def retrieve_hybrid_exact_scoped(
    conn: psycopg.Connection,
    contract: TaskContract,
    query: str,
    *,
    sources: tuple[tuple[str, str], ...],
    top_k: int = 4,
    candidate_k: int = 12,
    rrf_k: int = 60,
    semantic_weight: float = 1.0,
    lexical_weight: float = 1.0,
    minimum_hits_per_source: int = 0,
) -> list[HybridRetrievedChunk]:
    """Run hybrid ranking inside exact immutable identities.

    ``minimum_hits_per_source`` is an opt-in final-selection policy over the
    already-ranked candidate pool. Zero preserves the historical global top-k
    behavior exactly.
    """
    _validate_limits(top_k, candidate_k)
    semantic = retrieve_exact_scoped(
        conn,
        contract,
        query,
        sources=sources,
        top_k=candidate_k,
    )
    lexical = retrieve_lexical_exact_scoped(
        conn,
        contract,
        query,
        sources=sources,
        top_k=candidate_k,
    )
    pool_top_k = candidate_k if minimum_hits_per_source else top_k
    fused = reciprocal_rank_fusion(
        semantic,
        lexical,
        top_k=pool_top_k,
        candidate_k=candidate_k,
        rrf_k=rrf_k,
        semantic_weight=semantic_weight,
        lexical_weight=lexical_weight,
    )
    return select_minimum_source_hits(
        fused,
        sources=sources,
        top_k=top_k,
        minimum_hits_per_source=minimum_hits_per_source,
    )
