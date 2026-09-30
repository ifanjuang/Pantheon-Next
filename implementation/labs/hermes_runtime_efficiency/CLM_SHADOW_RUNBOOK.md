# CLM shadow-ranking qualification on the Linux node

Status: candidate qualification procedure for Pantheon issue #1047. This is not a production installation, Hermes route, authorization path or adoption decision.

## Objective

Run the published Contrastive-LM ranker locally on the Linux GPU node and compare its passive ranking against a small synthetic Pantheon decision corpus.

The first slice is deliberately one-way:

```text
synthetic state + candidate actions
              |
              v
        local CLM ranker
              |
              v
     shadow observation JSON

CLM output -> never dispatched to Hermes
CLM output -> never reaches an effect owner
```

Do not wire CLM into Hermes, Pantheon admission, the PEP/effect chokepoint, Hindsight, Knowledge or Cockpit during this qualification.

## Selected upstream candidate

The canonical qualification pin belongs in `implementation/qualification/external-pins.json`.

At the time this runbook was added:

```text
repository : Contrastive-LM/CLM
package    : contrastive-lm 0.1.0
git ref    : bb42c6c5bf914fd449bed2f6ca65be80602cb1f7
encoder    : Qwen/Qwen3-8B
API        : POST /v1/rank
```

The git ref is a reviewed qualification input, not deployment truth. Re-read the registry before running.

Known qualification caution at this pin:

- CLM is alpha software;
- upstream reports exist for unexpected `score` behavior, so this slice uses `/v1/rank` only;
- long-state truncation behavior is under upstream discussion, so the initial corpus intentionally stays short;
- a successful run does not qualify CLM for routing or activation.

## 1. GPU preflight

On the Linux node:

```bash
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv
python3 --version
```

Do not silently introduce quantization, a different encoder or CPU offload merely to make the reference run fit. Any such change creates a different experimental arm and must be recorded separately.

The upstream quickstart demonstrates the reference path on a 24 GB RTX 4090. If the Linux GPU cannot load Qwen3-8B with the selected serving configuration, record the run as blocked rather than calling a modified stack equivalent.

## 2. Create an isolated environment

Use a dedicated environment outside the Hermes environment:

```bash
python3 -m venv ~/.venvs/clm-shadow
source ~/.venvs/clm-shadow/bin/activate
python -m pip install --upgrade pip

python -m pip install \
  "git+https://github.com/Contrastive-LM/CLM.git@bb42c6c5bf914fd449bed2f6ca65be80602cb1f7"
python -m pip install huggingface_hub
```

Record the resolved environment rather than assuming dependency versions:

```bash
python -m pip freeze > /tmp/clm-shadow-pip-freeze.txt
python - <<'PY'
from importlib.metadata import version
print("contrastive-lm", version("contrastive-lm"))
print("vllm", version("vllm"))
PY
```

Do not install CLM into the Hermes Python environment for this slice.

## 3. Start the encoder on loopback only

Terminal A:

```bash
source ~/.venvs/clm-shadow/bin/activate

ENCODER_REVISION="$(python - <<'PY'
from huggingface_hub import model_info
print(model_info("Qwen/Qwen3-8B").sha)
PY
)"
printf '%s\n' "$ENCODER_REVISION" > /tmp/clm-shadow-encoder-revision

vllm serve Qwen/Qwen3-8B \
  --revision "$ENCODER_REVISION" \
  --served-model-name qwen3-8b \
  --runner pooling \
  --max-model-len 2048 \
  --host 127.0.0.1 \
  --port 8090
```

Keep the initial state length at 2048 for this first bounded qualification. Do not infer that this setting is sufficient for later production workloads.

## 4. Start CLM on loopback only

Terminal B:

```bash
source ~/.venvs/clm-shadow/bin/activate

export CLM_API_KEY="$(openssl rand -hex 32)"
printf '%s\n' "$CLM_API_KEY" > /tmp/clm-shadow-api-key
chmod 600 /tmp/clm-shadow-api-key

clm-serve \
  --host 127.0.0.1 \
  --port 8700 \
  --emb-url http://127.0.0.1:8090/v1/embeddings \
  --emb-model qwen3-8b \
  --max-tokens 2048 \
  --no-ui
```

The default CLM server host is not the desired qualification boundary here. Always pass `--host 127.0.0.1`.

Check health from another shell using the same key:

```bash
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

## 5. Record exact runtime identity

The shadow runner refuses an incomplete runtime receipt.

Create `/tmp/clm-runtime.json`:

```bash
source ~/.venvs/clm-shadow/bin/activate

CLM_GIT_REF="bb42c6c5bf914fd449bed2f6ca65be80602cb1f7"
ENCODER_REVISION="$(cat /tmp/clm-shadow-encoder-revision)"
CLM_PACKAGE_VERSION="$(python - <<'PY'
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
HEAD_PATH="${CLM_CKPT:-$HOME/.cache/clm/CLM_v0.1-8B.pt}"
HEAD_SHA256="$(sha256sum "$HEAD_PATH" | awk '{print $1}')"

python - <<PY
import json
from pathlib import Path

receipt = {
    "clm_git_ref": "$CLM_GIT_REF",
    "clm_package_version": "$CLM_PACKAGE_VERSION",
    "encoder_model": "Qwen/Qwen3-8B",
    "encoder_revision": "$ENCODER_REVISION",
    "head_sha256": "$HEAD_SHA256",
    "vllm_version": "$VLLM_VERSION",
    "device_name": "$DEVICE_NAME",
}
Path("/tmp/clm-runtime.json").write_text(
    json.dumps(receipt, indent=2) + "\n",
    encoding="utf-8",
)
PY

cat /tmp/clm-runtime.json
```

This receipt describes the observed runtime only:

```text
installed != qualified
runtime healthy != model useful
model useful != activated
```

## 6. Run the passive corpus

From a current Pantheon-Next checkout containing this lab:

```bash
export CLM_API_KEY="$(cat /tmp/clm-shadow-api-key)"

python implementation/labs/hermes_runtime_efficiency/clm_shadow_rank.py \
  implementation/labs/hermes_runtime_efficiency/clm_shadow_cases.json \
  --runtime-metadata /tmp/clm-runtime.json \
  --base-url http://127.0.0.1:8700 \
  --max-orderings 4 \
  --output /tmp/clm-shadow-report.json
```

Inspect only the observation summary first:

```bash
python - <<'PY'
import json
report = json.load(open("/tmp/clm-shadow-report.json"))
print(json.dumps(report["summary"], indent=2))
PY
```

The runner permutes candidate order. A case is `top_candidate_order_stable` only when the same candidate stays first across all tested orderings.

The initial useful signals are:

```text
expected_top1_all_orderings_rate
top_candidate_order_stable_rate
per-case rank probabilities
CLM latency header
transport elapsed time
```

Do not collapse them into one universal quality score.

## 7. Interpretation

First-pass interpretation:

```text
low expected-match rate
-> CLM is not useful for this decision family at the published head

high match but low order stability
-> reject as a routing primitive; ranking is too presentation-sensitive

high match + high order stability
-> candidate for a larger held-out shadow corpus only

good shadow corpus
!= permission to wire CLM into Hermes
```

Only after a larger held-out corpus should a separate experiment ask whether CLM can reduce a real Hermes selection cost.

## 8. Boundaries

Always preserve:

```text
CLM rank != Hermes decision
CLM rank != Pantheon authorization
fixture expected answer != professional truth
shadow observation != Evidence
runtime success != model qualification
model qualification != activation
```

The Pantheon effect owner / PEP remains unchanged and CLM receives no consequential credential.

## 9. Removal

The experiment is removable by deleting the CLM-specific lab files and qualification pin. No product module imports the shadow runner, no schema migration is introduced, and no runtime route depends on it.
