"""Regression tests for progressive request handling.

These tests exercise policy projection only. No role is dispatched, no workflow
runs, and no external effect is authorized.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import yaml

MODULE_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = MODULE_DIR.parent
sys.path.insert(0, str(MODULE_DIR))

from pantheon_mcp import policy, request_handling  # noqa: E402


SCOPE = {"scope_type": "task", "scope_id": "progressive-handling-test"}


class TestProgressiveRequestHandling(unittest.TestCase):
    def test_appointment_confirmation_is_harmless_k0_and_needs_no_contract(self):
        report = policy.classify_request(
            {
                "intent": "Améliore ce message : merci de confirmer le rendez-vous de mardi.",
                "requested_transformation": "rewrite",
            }
        )

        self.assertEqual(report["consequence_level"], "K0")
        self.assertFalse(report["task_contract_required"])
        self.assertEqual(report["required_gates"], [])
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
        self.assertIn(
            "legal_or_professional_risk",
            report["handling"]["governance_triggers"],
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
        self.assertIn(
            "project_history_reuse",
            report["handling"]["governance_triggers"],
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
        self.assertIn("evidence_gap", report["handling"]["governance_triggers"])
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
            report["handling"]["observed_conditions"],
        )
        self.assertIn(
            "source_required",
            report["handling"]["governance_triggers"],
        )

    def test_role_trigger_projection_is_subset_of_role_activation_doctrine(self):
        doctrine = (REPO_ROOT / "docs/governance/ROLE_ACTIVATION.md").read_text(
            encoding="utf-8"
        )
        marker = "mandatory_role_triggers:"
        start = doctrine.index(marker)
        end = doctrine.index("```", start)
        parsed = yaml.safe_load(doctrine[start:end])
        canonical = parsed["mandatory_role_triggers"]

        for trigger, roles in request_handling.ROLE_TRIGGER_MAP.items():
            for role in roles:
                self.assertIn(role, canonical, f"role missing from doctrine: {role}")
                self.assertIn(
                    trigger,
                    canonical[role],
                    f"{trigger} -> {role} is not owned by ROLE_ACTIVATION.md",
                )


if __name__ == "__main__":
    unittest.main()
