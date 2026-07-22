"""Tests for the transport-neutral Pantheon policy service."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = MODULE_DIR.parent
sys.path.insert(0, str(MODULE_DIR))

from pantheon_mcp import server  # noqa: E402
from pantheon_mcp.service import PantheonPolicyService, repository_commit  # noqa: E402


class TestPantheonPolicyService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = PantheonPolicyService(REPO_ROOT)

    def test_catalog_reports_http_projection_as_partial_not_activated(self):
        report = self.service.consultation_catalog()
        by_id = {item["id"]: item for item in report["surfaces"]}
        http = by_id["http_consultation_api"]
        self.assertEqual(http["status"], "implemented_read_only_partial")
        self.assertIn("internal", http["interface"][0])
        self.assertIn("activation remain to verify", http["limitation"])
        self.assertEqual(report["authorization_effect"], "none")

    def test_service_source_catalog_has_envelope(self):
        report = self.service.list_sources()
        self.assertEqual(report["result"], "listed")
        self.assertGreater(len(report["sources"]), 10)
        self.assertEqual(report["operation"], "sources.list")
        self.assertFalse(report["write_effect"])

    def test_mcp_list_sources_keeps_historical_array_shape(self):
        report = json.loads(server.list_sources())
        self.assertIsInstance(report, list)
        self.assertGreater(len(report), 10)
        self.assertIn("source_file", report[0])

    def test_unknown_source_key_never_becomes_a_path(self):
        report = self.service.read_doctrine("../../etc/passwd")
        self.assertEqual(report["error"], "unknown source key")
        self.assertNotIn("body", report)

    def test_preflight_rejects_insufficient_human_decision_level(self):
        report = self.service.evaluate_preflight(
            {
                "request": {
                    "intent": "Transmit a contractual professional position",
                    "external_effect": True,
                    "transmission_requested": True,
                    "scope": {"scope_type": "project", "scope_id": "fixture"},
                },
                "gate_signals": {
                    "task_contract_ref": "tc-fixture",
                    "evidence_pack_candidate_ref": "epc-fixture",
                    "human_decision_ref": "decision-fixture",
                    "human_decision_level": "C3",
                },
            }
        )
        self.assertEqual(
            report["policy_disposition"], "blocked_pending_human_decision"
        )
        self.assertIn(
            "human_decision_level_at_required_ceiling",
            report["missing_requirements"],
        )
        self.assertFalse(report["external_effect_allowed"])

    def test_repository_commit_is_read_without_shell_execution(self):
        commit = repository_commit(REPO_ROOT)
        self.assertNotEqual(commit, "unknown")
        self.assertGreaterEqual(len(commit), 7)


if __name__ == "__main__":
    unittest.main()
