"""CLI: ingest a dossier, run a question, emit candidates as YAML."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import store
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

    args = parser.parse_args()
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
