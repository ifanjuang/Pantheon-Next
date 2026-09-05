# PAIR + Unsloth Runtime Q1 Runbook

Status: candidate execution runbook. This file defines how to run Q1. It is not a record that Q1 ran or passed.

Companion contract: `docs/governance/PAIR_UNSLOTH_RUNTIME_QUALIFICATION.md`.
Machine-readable planning state: `tests/fixtures/pair_unsloth_runtime_q1.json`.

## 1. Scope and authority ceiling

This runbook is for an isolated qualification lab using:

- the always-on Linux RTX 4080 node as the headless PAIR / Unsloth host;
- the always-on Windows RTX 4090 node as the second PAIR node and Desktop observation console;
- the current Pantheon Hermes container only where a stage explicitly requires the current container network namespace.

It does not select a deployment topology. It does not authorize a task, admit Evidence, activate a runtime, or change the Pantheon Ubuntu deployment candidate.

Never change these repository-owned deployment inputs while executing Q1:

```text
deployment/ubuntu/release.env
deployment/ubuntu/install-node
implementation/hermes/distribution/pantheon-standard.lock.yaml
```

The following remain distinct throughout the lab:

```text
artifact downloaded != artifact qualified
runtime reachable != runtime accepted
model available != model approved
PAIR routed request != Pantheon authorization
Unsloth provider configured != provider authorized
successful execution != Evidence
```

## 2. Safety and evidence-handling rules

Do not write these values into committed files or lab artifacts:

- PAIR pairing PINs;
- Unsloth API keys;
- Hermes/provider secrets;
- prompt bodies or generated response bodies;
- private hostnames, user data or document content not required by the lab.

It is acceptable to record a one-way SHA-256 fingerprint of a temporary API key if correlation is needed.

Do not use `--yolo` for the Hermes tool-call test. If Hermes asks for approval for the bounded harmless tool call, approve that exact call only. Successful approval is not standing authorization.

PAIR must run only on the trusted local network used for this lab. If a restrictive firewall is active, open only the documented PAIR cluster ports from the peer node and remove the temporary rules during rollback.

Never run PAIR Desktop and `nvpair-tui` simultaneously on the same host. The Linux node uses the TUI; the Windows node uses Desktop.

## 3. Fixed Q1 lab inputs

These values are workload inputs, not production selections:

```text
PAIR Q1 model:       qwen3.5:4b
Unsloth Q1 model:    unsloth/Qwen3.5-4B-GGUF:UD-Q4_K_XL
Unsloth context:     16384 tokens
Unsloth API port:    18888/tcp
Hermes lab profile:  pantheon-q1-unsloth
```

The PAIR model is intentionally small enough to make node routing, failover and model retention the subject of the test rather than VRAM pressure. The Unsloth model is the corresponding small GGUF and is used only to test the provider seam. A later model-qualification decision is separate.

## 4. Common preparation on the Linux node

Run from a checkout of this PR branch.

### 4.1 Resolve qualification pins from the canonical registry

Do not type current PAIR, Unsloth or Hermes versions or commit SHAs into the runbook or shell by hand.

```bash
cd /path/to/Pantheon-Next

eval "$(python implementation/tools/export_external_qualification_pins.py \
  personal-ai-router unsloth hermes-agent)"

printf '%s\n' \
  "PAIR_PIN_ID=$PAIR_PIN_ID" \
  "PAIR_VERSION=$PAIR_VERSION" \
  "PAIR_REF=$PAIR_REF" \
  "UNSLOTH_PIN_ID=$UNSLOTH_PIN_ID" \
  "UNSLOTH_VERSION=$UNSLOTH_VERSION" \
  "UNSLOTH_REF=$UNSLOTH_REF" \
  "HERMES_PIN_ID=$HERMES_PIN_ID" \
  "HERMES_VERSION=$HERMES_VERSION" \
  "HERMES_REF=$HERMES_REF"
```

Stop if any required variable is empty.

### 4.2 Create an isolated lab root

```bash
export Q1_ROOT="$HOME/pantheon-labs/pair-unsloth-q1"
export Q1_ARTIFACTS="$Q1_ROOT/artifacts"
export Q1_PAIR_HOME="$Q1_ROOT/pair-home"
export Q1_PAIR_BIN="$Q1_ROOT/pair-bin"
export Q1_UNSLOTH_SRC="$Q1_ROOT/unsloth-src"
export Q1_UNSLOTH_VENV="$Q1_ROOT/unsloth-venv"
export PAIR_Q1_MODEL="qwen3.5:4b"
export UNSLOTH_Q1_MODEL="unsloth/Qwen3.5-4B-GGUF:UD-Q4_K_XL"
export UNSLOTH_Q1_CONTEXT="16384"
export UNSLOTH_Q1_PORT="18888"

mkdir -p "$Q1_ARTIFACTS" "$Q1_PAIR_HOME" "$Q1_PAIR_BIN"
chmod 700 "$Q1_ROOT" "$Q1_ARTIFACTS" "$Q1_PAIR_HOME"
```

### 4.3 Capture the host baseline

```bash
{
  date --iso-8601=seconds
  uname -a
  nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv,noheader
  docker --version 2>/dev/null || true
  python --version
  git rev-parse HEAD
} > "$Q1_ARTIFACTS/linux-baseline.txt"

systemctl is-active ollama > "$Q1_ARTIFACTS/system-ollama-before.state" 2>&1 || true
systemctl show ollama \
  -p FragmentPath -p DropInPaths -p Environment \
  > "$Q1_ARTIFACTS/system-ollama-before.txt" 2>&1 || true

sudo ss -ltnp | grep -E ':(11434|11435|1234|1235)\\b' \
  > "$Q1_ARTIFACTS/inference-listeners-before.txt" 2>&1 || true
```

Record, do not infer, whether the current Pantheon candidate Ollama service is active.

### 4.4 Hash the Pantheon-owned Ollama model-store metadata

Do not hash model contents; the goal is to detect unintended deletion/renaming of the Pantheon store without reading gigabytes of weights.

```bash
if sudo test -d /srv/ai/models/ollama; then
  sudo find /srv/ai/models/ollama -type f -printf '%P\t%s\n' \
    | sort \
    | sha256sum \
    > "$Q1_ARTIFACTS/pantheon-ollama-store-before.sha256"
else
  printf 'absent\n' > "$Q1_ARTIFACTS/pantheon-ollama-store-before.sha256"
fi
```

## 5. Q1A — isolated PAIR on Linux RTX 4080

### 5.1 Preconditions

Q1A must not run while the Pantheon-owned Ollama process occupies PAIR's local proxy port.

If the baseline says the system Ollama service was active, stop it for the lab window without editing its unit, drop-in, model path or environment:

```bash
if systemctl is-active --quiet ollama; then
  export Q1_SYSTEM_OLLAMA_WAS_ACTIVE=1
  sudo systemctl stop ollama
else
  export Q1_SYSTEM_OLLAMA_WAS_ACTIVE=0
fi

if sudo ss -ltnp | grep -q ':11434\\b'; then
  echo 'STOP: port 11434 is still occupied; identify the owner before continuing.' >&2
  sudo ss -ltnp | grep ':11434\\b' >&2 || true
  exit 1
fi
```

Do not kill an unknown process merely to free the port.

### 5.2 Download the PAIR release archive selected by the registry

Use the GitHub release metadata to resolve the x64 Linux service archive and validate its published digest. This keeps the pin registry as version authority while still validating the concrete release asset.

```bash
PAIR_RELEASE_JSON="$Q1_ROOT/pair-release.json"
PAIR_ARCHIVE="$Q1_ROOT/service-binaries-linux-x64.zip"

curl -fsSL \
  "https://api.github.com/repos/${PAIR_REPOSITORY}/releases/tags/v${PAIR_VERSION}" \
  -o "$PAIR_RELEASE_JSON"

PAIR_ASSET_URL="$(jq -r '.assets[] | select(.name == "service-binaries-linux-x64.zip") | .browser_download_url' "$PAIR_RELEASE_JSON")"
PAIR_ASSET_DIGEST="$(jq -r '.assets[] | select(.name == "service-binaries-linux-x64.zip") | .digest // empty' "$PAIR_RELEASE_JSON")"

test -n "$PAIR_ASSET_URL" || { echo 'PAIR Linux x64 asset not found'; exit 1; }

curl -fL "$PAIR_ASSET_URL" -o "$PAIR_ARCHIVE"
PAIR_ASSET_SHA256="$(sha256sum "$PAIR_ARCHIVE" | awk '{print $1}')"
printf '%s\n' "$PAIR_ASSET_SHA256" > "$Q1_ARTIFACTS/pair-linux-asset.sha256"

if [ -n "$PAIR_ASSET_DIGEST" ]; then
  test "sha256:$PAIR_ASSET_SHA256" = "$PAIR_ASSET_DIGEST" \
    || { echo 'PAIR asset digest mismatch'; exit 1; }
fi

rm -rf "$Q1_PAIR_BIN"
mkdir -p "$Q1_PAIR_BIN"
unzip -q "$PAIR_ARCHIVE" -d "$Q1_PAIR_BIN"
```

Find the TUI binary and record its own version output:

```bash
PAIR_TUI="$(find "$Q1_PAIR_BIN" -type f -name nvpair-tui -perm -u+x | head -n1)"
test -x "$PAIR_TUI" || { echo 'nvpair-tui not found'; exit 1; }
"$PAIR_TUI" --version | tee "$Q1_ARTIFACTS/pair-tui-version.txt"
```

### 5.3 Start PAIR with an isolated user-data home

Use a dedicated HOME/XDG tree so this Q1 does not reuse an existing PAIR profile or the real user's PAIR state.

```bash
mkdir -p "$Q1_PAIR_HOME/.config"

tmux new -s pair-q1
```

Inside the tmux session:

```bash
export HOME="$Q1_PAIR_HOME"
export XDG_CONFIG_HOME="$Q1_PAIR_HOME/.config"
exec "$PAIR_TUI"
```

Detach with `Ctrl-b d`. Reattach with:

```bash
tmux attach -t pair-q1
```

### 5.4 Install a PAIR-owned Ollama engine

In `nvpair-tui`:

1. Open **Engines** (`6`).
2. Select Ollama.
3. Press `i` to install.
4. Wait until the engine reaches a running/healthy state.
5. Press `p` and pull `qwen3.5:4b`.
6. Open **Proxies** (`4`) and record the displayed Ollama proxy endpoint and selected upstream.
7. Open **Engines** again and record the actual Ollama backend port shown by PAIR.

Do not assume the backend is `11435`; record what PAIR actually selected.

Set the observed backend port in the second SSH shell:

```bash
export PAIR_Q1_BACKEND_PORT='<observed-engine-port>'
```

### 5.5 Verify process/port ownership

```bash
sudo ss -ltnp | grep -E ':(11434|'"$PAIR_Q1_BACKEND_PORT"')\\b' \
  | tee "$Q1_ARTIFACTS/q1a-listeners.txt"

curl -fsS http://127.0.0.1:11434/v1/models \
  | jq '{object, model_count:(.data|length), model_ids:[.data[].id]}' \
  > "$Q1_ARTIFACTS/q1a-proxy-models-shape.json"
```

The PASS condition for `proxy_port_11434_behavior` is that PAIR owns the client-facing endpoint and `/v1/models` returns through it.

The PASS condition for `backend_relocation_if_pair_managed` is that the PAIR-installed Ollama backend is listening on a distinct PAIR-controlled port and PAIR reports that backend as its upstream.

### 5.6 Verify the PAIR-owned Ollama directly

The PAIR documentation places its managed Ollama under the PAIR user-data tree. Resolve the executable rather than assuming a complete path:

```bash
PAIR_OLLAMA="$(find "$Q1_PAIR_HOME" -type f -path '*/engine-bin/ollama/*' -name ollama -perm -u+x | head -n1)"
test -x "$PAIR_OLLAMA" || { echo 'PAIR-managed Ollama binary not found'; exit 1; }

PAIR_OLLAMA_ROOT="$(dirname "$(dirname "$PAIR_OLLAMA")")"
LD_LIBRARY_PATH="$PAIR_OLLAMA_ROOT/lib/ollama${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}" \
OLLAMA_HOST="127.0.0.1:$PAIR_Q1_BACKEND_PORT" \
  "$PAIR_OLLAMA" list \
  > "$Q1_ARTIFACTS/q1a-backend-model-list.txt"
```

Confirm the test model appears in the direct backend list and in PAIR `/v1/models`.

### 5.7 Send a bounded inference request without retaining content

```bash
Q1_BODY="$Q1_ROOT/q1a-body.json"
Q1_CODE="$Q1_ROOT/q1a-http-code.txt"

curl -sS -o "$Q1_BODY" -w '%{http_code}\n' \
  http://127.0.0.1:11434/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d "{\"model\":\"$PAIR_Q1_MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"Return the single token OK\"}],\"max_tokens\":8}" \
  > "$Q1_CODE"

jq '{
  object,
  model,
  choices_count:(.choices|length),
  finish_reason:.choices[0].finish_reason,
  usage
}' "$Q1_BODY" > "$Q1_ARTIFACTS/q1a-inference-shape.json"

cat "$Q1_CODE" > "$Q1_ARTIFACTS/q1a-http-code.txt"
rm -f "$Q1_BODY" "$Q1_CODE"
```

Do not persist the response text.

In the TUI, inspect **Workloads** (`5`) and record only workload metadata needed for the lab: state, model ID, timestamps and node identity where available. Do not copy prompt/response content.

### 5.8 Verify model retention across PAIR engine uninstall

Before uninstall:

```bash
PAIR_MODEL_STORE="$(find "$Q1_PAIR_HOME" -type d -name models -path '*/.ollama/*' -print -quit 2>/dev/null || true)"
if [ -z "$PAIR_MODEL_STORE" ] && [ -d "$Q1_PAIR_HOME/.ollama/models" ]; then
  PAIR_MODEL_STORE="$Q1_PAIR_HOME/.ollama/models"
fi

test -d "$PAIR_MODEL_STORE" || { echo 'PAIR model store not located; mark retention check unresolved'; }

if [ -d "$PAIR_MODEL_STORE" ]; then
  find "$PAIR_MODEL_STORE" -type f -printf '%P\t%s\n' | sort \
    | sha256sum > "$Q1_ARTIFACTS/q1a-pair-model-store-before.sha256"
fi
```

In the TUI **Engines** tab, select the PAIR-installed Ollama and press `u` to uninstall. Do not choose a model-delete action.

After uninstall:

```bash
if [ -d "$PAIR_MODEL_STORE" ]; then
  find "$PAIR_MODEL_STORE" -type f -printf '%P\t%s\n' | sort \
    | sha256sum > "$Q1_ARTIFACTS/q1a-pair-model-store-after.sha256"
  diff -u \
    "$Q1_ARTIFACTS/q1a-pair-model-store-before.sha256" \
    "$Q1_ARTIFACTS/q1a-pair-model-store-after.sha256"
fi
```

PASS only if the engine uninstall completes and the downloaded model files remain present. If the store cannot be located reliably, mark the check `unresolved`; do not guess.

### 5.9 Q1A rollback

Quit the TUI with `q`. Confirm its tmux session exited or terminate only that lab session:

```bash
tmux kill-session -t pair-q1 2>/dev/null || true
```

Restore the pre-lab system Ollama state:

```bash
if [ "$Q1_SYSTEM_OLLAMA_WAS_ACTIVE" = 1 ]; then
  sudo systemctl start ollama
fi

systemctl is-active ollama > "$Q1_ARTIFACTS/system-ollama-after-q1a.state" 2>&1 || true
sudo ss -ltnp | grep -E ':(11434|11435)\\b' \
  > "$Q1_ARTIFACTS/inference-listeners-after-q1a.txt" 2>&1 || true
```

Re-hash the Pantheon model-store metadata and compare:

```bash
if sudo test -d /srv/ai/models/ollama; then
  sudo find /srv/ai/models/ollama -type f -printf '%P\t%s\n' \
    | sort | sha256sum \
    > "$Q1_ARTIFACTS/pantheon-ollama-store-after-q1a.sha256"
else
  printf 'absent\n' > "$Q1_ARTIFACTS/pantheon-ollama-store-after-q1a.sha256"
fi

diff -u \
  "$Q1_ARTIFACTS/pantheon-ollama-store-before.sha256" \
  "$Q1_ARTIFACTS/pantheon-ollama-store-after-q1a.sha256"
```

Any unexplained change to the Pantheon-owned model store is a Q1A FAIL and stops the lab.

## 6. Q1B — Linux RTX 4080 + Windows RTX 4090 PAIR cluster

### 6.1 Prepare Windows and resolve the same PAIR pin

Run from the same PR checkout on Windows PowerShell:

```powershell
$lines = python implementation/tools/export_external_qualification_pins.py personal-ai-router
foreach ($line in $lines) {
  $name, $value = $line -split '=', 2
  Set-Item -Path "Env:$name" -Value $value
}

$Q1Root = Join-Path $HOME 'pantheon-labs\pair-unsloth-q1'
$Artifacts = Join-Path $Q1Root 'artifacts'
New-Item -ItemType Directory -Force -Path $Artifacts | Out-Null

nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv,noheader |
  Out-File (Join-Path $Artifacts 'windows-gpu-baseline.txt')
```

Resolve and verify the x64 Windows installer from the selected release:

```powershell
$release = Invoke-RestMethod "https://api.github.com/repos/$env:PAIR_REPOSITORY/releases/tags/v$env:PAIR_VERSION"
$assetName = "NVPAIR-Setup-$($env:PAIR_VERSION)-x64.exe"
$asset = $release.assets | Where-Object { $_.name -eq $assetName } | Select-Object -First 1
if (-not $asset) { throw "PAIR x64 Windows installer not found" }

$installer = Join-Path $Q1Root $assetName
Invoke-WebRequest $asset.browser_download_url -OutFile $installer

$actual = (Get-FileHash $installer -Algorithm SHA256).Hash.ToLowerInvariant()
$expected = ($asset.digest -replace '^sha256:', '').ToLowerInvariant()
$actual | Out-File (Join-Path $Artifacts 'pair-windows-asset.sha256')
if ($expected -and $actual -ne $expected) { throw 'PAIR Windows asset digest mismatch' }

Start-Process -FilePath $installer -Wait
```

Complete first-run setup in PAIR Desktop. Do not start `nvpair-tui` on this Windows node.

### 6.2 Prepare the same test model on Windows

In PAIR Desktop:

1. Open the local node's **Engine settings**.
2. Install/start Ollama through PAIR or record explicitly if PAIR adopts an existing compatible engine.
3. Add `qwen3.5:4b`.
4. Wait until the model is present in the local engine inventory.
5. Record the endpoint shown by **Endpoints** rather than assuming a remembered port.

The same exact model ID must be present independently on Linux and Windows.

### 6.3 Restart the isolated Linux PAIR environment for Q1B

On Linux, temporarily stop the Pantheon system Ollama again if it was active, verify `11434` is free, then restart the same isolated PAIR home used in Q1A.

If the PAIR-owned Ollama was uninstalled in Q1A, reinstall it in TUI **Engines** (`i`). Its retained model store should allow the test model to reappear without a fresh weight download; record whether that actually happens.

### 6.4 Restrictive Linux firewall, only if needed

First inspect the firewall. Do not change it if PAIR discovery/pairing already works.

```bash
sudo ufw status verbose 2>/dev/null || true
```

If UFW is active and blocks the peer, set the Windows node's trusted LAN IP:

```bash
export WINDOWS_Q1_IP='<windows-lan-ip>'
```

Add temporary peer-scoped rules:

```bash
sudo ufw allow from "$WINDOWS_Q1_IP" to any port 5353 proto udp comment 'PAIR-Q1'
for p in 14318 14319 14320 14321 14322 14323; do
  sudo ufw allow from "$WINDOWS_Q1_IP" to any port "$p" proto tcp comment 'PAIR-Q1'
done
```

Do not expose those ports to the Internet.

### 6.5 Pair the nodes

Preferred path for this topology:

1. On Windows Desktop, choose **Add node** and select/discover the Linux node, or enter its LAN IP.
2. On Linux TUI, open **Cluster** (`7`).
3. Accept the inbound invitation with `a`.
4. Enter the six-digit PIN shown by the inviter.
5. Do not save the PIN in artifacts.
6. Confirm both nodes show the same cluster membership.

If discovery is unreliable but direct IP pairing works, record that distinction. Do not reinterpret manual pairing as successful mDNS discovery.

### 6.6 Verify two-node eligibility

Before sending traffic, record from both nodes:

- both nodes online;
- Ollama healthy on both;
- `qwen3.5:4b` present on both;
- proxy endpoint healthy;
- no manual node pin left active unless the current subtest explicitly requires one.

On Linux TUI **Proxies**, press `a` if necessary to ensure automatic selection is active.

### 6.7 Generate a bounded concurrent burst

Use the Windows local PAIR endpoint so the Desktop **Jobs** view can provide `Ran on` observation.

First copy the current Windows Ollama/OpenAI-compatible endpoint from **Endpoints** into:

```powershell
$PairBase = 'http://127.0.0.1:11434'
$Model = 'qwen3.5:4b'
```

If Desktop displays a different port, use the displayed value instead.

Run twelve independent requests with PowerShell jobs:

```powershell
$jobs = 1..12 | ForEach-Object {
  Start-Job -ArgumentList $PairBase, $Model, $_ -ScriptBlock {
    param($Base, $ModelName, $Index)
    $body = @{
      model = $ModelName
      messages = @(@{ role = 'user'; content = "Return only OK $Index" })
      max_tokens = 16
    } | ConvertTo-Json -Depth 5
    $sw = [Diagnostics.Stopwatch]::StartNew()
    try {
      $null = Invoke-RestMethod "$Base/v1/chat/completions" -Method Post -ContentType 'application/json' -Body $body
      $sw.Stop()
      [pscustomobject]@{ index=$Index; status='success'; elapsed_ms=$sw.ElapsedMilliseconds }
    } catch {
      $sw.Stop()
      [pscustomobject]@{ index=$Index; status='error'; elapsed_ms=$sw.ElapsedMilliseconds; error=$_.Exception.Message }
    }
  }
}

$results = $jobs | Receive-Job -Wait
$jobs | Remove-Job
$results | ConvertTo-Json | Out-File (Join-Path $Artifacts 'q1b-burst-results.json')
```

Do not save response bodies.

In Windows Desktop **Jobs**, record the `Ran on` node for the twelve requests. Save only counts and request timing metadata, for example:

```json
{
  "linux_node_count": 0,
  "windows_node_count": 0,
  "other_count": 0
}
```

PASS for `concurrent_request_distribution` requires successful requests and observed use of both eligible nodes during a bounded concurrent burst. If every request goes to one node while both remain eligible, record the scheduler outcome and mark this check `unresolved` or `fail` according to the observed eligibility data; do not manufacture balance.

### 6.8 Stop the Linux PAIR service and verify failover

Quit Linux `nvpair-tui` with `q` or terminate only its tmux session. Do not power off the Linux host for the first failover test.

Wait until Windows shows the Linux node offline/ineligible, then send three more requests from Windows.

PASS requires:

- all three requests complete on Windows;
- Jobs shows `Ran on` Windows for those requests;
- no request is reported as served by the stopped Linux node.

### 6.9 Rejoin the Linux node

Restart `nvpair-tui` with the same isolated `HOME` and `XDG_CONFIG_HOME`.

PASS requires:

- prior cluster membership is restored or the required re-pair step is explicitly observed;
- Linux becomes online/eligible again;
- its engine/model inventory becomes visible;
- a new concurrent burst can use Linux again.

If re-pairing is required, record that as observed persistence behavior rather than silently repeating setup.

### 6.10 Q1B rollback

On Linux:

- leave/remove the temporary cluster membership if Q1 is ending;
- quit the TUI;
- restore the system Ollama pre-lab state;
- remove only firewall rules carrying the `PAIR-Q1` comment if they were added.

Inspect before deleting rules:

```bash
sudo ufw status numbered
```

Delete the specific Q1 rule numbers in descending order. Do not flush unrelated firewall rules.

On Windows, if PAIR was installed only for Q1 and the stage is complete, remove it through **Installed apps** after first leaving the test cluster. If PAIR installed an Ollama engine and engine-retention behavior is also being observed there, uninstall the engine from PAIR before removing the application and record whether its model files remain. Do not delete an existing user-managed Ollama installation.

## 7. Q1C — current Hermes container network namespace to local PAIR

Q1C answers one bounded question: can the current Pantheon Hermes container network namespace reach PAIR's plaintext local client ingress without changing networking?

### 7.1 Restore the PAIR lab endpoint on Linux

As in Q1A/Q1B:

- stop the system Ollama temporarily if needed;
- start the isolated Linux PAIR TUI;
- start/reinstall its PAIR-owned Ollama;
- confirm the test model is present;
- confirm `curl http://127.0.0.1:11434/v1/models` succeeds on the host.

### 7.2 Prove the current Compose/network configuration was not changed

```bash
sudo sha256sum /opt/pantheon-node/compose.yaml \
  > "$Q1_ARTIFACTS/q1c-compose-before.sha256"

docker inspect pantheon-hermes \
  --format '{{json .HostConfig.ExtraHosts}}' \
  > "$Q1_ARTIFACTS/q1c-hermes-extra-hosts.json"

docker inspect pantheon-hermes \
  --format '{{json .NetworkSettings.Networks}}' \
  > "$Q1_ARTIFACTS/q1c-hermes-networks.json"
```

Do not add `network_mode: host`, a relay container, iptables redirection or a Compose override before this measurement.

### 7.3 Probe PAIR from the actual Hermes container namespace

Use Python from inside the Hermes container so the test does not depend on `curl` being installed in the image:

```bash
docker exec -i pantheon-hermes python - <<'PY' \
  > "$Q1_ARTIFACTS/q1c-container-probe.txt" 2>&1
import socket
import urllib.error
import urllib.request

url = "http://host.docker.internal:11434/v1/models"
print("container_hostname=", socket.gethostname())
try:
    print("container_ip=", socket.gethostbyname(socket.gethostname()))
except Exception as exc:
    print("container_ip_error=", type(exc).__name__)
print("host_gateway_ip=", socket.gethostbyname("host.docker.internal"))

try:
    with urllib.request.urlopen(url, timeout=10) as response:
        print("http_status=", response.status)
        print("content_type=", response.headers.get("Content-Type"))
except urllib.error.HTTPError as exc:
    print("http_status=", exc.code)
    body = exc.read(512).decode("utf-8", errors="replace")
    print("error_body_prefix=", body)
except Exception as exc:
    print("transport_error=", type(exc).__name__, str(exc)[:200])
PY
```

This probe contains no user prompt or model response content.

### 7.4 Classify the observed result

Record exactly one of these categories:

- `accepted_http_2xx` — the current container path reaches PAIR's client API;
- `refused_http_403_loopback` — PAIR receives the request and rejects it at its local ingress gate;
- `connection_refused_or_timeout` — route/listener problem before an HTTP decision;
- `other_http_error` — PAIR or backend returns another HTTP status;
- `unresolved` — observation cannot distinguish the failure layer.

Do not pre-fill `403` before execution.

If the result is refusal, Q1C ends there. Host networking, a host-native Hermes process, an mTLS client path or a relay are separate candidate experiments and require their own qualification scope.

### 7.5 Q1C rollback and integrity check

```bash
sudo sha256sum /opt/pantheon-node/compose.yaml \
  > "$Q1_ARTIFACTS/q1c-compose-after.sha256"

diff -u \
  "$Q1_ARTIFACTS/q1c-compose-before.sha256" \
  "$Q1_ARTIFACTS/q1c-compose-after.sha256"
```

Quit the PAIR TUI and restore the system Ollama pre-lab state.

PASS for `no_relay_or_host_network_change_in_q1` requires the Compose hash to be unchanged.

## 8. Q1D — Unsloth through the existing Hermes provider seam

Q1D deliberately does not use `unsloth start hermes`. It runs the selected Unsloth code as an external inference server and uses the already-selected Hermes runtime's named-custom-provider support.

### 8.1 Prepare the pinned Unsloth source in an isolated venv

```bash
rm -rf "$Q1_UNSLOTH_SRC" "$Q1_UNSLOTH_VENV"

git clone --filter=blob:none "https://github.com/${UNSLOTH_REPOSITORY}.git" "$Q1_UNSLOTH_SRC"
git -C "$Q1_UNSLOTH_SRC" fetch --depth=1 origin "$UNSLOTH_REF"
git -C "$Q1_UNSLOTH_SRC" checkout --detach "$UNSLOTH_REF"

test "$(git -C "$Q1_UNSLOTH_SRC" rev-parse HEAD)" = "$UNSLOTH_REF" \
  || { echo 'Unsloth checkout does not match qualification pin'; exit 1; }

printf '%s\n' "$(git -C "$Q1_UNSLOTH_SRC" rev-parse HEAD)" \
  > "$Q1_ARTIFACTS/q1d-unsloth-source-ref.txt"

uv venv "$Q1_UNSLOTH_VENV" --python 3.13
uv pip install --python "$Q1_UNSLOTH_VENV/bin/python" \
  -e "$Q1_UNSLOTH_SRC" --torch-backend=auto

PATH="$Q1_UNSLOTH_VENV/bin:$PATH" unsloth studio setup
PATH="$Q1_UNSLOTH_VENV/bin:$PATH" unsloth --help \
  > "$Q1_ARTIFACTS/q1d-unsloth-cli-help.txt"
```

`unsloth studio setup` may compile/download runtime dependencies. Record their versions in the lab artifacts; do not reinterpret those transitive versions as new Pantheon pins.

### 8.2 Bind Unsloth only to the Docker bridge gateway

Derive the host-side gateway that `host.docker.internal` maps to for the current Docker bridge:

```bash
export Q1_DOCKER_GATEWAY="$(docker network inspect bridge -f '{{(index .IPAM.Config 0).Gateway}}')"
test -n "$Q1_DOCKER_GATEWAY" || { echo 'Docker bridge gateway unresolved'; exit 1; }
printf '%s\n' "$Q1_DOCKER_GATEWAY" > "$Q1_ARTIFACTS/q1d-docker-gateway.txt"
```

Before launch, verify the selected address is not a wildcard and is not a normal LAN address chosen by hand:

```bash
case "$Q1_DOCKER_GATEWAY" in
  0.0.0.0|::) echo 'Refusing wildcard Unsloth bind'; exit 1 ;;
esac
```

Start the server in tmux:

```bash
tmux new -s unsloth-q1
```

Inside the tmux session:

```bash
source "$Q1_UNSLOTH_VENV/bin/activate"
unsloth run \
  --model "$UNSLOTH_Q1_MODEL" \
  --max-seq-length "$UNSLOTH_Q1_CONTEXT" \
  --host "$Q1_DOCKER_GATEWAY" \
  --port "$UNSLOTH_Q1_PORT" \
  --api-key-name pantheon-q1
```

Unsloth prints a temporary API key. Copy it into the current operator shell as `UNSLOTH_Q1_API_KEY` but do not write it to a file or shell script.

```bash
read -rsp 'Temporary Unsloth Q1 API key: ' UNSLOTH_Q1_API_KEY
echo
export UNSLOTH_Q1_API_KEY
```

If a key fingerprint is useful:

```bash
printf '%s' "$UNSLOTH_Q1_API_KEY" | sha256sum \
  | awk '{print $1}' \
  > "$Q1_ARTIFACTS/q1d-unsloth-key-fingerprint.sha256"
```

Never save the key itself.

### 8.3 Verify the Unsloth OpenAI-compatible surface from the host

```bash
curl -fsS \
  -H "Authorization: Bearer $UNSLOTH_Q1_API_KEY" \
  "http://$Q1_DOCKER_GATEWAY:$UNSLOTH_Q1_PORT/v1/models" \
  | jq '{object, model_count:(.data|length), model_ids:[.data[].id]}' \
  > "$Q1_ARTIFACTS/q1d-models-shape.json"
```

Read the actual model ID returned by `/v1/models` and set it explicitly:

```bash
export UNSLOTH_Q1_SERVED_MODEL='<exact-id-returned-by-v1-models>'
```

Do not assume the served model ID is identical to the Hugging Face locator.

### 8.4 Verify direct streaming without retaining generated content

```bash
Q1_STREAM="$Q1_ROOT/q1d-stream.txt"

curl -sS -N \
  -H "Authorization: Bearer $UNSLOTH_Q1_API_KEY" \
  -H 'Content-Type: application/json' \
  "http://$Q1_DOCKER_GATEWAY:$UNSLOTH_Q1_PORT/v1/chat/completions" \
  -d "{\"model\":\"$UNSLOTH_Q1_SERVED_MODEL\",\"stream\":true,\"messages\":[{\"role\":\"user\",\"content\":\"Return the single token OK\"}],\"max_tokens\":8}" \
  > "$Q1_STREAM"

python - "$Q1_STREAM" <<'PY' > "$Q1_ARTIFACTS/q1d-stream-shape.txt"
import sys
from pathlib import Path
p = Path(sys.argv[1])
lines = [line for line in p.read_text(errors="replace").splitlines() if line.startswith("data:")]
print("sse_data_lines=", len(lines))
print("has_done=", any("[DONE]" in line for line in lines))
PY
rm -f "$Q1_STREAM"
```

PASS requires an actual streamed response grammar, not merely HTTP 200.

### 8.5 Verify structured tool-call capability directly

Send a harmless synthetic tool schema. The tool is not executed in this direct API check.

```bash
Q1_TOOL_BODY="$Q1_ROOT/q1d-tool-body.json"

curl -fsS \
  -H "Authorization: Bearer $UNSLOTH_Q1_API_KEY" \
  -H 'Content-Type: application/json' \
  "http://$Q1_DOCKER_GATEWAY:$UNSLOTH_Q1_PORT/v1/chat/completions" \
  -d "{\"model\":\"$UNSLOTH_Q1_SERVED_MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"Use the q1_echo tool with value PANTHEON_Q1_TOOL_OK.\"}],\"tools\":[{\"type\":\"function\",\"function\":{\"name\":\"q1_echo\",\"description\":\"Return a provided test string\",\"parameters\":{\"type\":\"object\",\"properties\":{\"value\":{\"type\":\"string\"}},\"required\":[\"value\"]}}}],\"tool_choice\":\"auto\",\"max_tokens\":64}" \
  > "$Q1_TOOL_BODY"

jq '{
  model,
  finish_reason:.choices[0].finish_reason,
  tool_call_count:(.choices[0].message.tool_calls // [] | length),
  tool_names:[(.choices[0].message.tool_calls // [])[].function.name]
}' "$Q1_TOOL_BODY" > "$Q1_ARTIFACTS/q1d-direct-tool-shape.json"
rm -f "$Q1_TOOL_BODY"
```

PASS requires a structured tool call for the named test tool. Text that merely describes calling a tool is not a structured-tool PASS.

### 8.6 Hash the governed Hermes profile before creating the temporary lab profile

The current Docker deployment uses a persistent Hermes data volume. Hash only metadata/configuration of the governed profile; do not print secrets.

```bash
docker exec pantheon-hermes sh -lc '
  if [ -d /opt/data/profiles/pantheon-governed ]; then
    find /opt/data/profiles/pantheon-governed -type f -printf "%P\\t%s\\n" | sort | sha256sum
  else
    echo absent
  fi
' > "$Q1_ARTIFACTS/q1d-governed-profile-before.sha256"
```

### 8.7 Create a temporary Hermes profile cloned from `pantheon-governed`

Use the selected Hermes runtime already in the container. Do not launch `unsloth start hermes` and do not set a new global `HERMES_HOME`.

```bash
docker exec pantheon-hermes \
  hermes profile create pantheon-q1-unsloth --clone-from pantheon-governed
```

Find the temporary profile config path:

```bash
docker exec pantheon-hermes \
  hermes -p pantheon-q1-unsloth config path \
  > "$Q1_ARTIFACTS/q1d-hermes-lab-config-path.txt"
```

### 8.8 Configure only the temporary Hermes profile

The named custom provider must point to the host through the existing `host.docker.internal` mapping. The API key remains process-local through `UNSLOTH_API_KEY`; do not persist it in YAML.

Use a Python/YAML edit inside the container so only the temporary profile config is changed. First obtain the config path from `hermes ... config path` and set `Q1_CONFIG` accordingly.

The resulting provider/model portion must be equivalent to:

```yaml
model:
  provider: custom:unsloth-q1
  default: <exact-id-from-Unsloth-v1-models>

providers:
  unsloth-q1:
    api: http://host.docker.internal:18888/v1
    key_env: UNSLOTH_API_KEY
    transport: chat_completions
```

Do not replace the rest of the cloned profile configuration. In particular, preserve the inherited Pantheon-governed memory/tool posture unless the lab explicitly records a necessary compatibility difference.

A bounded mutation command is:

```bash
Q1_CONFIG="$(tr -d '\r\n' < "$Q1_ARTIFACTS/q1d-hermes-lab-config-path.txt")"

docker exec -i \
  -e Q1_CONFIG="$Q1_CONFIG" \
  -e Q1_MODEL="$UNSLOTH_Q1_SERVED_MODEL" \
  pantheon-hermes python - <<'PY'
import os
from pathlib import Path
import yaml

path = Path(os.environ["Q1_CONFIG"])
data = yaml.safe_load(path.read_text()) or {}
data.setdefault("model", {})["provider"] = "custom:unsloth-q1"
data["model"]["default"] = os.environ["Q1_MODEL"]
data.setdefault("providers", {})["unsloth-q1"] = {
    "api": "http://host.docker.internal:18888/v1",
    "key_env": "UNSLOTH_API_KEY",
    "transport": "chat_completions",
}
path.write_text(yaml.safe_dump(data, sort_keys=False))
PY
```

Record a redacted view only:

```bash
docker exec pantheon-hermes \
  hermes -p pantheon-q1-unsloth config check \
  > "$Q1_ARTIFACTS/q1d-hermes-config-check.txt" 2>&1
```

### 8.9 Execute Hermes through the temporary profile

First a no-tool one-shot:

```bash
docker exec \
  -e UNSLOTH_API_KEY="$UNSLOTH_Q1_API_KEY" \
  pantheon-hermes \
  hermes -p pantheon-q1-unsloth -z 'Return the single token OK' \
  > /dev/null
```

Record only the exit status:

```bash
printf '%s\n' "$?" > "$Q1_ARTIFACTS/q1d-hermes-oneshot-exit.txt"
```

Then run a bounded harmless tool round trip under normal approval policy:

```bash
docker exec -it \
  -e UNSLOTH_API_KEY="$UNSLOTH_Q1_API_KEY" \
  pantheon-hermes \
  hermes -p pantheon-q1-unsloth chat \
  -t terminal \
  --max-turns 3 \
  -q 'Use the terminal tool once to run: printf PANTHEON_Q1_TOOL_OK . Return exactly its stdout.'
```

Do not use `--yolo`. If prompted, approve only that exact `printf` command.

PASS for the Hermes tool round trip requires all of the following:

- the model emits a real structured tool call that Hermes accepts;
- Hermes invokes the terminal tool under the current approval policy;
- the bounded command executes;
- the model receives the tool result and completes the turn;
- no provider fallback silently served the request instead.

Record exit status, provider/model identity and whether approval occurred. Do not persist the conversation body.

### 8.10 Context and provider-error checks

Context check: send a deterministic synthetic prompt larger than the tiny smoke test but below the configured `16384` limit and record success/failure plus token/latency metadata. Do not use project documents or private content.

Provider-error check: run a single Hermes request with a deliberately invalid process-local API key:

```bash
docker exec \
  -e UNSLOTH_API_KEY='q1-deliberately-invalid' \
  pantheon-hermes \
  hermes -p pantheon-q1-unsloth -z 'Return OK' \
  > /dev/null 2> "$Q1_ARTIFACTS/q1d-invalid-key-error.txt"
printf '%s\n' "$?" > "$Q1_ARTIFACTS/q1d-invalid-key-exit.txt"
```

Redact the error artifact if it unexpectedly contains credentials. PASS requires a clear provider/auth failure rather than silent fallback to another model/provider.

### 8.11 Q1D rollback

Delete only the temporary profile:

```bash
docker exec pantheon-hermes \
  hermes profile delete pantheon-q1-unsloth
```

Hash the governed profile again:

```bash
docker exec pantheon-hermes sh -lc '
  if [ -d /opt/data/profiles/pantheon-governed ]; then
    find /opt/data/profiles/pantheon-governed -type f -printf "%P\\t%s\\n" | sort | sha256sum
  else
    echo absent
  fi
' > "$Q1_ARTIFACTS/q1d-governed-profile-after.sha256"

diff -u \
  "$Q1_ARTIFACTS/q1d-governed-profile-before.sha256" \
  "$Q1_ARTIFACTS/q1d-governed-profile-after.sha256"
```

PASS for `pantheon_governed_profile_not_mutated` requires equality.

Stop only the Unsloth lab server and remove its temporary key from the shell:

```bash
tmux kill-session -t unsloth-q1 2>/dev/null || true
unset UNSLOTH_Q1_API_KEY
```

The source checkout, venv and downloaded model may remain under `$Q1_ROOT` until Q1E review. They are lab artifacts, not an installation claim.

## 9. Q1E — observation record and independent classification

Do not classify PAIR and Unsloth from narrative memory. Build one row per required check.

Each row must contain:

```json
{
  "check_id": "",
  "stage_id": "",
  "host": "",
  "command_or_action": "",
  "expected_observation": "",
  "actual_observation": "",
  "status": "pass|fail|unresolved|not_run",
  "artifact_ref": "",
  "started_at": "",
  "ended_at": "",
  "notes": ""
}
```

The observation file must not contain secrets, PINs, prompts or response bodies.

### 9.1 PAIR acceptance decision

PAIR can be classified `accepted` for a later deployment-design PR only if Q1 observations establish at minimum:

- exact selected artifact identity;
- isolated local proxy and PAIR-managed backend behavior;
- same-model two-node request routing;
- clean node exclusion and recovery;
- serving-node observability through an available surface;
- model retention across PAIR engine uninstall;
- rollback to the prior Pantheon system Ollama state;
- no unexplained change to `/srv/ai/models/ollama`;
- an explicit result for current Hermes-container-to-PAIR connectivity;
- a documented answer to the future Ollama lifecycle/port owner question.

A Q1C loopback refusal does not automatically reject PAIR. It rejects the current container-to-local-plaintext path and leaves topology redesign as a separate decision.

### 9.2 Unsloth acceptance decision

Unsloth can be classified `accepted` for a later provider/deployment-design PR only if Q1 observations establish at minimum:

- exact selected source identity;
- local OpenAI-compatible endpoint health;
- streaming;
- structured tool-call production;
- Hermes one-shot compatibility through a named custom provider;
- one bounded Hermes tool round trip under normal approval policy;
- explicit context behavior;
- explicit provider-error behavior with no silent fallback;
- no mutation of `pantheon-governed`;
- no `unsloth start hermes` ownership path;
- rollback of the temporary Hermes profile and Unsloth server.

### 9.3 Outcome vocabulary

Use only:

- `accepted` — all mandatory checks support proceeding to a separate deployment-design PR;
- `rejected` — a mandatory compatibility/safety property failed and no Q1-compatible composition remains;
- `unresolved` — one or more mandatory checks are not yet observed or cannot be attributed confidently.

`accepted` still does not mean deployed, activated, authorized or Evidence-admitted.

## 10. Stop conditions

Stop the lab immediately and record the stage `unresolved` or `fail` as appropriate if:

- an artifact digest does not match its release metadata;
- the checked-out source does not match the canonical pin;
- an unknown process owns a required port;
- the Pantheon Ollama model-store metadata changes unexpectedly;
- Q1 requires editing `release.env`, `install-node`, the Hermes distribution lock or production Compose to continue;
- PAIR requires exposing its local plaintext proxy to the LAN;
- Unsloth must bind to `0.0.0.0` merely to reach Hermes;
- a secret would need to be committed or persisted in a lab artifact;
- Hermes silently falls back to another provider during a compatibility check;
- the `pantheon-governed` profile changes during Q1D.

A stop condition is a useful qualification result. Do not bypass it merely to obtain a green lab.
