from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "templates/hermes/skills/pantheon-activity-projection/SKILL.md"
BASE_SOUL = ROOT / "hermes/profiles/_base/base-soul-rules.md"
REGISTRY = ROOT / "templates/TEMPLATE_REGISTRY.md"
REQUEST_INTAKE = ROOT / "templates/hermes/skills/pantheon-request-intake/SKILL.md"


def test_activity_projection_is_presentation_only_and_proportional() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "name: pantheon-activity-projection" in text
    assert "status: candidate_template_only" in text
    assert "governed_by: docs/governance/CONVERSATION_ACTIVITY_PROJECTION.md" in text

    for invariant in (
        "projection != persistence",
        "visible role != activated role",
        "handoff line != runtime dispatch",
        "retrieved source != truth",
        "runtime success != approval",
        "summary rationale != hidden chain-of-thought",
    ):
        assert invariant in text

    assert "simple direct request" in text
    assert "no activity projection, or one compact line only when materially useful" in text
    assert "Do not publish every tool call" in text
    assert "Do not emit progress merely to display activity" in BASE_SOUL.read_text(encoding="utf-8")


def test_activity_projection_explains_action_reason_goal_result_without_cot() -> None:
    text = SKILL.read_text(encoding="utf-8")

    for label in ("Action", "Reason", "Goal", "Result"):
        assert f"{label}\n=" in text

    assert "concise observable\nrationale" in text
    assert "two document revisions exist" in text
    assert "Do not generate a private reasoning transcript" in text


def test_activity_projection_requires_real_source_metadata_and_stable_refs() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "assign stable references" in text
    assert "[S1] Document title" in text
    assert "Index/revision: C2" in text
    assert "Date: 2026-05-14" in text
    assert "Never infer a missing date, index or version" in text
    assert "not identified" in text
    assert "source returned != source verified" in text
    assert "source name guessed from context != source citation" in text


def test_activity_projection_distinguishes_methods_skills_tools_and_real_use() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "## Methods, skills and tools" in text
    assert "Method\n= governed or task method actually selected/applied" in text
    assert "Skill\n= Hermes skill actually used" in text
    assert "Tool\n= concrete runtime tool/connector/capability actually invoked or observed" in text
    assert "Availability does not mean use" in text
    assert "List a skill or tool only when its use is observed" in text
    assert "Do not claim Docling, Hindsight, MCP, Drive" in text


def test_activity_projection_handoff_is_responsibility_not_dispatch() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "## Handoff" in text
    assert "→ Relais : Argos" in text
    assert "does not imply a new agent,\nsubagent, message bus or dispatch action" in text
    assert "If Hermes actually delegates runtime work" in text


def test_activity_projection_supports_interim_delivery_without_transport_dependency() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "supports safe interim assistant messages" in text
    assert "publish milestones progressively" in text
    assert "preserve the same structure\nin a compact final response" in text
    assert "do not introduce a second transport mechanism" in text


def test_activity_projection_is_bound_once_without_polluting_semantic_intake() -> None:
    base = BASE_SOUL.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    intake = REQUEST_INTAKE.read_text(encoding="utf-8")
    path = "templates/hermes/skills/pantheon-activity-projection/SKILL.md"

    assert "`pantheon-activity-projection` skill" in base
    assert "initial plan, action, observable\nreason, goal, cited sources" in base
    assert registry.count(path) == 1
    assert "pantheon-activity-projection" not in intake


def test_floquet_example_is_explicitly_non_authoritative() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "## Floquet acceptance example" in text
    assert "Source: [S1] Budget estimatif C2" in text
    assert "Skill: <only the skill actually used>" in text
    assert "Tool: <only the tool actually invoked>" in text
    assert "not a claim about the real Floquet corpus" in text
