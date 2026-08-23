from __future__ import annotations

from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[2]
RUNTIME = ROOT / "implementation" / "mvp_vertical"
TEST = ROOT / "implementation" / "tests" / "test_canonical_contract_runtime.py"


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"expected text not found in {path.relative_to(ROOT)}: {old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def replace_all(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"expected text not found in {path.relative_to(ROOT)}: {old!r}")
    path.write_text(text.replace(old, new), encoding="utf-8")


# Work Issue aggregate.
path = RUNTIME / "work_issues.py"
replace_once(path, "from .store import dsn_from_env\n", "from . import pantheon_contracts\nfrom .store import dsn_from_env\n")
replace_once(
    path,
    'SCHEMA = (\n    Path(__file__).resolve().parent\n    / "vendor"\n    / "pantheon"\n    / "work_issue_slice.schema.yaml"\n)\n',
    'SCHEMA = pantheon_contracts.schema_path("work_issue_slice")\n',
)

# Agency ProjectClaim aggregate.
path = RUNTIME / "agency_claims.py"
replace_once(path, "from . import agency_schema\n", "from . import agency_schema, pantheon_contracts\n")
replace_once(
    path,
    'SCHEMA = Path(__file__).resolve().parent / "vendor" / "pantheon" / "project_claim.schema.yaml"\n',
    'SCHEMA = pantheon_contracts.schema_path("project_claim")\n',
)
replace_all(path, "vendored Pantheon Next governance schema", "canonical Pantheon Next governance schema")

# Human-governed ProjectClaim candidate.
path = RUNTIME / "project_claim_candidates.py"
replace_once(
    path,
    "from . import agency_claims, agency_schema\n",
    "from . import agency_claims, agency_schema, pantheon_contracts\n",
)
replace_once(
    path,
    'SCHEMA = (\n    Path(__file__).resolve().parent\n    / "vendor"\n    / "pantheon"\n    / "project_claim_candidate.schema.yaml"\n)\n',
    'SCHEMA = pantheon_contracts.schema_path("project_claim_candidate")\n',
)

# Professional document version/currentness contracts.
path = RUNTIME / "project_document_currentness.py"
replace_once(
    path,
    "from . import project_document_admission, project_documents\n",
    "from . import pantheon_contracts, project_document_admission, project_documents\n",
)
replace_once(
    path,
    'VENDOR = Path(__file__).resolve().parent / "vendor" / "pantheon"\nVERSION_EVENT_SCHEMA = VENDOR / "document_version_event.schema.yaml"\nCURRENTNESS_SCHEMA = VENDOR / "document_currentness_projection.schema.yaml"\n',
    'VERSION_EVENT_SCHEMA = pantheon_contracts.schema_path("document_version_event")\nCURRENTNESS_SCHEMA = pantheon_contracts.schema_path("document_currentness_projection")\n',
)

# Decision Request and Decision record schemas.
path = RUNTIME / "decision_requests.py"
replace_once(
    path,
    "from psycopg.rows import dict_row\n\n\nMIGRATION",
    "from psycopg.rows import dict_row\n\nfrom . import pantheon_contracts\n\n\nMIGRATION",
)
replace_once(
    path,
    'REQUEST_SCHEMA = Path(__file__).resolve().parent / "vendor" / "pantheon" / "decision_request.schema.yaml"\nDECISION_SCHEMA = Path(__file__).resolve().parent / "vendor" / "pantheon" / "mvp_governed_loop_objects.schema.yaml"\n',
    'REQUEST_SCHEMA = pantheon_contracts.schema_path("decision_request")\nDECISION_SCHEMA = pantheon_contracts.schema_path("mvp_governed_loop_objects")\n',
)

# Document -> Knowledge contract.
path = RUNTIME / "knowledge.py"
replace_once(
    path,
    "from . import document_structure_read\n",
    "from . import document_structure_read, pantheon_contracts\n",
)
replace_once(
    path,
    'SCHEMA = Path(__file__).resolve().parent / "vendor" / "pantheon" / "document_knowledge_slice.schema.yaml"\n',
    'SCHEMA = pantheon_contracts.schema_path("document_knowledge_slice")\n',
)

# Work Issue scope contract.
path = RUNTIME / "work_issue_scopes.py"
replace_once(path, "from . import work_issues\n", "from . import pantheon_contracts, work_issues\n")
replace_once(
    path,
    'SCHEMA = (\n    Path(__file__).resolve().parent\n    / "vendor"\n    / "pantheon"\n    / "work_issue_scope_link.schema.yaml"\n)\n',
    'SCHEMA = pantheon_contracts.schema_path("work_issue_scope_link")\n',
)

# Project Anatomy owner: preserve its local validator/relative-ref behavior, but
# source every resource from the canonical contract registry rather than an
# independently copied/flattened vendor directory.
path = RUNTIME / "apu_owner.py"
replace_once(
    path,
    "from referencing.jsonschema import DRAFT202012\n\n\nMIGRATION",
    "from referencing.jsonschema import DRAFT202012\n\nfrom . import pantheon_contracts\n\n\nMIGRATION",
)
replace_once(path, 'VENDOR = Path(__file__).resolve().parent / "vendor" / "pantheon"\n', "")
replace_once(
    path,
    '''@lru_cache(maxsize=1)\ndef _registry() -> Registry:\n    resources: list[tuple[str, Resource]] = []\n    for uri, filename in (\n        ("shared.schema.yaml", "apu_shared.schema.yaml"),\n        ("source_representation.schema.yaml", "apu_source_representation.schema.yaml"),\n        ("attribute_claim.schema.yaml", "apu_attribute_claim.schema.yaml"),\n        ("relation_claim.schema.yaml", "apu_relation_claim.schema.yaml"),\n    ):\n        schema = yaml.safe_load((VENDOR / filename).read_text(encoding="utf-8"))\n        resources.append(\n            (uri, Resource.from_contents(schema, default_specification=DRAFT202012))\n        )\n    return Registry().with_resources(resources)\n\n\n@lru_cache(maxsize=None)\ndef _validator(name: str) -> jsonschema.Draft202012Validator:\n    path = VENDOR / f"apu_{name}.schema.yaml"\n    try:\n        schema = yaml.safe_load(path.read_text(encoding="utf-8"))\n    except (OSError, yaml.YAMLError) as exc:\n        raise ApuOwnerError(f"unable to load governed APU schema: {name}") from exc\n    if not isinstance(schema, dict):\n        raise ApuOwnerError(f"governed APU schema must be an object: {name}")\n    jsonschema.Draft202012Validator.check_schema(schema)\n    return jsonschema.Draft202012Validator(\n        schema,\n        format_checker=jsonschema.FormatChecker(),\n        registry=_registry(),\n    )\n''',
    '''@lru_cache(maxsize=1)\ndef _registry() -> Registry:\n    resources: list[tuple[str, Resource]] = []\n    for uri, contract_name in (\n        ("shared.schema.yaml", "apu_shared"),\n        ("source_representation.schema.yaml", "apu_source_representation"),\n        ("attribute_claim.schema.yaml", "apu_attribute_claim"),\n        ("relation_claim.schema.yaml", "apu_relation_claim"),\n    ):\n        schema = pantheon_contracts.load_schema(contract_name)\n        resources.append(\n            (uri, Resource.from_contents(schema, default_specification=DRAFT202012))\n        )\n    return Registry().with_resources(resources)\n\n\n@lru_cache(maxsize=None)\ndef _validator(name: str) -> jsonschema.Draft202012Validator:\n    contract_name = f"apu_{name}"\n    try:\n        schema = pantheon_contracts.load_schema(contract_name)\n    except pantheon_contracts.ContractUnavailable as exc:\n        raise ApuOwnerError(f"unable to load governed APU schema: {name}") from exc\n    if not isinstance(schema, dict):\n        raise ApuOwnerError(f"governed APU schema must be an object: {name}")\n    jsonschema.Draft202012Validator.check_schema(schema)\n    return jsonschema.Draft202012Validator(\n        schema,\n        format_checker=jsonschema.FormatChecker(),\n        registry=_registry(),\n    )\n''',
)

# The new architectural guard must now be clean before we run any broader tests.
subprocess.run(
    ["python", "-m", "pytest", "-q", "--tb=short", str(TEST)],
    cwd=ROOT / "implementation",
    check=True,
)

# The helper is migration-only and must not survive the resulting commit.
Path(__file__).unlink()
