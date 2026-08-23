from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "document_runtime_synthetic_check.py"


def _load():
    spec = importlib.util.spec_from_file_location("document_runtime_synthetic_check", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _observations(*, hermes="installed_observed"):
    return {
        "observations": [
            {
                "source": "paperless_gateway",
                "paperless_reachability_status": "reachable",
            },
            {"source": "pantheon_pdp", "readiness_status": "ready_observed"},
            {"source": "docling_serve", "reachability_status": "reachable"},
            {"source": "hermes_native_inventory", "installation_status": hermes},
        ]
    }


def _decision_payload():
    return {
        "decision": {
            "decision_id": "decision.synthetic.1",
            "decided_by": "human.operator",
            "approval_level": "C2",
            "scope": {"scope_type": "project", "scope_id": "synthetic"},
            "object_identity": "paperless-intake:synthetic:42:7",
            "content_digest": "sha256:abc",
            "expires_at": "2026-07-26T00:00:00Z",
        },
        "expectation": {
            "required_ceiling": "C2",
            "required_scope": {"scope_type": "project", "scope_id": "synthetic"},
            "object_identity": "paperless-intake:synthetic:42:7",
            "expected_digest": "sha256:abc",
        },
    }


def test_assessment_requires_all_four_independent_observations():
    module = _load()
    ready = module.assess_observations(_observations())
    assert ready["candidate_ready_for_synthetic_intake"] is True
    assert ready["production_authorization"] is False
    assert ready["safety_status"] == "not_inferred"

    missing_hermes = module.assess_observations(_observations(hermes="not_observed"))
    assert missing_hermes["candidate_ready_for_synthetic_intake"] is False
    assert missing_hermes["checks"]["hermes_skill_installed"] is False


def test_synthetic_contract_guard_requires_marker_and_exact_source(tmp_path):
    module = _load()
    contract = tmp_path / "task-contract.yaml"
    contract.write_text(
        "contract_id: tc.synthetic-check\n"
        "parent_project_id: synthetic-document-runtime\n"
        "source_ref: paperless/42/versions/7/synthetic.pdf\n",
        encoding="utf-8",
    )
    text = module._assert_synthetic_contract(
        contract, "paperless/42/versions/7/synthetic.pdf"
    )
    assert "synthetic-document-runtime" in text

    with pytest.raises(module.CheckError, match="source_ref"):
        module._assert_synthetic_contract(contract, "paperless/42/versions/8/other.pdf")

    real_contract = tmp_path / "real.yaml"
    real_contract.write_text(
        "contract_id: tc.project-client\nsource_ref: paperless/42/versions/7/client.pdf\n",
        encoding="utf-8",
    )
    with pytest.raises(module.CheckError, match="explicitly synthetic"):
        module._assert_synthetic_contract(real_contract, "paperless/42/versions/7/client.pdf")


def test_installed_skill_transport_is_fixed_and_strips_operator_secrets(tmp_path):
    module = _load()
    root = tmp_path / "pantheon-document-intake"
    script = root / "scripts" / "pantheon_document_intake.py"
    script.parent.mkdir(parents=True)
    script.write_text("# fixture\n", encoding="utf-8")
    observed = {}

    def runner(command, **kwargs):
        observed["command"] = command
        observed["kwargs"] = kwargs
        return SimpleNamespace(
            returncode=0,
            stdout=json.dumps(
                {
                    "document_id": 42,
                    "version_id": "7",
                    "source_ref": "paperless/42/versions/7/synthetic.pdf",
                }
            ),
            stderr="",
        )

    env = {
        "MVP_HERMES_API_KEY": "hermes-key",
        "PANTHEON_PAPERLESS_GATEWAY_URL": "http://gateway:8082",
        "PANTHEON_POLICY_API_KEY": "policy-secret",
        "PAPERLESS_API_TOKEN": "paperless-secret",
        "PANTHEON_DECISION_ISSUER_KEYS_PATH": "/secrets/issuers.yaml",
        "PANTHEON_DECISION_ISSUER_SIGNING_SECRET": "issuer-secret",
        "PATH": "/usr/bin",
    }
    result = module._run_skill_json(
        root,
        ["capture", "--document-id", "42", "--version-id", "7"],
        runner=runner,
        env_source=env,
    )
    assert observed["command"][1] == str(script)
    assert observed["command"][2:] == [
        "capture",
        "--document-id",
        "42",
        "--version-id",
        "7",
    ]
    assert "shell" not in observed["kwargs"]
    child_env = observed["kwargs"]["env"]
    assert child_env["MVP_HERMES_API_KEY"] == "hermes-key"
    assert child_env["PANTHEON_PAPERLESS_GATEWAY_URL"] == "http://gateway:8082"
    assert child_env["PATH"] == "/usr/bin"
    for secret_name in module._SKILL_STRIPPED_ENV:
        assert secret_name not in child_env
    assert result["source_ref"].endswith("synthetic.pdf")


def test_operator_helper_signs_decision_without_mutating_source_file(tmp_path):
    module = _load()
    path = tmp_path / "decision.json"
    original = _decision_payload()
    path.write_text(json.dumps(original), encoding="utf-8")

    signed, did_sign = module._prepare_decision_payload(path, signing_secret="test-secret")

    assert did_sign is True
    assert signed["decision"]["signature"]
    assert "signature" not in original["decision"]
    assert "signature" not in json.loads(path.read_text(encoding="utf-8"))["decision"]


def test_issuer_validation_uses_pep_returned_expectation(monkeypatch):
    module = _load()
    observed = {}
    payload = _decision_payload()
    expectation = {
        "required_ceiling": "C2",
        "required_scope": {"scope_type": "project", "scope_id": "synthetic"},
        "object_identity": "paperless-intake:synthetic:42:7",
        "expected_digest": "sha256:abc",
    }

    def fake_request(method, url, *, bearer, body=None, timeout=20.0):
        observed.update(
            {"method": method, "url": url, "bearer": bearer, "body": body, "timeout": timeout}
        )
        return {
            "verdict": "valid",
            "issuer_authenticated": True,
            "checks": {"issuer": "valid"},
            "findings": [],
            "gate_signal_validation_performed": True,
            "secret": "must-not-project",
        }

    monkeypatch.setattr(module, "_json_request", fake_request)
    result = module._validate_issuer_proof(
        policy_url="http://pdp:8000",
        policy_api_key="policy-key",
        decision_payload=payload,
        expectation=expectation,
    )

    assert observed["url"] == "http://pdp:8000/v1/policy/decisions:validate"
    assert observed["body"] == {"decision": payload["decision"], "expectation": expectation}
    assert result["verdict"] == "valid"
    assert result["issuer_authenticated"] is True
    assert "secret" not in result


def test_unsigned_decision_stays_explicitly_unproven(tmp_path):
    module = _load()
    path = tmp_path / "decision.json"
    path.write_text(json.dumps(_decision_payload()), encoding="utf-8")
    unsigned, did_sign = module._prepare_decision_payload(path, signing_secret=None)
    assert did_sign is False
    assert "signature" not in unsigned["decision"]
