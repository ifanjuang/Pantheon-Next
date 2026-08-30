"""Temporary #827 diagnostic: expose the post-#874 baseline observation in CI.

This file deliberately reuses the existing professional baseline test as the
single harness owner. It fails after capturing that test's observation so the
exact post-#874 result is visible in GitHub Actions. It is diagnostic-only and
must not be merged.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


BASELINE_PATH = Path(__file__).with_name("test_professional_quote_review_baseline.py")


def _load_baseline_module():
    spec = importlib.util.spec_from_file_location("q827_professional_baseline", BASELINE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_expose_post874_professional_baseline_observation(capsys) -> None:
    baseline = _load_baseline_module()
    baseline.test_current_project_aware_professional_review_baseline_is_observed_not_assumed()
    captured = capsys.readouterr().out
    marker = "PROFESSIONAL_QUOTE_REVIEW_BASELINE="
    observation = next(
        (line for line in captured.splitlines() if line.startswith(marker)),
        None,
    )
    assert observation is not None
    pytest.fail(observation, pytrace=False)
