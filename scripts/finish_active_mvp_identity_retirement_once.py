from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()


def replace(path: str, pairs: tuple[tuple[str, str], ...]) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    updated = text
    for old, new in pairs:
        updated = updated.replace(old, new)
    if updated != text:
        target.write_text(updated, encoding="utf-8")


# Synthetic/example identifiers are active test vocabulary, not historical provenance.
id_roots = (
    ROOT / "implementation/tests",
    ROOT / "implementation/dossiers",
    ROOT / "docs/governance/examples",
    ROOT / "schemas/examples",
    ROOT / "scripts/validate_governed_loop_fixture.py",
    ROOT / "implementation/demo/scenarios/architecture-fictif",
)
id_pattern = re.compile(r"(?<![A-Za-z0-9-])mvp\.")
for root in id_roots:
    paths = [root] if root.is_file() else list(root.rglob("*"))
    for path in paths:
        if not path.is_file() or path == SELF:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = id_pattern.sub("pantheon.", text)
        updated = updated.replace("MVP-ARCH-FICTIF-001", "PANTHEON-ARCH-FICTIF-001")
        updated = updated.replace("MVP-Bad-ID", "PANTHEON-Bad-ID")
        updated = updated.replace("pgvector://mvp-index", "pgvector://pantheon-index")
        if updated != text:
            path.write_text(updated, encoding="utf-8")

replace("implementation/compose.phase-b.yaml", (
    ("x-mvp-runtime: &mvp-runtime", "x-pantheon-runtime: &pantheon-runtime"),
    ("${PANTHEON_MVP_IMAGE_NAME:-pantheon-mvp}:${PANTHEON_MVP_IMAGE_TAG:-phase-b}", "${PANTHEON_IMAGE_NAME:-pantheon-app}:${PANTHEON_IMAGE_TAG:-phase-b}"),
    ("${PANTHEON_PG_USER:-pantheon_mvp}", "${PANTHEON_PG_USER:-pantheon}"),
    ("${PANTHEON_PG_DB:-pantheon_mvp}", "${PANTHEON_PG_DB:-pantheon}"),
    ("<<: *mvp-runtime", "<<: *pantheon-runtime"),
))
replace("implementation/docker-compose.yml", (
    ('pg_isready -U mvp -d mvp', 'pg_isready -U pantheon -d pantheon'),
    ('postgresql://pantheon:pantheon@pgvector:5432/mvp', 'postgresql://pantheon:pantheon@pgvector:5432/pantheon'),
))
replace("implementation/pantheon_app/store.py", (
    ('postgresql://pantheon:pantheon@localhost:5433/mvp', 'postgresql://pantheon:pantheon@localhost:5433/pantheon'),
    ("dossier is the MVP's project parent", "dossier is the candidate implementation's project parent"),
))
replace("implementation/pantheon_app/document_structure.py", (
    ('MVP persistence remains richer', 'Candidate persistence remains richer'),
))
replace("implementation/pantheon_app/apu_write_preparation.py", (
    ('pantheon-mvp.document-structure:', 'pantheon-app.document-structure:'),
))
replace("implementation/pantheon_app/apu_mapping_converter.py", (
    ('"implementation": "pantheon-mvp"', '"implementation": "pantheon-app"'),
))
replace("implementation/tools/run_hindsight_hermes_o1.sh", (
    ('PANTHEON_ROOT="$GITHUB_WORKSPACE/pantheon-mvp"', 'PANTHEON_ROOT="$GITHUB_WORKSPACE/monorepo/implementation"'),
))
replace("implementation/.github/workflows/hindsight-obsidian-hermes-o3-lab.yml", (
    ('path: pantheon-mvp', 'path: monorepo'),
    ('working-directory: pantheon-mvp', 'working-directory: monorepo/implementation'),
))
replace("implementation/README.md", (
    ('# Pantheon MVP', '# Pantheon candidate implementation'),
))
replace("implementation/pantheon_app/__init__.py", (
    ('Pantheon Next MVP loop', 'Pantheon Next governed task loop'),
))
replace("implementation/pantheon_app/cockpit/tool_catalog.json", (
    ('adapters bornés Pantheon MVP', 'adapters bornés Pantheon'),
))
replace("implementation/pantheon_app/cockpit/vendor/radix-icons/README.md", (
    ('Pantheon MVP Cockpit', 'Pantheon Cockpit'),
    ('into the MVP tree', 'into the implementation tree'),
    ('https://github.com/ifanjuang/pantheon-mvp.git', 'https://github.com/ifanjuang/Pantheon-Next.git'),
    ('main MVP tree', 'main implementation tree'),
    ('pantheon_app/cockpit/vendor/radix-icons/materialize-icons.sh', 'implementation/pantheon_app/cockpit/vendor/radix-icons/materialize-icons.sh'),
))
replace("implementation/pantheon_app/cockpit/vendor/radix-icons/SELECTION.md", (
    ('# Radix Icons — MVP semantic selection', '# Radix Icons — Cockpit semantic selection'),
    ('existing MVP Cockpit icon keys', 'existing Pantheon Cockpit icon keys'),
))
replace("implementation/demo/scenarios/README.md", (
    ('executable MVP', 'executable candidate'),
))
replace("implementation/demo/scenarios/architecture-fictif/README.md", (
    ('# Architecture MVP fictive scenario', '# Architecture fictive scenario'),
    ('examples/architecture/mvp_dossier_fictif/', 'implementation/demo/scenarios/architecture-fictif/'),
))
replace("implementation/demo/scenarios/architecture-fictif/corpus/00_manifest.md", (
    ('architecture MVP fictive', 'architecture fictive'),
))
replace("implementation/docs/cockpit/COCKPIT_LIVING_CARDS.md", (
    ('candidate presentation implementation in `pantheon-mvp`', 'candidate presentation implementation in `implementation/pantheon_app/cockpit/`'),
))
replace("implementation/docs/governance/PROFESSIONAL_DUTY_OF_CARE.md", (
    ('no independent MVP doctrine', 'no independent implementation doctrine'),
    ('The MVP may implement', 'The candidate implementation may implement'),
))

# Current schema/docs labels and consumers must not advertise the former repository/package as owner.
replace("schemas/registry.schema.yaml", (("          - pantheon-mvp\n", ""),))
replace("schemas/category_classification.schema.yaml", (
    ('consumed by pantheon-mvp and Cockpit', 'consumed by the Pantheon implementation and Cockpit'),
))
replace("schemas/tag_registry.schema.yaml", (
    ('by pantheon-mvp, Cockpit projections', 'by the Pantheon implementation, Cockpit projections'),
))
replace("schemas/governed_loop_objects.schema.yaml", (
    ('Pantheon Next MVP Governed Loop Objects', 'Pantheon Next Governed Loop Objects'),
    ('five central MVP governed task loop objects', 'five central governed task loop objects'),
))
replace("schemas/README.md", (
    ('## MVP vertical reconciliation', '## Governed-loop reconciliation'),
    ('The MVP bundle formalizes', 'The governed-loop bundle formalizes'),
))
replace("schemas/examples/governed_loop_objects.example.yaml", (
    ('the MVP governed loop object bundle', 'the governed-loop object bundle'),
))
replace("scripts/validate_governed_loop_fixture.py", (
    ('Pantheon Next MVP vertical fixture', 'Pantheon Next governed-loop fixture'),
    ('Validate an MVP fixture', 'Validate a governed-loop fixture'),
))

# Fixture prose is current example vocabulary; historical AI logs retain the old generation language.
fixture_root = ROOT / "docs/governance/examples/governed_loop_fixture"
for path in fixture_root.rglob("*"):
    if not path.is_file():
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    updated = text.replace("MVP vertical", "governed-loop").replace("MVP Vertical", "Governed-loop")
    updated = updated.replace("MVP Fixture", "Governed-loop Fixture")
    updated = updated.replace("MVP Validation", "Governed-loop Validation")
    updated = updated.replace("MVP validation", "governed-loop validation")
    updated = updated.replace("MVP Vocabulary", "Governed-loop Vocabulary")
    updated = updated.replace("MVP Object", "Governed-loop Object")
    updated = updated.replace("MVP Governance", "Governed-loop Governance")
    updated = updated.replace("Failing MVP Fixture", "Failing Governed-loop Fixture")
    updated = updated.replace("MVP Prevalidator", "Governed-loop Prevalidator")
    updated = updated.replace("MVP Source", "Governed-loop Source")
    updated = updated.replace("MVP Local", "Governed-loop Local")
    updated = updated.replace("MVP fixture", "governed-loop fixture")
    updated = updated.replace("MVP loop", "governed task loop")
    updated = updated.replace("Current MVP placement", "Current governed-loop placement")
    updated = updated.replace("The MVP must keep", "The governed loop must keep")
    if updated != text:
        path.write_text(updated, encoding="utf-8")

for path in (
    ROOT / "docs/governance/examples/task_contract.example.yaml",
    ROOT / "docs/governance/examples/evidence_pack_candidate.example.yaml",
    ROOT / "docs/governance/examples/decision_record.example.yaml",
    ROOT / "docs/governance/examples/register_candidate.example.yaml",
):
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace("# MVP governed task loop", "# Governed task loop"), encoding="utf-8")

# Test-local path aliases and probe identifiers should describe the current package.
for path_name in (
    "implementation/tests/test_agency_project_contacts_model.py",
    "implementation/tests/test_consequential_mutation_inventory.py",
):
    path = ROOT / path_name
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\bMVP\b", "APP", text)
    path.write_text(text, encoding="utf-8")
replace("implementation/tests/test_startup_migrations_lock_light.py", (("mvp_migrationprobe_", "pantheon_migrationprobe_"),))
replace("implementation/tests/test_entity_relation_migration.py", (("mvp_relationprobe_", "pantheon_relationprobe_"),))
replace("implementation/tests/test_phase_b_compose.py", (
    ('"mvp_document_source_binding"', '"pantheon_document_source_binding"'),
    ('"${PANTHEON_MVP_IMAGE_NAME:-pantheon-mvp}:"', '"${PANTHEON_IMAGE_NAME:-pantheon-app}:"'),
    ('"${PANTHEON_MVP_IMAGE_TAG:-phase-b}"', '"${PANTHEON_IMAGE_TAG:-phase-b}"'),
))
replace("tests/test_governed_loop_schema_reconciliation.py", (
    ('Validation-only checks for the MVP decision/schema reconciliation', 'Validation-only checks for the governed-loop decision/schema reconciliation'),
    ('test_documented_mvp_fixtures_follow_the_reconciled_schema', 'test_documented_governed_loop_fixtures_follow_the_reconciled_schema'),
))
replace("docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md", (
    ('Grouped row for the MVP vertical fixture directory', 'Grouped row for the governed-loop fixture directory'),
))

# Strengthen the existing current-posture test against technical identity regression.
posture = ROOT / "tests/test_governed_loop_current_posture.py"
text = posture.read_text(encoding="utf-8")
addition = '''\n\ndef test_retired_mvp_runtime_identity_does_not_return() -> None:\n    roots = (ROOT / "implementation/pantheon_app", ROOT / "implementation/compose.phase-b.yaml", ROOT / "implementation/docker-compose.yml")\n    forbidden = ("mvp_vertical", "pantheon-mvp-vertical", "mvp-cockpit-api", "PANTHEON_MVP_", "postgresql://pantheon:pantheon@localhost:5433/mvp")\n    offenders = []\n    for root in roots:\n        paths = [root] if root.is_file() else list(root.rglob("*"))\n        for path in paths:\n            if not path.is_file() or path.name == "signer.py":\n                continue\n            try:\n                payload = path.read_text(encoding="utf-8")\n            except UnicodeDecodeError:\n                continue\n            for token in forbidden:\n                if token in payload:\n                    offenders.append(f"{path.relative_to(ROOT)}:{token}")\n    assert not offenders, "retired runtime identity returned: " + ", ".join(offenders)\n'''
if "test_retired_mvp_runtime_identity_does_not_return" not in text:
    posture.write_text(text + addition, encoding="utf-8")

subprocess.run(["python", "-m", "compileall", "-q", "implementation/pantheon_app"], cwd=ROOT, check=True)
subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
SELF.unlink()
