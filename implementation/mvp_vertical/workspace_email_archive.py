"""Gmail/Workspace e-mail archive projection into admitted KROQI roots.

The exact RFC822 bytes are retained by storage_retention. AFFAIRES receives a
sanitized HTML derivative plus decoded attachments. This module keeps folder
routing technical: directory != governed Project identity.
"""

from __future__ import annotations

import base64
import hashlib
import html
import mimetypes
import os
import re
import tempfile
import unicodedata
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from email import policy
from email.message import Message
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import psycopg
from psycopg.rows import dict_row

from . import source_intake, storage_retention


MIGRATION = Path(__file__).resolve().parent / "sql" / "036_workspace_email_archive.sql"
MAX_RAW_BYTES = 50 * 1024 * 1024
MAX_MIME_PARTS = 500
MAX_ATTACHMENTS = 200
MAX_ATTACHMENT_BYTES = 50 * 1024 * 1024
DEFAULT_DESTINATION_SUBDIR = "Echanges"
WINDOWS_RESERVED = {
    "con", "prn", "aux", "nul",
    *(f"com{i}" for i in range(1, 10)),
    *(f"lpt{i}" for i in range(1, 10)),
}


class WorkspaceEmailArchiveError(RuntimeError):
    pass


class DestinationRequired(WorkspaceEmailArchiveError):
    pass


class DestinationCollision(WorkspaceEmailArchiveError):
    pass


class ArchivedDestinationConfirmationRequired(WorkspaceEmailArchiveError):
    pass


class DestinationChangeConfirmationRequired(WorkspaceEmailArchiveError):
    pass


class RawChecksumMismatch(WorkspaceEmailArchiveError):
    pass


class MimeNormalizationError(WorkspaceEmailArchiveError):
    pass


@dataclass(frozen=True)
class AffaireLocation:
    name: str
    state: str
    root: Path

    @property
    def project_dir(self) -> Path:
        return self.root / self.name


class _HTMLText(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        lowered = tag.casefold()
        if lowered in {"script", "style", "iframe", "object", "embed", "svg"}:
            self._skip += 1
            return
        if not self._skip and lowered in {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        lowered = tag.casefold()
        if lowered in {"script", "style", "iframe", "object", "embed", "svg"}:
            self._skip = max(0, self._skip - 1)
            return
        if not self._skip and lowered in {"p", "div", "li", "tr"}:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._skip:
            self._parts.append(data)

    def text(self) -> str:
        value = "".join(self._parts)
        lines = [" ".join(line.split()) for line in value.splitlines()]
        return "\n".join(line for line in lines if line).strip()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _required(value: Any, field: str, *, max_length: int = 500) -> str:
    text = str(value or "").strip()
    if not text:
        raise WorkspaceEmailArchiveError(f"{field} is required")
    if len(text) > max_length:
        raise WorkspaceEmailArchiveError(f"{field} exceeds {max_length} characters")
    return text


def _safe_component(value: str, *, fallback: str, max_length: int = 120) -> str:
    value = unicodedata.normalize("NFKC", str(value or ""))
    value = "".join(ch for ch in value if ord(ch) >= 32 and ch not in '<>:"/\\|?*')
    value = re.sub(r"\s+", " ", value).strip(" .")
    if not value:
        value = fallback
    stem = Path(value).stem.casefold()
    if stem in WINDOWS_RESERVED:
        value = "_" + value
    return value[:max_length].rstrip(" .") or fallback


def _safe_subdir(value: str) -> str:
    raw = str(value or "").strip().replace("\\", "/")
    if raw in {"", "."}:
        return ""
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts:
        raise WorkspaceEmailArchiveError("destination_subdir must stay below the AFFAIRE directory")
    parts = [_safe_component(part, fallback="Echanges", max_length=80) for part in path.parts]
    return "/".join(parts)


def _case_key(value: str) -> str:
    return unicodedata.normalize("NFKC", value).casefold()


def _direct_directories(root: Path) -> list[str]:
    if not root.exists():
        return []
    if not root.is_dir():
        raise WorkspaceEmailArchiveError(f"configured workspace root is not a directory: {root}")
    return sorted(
        [item.name for item in root.iterdir() if item.is_dir()],
        key=lambda value: (_case_key(value), value),
    )


def affaires_catalogue(
    *,
    active_root: str | Path,
    archive_project_root: str | Path | None = None,
) -> list[dict[str, str]]:
    active = Path(active_root).expanduser().resolve()
    archive = (
        Path(archive_project_root).expanduser().resolve()
        if archive_project_root is not None
        else None
    )
    rows: list[dict[str, str]] = []
    by_key: dict[str, list[dict[str, str]]] = {}
    for state, root in (("active", active), ("archived", archive)):
        if root is None:
            continue
        for name in _direct_directories(root):
            row = {"name": name, "state": state, "root_kind": "AFFAIRES" if state == "active" else "ARCHIVES/PROJET"}
            rows.append(row)
            by_key.setdefault(_case_key(name), []).append(row)
    collisions = {key for key, values in by_key.items() if len(values) > 1}
    for row in rows:
        row["routing_status"] = "collision" if _case_key(row["name"]) in collisions else "available"
    rows.sort(key=lambda row: (_case_key(row["name"]), row["state"]))
    return rows


def resolve_affaire(
    name: str,
    *,
    active_root: str | Path,
    archive_project_root: str | Path | None = None,
) -> AffaireLocation:
    wanted = _required(name, "affaire_name", max_length=255)
    catalog = affaires_catalogue(
        active_root=active_root,
        archive_project_root=archive_project_root,
    )
    matches = [row for row in catalog if row["name"] == wanted]
    if not matches:
        raise DestinationRequired(f"unknown AFFAIRES destination: {wanted}")
    if len(matches) != 1 or matches[0]["routing_status"] != "available":
        raise DestinationCollision(
            f"AFFAIRE {wanted!r} exists in more than one admitted root"
        )
    row = matches[0]
    root = (
        Path(active_root).expanduser().resolve()
        if row["state"] == "active"
        else Path(archive_project_root).expanduser().resolve()
    )
    project_dir = (root / wanted).resolve(strict=True)
    if not project_dir.is_relative_to(root) or not project_dir.is_dir():
        raise DestinationRequired("AFFAIRE destination is not a current directory")
    return AffaireLocation(name=wanted, state=row["state"], root=root)


def _decode_part_text(part: Message) -> str:
    try:
        content = part.get_content()
    except Exception:
        payload = part.get_payload(decode=True)
        if not isinstance(payload, (bytes, bytearray)):
            return ""
        charset = part.get_content_charset() or "utf-8"
        return bytes(payload).decode(charset, errors="replace")
    if isinstance(content, str):
        return content
    return ""


def _strip_html(value: str) -> str:
    parser = _HTMLText()
    try:
        parser.feed(value)
        parser.close()
    except Exception as exc:
        raise MimeNormalizationError("HTML body could not be normalized safely") from exc
    return parser.text()


def _message_date(value: str) -> str | None:
    if not value:
        return None
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError, OverflowError):
        return None
    if parsed is None:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def parse_rfc822(raw: bytes) -> dict[str, Any]:
    if not isinstance(raw, (bytes, bytearray)):
        raise MimeNormalizationError("RAW RFC822 input must be bytes")
    data = bytes(raw)
    if not data or len(data) > MAX_RAW_BYTES:
        raise MimeNormalizationError(
            f"RAW RFC822 must contain between 1 and {MAX_RAW_BYTES} bytes"
        )
    try:
        message = BytesParser(policy=policy.default).parsebytes(data)
    except Exception as exc:
        raise MimeNormalizationError("RAW RFC822 could not be parsed") from exc

    parts = list(message.walk())
    if len(parts) > MAX_MIME_PARTS:
        raise MimeNormalizationError(f"MIME message exceeds {MAX_MIME_PARTS} parts")

    plain_candidates: list[str] = []
    html_candidates: list[str] = []
    attachments: list[dict[str, Any]] = []
    total_attachment_bytes = 0

    for index, part in enumerate(parts):
        if part.is_multipart():
            continue
        content_type = part.get_content_type().casefold()
        disposition = (part.get_content_disposition() or "").casefold()
        filename = part.get_filename()
        content_id = str(part.get("Content-ID") or "").strip().strip("<>")

        is_attachment = disposition == "attachment" or bool(filename)
        if not is_attachment and content_type == "text/plain":
            text = _decode_part_text(part).strip()
            if text:
                plain_candidates.append(text)
            continue
        if not is_attachment and content_type == "text/html":
            text = _decode_part_text(part).strip()
            if text:
                html_candidates.append(text)
            continue

        if not is_attachment and disposition != "inline":
            continue
        payload = part.get_payload(decode=True)
        if not isinstance(payload, (bytes, bytearray)):
            continue
        payload_bytes = bytes(payload)
        if len(payload_bytes) > MAX_ATTACHMENT_BYTES:
            raise MimeNormalizationError(
                f"MIME part {index} exceeds {MAX_ATTACHMENT_BYTES} bytes"
            )
        total_attachment_bytes += len(payload_bytes)
        if total_attachment_bytes > MAX_RAW_BYTES:
            raise MimeNormalizationError("decoded attachment total exceeds archive bound")
        if len(attachments) >= MAX_ATTACHMENTS:
            raise MimeNormalizationError(
                f"MIME message exceeds {MAX_ATTACHMENTS} attachments"
            )
        guessed_ext = mimetypes.guess_extension(content_type) or ""
        original_filename = str(filename or f"attachment-{index}{guessed_ext}")
        attachments.append(
            {
                "mime_part_index": index,
                "original_filename": original_filename,
                "media_type": content_type,
                "content_id": content_id or None,
                "disposition": disposition or None,
                "byte_size": len(payload_bytes),
                "content_sha256": _sha256(payload_bytes),
                "bytes": payload_bytes,
            }
        )

    if plain_candidates:
        body_text = "\n\n".join(plain_candidates).strip()
        body_basis = "text/plain"
    elif html_candidates:
        body_text = "\n\n".join(_strip_html(item) for item in html_candidates).strip()
        body_basis = "text/html->text"
    else:
        body_text = ""
        body_basis = "none"

    headers = {
        key: str(message.get(key) or "").strip()
        for key in ("From", "To", "Cc", "Date", "Subject", "Message-ID")
    }
    return {
        "headers": headers,
        "source_date": _message_date(headers["Date"]),
        "body_text": body_text,
        "body_basis": body_basis,
        "attachments": attachments,
    }


def normalized_ask_context(
    parsed: dict[str, Any],
    *,
    provider_account_ref: str,
    gmail_message_id: str,
    gmail_thread_id: str,
    raw_sha256: str,
) -> bytes:
    payload = {
        "kind": "gmail_normalized_context/v1",
        "provider_account_ref": provider_account_ref,
        "gmail_message_id": gmail_message_id,
        "gmail_thread_id": gmail_thread_id,
        "server_verified_raw_sha256": raw_sha256,
        "headers": dict(parsed["headers"]),
        "body_text": parsed["body_text"],
        "body_basis": parsed["body_basis"],
        "attachments": [
            {
                key: attachment.get(key)
                for key in (
                    "mime_part_index",
                    "original_filename",
                    "media_type",
                    "content_id",
                    "disposition",
                    "byte_size",
                    "content_sha256",
                )
            }
            for attachment in parsed["attachments"]
        ],
    }
    import json
    return json.dumps(
        payload,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    tmp = Path(name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        try:
            tmp.unlink()
        except FileNotFoundError:
            pass


def _file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _relative_to_root(path: Path, root: Path) -> str:
    resolved = path.resolve(strict=False)
    root_resolved = root.resolve()
    if not resolved.is_relative_to(root_resolved):
        raise WorkspaceEmailArchiveError("visible archive path escaped admitted root")
    return resolved.relative_to(root_resolved).as_posix()


def _bundle_row(
    conn: psycopg.Connection,
    *,
    provider_account_ref: str,
    gmail_thread_id: str,
) -> dict[str, Any] | None:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT * FROM workspace_email_bundles
             WHERE provider_account_ref = %s AND gmail_thread_id = %s
            """,
            (provider_account_ref, gmail_thread_id),
        )
        row = cur.fetchone()
    return dict(row) if row is not None else None


def archive_state(
    conn: psycopg.Connection,
    *,
    provider_account_ref: str,
    gmail_thread_id: str,
    current_gmail_message_id: str,
    current_raw_sha256: str,
) -> dict[str, Any]:
    row = _bundle_row(
        conn,
        provider_account_ref=provider_account_ref,
        gmail_thread_id=gmail_thread_id,
    )
    if row is None:
        state = "absent"
    elif (
        row["current_gmail_message_id"] == current_gmail_message_id
        and row["current_raw_sha256"] == current_raw_sha256.lower()
    ):
        state = "current"
    else:
        state = "update_available"
    return {
        "archive_state": state,
        "archived_document_id": row["bundle_id"] if row else None,
        "archived_gmail_message_id": row["current_gmail_message_id"] if row else None,
        "archived_source_sha256": row["current_raw_sha256"] if row else None,
        "affaire_name": row["affaire_name"] if row else None,
        "affaire_state": row["affaire_state"] if row else None,
        "html_relative_path": row["html_relative_path"] if row else None,
    }


def _source_id(provider_account_ref: str, gmail_message_id: str) -> str:
    digest = hashlib.sha256(
        f"{provider_account_ref}\0{gmail_message_id}".encode("utf-8")
    ).hexdigest()[:32]
    return f"source-gmail-{digest}"


def _ensure_source(
    conn: psycopg.Connection,
    *,
    provider_account_ref: str,
    gmail_message_id: str,
    gmail_thread_id: str,
    raw_sha256: str,
    raw_storage_object_id: str,
    parsed: dict[str, Any],
    actor: str,
    idempotency_key: str,
) -> dict[str, Any]:
    source_id = _source_id(provider_account_ref, gmail_message_id)
    try:
        existing = source_intake.get_source(conn, source_id)
    except source_intake.SourceNotFound:
        return source_intake.create_source(
            conn,
            source_id=source_id,
            source_kind="email",
            origin_system="gmail",
            origin_external_ref=f"{provider_account_ref}:{gmail_message_id}",
            raw_source_ref=f"storage-object://{raw_storage_object_id}",
            received_at=datetime.now(timezone.utc),
            actor=actor,
            actor_kind="human",
            idempotency_key=f"{idempotency_key}:source",
            source_date=parsed.get("source_date"),
            mime_type="message/rfc822",
            checksum=raw_sha256,
            metadata={
                "provider_account_ref": provider_account_ref,
                "gmail_message_id": gmail_message_id,
                "gmail_thread_id": gmail_thread_id,
                "rfc_message_id": parsed["headers"].get("Message-ID") or None,
            },
        )
    if str(existing.get("checksum") or "").lower() != raw_sha256:
        raise RawChecksumMismatch(
            "existing Gmail Source identity has different exact RAW bytes"
        )
    return existing


def _destination_key(location: AffaireLocation, subdir: str) -> str:
    return f"{location.state}:{location.name}:{subdir}"


def _attachment_path(
    conn: psycopg.Connection,
    *,
    attachment: dict[str, Any],
    destination_dir: Path,
    destination_key: str,
    root: Path,
) -> tuple[Path, bool]:
    digest = attachment["content_sha256"]
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT visible_relative_path, byte_size
              FROM workspace_email_visible_attachments
             WHERE destination_key = %s AND content_sha256 = %s
            """,
            (destination_key, digest),
        )
        row = cur.fetchone()
    if row is not None:
        candidate = (root / row["visible_relative_path"]).resolve(strict=False)
        if not candidate.is_relative_to(root.resolve()):
            raise WorkspaceEmailArchiveError("indexed attachment escaped admitted root")
        if candidate.is_file():
            if candidate.stat().st_size != int(row["byte_size"]) or _file_digest(candidate) != digest:
                raise WorkspaceEmailArchiveError(
                    "indexed visible attachment no longer matches its verified digest"
                )
            return candidate, True

    original = _safe_component(
        attachment["original_filename"],
        fallback=f"attachment-{attachment['mime_part_index']}",
        max_length=180,
    )
    candidate = destination_dir / original
    if candidate.exists():
        if candidate.is_file() and _file_digest(candidate) == digest:
            return candidate, True
        stem = Path(original).stem[:140]
        suffix = Path(original).suffix[:20]
        candidate = destination_dir / f"{stem}--{digest[:8]}{suffix}"
        if candidate.exists():
            if not candidate.is_file() or _file_digest(candidate) != digest:
                raise WorkspaceEmailArchiveError(
                    "collision-safe attachment path is occupied by different bytes"
                )
            return candidate, True
    _atomic_write(candidate, attachment["bytes"])
    if _file_digest(candidate) != digest:
        raise WorkspaceEmailArchiveError("published attachment failed SHA-256 verification")
    return candidate, False


def _render_html(
    parsed: dict[str, Any],
    *,
    document_id: str,
    provider_account_ref: str,
    gmail_message_id: str,
    gmail_thread_id: str,
    raw_sha256: str,
    attachment_manifest: list[dict[str, Any]],
) -> bytes:
    headers = parsed["headers"]
    rows = []
    for label, key in (("De", "From"), ("À", "To"), ("Cc", "Cc"), ("Date", "Date"), ("Objet", "Subject")):
        value = headers.get(key) or ""
        if value:
            rows.append(
                f"<tr><th>{html.escape(label)}</th><td>{html.escape(value)}</td></tr>"
            )
    attachments_html = ""
    if attachment_manifest:
        items = []
        for item in attachment_manifest:
            href = html.escape(Path(item["visible_relative_path"]).name, quote=True)
            label = html.escape(item["original_filename"])
            items.append(
                f'<li><a href="{href}">{label}</a> '
                f'<small>SHA-256 {html.escape(item["content_sha256"])}</small></li>'
            )
        attachments_html = "<h2>Pièces jointes</h2><ul>" + "".join(items) + "</ul>"

    metadata = (
        f'<meta name="pantheon-document-id" content="{html.escape(document_id, quote=True)}">'
        f'<meta name="pantheon-provider-account-ref" content="{html.escape(provider_account_ref, quote=True)}">'
        f'<meta name="pantheon-gmail-message-id" content="{html.escape(gmail_message_id, quote=True)}">'
        f'<meta name="pantheon-gmail-thread-id" content="{html.escape(gmail_thread_id, quote=True)}">'
        f'<meta name="pantheon-raw-sha256" content="{raw_sha256}">'
    )
    title = html.escape(headers.get("Subject") or "(sans objet)")
    body = html.escape(parsed.get("body_text") or "")
    return (
        "<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\">"
        + metadata
        + f"<title>{title}</title></head><body>"
        + f"<h1>{title}</h1><table>{''.join(rows)}</table>"
        + f"<pre>{body}</pre>{attachments_html}"
        + "<hr><p><small>Projection HTML dérivée. Le RAW RFC822 exact est retenu séparément par Pantheon.</small></p>"
        + "</body></html>"
    ).encode("utf-8")


def _html_filename(parsed: dict[str, Any], gmail_thread_id: str) -> str:
    subject = _safe_component(
        parsed["headers"].get("Subject") or "Sans objet",
        fallback="Sans objet",
        max_length=110,
    )
    sender = _safe_component(
        parsed["headers"].get("From") or "Mail",
        fallback="Mail",
        max_length=60,
    )
    date_prefix = (parsed.get("source_date") or datetime.now(timezone.utc).date().isoformat())[:10]
    thread_suffix = hashlib.sha256(gmail_thread_id.encode("utf-8")).hexdigest()[:8]
    return f"{date_prefix} - {sender} - {subject}--{thread_suffix}.html"


def archive_email(
    conn: psycopg.Connection,
    *,
    raw_rfc822: bytes,
    provider_account_ref: str,
    gmail_message_id: str,
    gmail_thread_id: str,
    affaire_name: str,
    active_root: str | Path,
    archive_project_root: str | Path | None,
    raw_retention_root: str | Path,
    raw_storage_provider_ref: str,
    actor: str,
    idempotency_key: str,
    client_raw_sha256: str | None = None,
    destination_subdir: str = DEFAULT_DESTINATION_SUBDIR,
    confirm_archived_write: bool = False,
    confirm_destination_change: bool = False,
) -> dict[str, Any]:
    provider_account_ref = _required(provider_account_ref, "provider_account_ref")
    gmail_message_id = _required(gmail_message_id, "gmail_message_id")
    gmail_thread_id = _required(gmail_thread_id, "gmail_thread_id")
    actor = _required(actor, "actor")
    idempotency_key = _required(idempotency_key, "idempotency_key")
    location = resolve_affaire(
        affaire_name,
        active_root=active_root,
        archive_project_root=archive_project_root,
    )
    if location.state == "archived" and not confirm_archived_write:
        raise ArchivedDestinationConfirmationRequired(
            f"AFFAIRE {location.name!r} is archived; explicit confirmation is required"
        )
    subdir = _safe_subdir(destination_subdir)

    existing_bundle = _bundle_row(
        conn,
        provider_account_ref=provider_account_ref,
        gmail_thread_id=gmail_thread_id,
    )
    if existing_bundle is not None:
        changed = (
            existing_bundle["affaire_name"] != location.name
            or existing_bundle["affaire_state"] != location.state
            or existing_bundle["destination_subdir"] != subdir
        )
        if changed and not confirm_destination_change:
            raise DestinationChangeConfirmationRequired(
                "existing Gmail thread projection targets another AFFAIRE/destination"
            )

    raw = bytes(raw_rfc822)
    if not raw or len(raw) > MAX_RAW_BYTES:
        raise MimeNormalizationError(
            f"RAW RFC822 must contain between 1 and {MAX_RAW_BYTES} bytes"
        )
    raw_sha256 = _sha256(raw)
    if client_raw_sha256 is not None:
        asserted = str(client_raw_sha256).strip().lower()
        if asserted != raw_sha256:
            raise RawChecksumMismatch(
                f"client RAW SHA-256 mismatch: expected {asserted}, server found {raw_sha256}"
            )
    parsed = parse_rfc822(raw)

    retained = storage_retention.retain_bytes(
        conn,
        data=raw,
        media_type="message/rfc822",
        retention_root=Path(raw_retention_root),
        storage_provider_ref=raw_storage_provider_ref,
        expected_sha256=raw_sha256,
    )
    raw_storage_object_id = retained["storage_object"]["storage_object_id"]
    source = _ensure_source(
        conn,
        provider_account_ref=provider_account_ref,
        gmail_message_id=gmail_message_id,
        gmail_thread_id=gmail_thread_id,
        raw_sha256=raw_sha256,
        raw_storage_object_id=raw_storage_object_id,
        parsed=parsed,
        actor=actor,
        idempotency_key=idempotency_key,
    )

    project_dir = location.project_dir.resolve(strict=True)
    destination_dir = (project_dir / subdir).resolve(strict=False) if subdir else project_dir
    if not destination_dir.is_relative_to(project_dir):
        raise WorkspaceEmailArchiveError("destination escaped AFFAIRE directory")
    destination_dir.mkdir(parents=True, exist_ok=True)

    if existing_bundle is not None and not (
        existing_bundle["affaire_name"] != location.name
        or existing_bundle["affaire_state"] != location.state
        or existing_bundle["destination_subdir"] != subdir
    ):
        html_path = (location.root / existing_bundle["html_relative_path"]).resolve(strict=False)
        if not html_path.is_relative_to(location.root):
            raise WorkspaceEmailArchiveError("stored HTML path escaped admitted root")
    else:
        html_path = destination_dir / _html_filename(parsed, gmail_thread_id)

    destination_key = _destination_key(location, subdir)
    attachment_manifest: list[dict[str, Any]] = []
    added = reused = 0
    for attachment in parsed["attachments"]:
        visible_path, was_reused = _attachment_path(
            conn,
            attachment=attachment,
            destination_dir=destination_dir,
            destination_key=destination_key,
            root=location.root,
        )
        relative = _relative_to_root(visible_path, location.root)
        attachment_manifest.append(
            {
                "mime_part_index": attachment["mime_part_index"],
                "original_filename": attachment["original_filename"],
                "media_type": attachment["media_type"],
                "byte_size": attachment["byte_size"],
                "content_sha256": attachment["content_sha256"],
                "visible_relative_path": relative,
                "reused": was_reused,
            }
        )
        if was_reused:
            reused += 1
        else:
            added += 1

    bundle_id = (
        existing_bundle["bundle_id"]
        if existing_bundle is not None
        else f"email-bundle-{uuid.uuid4().hex}"
    )
    html_bytes = _render_html(
        parsed,
        document_id=bundle_id,
        provider_account_ref=provider_account_ref,
        gmail_message_id=gmail_message_id,
        gmail_thread_id=gmail_thread_id,
        raw_sha256=raw_sha256,
        attachment_manifest=attachment_manifest,
    )
    _atomic_write(html_path, html_bytes)
    html_relative = _relative_to_root(html_path, location.root)

    previous_html: Path | None = None
    if existing_bundle is not None:
        old_root = (
            Path(active_root).expanduser().resolve()
            if existing_bundle["affaire_state"] == "active"
            else (
                Path(archive_project_root).expanduser().resolve()
                if archive_project_root is not None
                else None
            )
        )
        if old_root is not None:
            candidate = (old_root / existing_bundle["html_relative_path"]).resolve(strict=False)
            if candidate.is_relative_to(old_root) and candidate != html_path:
                previous_html = candidate

    with conn.transaction():
        for item in attachment_manifest:
            conn.execute(
                """
                INSERT INTO workspace_email_visible_attachments (
                    destination_key, content_sha256, byte_size, media_type,
                    visible_relative_path
                ) VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (destination_key, content_sha256) DO UPDATE SET
                    visible_relative_path = EXCLUDED.visible_relative_path,
                    byte_size = EXCLUDED.byte_size,
                    media_type = EXCLUDED.media_type
                """,
                (
                    destination_key,
                    item["content_sha256"],
                    item["byte_size"],
                    item["media_type"],
                    item["visible_relative_path"],
                ),
            )
            conn.execute(
                """
                INSERT INTO workspace_email_attachment_occurrences (
                    provider_account_ref, gmail_message_id, mime_part_index,
                    original_filename, content_sha256, byte_size, media_type,
                    visible_relative_path
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (provider_account_ref, gmail_message_id, mime_part_index)
                DO UPDATE SET
                    original_filename = EXCLUDED.original_filename,
                    content_sha256 = EXCLUDED.content_sha256,
                    byte_size = EXCLUDED.byte_size,
                    media_type = EXCLUDED.media_type,
                    visible_relative_path = EXCLUDED.visible_relative_path
                """,
                (
                    provider_account_ref,
                    gmail_message_id,
                    item["mime_part_index"],
                    item["original_filename"],
                    item["content_sha256"],
                    item["byte_size"],
                    item["media_type"],
                    item["visible_relative_path"],
                ),
            )

        conn.execute(
            """
            INSERT INTO workspace_email_bundles (
                bundle_id, provider_account_ref, gmail_thread_id,
                current_gmail_message_id, current_raw_sha256, source_id,
                affaire_name, affaire_state, destination_subdir,
                html_relative_path
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (provider_account_ref, gmail_thread_id) DO UPDATE SET
                current_gmail_message_id = EXCLUDED.current_gmail_message_id,
                current_raw_sha256 = EXCLUDED.current_raw_sha256,
                source_id = EXCLUDED.source_id,
                affaire_name = EXCLUDED.affaire_name,
                affaire_state = EXCLUDED.affaire_state,
                destination_subdir = EXCLUDED.destination_subdir,
                html_relative_path = EXCLUDED.html_relative_path,
                updated_at = clock_timestamp()
            """,
            (
                bundle_id,
                provider_account_ref,
                gmail_thread_id,
                gmail_message_id,
                raw_sha256,
                source["source_id"],
                location.name,
                location.state,
                subdir,
                html_relative,
            ),
        )

    if previous_html is not None:
        try:
            previous_html.unlink()
        except FileNotFoundError:
            pass

    return {
        "status": "archived" if existing_bundle is None else "updated",
        "bundle_id": bundle_id,
        "source_id": source["source_id"],
        "raw_storage_object_id": raw_storage_object_id,
        "server_verified_raw_sha256": raw_sha256,
        "affaire": {
            "name": location.name,
            "state": location.state,
            "root_kind": "AFFAIRES" if location.state == "active" else "ARCHIVES/PROJET",
        },
        "html_relative_path": html_relative,
        "attachments_added": added,
        "attachments_reused": reused,
        "attachment_occurrences": attachment_manifest,
        "authority": {
            "archive_persisted": True,
            "is_evidence": False,
            "is_project_identity": False,
            "is_professional_truth": False,
            "hindsight_written_directly": False,
        },
    }


def decode_base64url_raw(value: str) -> bytes:
    encoded = _required(value, "raw_rfc822_base64url", max_length=80_000_000)
    padding = "=" * (-len(encoded) % 4)
    try:
        return base64.urlsafe_b64decode(encoded + padding)
    except Exception as exc:
        raise MimeNormalizationError("raw_rfc822_base64url is invalid") from exc


def ensure_schema(conn: psycopg.Connection) -> None:
    source_intake.initialize(conn)
    storage_retention.ensure_schema(conn)
    conn.execute(MIGRATION.read_text(encoding="utf-8"))
    conn.commit()
