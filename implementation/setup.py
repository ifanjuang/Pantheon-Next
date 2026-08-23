"""Setuptools build hooks for generated Pantheon contract package data.

The canonical schema source remains the monorepo-root ``schemas/`` tree. Before
building a wheel or sdist, this hook stages only the contracts consumed by the
implementation under ``mvp_vertical/_generated_contracts``. That directory is
ignored by Git and exists solely so a built artifact can validate contracts when
installed without a repository checkout.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import runpy
import shutil
import subprocess

from setuptools import setup
from setuptools.command.build_py import build_py as _build_py
from setuptools.command.sdist import sdist as _sdist

PROJECT_ROOT = Path(__file__).resolve().parent
MONOREPO_ROOT = PROJECT_ROOT.parent
PACKAGE_ROOT = PROJECT_ROOT / "mvp_vertical"
GENERATED_ROOT = PACKAGE_ROOT / "_generated_contracts"
MANIFEST_PATH = PACKAGE_ROOT / "contract_manifest.py"

_manifest_module = runpy.run_path(str(MANIFEST_PATH))
CONTRACT_PATHS: dict[str, str] = dict(_manifest_module["CONTRACT_PATHS"])
CANONICAL_REPOSITORY = str(_manifest_module["CANONICAL_REPOSITORY"])


def _git_revision() -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(MONOREPO_ROOT), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            timeout=2,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    value = result.stdout.strip()
    return value if result.returncode == 0 and len(value) == 40 else None


def _stage_contracts() -> None:
    canonical_available = (MONOREPO_ROOT / "schemas").is_dir()
    if not canonical_available:
        # A source distribution already carries the generated contract payload
        # produced from the canonical repository at sdist creation time.
        missing = [
            rel for rel in CONTRACT_PATHS.values() if not (GENERATED_ROOT / rel).is_file()
        ]
        if missing:
            raise RuntimeError(
                "canonical Pantheon schemas are unavailable and the source artifact "
                "does not contain its generated contract payload: " + ", ".join(missing)
            )
        return

    shutil.rmtree(GENERATED_ROOT, ignore_errors=True)
    contracts: list[dict[str, str]] = []
    for name, relative in sorted(CONTRACT_PATHS.items()):
        source = MONOREPO_ROOT / relative
        if not source.is_file():
            raise RuntimeError(f"canonical Pantheon contract is missing: {relative}")
        destination = GENERATED_ROOT / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        raw = source.read_bytes()
        contracts.append(
            {
                "name": name,
                "source_path": relative,
                "sha256": hashlib.sha256(raw).hexdigest(),
            }
        )

    manifest = {
        "kind": "pantheon_generated_contract_payload",
        "source_repository": CANONICAL_REPOSITORY,
        "source_revision": _git_revision(),
        "authority_transfer": False,
        "generated": True,
        "contracts": contracts,
    }
    (GENERATED_ROOT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


class build_py(_build_py):
    def run(self) -> None:
        _stage_contracts()
        super().run()


class sdist(_sdist):
    def run(self) -> None:
        _stage_contracts()
        super().run()


setup(cmdclass={"build_py": build_py, "sdist": sdist})
