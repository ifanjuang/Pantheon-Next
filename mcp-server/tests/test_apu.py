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
        self.assertTrue(any("requirement_id unresolved" in r for r in report["reference_errors"]))

    def test_unknown_object_type_is_reported(self):
        report = apu.validate_apu_dossier({"not_a_real_type": {}})
        self.assertEqual(report["result"], "error", report)
        self.assertTrue(any("unknown object type" in e for e in report["schema_errors"]))


if __name__ == "__main__":
    unittest.main()
