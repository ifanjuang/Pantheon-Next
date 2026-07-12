#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "catalog" / "schemas"
EXAMPLE = ROOT / "catalog" / "examples" / "docling-handoff-decision.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def parse_dt(value: str | None):
    if value is None:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def main() -> int:
    handoff_schema = load(SCHEMA_DIR / "provisioner-handoff-candidate.schema.json")
    decision_schema = load(SCHEMA_DIR / "handoff-decision.schema.json")
    data = load(EXAMPLE)

    Draft202012Validator(handoff_schema, format_checker=FormatChecker()).validate(data["handoff_candidate"])
    validator = Draft202012Validator(decision_schema, format_checker=FormatChecker())
    validator.validate(data["approval"])
    validator.validate(data["revocation"])

    handoff = data["handoff_candidate"]
    approval = data["approval"]
    revocation = data["revocation"]

    handoff_id = handoff["metadata"]["id"]
    if approval["spec"]["handoff_candidate"] != handoff_id:
        raise SystemExit("approval does not reference the handoff candidate")
    if revocation["spec"]["handoff_candidate"] != handoff_id:
        raise SystemExit("revocation does not reference the handoff candidate")
    if revocation["spec"]["supersedes"] != approval["metadata"]["id"]:
        raise SystemExit("revocation must supersede the approval")

    scope = approval["spec"]["authorized_scope"]
    if scope["provisioner"] != handoff["spec"]["selected_provisioner"]:
        raise SystemExit("approved provisioner differs from the handoff candidate")
    if scope["one_time"] is not True:
        raise SystemExit("handoff approval must remain one-time")

    effective = parse_dt(approval["spec"]["effective_at"])
    expires = parse_dt(approval["spec"]["expires_at"])
    if expires is None or expires <= effective:
        raise SystemExit("approved handoff must expire after it becomes effective")

    if approval["spec"]["decision_level"] not in {"C4", "C5"}:
        raise SystemExit("provisioner handoff approval requires C4 or C5")
    if approval["governance"]["activation_authorized"]:
        raise SystemExit("handoff approval must not authorize activation")
    if approval["governance"]["approval_is_execution"]:
        raise SystemExit("approval must not be represented as execution")
    if approval["governance"]["automatic_approval"]:
        raise SystemExit("automatic approval is forbidden")
    if revocation["spec"]["effective_at"] <= approval["spec"]["effective_at"]:
        raise SystemExit("revocation must occur after approval")

    print("OK: handoff human decision contracts are valid and bounded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
