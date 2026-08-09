from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs" / "governance" / "CAPABILITY_REGISTRY.md"
WORKFLOW_SCHEMA = ROOT / "schemas" / "workflow_manifest.schema.yaml"
SKILL_SCHEMA = ROOT / "schemas" / "skill_manifest.schema.yaml"


def test_capability_registry_does_not_require_skill_identity_equality() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")

    assert "skill_manifest.skill_id  ==  capability_step.capability_id" not in registry
    assert "There is no required identifier equality between `capability_id` and `skill_id`." in registry
    assert "Capability != Skill" in registry


def test_existing_schemas_keep_capability_and_backing_skill_as_separate_fields() -> None:
    workflow = WORKFLOW_SCHEMA.read_text(encoding="utf-8")
    skill = SKILL_SCHEMA.read_text(encoding="utf-8")

    assert "capability_id:" in workflow
    assert "skill_manifest_ref:" in workflow
    assert "Optional join to the admitted skill backing this step" in workflow
    assert "skill_id:" in skill


def test_identity_separation_is_semantic_not_a_lexical_inequality_rule() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")

    assert "Identifiers may happen to use the same lexical string" in registry
    assert "Such equality never establishes identity, admission, binding or authorization." in registry
