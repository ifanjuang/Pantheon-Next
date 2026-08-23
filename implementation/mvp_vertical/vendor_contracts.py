"""Compatibility facade for the canonical Pantheon contract registry.

Historically this module loaded committed snapshots from ``vendor/pantheon``.
After monorepo consolidation, the implementation consumes the repository-root
canonical schemas through :mod:`mvp_vertical.pantheon_contracts`. Keeping this
module temporarily avoids mixing contract-source migration with caller renames.

The facade transfers no authority: structural conformance is not approval,
Evidence admission, canonization or runtime authorization.
"""

from .pantheon_contracts import (  # noqa: F401
    CONTRACT_PATHS,
    ContractUnavailable,
    ContractViolation,
    declared_properties,
    definition_enum,
    load_schema,
    problems,
    provenance,
    schema_path,
    validate,
)

__all__ = [
    "CONTRACT_PATHS",
    "ContractUnavailable",
    "ContractViolation",
    "declared_properties",
    "definition_enum",
    "load_schema",
    "problems",
    "provenance",
    "schema_path",
    "validate",
]
