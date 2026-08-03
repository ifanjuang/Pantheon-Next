from __future__ import annotations

from pathlib import Path

import pytest

from mvp_vertical import (
    hermes_handoff_store,
    hermes_launch_context,
    hermes_scoped_context,
)
from mvp_vertical.hermes_execution_basis import (
    HermesExecutionBasis,
    HermesExecutionBasisError,
)


def test_execution_basis_normalizes_and_compares_exact_contract_identity() -> None:
    first = HermesExecutionBasis.from_values(
        requested_effect=" read_only ",
        task_contract_ref=" task:1 ",
        context_pack_ref=" context:1 ",
        preview_digest=" digest-1 ",
    )
    second = HermesExecutionBasis.from_values(
        requested_effect="read_only",
        task_contract_ref="task:1",
        context_pack_ref="context:1",
        preview_digest="digest-1",
    )

    assert first == second
    assert first.is_read_only is True


def test_execution_basis_keeps_each_dimension_independent() -> None:
    baseline = HermesExecutionBasis.from_values(
        requested_effect="read_only",
        task_contract_ref="task:1",
        context_pack_ref="context:1",
        preview_digest="digest-1",
    )
    changed_context = HermesExecutionBasis.from_values(
        requested_effect="read_only",
        task_contract_ref="task:1",
        context_pack_ref="context:2",
        preview_digest="digest-1",
    )

    assert baseline != changed_context


def test_execution_basis_refuses_incomplete_structure() -> None:
    with pytest.raises(HermesExecutionBasisError, match="context_pack_ref"):
        HermesExecutionBasis.from_values(
            requested_effect="read_only",
            task_contract_ref="task:1",
            context_pack_ref="",
            preview_digest="digest-1",
            label="test basis",
        )


def test_handoff_launch_and_runtime_share_basis_without_granting_authority() -> None:
    handoff_source = Path(hermes_handoff_store.__file__).read_text(encoding="utf-8")
    launch_source = Path(hermes_launch_context.__file__).read_text(encoding="utf-8")
    runtime_source = Path(hermes_scoped_context.__file__).read_text(encoding="utf-8")

    assert "HermesExecutionBasis.from_values" in handoff_source
    assert "HermesExecutionBasis.from_values" in launch_source
    assert "HermesExecutionBasis.from_values" in runtime_source
    assert "execution_authorized=false" in handoff_source
    assert 'current["admission_state"] != "admitted"' in launch_source
    assert 'scope["run_status"] != "running"' in runtime_source
    assert 'scope["run_requested_effect"] == "read_only"' in runtime_source
    assert '"launch reservation != runtime dispatch"' in launch_source
    assert '"runtime success != Evidence"' in runtime_source
