"""Read-only update-availability verification.

Where the family asks installed / observable / recoverable / exposed, this asks
whether a component is **current**: given a provided current version and the
latest available version, is an update available. It reports availability as data
— it goes nowhere to fetch the latest version and installs nothing (Pantheon is
not an updater). The comparison is provided-evidence-in, verdict-out.

It classifies *provided* evidence only: it performs no probe, no network fetch,
no NAS access and decides nothing. Insufficient evidence is reported as a
capability gap rather than improvised. The gate and the human decide.

Evidence shape (every field optional; all values are *provided*, never fetched)::

    component: hermes
    current_version: "1.4.2"
    available_version: "1.5.0"
    channel: stable
"""

from __future__ import annotations

import re

_READ_ONLY_NOTE = (
    "Classifies provided evidence only; performs no probe, no network fetch, no "
    "NAS access, no update, and decides nothing. The gate and the human decide."
)


def _parse_version(value):
    """Tolerant version parse: strip a leading v, drop any pre-release/build
    suffix, then read the leading integer of each dotted component. Returns a list
    of ints, or None when there is nothing to parse."""
    if not isinstance(value, str):
        return None
    text = value.strip()
    if not text:
        return None
    text = text.lstrip("vV")
    text = re.split(r"[-+ ]", text, maxsplit=1)[0]
    parts = text.split(".")
    out = []
    for part in parts:
        match = re.match(r"\d+", part)
        out.append(int(match.group()) if match else 0)
    return out or [0]


def _compare_version(a, b):
    """Return -1 / 0 / 1 comparing a to b, or None when either is unparseable."""
    pa, pb = _parse_version(a), _parse_version(b)
    if pa is None or pb is None:
        return None
    n = max(len(pa), len(pb))
    pa = pa + [0] * (n - len(pa))
    pb = pb + [0] * (n - len(pb))
    for x, y in zip(pa, pb):
        if x < y:
            return -1
        if x > y:
            return 1
    return 0


def verify_update(evidence: dict) -> dict:
    """Classify update availability from a provided current and available version
    and return the verdict as data. Read-only: it fetches nothing, updates nothing
    and decides nothing."""
    if not isinstance(evidence, dict):
        return {
            "result": "error",
            "problems": ["evidence must be a mapping of update evidence"],
            "posture": "read-only",
            "decides": False,
        }

    gaps: list[str] = []
    current = evidence.get("current_version")
    available = evidence.get("available_version")
    if not (isinstance(current, str) and current.strip()):
        gaps.append("no current version evidence ('current_version')")
    if not (isinstance(available, str) and available.strip()):
        gaps.append("no available version evidence ('available_version')")

    comparison = _compare_version(current, available)
    if comparison is None:
        verdict = "unknown"
    elif comparison == 0:
        verdict = "current"
    elif comparison < 0:
        verdict = "update_available"
    else:
        verdict = "ahead"

    return {
        "result": "ok",
        "component": str(evidence.get("component") or "unknown"),
        "current_version": current if isinstance(current, str) else None,
        "available_version": available if isinstance(available, str) else None,
        "verdict": verdict,
        "capability_gaps": gaps,
        "posture": "read-only",
        "decides": False,
        "note": _READ_ONLY_NOTE,
    }
