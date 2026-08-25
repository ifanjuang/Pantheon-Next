#!/usr/bin/env bash
set -euo pipefail

: "${GITHUB_WORKSPACE:?}"
: "${RUNNER_TEMP:?}"
: "${LIVESYNC_ROOT:?}"
: "${HERMES_ROOT:?}"

LAB_ROOT="$RUNNER_TEMP/hermes-livesync-reverse-q3"
ARTIFACTS="$LAB_ROOT/artifacts"
CLIENT_DB="$LAB_ROOT/client-db"
NAS_DB="$LAB_ROOT/nas-db"
NAS_VAULT="$LAB_ROOT/nas-vault"
CLIENT_SETTINGS="$LAB_ROOT/client-settings.json"
NAS_SETTINGS="$LAB_ROOT/nas-settings.json"
CLI="$LIVESYNC_ROOT/src/apps/cli/dist/index.cjs"
COUCHDB_CONTAINER="pantheon-hermes-livesync-q3-couchdb"
COUCHDB_URI="http://127.0.0.1:5990"
COUCHDB_USER="pantheon"
COUCHDB_PASSWORD="synthetic-only"
COUCHDB_DBNAME="pantheon-hermes-livesync-q3"
NAS_DAEMON_PID=""
NOTE_PATH="Affaires/Alpha/note.md"

mkdir -p "$ARTIFACTS" "$CLIENT_DB" "$NAS_DB" "$NAS_VAULT"

stop_nas_daemon() {
  if [[ -n "$NAS_DAEMON_PID" ]]; then
    kill "$NAS_DAEMON_PID" >/dev/null 2>&1 || true
    wait "$NAS_DAEMON_PID" >/dev/null 2>&1 || true
    NAS_DAEMON_PID=""
  fi
}

cleanup() {
  stop_nas_daemon
  docker stop "$COUCHDB_CONTAINER" >/dev/null 2>&1 || true
}
trap cleanup EXIT

run_cli() {
  node "$CLI" "$@"
}

configure_settings() {
  local settings_file="$1"
  run_cli init-settings --force "$settings_file" >/dev/null
  SETTINGS_FILE="$settings_file" \
  COUCHDB_URI="$COUCHDB_URI" \
  COUCHDB_USER="$COUCHDB_USER" \
  COUCHDB_PASSWORD="$COUCHDB_PASSWORD" \
  COUCHDB_DBNAME="$COUCHDB_DBNAME" \
  node <<'NODE'
const fs = require('node:fs');
const path = process.env.SETTINGS_FILE;
const data = JSON.parse(fs.readFileSync(path, 'utf8'));
data.couchDB_URI = process.env.COUCHDB_URI;
data.couchDB_USER = process.env.COUCHDB_USER;
data.couchDB_PASSWORD = process.env.COUCHDB_PASSWORD;
data.couchDB_DBNAME = process.env.COUCHDB_DBNAME;
data.liveSync = true;
data.syncOnStart = false;
data.syncOnSave = false;
data.usePluginSync = false;
data.encrypt = false;
data.passphrase = '';
data.isConfigured = true;
fs.writeFileSync(path, JSON.stringify(data, null, 2) + '\n');
NODE
}

sync_client() {
  run_cli "$CLIENT_DB" --settings "$CLIENT_SETTINGS" sync >/dev/null
}

wait_for_client_marker() {
  local marker="$1"
  local content=""
  for _ in $(seq 1 120); do
    sync_client || true
    if content="$(run_cli "$CLIENT_DB" --settings "$CLIENT_SETTINGS" cat "$NOTE_PATH" 2>/dev/null)" \
      && grep -Fq "$marker" <<<"$content"; then
      printf '%s\n' "$content" > "$ARTIFACTS/client-${marker}.md"
      return 0
    fi
    if [[ -n "$NAS_DAEMON_PID" ]] && ! kill -0 "$NAS_DAEMON_PID" 2>/dev/null; then
      echo "NAS daemon exited while waiting for client marker $marker" >&2
      cat "$ARTIFACTS/nas-daemon.log" >&2 || true
      return 1
    fi
    sleep 0.25
  done
  echo "Timed out waiting for client marker $marker" >&2
  cat "$ARTIFACTS/nas-daemon.log" >&2 || true
  return 1
}

hermes_note_action() {
  local action="$1"
  ACTION="$action" \
  HERMES_ROOT="$HERMES_ROOT" \
  OBSIDIAN_VAULT_PATH="$NAS_VAULT" \
  TERMINAL_CWD="$NAS_VAULT" \
  python - <<'PY'
import os
import sys
from pathlib import Path

hermes_root = Path(os.environ["HERMES_ROOT"]).resolve()
vault = Path(os.environ["OBSIDIAN_VAULT_PATH"]).resolve()
action = os.environ["ACTION"]
if not vault.is_absolute() or not vault.is_dir():
    raise SystemExit("configured synthetic vault must be an existing absolute path")

sys.path.insert(0, str(hermes_root))
from tools.file_tools import patch_tool, read_file_tool, write_file_tool

note = vault / "Affaires" / "Alpha" / "note.md"
if action == "create":
    content = "# Alpha\n\nPANTHEON_HERMES_LIVESYNC_CREATE\n\nStatus: draft\n"
    result = write_file_tool(str(note), content)
    if note.read_text(encoding="utf-8") != content:
        raise AssertionError(result)
elif action == "patch":
    before = read_file_tool(str(note))
    if "Status: draft" not in before:
        raise AssertionError(before)
    result = patch_tool(
        mode="replace",
        path=str(note),
        old_string="Status: draft",
        new_string="Status: PANTHEON_HERMES_LIVESYNC_PATCH",
    )
    after = note.read_text(encoding="utf-8")
    if "Status: PANTHEON_HERMES_LIVESYNC_PATCH" not in after:
        raise AssertionError(result)
else:
    raise SystemExit(f"unsupported action: {action}")
PY
}

docker run -d --rm \
  --name "$COUCHDB_CONTAINER" \
  -p 5990:5984 \
  -e COUCHDB_USER="$COUCHDB_USER" \
  -e COUCHDB_PASSWORD="$COUCHDB_PASSWORD" \
  -e COUCHDB_SINGLE_NODE=true \
  couchdb:3.5.0 >/dev/null

for _ in $(seq 1 90); do
  if curl -fsS -u "$COUCHDB_USER:$COUCHDB_PASSWORD" "$COUCHDB_URI/" >/dev/null; then
    break
  fi
  sleep 1
done
curl -fsS -u "$COUCHDB_USER:$COUCHDB_PASSWORD" "$COUCHDB_URI/" >/dev/null
curl -fsS -X PUT -u "$COUCHDB_USER:$COUCHDB_PASSWORD" "$COUCHDB_URI/$COUCHDB_DBNAME" > "$ARTIFACTS/couchdb-create.json"

configure_settings "$CLIENT_SETTINGS"
configure_settings "$NAS_SETTINGS"

run_cli "$NAS_DB" --settings "$NAS_SETTINGS" --vault "$NAS_VAULT" --interval 1 daemon \
  > "$ARTIFACTS/nas-daemon.log" 2>&1 &
NAS_DAEMON_PID=$!
sleep 1
kill -0 "$NAS_DAEMON_PID"

hermes_note_action create
test -f "$NAS_VAULT/$NOTE_PATH"
grep -Fq PANTHEON_HERMES_LIVESYNC_CREATE "$NAS_VAULT/$NOTE_PATH"
wait_for_client_marker PANTHEON_HERMES_LIVESYNC_CREATE

hermes_note_action patch
grep -Fq PANTHEON_HERMES_LIVESYNC_PATCH "$NAS_VAULT/$NOTE_PATH"
wait_for_client_marker PANTHEON_HERMES_LIVESYNC_PATCH

run_cli "$CLIENT_DB" --settings "$CLIENT_SETTINGS" cat "$NOTE_PATH" > "$ARTIFACTS/client-final-note.md"
cp "$NAS_VAULT/$NOTE_PATH" "$ARTIFACTS/nas-final-note.md"
cmp "$ARTIFACTS/client-final-note.md" "$ARTIFACTS/nas-final-note.md"

docker image inspect couchdb:3.5.0 --format '{{json .RepoDigests}}' > "$ARTIFACTS/couchdb-image-repodigests.json" || true

ARTIFACTS="$ARTIFACTS" LIVESYNC_ROOT="$LIVESYNC_ROOT" HERMES_ROOT="$HERMES_ROOT" python - <<'PY'
import json
import os
import subprocess
from pathlib import Path

artifacts = Path(os.environ["ARTIFACTS"])
livesync_root = Path(os.environ["LIVESYNC_ROOT"])
hermes_root = Path(os.environ["HERMES_ROOT"])
summary = {
    "kind": "hermes_livesync_reverse_q3_acceptance",
    "status": "passed",
    "hermes_commit": subprocess.check_output(["git", "-C", str(hermes_root), "rev-parse", "HEAD"], text=True).strip(),
    "livesync_commit": subprocess.check_output(["git", "-C", str(livesync_root), "rev-parse", "HEAD"], text=True).strip(),
    "livesync_cli_version": json.loads((livesync_root / "src/apps/cli/package.json").read_text())["version"],
    "couchdb_version": "3.5.0",
    "hermes_create_to_separate_client_verified": True,
    "hermes_patch_to_separate_client_verified": True,
    "nas_and_client_content_equal": True,
    "nas_mode": "daemon",
    "second_client_kind": "self-hosted-livesync-cli-local-db",
    "native_obsidian_client_verified": False,
    "hermes_direct_couchdb_write": False,
    "hindsight_ingestion_activated": False,
    "pantheon_state_mutated": False,
    "evidence_admitted": False,
    "delete_qualified": False,
    "move_rename_qualified": False,
}
(artifacts / "acceptance-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
PY

cat "$ARTIFACTS/acceptance-summary.json"
