# Crawl4AI — Hermes Adapter Placement Review

Status: external reference / support review — candidate only.

Date: 2026-06-21

External source reviewed:

```text
https://github.com/unclecode/crawl4ai
https://docs.crawl4ai.com/
```

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## What it is

Crawl4AI is an open-source Python crawler and scraper focused on producing LLM-ready Markdown, structured extraction and browser-controlled crawling for RAG, agents and data pipelines.

It can run as a Python SDK, CLI or self-hosted Docker API server.

## Initial qualification

Accepted:

```text
as a Hermes-side document / web extraction adapter candidate;
as a source-admission and Markdown-preparation tool candidate;
as a producer of Source Extraction Candidates, Markdown Candidates, Link Map Candidates and Evidence Pack Candidates;
as useful for public web, documentation, standards, product docs and known authorized sources.
```

Refused:

```text
as Pantheon runtime;
as Pantheon crawler;
as source of truth;
as Evidence Pack by itself;
as memory engine;
as approval engine;
as unrestricted browser automation;
as externally exposed Docker API without a separate operations/security review;
as automatic ingestion into canonical RAG or Registre Probatoire.
```

To verify:

```text
SDK safety in the Hermes sandbox;
version pinning and reproducibility;
network egress controls;
robots/legal/source authorization policy;
artifact retention and deletion;
Markdown fidelity on architecture/legal/regulatory documents;
source metadata preservation;
Docker API hardening if ever used;
SSRF and local-network protections;
whether Crawl4AI should be wrapped by a narrower IFJ-specific extraction adapter.
```

To arbitrate:

```text
whether first use is SDK-only or Docker API behind local loopback;
whether deep crawling is allowed in phase 1;
whether login/session/cookie crawling is prohibited entirely or allowed with explicit per-source approval;
whether outputs may enter the architecture knowledge registry as raw candidates.
```

## Placement

```yaml
module_manifest_candidate:
  id: crawl4ai-web-extraction-adapter
  owner_layer: execution_runtime
  type: tool
  status: candidate
  activation:
    state: sandbox_enabled_candidate
    scope: task
  task_authorization:
    state: unauthorized_by_default
  interface:
    allowed_inputs:
      - authorized_url
      - authorized_url_list
      - crawl_scope
      - extraction_schema
      - source_policy
    allowed_outputs:
      - source_extraction_candidate
      - markdown_candidate
      - link_map_candidate
      - evidence_pack_candidate
      - artifact_reference
      - capability_gap_signal
    forbidden_outputs:
      - truth_final
      - approval_final
      - canonical_memory
      - register_entry
      - unrestricted_crawl
      - credential_capture
      - external_publication
  governance:
    consequential: true
    risk_level: high
    approval_behavior: read_only_or_candidate_only
    memory_behavior: never_canonical
    scope_behavior: strict_source_scope
```

## Why it is useful

Crawl4AI is materially useful for Pantheon Next because document intelligence, source admission and architecture knowledge ingestion all need a reliable way to turn web pages and documentation into clean, reviewable Markdown without pretending retrieval is evidence.

Good uses:

```text
fetch a public regulation page into Markdown Candidate;
extract a public software documentation page before adapter review;
build a link map of an authorized documentation site;
prepare Source Extraction Candidates for a later Evidence Pack;
compare current docs against a previously reviewed excerpt.
```

Bad uses:

```text
crawl arbitrary websites without scope;
use crawler success as proof;
ingest into memory automatically;
follow login sessions without approval;
expose a crawler API to the internet;
let JavaScript hooks execute arbitrary code from requests;
allow local-network or metadata-service targets;
let a source become authoritative merely because it was scraped cleanly.
```

## Minimum Pantheon handoff shape

Before Hermes invokes Crawl4AI, the handoff should contain:

```yaml
governed_execution_handoff:
  linked_task_contract:
  scope:
  target_runtime: Hermes
  requested_effect: read_only
  action_family: web_extraction
  target:
    kind: url_set
    refs:
  source_policy:
    allowed_domains:
    forbidden_domains:
    robots_or_legal_note:
    login_or_cookie_use: prohibited_by_default
  forbidden_effects:
    - external_send
    - canonical_memory
    - approval_final
    - unrestricted_crawl
    - credential_capture
    - local_network_access
  expected_result_candidate: source_extraction_candidate
  expected_evidence_pack_candidate: true
  outcome_observation_expected: true
  trace_refs:
```

If any of these fields are missing, Hermes should return a `capability_gap_signal`, not crawl anyway.

## Security posture

Default posture for first admission:

```text
SDK only.
Read-only.
Public or explicitly authorized URLs only.
No login session.
No cookies.
No arbitrary hooks from user input.
No internal-network targets.
No file:// targets.
No automatic memory write.
No automatic vector-store ingestion.
No Docker API exposure.
```

The Docker API server is not rejected forever, but it belongs behind a separate operations/security review because the project history includes critical Docker API issues and a later secure-by-default hardening posture.

## Candidate phase sequence

```text
Phase 0 — reference review only, no install.
Phase 1 — Hermes sandbox SDK test on one public documentation URL.
Phase 2 — output contract: Markdown Candidate + source metadata + trace refs.
Phase 3 — evidence-chain test: can the output support Evidence Pack Candidate assembly without becoming proof?
Phase 4 — optional Docker API review, local loopback only, token required.
```

## Boundary note

Crawl4AI should not be added to Pantheon Next as a dependency. If used, it belongs in Hermes or another execution-runtime repository. Pantheon keeps only the review, manifest candidate, handoff expectations and forbidden collapses.
