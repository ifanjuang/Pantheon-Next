#!/usr/bin/env bash
# Re-vendor the governance schemas from Pantheon-Next at a given commit.
#
# Re-vendoring is a reviewed change, never automatic. After running this script,
# inspect the diff, reconcile the derived decision vocabulary and run the tests.
set -euo pipefail

SHA="${1:-}"
if [[ -z "$SHA" ]]; then
  echo "usage: tools/revendor.sh <commit-sha>" >&2
  exit 2
fi

REPO="ifanjuang/Pantheon-Next"
RAW="https://raw.githubusercontent.com/${REPO}/${SHA}/schemas"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
VENDOR="${HERE}/mvp_vertical/vendor/pantheon"
SCHEMAS=(
  "mvp_governed_loop_objects.schema.yaml"
  "document_knowledge_slice.schema.yaml"
  "work_issue_slice.schema.yaml"
)

echo "Re-vendoring from ${REPO}@${SHA}"
for name in "${SCHEMAS[@]}"; do
  echo "  fetch schemas/${name}"
  curl -fsSL "${RAW}/${name}" -o "${VENDOR}/${name}"
done

printf '%s\n' "$SHA" > "${VENDOR}/UPSTREAM_COMMIT"
echo "Pinned UPSTREAM_COMMIT -> ${SHA}"

echo
echo "Next steps (not automated — this is a reviewed change):"
echo "  1. git diff mvp_vertical/vendor/pantheon/"
echo "  2. re-sync decision_vocabulary.stand_in.yaml if the decision enum changed"
echo "  3. python tools/check_schema_drift.py"
echo "  4. pytest -q"
