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

Usage:
    python tools/check_schema_drift.py [--upstream-url URL] [--local PATH]
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCAL = ROOT / "mvp_vertical" / "vendor" / "pantheon" / "mvp_governed_loop_objects.schema.yaml"
UPSTREAM_COMMIT_FILE = ROOT / "mvp_vertical" / "vendor" / "pantheon" / "UPSTREAM_COMMIT"
UPSTREAM_REPO = "https://github.com/ifanjuang/Pantheon-Next"
DEFAULT_UPSTREAM_URL = (
    "https://raw.githubusercontent.com/ifanjuang/Pantheon-Next/main/"
    "schemas/mvp_governed_loop_objects.schema.yaml"
)


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
        # a def can itself be a scalar-with-enum (e.g. decision_value) — compare
        # its own shape signature, not only its nested properties
        for key in ("type", "enum", "const"):
            if l.get(key) != u.get(key) and (l.get(key) or u.get(key)):
                out.append(f"{name}.{key}: local={l.get(key)} upstream={u.get(key)}")
        lp, up = l.get("properties", {}), u.get("properties", {})
        newp = set(up) - set(lp)
        if newp:
            out.append(f"{name}: new properties upstream: {sorted(newp)}")
        for f in sorted(set(lp) & set(up)):
            # compare the shape signature that matters for validation
            for key in ("type", "enum", "const", "$ref"):
                if lp[f].get(key) != up[f].get(key) and (lp[f].get(key) or up[f].get(key)):
                    out.append(f"{name}.{f}.{key}: local={lp[f].get(key)} upstream={up[f].get(key)}")
            li = lp[f].get("items", {}) if isinstance(lp[f].get("items"), dict) else {}
            ui = up[f].get("items", {}) if isinstance(up[f].get("items"), dict) else {}
            for key in ("type", "$ref"):
                if li.get(key) != ui.get(key) and (li.get(key) or ui.get(key)):
                    out.append(f"{name}.{f}.items.{key}: local={li.get(key)} upstream={ui.get(key)}")
    return out


def _upstream_head_sha() -> str | None:
    try:
        r = subprocess.run(["git", "ls-remote", UPSTREAM_REPO, "main"],
                           capture_output=True, text=True, timeout=20)
        return r.stdout.split()[0] if r.returncode == 0 and r.stdout.strip() else None
    except Exception:
        return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--upstream-url", default=DEFAULT_UPSTREAM_URL)
    ap.add_argument("--local", default=str(DEFAULT_LOCAL))
    args = ap.parse_args()

    local = yaml.safe_load(Path(args.local).read_text(encoding="utf-8"))
    try:
        with urllib.request.urlopen(args.upstream_url, timeout=30) as resp:
            upstream = yaml.safe_load(resp.read().decode("utf-8"))
    except Exception as exc:  # network/availability — not drift
        print(f"SKIP: could not fetch upstream schema ({exc}). No drift asserted.")
        return 0

    pinned = UPSTREAM_COMMIT_FILE.read_text(encoding="utf-8").strip()
    head = _upstream_head_sha()
    if head and head != pinned:
        print(f"INFO: upstream HEAD {head[:12]} differs from pin {pinned[:12]} "
              "(a new commit is not itself drift — see structural check below).")
    else:
        print(f"INFO: pinned at {pinned[:12]}" + (f" (== upstream HEAD)" if head else ""))

    findings = diff_schemas(local, upstream)
    if not findings:
        print("COHERENT — vendored schema is structurally in sync with upstream.")
        return 0
    print("SCHEMA DRIFT DETECTED (vendored copy is behind upstream):")
    for f in findings:
        print("  -", f)
    print("\nAction: re-vendor the schema and reconcile emitted shapes "
          "(see the re-vendoring PR for the procedure).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
