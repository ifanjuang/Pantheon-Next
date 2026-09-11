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

    assert "Keep simple requests quiet" in text
    assert "2-4 meaningful milestones" in text
    assert "Do not publish every tool call" in text


def test_activity_projection_explains_action_reason_goal_result_without_cot() -> None:
    text = SKILL.read_text(encoding="utf-8")

    for field in ("Action:", "Raison:", "But:", "Résultat:"):
        assert field in text

    assert "concise observable rationale" in text
    assert "not private reasoning" in text
    assert "Never output a\nscratchpad, hidden chain-of-thought" in text


def test_activity_projection_requires_real_source_metadata_and_stable_refs() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "assign stable task-local\nreferences" in text
    assert "[S1] <observed title>" in text
    assert "Indice/révision: <observed value or non identifié>" in text
    assert "Date: <observed value or non identifiée>" in text
    assert "Never infer a missing title, date, index, revision" in text
    assert "source returned != source verified" in text
    assert "source name guessed from context != source citation" in text


def test_activity_projection_distinguishes_methods_skills_tools_and_real_use() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "## Method, skill and tool" in text
    assert "Méthode = governed/task method actually selected and applied" in text
    assert "Skill   = Hermes skill actually used in the current task" in text
    assert "Outil   = runtime tool, connector or capability actually invoked or observed" in text
    assert "Availability does not mean use" in text
    assert "Do not claim Docling, Hindsight, MCP, Drive" in text


def test_activity_projection_handoff_is_responsibility_not_dispatch() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "A `→ Relais` line means the next responsibility" in text
    assert "not a new agent or dispatch" in text
    assert "If\nHermes actually delegates runtime work" in text


def test_activity_projection_supports_native_interim_or_compact_final_delivery() -> None:
    text = SKILL.read_text(encoding="utf-8")
    base = BASE_SOUL.read_text(encoding="utf-8")

    assert "supports safe interim assistant messages" in text
    assert "publish meaningful milestones progressively" in text
    assert "compact final response" in text
    assert "do not introduce a second transport\nmechanism" in text
    assert "do not introduce a second transport mechanism" in base


def test_activity_projection_binding_stays_small_and_does_not_pollute_intake() -> None:
    base = BASE_SOUL.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    intake = REQUEST_INTAKE.read_text(encoding="utf-8")
    path = "templates/hermes/skills/pantheon-activity-projection/SKILL.md"

    assert base.count("pantheon-activity-projection") == 1
    assert "Keep simple requests quiet" in base
    assert "presentation never activates Roles" in base
    assert registry.count(path) == 1
    assert "pantheon-activity-projection" not in intake


def test_floquet_example_is_shape_only_and_contains_no_invented_project_fact() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "## Floquet acceptance shape" in text
    assert "<document réel>" in text
    assert "<indice observé>" in text
    assert "<skill réellement utilisé>" in text
    assert "<outil réellement invoqué>" in text
    assert "not a claim about the real Floquet corpus" in text
    assert "120 000" not in text
    assert "Budget estimatif C2" not in text
