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

mkdir -p "$ARTIFACTS" "$DB_A" "$DB_B" "$VAULT_B"

cleanup() {
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

sync_b() {
  run_cli "$DB_B" --settings "$SETTINGS_B" sync >/dev/null
}

mirror_b() {
  run_cli "$DB_B" --settings "$SETTINGS_B" mirror "$VAULT_B" > "$ARTIFACTS/mirror-last.log"
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

# Create: a synthetic client writes into its local LiveSync DB, replicates to
# CouchDB, and the headless NAS-side DB materialises a real vault directory.
printf 'PANTHEON_LIVESYNC_CREATE\n' | run_cli "$DB_A" --settings "$SETTINGS_A" put Projects/Alpha/note.md >/dev/null
sync_a
sync_b
mirror_b
test -f "$VAULT_B/Projects/Alpha/note.md"
grep -Fq 'PANTHEON_LIVESYNC_CREATE' "$VAULT_B/Projects/Alpha/note.md"
cp "$VAULT_B/Projects/Alpha/note.md" "$ARTIFACTS/create-note.md"

# Edit: the same remote document must reconverge into the materialised vault.
printf 'PANTHEON_LIVESYNC_EDIT\n' | run_cli "$DB_A" --settings "$SETTINGS_A" put Projects/Alpha/note.md >/dev/null
sync_a
sync_b
mirror_b
grep -Fq 'PANTHEON_LIVESYNC_EDIT' "$VAULT_B/Projects/Alpha/note.md"
cp "$VAULT_B/Projects/Alpha/note.md" "$ARTIFACTS/edit-note.md"

# Rename is represented as delete(old)+create(new), matching the file semantics
# the downstream Hindsight reconciliation lab already qualifies.
run_cli "$DB_A" --settings "$SETTINGS_A" rm Projects/Alpha/note.md >/dev/null
printf 'PANTHEON_LIVESYNC_RENAMED\n' | run_cli "$DB_A" --settings "$SETTINGS_A" put Projects/Alpha/renamed.md >/dev/null
sync_a
sync_b
mirror_b
test ! -e "$VAULT_B/Projects/Alpha/note.md"
test -f "$VAULT_B/Projects/Alpha/renamed.md"
grep -Fq 'PANTHEON_LIVESYNC_RENAMED' "$VAULT_B/Projects/Alpha/renamed.md"
cp "$VAULT_B/Projects/Alpha/renamed.md" "$ARTIFACTS/renamed-note.md"

# Delete: a tombstone propagated through CouchDB must remove the NAS file and
# must not be silently resurrected by the mirror step.
run_cli "$DB_A" --settings "$SETTINGS_A" rm Projects/Alpha/renamed.md >/dev/null
sync_a
sync_b
mirror_b
test ! -e "$VAULT_B/Projects/Alpha/renamed.md"

run_cli "$DB_B" --settings "$SETTINGS_B" ls > "$ARTIFACTS/nas-db-ls.txt"
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
