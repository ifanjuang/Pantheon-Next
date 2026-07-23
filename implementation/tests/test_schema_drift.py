"""Schema drift monitor — the pure diff function. Hermetic: NO network.

Only tools/check_schema_drift.py::main() touches the network; the diff logic is
pure and tested here against crafted schemas so the main suite stays offline.
"""

from __future__ import annotations

import sys
from pathlib import Path

# tools/ is dev tooling, not an installed package — ensure the repo root is on
# the path so this test resolves it however pytest is invoked (CI runs `pytest`,
# not `python -m pytest`, so the CWD is not automatically on sys.path).
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.check_schema_drift import (
    STATUS_DOC_FILE,
    UPSTREAM_COMMIT_FILE,
    diff_schemas,
    status_pin_findings,
    upstream_url_for,
    vendored_schemas,
    vocabulary_findings,
)

_PIN = "f8bc3bde142d1e105b7c9a966d8e0d62b39918c4"
_OLD = "782afb474dec572e63d2c944007e1cf5bab37a09"


def _schema(**overrides) -> dict:
    base = {
        "properties": {"object_type": {"enum": ["task_contract", "decision_record"]}},
        "$defs": {
            "decision_record": {
                "required": ["object_type", "decision"],
                "additionalProperties": True,
                "properties": {"decision": {"$ref": "#/$defs/decision_value"}},
            },
            "commitment_flag": {
                "required": ["phrase", "risk"],
                "additionalProperties": False,
                "properties": {"phrase": {"type": "string"}},
            },
            "decision_value": {"type": "string", "enum": ["approve", "refuse"]},
        },
    }
    base.update(overrides)
    return base


def test_identical_schemas_report_no_drift():
    assert diff_schemas(_schema(), _schema()) == []


def test_new_required_field_upstream_is_flagged():
    upstream = _schema()
    upstream["$defs"]["decision_record"]["required"].append("decision_id")
    findings = diff_schemas(_schema(), upstream)
    assert any("decision_record.required" in finding and "decision_id" in finding for finding in findings)


def test_new_object_type_upstream_is_flagged():
    upstream = _schema()
    upstream["properties"]["object_type"]["enum"].append("register_candidate")
    findings = diff_schemas(_schema(), upstream)
    assert any("object_type enum" in finding and "register_candidate" in finding for finding in findings)


def test_new_def_upstream_is_flagged():
    upstream = _schema()
    upstream["$defs"]["grounding_review"] = {"required": ["note"]}
    findings = diff_schemas(_schema(), upstream)
    assert any("$defs added upstream" in finding and "grounding_review" in finding for finding in findings)


def test_property_items_shape_change_is_flagged():
    local = _schema()
    local["$defs"]["result_candidate"] = {
        "properties": {"commitment_flags": {"type": "array", "items": {"type": "string"}}}
    }
    upstream = _schema()
    upstream["$defs"]["result_candidate"] = {
        "properties": {
            "commitment_flags": {
                "type": "array",
                "items": {"$ref": "#/$defs/commitment_flag"},
            }
        }
    }
    findings = diff_schemas(local, upstream)
    assert any("commitment_flags.items" in finding for finding in findings)


def test_enum_change_is_flagged():
    upstream = _schema()
    upstream["$defs"]["decision_value"]["enum"].append("request_revision")
    findings = diff_schemas(_schema(), upstream)
    assert any("decision_value.enum" in finding for finding in findings)


def _vocab(*decisions) -> dict:
    return {"status": "matches_vendored_decision_value", "allowed_decisions": list(decisions)}


def test_vocabulary_matching_schema_reports_no_drift():
    schema = _schema()
    schema["$defs"]["decision_value"]["enum"] = ["approve", "refuse"]
    assert vocabulary_findings(_vocab("approve", "refuse"), schema) == []


def test_vocabulary_left_on_retired_word_is_flagged():
    schema = _schema()
    schema["$defs"]["decision_value"]["enum"] = ["approve", "refuse"]
    findings = vocabulary_findings(_vocab("approve_for_internal_draft", "refuse"), schema)
    assert findings and "decision vocabulary" in findings[0]
    assert "approve_for_internal_draft" in findings[0]


def test_vocabulary_missing_schema_word_is_flagged():
    schema = _schema()
    schema["$defs"]["decision_value"]["enum"] = ["approve", "refuse", "request_revision"]
    findings = vocabulary_findings(_vocab("approve", "refuse"), schema)
    assert findings and "request_revision" in findings[0]


def test_vendored_schemas_discovers_every_vendored_schema():
    names = {path.name for path in vendored_schemas()}
    assert {"mvp_governed_loop_objects.schema.yaml", "work_issue_slice.schema.yaml"} <= names
    assert all(path.name.endswith(".schema.yaml") for path in vendored_schemas())


def test_status_pin_matching_reports_no_drift():
    assert status_pin_findings(f"vendored at UPSTREAM_COMMIT {_PIN}.", _PIN) == []


def test_status_pin_missing_citation_is_flagged():
    findings = status_pin_findings("no pin cited here", _PIN)
    assert findings and "cites no UPSTREAM_COMMIT" in findings[0]
    assert _PIN in findings[0]


def test_status_pin_citing_stale_commit_is_flagged():
    findings = status_pin_findings(f"vendored at UPSTREAM_COMMIT {_OLD}.", _PIN)
    assert findings and "GOVERNANCE_STATUS.md cites" in findings[0]
    assert _OLD in findings[0]


def test_live_status_document_pin_matches_the_vendored_commit():
    """Hermetic guard against the real files: the pin GOVERNANCE_STATUS.md cites
    must equal UPSTREAM_COMMIT (the drift PR #50 left it stale once)."""
    pinned = UPSTREAM_COMMIT_FILE.read_text(encoding="utf-8").strip()
    assert status_pin_findings(STATUS_DOC_FILE.read_text(encoding="utf-8"), pinned) == []


def test_upstream_url_follows_the_schemas_convention():
    url = upstream_url_for(Path("whatever/dir/work_issue_slice.schema.yaml"))
    assert url == (
        "https://raw.githubusercontent.com/ifanjuang/Pantheon-Next/"
        "main/schemas/work_issue_slice.schema.yaml"
    )
