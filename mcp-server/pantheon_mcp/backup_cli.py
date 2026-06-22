"""Read-only command-line entry point for backup / recoverability verification.

Classifies a component's backup posture from *provided* evidence (a YAML file or
stdin) — backup presence, freshness and a demonstrated restore — and prints the
verdict as JSON: if it dies, can we get it back (protected / degraded /
unprotected / unknown). It performs no probe, no NAS access, runs no backup or
restore and decides nothing; insufficient evidence is reported as a capability
gap.

The exit code lets the command gate a script: 0 only when the verdict is
``protected``; 1 otherwise (degraded / unprotected / unknown, or an input
error). It never reflects or performs a side effect.

Usage::

    pantheon-verify-backup path/to/evidence.yaml
    cat evidence.yaml | pantheon-verify-backup -
"""

from __future__ import annotations

import argparse
import json
import sys

import yaml

from . import backup


def _read(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="pantheon-verify-backup",
        description=(
            "Verify a component's backup / recoverability posture from provided "
            "backup / freshness / restore evidence (read-only). Prints the verdict "
            "as JSON; exit 0 only when the verdict is protected, 1 otherwise. It "
            "runs nothing and decides nothing."
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

    report = backup.verify_backup(data)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report.get("verdict") == "protected" else 1


def main() -> None:
    sys.exit(run())


if __name__ == "__main__":
    main()
