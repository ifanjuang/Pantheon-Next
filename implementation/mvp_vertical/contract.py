"""Task Contract loading and perimeter checks.

The contract is data; loading it grants nothing. Every operation in the
package takes the contract as input and refuses anything outside its
declared scope.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

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
    return TaskContract(
        raw=data,
        path=path,
        dossier=scope["dossier"],
        sources=tuple(scope["sources"]),
        operations=tuple(scope.get("operations", ())),
        forbidden=tuple(data.get("forbidden_scope", ())),
    )


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
