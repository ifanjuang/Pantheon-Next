from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE = ROOT / "docs" / "governance"
RUNTIME_REVIEW = GOVERNANCE / "HERMES_RUNTIME_SURFACE_REVIEW.md"
RUNTIME_GOVERNANCE = GOVERNANCE / "HERMES_RUNTIME_GOVERNANCE.md"
BINDINGS = GOVERNANCE / "HERMES_CAPABILITY_BINDINGS.md"
RETRIEVAL = GOVERNANCE / "HERMES_KNOWLEDGE_RETRIEVAL_BINDING.md"
LANGFUSE_RUNBOOK = ROOT / "operations" / "langfuse-hermes-first-test-runbook.md"
PROFILES = ROOT / "hermes" / "profiles"
PROFILE_README = PROFILES / "README.md"
PROFILE_CONSTITUTION = PROFILES / "PROFILE_CONSTITUTION.md"
BASE_SOUL_RULES = PROFILES / "_base" / "base-soul-rules.md"
EXTERNAL_PINS = ROOT / "implementation" / "qualification" / "external-pins.json"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _external_pin_version(pin_id: str) -> str:
    data = json.loads(_text(EXTERNAL_PINS))
    return data["pins"][pin_id]["version"]


def test_runtime_review_keeps_governed_profile_and_release_sensitive_constraints() -> None:
    review = _text(RUNTIME_REVIEW)

    assert "profile: pantheon-governed" in review
    assert "external_memory_provider: off" in review
    assert "built_in_memory_injection: off" in review
    assert "built_in_user_profile_injection: off" in review
    assert "memory_tool: off" in review
    assert "session_memory_key: forbidden" in review
    assert "real_browser_profile: disabled unless separately qualified" in review
    assert "browser_extension_control: disabled unless separately qualified" in review
    assert "remote_admin_update_surface: outside governed task path" in review
    assert "terminal_environment_backend: exact observed backend required" in review
    assert "existing runtime observer already records route/tool/memory posture" in review
    assert "profile: assistant-personal" not in review
    assert "OpenWebUI_memory_injection" not in review
    assert "OpenWebUI_automatic_RAG" not in review


def test_functional_profiles_inherit_one_governed_runtime_mode() -> None:
    readme = _text(PROFILE_README)
    constitution = _text(PROFILE_CONSTITUTION)
    base_rules = _text(BASE_SOUL_RULES)

    assert "functional profiles and runtime modes" in readme.lower()
    assert "must inherit the `pantheon-governed` runtime mode" in readme
    assert "built-in MEMORY.md injection: off" in readme
    assert "built-in USER.md profile injection: off" in readme
    assert "memory tool: off" in readme
    assert "X-Hermes-Session-Key: not sent" in readme
    assert "`assistant-personal` is a separate non-governed runtime mode" in readme
    assert "hermes memory off != built-in memory injection off" in readme
    assert "memory tool absent != memory injection disabled" in readme

    assert "## Runtime profile modes" in constitution
    assert "runtime_mode: pantheon-governed" in constitution
    assert "task_contract_use: required" in constitution
    assert "built_in_memory_injection: off" in constitution
    assert "built_in_user_profile_injection: off" in constitution
    assert "memory_tool: off" in constitution
    assert "session_memory_key: forbidden" in constitution
    assert "runtime_mode: assistant-personal" in constitution
    assert "task_contract_use: forbidden" in constitution
    assert "They must not be duplicated into parallel `*-governed` profile families" in constitution
    assert "profile route reachable != profile safe" in constitution
    assert "hermes memory off != built-in memory injection off" in constitution
    assert "memory tool absent != memory injection disabled" in constitution
    assert "runtime_mode: pantheon-governed" in constitution.split("## Kanban handoff convention", 1)[1]
    assert "A `pantheon-governed` task must not delegate into `assistant-personal`" in constitution
    assert "profile route fell back to default" in constitution

    assert "Any functional profile that receives a Pantheon Task Contract" in base_rules
    assert "built-in `MEMORY.md` prompt injection off" in base_rules
    assert "built-in `USER.md` profile injection off" in base_rules
    assert "memory tool off" in base_rules
    assert "`X-Hermes-Session-Key` absent" in base_rules
    assert "must remain `not_qualified`" in base_rules


def test_runtime_card_exposes_each_memory_posture_axis() -> None:
    governance = _text(RUNTIME_GOVERNANCE)

    assert "memory_posture:" in governance
    assert "external_provider: unknown | off | selected" in governance
    assert "built_in_memory_injection: unknown | off | on" in governance
    assert "built_in_user_profile_injection: unknown | off | on" in governance
    assert "memory_tool: unknown | off | on" in governance
    assert "session_memory_key: unknown | absent | present" in governance
    assert "Any unknown or `on/present/selected` value keeps the governed profile `not_qualified`" in governance
    assert "Pantheon displays and classifies the observation" in governance
    assert "it does not read arbitrary profile files" in governance


def test_binding_registry_prefers_replaceable_components_over_platform_sprawl() -> None:
    bindings = _text(BINDINGS)
    haystack_version = _external_pin_version("haystack")

    assert "`document_structural_analysis` | Docling preferred candidate" in bindings
    assert "`document_source_management` | `unbound`" in bindings
    assert "Paperless is superseded as a target dependency" in bindings
    assert "`observability` | Langfuse preferred candidate" in bindings
    assert "`knowledge_retrieval_pipeline` | `unbound`" in bindings
    assert "no canonical rag framework is required" in bindings.lower()
    assert f"Haystack {haystack_version} matched native quality" in bindings
    assert "`external_runtime_memory` | `unbound`" in bindings
    assert "Hermes native memory is a valid baseline" in bindings
    assert "Hindsight is the currently recommended external provider" in bindings
    assert "Obsidian + Hindsight = qualified and recommended external reference composition" in bindings
    assert "Obsidian + Hindsight != mandatory Pantheon stack" in bindings
    assert "historically qualified != current default recommendation" in bindings
    assert "provider implementation changes\n!= Pantheon governance owner changes" in bindings


def test_retrieval_binding_reuses_libraries_without_adopting_new_runtimes() -> None:
    retrieval = _text(RETRIEVAL)

    assert "binding_status: unbound" in retrieval
    assert "candidate_bindings: none selected" in retrieval
    assert "watchlist_bindings: Haystack, LlamaIndex, selected LangChain components" in retrieval
    assert "measured retrieval-quality gain               = none" in retrieval
    assert "do not expose Haystack's framework/agent control surface to Hermes" in retrieval
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


def test_runtime_target_selection_does_not_change_runtime_authority() -> None:
    review = _text(RUNTIME_REVIEW)
    candidate_runtime = _external_pin_version("hermes-agent")

    assert f"current candidate distribution runtime target: {candidate_runtime}" in review
    assert f"candidate_distribution_runtime_target: {candidate_runtime}" in review
    assert "candidate_distribution_pin_change_authorized: true" in review
    assert "target_selection_effect: candidate-only" in review
    assert "new_runtime_owner_required: false" in review
    assert "new_client_owner_required: false" in review
    assert "installation_effect: none" in review
    assert "activation_effect: none" in review
    assert "task_authorization_effect: none" in review
    assert "candidate pin selected != runtime observed" in review
    assert "candidate pin selected != runtime qualified" in review
    assert "runtime approval endpoint != Pantheon approval" in review
