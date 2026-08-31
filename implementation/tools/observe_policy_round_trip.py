#!/usr/bin/env python3
"""Observe one real chokepoint round-trip against a running policy decision point.

`WHAT_RUNS.md` recorded the internal consequential-write chokepoint as wired but
never observed: the application refuses correctly without a decision point, and
nothing showed it working with one.

This closes that by exercising the exact production path — `HttpPolicyClient`
into `enforce_consequential` — against a live `pantheon-policy-api`, and printing
the verdict. It reads only. It admits no Evidence, writes nothing, and authorizes
nothing: an allowed verdict here means the gate answered, not that any effect was
performed.

```text
gate answered != effect performed
observation != adoption
eligible != approved
```

Usage:

    # one terminal
    PANTHEON_REPO_PATH="$PWD" PANTHEON_POLICY_API_KEY=... \\
    PANTHEON_POLICY_HOST=127.0.0.1 PANTHEON_POLICY_PORT=8899 pantheon-policy-api

    # another
    MVP_POLICY_API_URL=http://127.0.0.1:8899 MVP_POLICY_API_KEY=... \\
    python implementation/tools/observe_policy_round_trip.py

Exit status is 0 when the round-trip completed and the gate returned a verdict —
allowed or refused. A refusal is a successful observation, not a failure. Only an
unreachable or misbehaving decision point exits non-zero.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
from pathlib import Path

IMPLEMENTATION = Path(__file__).resolve().parents[1]
if str(IMPLEMENTATION) not in sys.path:
    sys.path.insert(0, str(IMPLEMENTATION))

from mvp_vertical.policy_gate import HttpPolicyClient, enforce_consequential  # noqa: E402

# The exact request shape the decision point expects. Recorded here because it is
# not obvious from the client side and cost several attempts to establish:
#
#   - `request.scope` is an object with `scope_type` and `scope_id`, not a string;
#   - gate references live in `gate_signals`, a sibling of `request`, not inside it;
#   - `decision.expires_at` is an RFC 3339 string; an epoch integer is rejected.
SCOPE_TYPE = "project"


def _candidate(scope_id: str, *, with_gate_signals: bool) -> dict:
    candidate: dict = {
        "request": {
            "intent": "knowledge_update",
            "external_effect": False,
            "writes_state": True,
            "scope": {"scope_type": SCOPE_TYPE, "scope_id": scope_id},
        }
    }
    if with_gate_signals:
        candidate["gate_signals"] = {
            "task_contract_ref": "TC-observation",
            "evidence_pack_candidate_ref": "EPC-observation",
            "human_decision_ref": "dec-observation",
            "human_decision_level": "C2",
        }
    return candidate


def _decision_payload(scope_id: str, digest: str) -> dict:
    expires = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)
    return {
        "decision": {
            "decision_id": "dec-observation",
            "decided_by": "observation-operator",
            "scope": scope_id,
            "approval_level": "C2",
            "object_identity": scope_id,
            "content_digest": digest,
            "expires_at": expires.isoformat(),
        },
        "expectation": {
            "required_ceiling": "C2",
            "required_scope": scope_id,
            "object_identity": scope_id,
            "expected_digest": digest,
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base-url", default=os.getenv("MVP_POLICY_API_URL", ""))
    parser.add_argument("--api-key", default=os.getenv("MVP_POLICY_API_KEY", ""))
    parser.add_argument("--scope-id", default="observation/knowledge.sample")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    if not args.base_url or not args.api_key:
        parser.error(
            "a decision point is required: set MVP_POLICY_API_URL and MVP_POLICY_API_KEY "
            "(or pass --base-url/--api-key)"
        )

    client = HttpPolicyClient(args.base_url, args.api_key)
    digest = "sha256:" + "0" * 64
    payload = _decision_payload(args.scope_id, digest)

    observations = []
    # Both directions matter: the refusal proves the gate is not permissive by
    # default, and the allow proves the round-trip completes.
    for label, with_signals in (("without gate signals", False), ("with gate signals", True)):
        verdict = enforce_consequential(
            client, candidate=_candidate(args.scope_id, with_gate_signals=with_signals),
            decision_payload=payload,
        )
        observations.append(
            {
                "case": label,
                "allowed": verdict.allowed,
                "disposition": verdict.disposition,
                "reasons": list(verdict.reasons),
            }
        )

    unreachable = [o for o in observations if o["disposition"] == "policy_unavailable"]

    if args.format == "json":
        print(json.dumps({"observations": observations, "authority": {
            "effect_performed": False, "evidence_admitted": False, "approval_granted": False,
        }}, indent=2))
    else:
        print(f"decision point: {args.base_url}")
        for o in observations:
            print(f"\n  {o['case']}")
            print(f"    allowed     : {o['allowed']}")
            print(f"    disposition : {o['disposition']}")
            for reason in o["reasons"]:
                print(f"      - {reason}")
        print("\ngate answered != effect performed")

    if unreachable:
        print("\nthe decision point did not answer; this is not an observation", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
