"""Read-only validation tests for the generic registry foundation."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_registry_foundation_validator() -> None:
    result = subprocess.run(
        [sys.executable, ".github/scripts/check_registry_foundation.py"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_registry_foundation_starts_without_business_registries() -> None:
    business_registries = sorted((ROOT / "registries").rglob("*.registry.json"))
    assert business_registries == []
