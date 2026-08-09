import copy
from pathlib import Path

import jsonschema
import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "capability_passport.schema.yaml"
EXAMPLE_PATH = ROOT / "schemas" / "examples" / "capability_passport.skill.example.yaml"


def _load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        value = yaml.safe_load(handle)
    assert isinstance(value, dict)
    return value


def _validator() -> jsonschema.Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(schema)


def test_skill_passport_accepts_exact_release_provenance_without_authority_promotion() -> None:
    passport = _load(EXAMPLE_PATH)
    _validator().validate(passport)

    provenance = passport["implementation_provenance"]
    assert provenance["source_kind"] == "repository"
    assert provenance["content_digest"].startswith("sha256:")
    assert passport["status"] == "candidate"
    assert passport["governance"]["activation_state"] == "detected"
    assert passport["governance"]["task_authorization"] == "unauthorized"


def test_same_capability_can_reference_replacement_release_without_identity_change() -> None:
    release_a = _load(EXAMPLE_PATH)
    release_b = copy.deepcopy(release_a)
    release_b["implementation_provenance"]["commit_ref"] = "fedcba9876543210fedcba9876543210fedcba98"
    release_b["implementation_provenance"]["content_digest"] = (
        "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    )

    validator = _validator()
    validator.validate(release_a)
    validator.validate(release_b)

    assert release_a["passport_id"] == release_b["passport_id"]
    assert release_a["capability"] == release_b["capability"]
    assert release_a["implementation_provenance"] != release_b["implementation_provenance"]
    assert release_b["governance"]["task_authorization"] == "unauthorized"


def test_provenance_block_requires_an_immutable_release_anchor() -> None:
    passport = _load(EXAMPLE_PATH)
    provenance = passport["implementation_provenance"]
    provenance.pop("commit_ref")
    provenance.pop("content_digest")
    provenance.pop("package_digest", None)

    with pytest.raises(jsonschema.ValidationError):
        _validator().validate(passport)


def test_package_provenance_reuses_agent_plugin_vocabulary() -> None:
    passport = _load(EXAMPLE_PATH)
    passport["implementation_provenance"] = {
        "source_kind": "agent_plugin",
        "package_name": "example-plugin",
        "package_version": "1.2.3",
        "package_digest": "sha256:" + "c" * 64,
        "component_id": "agent-plugin-component-example",
        "component_kind": "skill",
        "component_ref": "skills/inspect-project-sources/SKILL.md",
        "observed_at": "2026-08-09T18:20:00Z",
    }

    _validator().validate(passport)
    provenance = passport["implementation_provenance"]
    assert set(
        [
            "package_name",
            "package_version",
            "package_digest",
            "component_id",
            "component_kind",
            "component_ref",
        ]
    ).issubset(provenance)


def test_provenance_rejects_unknown_fields_instead_of_becoming_runtime_inventory() -> None:
    passport = _load(EXAMPLE_PATH)
    passport["implementation_provenance"]["installed_path"] = "/runtime/skills/example"

    with pytest.raises(jsonschema.ValidationError):
        _validator().validate(passport)
