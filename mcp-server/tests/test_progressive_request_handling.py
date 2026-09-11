"""Regression tests for progressive request handling.

These tests exercise policy projection only. No role is dispatched, no workflow
runs, and no external effect is authorized.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

from pantheon_mcp import policy  # noqa: E402


SCOPE = {"scope_type": "task", "scope_id": "progressive-handling-test"}


class TestProgressiveRequestHandling(unittest.TestCase):
    def test_appointment_confirmation_is_not_professional_confirmation(self):
        report = policy.classify_request(
            {
                "intent": "Améliore ce message : merci de confirmer le rendez-vous de mardi.",
                "requested_transformation": "rewrite",
                "scope": SCOPE,
            }
        )

        self.assertEqual(report["consequence_level"], "K2")
        self.assertEqual(report["handling"]["disposition"], "PROCEED")
        self.assertEqual(report["handling"]["role_viewpoints"], [])
        self.assertIn(
            "preserve_claim_status_and_meaning",
            report["handling"]["constraints"],
        )

    def test_professional_claim_consults_before_effect_gate(self):
        report = policy.classify_request(
            {
                "intent": "Reformuler la réponse au client.",
                "requested_transformation": "rewrite",
                "scope": SCOPE,
                "observations": {
                    "professional_position": True,
                    "source_required": True,
                },
            }
        )

        self.assertEqual(report["consequence_level"], "K4")
        self.assertTrue(report["blocked_until_gate"])
        self.assertEqual(report["handling"]["disposition"], "CONSULT")
        self.assertEqual(report["handling"]["role_viewpoints"], ["ARGOS", "THEMIS"])
        self.assertEqual(
            report["handling"]["topology"]["suggested"],
            "sequential_handoff",
        )
        self.assertEqual(
            report["handling"]["next_state"]["purpose"],
            "establish_factual_basis",
        )
        self.assertFalse(report["handling"]["effect_gate"]["effect_requested_now"])
        self.assertIn(
            "do_not_strengthen_unverified_professional_claim",
            report["handling"]["constraints"],
        )

    def test_source_and_prior_state_use_fanout_then_synthesis(self):
        report = policy.classify_request(
            {
                "intent": "Comparer l'état actuel avec le dernier état connu.",
                "scope": SCOPE,
                "observations": {
                    "source_required": True,
                    "prior_state_required": True,
                },
            }
        )

        self.assertEqual(report["handling"]["disposition"], "CONSULT")
        self.assertEqual(report["handling"]["role_viewpoints"], ["ARGOS", "MNEMOSYNE"])
        self.assertEqual(
            report["handling"]["topology"]["suggested"],
            "fanout_extract_then_single_synthesis",
        )
        self.assertEqual(
            report["handling"]["next_state"]["completion_requires"],
            ["applicable_source_basis_qualified", "current_or_superseded_state_qualified"],
        )

    def test_material_contradiction_proposes_existing_rite(self):
        report = policy.classify_request(
            {
                "intent": "Examiner les pièces disponibles.",
                "scope": SCOPE,
                "observations": {
                    "contradiction_detected": True,
                },
            }
        )

        self.assertEqual(report["handling"]["disposition"], "CONSULT")
        self.assertIn("ARGOS", report["handling"]["role_viewpoints"])
        self.assertEqual(
            report["handling"]["rite_candidate"],
            "concordance_des_sources",
        )

    def test_external_transmission_moves_to_gate(self):
        report = policy.classify_request(
            {
                "intent": "Envoyer la réponse préparée.",
                "scope": SCOPE,
                "transmission_requested": True,
            }
        )

        self.assertEqual(report["consequence_level"], "K4")
        self.assertEqual(report["handling"]["disposition"], "GATE")
        self.assertIn("IRIS", report["handling"]["role_viewpoints"])
        self.assertTrue(report["handling"]["effect_gate"]["effect_requested_now"])
        self.assertEqual(
            report["handling"]["effect_gate"]["required_approval_ceiling"],
            "C4",
        )

    def test_semantic_observations_remain_explicitly_candidate(self):
        report = policy.classify_request(
            {
                "intent": "Examiner ce point.",
                "scope": SCOPE,
                "observations": {"source_required": True},
            }
        )

        self.assertIn(
            "semantic_observations_are_candidates_not_truth",
            report["handling"]["constraints"],
        )
        self.assertIn(
            "source_required",
            report["handling"]["triggers"],
        )


if __name__ == "__main__":
    unittest.main()
