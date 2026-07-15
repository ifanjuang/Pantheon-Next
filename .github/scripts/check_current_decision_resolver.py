#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "catalog" / "examples" / "current-decision-scenarios.json"
RESOLVER = ROOT / ".github" / "scripts" / "resolve_current_decision.py"

spec = importlib.util.spec_from_file_location("current_decision_resolver", RESOLVER)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)
resolve_current_decision = module.resolve_current_decision


def scope(resource: str = "docling"):
    return {"environment": "sandbox", "resource": resource, "preset": "docling_cpu_internal", "provisioner": "docker_compose", "one_time": True}


def decision(key: str, kind: str, effective: str, *, expires: str | None = None,
             subject: str = "handoff_candidate_docling_cpu_internal", decision_scope=None,
             supersedes: str | None = None, forced_id: str | None = None):
    rid = forced_id or f"handoff_decision_{key.replace('-', '_')}"
    field = "authorized_scope" if kind == "approve" else "reviewed_scope"
    return {
        "api_version": "pantheon.next/v0alpha1",
        "kind": "HandoffDecision",
        "metadata": {"id": rid, "created_at": effective, "status": {"approve": "approved", "refuse": "refused", "revoke": "revoked", "expire": "expired"}[kind]},
        "spec": {
            "handoff_candidate": subject,
            "decision": kind,
            "decided_by": "human_fixture",
            "decision_level": "C4",
            field: decision_scope or scope(),
            "effective_at": effective,
            "expires_at": expires if kind == "approve" else None,
            "reason": f"Fixture {key}",
            "evidence_references": [],
            "supersedes": supersedes,
        },
        "governance": {"approval_is_execution": False, "automatic_approval": False, "runtime_callback": False, "activation_authorized": False},
    }


RECORDS = {
    "approval-a": decision("approval_a", "approve", "2026-07-12T14:10:00Z", expires="2026-07-12T15:10:00Z"),
    "approval-b": decision("approval_b", "approve", "2026-07-12T14:12:00Z", expires="2026-07-12T15:12:00Z"),
    "approval-later": decision("approval_later", "approve", "2026-07-12T16:00:00Z", expires="2026-07-12T17:00:00Z"),
    "refusal-a": decision("refusal_a", "refuse", "2026-07-12T14:11:00Z"),
    "revocation-a": decision("revocation_a", "revoke", "2026-07-12T14:20:00Z", supersedes="handoff_decision_approval_a"),
    "expiration-a": decision("expiration_a", "expire", "2026-07-12T14:20:00Z", supersedes="handoff_decision_approval_a"),
    "approval-other-subject": decision("approval_other_subject", "approve", "2026-07-12T14:10:00Z", expires="2026-07-12T15:10:00Z", subject="handoff_candidate_other"),
    "approval-other-scope": decision("approval_other_scope", "approve", "2026-07-12T14:10:00Z", expires="2026-07-12T15:10:00Z", decision_scope=scope("other")),
    "approval-a-duplicate": decision("approval_a_duplicate", "approve", "2026-07-12T14:10:00Z", expires="2026-07-12T15:10:00Z", forced_id="handoff_decision_approval_a"),
    "orphan-revocation": decision("orphan_revocation", "revoke", "2026-07-12T14:20:00Z", supersedes="handoff_decision_missing"),
}


def main() -> int:
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    failures = []
    for scenario in data["scenarios"]:
        records = [RECORDS[key] for key in scenario["records"]]
        projection = resolve_current_decision(records, data["subject"], data["scope"], scenario["evaluation_time"])
        actual = projection["spec"]["outcome"]
        if actual != scenario["expected"]:
            failures.append(f"{scenario['id']}: expected {scenario['expected']}, got {actual}")
        governance = projection["governance"]
        if governance != {"read_only": True, "execution_authorized": False, "activation_authorized": False, "permission_token": False}:
            failures.append(f"{scenario['id']}: projection governance boundary changed")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"OK: {len(data['scenarios'])} deterministic current-decision scenarios passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
