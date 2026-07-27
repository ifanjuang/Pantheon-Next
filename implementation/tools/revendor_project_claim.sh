#!/usr/bin/env bash
# Re-vendor only the ProjectClaim governance schema from Pantheon-Next.
set -euo pipefail

SHA="${1:-}"
if [[ -z "$SHA" ]]; then
  echo "usage: tools/revendor_project_claim.sh <commit-sha>" >&2
  exit 2
fi

REPO="ifanjuang/Pantheon-Next"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
VENDOR="${HERE}/mvp_vertical/vendor/pantheon"
URL="https://raw.githubusercontent.com/${REPO}/${SHA}/schemas/project_claim.schema.yaml"

echo "Re-vendoring ProjectClaim from ${REPO}@${SHA}"
curl -fsSL "$URL" -o "${VENDOR}/project_claim.schema.yaml"
printf '%s\n' "$SHA" > "${VENDOR}/PROJECT_CLAIM_UPSTREAM_COMMIT"
echo "Pinned PROJECT_CLAIM_UPSTREAM_COMMIT -> ${SHA}"

echo
echo "Next steps (not automated — this is a reviewed change):"
echo "  1. git diff mvp_vertical/vendor/pantheon/project_claim.schema.yaml"
echo "  2. python tools/check_schema_drift.py --local mvp_vertical/vendor/pantheon/project_claim.schema.yaml"
echo "  3. pytest -q"
