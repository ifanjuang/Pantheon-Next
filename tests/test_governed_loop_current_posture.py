from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOOP = ROOT / "docs/governance/GOVERNED_TASK_LOOP.md"


def test_governed_loop_declares_current_partial_posture_without_adoption() -> None:
    text = LOOP.read_text(encoding="utf-8")

    assert "Status: candidate support doctrine" in text
    assert "co-located candidate implementation exists" in text
    assert "documented non-implemented" not in text
    assert "implementation_present != adopted" in text
    assert "synthetic_demonstration != real_dossier_acceptance" in text
    assert "runtime_success != authorization" in text
    assert "memory != Evidence" in text
    assert "not real-dossier acceptance" in text


def test_governed_loop_current_implementation_owners_remain_present() -> None:
    required = (
        "implementation/pantheon_app/contract.py",
        "implementation/pantheon_app/runner.py",
        "implementation/pantheon_app/terminal_gate_standin.py",
        "implementation/pantheon_app/register.py",
        "schemas/governed_loop_objects.schema.yaml",
        "ai_logs/2026-07-10-mvp-loop-first-demonstration.md",
    )

    for relative in required:
        assert (ROOT / relative).is_file(), relative


def test_governed_loop_no_longer_describes_an_external_schema_owner() -> None:
    text = LOOP.read_text(encoding="utf-8")

    assert "external binding vendors the schema" not in text.lower()
    assert "pantheon_contracts" in text
    assert "No second vocabulary owner is needed" in text


ACTIVE_IDENTITY_PATH_ROOTS = (
    ROOT / "implementation",
    ROOT / "docs/governance",
    ROOT / "schemas",
    ROOT / "scripts",
    ROOT / "tests",
)


def test_retired_mvp_generation_name_does_not_return_to_active_paths() -> None:
    offenders = []
    for root in ACTIVE_IDENTITY_PATH_ROOTS:
        for path in root.rglob("*"):
            relative = path.relative_to(ROOT).as_posix()
            if relative.startswith(("implementation/ai_logs/", "docs/audits/")):
                continue
            if relative == "docs/governance/authority/OBSOLETE_AND_ABSENT_INDEX.md":
                continue
            if "mvp" in path.name.lower():
                offenders.append(relative)
    assert not offenders, "retired MVP-named active paths: " + ", ".join(offenders)
