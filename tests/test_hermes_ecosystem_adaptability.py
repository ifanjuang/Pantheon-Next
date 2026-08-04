from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE = ROOT / "docs" / "governance"
RUNTIME_REVIEW = GOVERNANCE / "HERMES_RUNTIME_SURFACE_REVIEW.md"
BINDINGS = GOVERNANCE / "HERMES_CAPABILITY_BINDINGS.md"
RETRIEVAL = GOVERNANCE / "HERMES_KNOWLEDGE_RETRIEVAL_BINDING.md"
LANGFUSE_RUNBOOK = ROOT / "operations" / "langfuse-hermes-first-test-runbook.md"
PROFILES = ROOT / "hermes" / "profiles"
PROFILE_README = PROFILES / "README.md"
PROFILE_CONSTITUTION = PROFILES / "PROFILE_CONSTITUTION.md"
BASE_SOUL_RULES = PROFILES / "_base" / "base-soul-rules.md"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_governed_hermes_profile_excludes_hidden_memory_and_rag() -> None:
    review = _text(RUNTIME_REVIEW)

    assert "profile: pantheon-governed" in review
    assert "external_memory_provider: off" in review
    assert "automatic_runtime_recall: forbidden" in review
    assert "automatic_runtime_memory_write: forbidden" in review
    assert "OpenWebUI_memory_injection: forbidden" in review
    assert "OpenWebUI_automatic_RAG: forbidden" in review
    assert "profile: assistant-personal" in review
    assert "external_memory_provider: optional_one_only" in review
    assert "provider selected != memory admitted" in review
    assert "memory recalled != truth" in review


def test_functional_profiles_inherit_one_governed_runtime_mode() -> None:
    readme = _text(PROFILE_README)
    constitution = _text(PROFILE_CONSTITUTION)
    base_rules = _text(BASE_SOUL_RULES)

    assert "functional profiles and runtime modes" in readme.lower()
    assert "must inherit the `pantheon-governed` runtime mode" in readme
    assert "`assistant-personal` is a separate non-governed runtime mode" in readme
    assert "external provider absent from tool list != external memory proven off" in readme

    assert "## Runtime profile modes" in constitution
    assert "runtime_mode: pantheon-governed" in constitution
    assert "task_contract_use: required" in constitution
    assert "runtime_mode: assistant-personal" in constitution
    assert "task_contract_use: forbidden" in constitution
    assert "They must not be duplicated into parallel `*-governed` profile families" in constitution
    assert "profile route reachable != profile safe" in constitution
    assert "external provider absent from tool list != external memory proven off" in constitution
    assert "runtime_mode: pantheon-governed" in constitution.split("## Kanban handoff convention", 1)[1]
    assert "A `pantheon-governed` task must not delegate into `assistant-personal`" in constitution
    assert "profile route fell back to default" in constitution

    assert "Any functional profile that receives a Pantheon Task Contract" in base_rules
    assert "external memory provider off" in base_rules
    assert "hidden OpenWebUI automatic RAG forbidden" in base_rules
    assert "must remain `not_qualified`" in base_rules


def test_binding_registry_prefers_replaceable_components_over_platform_sprawl() -> None:
    bindings = _text(BINDINGS)

    assert "`document_structural_analysis` | Docling" in bindings
    assert "`document_source_management` | Paperless-ngx when selected" in bindings
    assert "`observability` | Langfuse" in bindings
    assert "`knowledge_retrieval_pipeline` | Haystack" in bindings
    assert "Mem0 as an official Hermes provider candidate" in bindings
    assert "Mnemosyne as a third-party local-first plugin/MCP candidate" in bindings
    assert "preferred_binding: unbound" in bindings
    assert "forbidden_profiles: pantheon-governed" in bindings
    assert "refuse as Pantheon or default Hermes runtime" in bindings
    assert "watch/reference only by default" in bindings
    assert "standard Hermes distribution lock remains limited" in bindings


def test_retrieval_binding_reuses_libraries_without_adopting_new_runtimes() -> None:
    retrieval = _text(RETRIEVAL)

    assert "candidate_bindings: Haystack" in retrieval
    assert "watchlist_bindings: LlamaIndex, selected LangChain components" in retrieval
    assert (
        "rejected_default_bindings: Langflow runtime, LangGraph runtime, "
        "RAGFlow integrated platform"
    ) in retrieval
    assert "component reused != framework adopted" in retrieval
    assert "visual flow != governed workflow" in retrieval
    assert "human-in-the-loop node != Pantheon approval" in retrieval
    assert "RAGFlow is retained as an integrated external RAG product reference" in retrieval


def test_langfuse_runbook_requires_live_path_evidence_and_no_deleted_review() -> None:
    runbook = _text(LANGFUSE_RUNBOOK)

    assert "docs/governance/HERMES_RUNTIME_SURFACE_REVIEW.md" in runbook
    assert "docs/governance/HERMES_CAPABILITY_BINDINGS.md" in runbook
    assert "selected_trace_paths: api_server | runs | openwebui_chat" in runbook
    assert "plugin present != plugin loaded" in runbook
    assert "langfuse_hook_path_not_observed" in runbook
    assert "run_correlation_verified" in runbook
    assert "reference_reviews/LANGFUSE_HERMES_OBSERVABILITY_ADAPTER.md" not in runbook
    assert "reference_reviews/LANGFUSE_HERMES_INSTALLATION_PACKAGE_CANDIDATE.md" not in runbook


def test_runtime_review_does_not_change_distribution_or_authority() -> None:
    review = _text(RUNTIME_REVIEW)

    assert "standard_distribution_components_change_required: false" in review
    assert "installation_effect: none" in review
    assert "activation_effect: none" in review
    assert "task_authorization_effect: none" in review
    assert "trace recorded != Evidence" in review
    assert "runtime success != Evidence" in review
