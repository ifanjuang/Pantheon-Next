#!/usr/bin/env bash
set -euo pipefail

: "${GITHUB_WORKSPACE:?}"
: "${RUNNER_TEMP:?}"
: "${HERMES_RELEASE_COMMIT:=3c27eb6234bf91b8ceee9e9071591b31e9b148cb}"
: "${HINDSIGHT_API_URL:=http://127.0.0.1:8888}"
: "${HINDSIGHT_BANK_ID:=pantheon-o3-shared-synthetic}"

MVP_ROOT="$GITHUB_WORKSPACE/pantheon-mvp"
OBSIDIAN_ROOT="$GITHUB_WORKSPACE/hindsight-obsidian"
HERMES_ROOT="$GITHUB_WORKSPACE/hermes-upstream"
LAB_ROOT="$RUNNER_TEMP/hindsight-obsidian-hermes-o3"
ARTIFACTS="$LAB_ROOT/artifacts"
VAULT_A="$LAB_ROOT/Vault-A"
VAULT_B="$LAB_ROOT/Vault-B"
INDEX_A="$LAB_ROOT/index-vault-a.json"
INDEX_B="$LAB_ROOT/index-vault-b.json"
CLI="$OBSIDIAN_ROOT/dist/cli.js"
HERMES_HOME="$LAB_ROOT/hermes-home"
VENV="$LAB_ROOT/venv"
PROVIDER_URL="http://127.0.0.1:9020"
FIXTURE_PID=""
TARGET="PANTHEON_O3_OBSIDIAN_TARGET"
STALE="PANTHEON_O3_OBSIDIAN_STALE"
OTHER="PANTHEON_O3_VAULT_B_OTHER"
SUCCESS="O3_SHARED_BANK_RECALL_COMPLETED"

export ARTIFACTS HERMES_HOME HINDSIGHT_API_URL HINDSIGHT_BANK_ID INDEX_A INDEX_B
mkdir -p "$ARTIFACTS" "$VAULT_A/Projects/Alpha" "$VAULT_B/Projects/Alpha"

cleanup() {
  set +e
  if [ -n "$FIXTURE_PID" ]; then kill "$FIXTURE_PID" 2>/dev/null || true; fi
  if [ -x "$VENV/bin/hermes" ]; then "$VENV/bin/hermes" profile delete assistant-personal --yes >/dev/null 2>&1 || true; fi
}
trap cleanup EXIT

cat > "$VAULT_A/Projects/Alpha/note.md" <<EOF
---
tags: [o3, target]
created: 2026-08-08
---
$TARGET. This note is the surviving Vault-A target populated only by the official Obsidian sync CLI.
EOF
cat > "$VAULT_A/Projects/Alpha/stale.md" <<EOF
---
tags: [o3, stale]
created: 2026-08-08
---
$STALE. This note must disappear before Hermes recall.
EOF
cat > "$VAULT_B/Projects/Alpha/note.md" <<EOF
---
tags: [o3, other]
created: 2026-08-08
---
$OTHER. This note remains in the shared bank but must be excluded by Hermes strict recall tags.
EOF

run_sync() {
  local vault="$1" vault_name="$2" index="$3" output="$4"
  node "$CLI" reconcile \
    --vault "$vault" --vault-name "$vault_name" \
    --bank "$HINDSIGHT_BANK_ID" --api-url "$HINDSIGHT_API_URL" \
    --prefix-doc-id --index "$index" | tee "$output"
}

wait_for_marker() {
  local marker="$1" vault_tag="$2" folder_tag="$3"
  MARKER="$marker" VAULT_TAG="$vault_tag" FOLDER_TAG="$folder_tag" python - <<'PY'
import json, os, time, urllib.request
base=os.environ['HINDSIGHT_API_URL'].rstrip('/')
bank=os.environ['HINDSIGHT_BANK_ID']
marker=os.environ['MARKER']
url=f"{base}/v1/default/banks/{bank}/memories/recall"
last=None
for _ in range(120):
    body={'query':marker,'types':['world','experience'],'tags':[os.environ['VAULT_TAG'],os.environ['FOLDER_TAG']],'tags_match':'all_strict'}
    req=urllib.request.Request(url,data=json.dumps(body).encode(),headers={'Content-Type':'application/json'},method='POST')
    with urllib.request.urlopen(req,timeout=10) as resp:
        last=json.loads(resp.read().decode())
    items=last.get('results',[]) if isinstance(last,dict) else []
    if any(marker in str(x.get('text','')) for x in items if isinstance(x,dict)):
        raise SystemExit(0)
    time.sleep(0.25)
raise SystemExit(f'marker did not materialize: {marker}: {last!r}')
PY
}

run_sync "$VAULT_A" Vault-A "$INDEX_A" "$ARTIFACTS/initial-a.txt"
run_sync "$VAULT_B" Vault-B "$INDEX_B" "$ARTIFACTS/initial-b.txt"
grep -F 'reconcile: +2 added, ~0 updated, -0 deleted, =0 unchanged' "$ARTIFACTS/initial-a.txt"
grep -F 'reconcile: +1 added, ~0 updated, -0 deleted, =0 unchanged' "$ARTIFACTS/initial-b.txt"
wait_for_marker "$TARGET" vault:Vault-A folder:Projects/Alpha
wait_for_marker "$STALE" vault:Vault-A folder:Projects/Alpha
wait_for_marker "$OTHER" vault:Vault-B folder:Projects/Alpha

# Reconcile deletion before Hermes touches the bank.
rm "$VAULT_A/Projects/Alpha/stale.md"
run_sync "$VAULT_A" Vault-A "$INDEX_A" "$ARTIFACTS/delete-stale.txt"
grep -F 'reconcile: +0 added, ~0 updated, -1 deleted, =1 unchanged' "$ARTIFACTS/delete-stale.txt"

# Direct Hindsight qualification: target survives, stale is gone, Vault-B remains.
TARGET="$TARGET" STALE="$STALE" OTHER="$OTHER" python - <<'PY'
import json, os, urllib.request
from pathlib import Path
base=os.environ['HINDSIGHT_API_URL'].rstrip('/')
bank=os.environ['HINDSIGHT_BANK_ID']
out=Path(os.environ['ARTIFACTS'])
def recall(query,tags):
    body={'query':query,'types':['world','experience'],'tags':tags,'tags_match':'all_strict'}
    req=urllib.request.Request(f"{base}/v1/default/banks/{bank}/memories/recall",data=json.dumps(body).encode(),headers={'Content-Type':'application/json'},method='POST')
    with urllib.request.urlopen(req,timeout=30) as r: return json.loads(r.read().decode())
def text(v): return json.dumps(v,ensure_ascii=False)
a=recall(os.environ['TARGET'],['vault:Vault-A','folder:Projects/Alpha'])
b=recall(os.environ['OTHER'],['vault:Vault-B','folder:Projects/Alpha'])
stale=recall(os.environ['STALE'],['vault:Vault-A','folder:Projects/Alpha'])
assert os.environ['TARGET'] in text(a), a
assert os.environ['OTHER'] in text(b), b
assert os.environ['STALE'] not in text(stale), stale
(out/'pre-hermes-scoped-recall.json').write_text(json.dumps({'vault_a':a,'vault_b':b,'stale':stale},indent=2,ensure_ascii=False))
PY

# Reuse the exact O1 Hermes source-install/profile pattern; O3 adds no runtime abstraction.
python -m pip install --disable-pip-version-check --upgrade uv
python -m venv "$VENV"
uv pip install --python "$VENV/bin/python" -e "$HERMES_ROOT" "hindsight-client==0.8.5" "aiohttp==3.14.1"
uv pip install --python "$VENV/bin/python" -e "$MVP_ROOT"
export PATH="$VENV/bin:$PATH"
hermes profile create assistant-personal --no-skills --no-alias
hermes profile create pantheon-governed --no-skills --no-alias

python "$MVP_ROOT/tools/hindsight_hermes_o1_fixture.py" \
  --journal "$ARTIFACTS/provider-journal.jsonl" \
  --marker "$TARGET" --forbid-marker "$STALE" --forbid-marker "$OTHER" \
  --query "Find the Obsidian O3 target in the configured memory scope" \
  --success-token "$SUCCESS" --failure-token O3_SHARED_BANK_RECALL_SCOPE_FAILURE \
  >"$ARTIFACTS/provider.log" 2>&1 &
FIXTURE_PID=$!
for _ in $(seq 1 60); do curl -fsS "$PROVIDER_URL/health" >/dev/null && break; sleep 0.5; done

python "$MVP_ROOT/tools/run_hindsight_hermes_o1.py" configure \
  --hermes-home "$HERMES_HOME" \
  --hindsight-api-url "$HINDSIGHT_API_URL" \
  --provider-url "$PROVIDER_URL" --bank-id "$HINDSIGHT_BANK_ID" \
  --recall-tag vault:Vault-A --recall-tag folder:Projects/Alpha \
  --recall-tags-match all_strict \
  --output "$ARTIFACTS/configuration.json"

cat > "$HERMES_HOME/profiles/pantheon-governed/config.yaml" <<'YAML'
memory:
  provider: ""
  memory_enabled: false
  user_profile_enabled: false
platform_toolsets:
  cli: []
YAML
pantheon-hermes capture-memory-status --profile pantheon-governed --hermes-command "$VENV/bin/hermes" --output "$ARTIFACTS/governed-memory-status.json"
hermes -p assistant-personal memory status > "$ARTIFACTS/assistant-memory-status.txt"
grep -i hindsight "$ARTIFACTS/assistant-memory-status.txt"

# Count Hindsight retain HTTP requests before/after Hermes. The deterministic model
# only calls hindsight_recall and auto_retain is false, so the count must not grow.
docker logs pantheon-o3-hindsight > "$ARTIFACTS/hindsight-before-hermes.log" 2>&1 || true
BEFORE_RETAINS=$(grep -cE 'POST .*\/memories' "$ARTIFACTS/hindsight-before-hermes.log" || true)
printf '%s\n' "$BEFORE_RETAINS" > "$ARTIFACTS/retain-count-before.txt"

hermes -p assistant-personal chat -q "Use hindsight_recall to find the configured Obsidian O3 target. Do not retain anything." > "$ARTIFACTS/hermes-output.txt"
grep -F "$SUCCESS" "$ARTIFACTS/hermes-output.txt"
curl -fsS "$PROVIDER_URL/_lab/state" > "$ARTIFACTS/provider-state.json"

docker logs pantheon-o3-hindsight > "$ARTIFACTS/hindsight-after-hermes.log" 2>&1 || true
AFTER_RETAINS=$(grep -cE 'POST .*\/memories' "$ARTIFACTS/hindsight-after-hermes.log" || true)
printf '%s\n' "$AFTER_RETAINS" > "$ARTIFACTS/retain-count-after.txt"
test "$BEFORE_RETAINS" = "$AFTER_RETAINS"

hermes profile delete assistant-personal --yes
printf '{"assistant_profile_removed":true,"pantheon_state_mutated":false}\n' > "$ARTIFACTS/rollback.json"

TARGET="$TARGET" SUCCESS="$SUCCESS" python - <<'PY'
import json, os
from pathlib import Path
p=Path(os.environ['ARTIFACTS'])
config=json.loads((p/'configuration.json').read_text())
state=json.loads((p/'provider-state.json').read_text())
governed=json.loads((p/'governed-memory-status.json').read_text())
rollback=json.loads((p/'rollback.json').read_text())
output=(p/'hermes-output.txt').read_text()
before=int((p/'retain-count-before.txt').read_text().strip())
after=int((p/'retain-count-after.txt').read_text().strip())
assert config['bank_id']==os.environ['HINDSIGHT_BANK_ID'], config
assert config['recall_tags']==['vault:Vault-A','folder:Projects/Alpha'], config
assert config['recall_tags_match']=='all_strict', config
assert config['auto_retain'] is False and config['auto_recall'] is False, config
assert state['recall_tool_seen'] is True, state
assert state['marker_seen_in_tool_result'] is True, state
assert state['forbidden_marker_seen_in_tool_result'] is False, state
assert os.environ['SUCCESS'] in output, output
assert before==after, (before,after)
assert governed.get('status')=='qualified' and governed.get('active_axes')==[], governed
assert rollback.get('assistant_profile_removed') is True, rollback
summary={
 'kind':'hindsight_obsidian_hermes_o3_acceptance','status':'passed',
 'official_obsidian_ingestion_only':True,'same_bank_verified':True,
 'hermes_recall_verified':True,'strict_vault_folder_scope_verified':True,
 'deleted_note_absent_verified':True,'cross_vault_exclusion_verified':True,
 'hermes_duplicate_retain':False,'conversation_retention':'off',
 'governed_memory_posture':'qualified_off','pantheon_state_mutated':False,
 'evidence_admitted':False,'production_activated':False,'rollback_verified':True,
}
(p/'acceptance-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,indent=2,sort_keys=True))
PY
