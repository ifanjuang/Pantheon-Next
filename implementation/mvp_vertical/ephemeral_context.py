"""Provider-neutral bounded ephemeral context leases for read-only runtime input.

Leases are transient byte holders only. They are not Sources, AFFAIRES
persistence, Hindsight memory, Evidence, execution admission or effect authority.
The immutable handoff binds only lease_ref + exact digest + bounded metadata.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


MIN_TTL_SECONDS = 60
MAX_TTL_SECONDS = 3600
MAX_LEASE_BYTES = 8 * 1024 * 1024
MAX_PROVENANCE_ITEMS = 100
LEASE_REF_RE = re.compile(r"^lease-[a-f0-9]{32}$")


class EphemeralContextError(RuntimeError):
    pass


class LeaseNotFound(EphemeralContextError):
    pass


class LeaseExpired(EphemeralContextError):
    pass


class LeaseCorrupt(EphemeralContextError):
    pass


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _parse_iso(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise LeaseCorrupt("lease manifest contains an invalid timestamp") from exc
    if parsed.tzinfo is None:
        raise LeaseCorrupt("lease manifest timestamp must be timezone-aware")
    return parsed.astimezone(timezone.utc)


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _validate_ref(lease_ref: str) -> str:
    value = str(lease_ref or "").strip()
    if not LEASE_REF_RE.fullmatch(value):
        raise EphemeralContextError("invalid ephemeral lease_ref")
    return value


def _bounded_provenance(items: list[dict[str, Any]] | None) -> list[dict[str, Any]]:
    values = list(items or [])
    if len(values) > MAX_PROVENANCE_ITEMS:
        raise EphemeralContextError(
            f"source_provenance exceeds {MAX_PROVENANCE_ITEMS} entries"
        )
    try:
        encoded = json.dumps(values, sort_keys=True, ensure_ascii=False).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise EphemeralContextError("source_provenance must be JSON serializable") from exc
    if len(encoded) > 128 * 1024:
        raise EphemeralContextError("source_provenance exceeds 128 KiB")
    return values


class EphemeralContextStore:
    """Filesystem-backed replaceable lease store.

    Restart loss is acceptable by contract. Missing/expired/corrupt leases fail
    closed and must be re-prepared from the provider rather than reconstructed
    from another source.
    """

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root).expanduser().resolve()
        if self.root.exists() and not self.root.is_dir():
            raise EphemeralContextError("ephemeral context root must be a directory")
        self.root.mkdir(parents=True, exist_ok=True)
        try:
            os.chmod(self.root, 0o700)
        except OSError:
            pass

    def _paths(self, lease_ref: str) -> tuple[Path, Path]:
        ref = _validate_ref(lease_ref)
        manifest = (self.root / f"{ref}.json").resolve(strict=False)
        payload = (self.root / f"{ref}.bin").resolve(strict=False)
        if not manifest.is_relative_to(self.root) or not payload.is_relative_to(self.root):
            raise EphemeralContextError("ephemeral lease path escaped lease root")
        return manifest, payload

    def create(
        self,
        data: bytes,
        *,
        media_type: str,
        source_provenance: list[dict[str, Any]] | None = None,
        ttl_seconds: int = 900,
        now: datetime | None = None,
    ) -> dict[str, Any]:
        if not isinstance(data, (bytes, bytearray)):
            raise EphemeralContextError("ephemeral lease data must be bytes")
        payload_bytes = bytes(data)
        if not payload_bytes:
            raise EphemeralContextError("ephemeral lease data must be non-empty")
        if len(payload_bytes) > MAX_LEASE_BYTES:
            raise EphemeralContextError(
                f"ephemeral lease exceeds {MAX_LEASE_BYTES} bytes"
            )
        if not MIN_TTL_SECONDS <= int(ttl_seconds) <= MAX_TTL_SECONDS:
            raise EphemeralContextError(
                f"ttl_seconds must be between {MIN_TTL_SECONDS} and {MAX_TTL_SECONDS}"
            )
        media = str(media_type or "").strip()
        if not media or len(media) > 200:
            raise EphemeralContextError("media_type is required and must be <= 200 chars")
        provenance = _bounded_provenance(source_provenance)

        created_at = (now or _utc_now()).astimezone(timezone.utc)
        expires_at = created_at + timedelta(seconds=int(ttl_seconds))
        lease_ref = f"lease-{uuid.uuid4().hex}"
        manifest_path, payload_path = self._paths(lease_ref)
        digest = _digest(payload_bytes)
        manifest = {
            "lease_ref": lease_ref,
            "content_sha256": digest,
            "byte_size": len(payload_bytes),
            "media_type": media,
            "source_provenance": provenance,
            "created_at": _iso(created_at),
            "expires_at": _iso(expires_at),
            "state": "active",
        }

        payload_tmp: Path | None = None
        manifest_tmp: Path | None = None
        try:
            fd, name = tempfile.mkstemp(prefix=f".{lease_ref}.", suffix=".bin.tmp", dir=self.root)
            payload_tmp = Path(name)
            with os.fdopen(fd, "wb") as handle:
                handle.write(payload_bytes)
                handle.flush()
                os.fsync(handle.fileno())
            os.chmod(payload_tmp, 0o600)

            fd, name = tempfile.mkstemp(prefix=f".{lease_ref}.", suffix=".json.tmp", dir=self.root)
            manifest_tmp = Path(name)
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                json.dump(manifest, handle, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
                handle.flush()
                os.fsync(handle.fileno())
            os.chmod(manifest_tmp, 0o600)

            os.replace(payload_tmp, payload_path)
            payload_tmp = None
            os.replace(manifest_tmp, manifest_path)
            manifest_tmp = None
        finally:
            for tmp in (payload_tmp, manifest_tmp):
                if tmp is not None:
                    try:
                        tmp.unlink()
                    except FileNotFoundError:
                        pass
        return dict(manifest)

    def metadata(
        self,
        lease_ref: str,
        *,
        expected_digest: str | None = None,
        now: datetime | None = None,
    ) -> dict[str, Any]:
        manifest_path, payload_path = self._paths(lease_ref)
        try:
            raw = manifest_path.read_text(encoding="utf-8")
            manifest = json.loads(raw)
        except FileNotFoundError as exc:
            raise LeaseNotFound(f"ephemeral lease is unavailable: {lease_ref}") from exc
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise LeaseCorrupt(f"ephemeral lease manifest is unreadable: {lease_ref}") from exc
        if not isinstance(manifest, dict) or manifest.get("lease_ref") != lease_ref:
            raise LeaseCorrupt("ephemeral lease manifest identity mismatch")
        digest = str(manifest.get("content_sha256") or "").lower()
        if len(digest) != 64 or any(char not in "0123456789abcdef" for char in digest):
            raise LeaseCorrupt("ephemeral lease manifest has an invalid SHA-256")
        if expected_digest is not None and digest != str(expected_digest).strip().lower():
            raise LeaseCorrupt("ephemeral lease digest differs from admitted digest")
        expires_at = _parse_iso(str(manifest.get("expires_at") or ""))
        current = (now or _utc_now()).astimezone(timezone.utc)
        if current >= expires_at:
            raise LeaseExpired(f"ephemeral lease expired: {lease_ref}")
        try:
            stat = payload_path.stat()
        except FileNotFoundError as exc:
            raise LeaseNotFound(f"ephemeral lease bytes are unavailable: {lease_ref}") from exc
        expected_size = int(manifest.get("byte_size") or -1)
        if not payload_path.is_file() or stat.st_size != expected_size:
            raise LeaseCorrupt("ephemeral lease byte size mismatch")
        return dict(manifest)

    def resolve(
        self,
        lease_ref: str,
        *,
        expected_digest: str | None = None,
        now: datetime | None = None,
    ) -> tuple[dict[str, Any], bytes]:
        manifest = self.metadata(
            lease_ref,
            expected_digest=expected_digest,
            now=now,
        )
        _, payload_path = self._paths(lease_ref)
        try:
            data = payload_path.read_bytes()
        except OSError as exc:
            raise LeaseNotFound(f"ephemeral lease bytes are unavailable: {lease_ref}") from exc
        digest = _digest(data)
        if digest != manifest["content_sha256"]:
            raise LeaseCorrupt("ephemeral lease bytes no longer match admitted digest")
        return manifest, data

    def cleanup_expired(self, *, now: datetime | None = None) -> int:
        current = (now or _utc_now()).astimezone(timezone.utc)
        removed = 0
        for manifest_path in self.root.glob("lease-*.json"):
            lease_ref = manifest_path.stem
            try:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                expires_at = _parse_iso(str(manifest.get("expires_at") or ""))
            except Exception:
                continue
            if current < expires_at:
                continue
            _, payload_path = self._paths(lease_ref)
            for path in (payload_path, manifest_path):
                try:
                    path.unlink()
                except FileNotFoundError:
                    pass
            removed += 1
        return removed
