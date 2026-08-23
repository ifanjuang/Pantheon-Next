import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "mvp_vertical" / "vendor" / "pantheon"


def test_project_claim_schema_is_vendored_and_pinned_separately() -> None:
    schema = yaml.safe_load((VENDOR / "project_claim.schema.yaml").read_text(encoding="utf-8"))
    assert schema["title"] == "Pantheon Next Project Claim"
    assert schema["x-boundary"]["system_of_record_mutation"] is False
    assert "backing_ref" in schema["properties"]

    # What this asserts is *separation*: ProjectClaim was reconciled later and
    # carries its own pin, so refreshing the governed-loop lineage does not imply
    # ProjectClaim was re-reviewed. Freezing either value as a literal asserted
    # something else — that neither pin ever moves — and broke the first time the
    # global pin was legitimately corrected. The sidecars are what tie a pin to
    # exact bytes; tests/test_vendored_contract_conformance.py checks those.
    global_pin = (VENDOR / "UPSTREAM_COMMIT").read_text(encoding="utf-8").strip()
    claim_pin = (VENDOR / "PROJECT_CLAIM_UPSTREAM_COMMIT").read_text(encoding="utf-8").strip()
    assert re.fullmatch(r"[0-9a-f]{40}", global_pin), global_pin
    assert re.fullmatch(r"[0-9a-f]{40}", claim_pin), claim_pin
    assert global_pin != claim_pin, "ProjectClaim must keep a pin of its own"


def test_project_claim_has_dedicated_revendor_helper() -> None:
    common = (ROOT / "tools" / "revendor.sh").read_text(encoding="utf-8")
    dedicated = (ROOT / "tools" / "revendor_project_claim.sh").read_text(encoding="utf-8")
    assert '"project_claim.schema.yaml"' not in common
    assert "project_claim.schema.yaml" in dedicated
    assert "PROJECT_CLAIM_UPSTREAM_COMMIT" in dedicated
