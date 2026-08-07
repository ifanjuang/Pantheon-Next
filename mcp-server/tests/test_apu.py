"""Read-only tests for the APU validation surface.

They validate fictional candidate dossiers against the governance schemas and
check the V0.2 / V0.1 compatibility posture. They execute nothing, persist
nothing and canonize nothing.
"""

import os
import unittest
from copy import deepcopy
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
        "stable_object": {
            "stable_object_id": "SO-1",
            "project_ref": "PRJ-1",
            "object_family": "spatial",
            "nomenclature": {"display_name": "Chambre 1"},
        },
        "source_representation": {
            "representation_id": "REP-1",
            "project_ref": "PRJ-1",
            "source_artifact_ref": "SRC-1",
            "source_kind": "drawing",
            "identifiers": [
                {"scheme": "drawing.fragment", "value": "bedroom-polygon-1"}
            ],
            "observed_at": "2026-08-07T12:00:00Z",
            "binding_ref": "binding.drawing.fixture",
            "adapter_version": "0.2-test",
            "freshness_token": "fixture-revision-1",
            "proof_status": "candidate",
        },
        "requirement": {
            "requirement_id": "REQ-1",
            "source": {"source_type": "program", "source_ref": "PRG-1"},
            "requirement_kind": "attribute",
            "target": {
                "entity_ref": {"entity_type": "stable_object", "entity_id": "SO-1"}
            },
            "constraint": {
                "operator": "min",
                "attribute_key": "area",
                "expected_value": {
                    "value_type": "number",
                    "value": 9,
                    "unit": "m2",
                },
            },
            "source_authority": "approved_client_decision",
            "proof_status": "accepted_as_support",
        },
        "attribute_claim": {
            "attribute_claim_id": "AC-1",
            "subject_ref": {
                "entity_type": "source_representation",
                "entity_id": "REP-1",
            },
            "attribute_key": "area",
            "value": {"value_type": "number", "value": 8.4, "unit": "m2"},
            "assertion_mode": "observed",
            "source_authority": "project_working_document",
            "proof_status": "candidate",
            "source_representation_refs": ["REP-1"],
        },
        "relation_claim": {
            "relation_claim_id": "REL-ID-1",
            "subject_ref": {
                "entity_type": "source_representation",
                "entity_id": "REP-1",
            },
            "relation_type": "identity.represents",
            "object_ref": {"entity_type": "stable_object", "entity_id": "SO-1"},
            "assertion_mode": "proposed",
            "source_authority": "model_interpretation_candidate",
            "proof_status": "candidate",
            "source_representation_refs": ["REP-1"],
        },
    }


class TestApuValidation(unittest.TestCase):
    def test_v02_dossier_is_ok_and_candidate_only(self):
        report = apu.validate_apu_dossier(_clean_dossier())
        self.assertEqual(report["result"], "ok", report)
        self.assertEqual(report["validated"], 6)
        self.assertEqual(report["canonical_validated"], 6)
        self.assertEqual(report["compatibility_validated"], 0)
        self.assertFalse(report["schema_errors"], report["schema_errors"])
        self.assertFalse(report["reference_errors"], report["reference_errors"])
        self.assertEqual(report["gate"]["posture"], "candidate-only")
        self.assertTrue(report["gate"]["canonical_emission_allowed"])
        self.assertFalse(report["gate"]["canonical_effect"])
        self.assertTrue(
            any(
                "identity relation remains candidate" in item
                for item in report["gate"]["human_decisions_required"]
            )
        )
        self.assertFalse(report["compatibility"]["legacy_detected"])

    def test_legacy_regulatory_claim_without_approval_is_flagged_without_promotion(self):
        legacy = {
            "stable_object": {
                "stable_object_id": "SO-LEGACY-1",
                "human_ref": "Porte existante",
                "kind": "opening",
                "proof_status": "candidate",
                "scope_type": "project",
                "scope_id": "PRJ-1",
            },
            "attribute_claim": {
                "attribute_claim_id": "AC-LEGACY-1",
                "about": {
                    "stable_object_id": "SO-LEGACY-1",
                    "attribute": "clear_width",
                },
                "modality": "observed",
                "value": {"mm": 900},
                "source_authority": "model_interpretation_candidate",
                "proof_status": "requires_more_evidence",
                "approval_state": "candidate",
                "allowed_use": ["regulatory_claim"],
                "forbidden_use": ["contractual_action"],
            },
        }
        report = apu.validate_apu_dossier(legacy)
        self.assertEqual(report["result"], "error", report)
        self.assertEqual(report["gate"]["posture"], "compatibility-only")
        self.assertFalse(report["gate"]["canonical_emission_allowed"])
        self.assertTrue(report["gate"]["regulatory_claims_without_approval"])
        self.assertTrue(report["compatibility"]["legacy_detected"])
        self.assertTrue(
            any("dropped embedded governance" in item for item in report["compatibility"]["warnings"])
        )

    def test_unresolved_v02_reference_is_reported(self):
        dossier = _clean_dossier()
        dossier["requirement"]["target"]["entity_ref"]["entity_id"] = "SO-MISSING"
        report = apu.validate_apu_dossier(dossier)
        self.assertEqual(report["result"], "error", report)
        self.assertTrue(
            any("target.entity_ref" in item and "unresolved" in item for item in report["reference_errors"]),
            report["reference_errors"],
        )

    def test_unknown_object_type_is_reported(self):
        report = apu.validate_apu_dossier({"not_a_real_type": {}})
        self.assertEqual(report["result"], "error", report)
        self.assertTrue(any("unknown object type" in item for item in report["schema_errors"]))



def _legacy_object_model_dossier() -> dict:
    """Coherent V0.1 object-model input retained only for compatibility reads."""
    return {
        "stable_object": [
            {
                "stable_object_id": "OBJ-DOOR-1",
                "human_ref": "Porte 1",
                "kind": "opening",
                "proof_status": "candidate",
                "scope_type": "project",
                "scope_id": "PRJ-1",
            },
            {
                "stable_object_id": "OBJ-WALL-1",
                "human_ref": "Mur 1",
                "kind": "boundary",
                "proof_status": "candidate",
                "scope_type": "project",
                "scope_id": "PRJ-1",
            },
        ],
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


class TestApuV01Compatibility(unittest.TestCase):
    def test_legacy_object_model_is_readable_but_never_canonical_emission(self):
        report = apu.validate_apu_dossier(_legacy_object_model_dossier())
        self.assertEqual(report["result"], "ok", report)
        self.assertEqual(report["canonical_validated"], 2)
        self.assertEqual(report["compatibility_validated"], 8)
        self.assertFalse(report["reference_errors"], report["reference_errors"])
        self.assertEqual(report["gate"]["posture"], "compatibility-only")
        self.assertFalse(report["gate"]["canonical_emission_allowed"])
        self.assertFalse(report["gate"]["canonical_effect"])
        self.assertIn("object_relation", report["compatibility"]["deprecated_input_types"])
        self.assertIn("spatial_node", report["compatibility"]["deprecated_input_types"])

    def test_dangling_legacy_relation_target_is_still_reported(self):
        dossier = deepcopy(_legacy_object_model_dossier())
        dossier["object_relation"]["to"] = "OBJ-DOES-NOT-EXIST"
        report = apu.validate_apu_dossier(dossier)
        self.assertEqual(report["result"], "error", report)
        self.assertTrue(
            any(".to" in item and "unresolved" in item for item in report["reference_errors"]),
            report["reference_errors"],
        )

    def test_legacy_inline_match_is_not_invented_as_source_representation(self):
        dossier = {
            "stable_object": {
                "stable_object_id": "SO-LEGACY-MATCH",
                "human_ref": "Porte historique",
                "kind": "opening",
                "proof_status": "candidate",
                "scope_type": "project",
                "scope_id": "PRJ-1",
                "matches": [
                    {
                        "source_candidate_id": "OP-CAND-088",
                        "source_artifact_id": "SRC-042",
                        "certainty": "E3",
                        "status": "candidate",
                        "match_axis": "cross_source",
                    }
                ],
            }
        }
        report = apu.validate_apu_dossier(dossier)
        self.assertEqual(report["result"], "ok", report)
        self.assertEqual(report["gate"]["posture"], "compatibility-only")
        self.assertFalse(report["gate"]["canonical_emission_allowed"])
        self.assertEqual(report["compatibility"]["unprojected_legacy_matches"], 1)
        self.assertTrue(
            any("no source_representation" in item for item in report["compatibility"]["warnings"])
        )


if __name__ == "__main__":
    unittest.main()
