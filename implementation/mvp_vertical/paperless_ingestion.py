"""Paperless exact-version intake into the existing Document -> Knowledge vertical.

This module deliberately reuses ``store.ingest`` instead of creating a second
chunking/indexing pipeline. Paperless remains the canonical backing resource for
the original bytes; a temporary contained file only adapts the exact version to
the existing Docling/direct-text conversion seam.
"""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any

import psycopg

from . import store
from .contract import TaskContract, assert_source_in_scope
from .documents import DocumentConverter
from .naming import DocumentName
from .paperless import PaperlessClient, PaperlessSourceCapture


BINDING_MIGRATION = Path(__file__).resolve().parent / "sql" / "paperless_source_bindings.sql"


class PaperlessBindingError(RuntimeError):
    """The external Paperless identity cannot be bound safely to a Project Document."""


def ensure_binding_schema(conn: psycopg.Connection) -> None:
    """Create only the external-source binding table in the executable candidate DB."""

    conn.execute(BINDING_MIGRATION.read_text(encoding="utf-8"))
    conn.commit()


def _binding_projection(capture: PaperlessSourceCapture, document_id: str) -> dict[str, Any]:
    return {
        "document_id": document_id,
        "backing_resource": "paperless_ngx",
        "external_document_id": capture.document_id,
        "external_version_id": capture.version_id,
        "storage_reference": capture.storage_reference,
        "original_filename": capture.original_filename,
        "content_hash": capture.content_hash,
    }


def bind_capture(
    conn: psycopg.Connection,
    *,
    document_id: str,
    capture: PaperlessSourceCapture,
) -> dict[str, Any]:
    """Persist the exact backing-resource identity after normal ingestion succeeds."""

    ensure_binding_schema(conn)
    digest = capture.content_hash.removeprefix("sha256:")
    with conn.transaction():
        conn.execute(
            """
            INSERT INTO paperless_source_bindings (
                document_id, backing_resource, paperless_document_id,
                paperless_version_id, storage_reference, original_filename,
                source_digest
            ) VALUES (%s, 'paperless_ngx', %s, %s, %s, %s, %s)
            ON CONFLICT (document_id) DO UPDATE SET
                paperless_document_id = EXCLUDED.paperless_document_id,
                paperless_version_id = EXCLUDED.paperless_version_id,
                storage_reference = EXCLUDED.storage_reference,
                original_filename = EXCLUDED.original_filename,
                source_digest = EXCLUDED.source_digest,
                bound_at = CURRENT_TIMESTAMP
            """,
            (
                document_id,
                capture.document_id,
                capture.version_id,
                capture.storage_reference,
                capture.original_filename,
                digest,
            ),
        )
    conn.commit()
    return _binding_projection(capture, document_id)


def get_binding(conn: psycopg.Connection, document_id: str) -> dict[str, Any]:
    ensure_binding_schema(conn)
    row = conn.execute(
        """
        SELECT document_id, backing_resource, paperless_document_id,
               paperless_version_id, storage_reference, original_filename,
               source_digest, bound_at
          FROM paperless_source_bindings
         WHERE document_id = %s
        """,
        (document_id,),
    ).fetchone()
    if row is None:
        raise KeyError(f"no Paperless source binding for {document_id}")
    return {
        "document_id": row[0],
        "backing_resource": row[1],
        "external_document_id": row[2],
        "external_version_id": row[3],
        "storage_reference": row[4],
        "original_filename": row[5],
        "content_hash": f"sha256:{row[6]}",
        "bound_at": row[7].isoformat() if row[7] is not None else None,
    }


def intake_paperless_document(
    conn: psycopg.Connection,
    contract: TaskContract,
    paperless: PaperlessClient,
    *,
    paperless_document_id: int,
    paperless_version_id: str,
    ingestion_id: str | None = None,
    docling: DocumentConverter | None = None,
    naming: DocumentName | None = None,
) -> dict[str, Any]:
    """Ingest one exact Paperless version through the existing bounded pipeline.

    The Task Contract must explicitly declare the generated Paperless ``source_ref``.
    That keeps source membership checks identical to NAS intake and prevents this
    adapter from broadening project scope merely because Paperless can see more
    documents.
    """

    capture = paperless.capture_document(
        paperless_document_id,
        version_id=paperless_version_id,
    )
    assert_source_in_scope(contract, capture.source_ref)

    with tempfile.TemporaryDirectory(prefix="pantheon-paperless-") as tmp:
        root = Path(tmp)
        contained = root / capture.source_ref
        contained.parent.mkdir(parents=True, exist_ok=True)
        contained.write_bytes(capture.content)
        total_chunks = store.ingest(
            conn,
            contract,
            root,
            ingestion_id=ingestion_id,
            docling=docling,
            source_refs=(capture.source_ref,),
            replace_dossier=False,
            naming_by_source={capture.source_ref: naming} if naming is not None else None,
        )

    card = store.get_document_card(conn, contract.dossier, capture.source_ref)
    expected_digest = capture.content_hash.removeprefix("sha256:")
    if card.get("source_digest") != expected_digest:
        raise PaperlessBindingError(
            "stored Project Document digest does not match the exact Paperless Source Capture"
        )

    binding = bind_capture(conn, document_id=card["document_id"], capture=capture)
    return {
        "chunks_ingested": total_chunks,
        "document": card,
        "source_capture": _binding_projection(capture, card["document_id"]),
        "binding": binding,
        "authority": {
            "source": True,
            "knowledge": False,
            "evidence": False,
            "professional_validation": False,
        },
    }
