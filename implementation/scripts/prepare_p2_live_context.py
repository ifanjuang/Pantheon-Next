#!/usr/bin/env python3
"""Prepare one fresh synthetic P2 Execution Admission without launching Hermes.

The command is operator-only qualification support. It persists synthetic fixture
records through existing owners and stops before launch. A separate invocation of
``hermes_live_binding_acceptance.py`` is required to consume the returned
``admission_id``.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

from mvp_vertical import store
from mvp_vertical.hermes_p2_live_fixture import P2LiveFixtureError, prepare_p2_live_admission


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepare a fresh synthetic P2 A/B admission for live Hermes qualification."
    )
    parser.add_argument("--variant", choices=("A", "B"), required=True)
    parser.add_argument("--ack", default="")
    parser.add_argument(
        "--actor",
        default=os.environ.get("PANTHEON_OPERATOR_ACTOR", ""),
        help="Human operator identity; prefer PANTHEON_OPERATOR_ACTOR.",
    )
    parser.add_argument("--ttl-seconds", type=int, default=1800)
    parser.add_argument(
        "--dsn",
        default=os.environ.get("MVP_PG_DSN", ""),
        help="Optional PostgreSQL DSN; otherwise MVP_PG_DSN/default store configuration is used.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.ack != "SYNTHETIC_ONLY":
        print(
            json.dumps(
                {
                    "object_type": "p2_live_admission_preparation_error",
                    "error": "preparation requires explicit --ack SYNTHETIC_ONLY",
                    "synthetic": True,
                    "execution_started": False,
                    "technical_receipt_is_evidence": False,
                    "production_authorization": False,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 1
    if not str(args.actor or "").strip():
        print(
            json.dumps(
                {
                    "object_type": "p2_live_admission_preparation_error",
                    "error": "--actor / PANTHEON_OPERATOR_ACTOR is required",
                    "synthetic": True,
                    "execution_started": False,
                    "technical_receipt_is_evidence": False,
                    "production_authorization": False,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 1

    conn = None
    try:
        conn = store.connect(args.dsn or None)
        receipt = prepare_p2_live_admission(
            conn,
            variant=args.variant,
            actor=args.actor,
            ttl_seconds=args.ttl_seconds,
        )
        print(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (P2LiveFixtureError, ValueError, OSError) as exc:
        print(
            json.dumps(
                {
                    "object_type": "p2_live_admission_preparation_error",
                    "error": str(exc),
                    "synthetic": True,
                    "execution_started": False,
                    "technical_receipt_is_evidence": False,
                    "production_authorization": False,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 1
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
