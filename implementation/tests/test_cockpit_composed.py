from pathlib import Path

from mvp_vertical import (
    agency_change_candidate_review,
    apu_mapping_reviews,
    apu_write_preparation,
    cockpit_composed,
    contradictory_review_store,
    entity_relations,
    execution_results,
    information_projection,
    knowledge_edit_variants,
    source_intake,
)


class FakeConnection:
    def __init__(self):
        self.statements = []
        self.commits = 0
        self.closed = False

    def execute(self, statement):
        self.statements.append(statement)

    def commit(self):
        self.commits += 1

    def close(self):
        self.closed = True


def test_composed_app_mounts_candidate_review_routes_without_startup_effects():
    app = cockpit_composed.create_composed_cockpit_app(
        connect_fn=lambda: None,
        initialize_fn=None,
        api_key="read-secret",
        editor_api_key="editor-secret",
        hermes_api_key="hermes-secret",
    )
    methods_by_path: dict[str, set[str]] = {}
    for route in app.routes:
        if hasattr(route, "path") and hasattr(route, "methods"):
            methods_by_path.setdefault(route.path, set()).update(route.methods or set())
    assert "GET" in methods_by_path["/agency/information/{information_id}/projection"]
    assert "GET" in methods_by_path[
        "/agency/projects/{project_id}/information-projections"
    ]
    assert "POST" in methods_by_path["/agency/entity-relations"]
    assert "GET" in methods_by_path["/agency/entity-relations/{relation_id}"]
    assert "GET" in methods_by_path[
        "/agency/projects/{project_id}/entity-relations"
    ]
    assert "GET" in methods_by_path[
        "/agency/entities/{entity_type}/{entity_id}/relations"
    ]
    assert "POST" in methods_by_path[
        "/agency/entity-relations/{relation_id}/retire"
    ]
    assert "POST" in methods_by_path["/execution-results"]
    assert "POST" in methods_by_path[
        "/execution-results/{execution_result_id}/results/{result_ref}/project-knowledge-edit-variant"
    ]
    assert "POST" in methods_by_path["/knowledge/{knowledge_id}/variant-edit-requests"]
    assert "GET" in methods_by_path["/knowledge/{knowledge_id}/edit-reviews"]
    assert "POST" in methods_by_path["/edit-requests/{request_id}/select-variant"]
    assert "POST" in methods_by_path["/edit-requests/{request_id}/apply-selected"]
    mapping_reviews_path = "/execution-results/{execution_result_id}/results/{result_ref}/mappings/{mapping_ref}/reviews"
    assert "POST" in methods_by_path[mapping_reviews_path]
    assert "GET" in methods_by_path[mapping_reviews_path]
    prepare_path = "/execution-results/{execution_result_id}/results/{result_ref}/mappings/{mapping_ref}/prepare-apu-write"
    assert "POST" in methods_by_path[prepare_path]
    assert "GET" in methods_by_path["/apu-write-commands/{command_id}"]
    assert "POST" in methods_by_path["/apu-write-commands/{command_id}/authorizations"]
    assert "GET" in methods_by_path["/apu-write-commands/{command_id}/authorizations"]


def test_composed_initializer_replays_owner_and_review_migrations_in_dependency_order(monkeypatch):
    connection = FakeConnection()
    monkeypatch.setattr(cockpit_composed.store, "connect", lambda: connection)
    cockpit_composed.initialize_composed_schema()
    assert connection.commits == 1
    assert connection.closed is True
    assert len(connection.statements) == 11
    assert "CREATE TABLE IF NOT EXISTS agency_sources" in connection.statements[2]
    assert "CREATE TABLE IF NOT EXISTS agency_information_projection_metadata" in connection.statements[3]
    assert "CREATE TABLE IF NOT EXISTS agency_entity_relations" in connection.statements[4]
    assert "CREATE TABLE IF NOT EXISTS execution_results" in connection.statements[7]
    assert "CREATE TABLE IF NOT EXISTS knowledge_edit_variants" in connection.statements[8]
    assert "CREATE TABLE IF NOT EXISTS apu_mapping_review_events" in connection.statements[9]
    assert "CREATE TABLE IF NOT EXISTS apu_write_command_candidates" in connection.statements[10]


def test_composed_migrations_are_packaged_under_sql_directory():
    for migration, expected_name in (
        (source_intake.MIGRATION, "010_source_intake_admission.sql"),
        (information_projection.MIGRATION, "013_information_card_projection.sql"),
        (entity_relations.MIGRATION, "015_entity_relations.sql"),
        (agency_change_candidate_review.MIGRATION, "005_change_candidate_review.sql"),
        (contradictory_review_store.MIGRATION, "003_contradictory_review_candidates.sql"),
        (execution_results.MIGRATION, "010_execution_results.sql"),
        (knowledge_edit_variants.MIGRATION, "014_knowledge_edit_variants.sql"),
        (apu_mapping_reviews.MIGRATION, "011_apu_mapping_reviews.sql"),
        (apu_write_preparation.MIGRATION, "012_apu_write_preparation.sql"),
    ):
        assert isinstance(migration, Path)
        assert migration.name == expected_name
        assert migration.parent.name == "sql"
        assert migration.is_file()


def test_console_entrypoint_targets_composed_cockpit():
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    assert 'mvp-cockpit-api = "mvp_vertical.cockpit_composed:run"' in pyproject
