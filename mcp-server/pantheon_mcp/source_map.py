"""Phase 1 — canonical source map.

Each MCP resource maps to one repository file. Every answer carries the
source file, its authority and status as declared by AUTHORITY_INDEX.md.
The server never invents doctrine: a missing file is reported as missing,
a candidate document is reported as candidate.
"""

from __future__ import annotations

import re
from pathlib import Path

from .repo import find_repo_root, read_repo_text, repo_file_exists

# key -> (relative path, short title)
SOURCES: dict[str, tuple[str, str]] = {
    "status": ("docs/governance/STATUS.md", "Repository status and posture"),
    "authority-index": ("docs/governance/AUTHORITY_INDEX.md", "Authority map"),
    "glossary": ("docs/governance/GLOSSARY.md", "Vocabulary and the four axes (E/V/K/C)"),
    "modules": ("docs/governance/MODULES.md", "Governance module map"),
    "capability-placement": ("docs/governance/CAPABILITY_PLACEMENT.md", "Where capabilities live"),
    "uniform-capability-governance": ("docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md", "One law, one passport, the chokepoint"),
    "task-contracts": ("docs/governance/TASK_CONTRACTS.md", "Task Contract doctrine"),
    "evidence-pack": ("docs/governance/EVIDENCE_PACK.md", "Evidence Pack doctrine"),
    "approvals": ("docs/governance/APPROVALS.md", "Approval ceilings C0-C5"),
    "memory": ("docs/governance/MEMORY.md", "Hermes memory vs Registre Probatoire"),
    "registre-probatoire": ("docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md", "Registre Probatoire central doc"),
    "answer-verification-gate": ("docs/governance/ANSWER_VERIFICATION_GATE.md", "Answer verification (V) and consequence (K)"),
    "user-decision-gate": ("docs/governance/USER_DECISION_GATE.md", "Escalation to the human"),
    "target-architecture": ("docs/governance/TARGET_ARCHITECTURE.md", "Coherence compass"),
    "domain-pack-spec": ("docs/governance/DOMAIN_PACK_SPEC.md", "Domain pack specification"),
    "preflight": ("docs/governance/MODULE_INVOCATION_PREFLIGHT.md", "Invocation and connectivity preflight"),
    "mcp-boundary": ("docs/governance/MCP_POLICY_SERVER_CANDIDATE.md", "MCP policy plane boundary"),
    "mcp-development": ("docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md", "MCP development roadmap"),
    "control-boundary": ("docs/governance/PANTHEON_CONTROL_BOUNDARY.md", "Pantheon Control boundary (dashboard/)"),
    "passport-template": ("templates/mcp_capability_passport.yaml", "Capability passport template"),
}

_ROW = re.compile(r"^\|\s*`(?P<path>[^`]+)`\s*\|\s*(?P<authority>[^|]+)\|\s*(?P<status>[^|]+)\|")


def load_authority_index(root: Path | None = None) -> dict[str, dict[str, str]]:
    """Parse the AUTHORITY_INDEX.md table into {path: {authority, status}}."""
    root = root or find_repo_root()
    out: dict[str, dict[str, str]] = {}
    try:
        text = read_repo_text(SOURCES["authority-index"][0], root)
    except FileNotFoundError:
        return out
    for line in text.splitlines():
        m = _ROW.match(line.strip())
        if m:
            out[m.group("path").strip()] = {
                "authority": m.group("authority").strip(),
                "status": m.group("status").strip(),
            }
    return out


def _first_paragraph(text: str) -> str:
    lines = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("#") or not s:
            if lines:
                break
            continue
        lines.append(s)
        if len(lines) >= 2:
            break
    return " ".join(lines)[:400]


def describe_source(key: str, root: Path | None = None) -> dict:
    """Return the governed description of one source, without its body."""
    root = root or find_repo_root()
    if key not in SOURCES:
        return {"key": key, "error": "unknown source key", "known_keys": sorted(SOURCES)}
    rel, title = SOURCES[key]
    index = load_authority_index(root)
    entry = index.get(rel, {})
    exists = repo_file_exists(rel, root)
    info = {
        "uri": f"pantheon://{key}",
        "title": title,
        "source_file": rel,
        "exists": exists,
        "authority": entry.get("authority", "not indexed"),
        "status": entry.get("status", "not indexed"),
    }
    if exists:
        info["summary"] = _first_paragraph(read_repo_text(rel, root))
    else:
        info["summary"] = "source file absent in this checkout; treat as documented elsewhere or pending"
    return info


def read_source(key: str, root: Path | None = None) -> dict:
    """Return one source with its full body, labeled with authority/status."""
    info = describe_source(key, root)
    if info.get("exists"):
        info["body"] = read_repo_text(SOURCES[key][0], root)
    return info


def list_sources(root: Path | None = None) -> list[dict]:
    return [describe_source(k, root) for k in sorted(SOURCES)]
