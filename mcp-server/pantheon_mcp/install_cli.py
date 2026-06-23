"""Read-only command-line entry point for install / liveness verification.

Classifies a component install from *provided* evidence (a YAML file or stdin) —
log / health / check results — and prints the verdict as JSON: installed,
answers, checks green, and a verdict of green / degraded / absent / unknown.
It performs no probe, no NAS access, installs nothing and decides nothing;
insufficient evidence is reported as a capability gap.

The exit code lets the command gate a script: 0 only when the verdict is
``green``; 1 otherwise (degraded / absent / unknown, or an input error). It
never reflects or performs a side effect.

Usage::

    pantheon-verify-install path/to/evidence.yaml
    cat evidence.yaml | pantheon-verify-install -
"""

from __future__ import annotations

import argparse
import json
import sys

import yaml

from . import install


def _read(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="pantheon-verify-install",
        description=(
            "Verify a component install from provided log / health / check "
            "evidence (read-only). Prints the verdict as JSON; exit 0 only when "
            "the verdict is green, 1 otherwise. It probes nothing and decides "
            "nothing."
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

    report = install.verify_install(data)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report.get("verdict") == "green" else 1


def main() -> None:
    sys.exit(run())


if __name__ == "__main__":
    main()
