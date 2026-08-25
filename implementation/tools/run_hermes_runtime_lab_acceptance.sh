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

MONOREPO_ROOT="$GITHUB_WORKSPACE/monorepo"
IMPLEMENTATION_ROOT="$MONOREPO_ROOT/implementation"
DISTRIBUTION_AUTHORITY_ROOT="$GITHUB_WORKSPACE/distribution-authority"
UPSTREAM_ROOT="$GITHUB_WORKSPACE/hermes-upstream"
LAB_ROOT="$RUNNER_TEMP/hermes-runtime-lab"
LAB_ARTIFACTS="$LAB_ROOT/artifacts"
HERMES_HOME="$LAB_ROOT/hermes-home"
HERMES_VENV="$LAB_ROOT/venv"
HERMES_SOURCE_DIR="$LAB_ROOT/source/hermes-agent-$HERMES_VERSION"
SOURCE_ARCHIVE="$LAB_ROOT/dist/hermes-agent-$HERMES_VERSION-source.tar.gz"

if [ -z "${PANTHEON_CONTEXT_PLUGIN_SOURCE:-}" ]; then
  PANTHEON_CONTEXT_PLUGIN_SOURCE="file://$MONOREPO_ROOT#implementation/hermes/plugins/pantheon-context-bridge"
fi

export LAB_ROOT LAB_ARTIFACTS HERMES_HOME HERMES_VENV HERMES_SOURCE_DIR
export PANTHEON_HERMES_API_BASE="${PANTHEON_HERMES_API_BASE:-$FIXTURE_URL}"
export PANTHEON_HERMES_API_KEY="${PANTHEON_HERMES_API_KEY:-pantheon-lab-key}"
export PANTHEON_HERMES_ACTOR="${PANTHEON_HERMES_ACTOR:-hermes-runtime-lab-binding}"

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
    "$HERMES_VENV/bin/hermes" -p "$PROFILE" plugins disable pantheon-context-bridge \
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
git archive --format=tar.gz --prefix="hermes-agent-$HERMES_VERSION/" \
  --output "$SOURCE_ARCHIVE" HEAD
printf 'sha256:%s\n' "$(sha256sum "$SOURCE_ARCHIVE" | awk '{print $1}')" \
  > "$LAB_ARTIFACTS/hermes-source-artifact.sha256"
printf '%s\n' "$SOURCE_ARCHIVE" > "$LAB_ARTIFACTS/hermes-source-artifact-path.txt"
git show -s --format='%H%n%G?%n%GS%n%s' HEAD \
  > "$LAB_ARTIFACTS/hermes-source-commit.txt"
tar -xzf "$SOURCE_ARCHIVE" -C "$LAB_ROOT/source"
grep -F "version = \"$HERMES_VERSION\"" "$HERMES_SOURCE_DIR/pyproject.toml"

phase "Install exact Hermes source and Pantheon bridge"
cd "$IMPLEMENTATION_ROOT"
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
import os
assert importlib.metadata.version("hermes-agent") == os.environ["HERMES_VERSION"]
PY

phase "Verify three-component distribution"
pantheon-hermes verify-distribution \
  --manifest hermes/distribution/pantheon-standard.lock.yaml \
  --schema "$DISTRIBUTION_AUTHORITY_ROOT/templates/hermes/distribution/distribution-lock.schema.yaml" \
  --monorepo-root "$MONOREPO_ROOT" \
  --output "$LAB_ARTIFACTS/distribution-verification.json"
python - <<'PY'
import json, os
from pathlib import Path
value = json.loads((Path(os.environ["LAB_ARTIFACTS"]) / "distribution-verification.json").read_text())
assert value["revision"] == 3
assert value["status"] == "candidate"
assert [item["component_id"] for item in value["components"]] == [
    "run-binding", "context-bridge", "runtime-observer"
]
assert all("source_repository" not in item for item in value["components"])
assert value["authority_effect"] == "none"
PY

phase "Start deterministic local fixtures"
python tools/hermes_runtime_lab_fixture.py \
  --journal "$LAB_ARTIFACTS/fixture-journal.jsonl" \
  > "$LAB_ARTIFACTS/fixture.log" 2>&1 &
FIXTURE_PID=$!
python tools/run_hermes_runtime_lab_acceptance.py wait-http \
  --url "$FIXTURE_URL/health" \
  --timeout 30 \
  --output "$LAB_ARTIFACTS/fixture-health.json"

phase "Create isolated governed profile"
hermes profile create "$PROFILE" --no-skills --no-alias
python tools/run_hermes_runtime_lab_acceptance.py configure \
  --hermes-home "$HERMES_HOME" \
  --fixture-url "$FIXTURE_URL" \
  --output "$LAB_ARTIFACTS/lab-configuration.json"

phase "Lock governed tool policy"
# The qualified Hermes release treats BFL as a recently-shipped core toolset and may add it
# back to an explicitly saved platform list until the operator has declined it.
# Use Hermes' supported final override instead of widening Pantheon's allowlist.
hermes -p "$PROFILE" config set agent.disabled_toolsets '["bfl"]' \
  > "$LAB_ARTIFACTS/tool-policy-set.txt"
hermes -p "$PROFILE" config get agent.disabled_toolsets \
  | tee "$LAB_ARTIFACTS/tool-policy-disabled.txt"
grep -F 'bfl' "$LAB_ARTIFACTS/tool-policy-disabled.txt"

phase "Install governed profile plugin disabled"
PLUGIN_SOURCE="$PANTHEON_CONTEXT_PLUGIN_SOURCE"
hermes -p "$PROFILE" plugins install "$PLUGIN_SOURCE" --no-enable \
  > "$LAB_ARTIFACTS/plugin-install.txt" 2>&1
PLUGIN_INSTALLED=true
PLUGIN_DIR="$HERMES_HOME/profiles/$PROFILE/plugins/pantheon-context-bridge"
test -f "$PLUGIN_DIR/plugin.yaml"
test -f "$PLUGIN_DIR/__init__.py"
find "$PLUGIN_DIR" -type f -not -path '*/.git/*' -print0 \
  | sort -z \
  | xargs -0 sha256sum \
  > "$LAB_ARTIFACTS/plugin-files.sha256"
hermes -p "$PROFILE" plugins list --plain --no-bundled \
  > "$LAB_ARTIFACTS/plugins-before-enable.txt"

phase "Enable governed profile plugin explicitly"
hermes -p "$PROFILE" plugins enable pantheon-context-bridge \
  > "$LAB_ARTIFACTS/plugin-enable.txt"
PLUGIN_ENABLED=true
hermes -p "$PROFILE" plugins list --plain --no-bundled \
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
python tools/run_hermes_runtime_lab_acceptance.py wait-http \
  --url "http://127.0.0.1:8642/health" \
  --timeout 90 \
  --output "$LAB_ARTIFACTS/gateway-health.json"
python tools/run_hermes_runtime_lab_acceptance.py wait-http \
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

phase "Observe route, official toolset envelope and memory"
pantheon-hermes capture-memory-status \
  --profile "$PROFILE" \
  --hermes-command "$HERMES_VENV/bin/hermes" \
  --output "$LAB_ARTIFACTS/memory-status-observe.json"
pantheon-hermes observe \
  --expected-profile "$PROFILE" \
  --memory-status-receipt "$LAB_ARTIFACTS/memory-status-observe.json" \
  --allowed-tool pantheon_context_manifest \
  --allowed-tool pantheon_context_entity \
  --required-tool pantheon_context_manifest \
  --required-tool pantheon_context_entity \
  --output "$LAB_ARTIFACTS/runtime-observation.json"

phase "Launch one synthetic admitted read-only run"
pantheon-hermes capture-memory-status \
  --profile "$PROFILE" \
  --hermes-command "$HERMES_VENV/bin/hermes" \
  --output "$LAB_ARTIFACTS/memory-status-launch.json"
pantheon-hermes launch \
  --expected-profile "$PROFILE" \
  --memory-status-receipt "$LAB_ARTIFACTS/memory-status-launch.json" \
  --allowed-tool pantheon_context_manifest \
  --allowed-tool pantheon_context_entity \
  --required-tool pantheon_context_manifest \
  --required-tool pantheon_context_entity \
  --admission-id admission-hermes-020-lab \
  --idempotency-key hermes-020-lab-launch \
  --output "$LAB_ARTIFACTS/launch-receipt.json"
RUN_ID="$(python -c 'import json,os,pathlib; print(json.loads((pathlib.Path(os.environ["LAB_ARTIFACTS"])/"launch-receipt.json").read_text())["run_id"])')"
python tools/run_hermes_runtime_lab_acceptance.py wait-run \
  --base-url "$HERMES_API_BASE" \
  --api-key "$HERMES_API_KEY" \
  --run-id "$RUN_ID" \
  --timeout 120 \
  --output "$LAB_ARTIFACTS/run-terminal.json"

phase "Reconcile exactly once"
pantheon-hermes reconcile \
  --receipt "$LAB_ARTIFACTS/launch-receipt.json" \
  --idempotency-key hermes-020-lab-reconcile \
  --output "$LAB_ARTIFACTS/return-receipt.json"
python tools/run_hermes_runtime_lab_acceptance.py wait-http \
  --url "$FIXTURE_URL/_lab/state" \
  --timeout 10 \
  --output "$LAB_ARTIFACTS/fixture-state.json"

phase "Disable profile plugin and stop gateway"
hermes -p "$PROFILE" plugins disable pantheon-context-bridge \
  > "$LAB_ARTIFACTS/plugin-disable.txt"
PLUGIN_ENABLED=false
kill "$GATEWAY_PID"
wait "$GATEWAY_PID" 2>/dev/null || true
GATEWAY_PID=""
sleep 1
if curl --silent --fail --max-time 2 \
    -H "Authorization: Bearer $HERMES_API_KEY" \
    "$HERMES_API_BASE/v1/capabilities" >/dev/null; then
  echo "profile route remained reachable after gateway rollback" >&2
  exit 1
fi
printf '{"gateway_stopped":true,"profile_route_unreachable":true,"plugin_disabled":true}\n' \
  > "$LAB_ARTIFACTS/rollback.json"

phase "Validate technical receipts"
python tools/run_hermes_runtime_lab_acceptance.py validate \
  --artifacts "$LAB_ARTIFACTS"
cat "$LAB_ARTIFACTS/acceptance-summary.json" >> "$GITHUB_STEP_SUMMARY"

phase "Laboratory acceptance complete"
