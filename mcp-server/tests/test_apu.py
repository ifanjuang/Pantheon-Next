"""Read-only tests for the APU validation surface.

They validate fictional candidate dossiers against the governance schemas and
check the gate posture. They execute nothing and canonize nothing.
"""

import os
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("PANTHEON_REPO_PATH", str(ROOT))

from pantheon_mcp import apu  # noqa: E402


def _clean_dossier() -> dict:
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
            "from_program": "PRG-1",
            "modality": "required",
            "kind": "area_min",
            "target": {"space_function": "bedroom"},
            "value": {"m2": 9},
        },
        "stable_object": {
            "stable_object_id": "SO-1",
            "kind": "space",
            "proof_status": "candidate",
        },
        "deviation": {
            "deviation_id": "DEV-1",
            "requirement_id": "REQ-1",
            "observed_target": "SO-1",
            "kind": "area_below_min",
            "resolution": "pending_human",
        },
    }


class TestApuValidation(unittest.TestCase):
    def test_clean_dossier_is_ok_and_candidate_only(self):
        report = apu.validate_apu_dossier(_clean_dossier())
        self.assertEqual(report["result"], "ok", report)
        self.assertEqual(report["validated"], 4)
        self.assertFalse(report["schema_errors"], report["schema_errors"])
        self.assertFalse(report["reference_errors"], report["reference_errors"])
        self.assertEqual(report["gate"]["posture"], "candidate-only")
        self.assertFalse(report["gate"]["canonical_effect"])
        # the pending deviation must surface as a human decision
        self.assertTrue(
            any("deviation pending" in h for h in report["gate"]["human_decisions_required"])
        )

    def test_regulatory_claim_without_approval_is_flagged(self):
        d = _clean_dossier()
        d["attribute_claim"] = {
            "attribute_claim_id": "AC-1",
            "about": {"stable_object_id": "SO-1", "attribute": "clear_width"},
            "source_authority": "model_interpretation_candidate",
            "proof_status": "requires_more_evidence",
            "allowed_use": ["regulatory_claim"],
        }
        report = apu.validate_apu_dossier(d)
        self.assertEqual(report["result"], "error", report)
        # either the schema allOf or the gate surfaces it; assert the gate does
        self.assertTrue(report["gate"]["regulatory_claims_without_approval"])

    def test_unresolved_reference_is_reported(self):
        d = _clean_dossier()
        d["deviation"]["requirement_id"] = "REQ-DOES-NOT-EXIST"
        report = apu.validate_apu_dossier(d)
        self.assertEqual(report["result"], "error", report)
        self.assertTrue(
            any("requirement_id" in r and "unresolved" in r for r in report["reference_errors"]),
            report["reference_errors"],
        )

    def test_unknown_object_type_is_reported(self):
        report = apu.validate_apu_dossier({"not_a_real_type": {}})
        self.assertEqual(report["result"], "error", report)
        self.assertTrue(any("unknown object type" in e for e in report["schema_errors"]))


def _object_model_dossier() -> dict:
    """A coherent project-object-model dossier whose every reference resolves
    against an in-dossier id (no external prefixes needed)."""
    return {
        "object_identity": [
            {"stable_id": "OBJ-DOOR-1", "object_kind": "opening"},
            {"stable_id": "OBJ-WALL-1", "object_kind": "boundary"},
        ],
        "object_group": {
            "object_group_id": "GRP-1",
            "kind": "opening_group",
            "members": ["OBJ-DOOR-1"],
        },
        "property_set": {
            "property_set_id": "PSET-1",
            "applies_to": "GRP-1",
            "property_set_type": "fire_properties",
            "claims": [
                {
                    "property_key": "fire_resistance_class",
                    "value": "EI30",
                    "value_type": "controlled_label",
                    "status": "specified_candidate",
                }
            ],
        },
        "instance_override": {
            "instance_override_id": "OVR-1",
            "target": "OBJ-DOOR-1",
            "overrides": "PSET-1.fire_resistance_class",
            "value": "EI60",
            "status": "to_verify",
        },
        "object_relation": {
            "relation_id": "REL-1",
            "type": "mounted_on",
            "from": "OBJ-DOOR-1",
            "to": "OBJ-WALL-1",
        },
        "spatial_node": [
            {"spatial_node_id": "BLD-1", "node_kind": "building"},
            {
                "spatial_node_id": "ZONE-1",
                "node_kind": "zone",
                "zone_type": "functional",
                "parent_id": "BLD-1",
                "member_object_ids": ["OBJ-DOOR-1"],
            },
        ],
    }


class TestApuObjectModel(unittest.TestCase):
    def test_object_model_references_resolve(self):
        report = apu.validate_apu_dossier(_object_model_dossier())
        self.assertEqual(report["result"], "ok", report)
        self.assertEqual(report["validated"], 8)
        self.assertFalse(report["reference_errors"], report["reference_errors"])
        self.assertEqual(report["gate"]["posture"], "candidate-only")
        self.assertFalse(report["gate"]["canonical_effect"])

    def test_dangling_relation_target_is_reported(self):
        d = _object_model_dossier()
        d["object_relation"]["to"] = "OBJ-DOES-NOT-EXIST"
        report = apu.validate_apu_dossier(d)
        self.assertEqual(report["result"], "error", report)
        self.assertTrue(
            any(".to" in r and "unresolved" in r for r in report["reference_errors"]),
            report["reference_errors"],
        )


if __name__ == "__main__":
    unittest.main()
