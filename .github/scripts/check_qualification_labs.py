#!/usr/bin/env python3
"""What each qualification lab blocks merges for, and what it actually tests.

Seventeen workflows check out an external project and run it. They cost a
maintenance stream that grows with every upstream release, and they return that
cost only where a red result would change a decision. Two questions decide
whether a lab earns its place, and neither was asked anywhere:

    which decision would be taken differently if this failed?
    is the thing it tests the thing the registry says we qualified?

This check does not answer the first — that is an arbitration, and it belongs to
a human. It makes the answer enumerable: a lab that blocks merges without naming
the decision it guards is counted, and the count is capped so the backlog shrinks
deliberately instead of growing.

The second question it does answer, mechanically. A lab either resolves its
external targets from `external-pins.json` at run time, or hardcodes them. A
hardcoded target that has drifted from the registry means the lab qualifies a
combination the repository no longer claims to have qualified — while its green
tick reads exactly like one that does. Each hardcoded target must be declared,
so a new one cannot appear unnoticed, and drift is reported against a cap.

    lab green            != qualification
    blocking             != guards a decision
    hardcoded target     != frozen deliberately
    frozen deliberately  != still current
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / ".github" / "workflows"
REGISTRY = ROOT / ".github" / "qualification-labs.json"
PINS = ROOT / "implementation" / "qualification" / "external-pins.json"

PIN_EXPORT = "export_external_qualification_pins.py"
OWN_REPOSITORY = "Pantheon-Next"

# An env value naming an external target, as opposed to fixture configuration.
TARGET_KEY = re.compile(r"_(COMMIT|REF|VERSION|BLOB)$")


def _triggers(document: dict) -> set[str]:
    # PyYAML reads a bare `on:` key as the boolean True.
    raw = document.get("on", document.get(True))
    if isinstance(raw, dict):
        return set(raw)
    if isinstance(raw, list):
        return set(raw)
    return {str(raw)} if raw else set()


def _external_checkouts(document: dict) -> set[str]:
    found: set[str] = set()
    for job in (document.get("jobs") or {}).values():
        for step in job.get("steps") or []:
            uses = step.get("uses")
            if not isinstance(uses, str) or not uses.startswith("actions/checkout"):
                continue
            repository = (step.get("with") or {}).get("repository")
            if repository and OWN_REPOSITORY not in str(repository):
                found.add(str(repository))
    return found


def _literal_env(document: dict) -> dict[str, str]:
    values: dict[str, str] = {}
    for job in (document.get("jobs") or {}).values():
        values.update(job.get("env") or {})
    values.update(document.get("env") or {})
    return {
        key: value
        for key, value in values.items()
        if isinstance(value, str) and "${{" not in value and TARGET_KEY.search(key)
    }


def discover(workflows: Path) -> dict[str, dict]:
    """Every workflow that runs somebody else's project."""
    labs: dict[str, dict] = {}
    for path in sorted(workflows.glob("*.yml")):
        raw = path.read_text(encoding="utf-8")
        document = yaml.safe_load(raw)
        external = _external_checkouts(document)
        resolves = PIN_EXPORT in raw
        if not external and not resolves:
            continue
        triggers = _triggers(document)
        labs[path.name] = {
            "workflow": path.name,
            "name": document.get("name", path.stem),
            "blocking": "pull_request" in triggers,
            "resolves_from_registry": resolves,
            "external": sorted(external),
            "literal_targets": _literal_env(document),
        }
    return labs


def pin_values(pins: dict) -> dict[str, str]:
    """Pin id -> the identifier a lab would pin itself to."""
    values: dict[str, str] = {}
    for identifier, pin in (pins.get("pins") or {}).items():
        value = pin.get("ref") or pin.get("version")
        if value:
            values[identifier] = str(value)
    return values


def verify(labs: dict[str, dict], registry: dict, pins: dict) -> tuple[list[str], list[dict]]:
    errors: list[str] = []
    entries = {str(entry.get("workflow", "")): entry for entry in registry.get("labs", [])}
    known = pin_values(pins)
    rows: list[dict] = []

    for name in sorted(set(labs) - set(entries)):
        errors.append(f"{name} runs an external project and has no entry here")
    for name in sorted(set(entries) - set(labs)):
        errors.append(f"{name} has an entry here but is no longer a qualification lab")

    for name, lab in sorted(labs.items()):
        entry = entries.get(name)
        if entry is None:
            continue
        declared = entry.get("targets") or {}
        drift: list[str] = []
        untracked: list[str] = []

        for key, value in sorted(lab["literal_targets"].items()):
            if key not in declared:
                errors.append(
                    f"{name}: env {key} pins an external target that is not declared "
                    "here; declare the registry pin it corresponds to, or null with "
                    "a reason if it is not an external target"
                )
                continue
            pin_id = declared[key]
            if pin_id is None:
                untracked.append(f"{key}={value[:12]}")
                continue
            if pin_id not in known:
                errors.append(f"{name}: {key} names pin {pin_id!r}, which the registry does not define")
                continue
            if not known[pin_id].startswith(value) and not value.startswith(known[pin_id]):
                drift.append(f"{key}={value[:12]} vs {pin_id}={known[pin_id][:12]}")

        for key in sorted(declared):
            if key not in lab["literal_targets"]:
                errors.append(f"{name}: declares target {key}, which the workflow no longer pins")

        rows.append(
            {
                "workflow": name,
                "label": entry.get("id") or lab["name"],
                "blocking": lab["blocking"],
                "from_registry": lab["resolves_from_registry"],
                "drift": drift,
                "untracked": untracked,
                "guards": entry.get("guards"),
            }
        )

    undeclared = [row for row in rows if row["blocking"] and not row["guards"]]
    ceiling = registry.get("blocking_without_declared_decision_ceiling")
    if isinstance(ceiling, int) and len(undeclared) > ceiling:
        errors.append(
            f"{len(undeclared)} labs block merges without naming the decision they "
            f"guard; the ceiling is {ceiling}. Name the decision, or take the lab "
            "off pull_request."
        )

    drifting = [row for row in rows if row["drift"]]
    drift_ceiling = registry.get("frozen_target_drift_ceiling")
    if isinstance(drift_ceiling, int) and len(drifting) > drift_ceiling:
        errors.append(
            f"{len(drifting)} labs qualify a target the registry no longer pins; the "
            f"ceiling is {drift_ceiling}. Re-point the lab, or stop letting its green "
            "read as a current qualification."
        )

    return errors, rows


def render(rows: list[dict], registry: dict) -> str:
    blocking = [row for row in rows if row["blocking"]]
    undeclared = [row for row in blocking if not row["guards"]]
    drifting = [row for row in rows if row["drift"]]

    out = [
        "# Qualification labs",
        "",
        f"{len(rows)} workflows run an external project. {len(blocking)} of them "
        "block merges.",
        "",
        f"- blocking without naming the decision they guard: **{len(undeclared)}**"
        + (
            f" (ceiling {registry['blocking_without_declared_decision_ceiling']})"
            if "blocking_without_declared_decision_ceiling" in registry
            else ""
        ),
        f"- qualifying a target the registry no longer pins: **{len(drifting)}**"
        + (
            f" (ceiling {registry['frozen_target_drift_ceiling']})"
            if "frozen_target_drift_ceiling" in registry
            else ""
        ),
        "",
        "Whether a lab earns a blocking slot is an arbitration, not an audit "
        "result. This report says which ones have not had it yet.",
        "",
        "| Lab | Blocks merges | Targets from | Decision it guards |",
        "|---|---|---|---|",
    ]
    for row in rows:
        source = "registry" if row["from_registry"] else "hardcoded"
        if row["drift"]:
            source += " ⚠ drifted"
        out.append(
            f"| `{row['label']}` | {'yes' if row['blocking'] else 'dispatch only'} | "
            f"{source} | {row['guards'] or '— not arbitrated —'} |"
        )

    if drifting:
        out += ["", "## Qualifying something the registry does not pin", ""]
        for row in drifting:
            out.append(f"- `{row['label']}` — " + "; ".join(row["drift"]))

    untracked = [row for row in rows if row["untracked"]]
    if untracked:
        out += [
            "",
            "## Pinned outside the registry",
            "",
            "Declared as not corresponding to a registry pin. Each is an external "
            "identifier the qualification registry does not govern.",
            "",
        ]
        for row in untracked:
            out.append(f"- `{row['label']}` — " + ", ".join(row["untracked"]))
    out.append("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    parser.add_argument("--workflows", type=Path, default=WORKFLOWS)
    parser.add_argument("--pins", type=Path, default=PINS)
    args = parser.parse_args()

    labs = discover(args.workflows)
    registry = json.loads(args.registry.read_text(encoding="utf-8"))
    pins = json.loads(args.pins.read_text(encoding="utf-8"))
    errors, rows = verify(labs, registry, pins)

    report = render(rows, registry)
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(report + "\n")

    if errors:
        print("\nQualification labs are not fully accounted for:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
