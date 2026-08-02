#!/usr/bin/env python3
"""Cross-repository architecture audit for Pantheon-Next and pantheon-mvp.

The audit is report-only. It identifies architecture convergence candidates,
but never renames, moves or deletes an artifact.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

ARCHITECTURE_SUFFIXES = {
    ".py", ".json", ".yaml", ".yml", ".md", ".sql", ".js", ".css",
    ".html", ".toml", ".sh",
}
EXCLUDED_PARTS = {
    ".git", ".pytest_cache", ".venv", "venv", "__pycache__", "node_modules",
    "dist", "build",
}
GENERATION_PATH_TOKEN = re.compile(r"(?:^|[_./-])v\d+(?:$|[_./-])", re.IGNORECASE)
GENERATION_IDENTITY_TOKEN = re.compile(
    r"(?:/v\d+(?=/)|\b[a-z][a-z0-9_-]*[_-]v\d+\b|\bv\d+[_-][a-z][a-z0-9_-]*\b)",
    re.IGNORECASE,
)
COMPATIBILITY_PATH_TOKEN = re.compile(
    r"(?:^|[_./-])(?:legacy|compat(?:ibility)?|deprecated|obsolete|old)(?:$|[_./-])",
    re.IGNORECASE,
)
RUNTIME_BOUNDARY_PATTERNS = {
    "scheduler": re.compile(r"\bschedul(?:er|ing)\b", re.IGNORECASE),
    "queue": re.compile(r"\bqueue(?:d|s|ing)?\b", re.IGNORECASE),
    "provider_router": re.compile(r"\bprovider[_ -]?rout(?:er|ing)\b", re.IGNORECASE),
    "plugin_manager": re.compile(r"\bplugin[_ -]?manager\b", re.IGNORECASE),
    "memory_engine": re.compile(r"\bmemory[_ -]?engine\b", re.IGNORECASE),
    "automatic_approval": re.compile(r"\b(?:automatic|auto)[_ -]?approv(?:al|e)\b", re.IGNORECASE),
}
HISTORICAL_PARTS = {"ai_logs", "archive", "archives", "history"}
REFERENCE_PARTS = {"vendor", "vendored", "fixtures", "examples"}
PROJECTION_PARTS = {"cockpit", "openwebui"}
PRIORITY_ORDER = {f"P{number}": number for number in range(6)}


@dataclass(frozen=True)
class RepositorySpec:
    name: str
    role: str
    root: Path


@dataclass(frozen=True)
class ConceptRule:
    concept_id: str
    label: str
    canonical_owner: str
    patterns: tuple[str, ...]
    max_active_implementations: int = 4
    max_authority_definitions: int = 8


@dataclass(frozen=True)
class OwnershipRegistry:
    registry_id: str
    revision: int
    concepts: tuple[ConceptRule, ...]


@dataclass(frozen=True)
class Artifact:
    repository: str
    repository_role: str
    path: str
    suffix: str
    stem: str
    lines: int
    bytes: int
    meaningful: bool
    digest: str
    posture: str
    generation_named: bool
    generation_identities: tuple[str, ...]
    compatibility_named: bool
    concepts: tuple[str, ...]
    runtime_boundary_terms: tuple[str, ...]


@dataclass(frozen=True)
class Finding:
    finding_id: str
    priority: str
    category: str
    subject: str
    canonical_owner: str | None
    recommendation: str
    artifacts: tuple[str, ...]
    review_state: str = "unreviewed"


def repository_spec(value: str) -> RepositorySpec:
    try:
        name, role, raw_root = value.split("=", 2)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("expected NAME=ROLE=PATH") from exc
    root = Path(raw_root).expanduser().resolve()
    if not root.is_dir():
        raise argparse.ArgumentTypeError(f"repository root does not exist: {root}")
    return RepositorySpec(name=name, role=role, root=root)


def load_registry(path: Path) -> OwnershipRegistry:
    payload = json.loads(path.read_text(encoding="utf-8"))
    revision = int(payload["revision"])
    if revision < 1:
        raise ValueError("ownership registry revision must be positive")
    concepts = []
    seen: set[str] = set()
    for item in payload.get("concepts", []):
        concept_id = item["id"]
        if concept_id in seen:
            raise ValueError(f"duplicate concept id: {concept_id}")
        seen.add(concept_id)
        patterns = tuple(item.get("patterns", [re.escape(concept_id)]))
        for pattern in patterns:
            re.compile(pattern, re.IGNORECASE)
        concepts.append(
            ConceptRule(
                concept_id=concept_id,
                label=item.get("label", concept_id),
                canonical_owner=item["canonical_owner"],
                patterns=patterns,
                max_active_implementations=int(item.get("max_active_implementations", 4)),
                max_authority_definitions=int(item.get("max_authority_definitions", 8)),
            )
        )
    if not concepts:
        raise ValueError("ownership registry must declare at least one concept")
    return OwnershipRegistry(
        registry_id=payload["registry_id"],
        revision=revision,
        concepts=tuple(concepts),
    )


def iter_artifacts(root: Path) -> list[Path]:
    return sorted(
        path for path in root.rglob("*")
        if path.is_file()
        and path.suffix.lower() in ARCHITECTURE_SUFFIXES
        and not any(part in EXCLUDED_PARTS for part in path.parts)
    )


def classify_posture(path: str, suffix: str) -> str:
    parts = {part.lower() for part in Path(path).parts}
    name = Path(path).name.lower()
    stem = Path(path).stem.lower()
    if parts & HISTORICAL_PARTS or name.startswith("changelog"):
        return "history"
    if parts & REFERENCE_PARTS:
        return "reference"
    if "tests" in parts or name.startswith("test_"):
        return "test"
    if "migrations" in parts or ("sql" in parts and re.match(r"^\d+[_-]", stem)):
        return "migration"
    if parts & PROJECTION_PARTS or suffix in {".js", ".css", ".html"}:
        return "projection"
    if (
        "schemas" in parts
        or "governance" in parts
        or "authority" in parts
        or any(token in stem for token in ("schema", "contract", "doctrine", "authority"))
    ):
        return "authority"
    if suffix in {".py", ".sql", ".sh"} or name.startswith(("compose.", "docker-compose")):
        return "implementation"
    return "documentation"


def _python_active_surface(text: str) -> str:
    """Return executable names and strings while excluding comments and docstrings."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return text
    docstring_nodes: set[int] = set()
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if (
            isinstance(body, list)
            and body
            and isinstance(body[0], ast.Expr)
            and isinstance(body[0].value, ast.Constant)
            and isinstance(body[0].value.value, str)
        ):
            docstring_nodes.add(id(body[0].value))
    tokens: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            tokens.append(node.id)
        elif isinstance(node, ast.Attribute):
            tokens.append(node.attr)
        elif isinstance(node, ast.alias):
            tokens.extend(filter(None, (node.name, node.asname)))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            tokens.append(node.name)
        elif (
            isinstance(node, ast.Constant)
            and isinstance(node.value, str)
            and id(node) not in docstring_nodes
        ):
            tokens.append(node.value)
    return "\n".join(tokens)


def _active_surface(text: str, suffix: str, posture: str) -> str:
    if suffix == ".py" and posture in {"implementation", "projection", "test"}:
        return _python_active_surface(text)
    return text


def _concept_hits(text: str, rules: Iterable[ConceptRule]) -> tuple[str, ...]:
    hits = []
    for rule in rules:
        if any(re.search(pattern, text, re.IGNORECASE) for pattern in rule.patterns):
            hits.append(rule.concept_id)
    return tuple(sorted(hits))


def inspect_artifact(spec: RepositorySpec, path: Path, registry: OwnershipRegistry) -> Artifact:
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    relative = path.relative_to(spec.root).as_posix()
    suffix = path.suffix.lower()
    posture = classify_posture(relative, suffix)
    active_surface = _active_surface(text, suffix, posture)
    generation_identities = tuple(
        sorted(set(GENERATION_IDENTITY_TOKEN.findall(active_surface)))
    )
    runtime_terms = ()
    if posture == "implementation":
        runtime_terms = tuple(
            sorted(
                name
                for name, pattern in RUNTIME_BOUNDARY_PATTERNS.items()
                if pattern.search(active_surface)
            )
        )
    return Artifact(
        repository=spec.name,
        repository_role=spec.role,
        path=relative,
        suffix=suffix,
        stem=path.stem.lower(),
        lines=len(text.splitlines()),
        bytes=len(raw),
        meaningful=bool(text.strip()),
        digest=hashlib.sha256(raw).hexdigest(),
        posture=posture,
        generation_named=bool(GENERATION_PATH_TOKEN.search(relative)),
        generation_identities=generation_identities,
        compatibility_named=bool(COMPATIBILITY_PATH_TOKEN.search(relative)),
        concepts=_concept_hits(text + "\n" + relative.replace("/", " "), registry.concepts),
        runtime_boundary_terms=runtime_terms,
    )


def build_inventory(specs: list[RepositorySpec], registry: OwnershipRegistry) -> list[Artifact]:
    return [
        inspect_artifact(spec, path, registry)
        for spec in specs
        for path in iter_artifacts(spec.root)
    ]


def exact_duplicates(records: list[Artifact]) -> list[list[Artifact]]:
    groups: dict[str, list[Artifact]] = defaultdict(list)
    for record in records:
        if record.meaningful:
            groups[record.digest].append(record)
    return [
        sorted(group, key=lambda item: (item.repository, item.path))
        for group in groups.values()
        if len(group) > 1
    ]


def repeated_stems(records: list[Artifact]) -> list[list[Artifact]]:
    groups: dict[str, list[Artifact]] = defaultdict(list)
    for record in records:
        if record.meaningful and record.stem not in {"readme", "index", "__init__"}:
            groups[record.stem].append(record)
    return [
        sorted(group, key=lambda item: (item.repository, item.path))
        for group in groups.values()
        if len({item.repository for item in group}) > 1
    ]


def _refs(records: Iterable[Artifact]) -> tuple[str, ...]:
    return tuple(sorted(f"{item.repository}:{item.path}" for item in records))


def _finding(
    *,
    priority: str,
    category: str,
    subject: str,
    canonical_owner: str | None,
    recommendation: str,
    artifacts: tuple[str, ...],
) -> Finding:
    identity = json.dumps(
        [priority, category, subject, canonical_owner, artifacts],
        ensure_ascii=False,
        separators=(",", ":"),
    )
    finding_id = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:12]
    return Finding(
        finding_id=finding_id,
        priority=priority,
        category=category,
        subject=subject,
        canonical_owner=canonical_owner,
        recommendation=recommendation,
        artifacts=artifacts,
    )


def build_findings(
    specs: list[RepositorySpec],
    records: list[Artifact],
    registry: OwnershipRegistry,
) -> list[Finding]:
    findings: list[Finding] = []

    for record in records:
        low_risk = record.posture in {"history", "migration", "reference"}
        if record.generation_named:
            findings.append(_finding(
                priority="P5" if low_risk else "P1",
                category="generation_name",
                subject=f"generation-named path: {record.path}",
                canonical_owner=None,
                recommendation=(
                    "Rename the active identity by responsibility; keep ordered migration "
                    "or historical identifiers only where provenance requires them."
                ),
                artifacts=_refs([record]),
            ))
        if record.generation_identities:
            findings.append(_finding(
                priority="P5" if low_risk else "P1",
                category="generation_identity",
                subject=", ".join(record.generation_identities[:5]),
                canonical_owner=None,
                recommendation=(
                    "Remove generation labels from internal routes, modules and contracts. "
                    "Retain an external protocol version only at the adapter boundary."
                ),
                artifacts=_refs([record]),
            ))
        if record.compatibility_named:
            findings.append(_finding(
                priority="P5" if low_risk else "P2",
                category="compatibility_path",
                subject=f"compatibility-labelled path: {record.path}",
                canonical_owner=None,
                recommendation=(
                    "Prove active consumers, define one removal condition, then merge or remove "
                    "the compatibility path instead of preserving a parallel architecture."
                ),
                artifacts=_refs([record]),
            ))
        if record.runtime_boundary_terms:
            findings.append(_finding(
                priority="P0",
                category="runtime_boundary",
                subject=", ".join(record.runtime_boundary_terms),
                canonical_owner="Hermes/external runtime",
                recommendation=(
                    "Verify that this code is only a bounded adapter or observation seam. "
                    "Move scheduling, queues, provider routing, plugin lifecycle, memory runtime "
                    "or approval automation to the owning external runtime."
                ),
                artifacts=_refs([record]),
            ))

    for group in exact_duplicates(records):
        postures = {item.posture for item in group}
        repositories = {item.repository for item in group}
        if postures & {"reference", "history"}:
            priority = "P4"
            recommendation = (
                "Keep one canonical source and retain other copies only as pinned reference "
                "artifacts with an explicit drift check."
            )
        elif len(repositories) == 1:
            priority = "P2"
            recommendation = (
                "Select one active artifact, redirect consumers, then remove the duplicate "
                "after import, route, deployment and documentation checks."
            )
        else:
            priority = "P3"
            recommendation = (
                "Identify the canonical owner; replace the secondary copy with conformance, "
                "vendoring metadata or a generated projection."
            )
        findings.append(_finding(
            priority=priority,
            category="exact_duplicate",
            subject=f"exact duplicate ({len(group)} artifacts)",
            canonical_owner=None,
            recommendation=recommendation,
            artifacts=_refs(group),
        ))

    for group in repeated_stems(records):
        findings.append(_finding(
            priority="P4",
            category="repeated_name",
            subject=f"repeated stem: {group[0].stem}",
            canonical_owner=None,
            recommendation=(
                "Check whether the files represent definition, implementation, adapter or "
                "projection. Rename by responsibility or consolidate if they compete."
            ),
            artifacts=_refs(group),
        ))

    spec_names = {spec.name for spec in specs}
    by_concept: dict[str, list[Artifact]] = defaultdict(list)
    for record in records:
        for concept in record.concepts:
            by_concept[concept].append(record)

    for rule in registry.concepts:
        matches = by_concept.get(rule.concept_id, [])
        authority = [item for item in matches if item.posture == "authority"]
        wrong_owner = [item for item in authority if item.repository != rule.canonical_owner]
        if wrong_owner:
            findings.append(_finding(
                priority="P0",
                category="authority_collision",
                subject=rule.label,
                canonical_owner=rule.canonical_owner,
                recommendation=(
                    f"Keep the semantic definition in {rule.canonical_owner}. Convert non-owner "
                    "artifacts to conformance schemas, implementations, adapters or projections "
                    "without redefining lifecycle, status or authority."
                ),
                artifacts=_refs(wrong_owner),
            ))
        owner_definitions = [
            item for item in authority if item.repository == rule.canonical_owner
        ]
        if len(owner_definitions) > rule.max_authority_definitions:
            findings.append(_finding(
                priority="P2",
                category="authority_fragmentation",
                subject=rule.label,
                canonical_owner=rule.canonical_owner,
                recommendation=(
                    "Choose one canonical definition and make the remaining documents explicit "
                    "specializations or indexed references."
                ),
                artifacts=_refs(owner_definitions),
            ))
        active_implementations = [
            item for item in matches
            if item.posture == "implementation" and item.repository in spec_names
        ]
        per_repository = Counter(item.repository for item in active_implementations)
        for repository, count in sorted(per_repository.items()):
            if count > rule.max_active_implementations:
                fragmented = [item for item in active_implementations if item.repository == repository]
                findings.append(_finding(
                    priority="P2",
                    category="implementation_fragmentation",
                    subject=f"{rule.label} in {repository}",
                    canonical_owner=rule.canonical_owner,
                    recommendation=(
                        "Consolidate the active path behind one application service or adapter; "
                        "keep separate domain states only when they represent distinct invariants."
                    ),
                    artifacts=_refs(fragmented),
                ))

    return sorted(
        findings,
        key=lambda item: (
            PRIORITY_ORDER[item.priority],
            item.category,
            item.subject,
            item.artifacts,
        ),
    )


def concept_matrix(records: list[Artifact], registry: OwnershipRegistry) -> dict[str, dict[str, object]]:
    matrix: dict[str, dict[str, object]] = {}
    for rule in registry.concepts:
        matches = [record for record in records if rule.concept_id in record.concepts]
        counts: dict[str, Counter[str]] = defaultdict(Counter)
        for item in matches:
            counts[item.repository][item.posture] += 1
        matrix[rule.concept_id] = {
            "label": rule.label,
            "canonical_owner": rule.canonical_owner,
            "repositories": {
                repository: dict(sorted(postures.items()))
                for repository, postures in sorted(counts.items())
            },
        }
    return matrix


def render_markdown(
    specs: list[RepositorySpec],
    records: list[Artifact],
    registry: OwnershipRegistry,
    findings: list[Finding] | None = None,
) -> str:
    findings = findings if findings is not None else build_findings(specs, records, registry)
    counts = Counter(item.priority for item in findings)
    matrix = concept_matrix(records, registry)
    lines = [
        "# Pantheon architecture convergence inventory",
        "",
        "> Report-only: a finding is not deletion proof or an authority decision.",
        "",
        "## Repositories",
        "",
    ]
    lines.extend(f"- **{spec.name}** — {spec.role} — `{spec.root}`" for spec in specs)
    lines.extend([
        "",
        "## Registry",
        "",
        f"- ID: `{registry.registry_id}`",
        f"- Revision: **{registry.revision}**",
        f"- Governed concepts: **{len(registry.concepts)}**",
        "",
        "## Summary",
        "",
        f"- Architecture artifacts: **{len(records)}**",
        f"- Findings: **{len(findings)}**",
    ])
    lines.extend(f"- {priority}: **{counts.get(priority, 0)}**" for priority in PRIORITY_ORDER)
    lines.extend(["", "## Prioritized findings", ""])
    if not findings:
        lines.append("None detected.")
    for finding in findings:
        owner = f" — owner `{finding.canonical_owner}`" if finding.canonical_owner else ""
        lines.append(
            f"- **{finding.priority} · {finding.category} · {finding.finding_id}** "
            f"— {finding.subject}{owner}"
        )
        lines.append(f"  - Recommendation: {finding.recommendation}")
        lines.extend(f"  - `{artifact}`" for artifact in finding.artifacts[:20])
        if len(finding.artifacts) > 20:
            lines.append(f"  - … {len(finding.artifacts) - 20} more")
    lines.extend(["", "## Concept ownership matrix", ""])
    for concept_id, entry in matrix.items():
        lines.append(
            f"- **{entry['label']}** (`{concept_id}`) — owner `{entry['canonical_owner']}`"
        )
        repositories = entry["repositories"]
        if not repositories:
            lines.append("  - no artifact detected")
            continue
        for repository, postures in repositories.items():
            rendered = ", ".join(f"{name}={count}" for name, count in postures.items())
            lines.append(f"  - `{repository}`: {rendered}")
    lines.extend([
        "",
        "## Decision vocabulary",
        "",
        "- `retain`: responsibility is unique and correctly placed.",
        "- `simplify`: preserve the concept but reduce wrappers or repeated validation.",
        "- `merge`: competing active paths become one canonical path.",
        "- `move`: responsibility belongs to another repository or layer.",
        "- `vendor/reference only`: immutable or pinned copy with drift detection.",
        "- `deprecate`: bounded transition with named consumers and removal condition.",
        "- `remove`: no active consumer, authority, deployment or compatibility obligation remains.",
        "",
    ])
    return "\n".join(lines) + "\n"


def _json_payload(
    specs: list[RepositorySpec],
    records: list[Artifact],
    registry: OwnershipRegistry,
    findings: list[Finding],
) -> dict[str, object]:
    return {
        "registry": {
            "registry_id": registry.registry_id,
            "revision": registry.revision,
            "concepts": [asdict(rule) for rule in registry.concepts],
        },
        "repositories": [
            {"name": spec.name, "role": spec.role, "root": str(spec.root)}
            for spec in specs
        ],
        "artifacts": [asdict(record) for record in records],
        "findings": [asdict(finding) for finding in findings],
        "concept_matrix": concept_matrix(records, registry),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repository",
        action="append",
        type=repository_spec,
        required=True,
        help="repeat NAME=ROLE=PATH for pantheon-mvp and Pantheon-Next",
    )
    parser.add_argument("--authority-registry", type=Path, required=True)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--fail-on-generation-names", action="store_true")
    parser.add_argument(
        "--fail-on-priority",
        action="append",
        choices=tuple(PRIORITY_ORDER),
        help="return 1 when at least one finding has this priority",
    )
    args = parser.parse_args()

    registry = load_registry(args.authority_registry.resolve())
    records = build_inventory(args.repository, registry)
    findings = build_findings(args.repository, records, registry)
    if args.format == "json":
        rendered = json.dumps(
            _json_payload(args.repository, records, registry, findings),
            indent=2,
            sort_keys=True,
        ) + "\n"
    else:
        rendered = render_markdown(args.repository, records, registry, findings)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

    if args.fail_on_generation_names and any(
        record.generation_named or record.generation_identities for record in records
    ):
        return 1
    fail_priorities = set(args.fail_on_priority or [])
    return 1 if fail_priorities & {finding.priority for finding in findings} else 0


if __name__ == "__main__":
    raise SystemExit(main())
