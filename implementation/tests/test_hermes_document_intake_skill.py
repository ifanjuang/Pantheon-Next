from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "hermes" / "skills" / "pantheon-document-intake" / "SKILL.md"
SCRIPT = SKILL.parent / "scripts" / "pantheon_document_intake.py"


def _load_script():
    spec = importlib.util.spec_from_file_location("pantheon_document_intake_skill", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_skill_uses_standard_frontmatter_and_operating_sections():
    text = SKILL.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    _, frontmatter, body = text.split("---", 2)
    metadata = yaml.safe_load(frontmatter)
    assert metadata["name"] == "pantheon-document-intake"
    assert metadata["description"].endswith(".")
    assert len(metadata["description"]) <= 60
    assert metadata["version"] == "0.1.0"
    assert metadata["metadata"]["hermes"]["category"] == "productivity"
    for section in (
        "## When to Use",
        "## Prerequisites",
        "## How to Run",
        "## Quick Reference",
        "## Procedure",
        "## Pitfalls",
        "## Verification",
    ):
        assert section in body


def test_skill_preserves_pantheon_boundaries_in_text():
    text = SKILL.read_text(encoding="utf-8")
    for required in (
        "Project Document candidate != Knowledge Item",
        "Source Capture != Evidence",
        "Paperless metadata != canonical business classification",
        "Do not call Paperless directly from the skill",
        "Caller-supplied `expectation` values",
    ):
        assert required in text


def test_transport_script_never_asks_for_paperless_or_policy_secret():
    text = SCRIPT.read_text(encoding="utf-8")
    assert "PAPERLESS_API_TOKEN" not in text
    assert "PANTHEON_POLICY_API_KEY" not in text
    assert "MVP_HERMES_API_KEY" in text


def test_gateway_client_keeps_hermes_key_in_authorization_header(monkeypatch):
    module = _load_script()
    observed = {}

    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def read(self):
            return b'{"count":0,"documents":[]}'

    def fake_urlopen(request, timeout):
        observed["url"] = request.full_url
        observed["authorization"] = request.get_header("Authorization")
        observed["data"] = request.data
        observed["timeout"] = timeout
        return Response()

    monkeypatch.setenv("MVP_HERMES_API_KEY", "super-secret-runtime-key")
    monkeypatch.setenv("PANTHEON_PAPERLESS_GATEWAY_URL", "http://gateway.internal:8082")
    monkeypatch.setattr(module, "urlopen", fake_urlopen)

    client = module.GatewayClient()
    payload = client.request("GET", "/v1/paperless/documents", params={"query": "CCTP"})
    assert payload["count"] == 0
    assert observed["url"].endswith("/v1/paperless/documents?query=CCTP")
    assert observed["authorization"] == "Bearer super-secret-runtime-key"
    assert observed["data"] is None
    assert "super-secret-runtime-key" not in observed["url"]


def test_intake_command_sends_contract_and_decision_without_local_policy(monkeypatch, tmp_path, capsys):
    module = _load_script()
    contract = tmp_path / "task-contract.yaml"
    decision = tmp_path / "decision.json"
    contract.write_text("object_type: task_contract\n", encoding="utf-8")
    decision.write_text(json.dumps({"decision": {"decision_id": "d1"}}), encoding="utf-8")
    observed = {}

    class FakeClient:
        def request(self, method, path, *, params=None, body=None):
            observed.update({"method": method, "path": path, "params": params, "body": body})
            return {"status": "blocked", "effect_ran": False}

    monkeypatch.setattr(module, "GatewayClient", FakeClient)
    monkeypatch.setattr(
        module.sys,
        "argv",
        [
            "pantheon-document-intake",
            "intake",
            "--document-id",
            "42",
            "--version-id",
            "7",
            "--contract",
            str(contract),
            "--decision",
            str(decision),
        ],
    )
    assert module.main() == 0
    assert observed["method"] == "POST"
    assert observed["path"] == "/v1/paperless/intakes"
    assert observed["body"]["paperless_document_id"] == 42
    assert observed["body"]["paperless_version_id"] == "7"
    assert observed["body"]["task_contract_yaml"] == "object_type: task_contract\n"
    assert observed["body"]["decision_payload"] == {"decision": {"decision_id": "d1"}}
    assert "expectation" not in observed["body"]
    assert json.loads(capsys.readouterr().out)["status"] == "blocked"


def test_metadata_command_requires_exact_version_and_contract():
    module = _load_script()
    parser = module.build_parser()
    args = parser.parse_args(
        [
            "update-metadata",
            "--document-id",
            "42",
            "--version-id",
            "7",
            "--contract",
            "contract.yaml",
            "--changes",
            "changes.json",
            "--decision",
            "decision.json",
        ]
    )
    assert args.version_id == "7"
    assert args.contract == "contract.yaml"
    assert not hasattr(args, "candidate")
