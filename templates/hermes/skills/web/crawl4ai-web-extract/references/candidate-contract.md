# Crawl4AI Web Extraction Candidate Contract

Status: template reference — non-executable.

This reference defines the expected shape of a Crawl4AI-backed Hermes skill result.

It is not a schema.
It is not a validation rule.
It is not an Evidence Pack.
It is not a Registre Probatoire entry.

## Result Candidate

```json
{
  "candidate_type": "web_extraction_candidate",
  "adapter_id": "crawl4ai",
  "adapter_version": "unknown_or_reported",
  "skill_id": "hermes.skills.web_extract.crawl4ai",
  "task_contract_ref": "TC-...",
  "scope_id": "SCOPE-...",
  "requested_effect": "read_only",
  "source": {
    "url": "https://example.com/page",
    "retrieved_at": "2026-06-21T00:00:00Z",
    "access_mode": "public_web",
    "allowed_domain": "example.com",
    "crawl_depth": 0,
    "page_count": 1,
    "page_cap": 1,
    "include_external": false
  },
  "execution": {
    "mode": "cli_or_python_sdk",
    "command_summary": "crwl <url> -o markdown --bypass-cache",
    "cache_mode": "bypass",
    "proxy_used": false,
    "authenticated_session_used": false,
    "llm_extraction_used": false
  },
  "extraction": {
    "markdown": "...",
    "fit_markdown": null,
    "structured_json": null,
    "links": [],
    "metadata": {}
  },
  "quality": {
    "success": true,
    "error_message": null,
    "flags": ["review_required"],
    "limitations": [
      "web_content_may_change",
      "not_source_of_truth_without_review"
    ],
    "review_recommendation": "human_source_review_required_before_consequential_use"
  },
  "governance_status": {
    "evidence_status": "source_candidate",
    "memory_status": "not_memory",
    "approval_status": "not_approved",
    "truth_status": "not_validated"
  }
}
```

## Evidence Pack Candidate

```json
{
  "candidate_type": "evidence_pack_candidate",
  "produced_from": "web_extraction_candidate",
  "scope_id": "SCOPE-...",
  "claims_supported": [],
  "sources": [
    {
      "url": "https://example.com/page",
      "retrieved_at": "2026-06-21T00:00:00Z",
      "status": "source_candidate",
      "authority_class": "unknown_until_review",
      "freshness": "retrieved_now_but_content_may_change"
    }
  ],
  "limitations": [
    "retrieval_success_is_not_evidence_approval",
    "markdown_conversion_may_drop_layout_or_dynamic_elements",
    "source_authority_must_be_reviewed_separately"
  ],
  "required_review": [
    "source_authority",
    "content_completeness",
    "claim_mapping",
    "date_version_validity",
    "scope_fit"
  ],
  "governance_status": "candidate"
}
```

## Capability Gap

```json
{
  "candidate_type": "capability_gap",
  "missing": "dependency_or_scope_or_permission",
  "needed_for": "bounded_web_extraction",
  "blocked_effect": "crawl_not_run",
  "consequence_if_ignored": "unauthorized_or_unreviewable_source_use",
  "safe_fallback": "manual_source_review_or_request_scope_confirmation",
  "required_human_or_admin_action": "install_dependency_or_validate_scope_or approve_task_contract",
  "status": "blocked"
}
```

## Status rule

```text
runtime_task_status = success
```

never implies:

```text
governance_result_status = approved
truth_status = validated
memory_status = canonical
```

The correct default is:

```text
governance_result_status = candidate
review_required = true
```
