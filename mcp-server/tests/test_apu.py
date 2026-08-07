"""Read-only tests for the APU V0.2 validation surface.

They validate fictional candidate dossiers against governance schemas and ensure
that V0.2 is canonical-write while selected V0.1 carriers remain explicit
legacy-read compatibility only. They execute nothing and canonize nothing.
"""

import os
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("PANTHEON_REPO_PATH", str(ROOT))

from pantheon_mcp import apu  # noqa: E402


def _v02_dossier() -> dict:
    return {
        "program": {
            "program_id": "PRG-1",
            "program_type": "housing",
            "program_layer": "specific_requirement",
            "source_authority": "approved_client_decision",
            "proof_status": "accepted_as_support",
        },
        "requirement": {
            "requirement_id": "REQ-1",
            "origin": {"origin_kind": "program", "origin_ref": "PRG-1"},
            "kind": "attribute",
            "target": {
                "selector": {"classification": {"scheme": "architecture.space", "value": "bedroom"}},
                "attribute_key": "geometry.net_area",
            },
            "operator": "gte",
            "expected_value": {"value_type": "number", "value": 9, "unit": "m2"},
            "source_authority": "approved_client_decision",
            "proof_status": "accepted_as_support",
        },
        "stable_object": {
            "stable_object_id": "DOOR-1",
            "project_ref": "PRJ-1",
            "object_family": "element",
            "nomenclature": {"display_name": "Porte D1"},
        },
        "source_representation": {
            "representation_id": "REP-RVT-1",
            "project_ref": "PRJ-1",
            "source_artifact_ref": "REVIT-MODEL-1",
            "source_kind": "revit",
            "identifiers": [{"scheme": "revit.element_id", "value": "40291"}],
            "observed_at": "2026-08-07T15:15:00Z",
            "technical_status": "observed",
        },
        "attribute_claim": {
            "attribute_claim_id": "AC-1",
            "subject_ref": {"entity_type": "source_representation", "entity_id": "REP-RVT-1"},
            "attribute_key": "architecture.clear_width",
            "value": {"value_type": "number", "value": 830, "unit": "mm"},
            "assertion_mode": "observed",
            "source_authority": "project_working_document",
            "proof_status": "source_complete_for_task",
            "source_representation_refs": ["REP-RVT-1"],
        },
        "relation_claim": {
            "relation_claim_id": "RC-1",
            "subject_ref": {"entity_type": "source_representation", "entity_id": "REP-RVT-1"},
            "relation_type": "identity.represents",
            "object_ref": {"entity_type": "stable_object", "entity_id": "DOOR-1"},
            "assertion_mode": "proposed",
            "source_authority": "model_interpretation_candidate",
            "proof_status": "candidate",
            "certainty": "E3",
            "source_representation_refs": ["REP-RVT-1"],
        },
    }


class TestApuV02Validation(unittest.TestCase):
    def test_v02_dossier_is_ok_candidate_only_and_canonical(self):
        report = apu.validate_apu_dossier(_v02_dossier())
        self.assertEqual(report["result"], "ok", report)
        self.assertEqual(report["validated"], 6)
        self.assertFalse(report["schema_errors"], report["schema_errors"])
        self.assertFalse(report["reference_errors"], report["reference_errors"])
        self.assertFalse(report["compatibility"]["legacy_read"])
        self.assertFalse(report["compatibility"]["legacy_objects"])
        self.assertEqual(report["gate"]["posture"], "candidate-only")
        self.assertFalse(report["gate"]["canonical_effect"])
        self.assertTrue(
            any("identity match" in item for item in report["gate"]["human_decisions_required"]),
            report["gate"]["human_decisions_required"],
        )

    def test_source_claim_can_exist_before_project_identity_resolution(self):
        dossier = _v02_dossier()
        dossier.pop("stable_object")
        dossier.pop("relation_claim")
        report = apu.validate_apu_dossier(
            {
                "source_representation": dossier["source_representation"],
                "attribute_claim": dossier["attribute_claim"],
            }
        )
        self.assertEqual(report["result"], "ok", report)
        self.assertFalse(report["reference_errors"], report["reference_errors"])

    def test_dangling_relation_target_is_reported(self):
        dossier = _v02_dossier()
        dossier["relation_claim"]["object_ref"]["entity_id"] = "DOOR-DOES-NOT-EXIST"
        report = apu.validate_apu_dossier(dossier)
        self.assertEqual(report["result"], "error", report)
        self.assertTrue(
            any("object_ref.entity_id" in item and "unresolved" in item for item in report["reference_errors"]),
            report["reference_errors"],
        )

    def test_v02_claim_cannot_self_grant_approval_or_use(self):
        dossier = _v02_dossier()
        dossier["attribute_claim"]["approval_state"] = "approved_for_contractual_action"
        dossier["attribute_claim"]["allowed_use"] = ["regulatory_claim"]
        report = apu.validate_apu_dossier(dossier)
        self.assertEqual(report["result"], "error", report)
        self.assertTrue(
            any("additional properties" in item.lower() for item in report["schema_errors"]),
            report["schema_errors"],
        )
        self.assertFalse(report["gate"]["regulatory_claims_without_approval"])

    def test_legacy_carrier_is_readable_but_explicitly_flagged(self):
        report = apu.validate_apu_dossier(
            {"object_identity": {"stable_id": "OBJ-LEGACY-1", "object_kind": "opening"}}
        )
        self.assertEqual(report["result"], "ok", report)
        self.assertTrue(report["compatibility"]["legacy_read"])
        self.assertEqual(report["compatibility"]["legacy_objects"], ["object_identity[0]"])
        self.assertNotIn("object_identity", report["compatibility"]["canonical_write_types"])

    def test_unknown_object_type_is_reported(self):
        report = apu.validate_apu_dossier({"not_a_real_type": {}})
        self.assertEqual(report["result"], "error", report)
        self.assertTrue(any("unknown object type" in item for item in report["schema_errors"]))


if __name__ == "__main__":
    unittest.main()
