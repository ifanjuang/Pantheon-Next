from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "mvp_vertical" / "vendor" / "pantheon"


def test_project_claim_schema_is_vendored_and_pinned_separately() -> None:
    schema = yaml.safe_load((VENDOR / "project_claim.schema.yaml").read_text(encoding="utf-8"))
    assert schema["title"] == "Pantheon Next Project Claim"
    assert schema["x-boundary"]["system_of_record_mutation"] is False
    assert "backing_ref" in schema["properties"]

    global_pin = (VENDOR / "UPSTREAM_COMMIT").read_text(encoding="utf-8").strip()
    claim_pin = (VENDOR / "PROJECT_CLAIM_UPSTREAM_COMMIT").read_text(encoding="utf-8").strip()
    assert global_pin == "f8bc3bde142d1e105b7c9a966d8e0d62b39918c4"
    assert claim_pin == "375fc115d2e946b82dbd27eb430d31c84a95236d"


def test_project_claim_has_dedicated_revendor_helper() -> None:
    common = (ROOT / "tools" / "revendor.sh").read_text(encoding="utf-8")
    dedicated = (ROOT / "tools" / "revendor_project_claim.sh").read_text(encoding="utf-8")
    assert '"project_claim.schema.yaml"' not in common
    assert "project_claim.schema.yaml" in dedicated
    assert "PROJECT_CLAIM_UPSTREAM_COMMIT" in dedicated
