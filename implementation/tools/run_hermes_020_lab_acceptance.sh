#!/usr/bin/env bash
set -euo pipefail

: "${GITHUB_WORKSPACE:?}"
: "${RUNNER_TEMP:?}"
: "${GITHUB_STEP_SUMMARY:=/dev/null}"
: "${HERMES_RELEASE_COMMIT:?}"
: "${HERMES_VERSION:?}"
: "${PROFILE:=pantheon-governed}"
: "${PROFILE_KEY:=hermes-profile-lab-key}"
: "${FIXTURE_URL:=http://127.0.0.1:9010}"
: "${HERMES_API_BASE:=http://127.0.0.1:8642/p/pantheon-governed}"
: "${HERMES_API_KEY:=$PROFILE_KEY}"

MVP_ROOT="$GITHUB_WORKSPACE/pantheon-mvp"
NEXT_ROOT="$GITHUB_WORKSPACE/Pantheon-Next"
UPSTREAM_ROOT="$GITHUB_WORKSPACE/hermes-upstream"
LAB_ROOT="$RUNNER_TEMP/hermes-020-lab"
LAB_ARTIFACTS="$LAB_ROOT/artifacts"
HERMES_HOME="$LAB_ROOT/hermes-home"
HERMES_VENV="$LAB_ROOT/venv"
HERMES_SOURCE_DIR="$LAB_ROOT/source/hermes-agent-0.20.0"
SOURCE_ARCHIVE="$LAB_ROOT/dist/hermes-agent-0.20.0-source.tar.gz"
PANTHEON_CONTEXT_PLUGIN_SOURCE="${PANTHEON_CONTEXT_PLUGIN_SOURCE:-file://$MVP_ROOT#hermes/plugins/pantheon-context-bridge}"

export LAB_ROOT LAB_ARTIFACTS HERMES_HOME HERMES_VENV HERMES_SOURCE_DIR
export PANTHEON_HERMES_API_BASE="${PANTHEON_HERMES_API_BASE:-$FIXTURE_URL}"
export PANTHEON_HERMES_API_KEY="${PANTHEON_HERMES_API_KEY:-pantheon-lab-key}"
export PANTHEON_HERMES_ACTOR="${PANTHEON_HERMES_ACTOR:-hermes-020-lab-binding}"

mkdir -p "$LAB_ARTIFACTS" "$LAB_ROOT/dist" "$LAB_ROOT/source"
FIXTURE_PID=""
GATEWAY_PID=""
PLUGIN_INSTALLED=false
PLUGIN_ENABLED=false

phase() {
  printf '\n== %s ==\n' "$1"
}

cleanup() {
  set +e
  if [ "$PLUGIN_ENABLED" = true ] && [ -x "$HERMES_VENV/bin/hermes" ]; then
    "$HERMES_VENV/bin/hermes" plugins disable pantheon-context-bridge \
      > "$LAB_ARTIFACTS/plugin-disable-cleanup.txt" 2>&1
  fi
  if [ -n "$GATEWAY_PID" ]; then
    kill "$GATEWAY_PID" 2>/dev/null || true
    wait "$GATEWAY_PID" 2>/dev/null || true
  fi
  if [ -n "$FIXTURE_PID" ]; then
    kill "$FIXTURE_PID" 2>/dev/null || true
    wait "$FIXTURE_PID" 2>/dev/null || true
  fi
}
trap cleanup EXIT

phase "Create exact source artifact"
cd "$UPSTREAM_ROOT"
test "$(git rev-parse HEAD)" = "$HERMES_RELEASE_COMMIT"
git archive --format=tar.gz --prefix=hermes-agent-0.20.0/ \
  --output "$SOURCE_ARCHIVE" HEAD
printf 'sha256:%s\n' "$(sha256sum "$SOURCE_ARCHIVE" | awk '{print $1}')" \
  > "$LAB_ARTIFACTS/hermes-source-artifact.sha256"
printf '%s\n' "$SOURCE_ARCHIVE" > "$LAB_ARTIFACTS/hermes-source-artifact-path.txt"
git show -s --format='%H%n%G?%n%GS%n%s' HEAD \
  > "$LAB_ARTIFACTS/hermes-source-commit.txt"
tar -xzf "$SOURCE_ARCHIVE" -C "$LAB_ROOT/source"
grep -F 'version = "0.20.0"' "$HERMES_SOURCE_DIR/pyproject.toml"

phase "Install exact Hermes source and Pantheon bridge"
cd "$MVP_ROOT"
python -m pip install --disable-pip-version-check --upgrade uv
python -m venv "$HERMES_VENV"
uv pip install --python "$HERMES_VENV/bin/python" \
  -e "$HERMES_SOURCE_DIR" \
  "aiohttp==3.14.1"
uv pip install --python "$HERMES_VENV/bin/python" -e .
export PATH="$HERMES_VENV/bin:$PATH"
hermes --version | tee "$LAB_ARTIFACTS/hermes-version.txt"
grep -F "$HERMES_VERSION" "$LAB_ARTIFACTS/hermes-version.txt"
python - <<'PY'
import importlib.metadata
assert importlib.metadata.version("hermes-agent") == "0.20.0"
PY

phase "Verify three-component distribution"
pantheon-hermes verify-distribution \
  --manifest hermes/distribution/pantheon-standard.lock.yaml \
  --schema "$NEXT_ROOT/templates/hermes/distribution/distribution-lock.schema.yaml" \
  --mvp-root "$MVP_ROOT" \
  --next-root "$NEXT_ROOT" \
  --output "$LAB_ARTIFACTS/distribution-verification.json"
python - <<'PY'
import json, os
from pathlib import Path
value = json.loads((Path(os.environ["LAB_ARTIFACTS"]) / "distribution-verification.json").read_text())
assert value["status"] == "candidate"
assert [item["component_id"] for item in value["components"]] == [
    "run-binding", "context-bridge", "runtime-observer"
]
assert value["authority_effect"] == "none"
PY

phase "Start deterministic local fixtures"
python tools/hermes_020_lab_fixture.py \
  --journal "$LAB_ARTIFACTS/fixture-journal.jsonl" \
  > "$LAB_ARTIFACTS/fixture.log" 2>&1 &
FIXTURE_PID=$!
python tools/run_hermes_020_lab_acceptance.py wait-http \
  --url "$FIXTURE_URL/health" \
  --timeout 30 \
  --output "$LAB_ARTIFACTS/fixture-health.json"

phase "Create isolated governed profile"
hermes profile create "$PROFILE" --no-skills --no-alias
python tools/run_hermes_020_lab_acceptance.py configure \
  --hermes-home "$HERMES_HOME" \
  --fixture-url "$FIXTURE_URL" \
  --output "$LAB_ARTIFACTS/lab-configuration.json"

phase "Install gateway plugin disabled"
PLUGIN_SOURCE="$PANTHEON_CONTEXT_PLUGIN_SOURCE"
hermes plugins install "$PLUGIN_SOURCE" --no-enable \
  > "$LAB_ARTIFACTS/plugin-install.txt" 2>&1
PLUGIN_INSTALLED=true
PLUGIN_DIR="$HERMES_HOME/plugins/pantheon-context-bridge"
test -f "$PLUGIN_DIR/plugin.yaml"
test -f "$PLUGIN_DIR/__init__.py"
find "$PLUGIN_DIR" -type f -not -path '*/.git/*' -print0 \
  | sort -z \
  | xargs -0 sha256sum \
  > "$LAB_ARTIFACTS/plugin-files.sha256"
hermes plugins list --plain --no-bundled \
  > "$LAB_ARTIFACTS/plugins-before-enable.txt"

phase "Enable gateway plugin explicitly"
hermes plugins enable pantheon-context-bridge \
  > "$LAB_ARTIFACTS/plugin-enable.txt"
PLUGIN_ENABLED=true
hermes plugins list --plain --no-bundled \
  > "$LAB_ARTIFACTS/plugins-after-enable.txt"
grep -F "pantheon-context-bridge" "$LAB_ARTIFACTS/plugins-after-enable.txt"

phase "Qualify governed memory before startup"
pantheon-hermes capture-memory-status \
  --profile "$PROFILE" \
  --hermes-command "$HERMES_VENV/bin/hermes" \
  --output "$LAB_ARTIFACTS/memory-status-prestart.json"
python - <<'PY'
import json, os
from pathlib import Path
value = json.loads((Path(os.environ["LAB_ARTIFACTS"]) / "memory-status-prestart.json").read_text())
assert value["status"] == "qualified", value
assert value["active_axes"] == []
assert value["missing_axes"] == []
PY

phase "Start real multiplexing gateway"
HERMES_PLUGINS_DEBUG=1 hermes gateway run \
  > "$LAB_ARTIFACTS/hermes-gateway.log" 2>&1 &
GATEWAY_PID=$!
python tools/run_hermes_020_lab_acceptance.py wait-http \
  --url "http://127.0.0.1:8642/health" \
  --timeout 90 \
  --output "$LAB_ARTIFACTS/gateway-health.json"
python tools/run_hermes_020_lab_acceptance.py wait-http \
  --url "$HERMES_API_BASE/v1/capabilities" \
  --bearer "$HERMES_API_KEY" \
  --timeout 90 \
  --output "$LAB_ARTIFACTS/profile-capabilities.json"

phase "Prove profile-specific authentication"
if curl --silent --fail --max-time 5 \
    -H "Authorization: Bearer hermes-default-lab-key" \
    "$HERMES_API_BASE/v1/capabilities" >/dev/null; then
  echo "default API key unexpectedly authenticated the named profile route" >&2
  exit 1
fi
printf '{"profile_key_accepted":true,"default_key_rejected":true}\n' \
  > "$LAB_ARTIFACTS/profile-authentication.json"

phase "Capture memory posture after startup"
pantheon-hermes capture-memory-status \
  --profile "$PROFILE" \
  --hermes-command "$HERMES_VENV/bin/hermes" \
  --output "$LAB_ARTIFACTS/memory-status-poststart.json"
python - <<'PY'
import json, os
from pathlib import Path
value = json.loads((Path(os.environ["LAB_ARTIFACTS"]) / "memory-status-poststart.json").read_text())
assert value["status"] == "qualified", value
assert value["active_axes"] == []
assert value["missing_axes"] == []
PY

phase "Execute one admitted read-only run"
python tools/run_hermes_020_lab_acceptance.py execute \
  --api-base "$HERMES_API_BASE" \
  --api-key "$HERMES_API_KEY" \
  --output "$LAB_ARTIFACTS/run-result.json"

phase "Validate bounded result and no-authority posture"
python tools/run_hermes_020_lab_acceptance.py validate \
  --artifacts "$LAB_ARTIFACTS"

phase "Rollback profile and plugin"
hermes plugins disable pantheon-context-bridge \
  > "$LAB_ARTIFACTS/plugin-disable.txt"
PLUGIN_ENABLED=false
hermes profile delete "$PROFILE" --yes \
  > "$LAB_ARTIFACTS/profile-delete.txt"
printf '{"profile_removed":true,"plugin_disabled":true,"production_activation":false}\n' \
  > "$LAB_ARTIFACTS/rollback.json"

printf '\n## Hermes 0.20.0 laboratory acceptance\n\n' >> "$GITHUB_STEP_SUMMARY"
printf -- '- exact source commit: `%s`\n' "$HERMES_RELEASE_COMMIT" >> "$GITHUB_STEP_SUMMARY"
printf -- '- observed version: `%s`\n' "$HERMES_VERSION" >> "$GITHUB_STEP_SUMMARY"
printf -- '- profile: `%s`\n' "$PROFILE" >> "$GITHUB_STEP_SUMMARY"
printf -- '- production activation: `false`\n' >> "$GITHUB_STEP_SUMMARY"
printf -- '- task authorization side effect: `false`\n' >> "$GITHUB_STEP_SUMMARY"
printf -- '- Evidence admission side effect: `false`\n' >> "$GITHUB_STEP_SUMMARY"
printf -- '- memory posture: `qualified / all axes off`\n' >> "$GITHUB_STEP_SUMMARY"
