"""pgvector store: bounded ingestion and scope-first retrieval.

The two rules that matter live here:

1. Ingestion reads ONLY the contract's declared sources — anything else
   raises before touching the database.
2. Retrieval filters on the declared perimeter in SQL *before* vector
   ranking. A query cannot see outside the contract by construction.
"""

from __future__ import annotations

import hashlib
import json
import mimetypes
import os
import uuid
from dataclasses import dataclass
from pathlib import Path

import psycopg

from .contract import TaskContract, assert_source_in_scope, resolve_source_within
from .documents import (
    ConvertedDocument,
    DocumentConversionError,
    DocumentConverter,
    converter_for,
    file_digest,
)
from .embedder import DIM, embed, to_pgvector
from .naming import DocumentName, parse_document_name

# Audit identity (external review, finding #6): every chunk carries enough to
# prove, at retrieval time, exactly what produced it — which contract version
# (contract_id + contract_digest), which ingestion run (ingestion_id, an
# injectable nonce, finding #8), and which source version (source_digest).
#
# This DDL runs on EVERY connect(), so it must stay lock-light: CREATE TABLE IF
# NOT EXISTS is a no-op when the table is present. We deliberately do NOT ALTER
# here — an ALTER … ADD COLUMN takes an ACCESS EXCLUSIVE lock on every connect,
# which deadlocks against a long-lived session connection holding chunks (that
# hung a CI run). A pre-existing table from before this change must be dropped
# and re-created (DROP TABLE chunks); the DEFAULT '' keeps a legacy partial
# INSERT that omits the columns valid.
DDL = f"""
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS chunks (
    id        BIGSERIAL PRIMARY KEY,
    dossier   TEXT NOT NULL,
    source_ref TEXT NOT NULL,
    chunk_no  INT  NOT NULL,
    body      TEXT NOT NULL,
    embedding vector({DIM}) NOT NULL,
    contract_id     TEXT NOT NULL DEFAULT '',
    contract_digest TEXT NOT NULL DEFAULT '',
    ingestion_id    TEXT NOT NULL DEFAULT '',
    source_digest   TEXT NOT NULL DEFAULT '',
    UNIQUE (dossier, source_ref, chunk_no)
);
CREATE TABLE IF NOT EXISTS source_documents (
    document_id TEXT PRIMARY KEY,
    dossier TEXT NOT NULL,
    parent_project_id TEXT NOT NULL,
    source_ref TEXT NOT NULL,
    source_digest TEXT NOT NULL,
    media_type TEXT NOT NULL,
    byte_size BIGINT NOT NULL,
    analysis_status TEXT NOT NULL,
    current_extraction_id TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (dossier, source_ref)
);
CREATE TABLE IF NOT EXISTS document_naming (
    document_id TEXT PRIMARY KEY REFERENCES source_documents(document_id) ON DELETE CASCADE,
    project_code TEXT NOT NULL,
    revision_index TEXT NOT NULL,
    phase_code TEXT NOT NULL,
    phase_folder TEXT NOT NULL,
    distributor TEXT NOT NULL,
    document_type TEXT NOT NULL,
    object_name TEXT NOT NULL,
    document_date DATE NOT NULL,
    extension TEXT NOT NULL,
    filename TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS extraction_runs (
    extraction_id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL REFERENCES source_documents(document_id) ON DELETE CASCADE,
    contract_id TEXT NOT NULL,
    contract_digest TEXT NOT NULL,
    source_digest TEXT NOT NULL,
    converter TEXT NOT NULL,
    converter_version TEXT NOT NULL,
    config_digest TEXT NOT NULL,
    status TEXT NOT NULL,
    markdown_content TEXT,
    document_json JSONB,
    chunk_count INT NOT NULL DEFAULT 0,
    processing_time DOUBLE PRECISION,
    quality_flags JSONB NOT NULL DEFAULT '[]'::jsonb,
    error TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS extraction_cache_lookup
    ON extraction_runs (document_id, source_digest, converter, converter_version, config_digest);
CREATE TABLE IF NOT EXISTS document_versions (
    document_id TEXT NOT NULL REFERENCES source_documents(document_id) ON DELETE CASCADE,
    version INT NOT NULL CHECK (version > 0),
    source_ref TEXT NOT NULL,
    source_digest TEXT NOT NULL,
    media_type TEXT NOT NULL,
    byte_size BIGINT NOT NULL CHECK (byte_size > 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (document_id, version),
    UNIQUE (document_id, source_digest)
);
CREATE TABLE IF NOT EXISTS extraction_observations (
    extraction_id TEXT PRIMARY KEY REFERENCES extraction_runs(extraction_id) ON DELETE CASCADE,
    observation_kind TEXT NOT NULL CHECK (
        observation_kind IN ('direct_text', 'fixture', 'live_parser')
    )
);
CREATE TABLE IF NOT EXISTS document_extraction_bindings (
    document_id TEXT PRIMARY KEY REFERENCES source_documents(document_id) ON DELETE CASCADE,
    extraction_id TEXT NOT NULL REFERENCES extraction_runs(extraction_id) ON DELETE RESTRICT,
    ingestion_id TEXT NOT NULL,
    cache_reused BOOLEAN NOT NULL DEFAULT FALSE,
    bound_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS knowledge_items (
    knowledge_id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL REFERENCES source_documents(document_id) ON DELETE RESTRICT,
    source_version INT NOT NULL CHECK (source_version > 0),
    source_digest TEXT NOT NULL,
    extraction_id TEXT NOT NULL REFERENCES extraction_runs(extraction_id) ON DELETE RESTRICT,
    title TEXT NOT NULL CHECK (length(title) > 0),
    family TEXT NOT NULL CHECK (
        family IN ('referentiels', 'responsabilite', 'methodologie', 'techniques', 'reglementations')
    ),
    markdown TEXT NOT NULL CHECK (length(markdown) > 0),
    markdown_digest TEXT NOT NULL,
    source_chunk_refs JSONB NOT NULL,
    review_status TEXT NOT NULL CHECK (
        review_status IN ('generated_unreviewed', 'needs_review', 'reviewed', 'superseded')
    ),
    version INT NOT NULL CHECK (version > 0),
    created_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS knowledge_project_lookup
    ON knowledge_items (document_id, updated_at DESC);
CREATE TABLE IF NOT EXISTS knowledge_source_chunks (
    knowledge_id TEXT NOT NULL REFERENCES knowledge_items(knowledge_id) ON DELETE CASCADE,
    chunk_ref TEXT NOT NULL,
    document_id TEXT NOT NULL REFERENCES source_documents(document_id) ON DELETE RESTRICT,
    extraction_id TEXT NOT NULL REFERENCES extraction_runs(extraction_id) ON DELETE RESTRICT,
    ordinal INT NOT NULL CHECK (ordinal >= 0),
    text_digest TEXT NOT NULL,
    source_ref TEXT NOT NULL,
    source_digest TEXT NOT NULL,
    structural_locator TEXT NOT NULL,
    PRIMARY KEY (knowledge_id, chunk_ref)
);
CREATE TABLE IF NOT EXISTS knowledge_events (
    event_id TEXT PRIMARY KEY,
    aggregate_kind TEXT NOT NULL DEFAULT 'knowledge' CHECK (aggregate_kind = 'knowledge'),
    aggregate_ref TEXT NOT NULL REFERENCES knowledge_items(knowledge_id) ON DELETE RESTRICT,
    event_type TEXT NOT NULL CHECK (
        event_type IN ('knowledge_published', 'knowledge_revised', 'knowledge_review_status_changed')
    ),
    actor TEXT NOT NULL,
    actor_kind TEXT NOT NULL CHECK (actor_kind IN ('human', 'hermes', 'system')),
    expected_version INT NOT NULL CHECK (expected_version >= 0),
    resulting_version INT NOT NULL CHECK (resulting_version = expected_version + 1),
    idempotency_key TEXT NOT NULL UNIQUE,
    payload_digest TEXT NOT NULL,
    result_snapshot JSONB NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS knowledge_edit_requests (
    request_id TEXT PRIMARY KEY,
    knowledge_id TEXT NOT NULL REFERENCES knowledge_items(knowledge_id) ON DELETE CASCADE,
    instruction_kind TEXT NOT NULL CHECK (
        instruction_kind IN ('rewrite', 'expand', 'simplify', 'verify', 'move_to_lot')
    ),
    instruction TEXT NOT NULL,
    base_version INT NOT NULL CHECK (base_version > 0),
    selection_start INT NOT NULL CHECK (selection_start >= 0),
    selection_end INT NOT NULL CHECK (selection_end >= selection_start),
    selected_text_digest TEXT NOT NULL,
    replacement_markdown TEXT,
    status TEXT NOT NULL CHECK (
        status IN ('queued_for_hermes', 'proposed', 'applied', 'conflict', 'rejected')
    ),
    requested_by TEXT NOT NULL,
    request_idempotency_key TEXT NOT NULL UNIQUE,
    request_payload_digest TEXT NOT NULL,
    apply_idempotency_key TEXT UNIQUE,
    apply_payload_digest TEXT,
    apply_result_snapshot JSONB,
    applied_version INT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def contract_digest(contract: TaskContract) -> str:
    """sha256 over the canonical contract — proves which contract version an
    ingested chunk was scoped by. Same shape/discipline as the gate's digests."""
    canonical = json.dumps(contract.raw, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return _sha256(canonical)


def _document_id(dossier: str, source_ref: str) -> str:
    identity = dossier + "\0" + source_ref
    return f"doc-{_sha256(identity)[:24]}"


def _extraction_id(ingestion_id: str, document_id: str) -> str:
    return f"ext-{ingestion_id}-{document_id.removeprefix('doc-')}"


def _observation_kind(converter: DocumentConverter | None) -> str | None:
    if converter is None:
        return None
    kind = getattr(converter, "observation_kind", None)
    if kind not in {"direct_text", "fixture", "live_parser"}:
        raise DocumentConversionError(
            "document converter must declare observation_kind as direct_text, fixture or live_parser"
        )
    return kind


def _record_document_version(
    conn: psycopg.Connection,
    document_id: str,
    source_ref: str,
    source_digest: str,
    media_type: str,
    byte_size: int,
) -> None:
    conn.execute(
        """
        INSERT INTO document_versions (
            document_id, version, source_ref, source_digest, media_type, byte_size
        )
        SELECT %s, COALESCE(MAX(version), 0) + 1, %s, %s, %s, %s
          FROM document_versions
         WHERE document_id = %s
           AND NOT EXISTS (
               SELECT 1 FROM document_versions
                WHERE document_id = %s AND source_digest = %s
           )
        ON CONFLICT (document_id, source_digest) DO NOTHING
        """,
        (
            document_id, source_ref, source_digest, media_type, byte_size,
            document_id, document_id, source_digest,
        ),
    )


def _parent_project_id(contract: TaskContract) -> str:
    scope = contract.raw.get("scope") or {}
    return str(scope.get("parent_project_id") or scope.get("project_id") or contract.dossier)


def dsn_from_env() -> str:
    return os.environ.get(
        "MVP_PG_DSN",
        "postgresql://mvp:mvp@localhost:5433/mvp",
    )


@dataclass(frozen=True)
class RetrievedChunk:
    source_ref: str
    chunk_no: int
    body: str
    distance: float
    # Audit identity (finding #6). Default to "" so a legacy/manual construction
    # (e.g. test helpers, or a pre-migration row) stays valid.
    contract_id: str = ""
    contract_digest: str = ""
    ingestion_id: str = ""
    source_digest: str = ""

    @property
    def retrieval_trace(self) -> str:
        # Unchanged format — verify_draft parses [source_ref#chunk-N] from it.
        return f"pgvector://chunks/{self.source_ref}#chunk-{self.chunk_no}"

    @property
    def retrieval_audit(self) -> dict:
        """The auditable identity of this chunk: which contract version, which
        ingestion run, and which source version produced it."""
        return {
            "contract_id": self.contract_id,
            "contract_digest": self.contract_digest,
            "ingestion_id": self.ingestion_id,
            "source_digest": self.source_digest,
        }


def connect(dsn: str | None = None) -> psycopg.Connection:
    conn = psycopg.connect(dsn or dsn_from_env())
    with conn.cursor() as cur:
        cur.execute(DDL)
    conn.commit()
    return conn


def chunk_text(text: str, max_chars: int = 600) -> list[str]:
    blocks, current = [], ""
    for para in text.split("\n\n"):
        para = para.strip()
        if not para:
            continue
        if len(current) + len(para) + 2 > max_chars and current:
            blocks.append(current)
            current = para
        else:
            current = f"{current}\n\n{para}" if current else para
    if current:
        blocks.append(current)
    return blocks


def _cached_conversion(
    conn: psycopg.Connection,
    *,
    document_id: str,
    source_digest: str,
    converter: DocumentConverter,
) -> tuple[ConvertedDocument, str] | None:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT extraction_id, markdown_content, document_json, status,
                   processing_time, quality_flags
              FROM extraction_runs
             WHERE document_id = %s AND source_digest = %s
               AND converter = %s AND converter_version = %s AND config_digest = %s
               AND status IN ('ready', 'needs_review')
             ORDER BY finished_at DESC
             LIMIT 1
            """,
            (
                document_id,
                source_digest,
                converter.converter,
                converter.converter_version,
                converter.config_digest,
            ),
        )
        row = cur.fetchone()
    if row is None:
        return None
    extraction_id, markdown, document_json, status, processing_time, quality_flags = row
    return (
        ConvertedDocument(
            markdown=markdown,
            document_json=document_json,
            converter=converter.converter,
            converter_version=converter.converter_version,
            config_digest=converter.config_digest,
            status=status,
            processing_time=processing_time,
            quality_flags=tuple(quality_flags or ()) + ("cache_reused",),
        ),
        extraction_id,
    )


def _upsert_document_naming(
    conn: psycopg.Connection,
    document_id: str,
    naming: DocumentName | None,
) -> None:
    if naming is None:
        return
    conn.execute(
        """
        INSERT INTO document_naming (
            document_id, project_code, revision_index, phase_code, phase_folder,
            distributor, document_type, object_name, document_date, extension, filename
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (document_id) DO UPDATE SET
            project_code = EXCLUDED.project_code,
            revision_index = EXCLUDED.revision_index,
            phase_code = EXCLUDED.phase_code,
            phase_folder = EXCLUDED.phase_folder,
            distributor = EXCLUDED.distributor,
            document_type = EXCLUDED.document_type,
            object_name = EXCLUDED.object_name,
            document_date = EXCLUDED.document_date,
            extension = EXCLUDED.extension,
            filename = EXCLUDED.filename
        """,
        (
            document_id, naming.project_code, naming.revision_index,
            naming.phase_code, naming.phase_folder, naming.distributor,
            naming.document_type, naming.object_name, naming.document_date,
            naming.extension, naming.filename,
        ),
    )


def _record_failed_extraction(
    conn: psycopg.Connection,
    *,
    contract: TaskContract,
    source_ref: str,
    path: Path,
    source_digest: str,
    ingestion_id: str,
    converter: DocumentConverter | None,
    error: Exception,
    naming: DocumentName | None = None,
) -> None:
    document_id = _document_id(contract.dossier, source_ref)
    extraction_id = _extraction_id(ingestion_id, document_id)
    media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    with conn.transaction():
        conn.execute(
            """
            INSERT INTO source_documents (
                document_id, dossier, parent_project_id, source_ref, source_digest, media_type,
                byte_size, analysis_status, current_extraction_id
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, 'failed', %s)
            ON CONFLICT (dossier, source_ref) DO UPDATE SET
                parent_project_id = EXCLUDED.parent_project_id,
                source_digest = EXCLUDED.source_digest,
                media_type = EXCLUDED.media_type,
                byte_size = EXCLUDED.byte_size,
                analysis_status = 'failed',
                current_extraction_id = EXCLUDED.current_extraction_id,
                updated_at = CURRENT_TIMESTAMP
            """,
            (
                document_id, contract.dossier, _parent_project_id(contract),
                source_ref, source_digest,
                media_type, path.stat().st_size, extraction_id,
            ),
        )
        _upsert_document_naming(conn, document_id, naming)
        _record_document_version(
            conn, document_id, source_ref, source_digest, media_type, path.stat().st_size
        )
        conn.execute(
            """
            INSERT INTO extraction_runs (
                extraction_id, document_id, contract_id, contract_digest,
                source_digest, converter, converter_version, config_digest,
                status, error
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'failed', %s)
            """,
            (
                extraction_id, document_id, contract.contract_id, contract_digest(contract),
                source_digest,
                converter.converter if converter else "unavailable",
                converter.converter_version if converter else "unknown",
                converter.config_digest if converter else "unknown",
                str(error),
            ),
        )
        observation_kind = _observation_kind(converter)
        if observation_kind is not None:
            conn.execute(
                "INSERT INTO extraction_observations (extraction_id, observation_kind) "
                "VALUES (%s, %s)",
                (extraction_id, observation_kind),
            )
        conn.execute(
            """
            INSERT INTO document_extraction_bindings (
                document_id, extraction_id, ingestion_id, cache_reused
            ) VALUES (%s, %s, %s, FALSE)
            ON CONFLICT (document_id) DO UPDATE SET
                extraction_id = EXCLUDED.extraction_id,
                ingestion_id = EXCLUDED.ingestion_id,
                cache_reused = FALSE,
                bound_at = CURRENT_TIMESTAMP
            """,
            (document_id, extraction_id, ingestion_id),
        )
    conn.commit()


def ingest(
    conn: psycopg.Connection,
    contract: TaskContract,
    root: Path,
    *,
    ingestion_id: str | None = None,
    docling: DocumentConverter | None = None,
    source_refs: tuple[str, ...] | None = None,
    replace_dossier: bool = True,
    naming_by_source: dict[str, DocumentName] | None = None,
) -> int:
    """Ingest the contract's declared sources — and nothing else.

    Every chunk is stamped with its audit identity (finding #6): the contract
    id and digest, the ingestion id (a per-run nonce — injectable for tests and
    replay, finding #8; defaults to a fresh uuid), and the digest of the exact
    source content it came from. Re-ingesting replaces the dossier's chunks with
    a new ingestion_id, so what is retrievable is always provably from one run.
    """
    ingestion_id = ingestion_id or uuid.uuid4().hex
    cdigest = contract_digest(contract)
    selected_sources = source_refs if source_refs is not None else contract.sources
    if not selected_sources:
        return 0
    prepared: list[
        tuple[
            str, Path, str, ConvertedDocument, list[str], DocumentName | None, str, str | None
        ]
    ] = []
    for source_ref in selected_sources:
        assert_source_in_scope(contract, source_ref)  # explicit guard at the effect boundary
        naming = (naming_by_source or {}).get(source_ref)
        path = resolve_source_within(root, source_ref, contract.contract_id)
        sdigest = file_digest(path)
        selected: DocumentConverter | None = None
        try:
            selected = converter_for(path, docling)
            document_id = _document_id(contract.dossier, source_ref)
            cached = _cached_conversion(
                conn,
                document_id=document_id,
                source_digest=sdigest,
                converter=selected,
            )
            if cached is None:
                converted = selected.convert(path)
                reused_extraction_id = None
            else:
                converted, reused_extraction_id = cached
            chunks = chunk_text(converted.markdown)
            if not chunks:
                raise DocumentConversionError(
                    f"conversion produced no retrievable content: {path.name}"
                )
            prepared.append(
                (
                    source_ref, path, sdigest, converted, chunks, naming,
                    _observation_kind(selected), reused_extraction_id,
                )
            )
        except (DocumentConversionError, OSError) as exc:
            _record_failed_extraction(
                conn,
                contract=contract,
                source_ref=source_ref,
                path=path,
                source_digest=sdigest,
                ingestion_id=ingestion_id,
                converter=selected,
                error=exc,
                naming=naming,
            )
            raise

    # Cache lookups are reads but psycopg starts a transaction for them. End
    # that read transaction before the atomic replacement below.
    conn.commit()
    total = 0
    with conn.transaction():
        if replace_dossier:
            conn.execute("DELETE FROM chunks WHERE dossier = %s", (contract.dossier,))
        else:
            conn.execute(
                "DELETE FROM chunks WHERE dossier = %s AND source_ref = ANY(%s)",
                (contract.dossier, list(selected_sources)),
            )
        for (
            source_ref, path, sdigest, converted, chunks, naming,
            observation_kind, reused_extraction_id,
        ) in prepared:
            document_id = _document_id(contract.dossier, source_ref)
            extraction_id = reused_extraction_id or _extraction_id(ingestion_id, document_id)
            media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            conn.execute(
                """
                INSERT INTO source_documents (
                    document_id, dossier, parent_project_id, source_ref, source_digest, media_type,
                    byte_size, analysis_status, current_extraction_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (dossier, source_ref) DO UPDATE SET
                    parent_project_id = EXCLUDED.parent_project_id,
                    source_digest = EXCLUDED.source_digest,
                    media_type = EXCLUDED.media_type,
                    byte_size = EXCLUDED.byte_size,
                    analysis_status = EXCLUDED.analysis_status,
                    current_extraction_id = EXCLUDED.current_extraction_id,
                    updated_at = CURRENT_TIMESTAMP
                """,
                (
                    document_id, contract.dossier, _parent_project_id(contract), source_ref,
                    sdigest, media_type,
                    path.stat().st_size, converted.status, extraction_id,
                ),
            )
            _upsert_document_naming(conn, document_id, naming)
            _record_document_version(
                conn, document_id, source_ref, sdigest, media_type, path.stat().st_size
            )
            if reused_extraction_id is None:
                conn.execute(
                    """
                    INSERT INTO extraction_runs (
                        extraction_id, document_id, contract_id, contract_digest,
                        source_digest, converter, converter_version, config_digest,
                        status, markdown_content, document_json, chunk_count,
                        processing_time, quality_flags
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb,
                              %s, %s, %s::jsonb)
                    """,
                    (
                        extraction_id, document_id, contract.contract_id, cdigest,
                        sdigest, converted.converter, converted.converter_version,
                        converted.config_digest, converted.status, converted.markdown,
                        json.dumps(converted.document_json), len(chunks),
                        converted.processing_time, json.dumps(converted.quality_flags),
                    ),
                )
                conn.execute(
                    """
                    INSERT INTO extraction_observations (extraction_id, observation_kind)
                    VALUES (%s, %s)
                    """,
                    (extraction_id, observation_kind),
                )
            conn.execute(
                """
                INSERT INTO document_extraction_bindings (
                    document_id, extraction_id, ingestion_id, cache_reused
                ) VALUES (%s, %s, %s, %s)
                ON CONFLICT (document_id) DO UPDATE SET
                    extraction_id = EXCLUDED.extraction_id,
                    ingestion_id = EXCLUDED.ingestion_id,
                    cache_reused = EXCLUDED.cache_reused,
                    bound_at = CURRENT_TIMESTAMP
                """,
                (document_id, extraction_id, ingestion_id, reused_extraction_id is not None),
            )
            for i, body in enumerate(chunks):
                conn.execute(
                    "INSERT INTO chunks"
                    " (dossier, source_ref, chunk_no, body, embedding,"
                    "  contract_id, contract_digest, ingestion_id, source_digest)"
                    " VALUES (%s, %s, %s, %s, %s::vector, %s, %s, %s, %s)",
                    (
                        contract.dossier, source_ref, i, body,
                        to_pgvector(embed(body)), contract.contract_id, cdigest,
                        ingestion_id, sdigest,
                    ),
                )
                total += 1
    return total


def intake_document(
    conn: psycopg.Connection,
    contract: TaskContract,
    root: Path,
    source_ref: str,
    *,
    ingestion_id: str | None = None,
    docling: DocumentConverter | None = None,
) -> int:
    """Validate and incrementally ingest one explicitly declared NAS document."""
    assert_source_in_scope(contract, source_ref)
    naming = parse_document_name(source_ref)
    return ingest(
        conn,
        contract,
        root,
        ingestion_id=ingestion_id,
        docling=docling,
        source_refs=(source_ref,),
        replace_dossier=False,
        naming_by_source={source_ref: naming},
    )


def get_document_card(conn: psycopg.Connection, dossier: str, source_ref: str) -> dict:
    """Return the bounded Project Document Card projection.

    The projection contains no duplicate source and no inferred authority. The
    dossier is the MVP's project parent; a future cockpit may resolve its human
    display name without changing this persistence contract.
    """
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT d.document_id, d.parent_project_id, d.source_ref, d.source_digest,
                   d.media_type, d.byte_size, d.analysis_status,
                   e.extraction_id, e.converter, e.converter_version,
                   e.quality_flags, e.chunk_count, e.error, e.finished_at,
                   o.observation_kind, b.cache_reused,
                   n.project_code, n.revision_index, n.phase_code, n.phase_folder,
                   n.distributor, n.document_type, n.object_name, n.document_date,
                   n.extension
              FROM source_documents d
              LEFT JOIN extraction_runs e ON e.extraction_id = d.current_extraction_id
              LEFT JOIN extraction_observations o ON o.extraction_id = e.extraction_id
              LEFT JOIN document_extraction_bindings b ON b.document_id = d.document_id
              LEFT JOIN document_naming n ON n.document_id = d.document_id
             WHERE d.dossier = %s AND d.source_ref = %s
            """,
            (dossier, source_ref),
        )
        row = cur.fetchone()
    if row is None:
        raise KeyError(f"unknown document source: {dossier}/{source_ref}")
    (
        document_id, parent_project_id, locator, source_digest, media_type,
        byte_size, analysis_status, extraction_id, converter,
        converter_version, quality_flags, chunk_count, error, finished_at,
        observation_kind, cache_reused,
        project_code, revision_index, phase_code, phase_folder, distributor,
        document_type, object_name, document_date, extension,
    ) = row
    return {
        "card_type": "project_document",
        "card_id": f"card-{document_id}",
        "document_id": document_id,
        "parent_project_id": parent_project_id,
        "title": Path(locator).name,
        "source_ref": locator,
        "source_digest": source_digest,
        "media_type": media_type,
        "byte_size": byte_size,
        "analysis_status": analysis_status,
        "naming": {
            "project_code": project_code,
            "revision_index": revision_index,
            "phase_code": phase_code,
            "phase_folder": phase_folder,
            "distributor": distributor,
            "document_type": document_type,
            "object_name": object_name,
            "document_date": document_date.isoformat() if document_date else None,
            "extension": extension,
            "validated": project_code is not None,
        },
        "extraction": {
            "extraction_id": extraction_id,
            "converter": converter,
            "converter_version": converter_version,
            "observation_kind": observation_kind,
            "quality_flags": list(quality_flags or []) + (["cache_reused"] if cache_reused else []),
            "chunk_count": chunk_count or 0,
            "chunk_refs": [
                f"chunk.{extraction_id}.{number:04d}" for number in range(chunk_count or 0)
            ] if extraction_id else [],
            "error": error,
            "finished_at": finished_at.isoformat() if finished_at else None,
        },
        "authority": {
            "is_source": False,
            "is_evidence": False,
            "is_memory": False,
        },
    }


def list_document_cards(conn: psycopg.Connection, parent_project_id: str) -> list[dict]:
    """List stable card projections for one project parent, newest first."""
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT dossier, source_ref
              FROM source_documents
             WHERE parent_project_id = %s
             ORDER BY updated_at DESC, source_ref ASC
            """,
            (parent_project_id,),
        )
        locators = cur.fetchall()
    return [get_document_card(conn, dossier, source_ref) for dossier, source_ref in locators]


def get_document_card_by_id(conn: psycopg.Connection, document_id: str) -> dict:
    """Resolve a card by its stable document identity."""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT dossier, source_ref FROM source_documents WHERE document_id = %s",
            (document_id,),
        )
        row = cur.fetchone()
    if row is None:
        raise KeyError(f"unknown document: {document_id}")
    return get_document_card(conn, row[0], row[1])


def get_document_markdown(conn: psycopg.Connection, document_id: str) -> str:
    """Return the current derived Markdown representation, never the original."""
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT e.markdown_content
              FROM source_documents d
              JOIN extraction_runs e ON e.extraction_id = d.current_extraction_id
             WHERE d.document_id = %s
            """,
            (document_id,),
        )
        row = cur.fetchone()
    if row is None or row[0] is None:
        raise KeyError(f"no Markdown representation for document: {document_id}")
    return row[0]


def get_document_source(conn: psycopg.Connection, document_id: str) -> tuple[str, str]:
    """Return the dossier and bounded relative source locator for preview delivery."""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT dossier, source_ref FROM source_documents WHERE document_id = %s",
            (document_id,),
        )
        row = cur.fetchone()
    if row is None:
        raise KeyError(f"unknown document: {document_id}")
    return row[0], row[1]


def retrieve_scoped(
    conn: psycopg.Connection,
    contract: TaskContract,
    query: str,
    top_k: int = 4,
) -> list[RetrievedChunk]:
    """Scope filter in SQL first, vector ranking second."""
    qvec = to_pgvector(embed(query))
    with conn.cursor() as cur:
        cur.execute(
            "SELECT source_ref, chunk_no, body, embedding <=> %s::vector AS distance,"
            "       contract_id, contract_digest, ingestion_id, source_digest"
            " FROM chunks"
            " WHERE dossier = %s AND source_ref = ANY(%s)"   # the boundary
            " ORDER BY distance ASC"
            " LIMIT %s",
            (qvec, contract.dossier, list(contract.sources), top_k),
        )
        return [RetrievedChunk(*row) for row in cur.fetchall()]
