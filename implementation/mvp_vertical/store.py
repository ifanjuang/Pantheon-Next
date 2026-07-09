"""pgvector store: bounded ingestion and scope-first retrieval.

The two rules that matter live here:

1. Ingestion reads ONLY the contract's declared sources — anything else
   raises before touching the database.
2. Retrieval filters on the declared perimeter in SQL *before* vector
   ranking. A query cannot see outside the contract by construction.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import psycopg

from .contract import TaskContract, assert_source_in_scope
from .embedder import DIM, embed, to_pgvector

DDL = f"""
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS chunks (
    id        BIGSERIAL PRIMARY KEY,
    dossier   TEXT NOT NULL,
    source_ref TEXT NOT NULL,
    chunk_no  INT  NOT NULL,
    body      TEXT NOT NULL,
    embedding vector({DIM}) NOT NULL,
    UNIQUE (dossier, source_ref, chunk_no)
);
"""


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

    @property
    def retrieval_trace(self) -> str:
        return f"pgvector://chunks/{self.source_ref}#chunk-{self.chunk_no}"


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


def ingest(conn: psycopg.Connection, contract: TaskContract, root: Path) -> int:
    """Ingest the contract's declared sources — and nothing else."""
    total = 0
    with conn.cursor() as cur:
        cur.execute("DELETE FROM chunks WHERE dossier = %s", (contract.dossier,))
        for source_ref in contract.sources:
            assert_source_in_scope(contract, source_ref)  # tautological by loop, kept as guard
            path = root / source_ref
            text = path.read_text(encoding="utf-8")
            for i, body in enumerate(chunk_text(text)):
                cur.execute(
                    "INSERT INTO chunks (dossier, source_ref, chunk_no, body, embedding)"
                    " VALUES (%s, %s, %s, %s, %s::vector)",
                    (contract.dossier, source_ref, i, body, to_pgvector(embed(body))),
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
            "SELECT source_ref, chunk_no, body, embedding <=> %s::vector AS distance"
            " FROM chunks"
            " WHERE dossier = %s AND source_ref = ANY(%s)"   # the boundary
            " ORDER BY distance ASC"
            " LIMIT %s",
            (qvec, contract.dossier, list(contract.sources), top_k),
        )
        return [RetrievedChunk(*row) for row in cur.fetchall()]
