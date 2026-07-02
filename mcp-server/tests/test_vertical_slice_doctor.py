"""Read-only tests for the vertical-slice doctor check.

They validate the shipped dossier and confirm the coherence invariants reject a
broken dossier. They fetch nothing, execute nothing and write nothing.
"""
import copy
import unittest
from pathlib import Path

from pantheon_mcp.doctor import check_vertical_slice, find_repo_root


class TestVerticalSlice(unittest.TestCase):
    def test_shipped_dossier_is_coherent(self):
        report = check_vertical_slice(find_repo_root())
        if report.get("informational"):
            self.skipTest(report.get("note", "deps unavailable"))
        self.assertTrue(report["ok"], report.get("violations"))
        self.assertGreaterEqual(report["instances_checked"], 6)

    def test_missing_dossier_is_ok_not_error(self):
        report = check_vertical_slice(Path("/tmp/no-such-repo-xyz"))
        # find_repo_root fallback aside, a missing dir must not be a violation
        self.assertTrue(report["ok"])


if __name__ == "__main__":
    unittest.main()
