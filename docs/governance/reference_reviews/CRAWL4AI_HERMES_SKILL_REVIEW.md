# Crawl4AI Hermes Skill Review

Status: external reference / support review — documented non-implemented.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

This review qualifies `unclecode/crawl4ai` as a candidate implementation detail for a Hermes-side web extraction skill.

It does not install Crawl4AI.

It does not add a runtime, crawler service, Docker service, queue, scheduler, gateway, API endpoint, browser pool, MCP host, RAG importer, approval engine, evidence engine or memory engine.

It does not authorize any crawl. It only records the placement and provides a non-executable Hermes-compatible skill template under `templates/`.

## External project reviewed

```text
Repository: https://github.com/unclecode/crawl4ai
Documentation: https://docs.crawl4ai.com/
Reviewed posture: v0.9.x documentation and GitHub README visible on 2026-06-21
```

Crawl4AI is an open-source LLM-oriented web crawler and scraper. The public README describes it as a tool that turns web content into clean Markdown for RAG, agents and data pipelines. The v0.9 README also announces a secure-by-default Docker API server release and recent security-hardening work around Docker API vulnerabilities.

Relevant capabilities observed:

- public URL to Markdown extraction;
- `crwl` command-line interface;
- Python SDK via `AsyncWebCrawler`;
- configurable browser and crawler settings;
- CSS/XPath structured extraction;
- LLM-based structured extraction;
- dynamic page handling;
- deep crawling with explicit depth and page limits;
- fit Markdown / filtered Markdown output;
- proxy and SSL configuration;
- Docker API server, which is not admitted by this review.

## Placement decision

Accepted:

```text
Crawl4AI may be used as a Hermes-side adapter inside a bounded web extraction skill.
```

Refused:

```text
Crawl4AI as Pantheon doctrine.
Crawl4AI as Pantheon runtime.
Crawl4AI Docker API server as a default Pantheon service.
Crawl4AI output as validated truth.
Crawl4AI output as canonical memory.
Crawl4AI output as approved evidence.
Crawl4AI deep crawl as an unbounded ingestion mechanism.
Crawl4AI anti-bot / stealth / proxy escalation as a default agency behavior.
```

To verify:

```text
Installed version on Hermes.
Whether the local target has Playwright browsers installed.
Whether the `crwl` CLI is present in Hermes PATH.
Whether Crawl4AI respects the target site's access policy for the specific run.
Whether the output contains enough source anchors for Evidence Pack Candidate use.
Whether dynamic JavaScript output is stable enough for the dossier.
```

To arbitrate:

```text
Whether the skill should stay manual only or become dashboard-installable later.
Whether the Docker API server is ever admitted; default answer is no until explicitly reviewed.
Whether authenticated sessions are allowed for client/private portals; default answer is no.
Whether deep crawling can be allowed for public regulatory or product documentation with explicit page/depth caps.
```

## Why it is useful

The useful capability is not crawling for its own sake. The useful capability is controlled source preparation:

```text
URL / small URL set
-> bounded Hermes execution
-> Web Extraction Candidate
-> Evidence Pack Candidate
-> Pantheon review gate
```

This fits Pantheon because many professional questions require a current external source to be transformed into a reviewable corpus before any claim is made.

Examples:

- retrieve a public manufacturer page before comparing a product claim;
- turn an official documentation page into Markdown before a source review;
- extract a public changelog into a candidate evidence note;
- prepare a small regulatory or technical web corpus for human review.

The capability becomes consequential when the extracted content is used to support a professional assertion, decision, memory or external communication. At that point Pantheon governs the status, evidence and approval path.

## Boundary

Crawl4AI belongs to the execution runtime.

Pantheon may define:

- source-admission rules;
- allowed output statuses;
- risk triggers;
- Evidence Pack Candidate expectations;
- scope and memory constraints;
- approval gates for consequential use.

Hermes may execute:

- installation checks;
- single URL extraction;
- bounded multi-URL extraction;
- bounded deep crawl;
- Markdown / JSON candidate generation;
- quality report generation;
- Capability Gap reporting.

Pantheon must not execute:

- browser automation;
- crawling;
- scraping;
- Docker API calls;
- background crawl jobs;
- hidden ingestion;
- automatic RAG import;
- evidence approval;
- memory promotion.

## Candidate manifest sketch

This is a sketch only. The canonical executable schema, if created, belongs under `schemas/` and requires explicit approval.

```yaml
module_manifest:
  id: hermes.skills.web_extract.crawl4ai
  name: Crawl4AI web extraction skill
  version: candidate
  owner_layer: execution_runtime
  type: skill
  description: Bounded public-web extraction to Markdown or JSON candidates using Crawl4AI.
  status: candidate
  activation:
    state: candidate
    scope: task
  task_authorization:
    state: unauthorized
  interface:
    allowed_inputs:
      - task_contract
      - public_url
      - public_url_set
      - extraction_profile
      - depth_cap
      - page_cap
      - allowed_domain
    allowed_outputs:
      - web_extraction_candidate
      - evidence_pack_candidate
      - source_quality_report
      - capability_gap
    forbidden_outputs:
      - validated_truth
      - approved_evidence
      - canonical_memory
      - approval_event
      - external_delivery
      - unbounded_corpus
    envelope: task_contract_in / candidate_out / evidence_pack_out
  governance:
    consequential: true
    risk_level: high
    approval_behavior: review_required_for_consequential_use
    memory_behavior: candidate_only
    scope_behavior: task_or_dossier_bound
  dependencies:
    requires:
      - python
      - crawl4ai
      - playwright_browser_runtime
    optional:
      - local_llm_provider_for_llm_extraction
      - proxy_configuration
  composition:
    talks_only_via_envelope: true
  provenance:
    source: https://github.com/unclecode/crawl4ai
    reviewed_by: ChatGPT
```

## Output candidate shape

```json
{
  "candidate_type": "web_extraction_candidate",
  "adapter_id": "crawl4ai",
  "adapter_version": "unknown_or_reported",
  "task_contract_ref": "TC-...",
  "scope_id": "...",
  "source": {
    "url": "https://example.com/page",
    "retrieved_at": "2026-06-21T00:00:00+02:00",
    "access_mode": "public_web",
    "allowed_domain": "example.com",
    "crawl_depth": 0,
    "page_count": 1
  },
  "extraction": {
    "markdown": "...",
    "fit_markdown": "...",
    "structured_json": null,
    "links": [],
    "metadata": {}
  },
  "quality_flags": [
    "review_required"
  ],
  "limitations": [
    "web_content_may_change",
    "not_source_of_truth_without_review"
  ],
  "evidence_status": "source_candidate",
  "memory_status": "not_memory"
}
```

## Risk gates

The skill must stop or return a Capability Gap when any of these applies:

- no Task Contract or no stated scope;
- unclear target URL;
- private, authenticated or client portal content;
- request to bypass paywalls, anti-bot systems or access controls;
- request for unbounded crawling;
- missing domain cap for deep crawl;
- missing page cap for multi-page extraction;
- missing approval for consequential use;
- extraction intended to support a contractual, regulatory, legal, financial, planning, insurance or professional-liability claim without evidence review.

## Default run posture

Default to the safest useful mode:

```text
single public URL
same domain only
no authenticated session
no proxy unless explicitly configured
no stealth escalation
no deep crawl unless capped
fresh extraction preferred
candidate output only
```

## Relationship to existing doctrine

This review follows:

- `STATUS.md` for the non-runtime repository boundary;
- `CAPABILITY_PLACEMENT.md` for execution-runtime placement;
- `MODULAR_DOMAIN_REORIENTATION.md` for the module envelope;
- `DOMAIN_PACK_SPEC.md` for source admission and evidence expectations;
- `SKILL_LIFECYCLE.md` for declared / admitted / task-authorized separation;
- `PADDLEOCR_HERMES_SKILL_NOTE.md` as the closest document-extraction precedent.

If this review conflicts with those documents, those documents win.

## Boundary phrase

```text
Crawl4AI retrieves.
Hermes executes the bounded skill.
Pantheon governs the candidate.
The validated remains.
```
