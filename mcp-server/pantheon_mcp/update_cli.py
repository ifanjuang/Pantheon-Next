"""Read-only command-line entry point for update-availability verification.

Classifies update availability from *provided* evidence (a YAML file or stdin) —
a current version and the latest available version — and prints the verdict as
JSON: is it current (current / update_available / ahead / unknown). It performs
no probe, no network fetch, no NAS access, no update and decides nothing;
insufficient evidence is reported as a capability gap.

The exit code lets the command gate a script: 0 only when the verdict is
``current``; 1 otherwise (update_available / ahead / unknown, or an input error).
It never reflects or performs a side effect.

Usage::

    pantheon-verify-update path/to/evidence.yaml
    cat evidence.yaml | pantheon-verify-update -
"""

from __future__ import annotations

import argparse
import json
import sys

import yaml

from . import update


def _read(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="pantheon-verify-update",
        description=(
            "Verify update availability from a provided current and available "
            "version (read-only). Prints the verdict as JSON; exit 0 only when the "
            "verdict is current, 1 otherwise. It fetches nothing, updates nothing "
            "and decides nothing."
        ),
    )
    parser.add_argument(
        "evidence",
        nargs="?",
        default="-",
        help="path to a YAML evidence file, or '-' for stdin (default: stdin)",
    )
    args = parser.parse_args(argv)

    try:
        raw = _read(args.evidence)
    except OSError as exc:
        print(json.dumps({"result": "error", "problems": [f"cannot read evidence: {exc}"]}))
        return 1

    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        print(json.dumps({"result": "error", "problems": [f"invalid YAML: {exc}"]}))
        return 1

    report = update.verify_update(data)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report.get("verdict") == "current" else 1


def main() -> None:
    sys.exit(run())


if __name__ == "__main__":
    main()
