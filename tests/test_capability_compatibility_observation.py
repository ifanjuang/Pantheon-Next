import copy
import json
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "catalog" / "schemas" / "capability-compatibility-observation.schema.json"
EXAMPLE_PATH = ROOT / "catalog" / "observations" / "document-analysis-docling-compatibility.yaml"
BINDING_PATH = ROOT / "catalog" / "bindings" / "document-analysis-docling.yaml"


def _load_yaml(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _validator() -> jsonschema.Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(schema)


def test_compatibility_observation_is_exact_release_and_non_authorizing() -> None:
    observation = _load_yaml(EXAMPLE_PATH)
    binding = _load_yaml(BINDING_PATH)
    _validator().validate(observation)

    assert observation["subject"]["binding_id"] == binding["metadata"]["id"]
    assert observation["subject"]["implementation_anchor"] == binding["spec"]["implementation_anchor"]
    assert observation["observation"]["compatibility_status"] == "compatible"
    assert observation["observation"]["safety_status"] == "not_evaluated"
    assert observation["governance"]["authorization_effect"] == "none"
    assert observation["governance"]["activation_effect"] == "none"
    assert observation["governance"]["evidence_effect"] == "none"


def test_compatibility_safety_and_health_are_independent_axes() -> None:
    observation = _load_yaml(EXAMPLE_PATH)
    changed = copy.deepcopy(observation)
    changed["observation"]["compatibility_status"] = "compatible"
    changed["observation"]["safety_status"] = "not_qualified"
    changed["observation"]["health_status"] = "healthy"

    _validator().validate(changed)
    assert changed["observation"]["compatibility_status"] == "compatible"
    assert changed["observation"]["safety_status"] == "not_qualified"
    assert changed["observation"]["health_status"] == "healthy"
    assert changed["governance"]["professional_approval_effect"] == "none"


def test_stale_observation_remains_observation_not_evidence_or_authorization() -> None:
    observation = _load_yaml(EXAMPLE_PATH)
    observation["metadata"]["status"] = "stale"
    observation["observation"]["freshness_status"] = "stale"

    _validator().validate(observation)
    assert observation["governance"]["authorization_effect"] == "none"
    assert observation["governance"]["evidence_effect"] == "none"


def test_replacement_release_requires_distinct_observation_lineage() -> None:
    release_a = _load_yaml(EXAMPLE_PATH)
    release_b = copy.deepcopy(release_a)
    release_b["metadata"]["id"] = "capability_compatibility_document_analysis_docling_release_b"
    release_b["subject"]["implementation_anchor"]["value"] = "sha256:" + "b" * 64
    release_b["observation"]["source_observation_ref"] = "observation.document_analysis.docling.release_b"
    release_b["supersedes"] = release_a["metadata"]["id"]

    _validator().validate(release_a)
    _validator().validate(release_b)

    assert release_a["subject"]["binding_id"] == release_b["subject"]["binding_id"]
    assert release_a["subject"]["implementation_anchor"] != release_b["subject"]["implementation_anchor"]
    assert release_b["supersedes"] == release_a["metadata"]["id"]
    assert release_b["governance"]["release_replacement_inherits_observation"] is False
