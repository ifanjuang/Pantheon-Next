"""Load and validate the canonical Pantheon Next contracts.

A monorepo checkout reads the repository-root ``schemas/`` files directly. A
built distribution reads an exact generated copy staged inside the wheel at
build time. The generated copy is distribution material only: it is never a
second version-controlled authority.

Conformance remains distinct from authorization. A payload that validates is
structurally conformant; it is not approved, Evidence, admitted or canonized.
"""

from __future__ import annotations

from functools import lru_cache
import hashlib
import json
from pathlib import Path
import subprocess
from typing import Any

import jsonschema
from referencing import Registry, Resource
import yaml

from .contract_manifest import CANONICAL_REPOSITORY, CONTRACT_PATHS

_PACKAGE_ROOT = Path(__file__).resolve().parent
_MONOREPO_ROOT = Path(__file__).resolve().parents[2]
_GENERATED_ROOT = _PACKAGE_ROOT / "_generated_contracts"
_MANIFEST = _GENERATED_ROOT / "manifest.json"


class ContractViolation(ValueError):
    """An emitted payload does not conform to the canonical contract."""


class ContractUnavailable(RuntimeError):
    """A declared canonical contract is missing, unreadable or invalid."""


def _source_root() -> tuple[Path, str]:
    if (_MONOREPO_ROOT / "schemas").is_dir():
        return _MONOREPO_ROOT, "canonical-repository"
    if (_GENERATED_ROOT / "schemas").is_dir():
        return _GENERATED_ROOT, "packaged-build-artifact"
    raise ContractUnavailable(
        "canonical Pantheon contracts unavailable: neither monorepo schemas/ "
        "nor packaged generated contracts are present"
    )


def _relative_path(name: str) -> str:
    try:
        return CONTRACT_PATHS[name]
    except KeyError as exc:
        raise ContractUnavailable(f"unknown Pantheon contract: {name}") from exc


def schema_path(name: str) -> Path:
    root, _ = _source_root()
    path = root / _relative_path(name)
    if not path.is_file():
        raise ContractUnavailable(
            f"canonical Pantheon contract unavailable: {name} ({_relative_path(name)})"
        )
    return path


@lru_cache(maxsize=None)
def load_schema(name: str) -> dict[str, Any]:
    path = schema_path(name)
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ContractUnavailable(f"cannot read Pantheon contract: {name}") from exc
    except yaml.YAMLError as exc:
        raise ContractUnavailable(f"Pantheon contract is not valid YAML: {name}") from exc
    if not isinstance(value, dict):
        raise ContractUnavailable(f"Pantheon contract is not a mapping: {name}")
    return value


def _schema_with_file_id(name: str) -> dict[str, Any]:
    schema = dict(load_schema(name))
    schema.setdefault("$id", schema_path(name).resolve().as_uri())
    return schema


@lru_cache(maxsize=1)
def _registry() -> Registry:
    registry = Registry()
    for name in CONTRACT_PATHS:
        path = schema_path(name)
        schema = _schema_with_file_id(name)
        try:
            resource = Resource.from_contents(schema)
        except Exception as exc:  # pragma: no cover - guarded by schema tests
            raise ContractUnavailable(f"cannot register Pantheon contract: {name}") from exc
        registry = registry.with_resource(path.resolve().as_uri(), resource)
    return registry


@lru_cache(maxsize=None)
def _validator(name: str) -> jsonschema.Draft202012Validator:
    schema = _schema_with_file_id(name)
    try:
        jsonschema.Draft202012Validator.check_schema(schema)
    except jsonschema.SchemaError as exc:
        raise ContractUnavailable(f"Pantheon contract is not a valid schema: {name}") from exc
    return jsonschema.Draft202012Validator(schema, registry=_registry())


def problems(name: str, payload: Any) -> list[str]:
    """Deterministic conformance findings. Empty means structurally conformant."""
    try:
        errors = sorted(
            _validator(name).iter_errors(payload),
            key=lambda error: (
                tuple(str(part) for part in error.absolute_path),
                error.message,
            ),
        )
    except ContractUnavailable:
        raise
    except Exception as exc:
        raise ContractUnavailable(f"cannot resolve Pantheon contract graph: {name}") from exc
    return [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in errors
    ]


def declared_properties(name: str) -> frozenset[str]:
    return frozenset(load_schema(name).get("properties", {}))


def validate(name: str, payload: Any) -> Any:
    found = problems(name, payload)
    if found:
        raise ContractViolation(
            f"payload does not conform to the canonical {name} contract: "
            + "; ".join(found)
        )
    return payload


def definition_enum(name: str, definition: str) -> tuple[Any, ...]:
    """Read one closed enum directly from a canonical schema definition."""
    value = load_schema(name).get("$defs", {}).get(definition, {}).get("enum")
    if not isinstance(value, list) or not value:
        raise ContractUnavailable(
            f"Pantheon contract {name} has no non-empty $defs.{definition}.enum"
        )
    return tuple(value)


def _git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(
        f"blob {len(raw)}\0".encode("ascii") + raw,
        usedforsecurity=False,
    ).hexdigest()


def _repository_revision() -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(_MONOREPO_ROOT), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            timeout=2,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    value = result.stdout.strip()
    return value if result.returncode == 0 and len(value) == 40 else None


def _packaged_manifest() -> dict[str, Any]:
    if not _MANIFEST.is_file():
        return {}
    try:
        value = json.loads(_MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def provenance(name: str) -> dict[str, Any]:
    """Provenance of the exact schema bytes currently used for validation."""
    path = schema_path(name)
    raw = path.read_bytes()
    _, source_kind = _source_root()
    manifest = _packaged_manifest() if source_kind == "packaged-build-artifact" else {}
    revision = (
        manifest.get("source_revision")
        if source_kind == "packaged-build-artifact"
        else _repository_revision()
    )
    return {
        "source_repository": CANONICAL_REPOSITORY,
        "source_path": _relative_path(name),
        "source_commit": revision,
        "source_blob_sha": _git_blob_sha(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "posture": source_kind,
        "authority_transfer": False,
    }
