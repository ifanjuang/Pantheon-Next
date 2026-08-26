"""Regression checks for Cockpit information-architecture convergence."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE = ROOT / "docs" / "governance"
OLD_INFORMATION_ARCHITECTURE = GOVERNANCE / "PANTHEON_COCKPIT_INFORMATION_ARCHITECTURE.md"
STRUCTURED_INTERFACE = GOVERNANCE / "PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md"
KNOWLEDGE_GOVERNANCE = GOVERNANCE / "KNOWLEDGE_INGESTION_AND_MEMORY.md"
DECISION_REQUEST_SCHEMA = ROOT / "schemas" / "decision_request.schema.yaml"
AUTHORITY_INDEX = GOVERNANCE / "authority" / "GOVERNANCE_AUTHORITY_INDEX.md"


def test_five_space_cockpit_owner_is_retired_in_favor_of_six_space_owner() -> None:
    assert not OLD_INFORMATION_ARCHITECTURE.exists()

    structured = STRUCTURED_INTERFACE.read_text(encoding="utf-8")
    assert "Pantheon ↔ Décisions ↔ Affaires ↔ Connaissances ↔ Compétences ↔ Outils" in structured

    authority = AUTHORITY_INDEX.read_text(encoding="utf-8")
    assert "PANTHEON_COCKPIT_INFORMATION_ARCHITECTURE.md" not in authority
    assert "PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md" in authority
    assert "six root spaces" in authority


def test_retired_owner_does_not_remove_decision_work_issue_boundary() -> None:
    decision_schema = DECISION_REQUEST_SCHEMA.read_text(encoding="utf-8")

    assert "one_active_blocking_request_per_work_issue: true" in decision_schema
    assert "work_issue_continuation_is_separate: true" in decision_schema
    assert "automatic_work_issue_transition: false" in decision_schema
    assert "automatic_runtime_continuation: false" in decision_schema


def test_retired_owner_does_not_remove_project_to_general_knowledge_boundary() -> None:
    knowledge = KNOWLEDGE_GOVERNANCE.read_text(encoding="utf-8")

    assert "project first; general only after human promotion" in knowledge
    assert "may become general only after explicit extraction, anonymization if needed, and validation" in knowledge
    assert "explicitly promoted to general or agency memory" in knowledge
