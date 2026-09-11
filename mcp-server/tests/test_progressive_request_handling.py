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
    def test_harmless_rewrite_exits_at_k0_without_contract(self):
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

    def test_source_basis_precedes_consequential_judgement(self):
        report = policy.classify_request(
            {
                "intent": "Reformuler une réponse qui porte une position engageante.",
                "requested_transformation": "rewrite",
                "scope": SCOPE,
                "professional_position": True,
                "conditions": ["source_required", "legal_or_professional_risk"],
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
            report["handling"]["completion_requirements"],
            ["supporting_basis_qualified", "consequence_boundary_reviewed"],
        )
        self.assertFalse(report["handling"]["effect_gate"]["effect_requested_now"])
        self.assertIn(
            "do_not_increase_claim_authority_without_support",
            report["handling"]["constraints"],
        )

    def test_source_and_continuity_use_fanout_then_synthesis(self):
        report = policy.classify_request(
            {
                "intent": "Comparer l'état actuel avec un état antérieur.",
                "scope": SCOPE,
                "conditions": ["source_required", "project_history_reuse"],
            }
        )

        self.assertEqual(report["handling"]["disposition"], "CONSULT")
        self.assertEqual(report["handling"]["role_viewpoints"], ["ARGOS", "MNEMOSYNE"])
        self.assertEqual(
            report["handling"]["topology"]["suggested"],
            "fanout_extract_then_single_synthesis",
        )
        self.assertEqual(
            report["handling"]["completion_requirements"],
            ["supporting_basis_qualified", "current_state_qualified"],
        )

    def test_conflict_proposes_existing_rite_without_new_conflict_schema(self):
        report = policy.classify_request(
            {
                "intent": "Examiner des éléments contradictoires.",
                "scope": SCOPE,
                "conditions": ["evidence_gap"],
                "conflict_detected": True,
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
                "conditions": ["external_transmission"],
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

    def test_declared_conditions_remain_candidate_inputs(self):
        report = policy.classify_request(
            {
                "intent": "Examiner ce point.",
                "scope": SCOPE,
                "conditions": ["source_required"],
            }
        )

        self.assertIn(
            "declared_conditions_are_candidates_not_truth",
            report["handling"]["constraints"],
        )
        self.assertEqual(report["handling"]["conditions"], ["source_required"])

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
