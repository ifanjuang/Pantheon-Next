from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "templates/source_research_summary_workflow_manifest.template.yaml"
SCHEMA = ROOT / "schemas/workflow_manifest.schema.yaml"
REGISTRY = ROOT / "templates/TEMPLATE_REGISTRY.md"


def _load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_source_research_summary_manifest_conforms_to_current_schema():
    manifest = _load_yaml(MANIFEST)
    schema = _load_yaml(SCHEMA)

    errors = sorted(
        Draft202012Validator(schema).iter_errors(manifest),
        key=lambda error: list(error.absolute_path),
    )
    assert not errors, "\n".join(
        f"{list(error.absolute_path)}: {error.message}" for error in errors
    )


def test_source_research_summary_manifest_reuses_existing_source_boundaries():
    manifest = _load_yaml(MANIFEST)
    text = MANIFEST.read_text(encoding="utf-8")

    assert manifest["workflow_id"] == "research.multi_source_summary"
    assert manifest["reasoning_topology_requirements"]["default_topology"] == (
        "fanout_extract_then_single_synthesis"
    )
    assert set(manifest["reasoning_topology_requirements"]["allowed_topologies"]) == {
        "single_primary_reasoning_context",
        "fanout_extract_then_single_synthesis",
    }

    assert "workspace source-notebook entries as seed sources" in text
    assert "task-relevant references discovered inside inspected sources" in text
    assert "discovered references are Source Leads" in text
    assert "never implied by a Markdown link" in text
    assert "unbounded crawling" in text
    assert "unbounded_recursive_crawl" in text
    assert "recursive crawl is not a default behavior" in text
    assert "same URL may expose different content" in text
    assert "Research outputs, source leads, caches, and summaries do not promote themselves" in text


def test_source_research_summary_manifest_is_registered_once():
    registry = REGISTRY.read_text(encoding="utf-8")
    manifest_path = "templates/source_research_summary_workflow_manifest.template.yaml"
    assert registry.count(manifest_path) == 1
