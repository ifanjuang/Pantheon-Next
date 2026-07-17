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

from tools.check_schema_drift import diff_schemas


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
                "required": ["phrase", "risk"], "additionalProperties": False,
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
    up = _schema()
    up["$defs"]["decision_record"]["required"].append("decision_id")
    findings = diff_schemas(_schema(), up)
    assert any("decision_record.required" in f and "decision_id" in f for f in findings)


def test_new_object_type_upstream_is_flagged():
    up = _schema()
    up["properties"]["object_type"]["enum"].append("register_candidate")
    findings = diff_schemas(_schema(), up)
    assert any("object_type enum" in f and "register_candidate" in f for f in findings)


def test_new_def_upstream_is_flagged():
    up = _schema()
    up["$defs"]["grounding_review"] = {"required": ["note"]}
    findings = diff_schemas(_schema(), up)
    assert any("$defs added upstream" in f and "grounding_review" in f for f in findings)


def test_property_items_shape_change_is_flagged():
    # exactly the commitment_flags string-vs-object drift this session hit
    local = _schema()
    local["$defs"]["result_candidate"] = {
        "properties": {"commitment_flags": {"type": "array", "items": {"type": "string"}}}}
    up = _schema()
    up["$defs"]["result_candidate"] = {
        "properties": {"commitment_flags": {"type": "array", "items": {"$ref": "#/$defs/commitment_flag"}}}}
    findings = diff_schemas(local, up)
    assert any("commitment_flags.items" in f for f in findings)


def test_enum_change_is_flagged():
    up = _schema()
    up["$defs"]["decision_value"]["enum"].append("request_revision")
    findings = diff_schemas(_schema(), up)
    assert any("decision_value.enum" in f for f in findings)
