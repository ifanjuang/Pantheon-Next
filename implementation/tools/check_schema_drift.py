#!/usr/bin/env python3
"""Schema drift monitor — is our vendored copy still coherent with upstream?

The vendored governance files are pinned to the Pantheon-Next commit recorded
in UPSTREAM_COMMIT. Upstream evolves; this tool tells us when the primary loop
schema falls behind in a way that MATTERS (structure), not merely when upstream
has any new commit.

Report-only. It is NOT part of the blocking test suite — it runs in a separate
scheduled workflow so a drift is surfaced, never used to gate a PR. The diff
logic (`diff_schemas`) is pure and network-free, and is unit-tested; only
`main()` reaches the network.

Signal:
  - structural difference (object types, required fields, property/def shapes)
    -> DRIFT, exit 1.
  - upstream HEAD sha != UPSTREAM_COMMIT -> reported as INFO only (a new commit
    upstream is not itself drift; the schema content is what matters).
  - cannot fetch upstream -> soft SKIP, exit 0 (a network hiccup is not drift).

By default it checks EVERY vendored `*.schema.yaml` (each mapped to
`schemas/<name>` upstream), so a newly vendored schema is covered automatically.

It ALSO runs one purely-local, offline check: the gate's closed decision
vocabulary (`decision_vocabulary.stand_in.yaml`) must match the vendored
schema's `$defs.decision_value` enum. That file declares the schema
authoritative if the two diverge; this makes that promise checkable instead of
a manual reconciliation the drift monitor used to miss.

Usage:
    python tools/check_schema_drift.py                 # all vendored schemas
    python tools/check_schema_drift.py --local PATH [--upstream-url URL]  # one
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
VENDOR_DIR = ROOT / "mvp_vertical" / "vendor" / "pantheon"
UPSTREAM_COMMIT_FILE = VENDOR_DIR / "UPSTREAM_COMMIT"
UPSTREAM_REPO = "https://github.com/ifanjuang/Pantheon-Next"
# Every vendored *.schema.yaml maps to schemas/<name> upstream (raw main). New
# vendored schemas are picked up automatically — no hardcoded list to forget.
UPSTREAM_RAW_BASE = "https://raw.githubusercontent.com/ifanjuang/Pantheon-Next/main/schemas/"

# The gate's closed decision vocabulary and the vendored schema that defines the
# canonical decision enum it must mirror. Both are local — the coherence check
# between them needs no network.
DECISION_VOCAB_FILE = VENDOR_DIR / "decision_vocabulary.stand_in.yaml"
DECISION_SCHEMA_FILE = VENDOR_DIR / "mvp_governed_loop_objects.schema.yaml"

# The live status document cites the vendored pin in prose. A past re-vendoring
# (PR #50) left that citation stale while UPSTREAM_COMMIT moved — a documentary
# drift the structural schema check cannot see. This offline invariant closes
# that gap: the pin GOVERNANCE_STATUS.md cites must equal UPSTREAM_COMMIT. The
# CHANGELOG intentionally keeps historical release pins and is not checked here.
STATUS_DOC_FILE = ROOT / "GOVERNANCE_STATUS.md"
_UPSTREAM_COMMIT_CITATION = re.compile(r"UPSTREAM_COMMIT\s+([0-9a-f]{40})")


def vendored_schemas() -> list[Path]:
    """Every vendored schema this repo pins, sorted for stable output."""
    return sorted(VENDOR_DIR.glob("*.schema.yaml"))


def upstream_url_for(local: Path) -> str:
    """The raw upstream URL for a vendored schema (schemas/<name> convention)."""
    return UPSTREAM_RAW_BASE + local.name


def diff_schemas(local: dict, upstream: dict) -> list[str]:
    """Pure structural diff. Returns a list of human-readable drift findings;
    empty means the vendored copy is structurally coherent with upstream."""
    out: list[str] = []

    lt = set(local.get("properties", {}).get("object_type", {}).get("enum", []))
    ut = set(upstream.get("properties", {}).get("object_type", {}).get("enum", []))
    if lt != ut:
        out.append(f"object_type enum: +upstream {sorted(ut - lt)} / -upstream {sorted(lt - ut)}")

    ld, ud = local.get("$defs", {}), upstream.get("$defs", {})
    added, removed = set(ud) - set(ld), set(ld) - set(ud)
    if added:
        out.append(f"$defs added upstream: {sorted(added)}")
    if removed:
        out.append(f"$defs removed upstream (present locally): {sorted(removed)}")

    for name in sorted(set(ld) & set(ud)):
        l, u = ld[name], ud[name]
        lr, ur = set(l.get("required", [])), set(u.get("required", []))
        if lr != ur:
            out.append(f"{name}.required: +upstream {sorted(ur - lr)} / -upstream {sorted(lr - ur)}")
        if l.get("additionalProperties") != u.get("additionalProperties"):
            out.append(f"{name}.additionalProperties: local={l.get('additionalProperties')} "
                       f"upstream={u.get('additionalProperties')}")
        for key in ("type", "enum", "const"):
            if l.get(key) != u.get(key) and (l.get(key) or u.get(key)):
                out.append(f"{name}.{key}: local={l.get(key)} upstream={u.get(key)}")
        lp, up = l.get("properties", {}), u.get("properties", {})
        newp = set(up) - set(lp)
        if newp:
            out.append(f"{name}: new properties upstream: {sorted(newp)}")
        for f in sorted(set(lp) & set(up)):
            for key in ("type", "enum", "const", "$ref"):
                if lp[f].get(key) != up[f].get(key) and (lp[f].get(key) or up[f].get(key)):
                    out.append(f"{name}.{f}.{key}: local={lp[f].get(key)} upstream={up[f].get(key)}")
            li = lp[f].get("items", {}) if isinstance(lp[f].get("items"), dict) else {}
            ui = up[f].get("items", {}) if isinstance(up[f].get("items"), dict) else {}
            for key in ("type", "$ref"):
                if li.get(key) != ui.get(key) and (li.get(key) or ui.get(key)):
                    out.append(f"{name}.{f}.items.{key}: local={li.get(key)} upstream={ui.get(key)}")
    return out


def vocabulary_findings(vocab: dict, schema: dict) -> list[str]:
    """Check that the closed decision vocabulary mirrors the vendored schema."""
    allowed = set(vocab.get("allowed_decisions", []))
    enum = set(schema.get("$defs", {}).get("decision_value", {}).get("enum", []))
    if allowed == enum:
        return []
    return [
        "decision vocabulary: allowed_decisions vs schema $defs.decision_value.enum "
        f"— only-in-vocab {sorted(allowed - enum)} / only-in-schema {sorted(enum - allowed)}"
    ]


def status_pin_findings(status_text: str, pinned: str) -> list[str]:
    """Pure, network-free check: the live status document must cite the pinned
    commit. Returns human-readable drift findings; empty means coherent.

    A missing citation is itself a finding: if the prose stops citing any
    40-char commit (deleted, shortened or reworded), the guard would otherwise
    silently pass and a later re-vendoring could recreate the stale-citation
    problem undetected. The document must carry exactly the pinned commit."""
    cited = set(_UPSTREAM_COMMIT_CITATION.findall(status_text))
    if not cited:
        return [
            "status pin: GOVERNANCE_STATUS.md cites no UPSTREAM_COMMIT commit; "
            f"it must cite the vendored pin {pinned}"
        ]
    stale = sorted(sha for sha in cited if sha != pinned)
    if not stale:
        return []
    return [
        "status pin: GOVERNANCE_STATUS.md cites UPSTREAM_COMMIT "
        f"{stale} but the vendored pin is {pinned}"
    ]


def _check_status_pin() -> bool:
    """Report-only local check. Returns True if the status pin drifted."""
    if not (STATUS_DOC_FILE.exists() and UPSTREAM_COMMIT_FILE.exists()):
        return False
    pinned = UPSTREAM_COMMIT_FILE.read_text(encoding="utf-8").strip()
    findings = status_pin_findings(STATUS_DOC_FILE.read_text(encoding="utf-8"), pinned)
    if not findings:
        print(f"  COHERENT {STATUS_DOC_FILE.name} (pin citation matches UPSTREAM_COMMIT)")
        return False
    print(f"  DRIFT {STATUS_DOC_FILE.name}:")
    for finding in findings:
        print("     -", finding)
    return True


def _check_decision_vocabulary() -> bool:
    """Report-only local check. Returns True if the vocabulary drifted."""
    if not (DECISION_VOCAB_FILE.exists() and DECISION_SCHEMA_FILE.exists()):
        return False
    vocab = yaml.safe_load(DECISION_VOCAB_FILE.read_text(encoding="utf-8"))
    schema = yaml.safe_load(DECISION_SCHEMA_FILE.read_text(encoding="utf-8"))
    findings = vocabulary_findings(vocab, schema)
    if not findings:
        print(f"  COHERENT {DECISION_VOCAB_FILE.name} (matches schema $defs.decision_value)")
        return False
    print(f"  DRIFT {DECISION_VOCAB_FILE.name}:")
    for finding in findings:
        print("     -", finding)
    return True


def _upstream_head_sha() -> str | None:
    try:
        result = subprocess.run(
            ["git", "ls-remote", UPSTREAM_REPO, "main"],
            capture_output=True,
            text=True,
            timeout=20,
        )
        return result.stdout.split()[0] if result.returncode == 0 and result.stdout.strip() else None
    except Exception:
        return None


def _check_one(local_path: Path, url: str) -> tuple[str, list[str] | None]:
    local = yaml.safe_load(local_path.read_text(encoding="utf-8"))
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            upstream = yaml.safe_load(response.read().decode("utf-8"))
    except Exception as exc:
        print(f"  SKIP {local_path.name}: could not fetch upstream ({exc})")
        return "skip", None
    findings = diff_schemas(local, upstream)
    if not findings:
        print(f"  COHERENT {local_path.name}")
        return "coherent", []
    print(f"  DRIFT {local_path.name}:")
    for finding in findings:
        print("     -", finding)
    return "drift", findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local", help="check only this one vendored schema")
    parser.add_argument("--upstream-url", help="upstream URL for --local")
    args = parser.parse_args()

    if args.local:
        pairs = [(Path(args.local), args.upstream_url or upstream_url_for(Path(args.local)))]
    else:
        pairs = [(path, upstream_url_for(path)) for path in vendored_schemas()]
    if not pairs:
        print("No vendored *.schema.yaml found — nothing to check.")
        return 0

    pinned = UPSTREAM_COMMIT_FILE.read_text(encoding="utf-8").strip()
    head = _upstream_head_sha()
    if head and head != pinned:
        print(
            f"INFO: upstream HEAD {head[:12]} differs from pin {pinned[:12]} "
            "(a new commit is not itself drift — the structural check below is what matters)."
        )
    else:
        print(f"INFO: pinned at {pinned[:12]}" + (" (== upstream HEAD)" if head else ""))
    print(f"Checking {len(pairs)} vendored schema(s):")

    drifted = False
    for local_path, url in pairs:
        state, _ = _check_one(local_path, url)
        drifted = drifted or state == "drift"

    vocabulary_drift = _check_decision_vocabulary()
    status_pin_drift = _check_status_pin()
    if drifted or vocabulary_drift or status_pin_drift:
        print(
            "\nDRIFT DETECTED — re-vendor the drifted schema(s), re-sync the "
            "decision vocabulary and/or correct the GOVERNANCE_STATUS.md pin "
            "citation, then reconcile emitted shapes "
            "(see tools/revendor.sh and the re-vendoring PR for the procedure)."
        )
        return 1
    print(
        "\nAll vendored schemas, the decision vocabulary and the status pin are "
        "in sync with upstream."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
