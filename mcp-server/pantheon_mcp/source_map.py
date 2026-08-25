"""Phase 1 — canonical source map.

Each MCP resource maps to one repository file. Every answer carries the
source file, its effective authority-index labels, declared status header and
content fingerprint. The server never invents doctrine: a missing file is
reported as missing and an unindexed file stays unindexed.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from .authority_index import load_authority_catalog, resolve_authority
from .repo import find_repo_root, read_repo_text, repo_file_exists

# key -> (relative path, short title)
SOURCES: dict[str, tuple[str, str]] = {
    "status": ("docs/governance/STATUS.md", "Repository status and posture"),
    "what-runs": ("docs/governance/WHAT_RUNS.md", "Runtime-status honesty map"),
    "authority-index": ("docs/governance/AUTHORITY_INDEX.md", "Authority map"),
    "glossary": ("docs/governance/GLOSSARY.md", "Vocabulary and the four axes (E/V/K/C)"),
    "architecture": ("docs/governance/ARCHITECTURE.md", "Pantheon architecture boundary"),
    "modules": ("docs/governance/MODULES.md", "Governance module map"),
    "capability-placement": ("docs/governance/CAPABILITY_PLACEMENT.md", "Where capabilities live"),
    "capability-registry": (
        "docs/governance/CAPABILITY_REGISTRY.md",
        "Governed capability declaration model",
    ),
    "uniform-capability-governance": (
        "docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md",
        "One law, one passport, the chokepoint",
    ),
    "task-contracts": ("docs/governance/TASK_CONTRACTS.md", "Task Contract doctrine"),
    "evidence-pack": ("docs/governance/EVIDENCE_PACK.md", "Evidence Pack doctrine"),
    "approvals": ("docs/governance/APPROVALS.md", "Approval ceilings C0-C5"),
    "memory": ("docs/governance/MEMORY.md", "Hermes memory vs Registre Probatoire"),
    "registre-probatoire": (
        "docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md",
        "Registre Probatoire central doc",
    ),
    "knowledge-ingestion-memory": (
        "docs/governance/KNOWLEDGE_INGESTION_AND_MEMORY.md",
        "Knowledge ingestion and memory boundary",
    ),
    "source-ingestion-retrieval": (
        "docs/governance/SOURCE_INGESTION_RETRIEVAL_MODEL.md",
        "Source ingestion and retrieval model",
    ),
    "answer-verification-gate": (
        "docs/governance/ANSWER_VERIFICATION_GATE.md",
        "Answer verification (V) and consequence (K)",
    ),
    "user-decision-gate": ("docs/governance/USER_DECISION_GATE.md", "Escalation to the human"),
    "target-architecture": ("docs/governance/TARGET_ARCHITECTURE.md", "Coherence compass"),
    "domain-pack-spec": ("docs/governance/DOMAIN_PACK_SPEC.md", "Domain pack specification"),
    "preflight": (
        "docs/governance/MODULE_INVOCATION_PREFLIGHT.md",
        "Invocation and connectivity preflight",
    ),
    "mcp-boundary": (
        "mcp-server/docs/HTTP_API_CONTRACT.md",
        "Implemented Pantheon policy service boundary",
    ),
    "hermes-runtime-governance": (
        "docs/governance/HERMES_RUNTIME_GOVERNANCE.md",
        "Hermes runtime governance projection",
    ),
    "openwebui-integration": (
        "docs/governance/OPENWEBUI_INTEGRATION.md",
        "OpenWebUI exposure boundary",
    ),
    "control-boundary": (
        "docs/governance/PANTHEON_CONTROL_BOUNDARY.md",
        "Pantheon Control boundary (dashboard/)",
    ),
    "control-plane-boundary": (
        "docs/governance/PANTHEON_CONTROL_PLANE_BOUNDARY.md",
        "Pantheon Control operational-state boundary",
    ),
    "passport-template": ("templates/mcp_capability_passport.yaml", "Capability passport template"),
}

STRUCTURE_SECTIONS: tuple[dict, ...] = (
    {
        "key": "orientation",
        "title": "Orientation and authority",
        "reason": (
            "Locate the repository posture, controlled vocabulary, governance "
            "areas and the authority that may be relied upon."
        ),
        "sources": ("status", "authority-index", "glossary", "modules"),
    },
    {
        "key": "delegation-and-decision",
        "title": "Delegation and decision boundaries",
        "reason": (
            "Separate bounded Hermes execution from evidence, approval and "
            "explicit human escalation."
        ),
        "sources": (
            "task-contracts",
            "evidence-pack",
            "approvals",
            "user-decision-gate",
        ),
    },
    {
        "key": "truth-and-records",
        "title": "Truth, verification and governed records",
        "reason": (
            "Keep runtime memory non-authoritative while making consequential "
            "claims traceable and reviewable."
        ),
        "sources": (
            "memory",
            "registre-probatoire",
            "knowledge-ingestion-memory",
            "source-ingestion-retrieval",
            "answer-verification-gate",
        ),
    },
    {
        "key": "capabilities-and-architecture",
        "title": "Capabilities and architecture",
        "reason": (
            "Place capabilities in the correct layer and expose their governed "
            "admission contract without turning Pantheon into a runtime."
        ),
        "sources": (
            "capability-placement",
            "capability-registry",
            "uniform-capability-governance",
            "target-architecture",
            "domain-pack-spec",
            "preflight",
            "control-plane-boundary",
            "passport-template",
        ),
    },
    {
        "key": "policy-interface",
        "title": "Read-only policy interface",
        "reason": (
            "Give Hermes a traceable view of governance while preserving the "
            "one-way boundary: Pantheon governs and Hermes executes."
        ),
        "sources": (
            "mcp-boundary",
            "hermes-runtime-governance",
            "openwebui-integration",
            "control-boundary",
        ),
    },
)


def load_authority_index(root: Path | None = None) -> dict[str, dict[str, str]]:
    """Compatibility view of exact rows across the effective authority map."""
    root = root or find_repo_root()
    catalog = load_authority_catalog(root)
    return {
        record["path"]: {
            "authority": record["authority"],
            "status": record["repo_state"],
            "source_index": record["source_index"],
            "source_line": record["source_line"],
        }
        for record in catalog["records"]
    }


_STATUS_HEADER = re.compile(r"^Status:\s*(?P<status>.+?)\s*$", re.MULTILINE)


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


def repository_version(root: Path | None = None) -> str:
    """Return the declared repository release version, or ``unknown``."""
    root = root or find_repo_root()
    try:
        return read_repo_text("VERSION", root).strip() or "unknown"
    except FileNotFoundError:
        return "unknown"


def describe_source(
    key: str,
    root: Path | None = None,
    *,
    catalog: dict | None = None,
) -> dict:
    """Return the governed description of one source, without its body."""
    root = root or find_repo_root()
    if key not in SOURCES:
        return {
            "key": key,
            "error": "unknown source key",
            "known_keys": sorted(SOURCES),
        }
    rel, title = SOURCES[key]
    resolution = resolve_authority(rel, catalog or load_authority_catalog(root))
    exists = repo_file_exists(rel, root)
    info = {
        "uri": f"pantheon://{key}",
        "title": title,
        "source_file": rel,
        "exists": exists,
        "authority": resolution["authority"],
        "status": resolution["repo_state"],
        "authority_resolution": resolution["resolution"],
        "authority_ok": resolution["resolution"] == "resolved",
        "authority_source": {
            "index": resolution["source_index"],
            "line": resolution["source_line"],
            "entry": resolution["entry"],
            "matched_path": resolution.get("matched_path"),
            "match_type": resolution.get("match_type"),
        },
        "authority_diagnostics": resolution["diagnostics"],
    }
    if exists:
        text = read_repo_text(rel, root)
        status_header = _STATUS_HEADER.search(text)
        info["declared_status"] = (
            status_header.group("status") if status_header else "not declared"
        )
        info["content_sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
        info["summary"] = _first_paragraph(text)
    else:
        info["declared_status"] = "not available"
        info["content_sha256"] = None
        info["summary"] = (
            "source file absent in this checkout; "
            "treat as documented elsewhere or pending"
        )
    return info


def read_source(key: str, root: Path | None = None) -> dict:
    """Return one source with its full body, labeled with authority/status."""
    info = describe_source(key, root)
    if info.get("exists"):
        info["body"] = read_repo_text(SOURCES[key][0], root)
    return info


def list_sources(root: Path | None = None) -> list[dict]:
    root = root or find_repo_root()
    catalog = load_authority_catalog(root)
    return [describe_source(k, root, catalog=catalog) for k in sorted(SOURCES)]


def explain_structure(key: str = "", root: Path | None = None) -> dict:
    """Explain the governed document structure without creating new doctrine."""
    root = root or find_repo_root()
    if key and key not in SOURCES:
        return {
            "key": key,
            "error": "unknown source key",
            "known_keys": sorted(SOURCES),
        }

    sections = [
        {
            **section,
            "sources": [
                {
                    "key": source_key,
                    "title": SOURCES[source_key][1],
                    "uri": f"pantheon://{source_key}",
                }
                for source_key in section["sources"]
            ],
        }
        for section in STRUCTURE_SECTIONS
        if not key or key in section["sources"]
    ]
    response = {
        "purpose": (
            "Read-only governance wiki for Hermes: locate a rule, understand why "
            "it sits in the structure, then follow its traced repository source."
        ),
        "boundary": {
            "exposure": "OpenWebUI exposes",
            "execution": "Hermes executes",
            "governance": "Pantheon governs",
            "effect": "informational only; this response grants no authority",
        },
        "sections": sections,
    }
    if key:
        response["focus"] = describe_source(key, root)
    return response
