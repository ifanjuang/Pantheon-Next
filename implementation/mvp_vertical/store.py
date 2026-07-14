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
import os
import uuid
from dataclasses import dataclass
from pathlib import Path

import psycopg

from .contract import TaskContract, assert_source_in_scope, resolve_source_within
from .embedder import DIM, embed, to_pgvector

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
"""


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def contract_digest(contract: TaskContract) -> str:
    """sha256 over the canonical contract — proves which contract version an
    ingested chunk was scoped by. Same shape/discipline as the gate's digests."""
    canonical = json.dumps(contract.raw, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return _sha256(canonical)


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


def ingest(
    conn: psycopg.Connection,
    contract: TaskContract,
    root: Path,
    *,
    ingestion_id: str | None = None,
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
    total = 0
    with conn.cursor() as cur:
        cur.execute("DELETE FROM chunks WHERE dossier = %s", (contract.dossier,))
        for source_ref in contract.sources:
            assert_source_in_scope(contract, source_ref)  # tautological by loop, kept as guard
            path = resolve_source_within(root, source_ref, contract.contract_id)
            text = path.read_text(encoding="utf-8")
            sdigest = _sha256(text)  # the exact source version ingested
            for i, body in enumerate(chunk_text(text)):
                cur.execute(
                    "INSERT INTO chunks"
                    " (dossier, source_ref, chunk_no, body, embedding,"
                    "  contract_id, contract_digest, ingestion_id, source_digest)"
                    " VALUES (%s, %s, %s, %s, %s::vector, %s, %s, %s, %s)",
                    (contract.dossier, source_ref, i, body, to_pgvector(embed(body)),
                     contract.contract_id, cdigest, ingestion_id, sdigest),
                )
                total += 1
    conn.commit()
    return total


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
