"""CLI: ingest a dossier, run a question, record a decision, propose retention."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import register, store, terminal_gate_standin as gate
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

    p_register = sub.add_parser(
        "register",
        help="propose a Register Candidate from an approved decision (Block 3)",
    )
    p_register.add_argument("--decision-record", required=True,
                            help="YAML decision_record produced by `decide`")
    p_register.add_argument("--retention-authorized", action="store_true",
                            help="explicit human authorization to retain — required")
    p_register.add_argument("--authorized-by", required=True,
                            help="human authorizing retention; the system may not (Gate 5)")
    p_register.add_argument("--statement", required=True,
                            help="what is being registered (human-authored)")
    p_register.add_argument("--scope", required=True, help="where the statement applies")
    p_register.add_argument("--rationale", default="", help="why retention is authorized")
    p_register.add_argument("--output", help="write the register_candidate here (default: stdout)")

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

    # Retention proposal (Block 3) — no database, no perimeter. Reads a decision
    # record and proposes a register candidate; refuses unless the decision was
    # gate-produced and approved, retention is explicitly authorized, and a human
    # (never the system) authorizes it. Writes nothing durable.
    if args.command == "register":
        decision = register.load_decision_record(args.decision_record)
        try:
            candidate = register.propose_register_candidate(
                decision,
                retention_authorized=args.retention_authorized,
                statement=args.statement,
                scope=args.scope,
                authorized_by=args.authorized_by,
                rationale=args.rationale,
            )
        except register.RegisterRefusal as refusal:
            print(f"register refused: {refusal}", file=sys.stderr)
            return 1
        text = register.to_yaml(candidate)
        if args.output:
            Path(args.output).write_text(text, encoding="utf-8")
            print(f"wrote {args.output} (register_candidate)")
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
