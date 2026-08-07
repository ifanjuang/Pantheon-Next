"""Tests for the explicit Project Anatomy V0.1 compatibility projection."""

import os
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("PANTHEON_REPO_PATH", str(ROOT))

from pantheon_mcp.apu_compat import (  # noqa: E402
    adapt_v01_dossier,
    compatibility_only_types,
    load_compatibility_registry,
)


class TestApuCompatibilityRegistry(unittest.TestCase):
    def test_deprecated_carriers_are_never_canonical_emission(self):
        registry = load_compatibility_registry()
        entries = registry["entries"]
        for name in compatibility_only_types():
            self.assertEqual(entries[name]["status"], "compatibility_only")
            self.assertIs(entries[name]["canonical_emission"], False)
            self.assertTrue(entries[name]["replacement"])
        self.assertIn("object_relation", compatibility_only_types())
        self.assertIn("object_identity", compatibility_only_types())
        self.assertNotIn("relation_claim", compatibility_only_types())


class TestApuCompatibilityProjection(unittest.TestCase):
    def test_legacy_inline_match_is_retained_as_warning_not_invented_relation(self):
        legacy = {
            "stable_object": {
                "stable_object_id": "SO-LEGACY",
                "human_ref": "Porte historique",
                "kind": "opening",
                "proof_status": "candidate",
                "scope_type": "project",
                "scope_id": "PRJ-1",
                "matches": [
                    {
                        "source_candidate_id": "OP-CAND-1",
                        "source_artifact_id": "SRC-1",
                        "certainty": "E3",
                        "status": "candidate",
                        "match_axis": "cross_source",
                    }
                ],
            }
        }
        adapted = adapt_v01_dossier(legacy)
        canonical = adapted["canonical_dossier"]
        report = adapted["compatibility"]
        self.assertEqual(canonical["stable_object"][0]["stable_object_id"], "SO-LEGACY")
        self.assertNotIn("source_representation", canonical)
        self.assertNotIn("relation_claim", canonical)
        self.assertEqual(report["unprojected_legacy_matches"], 1)
        self.assertTrue(report["legacy_detected"])
        self.assertFalse(report["canonical_emission_allowed"])
        self.assertFalse(report["authority_transfer"])

    def test_legacy_requirement_and_claim_map_only_mechanical_fields(self):
        legacy = {
            "requirement": {
                "requirement_id": "REQ-AREA",
                "from_program": "PRG-1",
                "modality": "required",
                "kind": "area_min",
                "target": {"space_function": "bedroom"},
                "value": {"m2": 9},
                "scope_type": "project",
                "scope_id": "PRJ-1",
                "source_authority": "approved_client_decision",
                "proof_status": "accepted_as_support",
            },
            "attribute_claim": {
                "attribute_claim_id": "AC-AREA",
                "about": {"stable_object_id": "SO-1", "attribute": "area"},
                "modality": "observed",
                "value": {"m2": 8.4},
                "source_authority": "project_working_document",
                "proof_status": "candidate",
                "approval_state": "candidate",
                "allowed_use": ["internal_review"],
            },
        }
        adapted = adapt_v01_dossier(legacy)
        requirement = adapted["canonical_dossier"]["requirement"][0]
        claim = adapted["canonical_dossier"]["attribute_claim"][0]
        self.assertEqual(requirement["source"], {"source_type": "program", "source_ref": "PRG-1"})
        self.assertEqual(requirement["constraint"]["operator"], "min")
        self.assertEqual(requirement["constraint"]["expected_value"]["unit"], "m2")
        self.assertEqual(claim["subject_ref"], {"entity_type": "stable_object", "entity_id": "SO-1"})
        self.assertEqual(claim["value"]["unit"], "m2")
        self.assertNotIn("approval_state", claim)
        self.assertNotIn("allowed_use", claim)
        self.assertTrue(
            any("dropped embedded governance" in item for item in adapted["compatibility"]["warnings"])
        )

    def test_required_legacy_attribute_claim_is_not_converted_into_observed_fact(self):
        legacy = {
            "attribute_claim": {
                "attribute_claim_id": "AC-REQUIRED",
                "about": {"stable_object_id": "SO-1", "attribute": "area"},
                "modality": "required",
                "value": {"m2": 9},
                "source_authority": "approved_client_decision",
                "proof_status": "accepted_as_support",
            }
        }
        adapted = adapt_v01_dossier(legacy)
        self.assertNotIn("attribute_claim", adapted["canonical_dossier"])
        self.assertTrue(
            any("prescriptive intent must migrate as requirement" in item for item in adapted["compatibility"]["errors"])
        )
        self.assertFalse(adapted["compatibility"]["canonical_emission_allowed"])

    def test_compatibility_only_carrier_is_preserved_outside_canonical_dossier(self):
        legacy = {
            "object_relation": {
                "relation_id": "REL-OLD",
                "type": "opens_to",
                "from": "SO-A",
                "to": "SO-B",
            }
        }
        adapted = adapt_v01_dossier(legacy)
        self.assertNotIn("object_relation", adapted["canonical_dossier"])
        self.assertIn("object_relation", adapted["compatibility_records"])
        self.assertIn("object_relation", adapted["compatibility"]["deprecated_input_types"])
        self.assertFalse(adapted["compatibility"]["canonical_emission_allowed"])


if __name__ == "__main__":
    unittest.main()
