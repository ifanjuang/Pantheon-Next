"""Validate emitted payloads against the vendored Pantheon-Next contracts.

The vendored schemas under ``vendor/pantheon/`` are read-only snapshots pinned by
a ``*.source.json`` sidecar. They are the shape Pantheon-Next defines; this repo
implements it. Nothing here transfers authority: a payload that validates is
conformant, not approved, admitted or canonized.

Without this, conformance was asserted by *name*: a migration called
``013_information_card_projection.sql`` carried the contract's name and nothing
checked that what it produced matched. Where a payload was checked at all, it was
against a hand-copied ``required`` set that drifts silently from the contract it
mirrors.

Loading is cached: the schemas are immutable snapshots and validating a batch of
records should not re-read and re-compile them each time.
"""

from __future__ import annotations

from functools import lru_cache
import json
from pathlib import Path
from typing import Any

import jsonschema
import yaml

VENDOR = Path(__file__).resolve().parent / "vendor" / "pantheon"


class ContractViolation(ValueError):
    """An emitted payload does not conform to the vendored contract."""


class ContractUnavailable(RuntimeError):
    """The vendored contract is missing, unreadable or not a valid schema."""


@lru_cache(maxsize=None)
def _validator(name: str) -> jsonschema.Draft202012Validator:
    path = VENDOR / f"{name}.schema.yaml"
    try:
        schema = yaml.safe_load(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ContractUnavailable(f"vendored contract unavailable: {name}") from exc
    except yaml.YAMLError as exc:
        raise ContractUnavailable(f"vendored contract is not valid YAML: {name}") from exc
    try:
        jsonschema.Draft202012Validator.check_schema(schema)
    except jsonschema.SchemaError as exc:
        raise ContractUnavailable(f"vendored contract is not a valid schema: {name}") from exc
    return jsonschema.Draft202012Validator(schema)


def problems(name: str, payload: Any) -> list[str]:
    """Deterministic, human-readable conformance problems. Empty means conformant."""
    errors = sorted(
        _validator(name).iter_errors(payload),
        key=lambda error: (tuple(str(part) for part in error.absolute_path), error.message),
    )
    return [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in errors
    ]


def declared_properties(name: str) -> frozenset[str]:
    """The top-level field names the contract declares.

    Callers that want to name the offending fields in their own error message can
    subtract this from a payload instead of restating the field list, which is the
    hand-copy this module exists to remove.
    """
    return frozenset(_validator(name).schema.get("properties", {}))


def validate(name: str, payload: Any) -> Any:
    """Return the payload when it conforms; raise ContractViolation otherwise."""
    found = problems(name, payload)
    if found:
        raise ContractViolation(
            f"payload does not conform to the vendored {name} contract: " + "; ".join(found)
        )
    return payload


def provenance(name: str) -> dict:
    """The recorded upstream provenance of one vendored contract."""
    try:
        return json.loads((VENDOR / f"{name}.source.json").read_text(encoding="utf-8"))
    except OSError as exc:
        raise ContractUnavailable(f"vendored provenance unavailable: {name}") from exc
