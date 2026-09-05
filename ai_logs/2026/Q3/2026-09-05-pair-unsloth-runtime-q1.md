# 2026-09-05 — PAIR + Unsloth runtime Q1 qualification planning

## Objective

Create a bounded qualification-only slice for NVIDIA Personal AI Router and Unsloth after reviewing current Pantheon `main`, current external qualification owners, the Ubuntu deployment candidate, Hermes runtime posture, and the current upstream PAIR/Unsloth source and releases.

No live lab was executed by this change.

## Verified Pantheon baseline

```text
main = fd39f1d377d57eb2dc03060c0f93b21763b745b7
```

No open Pantheon PR matching PAIR, Unsloth, Hermes inference routing, or an external physical inference router was found before the branch was created.

Existing owners reused:

- `implementation/qualification/external-pins.json` — sole current qualification target owner;
- `implementation/qualification/external-upstream-observations.json` — upstream observation owner;
- existing Hermes external-runtime/provider boundaries;
- existing Ubuntu deployment candidate;
- existing governance non-equivalences.

No new scheduler, provider router, runtime owner, resource type, persistence path, approval path, or Evidence owner is introduced.

## Upstream observations used

PAIR source review establishes a request-level router around supported engines and paired nodes. One request runs on one eligible node; PAIR does not pool VRAM or shard a request across machines. Its plaintext local-client ingress is loopback-only while paired peer ingress uses mTLS. Its current documented engine surface is Ollama and LM Studio.

Unsloth source review establishes a current release with a local OpenAI-compatible serving surface. Its convenience `unsloth start hermes` path may resolve/install Hermes and writes a session-scoped Hermes configuration. Pantheon does not need that second Hermes configuration for the question under test because the existing Hermes runtime already supports custom OpenAI-compatible providers.

These are upstream observations, not live Pantheon runtime facts.

## Repository conflicts to observe rather than assume

The Ubuntu deployment candidate currently owns Ollama lifecycle and configures it on the standard Ollama port. PAIR may want that same port for its compatibility proxy and may relocate a PAIR-managed backend. Exact coexistence/ownership behavior must be executed before any deployment change.

Hermes currently runs in Docker Compose in the Ubuntu candidate. Because PAIR's plaintext client gate is loopback-only, the current container-to-host path may be refused. That outcome is deliberately left `not_run`; the qualification contract forbids pre-recording the expected HTTP status from source review alone.

## Q1 stages

1. isolated PAIR on the always-on Linux GPU node;
2. Linux + Windows PAIR cluster with the same bounded test model on both nodes;
3. current Hermes container networking path against the local PAIR proxy;
4. Unsloth as a custom OpenAI-compatible provider of the existing Hermes candidate, without `unsloth start hermes`;
5. independent candidate classification with no activation.

The machine-readable fixture starts with `live_executed = false` and every stage `result = not_run`.

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
tests/fixtures/pair_unsloth_runtime_q1.json
tests/test_pair_unsloth_runtime_q1_contract.py
ai_logs/2026/Q3/2026-09-05-pair-unsloth-runtime-q1.md
```

## Explicit non-changes

- no `deployment/ubuntu/release.env` change;
- no `deployment/ubuntu/install-node` change;
- no Hermes distribution lock change;
- no PAIR installation;
- no Unsloth installation;
- no runtime activation;
- no task authorization;
- no Evidence admission.
