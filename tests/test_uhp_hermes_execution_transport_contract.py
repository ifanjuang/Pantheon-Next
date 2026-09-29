from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
JUNCTION = ROOT / "docs" / "governance" / "HERMES_RUN_LAUNCH_JUNCTION.md"


def test_uhp_remains_external_transport_candidate_not_pantheon_dispatch_owner() -> None:
    text = JUNCTION.read_text(encoding="utf-8")

    assert "Replaceable execution transport qualification — UHP #1141" in text
    assert "Pantheon does not become the UHP task client" in text
    assert "current: native Hermes Runs API" in text
    assert "candidate: UHP client -> UHP server -> Hermes" in text
    assert "current qualification pin is UHP 2026-09-28" in text
    assert "UHP Full lifecycle management is outside the selected scope" in text
    assert "two distinct one-shot Execution Admissions" in text


def test_uhp_candidate_preserves_identity_tool_and_ephemeral_context_boundaries() -> None:
    text = JUNCTION.read_text(encoding="utf-8")

    assert "UHP configured harness != effective Hermes tool surface proven" in text
    assert "UHP session id != Pantheon admission identity" in text
    assert "UHP task accepted != Pantheon authorization" in text
    assert "UHP success != Evidence" in text
    assert "UHP input_file available != ephemeral source-context lease qualified" in text
    assert "#1125 is not superseded merely because UHP Extended can transport files" in text
    assert "replace_native_binding" in text
    assert "partial_transport_only" in text


def test_launch_junction_uses_current_colocated_execution_owner() -> None:
    text = JUNCTION.read_text(encoding="utf-8")

    assert "co-located under `Pantheon-Next/implementation/`" in text
    assert "former `ifanjuang/pantheon-mvp` repository is provenance only" in text
    assert "implementation/scripts/hermes_live_binding_acceptance.py" in text
