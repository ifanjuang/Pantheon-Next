#!/usr/bin/env bash
set -euo pipefail

: "${OBSIDIAN_SYNC_EMAIL:?missing OBSIDIAN_SYNC_EMAIL}"
: "${OBSIDIAN_SYNC_PASSWORD:?missing OBSIDIAN_SYNC_PASSWORD}"
: "${OBSIDIAN_SYNC_VAULT:?missing OBSIDIAN_SYNC_VAULT}"
: "${PANTHEON_Q2A_RUN_ID:?missing PANTHEON_Q2A_RUN_ID}"

EXPECTED_VERSION="0.0.14"
ROOT="${RUNNER_TEMP:-/tmp}/obsidian-headless-sync-q2a"
A="$ROOT/device-a"
B="$ROOT/device-b"
ARTIFACTS="$ROOT/artifacts"
PREFIX="pantheon-q2a-${PANTHEON_Q2A_RUN_ID}"
mkdir -p "$A" "$B" "$ARTIFACTS"

cleanup() {
  if [[ -n "${CONTINUOUS_PID:-}" ]]; then
    kill "$CONTINUOUS_PID" 2>/dev/null || true
    wait "$CONTINUOUS_PID" 2>/dev/null || true
  fi
  ob sync-unlink --path "$A" >/dev/null 2>&1 || true
  ob sync-unlink --path "$B" >/dev/null 2>&1 || true
  ob logout >/dev/null 2>&1 || true
}
trap cleanup EXIT

actual_version="$(npm view obsidian-headless version)"
installed_version="$(npm list -g obsidian-headless --json | python -c 'import json,sys; print(json.load(sys.stdin)["dependencies"]["obsidian-headless"]["version"])')"
test "$actual_version" = "$EXPECTED_VERSION"
test "$installed_version" = "$EXPECTED_VERSION"

# Dedicated synthetic account/vault only. No production or governed Pantheon path is mounted here.
ob login --email "$OBSIDIAN_SYNC_EMAIL" --password "$OBSIDIAN_SYNC_PASSWORD" >/dev/null
ob sync-list-remote --json > "$ARTIFACTS/remote-vaults.json"
python - "$ARTIFACTS/remote-vaults.json" "$OBSIDIAN_SYNC_VAULT" <<'PY'
import json, sys
payload = json.load(open(sys.argv[1], encoding="utf-8"))
needle = sys.argv[2]
text = json.dumps(payload)
if needle not in text:
    raise SystemExit("configured synthetic vault was not visible to the account")
PY

setup_vault() {
  local path="$1"
  local device="$2"
  local args=(sync-setup --vault "$OBSIDIAN_SYNC_VAULT" --path "$path" --device-name "$device" --json)
  if [[ -n "${OBSIDIAN_SYNC_E2EE_PASSWORD:-}" ]]; then
    args+=(--password "$OBSIDIAN_SYNC_E2EE_PASSWORD")
  fi
  ob "${args[@]}" > "$ARTIFACTS/setup-${device}.json"
  ob sync-config --path "$path" --mode bidirectional --conflict-strategy conflict >/dev/null
  ob sync --path "$path"
}

setup_vault "$A" "pantheon-q2a-a-${PANTHEON_Q2A_RUN_ID}"
setup_vault "$B" "pantheon-q2a-b-${PANTHEON_Q2A_RUN_ID}"

mkdir -p "$A/$PREFIX"
printf 'create:%s\n' "$PANTHEON_Q2A_RUN_ID" > "$A/$PREFIX/crud.md"
ob sync --path "$A"
ob sync --path "$B"
grep -q "create:$PANTHEON_Q2A_RUN_ID" "$B/$PREFIX/crud.md"

printf 'edit:%s\n' "$PANTHEON_Q2A_RUN_ID" > "$A/$PREFIX/crud.md"
ob sync --path "$A"
ob sync --path "$B"
grep -q "edit:$PANTHEON_Q2A_RUN_ID" "$B/$PREFIX/crud.md"

mv "$A/$PREFIX/crud.md" "$A/$PREFIX/renamed.md"
ob sync --path "$A"
ob sync --path "$B"
test -f "$B/$PREFIX/renamed.md"
test ! -f "$B/$PREFIX/crud.md"

rm "$A/$PREFIX/renamed.md"
ob sync --path "$A"
ob sync --path "$B"
test ! -f "$B/$PREFIX/renamed.md"

# Local work while the continuous sync loop is absent, followed by explicit reconvergence.
printf 'stopped-loop:%s\n' "$PANTHEON_Q2A_RUN_ID" > "$A/$PREFIX/stopped-loop.md"
ob sync --path "$A"
ob sync --path "$B"
grep -q "stopped-loop:$PANTHEON_Q2A_RUN_ID" "$B/$PREFIX/stopped-loop.md"

# Concurrent edits from the same synchronized base. The conflict strategy must preserve both markers somewhere.
printf 'base:%s\n' "$PANTHEON_Q2A_RUN_ID" > "$A/$PREFIX/conflict.md"
ob sync --path "$A"
ob sync --path "$B"
printf 'device-a:%s\n' "$PANTHEON_Q2A_RUN_ID" > "$A/$PREFIX/conflict.md"
printf 'device-b:%s\n' "$PANTHEON_Q2A_RUN_ID" > "$B/$PREFIX/conflict.md"
ob sync --path "$A"
ob sync --path "$B"
ob sync --path "$A"
find "$A/$PREFIX" "$B/$PREFIX" -maxdepth 1 -type f -print > "$ARTIFACTS/conflict-files.txt"
grep -R -q "device-a:$PANTHEON_Q2A_RUN_ID" "$A/$PREFIX" "$B/$PREFIX"
grep -R -q "device-b:$PANTHEON_Q2A_RUN_ID" "$A/$PREFIX" "$B/$PREFIX"

# One long-running materializer. Device B stays one-shot and represents the other client side.
ob sync --continuous --path "$A" > "$ARTIFACTS/continuous-a.log" 2>&1 &
CONTINUOUS_PID=$!
sleep 3
kill -0 "$CONTINUOUS_PID"
printf 'continuous:%s\n' "$PANTHEON_Q2A_RUN_ID" > "$B/$PREFIX/continuous.md"
ob sync --path "$B"
for _ in $(seq 1 30); do
  if [[ -f "$A/$PREFIX/continuous.md" ]] && grep -q "continuous:$PANTHEON_Q2A_RUN_ID" "$A/$PREFIX/continuous.md"; then
    break
  fi
  sleep 2
done
grep -q "continuous:$PANTHEON_Q2A_RUN_ID" "$A/$PREFIX/continuous.md"

kill "$CONTINUOUS_PID"
wait "$CONTINUOUS_PID" 2>/dev/null || true
unset CONTINUOUS_PID
printf 'restart:%s\n' "$PANTHEON_Q2A_RUN_ID" > "$B/$PREFIX/restart.md"
ob sync --continuous --path "$A" >> "$ARTIFACTS/continuous-a.log" 2>&1 &
CONTINUOUS_PID=$!
sleep 3
kill -0 "$CONTINUOUS_PID"
ob sync --path "$B"
for _ in $(seq 1 30); do
  if [[ -f "$A/$PREFIX/restart.md" ]] && grep -q "restart:$PANTHEON_Q2A_RUN_ID" "$A/$PREFIX/restart.md"; then
    break
  fi
  sleep 2
done
grep -q "restart:$PANTHEON_Q2A_RUN_ID" "$A/$PREFIX/restart.md"

ob sync-status --path "$A" > "$ARTIFACTS/status-a.txt"
ob sync-status --path "$B" > "$ARTIFACTS/status-b.txt"

python - "$ARTIFACTS/observed-result.json" <<'PY'
import json, os, sys
out = {
    "qualification_issue": 958,
    "parent_owner_issue": 660,
    "package": "obsidian-headless",
    "version": "0.0.14",
    "live_obsidian_sync_executed": True,
    "scope": "dedicated synthetic Obsidian Sync account/vault",
    "observed": {
        "create_edit_rename_delete": "pass",
        "local_changes_while_sync_loop_stopped_reconverge": "pass",
        "concurrent_conflict_preserves_both_markers": "pass",
        "continuous_materialization": "pass",
        "daemon_restart": "pass",
        "one_long_running_materializer_in_harness": "pass"
    },
    "not_observed_here": {
        "native_desktop_offline_reconnect": "requires Q2b/native client",
        "ubuntu_host_reboot_redeploy": "requires Q2b/#864 node",
        "network_interruption_recovery": "requires Q2b/#864 node",
        "production_secrets_posture": "requires deployment review",
        "backup_rollback": "requires Q2b/#864 node"
    },
    "authority": {
        "production_switch": False,
        "issue_660_changed": False,
        "issue_659_changed": False,
        "hindsight_activated": False,
        "workspace_index_provider_selected": False
    }
}
with open(sys.argv[1], "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, sort_keys=True)
PY

# Remove only this run-scoped synthetic material, then observe propagation.
rm -rf "$A/$PREFIX"
ob sync --path "$A"
ob sync --path "$B"
test ! -e "$B/$PREFIX"
