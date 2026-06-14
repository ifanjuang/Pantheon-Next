"""Read-only doctor checks.

Mirrors the governance CI so Hermes, OpenWebUI or the dashboard can ask
"are the checks green?" without running CI. The doctor verifies, cites and
flags; it never edits, fixes or decides.
"""

from __future__ import annotations

import re
from pathlib import Path

from .repo import find_repo_root

try:  # optional; the doctor degrades gracefully without them
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None

try:
    import jsonschema  # type: ignore
except Exception:  # pragma: no cover
    jsonschema = None

MANDATORY_FILES = [
    "README.md",
    "CLAUDE.md",
    "VERSION",
    "CHANGELOG.md",
    "ai_logs/README.md",
    "docs/governance/README.md",
    "docs/governance/STATUS.md",
    "docs/governance/ROADMAP.md",
    "docs/governance/GLOSSARY.md",
    "docs/governance/AUTHORITY_INDEX.md",
    "docs/governance/MODULES.md",
    "docs/governance/MEMORY.md",
    "docs/governance/APPROVALS.md",
    "docs/governance/TASK_CONTRACTS.md",
    "docs/governance/EVIDENCE_PACK.md",
]

FORBIDDEN_PHRASES = [
    "Pantheon executes",
    "Pantheon Agent Runtime",
    "Pantheon tool runtime",
    "automatic memory promotion",
    "hidden workflow runtime",
    "provider router",
    "scheduler",
    "queue",
]

# Same negation grammar as .github/workflows/governance-ci.yml.
NEGATION = re.compile(
    r"\b("
    r"must not|do not|does not|did not|is not|are not|will not|would not|"
    r"cannot|can ?not|may not|should not|shall not|must never|never|"
    r"without|forbidden|prohibited|refus(e|es|ed|al|ing)?|reject(s|ed|ion|ing)?|disallowed|denied|excluded|"
    r"incompatible|"
    r"intentionally absent|voluntarily not|not implemented|not migrated|"
    r"non implémenté|absent|avoid(s|ed|ing)?|"
    r"belongs outside|outside pantheon|on the hermes side|"
    r"stays? on the|remains? on the|stays? outside|remains? outside|"
    r"external (execution|runtime|tool|action|capability|capabilities)|"
    r"runtime state|boundary rule|stub present|"
    r"hermes-side|hermes side|"
    r"risky capabilities|risks?:|drift|"
    r"requires? (a |an )?task contract|task contract requirement|requires? approval|"
    r"remove(s|d|al)?|reformulate|transform or remove|"
    r"\bno\b|"
    r"governance[- ]only|governance-first|read[- ]only|policy[- ]gated|"
    r"not (recreate|implement|introduce|expose|grant|run|execute|"
    r"approve|own|migrate|install|schedule|queue|route|promote|"
    r"a |an |another |the )"
    r")",
    re.IGNORECASE,
)

QUEUE_OK = re.compile(
    r"review[- ]?queue|decision queue|impact[- ]?queue|"
    r"queue of governed decisions|governed (review|decision) queue",
    re.IGNORECASE,
)

RETIRED_VOCABULARY = re.compile(r"Canonical Memory|Memory Candidate")
RETIRED_OK = re.compile(
    r"formerly|former name|in place of|replaces the former|the former term",
    re.IGNORECASE,
)


def _section_context(lines: list[str], idx: int) -> str:
    start = 0
    for i in range(idx, -1, -1):
        if re.match(r"^#{1,6}\s", lines[i]):
            start = i
            break
    return "\n".join(lines[start : idx + 1])


def check_mandatory_files(root: Path | None = None) -> dict:
    root = root or find_repo_root()
    missing = [f for f in MANDATORY_FILES if not (root / f).is_file()]
    return {"check": "mandatory_files", "ok": not missing, "missing": missing}


def check_runtime_phrases(root: Path | None = None) -> dict:
    root = root or find_repo_root()
    failures = []
    for md in sorted((root / "docs" / "governance").rglob("*.md")):
        lines = md.read_text(encoding="utf-8").splitlines()
        head = "\n".join(lines[:3])
        for i, line in enumerate(lines):
            for phrase in FORBIDDEN_PHRASES:
                if re.search(r"\b" + re.escape(phrase) + r"\b", line, re.IGNORECASE):
                    ctx = _section_context(lines, i)
                    if NEGATION.search(ctx):
                        continue
                    if phrase == "queue" and (
                        QUEUE_OK.search(line) or QUEUE_OK.search(ctx) or QUEUE_OK.search(head)
                    ):
                        continue
                    failures.append(
                        {"file": str(md.relative_to(root)), "line": i + 1, "phrase": phrase}
                    )
    return {"check": "runtime_phrases", "ok": not failures, "violations": failures}


def check_retired_vocabulary(root: Path | None = None) -> dict:
    """Full-corpus scan for retired Registre Probatoire vocabulary.

    Informational: the CI guards new diffs; the doctor reports the remaining
    legacy occurrences (the issue #90 worklist). It never blocks.
    """
    root = root or find_repo_root()
    hits = []
    for md in sorted((root / "docs").rglob("*.md")):
        for i, line in enumerate(md.read_text(encoding="utf-8").splitlines()):
            if RETIRED_VOCABULARY.search(line) and not RETIRED_OK.search(line):
                hits.append({"file": str(md.relative_to(root)), "line": i + 1})
    return {
        "check": "retired_vocabulary",
        "informational": True,
        "ok": not hits,
        "remaining_occurrences": len(hits),
        "occurrences": hits,
    }


def evaluate_impact_review(data: dict) -> list[str]:
    """Apply the cascade rule to one impact_review instance.

    The rule is declarative and read-only: it never edits the review or the
    targets. It flags, it does not fix.

    - A critical-severity impact must route to arbitration. It must never be
      silently downgraded (supersede/archive/revoke/obsolete) in place.
    - A resolved review must carry a recorded decision for every target.
    """
    violations: list[str] = []
    impacted = data.get("impacted") or []
    for item in impacted:
        if not isinstance(item, dict):
            continue
        target = item.get("target_id", "?")
        severity = item.get("severity", "none")
        impact_status = item.get("impact_status", "")
        if severity == "critical" and impact_status != "critical_arbitration":
            violations.append(
                f"critical impact on {target} must be 'critical_arbitration', "
                f"found '{impact_status}' (no silent downgrade)"
            )
    if data.get("status") == "resolved":
        for item in impacted:
            if isinstance(item, dict) and item.get("decision", "pending") == "pending":
                violations.append(
                    f"impact review resolved while {item.get('target_id', '?')} "
                    f"decision is still pending"
                )
    return violations


def check_cascade_rule(root: Path | None = None) -> dict:
    """Validate impact_review instances against the schema and the cascade rule.

    Read-only. Scans known example/instance locations, validates each against
    `schemas/impact_review.schema.yaml` when jsonschema is available, then
    applies the declarative cascade rule.
    """
    root = root or find_repo_root()
    if yaml is None:
        return {
            "check": "cascade_rule",
            "ok": True,
            "informational": True,
            "note": "PyYAML unavailable; cascade rule not evaluated.",
        }

    schema = None
    schema_path = root / "schemas" / "impact_review.schema.yaml"
    if jsonschema is not None and schema_path.exists():
        try:
            schema = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
        except Exception:
            schema = None

    scan_dirs = [root / "schemas" / "examples", root / "docs" / "examples"]
    violations: list[dict] = []
    checked = 0
    for directory in scan_dirs:
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*.y*ml")):
            try:
                data = yaml.safe_load(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            if not isinstance(data, dict) or "impact_review_id" not in data:
                continue
            checked += 1
            rel = str(path.relative_to(root))
            if schema is not None:
                try:
                    jsonschema.validate(instance=data, schema=schema)
                except Exception as exc:  # validation error
                    violations.append({"file": rel, "message": f"schema invalid: {getattr(exc, 'message', str(exc))}"})
                    continue
            for message in evaluate_impact_review(data):
                violations.append({"file": rel, "message": message})

    return {
        "check": "cascade_rule",
        "ok": not violations,
        "instances_checked": checked,
        "violations": violations,
    }


def run_all(root: Path | None = None) -> dict:
    root = root or find_repo_root()
    checks = [
        check_mandatory_files(root),
        check_runtime_phrases(root),
        check_retired_vocabulary(root),
        check_cascade_rule(root),
    ]
    blocking = [c for c in checks if not c.get("informational")]
    return {
        "ok": all(c["ok"] for c in blocking),
        "checks": checks,
        "authority_note": (
            "Doctor checks verify and cite; they do not edit, fix or decide. "
            "Informational checks report state without blocking."
        ),
    }
