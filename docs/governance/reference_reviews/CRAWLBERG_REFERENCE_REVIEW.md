# Crawlberg Reference Review — Web Evidence Intake Adapter Pattern

Status: candidate external reference / to verify — adapter inspiration only.

Repo state: documented non-implemented.

Reviewed: 2026-07-05.

Source reviewed: `https://github.com/xberg-io/crawlberg`

This document records a distillation of `xberg-io/crawlberg` for Pantheon Next. It does not add a dependency, runtime, crawler, MCP server, Hermes skill, OpenWebUI plugin, connector gateway, scheduler, queue, WAF bypass, browser automation service, knowledge-base mutator, approval engine or memory engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Review question

```text
Can a Crawlberg-like component help Pantheon Next ingest public web material without collapsing retrieval, evidence, approval or memory?
```

Answer:

```text
Yes, as an execution-runtime adapter pattern.
No, as a Pantheon dependency or governance-core component.
```

## What Crawlberg appears to provide

Crawlberg presents itself as a Rust crawling substrate with language bindings and operational surfaces. The useful signals for Pantheon are:

- web crawling and scraping;
- HTML to Markdown conversion;
- structured extraction of text, metadata, links, images, headings, JSON-LD, Open Graph and response headers;
- robots and sitemap handling;
- per-domain throttling;
- configurable depth, page limits and concurrency;
- optional headless-browser fallback for JavaScript-heavy pages;
- SSRF-safe default posture against loopback, private, link-local and cloud-metadata targets;
- batch and streaming crawl events;
- REST and MCP surfaces;
- OpenTelemetry traces and metrics;
- antibot and WAF-detection surfaces, including browser escalation and optional caller-owned bypass provider hooks.

These are execution capabilities. They do not create a proof, source truth, professional validation, user approval or canonical memory.

## Pantheon distillation

A web crawl should enter Pantheon as a source-intake candidate, not as truth.

```text
URL / sitemap / public web perimeter
→ Web Source Intake Candidate
→ Source Reference Candidate
→ Retrieved Web Knowledge
→ Context Sufficiency Check
→ Evidence Candidate
→ Evidence Pack Candidate
→ Output Candidate
→ User / Zeus Gate
```

Forbidden shortcuts:

```text
fetched -> trusted
converted to Markdown -> evidence
site metadata -> authority
crawl success -> proof
browser-rendered -> reliable
MCP call succeeded -> task approved
trace exists -> Evidence Pack
retrieved webpage -> memory
```

## Placement

### Exposure surface

The exposure surface may show:

- target URL or domain;
- allowed source perimeter;
- crawl depth and page limit;
- public/authenticated/private source status;
- robots status;
- result status;
- source freshness warning;
- Evidence Candidate cards;
- Capability Gap cards;
- User Decision Gates.

It must not become the crawler, source authority, approval authority, memory authority or hidden connector manager.

### Execution runtime

Hermes or another execution runtime may execute a Crawlberg-like adapter under Task Contract.

Permitted runtime actions, if scoped:

- fetch public pages;
- parse sitemaps;
- respect robots policy;
- throttle requests;
- convert HTML to Markdown;
- extract metadata and links;
- preserve source references;
- report failures, redirects, blocked pages and render mode;
- produce Result Candidates and Evidence Pack Candidates.

The runtime must not approve sources, promote knowledge, write canonical memory, create a Registre Probatoire entry, bypass source policy, or convert a crawl result into professional validation.

### Pantheon

Pantheon governs:

- whether web intake is allowed for the task;
- which domains and paths are in scope;
- whether authentication is allowed;
- whether browser rendering is allowed;
- whether robots and rate-limit behavior are acceptable;
- which extracted claims may become Evidence Candidates;
- freshness expectations;
- conflict handling;
- approval and memory gates.

Pantheon does not crawl, schedule crawls, rotate proxies, execute browser sessions, run an MCP crawler, or own crawl state.

## Candidate Task Contract shape

Specification only. Not an executable schema.

```text
web_evidence_intake_task:
  task_id:
  objective:
  source_scope:
    target_urls:
    allowed_domains:
    allowed_paths:
    forbidden_domains:
    forbidden_paths:
    max_depth:
    max_pages:
    max_duration:
  access_policy:
    public_only: true
    authentication_allowed: false by default
    robots_policy: respect_required
    rate_limit_policy:
    browser_rendering: disabled | allowed_if_needed | requires_approval
    antibot_bypass: forbidden by default
    private_network_access: forbidden
  evidence_expectation:
    claims_expected:
    freshness_required:
    source_authority_class_expected:
    contradiction_policy:
  output_policy:
    allowed_outputs:
      - result_candidate
      - evidence_pack_candidate
      - capability_gap
    forbidden_outputs:
      - truth_status_final
      - approval
      - canonical_memory
      - external_action
  trace_expectation:
    trace_refs_required: true
```

## Candidate result shape

Specification only. Not an executable schema.

```text
web_result_candidate:
  job_id:
  requested_scope:
  actual_scope:
  fetched_at:
  runtime_tool:
  runtime_version:
  pages:
    - url:
      final_url:
      status_code:
      title:
      source_hash:
      crawl_depth:
      robots_status:
      render_mode:
      markdown_ref:
      extracted_metadata:
      extracted_links:
      extracted_images:
      response_headers_summary:
      limitations:
  blocked_or_failed:
    - url:
      reason:
      safe_next_action:
  evidence_pack_candidate:
    candidate_claims:
    source_refs:
    freshness_flags:
    contradictions:
    unsupported_claims:
    review_required:
  trace_refs:
  governance_result_status: candidate | to_verify | blocked
```

## Gates

### Entry gate

Before dispatch:

- target source is named;
- domain is allowed;
- depth and page limits are bounded;
- private network targets are refused;
- robots policy is explicit;
- authentication is off unless approved;
- browser mode is off or explicitly justified;
- expected claims and evidence expectations are named.

### Evidence gate

After return:

- source references are localizable;
- extracted claims are separated from page content;
- freshness and authority class are visible;
- contradictions are surfaced;
- insufficient evidence remains first-class;
- trace references do not replace Evidence Pack content.

### Memory gate

A crawled page, Markdown extract or web result does not enter memory by default. At most, it may become a Register Candidate if the user validates scope, source status, evidence link and reuse boundary.

## Antibot, browser and bypass boundary

Crawlberg exposes WAF detection, browser escalation and bypass-provider hooks. Pantheon should classify these as sensitive execution surfaces.

Allowed by default:

- public HTTP fetch;
- sitemap reading;
- robots-aware crawling;
- conservative throttling;
- browser rendering only when the Task Contract allows it for public JavaScript-heavy pages.

Requires explicit approval:

- authenticated session use;
- cookie or bearer-token use;
- headless browser always-on mode;
- deep crawl beyond the initial contract;
- paid escalation or cost-bearing provider;
- recurring crawl.

Refused by default:

- bypass of access controls;
- stealth mode to defeat a site's expressed refusal;
- proxy rotation to force access;
- crawling private networks, local services or cloud metadata;
- automatic ingestion into canonical knowledge;
- using a WAF bypass result as stronger evidence than an ordinary source.

Governance rule:

```text
A blocked page is often a boundary signal, not an engineering problem to overcome.
```

## Observability boundary

OpenTelemetry traces and crawl metrics are useful for audit support:

- fetched pages;
- blocked pages;
- robots refusals;
- WAF detections;
- browser escalations;
- timeouts;
- result counts;
- trace correlation.

They remain runtime observation. They are not Evidence Pack by themselves and do not prove professional claims.

## Card-stack projection

A Crawlberg-like adapter maps well to the card grammar:

- Web Source Card — target URL, domain, authority class, freshness.
- Crawl Job Card — scope, depth, limits, render mode, status.
- Evidence Candidate Card — extracted claim, source reference, confidence limits.
- Conflict Card — contradictory pages, stale source, unsupported claim.
- Capability Gap Card — blocked page, robots refusal, authentication missing, browser forbidden.
- Zeus Gate Card — decide whether to accept, reject, request more evidence, or stop.

Cards display status. They do not execute the crawl.

## Decision

Accepted:

- Crawlberg as inspiration for a Web Evidence Intake adapter pattern.
- Its separation between substrate and operational productization is compatible with Pantheon's kernel / adapter split.
- HTML to Markdown, metadata extraction, source refs, streaming events and observability are useful candidate signals.

Refused:

- adding Crawlberg as a Pantheon dependency;
- making Pantheon a crawler or MCP tool host;
- treating crawl success as proof;
- allowing automatic knowledge or memory mutation;
- normalizing stealth or bypass behavior inside governance doctrine.

To verify:

- whether a Hermes-side skill should wrap Crawlberg or another crawler;
- exact security posture for SSRF, private network refusal and credential handling;
- whether MCP exposure is useful or too broad for the first adapter;
- how trace references should be displayed in the cockpit;
- whether recurring web watch belongs in a future external runtime task pattern.

To arbitrate:

- whether architecture-domain source packs may include allowlisted public web sources such as municipal urbanism pages;
- whether authenticated portals can ever be crawled under user-approved session scope;
- whether browser rendering should be allowed for official public sources that require JavaScript;
- whether web intake can seed Knowledge Candidates, or only Evidence Candidates, in the first version.

## Final rule

```text
The web can provide candidate material.
The crawl can preserve provenance.
The trace can support audit.
Only governed evidence and approval can support delivery.
Only validated, scoped material may remain.
```
