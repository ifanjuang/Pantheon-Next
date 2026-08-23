"""Bounded Paperless-ngx adapter for the external Pantheon MVP runtime.

Paperless is treated as a document source-management runtime and backing store.
This module does not turn Paperless metadata, OCR, search scores or task success
into Pantheon truth, Evidence, Knowledge or approval.

Read operations may be used directly by a reviewed cockpit/Hermes binding.
External writes are exposed only through explicit helpers that route the effect
through ``policy_gate.governed_effect``.
"""

from __future__ import annotations

import hashlib
import json
import mimetypes
import re
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator
from urllib.parse import quote, unquote, urlparse

from .policy_gate import PolicyClient, governed_effect


class PaperlessError(RuntimeError):
    """Paperless could not satisfy the bounded adapter request."""


class PaperlessConfigurationError(PaperlessError):
    """The adapter configuration is unsafe or incomplete."""


class PaperlessMutationError(PaperlessError):
    """A requested mutation exceeds the adapter's allowlisted surface."""


_ALLOWED_METADATA_FIELDS = frozenset(
    {
        "title",
        "correspondent",
        "document_type",
        "storage_path",
        "tags",
        "archive_serial_number",
        "custom_fields",
    }
)

_CONTENT_DISPOSITION_FILENAME = re.compile(r'filename="?([^";]+)"?', re.I)
_CONTENT_DISPOSITION_FILENAME_STAR = re.compile(r"filename\*=UTF-8''([^;]+)", re.I)
_SAFE_FILENAME = re.compile(r"[^A-Za-z0-9._-]+")


@dataclass(frozen=True)
class PaperlessBinary:
    document_id: int
    version_id: str
    filename: str
    media_type: str
    content: bytes
    sha256: str


@dataclass(frozen=True)
class PaperlessSourceCapture:
    """Exact external source identity suitable for a governed Source Capture."""

    document_id: int
    version_id: str
    original_filename: str
    media_type: str
    byte_size: int
    content_hash: str
    storage_reference: str
    source_ref: str
    content: bytes

    @contextmanager
    def materialized(self) -> Iterator[Path]:
        """Materialize exact bytes temporarily for Docling/OCR, then remove them."""

        suffix = Path(self.original_filename).suffix
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as handle:
            handle.write(self.content)
            temp_path = Path(handle.name)
        try:
            yield temp_path
        finally:
            temp_path.unlink(missing_ok=True)


def paperless_source_ref(document_id: int, version_id: str, filename: str) -> str:
    """Return a Task-Contract-safe relative locator for one exact version."""

    if document_id <= 0:
        raise ValueError("Paperless document_id must be positive")
    version = str(version_id).strip()
    if not version:
        raise ValueError("an exact Paperless version_id is required")
    basename = Path(filename.replace("\\", "/")).name.strip() or f"document-{document_id}"
    safe_name = _SAFE_FILENAME.sub("-", basename).strip("-") or f"document-{document_id}"
    return f"paperless/{document_id}/versions/{quote(version, safe='-_.')}/{safe_name}"


def _filename_from_headers(headers: Any, fallback: str) -> str:
    disposition = str(headers.get("content-disposition", ""))
    star = _CONTENT_DISPOSITION_FILENAME_STAR.search(disposition)
    if star:
        return Path(unquote(star.group(1))).name or fallback
    normal = _CONTENT_DISPOSITION_FILENAME.search(disposition)
    if normal:
        return Path(normal.group(1)).name or fallback
    return fallback


class PaperlessClient:
    """Small API client for one reviewed Paperless-ngx instance.

    The Paperless token is an external runtime secret. It is used only in the
    Authorization header and is never returned by this adapter.
    """

    def __init__(
        self,
        base_url: str,
        token: str,
        *,
        timeout: float = 30.0,
        client: Any | None = None,
    ) -> None:
        parsed = urlparse(base_url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise PaperlessConfigurationError("Paperless base_url must use http:// or https://")
        if not token.strip():
            raise PaperlessConfigurationError("Paperless API token is required")
        self.base_url = base_url.rstrip("/")
        self._token = token
        self.timeout = timeout
        self._client = client

    @classmethod
    def from_env(cls) -> "PaperlessClient":
        import os

        return cls(
            os.environ.get("PAPERLESS_API_URL", "http://paperless:8000"),
            os.environ.get("PAPERLESS_API_TOKEN", ""),
            timeout=float(os.environ.get("PAPERLESS_API_TIMEOUT", "30")),
        )

    def _request(self, method: str, path: str, **kwargs: Any):
        client = self._client
        owns_client = client is None
        if owns_client:
            import httpx  # lazy: cockpit/runtime extra owns the HTTP dependency

            client = httpx.Client(timeout=self.timeout, follow_redirects=False)
        headers = dict(kwargs.pop("headers", {}) or {})
        headers["Authorization"] = f"Token {self._token}"
        headers.setdefault("Accept", "application/json")
        try:
            response = client.request(
                method,
                f"{self.base_url}{path}",
                headers=headers,
                timeout=self.timeout,
                follow_redirects=False,
                **kwargs,
            )
            response.raise_for_status()
            return response
        except Exception as exc:
            raise PaperlessError(f"Paperless request failed: {method} {path}: {exc}") from exc
        finally:
            if owns_client:
                client.close()

    def probe(self) -> dict[str, Any]:
        """Bounded reachability probe; success is not a safety verdict."""

        payload = self._request("GET", "/api/documents/", params={"page_size": 1}).json()
        return {
            "reachable": True,
            "document_count": payload.get("count"),
            "authority_effect": "none",
        }

    def list_documents(
        self,
        *,
        query: str | None = None,
        page: int = 1,
        page_size: int = 50,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {"page": page, "page_size": page_size}
        if query:
            params["query"] = query
        return self._request("GET", "/api/documents/", params=params).json()

    def get_document(self, document_id: int, *, version_id: str | None = None) -> dict[str, Any]:
        params = {"version": version_id} if version_id is not None else None
        return self._request("GET", f"/api/documents/{document_id}/", params=params).json()

    def get_metadata(self, document_id: int, *, version_id: str | None = None) -> dict[str, Any]:
        params = {"version": version_id} if version_id is not None else None
        return self._request(
            "GET", f"/api/documents/{document_id}/metadata/", params=params
        ).json()

    def download_document(
        self,
        document_id: int,
        *,
        version_id: str,
        preview: bool = False,
    ) -> PaperlessBinary:
        """Download one exact version; mutable latest is not enough for capture."""

        version = str(version_id).strip()
        if not version:
            raise PaperlessConfigurationError("exact version_id is required for source capture")
        suffix = "preview" if preview else "download"
        response = self._request(
            "GET",
            f"/api/documents/{document_id}/{suffix}/",
            params={"version": version},
            headers={"Accept": "*/*"},
        )
        media_type = response.headers.get("content-type", "application/octet-stream").split(";", 1)[0]
        guessed_extension = mimetypes.guess_extension(media_type) or ""
        fallback = f"paperless-{document_id}{guessed_extension}"
        filename = _filename_from_headers(response.headers, fallback)
        content = bytes(response.content)
        return PaperlessBinary(
            document_id=document_id,
            version_id=version,
            filename=filename,
            media_type=media_type,
            content=content,
            sha256=hashlib.sha256(content).hexdigest(),
        )

    def capture_document(self, document_id: int, *, version_id: str) -> PaperlessSourceCapture:
        binary = self.download_document(document_id, version_id=version_id)
        source_ref = paperless_source_ref(document_id, binary.version_id, binary.filename)
        return PaperlessSourceCapture(
            document_id=document_id,
            version_id=binary.version_id,
            original_filename=binary.filename,
            media_type=binary.media_type,
            byte_size=len(binary.content),
            content_hash=f"sha256:{binary.sha256}",
            storage_reference=(
                f"paperless://document/{document_id}/version/"
                f"{quote(binary.version_id, safe='-_.')}"
            ),
            source_ref=source_ref,
            content=binary.content,
        )

    def get_task(self, task_id: str) -> dict[str, Any]:
        payload = self._request("GET", "/api/tasks/", params={"task_id": task_id}).json()
        if isinstance(payload, dict) and isinstance(payload.get("results"), list):
            results = payload["results"]
            return results[0] if results else {"task_id": task_id, "status": "unknown"}
        if isinstance(payload, list):
            return payload[0] if payload else {"task_id": task_id, "status": "unknown"}
        return payload

    def post_document(
        self,
        *,
        filename: str,
        content: bytes,
        media_type: str = "application/octet-stream",
        title: str | None = None,
        tags: list[int] | None = None,
        custom_fields: dict[int | str, Any] | None = None,
    ) -> str:
        """Perform native upload. Prefer ``governed_post_document`` for real use."""

        # httpx multipart expects a mapping; list values are expanded to repeated
        # form fields, which matches Paperless' repeated ``tags`` contract.
        data: dict[str, Any] = {}
        if title:
            data["title"] = title
        if tags:
            data["tags"] = [str(tag) for tag in tags]
        if custom_fields:
            data["custom_fields"] = json.dumps(custom_fields, separators=(",", ":"))
        response = self._request(
            "POST",
            "/api/documents/post_document/",
            files={"document": (Path(filename).name, content, media_type)},
            data=data,
        )
        payload = response.json()
        if isinstance(payload, str):
            return payload
        if isinstance(payload, dict):
            for key in ("task_id", "id", "task"):
                if payload.get(key):
                    return str(payload[key])
        raise PaperlessError("Paperless upload did not return a consumption task id")

    def update_document_metadata(self, document_id: int, changes: dict[str, Any]) -> dict[str, Any]:
        """Perform one allowlisted metadata mutation. Prefer the governed helper."""

        unknown = sorted(set(changes) - _ALLOWED_METADATA_FIELDS)
        if unknown:
            raise PaperlessMutationError(
                "metadata mutation contains forbidden fields: " + ", ".join(unknown)
            )
        if not changes:
            raise PaperlessMutationError("metadata mutation is empty")
        return self._request(
            "PATCH", f"/api/documents/{document_id}/", json=changes
        ).json()


def governed_update_document_metadata(
    policy: PolicyClient,
    paperless: PaperlessClient,
    *,
    document_id: int,
    changes: dict[str, Any],
    decision_payload: dict[str, Any],
    candidate: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Apply classification/metadata only after Pantheon policy allows the effect."""

    proposed = {
        "effect_kind": "external_document_metadata_update",
        "resource": "paperless_ngx",
        "document_id": document_id,
        "changed_fields": sorted(changes),
        **(candidate or {}),
    }
    return governed_effect(
        policy,
        candidate=proposed,
        decision_payload=decision_payload,
        effect=lambda: paperless.update_document_metadata(document_id, changes),
    )


def governed_post_document(
    policy: PolicyClient,
    paperless: PaperlessClient,
    *,
    filename: str,
    content: bytes,
    decision_payload: dict[str, Any],
    media_type: str = "application/octet-stream",
    title: str | None = None,
    tags: list[int] | None = None,
    custom_fields: dict[int | str, Any] | None = None,
    candidate: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Upload one source only after a valid consequential Pantheon gate."""

    digest = hashlib.sha256(content).hexdigest()
    proposed = {
        "effect_kind": "external_document_upload",
        "resource": "paperless_ngx",
        "filename": Path(filename).name,
        "content_hash": f"sha256:{digest}",
        **(candidate or {}),
    }
    return governed_effect(
        policy,
        candidate=proposed,
        decision_payload=decision_payload,
        effect=lambda: paperless.post_document(
            filename=filename,
            content=content,
            media_type=media_type,
            title=title,
            tags=tags,
            custom_fields=custom_fields,
        ),
    )
