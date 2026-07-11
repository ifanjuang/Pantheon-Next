"""Task Contract loading and perimeter checks.

The contract is data; loading it grants nothing. Every operation in the
package takes the contract as input and refuses anything outside its
declared scope.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

import yaml

REQUIRED_FIELDS = (
    "object_type",
    "object_id",
    "contract_id",
    "status",
    "declared_scope",
    "forbidden_scope",
    "expected_output",
)


class ContractError(ValueError):
    """The contract is malformed or an operation falls outside it."""


@dataclass(frozen=True)
class TaskContract:
    raw: dict
    path: Path
    dossier: str
    sources: tuple[str, ...]
    operations: tuple[str, ...]
    forbidden: tuple[str, ...] = field(default=())

    @property
    def contract_id(self) -> str:
        return self.raw["contract_id"]


def load_contract(path: str | Path) -> TaskContract:
    path = Path(path)
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ContractError(f"{path}: contract is not a mapping")
    missing = [f for f in REQUIRED_FIELDS if f not in data]
    if missing:
        raise ContractError(f"{path}: missing contract fields: {missing}")
    if data["object_type"] != "task_contract":
        raise ContractError(f"{path}: object_type is not task_contract")
    scope = data["declared_scope"]
    sources = tuple(scope["sources"])
    # A declared perimeter must not, by itself, be able to point the runner at
    # an absolute path or out of the tree. Shape is checked here, at load, so an
    # unsafe contract never loads; symlink escape is checked at read time
    # (resolve_source_within) because it needs the ingestion root.
    for source_ref in sources:
        assert_source_path_safe(source_ref, data["contract_id"])
    return TaskContract(
        raw=data,
        path=path,
        dossier=scope["dossier"],
        sources=sources,
        operations=tuple(scope.get("operations", ())),
        forbidden=tuple(data.get("forbidden_scope", ())),
    )


def assert_source_path_safe(source_ref: str, contract_id: str) -> None:
    """Reject a declared source that is absolute or traverses out of the tree.

    Membership in the declared set (assert_source_in_scope) says nothing about
    the *shape* of a path: a contract that declares '/etc/passwd' or
    '../../secret.md' would pass membership and be read verbatim. This guard
    closes two of the three attacks the adoption gate names — absolute paths
    and '..' traversal — before any file is touched. The third, symlink
    escape, is caught at read time by resolve_source_within.
    """
    if not source_ref or not source_ref.strip():
        raise ContractError(f"contract {contract_id}: empty declared source")
    if "\\" in source_ref or PurePosixPath(source_ref).is_absolute():
        raise ContractError(
            f"contract {contract_id}: declared source is not a relative path: {source_ref!r}"
        )
    if ".." in PurePosixPath(source_ref).parts:
        raise ContractError(
            f"contract {contract_id}: declared source traverses out of tree ('..'): {source_ref!r}"
        )


def resolve_source_within(root: Path, source_ref: str, contract_id: str) -> Path:
    """Resolve a declared source against root and assert symlink-safe containment.

    Path.resolve() follows symlinks, so an in-tree file that is a symlink
    pointing outside the tree is caught here even though its declared path
    looks clean. Returns the resolved, contained path ready to read.
    """
    root_real = root.resolve()
    target_real = (root / source_ref).resolve()
    if not target_real.is_relative_to(root_real):
        raise ContractError(
            f"contract {contract_id}: declared source resolves outside the tree "
            f"(symlink escape?): {source_ref!r} -> {target_real}"
        )
    return target_real


def assert_source_in_scope(contract: TaskContract, source_ref: str) -> None:
    if source_ref not in contract.sources:
        raise ContractError(
            f"source outside declared perimeter: {source_ref!r} "
            f"(contract {contract.contract_id})"
        )


def assert_operation_allowed(contract: TaskContract, operation: str) -> None:
    if operation in contract.forbidden:
        raise ContractError(
            f"operation forbidden by contract {contract.contract_id}: {operation}"
        )
    if contract.operations and operation not in contract.operations:
        raise ContractError(
            f"operation not declared by contract {contract.contract_id}: {operation}"
        )
