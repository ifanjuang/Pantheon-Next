#!/usr/bin/env bash
set -euo pipefail

: "${GITHUB_WORKSPACE:?}"
: "${RUNNER_TEMP:?}"
: "${LIVESYNC_ROOT:=$GITHUB_WORKSPACE/obsidian-livesync}"

LAB_ROOT="$RUNNER_TEMP/livesync-headless-mirror-s1"
ARTIFACTS="$LAB_ROOT/artifacts"
DB_A="$LAB_ROOT/client-db"
DB_B="$LAB_ROOT/nas-db"
VAULT_B="$LAB_ROOT/nas-vault"
SETTINGS_A="$LAB_ROOT/client-settings.json"
SETTINGS_B="$LAB_ROOT/nas-settings.json"
CLI="$LIVESYNC_ROOT/src/apps/cli/dist/index.cjs"
COUCHDB_CONTAINER="pantheon-livesync-s1-couchdb"
COUCHDB_URI="http://127.0.0.1:5989"
COUCHDB_USER="pantheon"
COUCHDB_PASSWORD="synthetic-only"
COUCHDB_DBNAME="pantheon-livesync-s1"
NAS_DAEMON_PID=""

mkdir -p "$ARTIFACTS" "$DB_A" "$DB_B" "$VAULT_B"

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

sync_a() {
  run_cli "$DB_A" --settings "$SETTINGS_A" sync >/dev/null
}

wait_for_content() {
  local path="$1" marker="$2"
  for _ in $(seq 1 120); do
    if [[ -f "$path" ]] && grep -Fq "$marker" "$path"; then
      return 0
    fi
    if [[ -n "$NAS_DAEMON_PID" ]] && ! kill -0 "$NAS_DAEMON_PID" 2>/dev/null; then
      echo "NAS daemon exited while waiting for $path" >&2
      cat "$ARTIFACTS/nas-daemon.log" >&2 || true
      return 1
    fi
    sleep 0.25
  done
  echo "Timed out waiting for marker $marker in $path" >&2
  cat "$ARTIFACTS/nas-daemon.log" >&2 || true
  return 1
}

wait_for_absence() {
  local path="$1"
  for _ in $(seq 1 120); do
    if [[ ! -e "$path" ]]; then
      return 0
    fi
    if [[ -n "$NAS_DAEMON_PID" ]] && ! kill -0 "$NAS_DAEMON_PID" 2>/dev/null; then
      echo "NAS daemon exited while waiting for deletion of $path" >&2
      cat "$ARTIFACTS/nas-daemon.log" >&2 || true
      return 1
    fi
    sleep 0.25
  done
  echo "Timed out waiting for deletion of $path" >&2
  cat "$ARTIFACTS/nas-daemon.log" >&2 || true
  return 1
}

docker run -d --rm \
  --name "$COUCHDB_CONTAINER" \
  -p 5989:5984 \
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

configure_settings "$SETTINGS_A"
configure_settings "$SETTINGS_B"

# The intended NAS deployment is the long-running daemon, not a sequence of
# unrelated one-shot sync+mirror invocations. It owns only its private local DB
# and the dedicated synthetic NAS vault path.
run_cli "$DB_B" --settings "$SETTINGS_B" --vault "$VAULT_B" --interval 1 daemon \
  > "$ARTIFACTS/nas-daemon.log" 2>&1 &
NAS_DAEMON_PID=$!
sleep 1
kill -0 "$NAS_DAEMON_PID"

# Create: synthetic client DB -> CouchDB -> headless daemon -> filesystem vault.
printf 'PANTHEON_LIVESYNC_CREATE\n' | run_cli "$DB_A" --settings "$SETTINGS_A" put Projects/Alpha/note.md >/dev/null
sync_a
wait_for_content "$VAULT_B/Projects/Alpha/note.md" PANTHEON_LIVESYNC_CREATE
cp "$VAULT_B/Projects/Alpha/note.md" "$ARTIFACTS/create-note.md"

# Edit must reconverge into the same materialised file.
printf 'PANTHEON_LIVESYNC_EDIT\n' | run_cli "$DB_A" --settings "$SETTINGS_A" put Projects/Alpha/note.md >/dev/null
sync_a
wait_for_content "$VAULT_B/Projects/Alpha/note.md" PANTHEON_LIVESYNC_EDIT
cp "$VAULT_B/Projects/Alpha/note.md" "$ARTIFACTS/edit-note.md"

# Rename is delete(old)+create(new). A correct daemon mirror must not leave the
# old Markdown path behind because downstream Hindsight would otherwise ingest
# a stale duplicate.
run_cli "$DB_A" --settings "$SETTINGS_A" rm Projects/Alpha/note.md >/dev/null
printf 'PANTHEON_LIVESYNC_RENAMED\n' | run_cli "$DB_A" --settings "$SETTINGS_A" put Projects/Alpha/renamed.md >/dev/null
sync_a
wait_for_absence "$VAULT_B/Projects/Alpha/note.md"
wait_for_content "$VAULT_B/Projects/Alpha/renamed.md" PANTHEON_LIVESYNC_RENAMED
cp "$VAULT_B/Projects/Alpha/renamed.md" "$ARTIFACTS/renamed-note.md"

# Delete must remove the real filesystem representation and remain removed.
run_cli "$DB_A" --settings "$SETTINGS_A" rm Projects/Alpha/renamed.md >/dev/null
sync_a
wait_for_absence "$VAULT_B/Projects/Alpha/renamed.md"
sleep 1
test ! -e "$VAULT_B/Projects/Alpha/renamed.md"

# Do not open the daemon's internal LevelDB from a second process merely for
# observation. The qualified boundary is the materialised filesystem vault.
docker image inspect couchdb:3.5.0 --format '{{json .RepoDigests}}' > "$ARTIFACTS/couchdb-image-repodigests.json" || true

ARTIFACTS="$ARTIFACTS" LIVESYNC_ROOT="$LIVESYNC_ROOT" python - <<'PY'
import json
import os
import subprocess
from pathlib import Path

artifacts = Path(os.environ['ARTIFACTS'])
root = Path(os.environ['LIVESYNC_ROOT'])
commit = subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'], text=True).strip()
package = json.loads((root / 'src/apps/cli/package.json').read_text())
summary = {
    'kind': 'livesync_headless_mirror_s1_acceptance',
    'status': 'passed',
    'livesync_commit': commit,
    'livesync_cli_version': package['version'],
    'couchdb_version': '3.5.0',
    'nas_mode': 'daemon',
    'create_verified': True,
    'edit_verified': True,
    'rename_verified': True,
    'delete_verified': True,
    'separate_database_and_vault_paths_verified': True,
    'headless_materialization_verified': True,
    'obsidian_gui_required': False,
    'hindsight_ingestion_activated': False,
    'pantheon_state_mutated': False,
    'evidence_admitted': False,
}
(artifacts / 'acceptance-summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
PY

cat "$ARTIFACTS/acceptance-summary.json"
