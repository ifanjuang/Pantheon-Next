from __future__ import annotations

from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "templates/hermes/skills/pantheon-activity-projection/SKILL.md"
SOUL_APPEND = ROOT / "templates/hermes/profiles/pantheon-governed/SOUL.append.md"
CONFIGURE = ROOT / "deployment/ubuntu/configure-hermes-activity-projection"


def test_activity_projection_skill_has_bounded_visible_contract() -> None:
    text = SKILL.read_text(encoding="utf-8")
    assert "name: pantheon-activity-projection" in text
    assert "status: candidate_template_only" in text
    assert "governed_by: docs/governance/CONVERSATION_ACTIVITY_PROJECTION.md" in text
    assert "trace_reference: docs/governance/ROLE_DIALOGUE_TRACE.md" in text
    assert "summary rationale != hidden chain-of-thought" in text
    assert "one compact initial plan" in text
    assert "only meaningful milestones" in text
    assert "do not invent one merely" in text
    assert "Hermes is a runtime, not a Pantheon Role" in text
    assert "## Observable Role outcomes" in text
    for readiness in (
        "ready",
        "ready_with_limits",
        "needs_revision",
        "needs_user_input",
        "blocked",
    ):
        assert readiness in text
    assert "draft complete != transmission authorized" in text
    assert "Do not activate extra Roles merely to populate" in text
    for role in (
        "Athena", "Argos", "Themis", "Apollo", "Hephaistos", "Iris", "Zeus", "Mnemosyne"
    ):
        assert role in text


def test_governed_profile_supplement_requires_progress_without_private_reasoning() -> None:
    text = SOUL_APPEND.read_text(encoding="utf-8")
    assert "For every non-trivial Pantheon-governed request" in text
    assert "publish the plan before" in text
    assert "material tool call" in text
    assert "never private reasoning" in text
    assert "Do not display every canonical Role" in text
    assert "visible" in text and "role label identifies a governance responsibility" in text


def test_linux_configurator_is_idempotent_and_keeps_a_backup() -> None:
    text = CONFIGURE.read_text(encoding="utf-8")
    subprocess.run(["bash", "-n", str(CONFIGURE)], check=True)
    assert "--check" in text and "--apply" in text
    assert "BEGIN PANTHEON ACTIVITY PROJECTION" in text
    assert "backups/hermes-activity-" in text
    assert "diff -qr" in text
    assert "docker restart pantheon-hermes" in text
    assert "projection != persistence" in text
    assert "check_profile_display" in text
    assert "apply_profile_display" in text
    assert 'config set display.interim_assistant_messages true' in text
    assert 'config set display.show_reasoning false' in text
    assert 'config set plugins.stream_reasoning_deltas false' in text
    for skill in (
        "external-commitment-guard",
        "ifja-project-context",
 "ifja-vault-search",
        "pantheon-activity-projection",
        "pantheon-governed-method",
        "pantheon-request-intake",
        "source-research",
    ):
        assert skill in text
    assert "rsync -a --delete --exclude '__pycache__/'" in text
    assert "--with-ifja-adapter" in text
    assert "optional contextual adapter" in text
    assert 'die "--bind-local-mcp requires --with-ifja-adapter"' in text


def test_whatsapp_governed_routing_is_explicit_scoped_and_non_destructive() -> None:
    text = CONFIGURE.read_text(encoding="utf-8")
    assert "--route-whatsapp" in text
    assert "--whatsapp-chat-id" in text
    assert "--all-authorized-whatsapp" in text
    assert '--route-whatsapp requires --whatsapp-chat-id or --all-authorized-whatsapp' in text
    assert '[$route] + map(select(.name != "pantheon-governed-whatsapp"))' in text
    assert 'map(select(.name != "pantheon-governed-whatsapp")) + [$route]' in text
    assert 'if index($profile) then . else . + [$profile] end' in text
    assert 'if ((update_allowlist == 1))' in text
    assert '. == null or . == "null"' in text
    assert 'refusing to replace it' in text
    assert 'Config key not set: $key' in text
    assert 'cp -a "$CONFIG_TARGET" "$backup_root/config.yaml"' in text


def test_whatsapp_projection_uses_supported_config_not_a_provider_patch() -> None:
    text = CONFIGURE.read_text(encoding="utf-8")
    assert "config set gateway.multiplex_profiles true" in text
    assert 'config set gateway.profile_routes "$merged_routes"' in text
    assert "config set display.platforms.whatsapp.show_reasoning false" in text
    assert "config set display.platforms.whatsapp.interim_assistant_messages true" in text
    assert "config set display.platforms.whatsapp.tool_progress new" in text
    assert 'config set plugins.stream_reasoning_deltas false' in text
    assert "no provider patch" in text


def test_governed_local_mcp_binding_is_explicit_filtered_and_fail_closed() -> None:
    text = CONFIGURE.read_text(encoding="utf-8")
    assert "--bind-local-mcp" in text
    assert "get_profile_optional_config_json default mcp_servers" in text
    for server in ("docling", "hindsight-affaires", "hindsight-documentaires", "hindsight-memory", "pantheon-policy"):
        assert server in text
    assert '"Doclin"' not in text
    assert '"tools": {"include": ["recall"]}' in text
    assert 'endswith("/mcp/hermes/")' in text
    assert "required local Hindsight bindings are absent; refusing partial inheritance" in text
    assert "'$current + $selected'" in text
    assert 'config set --force mcp_servers "$merged"' in text
    assert 'cp -a "$PROFILE_CONFIG_TARGET" "$backup_root/profile-config.yaml"' in text
    for tool in (
        "route_governed_request",
        "evaluate_preflight",
        "prepare_task_contract_skeleton",
        "prepare_evidence_pack_skeleton",
        "plan_context_pack",
        "validate_context_pack",
    ):
        assert tool in text
    assert '"list_sources"' not in text
    assert '"prompts": false' in text
    assert '"resources": false' in text
    assert '"enabled": false' in text
    assert 'supports_parallel_tool_calls = false' in text


def test_docling_mcp_introspection_tools_are_hidden_from_governed_profile() -> None:
    text = CONFIGURE.read_text(encoding="utf-8")
    assert '.docling.tools = (' in text
    assert '.docling.tools.prompts == false' in text
    assert '.docling.tools.resources == false' in text


def test_curated_default_capabilities_remain_bounded_and_searchable() -> None:
    text = CONFIGURE.read_text(encoding="utf-8")
    assert "--with-curated-default-skills" in text
    for skill in (
        "architecture-diagram",
        "excalidraw",
        "obsidian",
        "pdf",
        "ocr-and-documents",
        "docx",
        "xlsx",
        "powerpoint",
        "google-workspace",
        "grounded-citations",
    ):
        assert skill in text
    assert 'HERMES_IMAGE_SKILLS_ROOT="${HERMES_IMAGE_SKILLS_ROOT:-/opt/hermes/skills}"' in text
    assert 'docker cp "$CONTAINER:$source/." "$target/"' in text
    assert 'source="$CURATED_STAGE_ROOT/$name"' in text
    assert 'source="$HERMES_ROOT/skills/$path"' not in text
    assert "tools.tool_search.enabled auto" in text
    assert ".no-bundled-skills" in text
    assert "whole default skill catalogue" in text


def test_optional_runtime_dependencies_are_preflighted_before_profile_mutation() -> None:
    text = CONFIGURE.read_text(encoding="utf-8")
    preflight = text.index("preflight_optional_dependencies")
    backup = text.index('stamp="$(date -u +%Y%m%dT%H%M%SZ)"')
    first_profile_install = text.index('install -d -m 0755 "$PROFILE_ROOT/skills"')
    assert preflight < backup < first_profile_install
    assert "prepare_local_mcp_selection" in text
    assert "stage_curated_default_skills" in text
    assert "preflight_whatsapp_runtime" in text
    assert '[[ -n "$LOCAL_MCP_SELECTED" ]] || die "local MCP bindings were not preflighted"' in text
    assert '[[ -n "$CURATED_STAGE_ROOT" ]] || die "curated skills were not staged"' in text
