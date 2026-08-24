#!/usr/bin/env bash
set -euo pipefail

: "${GITHUB_WORKSPACE:?}"
: "${RUNNER_TEMP:?}"

IMPLEMENTATION_ROOT="$GITHUB_WORKSPACE/monorepo/implementation"
BASE_SCRIPT="$IMPLEMENTATION_ROOT/tools/run_hermes_020_lab_acceptance.sh"
VARIANT_SCRIPT="$RUNNER_TEMP/run-hermes-020-variant-lab.sh"

python - "$BASE_SCRIPT" "$VARIANT_SCRIPT" <<'PY'
from pathlib import Path
import sys

source = Path(sys.argv[1]).read_text(encoding="utf-8")
replacements = {
    "python tools/hermes_020_lab_fixture.py": "python tools/hermes_020_variant_lab_fixture.py",
    "python tools/run_hermes_020_lab_acceptance.py": "python tools/run_hermes_020_variant_lab_acceptance.py",
}
for old, new in replacements.items():
    if old not in source:
        raise SystemExit(f"variant laboratory overlay marker is missing: {old}")
    source = source.replace(old, new)
Path(sys.argv[2]).write_text(source, encoding="utf-8")
PY

chmod +x "$VARIANT_SCRIPT"
exec "$VARIANT_SCRIPT"
