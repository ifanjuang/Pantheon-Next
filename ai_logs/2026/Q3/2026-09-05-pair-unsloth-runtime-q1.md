# 2026-09-05 — PAIR + Unsloth runtime Q1 qualification planning

## Objective

Create a bounded qualification-only slice for NVIDIA Personal AI Router and Unsloth after reviewing current Pantheon `main`, current external qualification owners, the Ubuntu deployment candidate, Hermes runtime posture, and the current upstream PAIR/Unsloth source and releases.

No live lab was executed by this change.

## Verified Pantheon baseline

The branch was created from:

```text
initial main = fd39f1d377d57eb2dc03060c0f93b21763b745b7
```

Before merge-readiness corrections on 2026-09-05, `main` was revalidated and had advanced to:

```text
current main = a7080fa7997f47594332db3f3c7cece265beb3fb
```

The intervening commits include Hermes context-admission/read-budget work and an updated candidate Hermes distribution lock. They do not replace the PAIR/Unsloth qualification owners or introduce a parallel PAIR/Unsloth routing path. This branch must synchronize with that current `main` and preserve those newer Hermes changes; the Q1 planning slice still does not modify the Hermes distribution lock.

No parallel Pantheon PR for PAIR/Unsloth inference routing was found before the branch was created. The existing Hermes Desktop PR remains draft and is not treated as current `main` authority.

Existing owners reused:

- `implementation/qualification/external-pins.json` — sole current qualification target owner;
- `implementation/qualification/external-upstream-observations.json` — upstream observation owner;
- existing Hermes external-runtime/provider boundaries;
- existing Ubuntu deployment candidate;
- existing governance non-equivalences.

No new scheduler, provider router, runtime owner, resource type, persistence path, approval path, or Evidence owner is introduced.

## Upstream observations used

PAIR source/documentation review establishes a request-level router around supported engines and paired nodes. One request runs on one eligible node; PAIR does not pool VRAM or shard one request across machines. Its plaintext local-client ingress is loopback-only while paired peer ingress uses mTLS. Its current documented engine surface is Ollama and LM Studio.

PAIR's terminal interface is appropriate for the headless Linux node, but its own documentation says the TUI does not expose the per-request serving-node identity. The Q1 topology therefore uses PAIR Desktop on the Windows node as the Jobs / `Ran on` observation surface and `nvpair-tui` on Linux. Desktop and TUI are never launched together on one host.

PAIR's engine-lifecycle documentation also states that uninstalling a PAIR-installed engine leaves downloaded model files in the engine store. Q1 therefore tests this property explicitly rather than assuming it, while separately proving that the Pantheon-owned `/srv/ai/models/ollama` store is unchanged.

Unsloth source review establishes a local OpenAI-compatible serving surface and a one-line `unsloth run` server that generates an API key. The Q1 runbook resolves the selected source from the canonical Pantheon pin, uses an isolated source checkout/venv/Studio home/HF cache, and binds the endpoint to the host-side Docker bridge gateway needed by the current Hermes container.

That bind is now described precisely as bridge-scoped, not Hermes-only. A bridge gateway bind avoids wildcard/LAN exposure but does not prove that another compatible container cannot reach the endpoint.

The convenience `unsloth start hermes` path is deliberately excluded. The selected Hermes runtime already supports named custom OpenAI-compatible providers.

These are upstream observations, not live Pantheon runtime facts.

## Repository conflicts to observe rather than assume

The Ubuntu deployment candidate currently owns Ollama lifecycle and configures it on the standard Ollama port. PAIR may want that same port for its compatibility proxy and may relocate a PAIR-managed backend. Exact coexistence/ownership behavior must be executed before any deployment change.

Hermes currently runs in Docker Compose in the Ubuntu candidate and has `host.docker.internal:host-gateway`. Because PAIR's plaintext client gate is loopback-only, the current container-to-host path may be refused. That outcome remains `not_run`; Q1C probes from the real `pantheon-hermes` network namespace and records the actual HTTP/transport result before any workaround.

## Executable runbook convergence

The planning slice contains `docs/governance/PAIR_UNSLOTH_RUNTIME_Q1_RUNBOOK.md` with explicit:

- Linux and Windows preparation;
- qualification-pin export rather than duplicated current version literals;
- release-asset digest validation;
- isolated PAIR HOME/XDG state;
- bounded stop/restore of the current system Ollama only to free the PAIR proxy port;
- port/process/backend observations;
- model-store before/after manifests;
- Windows pairing, concurrent burst, failover and rejoin;
- peer-scoped firewall changes only when necessary and explicit rollback;
- current Hermes-container namespace probe without `network_mode: host` or relay;
- pinned Unsloth source checkout, isolated venv/home/cache and bridge-scoped Docker bind;
- capture of the effective Q1D runtime dependency closure after setup: Python packages, Torch/CUDA view, and actual llama.cpp/`llama-server` identity when discoverable;
- OpenAI model-list, streaming and structured-tool checks;
- a temporary Hermes profile using a named custom provider;
- normal Hermes approval policy for one harmless tool round trip, with no `--yolo`;
- deliberate invalid-provider-key check to detect silent fallback;
- governed-profile hash before/after;
- observation-row schema and independent candidate decision gates;
- stop conditions rather than workaround-by-default behavior.

An initially considered `pantheon-governed` profile clone was rejected during runbook review. Hermes profile cloning copies `.env` and configuration; Q1 does not need those secrets. The final runbook creates a fresh `pantheon-q1-unsloth` profile with no bundled skills and writes only the temporary provider/model/memory-off posture. `pantheon-governed` is read only through a metadata hash before/after and must not change.

The Unsloth source ref is not treated as a complete runtime closure. `uv --torch-backend=auto` and Studio setup can resolve runtime dependencies dynamically, so Q1 records the environment actually used. An unidentified dynamically resolved component remains `unresolved`; it is not inferred from the source pin and does not trigger speculative new canonical pins in this planning slice.

## Governance CI corrections

The first CI pass exposed two Q1-owned defects:

1. the two new `candidate` governance documents were not indexed;
2. a contract test matched a narrower literal `Do not use --yolo` sentence than the runbook's actual `Do not use Hermes --yolo` wording.

The corrections are deliberately minimal:

- both PAIR/Unsloth candidate documents are indexed in `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md` without promotion or new authority;
- the test now checks the existing stable prohibition sentence rather than weakening the prohibition;
- the fixture revision advances to 2 for the runtime-closure and bridge-scope semantics.

The unrelated LiveSync security-seed workflow timeout observed on the first PR head is not classified as a Q1 defect merely because it ran on the same pull request; its focused contract passed and its live Obsidian session timed out independently. A later rerun/current-head result decides whether it remains an external integration flake or a repository-wide blocker.

## Q1 stages

1. isolated PAIR on the always-on Linux RTX 4080 node;
2. Linux + Windows RTX 4090 PAIR cluster with the same bounded test model on both nodes;
3. current Hermes container networking path against the local PAIR proxy;
4. isolated Unsloth as a named custom OpenAI-compatible provider of the existing Hermes runtime, without `unsloth start hermes`;
5. independent candidate classification from sanitized observation rows with no activation.

The machine-readable fixture remains `live_executed = false` and every stage `result = not_run`.

## Observation structure

Every required check must eventually produce a sanitized row containing:

```text
check_id
stage_id
host
command_or_action
expected_observation
actual_observation
status
artifact_ref
started_at
ended_at
notes
```

Secrets, pairing PINs, prompt bodies and generated response bodies are excluded.

## Authority ceiling

```text
upstream observed != pin selected
pin selected != runtime observed
runtime observed != runtime qualified
runtime qualified != runtime activated
PAIR routing != Pantheon authorization
Unsloth provider configured != provider authorized
runtime success != task authorization
runtime success != Evidence
```

## Files

```text
implementation/qualification/external-pins.json
implementation/qualification/external-upstream-observations.json
docs/governance/PAIR_UNSLOTH_RUNTIME_QUALIFICATION.md
docs/governance/PAIR_UNSLOTH_RUNTIME_Q1_RUNBOOK.md
docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
tests/fixtures/pair_unsloth_runtime_q1.json
tests/test_pair_unsloth_runtime_q1_contract.py
ai_logs/2026/Q3/2026-09-05-pair-unsloth-runtime-q1.md
```

## Explicit non-changes

- no `deployment/ubuntu/release.env` change;
- no `deployment/ubuntu/install-node` change;
- no production Compose change;
- no Hermes distribution lock change;
- no PAIR installation executed;
- no Unsloth installation executed;
- no runtime activation;
- no task authorization;
- no Evidence admission.
