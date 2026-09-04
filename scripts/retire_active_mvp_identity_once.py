from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

MOVES = [
    ("implementation/mvp_vertical", "implementation/pantheon_app"),
    ("implementation/demo/scenarios/architecture-mvp-fictif", "implementation/demo/scenarios/architecture-fictif"),
    ("docs/governance/examples/mvp_vertical_fixture", "docs/governance/examples/governed_loop_fixture"),
    ("schemas/mvp_governed_loop_objects.schema.yaml", "schemas/governed_loop_objects.schema.yaml"),
    ("schemas/examples/mvp_governed_loop_objects.example.yaml", "schemas/examples/governed_loop_objects.example.yaml"),
    ("scripts/validate_mvp_fixture.py", "scripts/validate_governed_loop_fixture.py"),
    ("docs/governance/MVP_GOVERNED_TASK_LOOP.md", "docs/governance/GOVERNED_TASK_LOOP.md"),
    ("docs/governance/NEXT_MVP_REPOSITORY_PLACEMENT.md", "docs/governance/REPOSITORY_PLACEMENT.md"),
    ("docs/governance/examples/mvp_task_contract.yaml", "docs/governance/examples/task_contract.example.yaml"),
    ("docs/governance/examples/mvp_evidence_pack_candidate.yaml", "docs/governance/examples/evidence_pack_candidate.example.yaml"),
    ("docs/governance/examples/mvp_decision_record.yaml", "docs/governance/examples/decision_record.example.yaml"),
    ("docs/governance/examples/mvp_memory_candidate.yaml", "docs/governance/examples/register_candidate.example.yaml"),
    ("tests/test_mvp_governed_loop_current_posture.py", "tests/test_governed_loop_current_posture.py"),
    ("tests/test_mvp_governed_loop_request_provenance.py", "tests/test_governed_loop_request_provenance.py"),
    ("tests/test_mvp_loop_provider_agnostic.py", "tests/test_governed_loop_provider_agnostic.py"),
    ("tests/test_mvp_schema_reconciliation.py", "tests/test_governed_loop_schema_reconciliation.py"),
]

HISTORICAL_PREFIXES = ("ai_logs/", "implementation/ai_logs/", "docs/audits/")
HISTORICAL_EXACT = {
    "CHANGELOG.md",
    "CHANGELOG_ARCHIVE.md",
    "implementation/CHANGELOG.md",
    "implementation/IMPORT_PROVENANCE.md",
    "docs/governance/authority/OBSOLETE_AND_ABSENT_INDEX.md",
}
TEXT_SUFFIXES = {
    ".py", ".md", ".toml", ".yaml", ".yml", ".json", ".js", ".html",
    ".css", ".sql", ".sh", ".txt", ".env", ".lock", ".ini", ".cfg", ".xml",
}
TEXT_NAMES = {"Dockerfile", "Makefile", ".gitmodules"}
RUNTIME_TOKEN = re.compile(r"(?<![A-Za-z0-9_])MVP_[A-Z0-9_]+")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def historical(path: Path) -> bool:
    value = rel(path)
    return ".git" in path.parts or value in HISTORICAL_EXACT or value.startswith(HISTORICAL_PREFIXES)


def text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in TEXT_NAMES


for source, target in MOVES:
    src = ROOT / source
    dst = ROOT / target
    if not src.exists():
        raise SystemExit(f"missing rename source: {source}")
    if dst.exists():
        raise SystemExit(f"rename target already exists: {target}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "mv", source, target], cwd=ROOT, check=True)

runtime_tokens: set[str] = set()
for path in ROOT.rglob("*"):
    if not path.is_file() or not text_file(path) or historical(path):
        continue
    value = rel(path)
    if value.startswith(".github/workflows/"):
        continue
    if not value.startswith(("implementation/", "deployment/", "templates/", ".github/scripts/")):
        continue
    try:
        runtime_tokens.update(RUNTIME_TOKEN.findall(path.read_text(encoding="utf-8")))
    except UnicodeDecodeError:
        pass

replacements = [
    ("NEXT_MVP_REPOSITORY_PLACEMENT.md", "REPOSITORY_PLACEMENT.md"),
    ("MVP_GOVERNED_TASK_LOOP.md", "GOVERNED_TASK_LOOP.md"),
    ("architecture-mvp-fictif", "architecture-fictif"),
    ("mvp_vertical_fixture", "governed_loop_fixture"),
    ("validate_mvp_fixture.py", "validate_governed_loop_fixture.py"),
    ("validate_mvp_fixture", "validate_governed_loop_fixture"),
    ("mvp_governed_loop_objects", "governed_loop_objects"),
    ("mvp_task_contract.yaml", "task_contract.example.yaml"),
    ("mvp_evidence_pack_candidate.yaml", "evidence_pack_candidate.example.yaml"),
    ("mvp_decision_record.yaml", "decision_record.example.yaml"),
    ("mvp_memory_candidate.yaml", "register_candidate.example.yaml"),
    ("pantheon-mvp-vertical", "pantheon-app"),
    ("mvp-cockpit-api", "pantheon-cockpit"),
    ("mvp-vertical", "pantheon-app"),
    ("implementation/mvp_vertical", "implementation/pantheon_app"),
    ("mvp_vertical", "pantheon_app"),
    ("postgresql://mvp:mvp@", "postgresql://pantheon:pantheon@"),
    ("POSTGRES_USER: mvp", "POSTGRES_USER: pantheon"),
    ("POSTGRES_PASSWORD: mvp", "POSTGRES_PASSWORD: pantheon"),
    ("POSTGRES_DB: mvp", "POSTGRES_DB: pantheon"),
    ("POSTGRES_USER=mvp", "POSTGRES_USER=pantheon"),
    ("POSTGRES_PASSWORD=mvp", "POSTGRES_PASSWORD=pantheon"),
    ("POSTGRES_DB=mvp", "POSTGRES_DB=pantheon"),
]
runtime_replacements = [
    (token, "PANTHEON_" + token.removeprefix("MVP_"))
    for token in sorted(runtime_tokens, key=len, reverse=True)
]

for path in ROOT.rglob("*"):
    if not path.is_file() or not text_file(path) or historical(path) or path == SELF:
        continue
    value = rel(path)
    if value.startswith(".github/workflows/"):
        continue
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    updated = original
    for old, new in replacements + runtime_replacements:
        updated = updated.replace(old, new)
    if updated != original:
        path.write_text(updated, encoding="utf-8")

signer = ROOT / "implementation/pantheon_app/signer.py"
signer_text = signer.read_text(encoding="utf-8")
old_line = '"system", "runner", "hermes", "pantheon-app", "pantheon_app", "gate",'
new_line = '"system", "runner", "hermes", "pantheon-app", "pantheon_app", "mvp-vertical", "mvp_vertical", "gate",'
if old_line not in signer_text:
    raise SystemExit("signer identity line changed; refusing rewrite")
signer_text = signer_text.replace(old_line, new_line, 1)
marker = "# Identities that ARE the system and can never be a human signer."
signer_text = signer_text.replace(
    marker,
    marker + "\n# Former implementation names remain deny-only reserved identities; they are not compatibility aliases.",
    1,
)
signer.write_text(signer_text, encoding="utf-8")

placement = ROOT / "docs/governance/REPOSITORY_PLACEMENT.md"
text = placement.read_text(encoding="utf-8")
text = text.replace(
    "- declarative Hermes and OpenWebUI templates without executable adapter ownership;",
    "- declarative Hermes templates without executable adapter ownership;",
).replace(
    "- OpenWebUI functions, tools, pipes or actions implemented as code;",
    "- bounded interaction or projection adapters implemented as code;",
).replace(
    "Pantheon governs the classification. `implementation/` carries bounded candidate implementation. OpenWebUI exposes operational surfaces where installed. Hermes performs authorized work where separately activated.",
    "Pantheon governs the classification. `implementation/` carries bounded candidate implementation. Hermes performs authorized work where separately activated; Pantheon Cockpit projects governed review and status surfaces.",
)
placement.write_text(text, encoding="utf-8")

loop = ROOT / "docs/governance/GOVERNED_TASK_LOOP.md"
text = loop.read_text(encoding="utf-8")
for old, new in (
    ("# MVP Governed Task Loop", "# Governed Task Loop"),
    ("Canonical MVP decision vocabulary", "Canonical decision vocabulary"),
    ("closed MVP decision vocabulary", "closed decision vocabulary"),
    ("What this MVP is not", "What this loop is not"),
    ("The MVP is demonstrated", "The loop is demonstrated"),
    ("Pantheon MVP Vertical bundle", "Pantheon governed-loop implementation"),
):
    text = text.replace(old, new)
loop.write_text(text, encoding="utf-8")

revit = ROOT / "revit-plugin/docs/ARCHITECTURE.md"
if revit.exists():
    revit.write_text(
        revit.read_text(encoding="utf-8").replace("pantheon-mvp", "Pantheon Next implementation"),
        encoding="utf-8",
    )

posture = ROOT / "tests/test_governed_loop_current_posture.py"
text = posture.read_text(encoding="utf-8").replace("test_mvp_loop_", "test_governed_loop_")
text += '''\n\nACTIVE_IDENTITY_PATH_ROOTS = (\n    ROOT / "implementation",\n    ROOT / "docs/governance",\n    ROOT / "schemas",\n    ROOT / "scripts",\n    ROOT / "tests",\n)\n\n\ndef test_retired_mvp_generation_name_does_not_return_to_active_paths() -> None:\n    offenders = []\n    for root in ACTIVE_IDENTITY_PATH_ROOTS:\n        for path in root.rglob("*"):\n            relative = path.relative_to(ROOT).as_posix()\n            if relative.startswith(("implementation/ai_logs/", "docs/audits/")):\n                continue\n            if relative == "docs/governance/authority/OBSOLETE_AND_ABSENT_INDEX.md":\n                continue\n            if "mvp" in path.name.lower():\n                offenders.append(relative)\n    assert not offenders, "retired MVP-named active paths: " + ", ".join(offenders)\n'''
posture.write_text(text, encoding="utf-8")

for name in (
    "test_governed_loop_request_provenance.py",
    "test_governed_loop_provider_agnostic.py",
    "test_governed_loop_schema_reconciliation.py",
):
    path = ROOT / "tests" / name
    text = path.read_text(encoding="utf-8")
    text = text.replace("mvp_governed_loop", "governed_loop")
    text = text.replace("mvp_loop", "governed_loop")
    text = text.replace("mvp_schema", "governed_loop_schema")
    path.write_text(text, encoding="utf-8")

path_offenders: list[str] = []
for root in (ROOT / "implementation", ROOT / "docs/governance", ROOT / "schemas", ROOT / "scripts", ROOT / "tests"):
    for path in root.rglob("*"):
        if not path.exists() or historical(path) or path == SELF:
            continue
        if "mvp" in path.name.lower():
            path_offenders.append(rel(path))
if path_offenders:
    raise SystemExit("active MVP-named paths remain:\n" + "\n".join(path_offenders))

content_offenders: list[str] = []
for root in (ROOT / "implementation", ROOT / "deployment", ROOT / "templates"):
    for path in root.rglob("*"):
        if not path.is_file() or not text_file(path) or historical(path) or path == signer:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(token in text for token in ("mvp_vertical", "pantheon-mvp-vertical", "mvp-cockpit-api")):
            content_offenders.append(rel(path))
        elif RUNTIME_TOKEN.search(text):
            content_offenders.append(rel(path))
if content_offenders:
    raise SystemExit("active runtime MVP tokens remain:\n" + "\n".join(sorted(set(content_offenders))))

subprocess.run(["python", "-m", "compileall", "-q", "implementation/pantheon_app"], cwd=ROOT, check=True)
subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
SELF.unlink()
print("runtime MVP tokens renamed:", ", ".join(sorted(runtime_tokens)))
