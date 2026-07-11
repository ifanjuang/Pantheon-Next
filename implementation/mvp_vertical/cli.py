"""CLI: ingest a dossier, run a question, record a human decision."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import store, terminal_gate_standin as gate
from .contract import load_contract
from .runner import run


def main() -> int:
    parser = argparse.ArgumentParser(prog="mvp-vertical")
    sub = parser.add_subparsers(dest="command", required=True)

    p_ingest = sub.add_parser("ingest", help="ingest the contract's declared sources")
    p_ingest.add_argument("--contract", required=True)
    p_ingest.add_argument("--root", default=".")

    p_run = sub.add_parser("run", help="answer a question inside the contract's perimeter")
    p_run.add_argument("--contract", required=True)
    p_run.add_argument("--question", required=True)
    p_run.add_argument("--output", help="write the YAML stream here (default: stdout)")

    p_decide = sub.add_parser(
        "decide",
        help="record a HUMAN decision on a candidate stream (terminal gate stand-in)",
    )
    p_decide.add_argument("--candidates", required=True, help="YAML stream produced by `run`")
    p_decide.add_argument("--decision", required=True,
                          help="approve | refuse | request_revision | request_more_evidence")
    p_decide.add_argument("--decided-by", required=True,
                          help="human identity; the system may not sign (Gate 5)")
    p_decide.add_argument("--rationale", default="")
    p_decide.add_argument("--output", help="write the decision_record here (default: stdout)")

    args = parser.parse_args()

    # The decision gate touches no database and no contract perimeter — it only
    # records a human choice on an existing candidate stream.
    if args.command == "decide":
        documents = gate.load_candidates(args.candidates)
        try:
            record = gate.record_decision(
                documents,
                decision=args.decision,
                decided_by=args.decided_by,
                rationale=args.rationale,
            )
        except gate.GateRefusal as refusal:
            # A refusal is a first-class governance outcome, not a crash.
            print(f"gate refused: {refusal}", file=sys.stderr)
            return 1
        text = gate.to_yaml(record)
        if args.output:
            Path(args.output).write_text(text, encoding="utf-8")
            print(f"wrote {args.output} (decision_record: {record['decision']})")
        else:
            sys.stdout.write(text)
        return 0

    contract = load_contract(args.contract)
    conn = store.connect()
    try:
        if args.command == "ingest":
            n = store.ingest(conn, contract, Path(args.root))
            print(f"ingested {n} chunks from {len(contract.sources)} declared sources")
            return 0
        output = run(conn, contract, args.question)
        text = output.to_yaml()
        if args.output:
            Path(args.output).write_text(text, encoding="utf-8")
            print(f"wrote {args.output} ({output.kind})")
        else:
            sys.stdout.write(text)
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
