from __future__ import annotations

import json
from pathlib import Path

from mvp_vertical import hermes_cli


class _FakeBinding:
    def __init__(self) -> None:
        self.launch_calls = []
        self.reconcile_calls = []

    def launch(self, **values):
        self.launch_calls.append(values)
        return {
            "kind": "external_hermes_run_launch_receipt",
            "admission_id": values["admission_id"],
            "run_id": "run-1",
            "automatic_retry_performed": False,
            "provider_routing_performed": False,
            "technical_receipt_is_evidence": False,
        }

    def reconcile_once(self, **values):
        self.reconcile_calls.append(values)
        return {
            "kind": "hermes_run_reconciliation",
            "run_id": values["launch_receipt"]["run_id"],
            "pantheon_return_recorded": True,
            "scheduler_effect": False,
            "retry_effect": False,
            "technical_receipt_is_evidence": False,
        }


def test_launch_is_one_shot_and_writes_receipt(monkeypatch, tmp_path: Path) -> None:
    binding = _FakeBinding()
    monkeypatch.setattr(hermes_cli, "_binding", lambda args: binding)
    output = tmp_path / "launch.json"

    status = hermes_cli.main(
        [
            "launch",
            "--allowed-tool",
            "pantheon_context_manifest",
            "--admission-id",
            "admission-1",
            "--idempotency-key",
            "operator-key",
            "--output",
            str(output),
        ]
    )

    assert status == 0
    assert binding.launch_calls == [
        {"admission_id": "admission-1", "idempotency_key": "operator-key"}
    ]
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["automatic_retry_performed"] is False
    assert payload["provider_routing_performed"] is False
    assert payload["technical_receipt_is_evidence"] is False


def test_reconcile_observes_once_without_scheduler_or_retry(monkeypatch, tmp_path: Path) -> None:
    binding = _FakeBinding()
    monkeypatch.setattr(hermes_cli, "_binding", lambda args: binding)
    receipt = tmp_path / "launch.json"
    receipt.write_text(json.dumps({"admission_id": "admission-1", "run_id": "run-1"}), encoding="utf-8")
    output = tmp_path / "return.json"

    status = hermes_cli.main(
        [
            "reconcile",
            "--receipt",
            str(receipt),
            "--idempotency-key",
            "reconcile-key",
            "--output",
            str(output),
        ]
    )

    assert status == 0
    assert len(binding.reconcile_calls) == 1
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["scheduler_effect"] is False
    assert payload["retry_effect"] is False
    assert payload["technical_receipt_is_evidence"] is False


def test_launch_refuses_non_admission_identity(monkeypatch, capsys) -> None:
    monkeypatch.setattr(hermes_cli, "_binding", lambda args: _FakeBinding())

    status = hermes_cli.main(
        [
            "launch",
            "--allowed-tool",
            "pantheon_context_manifest",
            "--admission-id",
            "task-1",
            "--idempotency-key",
            "operator-key",
        ]
    )

    assert status == 1
    assert "must be a Pantheon admission-... identity" in capsys.readouterr().err


def test_observe_requires_explicit_allowlist() -> None:
    parser = hermes_cli.build_parser()
    try:
        parser.parse_args(["observe"])
    except SystemExit as exc:
        assert exc.code == 2
    else:
        raise AssertionError("observe accepted an unspecified tool surface")
