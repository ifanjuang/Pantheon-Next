# Hermes local runtime — observed status

This note records the observed local deployment state on 2026-09-10. It is an
operational snapshot, not a portable architecture requirement.

## Working path

The following path is currently working:

```text
Telegram / WhatsApp / Discord
        -> Hermes gateway
        -> custom:ollama@ifja
        -> NVPair proxy http://127.0.0.1:11435/v1
        -> qwen3.5:9b
```

Observed checks:

- `pantheon-hermes` is running.
- the Hermes status endpoint reports the gateway, dashboard and storage as
  healthy;
- Telegram, WhatsApp, Discord and the API server report `connected`;
- an actual Telegram request produced a model response after the model change;
- Hindsight is connected and recalls memories, although retain visibility can
  time out after 30 seconds and a recall can miss the immediately preceding
  turn;
- the local NVPair proxy is listening on port `11435`;
- the NVPair catalogue currently advertises `qwen3.5:9b`, `gemma3:12b` and
  `gpt-oss:20b`.

## Model correction applied

Hermes previously selected `qwen3.8:27b` as its primary model. NVPair returned
HTTP 502 with `no available node advertises the requested model`, so the chat
gateway accepted messages but could not generate a response.

The persistent Hermes configuration now selects:

```yaml
model:
  default: qwen3.5:9b
  provider: custom:ollama@ifja
  context_length: 65536
```

The pre-change configuration is retained on the host as:

```text
/srv/pantheon/hermes/config.yaml.bak-20260909-model-fallback
```

This restores service but is not yet a true inter-model fallback. NVPair can
route a requested model to another node that advertises that same model. It
does not translate a request for an unavailable `qwen3.8:27b` into a request for
`qwen3.5:9b`.

## PC00 and failover limitation

PC00 is registered as an NVPair cluster member at `192.168.50.14`. It was
reachable during the final check, but it still did not advertise a model in the
NVPair model catalogue. Direct plaintext access to its Ollama port is correctly
refused; cluster peers must use the NVPair mTLS ingress.

Keeping PC00 usable for Hermes requires all of the following:

1. firmware Wake-on-LAN enabled and wake packets forwarded on the local network;
2. NVPair and Ollama started automatically when PC00 boots;
3. PC00 sleep inhibited while an inference or conversation lease is active;
4. an idle grace period after the last request before sleep is allowed;
5. a Hermes-side inter-model fallback for the case where PC00 cannot wake or
   does not advertise the requested model.

Until those five conditions are implemented and tested, `qwen3.5:9b` on the
always-available node is the operational primary model.

## Marker state

`pantheon-marker-api.service` is enabled for `multi-user.target` and starts with
Linux. It was active during the 2026-09-10 check and listened on
`127.0.0.1:8001`.

The Marker API process and the Surya model have different lifecycles:

- the Marker API remains active after boot;
- the Surya/vLLM container is started on demand for OCR;
- no `surya-vllm` container was running during the check;
- the intended idle policy releases the GPU model after ten minutes, so a new
  OCR conversion can have a cold-start delay.

## Known behavioural limits

- A Telegram answer about the Floquet project returned a generic answer instead
  of consulting the IFJA vaults.
- The answer exposed a `Reasoning` block to the chat surface.
- `ifja-vault-search` is installed and present in Hermes' loaded skill index,
  but installation/discovery alone does not prove that the model invoked it for
  a particular turn.
- Hindsight retain visibility timeouts can make the latest conversational turn
  temporarily unavailable to recall.

These are separate from Telegram connectivity and should be tested as retrieval
and presentation issues.

The follow-up inspection found six Floquet documents already indexed in
`IFJA_AFFAIRES`, including the project page and its CERFA extraction. The
authoritative project page currently records permit number
`PC 76095 26 00011`. A broad semantic recall also returned unrelated permit
numbers, which confirms that Hermes must resolve the project, open the exact
document and avoid answering from an unverified recall snippet.

Version `0.6.0` of `ifja-vault-search` adds a bounded second lookup in the
external `hermes` Hindsight bank for recent projects. Facts found only there are
labelled as recent conversational memory until confirmed in `IFJA_AFFAIRES`.

## IFJA skill added to Hermes

The IFJA-specific skill added by this deployment is
[`ifja-vault-search`](../../implementation/hermes/skills/ifja-vault-search/SKILL.md).
Its complete source consists of:

- `SKILL.md` — routing, project resolution, query limits and answer rules;
- `agents/openai.yaml` — agent metadata;
- `references/vault-map.md` — source and bank routing;
- `references/pdf-plans.md` — PDF and plan verification rules;
- `scripts/compact_hindsight_result.py` — bounded compaction of large results;
- `scripts/list_project_files.py` — project file inventory helper.

## Complete installed skill inventory

The following `SKILL.md` files were present in the live Hermes volume during the
check. Presence does not guarantee that every optional dependency or external
account is configured.

### Apple

- `apple-notes`
- `apple-reminders`
- `findmy`
- `imessage`

### Autonomous agents

- `claude-code`
- `codex`
- `computer-use`
- `hermes-agent`
- `merge-reconciler`
- `opencode`

### Creative

- `architecture-diagram`
- `ascii-art`
- `ascii-video`
- `baoyu-infographic`
- `claude-design`
- `comfyui`
- `design-md`
- `excalidraw`
- `humanizer`
- `manim-video`
- `p5js`
- `popular-web-designs`
- `pretext`
- `sketch`
- `songwriting-and-ai-music`
- `touchdesigner-mcp`

### DevOps, email and GitHub

- `sdlc-review`
- `email-inbox-triage`
- `himalaya`
- `github-auth`
- `github-code-review`
- `github-issue-to-pr`
- `github-issues`
- `github-pr-workflow`
- `github-repo-management`

### IFJA

- `ifja-vault-search`

### Media and MLOps

- `gif-search`
- `songsee`
- `youtube-content`
- `evaluating-llms-harness`
- `weights-and-biases`
- `huggingface-hub`
- `llama-cpp`
- `serving-llms-vllm`

### Notes and productivity

- `obsidian`
- `airtable`
- `box`
- `document-to-action-items`
- `docx`
- `google-workspace`
- `maps`
- `meeting-action-items`
- `nano-pdf`
- `notion`
- `ocr-and-documents`
- `pdf-to-doc-conversion`
- `pdf`
- `powerpoint`
- `product-price-monitor`
- `session-librarian`
- `teams-meeting-pipeline`
- `weekly-review-planning`
- `xlsx`

### Research

- `arxiv`
- `blogwatcher`
- `competitor-news-monitor`
- `grounded-citations`
- `hindsight-memory-banks`
- `llm-wiki`
- `research-paper-writing`

### Smart home and social media

- `openhue`
- `xurl`

### Software development

- `codebase-inspection`
- `dogfood`
- `github`
- `hermes-agent-skill-authoring`
- `inspecting-hermes-desktop-dom`
- `node-inspect-debugger`
- `plan`
- `python-debugpy`
- `requesting-code-review`
- `simplify-code`
- `spike`
- `systematic-debugging`
- `test-driven-development`

### Web

- `blocked-page-recovery`
