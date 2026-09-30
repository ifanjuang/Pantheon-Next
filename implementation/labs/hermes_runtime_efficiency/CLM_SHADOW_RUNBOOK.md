# CLM shadow-ranking qualification on the Linux node

Status: candidate qualification procedure for Pantheon issue #1047. This is not a production installation, Hermes route, authorization path or adoption decision.

## Objective

Run the reviewed Contrastive-LM candidate locally on the Linux GPU node and record passive rankings over a short synthetic Pantheon corpus.

```text
synthetic state + fixed candidate actions
                  |
                  v
          local CLM /v1/rank
                  |
                  v
         shadow observation JSON

CLM output -> never dispatched to Hermes
CLM output -> never reaches an effect owner
```

Do not wire CLM into Hermes, Pantheon admission, the PEP/effect chokepoint, Hindsight, Knowledge or Cockpit during this qualification.

## Authority and artifact source

All candidate identities come from the existing canonical qualification owner:

```text
implementation/qualification/external-pins.json
  -> pins.contrastive-lm
```

The run must not resolve mutable upstream `main` / latest model state and then call it equivalent.

The pin owns:

```text
CLM repository + exact git ref
package version
encoder model + exact revision
public CLM head repository + exact revision + file + SHA-256
API surface
```

The pin is qualification input only:

```text
selected candidate != installed
installed != qualified
qualified != activated
shadow rank != Hermes decision
```

Known upstream cautions for this slice:

- CLM is alpha software;
- upstream reports exist for unexpected typed `score` behavior, so this slice uses `/v1/rank` only;
- long-state truncation behavior is still a qualification concern, so the first corpus intentionally stays short;
- a successful run does not qualify CLM for routing or activation.

## 1. Repository and GPU preflight

Use a current checkout containing this qualification slice:

```bash
git rev-parse HEAD
git status --short

nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv
python3 --version
```

Do not silently introduce quantization, a different encoder, CPU offload or another serving backend merely to make the reference run fit. Such a change is a different experimental arm and must be qualified separately.

If the selected reference stack cannot load on the Linux GPU, record this first run as blocked rather than treating a modified stack as equivalent.

## 2. Export the canonical CLM candidate

From the Pantheon-Next repository root:

```bash
python3 - <<'PY' > /tmp/clm-shadow-pin.env
import json
import shlex
from pathlib import Path

registry = json.loads(
    Path("implementation/qualification/external-pins.json").read_text(encoding="utf-8")
)
pin = registry["pins"]["contrastive-lm"]

fields = {
    "CLM_REPOSITORY": "repository",
    "CLM_VERSION": "version",
    "CLM_GIT_REF": "ref",
    "CLM_ENCODER_MODEL": "encoder_model",
    "CLM_ENCODER_REVISION": "encoder_revision",
    "CLM_HEAD_REPOSITORY": "head_repository",
    "CLM_HEAD_REVISION": "head_revision",
    "CLM_HEAD_FILE": "head_file",
    "CLM_HEAD_SHA256": "head_sha256",
    "CLM_API_SURFACE": "api_surface",
}
for env_name, field in fields.items():
    value = str(pin[field])
    print(f"export {env_name}={shlex.quote(value)}")
PY

source /tmp/clm-shadow-pin.env
cat /tmp/clm-shadow-pin.env
```

Do not hand-edit this file to make a run pass. A different candidate belongs in the qualification registry through a reviewed repository change.

## 3. Create an isolated CLM environment

Do not install CLM into the Hermes Python environment.

```bash
python3 -m venv ~/.venvs/clm-shadow
source ~/.venvs/clm-shadow/bin/activate
python -m pip install --upgrade pip

python -m pip install \
  "git+https://github.com/${CLM_REPOSITORY}.git@${CLM_GIT_REF}" \
  huggingface_hub
```

Verify the installed package identity:

```bash
CLM_PACKAGE_OBSERVED="$(python - <<'PY'
from importlib.metadata import version
print(version("contrastive-lm"))
PY
)"
VLLM_VERSION="$(python - <<'PY'
from importlib.metadata import version
print(version("vllm"))
PY
)"

printf 'contrastive-lm=%s\nvllm=%s\n' "$CLM_PACKAGE_OBSERVED" "$VLLM_VERSION"

test "$CLM_PACKAGE_OBSERVED" = "$CLM_VERSION" || {
  echo "contrastive-lm package version differs from canonical pin" >&2
  exit 1
}

python -m pip freeze > /tmp/clm-shadow-pip-freeze.txt
```

## 4. Fetch and verify the exact CLM head

Download the exact Hugging Face artifact selected by the registry, not its mutable latest state:

```bash
source ~/.venvs/clm-shadow/bin/activate
source /tmp/clm-shadow-pin.env

python - <<'PY'
import os
from pathlib import Path
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id=os.environ["CLM_HEAD_REPOSITORY"],
    filename=os.environ["CLM_HEAD_FILE"],
    revision=os.environ["CLM_HEAD_REVISION"],
)
Path("/tmp/clm-shadow-head-path").write_text(path + "\n", encoding="utf-8")
print(path)
PY

HEAD_PATH="$(cat /tmp/clm-shadow-head-path)"
HEAD_SHA256="$(sha256sum "$HEAD_PATH" | awk '{print $1}')"

printf 'head=%s\nsha256=%s\n' "$HEAD_PATH" "$HEAD_SHA256"

test "$HEAD_SHA256" = "$CLM_HEAD_SHA256" || {
  echo "CLM head SHA-256 differs from canonical pin" >&2
  exit 1
}
```

## 5. Start the exact encoder on loopback

Terminal A:

```bash
source ~/.venvs/clm-shadow/bin/activate
source /tmp/clm-shadow-pin.env

vllm serve "$CLM_ENCODER_MODEL" \
  --revision "$CLM_ENCODER_REVISION" \
  --served-model-name qwen3-8b \
  --runner pooling \
  --max-model-len 2048 \
  --host 127.0.0.1 \
  --port 8090
```

The first qualification intentionally keeps the CLM state limit at 2048 tokens. This does not establish that 2048 is sufficient for later professional workloads.

## 6. Start CLM with the verified head

Terminal B:

```bash
source ~/.venvs/clm-shadow/bin/activate
source /tmp/clm-shadow-pin.env

HEAD_PATH="$(cat /tmp/clm-shadow-head-path)"

export CLM_API_KEY="$(openssl rand -hex 32)"
printf '%s\n' "$CLM_API_KEY" > /tmp/clm-shadow-api-key
chmod 600 /tmp/clm-shadow-api-key

clm-serve \
  --host 127.0.0.1 \
  --port 8700 \
  --emb-url http://127.0.0.1:8090/v1/embeddings \
  --emb-model qwen3-8b \
  --max-tokens 2048 \
  --ckpt "$HEAD_PATH" \
  --no-download \
  --no-ui
```

Always pass `--host 127.0.0.1`. The upstream server's general-purpose default is not the boundary selected for this local qualification.

## 7. Verify the live local surface

From another shell:

```bash
source ~/.venvs/clm-shadow/bin/activate
export CLM_API_KEY="$(cat /tmp/clm-shadow-api-key)"

curl -fsS http://127.0.0.1:8700/health | python -m json.tool
curl -fsS \
  -H "Authorization: Bearer $CLM_API_KEY" \
  http://127.0.0.1:8700/v1/models | python -m json.tool
```

Required observations:

```text
health.ok       = true
health.embedder = true
health.mock     != true
clm-latest      is exposed
```

A healthy process is only a technical observation.

## 8. Record exact runtime identity

Create the runtime receipt from the exact values already used to serve:

```bash
source ~/.venvs/clm-shadow/bin/activate
source /tmp/clm-shadow-pin.env

CLM_PACKAGE_OBSERVED="$(python - <<'PY'
from importlib.metadata import version
print(version("contrastive-lm"))
PY
)"
VLLM_VERSION="$(python - <<'PY'
from importlib.metadata import version
print(version("vllm"))
PY
)"
DEVICE_NAME="$(nvidia-smi --query-gpu=name --format=csv,noheader | head -n1)"
HEAD_PATH="$(cat /tmp/clm-shadow-head-path)"
HEAD_SHA256="$(sha256sum "$HEAD_PATH" | awk '{print $1}')"

export CLM_PACKAGE_OBSERVED VLLM_VERSION DEVICE_NAME HEAD_SHA256

python - <<'PY'
import json
import os
from pathlib import Path

receipt = {
    "clm_git_ref": os.environ["CLM_GIT_REF"],
    "clm_package_version": os.environ["CLM_PACKAGE_OBSERVED"],
    "encoder_model": os.environ["CLM_ENCODER_MODEL"],
    "encoder_revision": os.environ["CLM_ENCODER_REVISION"],
    "head_sha256": os.environ["HEAD_SHA256"],
    "vllm_version": os.environ["VLLM_VERSION"],
    "device_name": os.environ["DEVICE_NAME"],
}
Path("/tmp/clm-runtime.json").write_text(
    json.dumps(receipt, indent=2) + "\n",
    encoding="utf-8",
)
PY

cat /tmp/clm-runtime.json
```

The shadow runner independently compares this receipt against `external-pins.json`. A different CLM git ref, package version, encoder model/revision or head SHA-256 fails the run before ranking.

## 9. Run the passive corpus

From the Pantheon-Next repository root:

```bash
export CLM_API_KEY="$(cat /tmp/clm-shadow-api-key)"

python implementation/labs/hermes_runtime_efficiency/clm_shadow_rank.py \
  implementation/labs/hermes_runtime_efficiency/clm_shadow_cases.json \
  --runtime-metadata /tmp/clm-runtime.json \
  --pin-registry implementation/qualification/external-pins.json \
  --base-url http://127.0.0.1:8700 \
  --max-orderings 4 \
  --output /tmp/clm-shadow-report.json
```

Inspect the observation summary:

```bash
python - <<'PY'
import json
from pathlib import Path

report = json.loads(Path("/tmp/clm-shadow-report.json").read_text(encoding="utf-8"))
print(json.dumps(report["summary"], indent=2))
PY
```

The runner deliberately permutes candidate order. A case is `top_candidate_order_stable` only when the same candidate remains first across all tested orderings.

Initial signals:

```text
expected_top1_all_orderings_rate
top_candidate_order_stable_rate
per-case ranked probabilities
CLM latency header
transport elapsed time
```

Do not collapse them into one universal model score.

## 10. First-pass interpretation

```text
low expected-match rate
-> published CLM candidate is not useful for this decision family

high expected match + low order stability
-> presentation sensitivity is material; do not use as a routing primitive

high expected match + high order stability
-> candidate for a larger held-out shadow corpus only

good synthetic shadow result
!= permission to wire CLM into Hermes
```

Only after a larger held-out corpus should a separate experiment ask whether CLM can reduce real Hermes selection cost.

## 11. Preserved boundaries

```text
CLM rank != Hermes decision
CLM rank != Pantheon authorization
fixture expected answer != professional truth
shadow observation != Evidence
runtime success != model qualification
model qualification != activation
```

CLM receives no consequential credential. The Pantheon effect owner / PEP remains unchanged.

## 12. Removal

The experiment remains removable. Deleting the CLM-specific lab files and qualification pin restores the previous #1047 lab behavior; no product module imports the shadow runner, no schema migration is introduced, and no runtime route depends on it.
