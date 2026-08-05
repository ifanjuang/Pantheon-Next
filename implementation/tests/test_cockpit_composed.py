from pathlib import Path

from mvp_vertical import (
    agency_change_candidate_review,
    apu_mapping_reviews,
    cockpit_composed,
    contradictory_review_store,
    execution_results,
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
        if not hasattr(route, "path") or not hasattr(route, "methods"):
            continue
        methods_by_path.setdefault(route.path, set()).update(route.methods or set())

    assert "POST" in methods_by_path["/projects/{project_id}/contradictory-reviews"]
    assert "GET" in methods_by_path["/projects/{project_id}/contradictory-reviews"]
    assert "GET" in methods_by_path["/contradictory-reviews/{review_id}"]
    assert "POST" in methods_by_path["/execution-results"]
    assert "GET" in methods_by_path["/execution-results/{execution_result_id}"]
    assert "GET" in methods_by_path["/projects/{project_ref}/execution-results"]
    assert "POST" in methods_by_path[
        "/execution-results/{execution_result_id}/results/{result_ref}/dispositions"
    ]
    mapping_reviews_path = (
        "/execution-results/{execution_result_id}/results/{result_ref}"
        "/mappings/{mapping_ref}/reviews"
    )
    assert "POST" in methods_by_path[mapping_reviews_path]
    assert "GET" in methods_by_path[mapping_reviews_path]
    assert "/v1/projects/{project_id}/contradictory-reviews" not in methods_by_path
    assert "/v1/contradictory-reviews/{review_id}" not in methods_by_path


def test_composed_initializer_replays_review_migrations_after_dependencies(monkeypatch):
    connection = FakeConnection()
    monkeypatch.setattr(cockpit_composed.store, "connect", lambda: connection)

    cockpit_composed.initialize_composed_schema()

    assert connection.commits == 1
    assert connection.closed is True
    assert len(connection.statements) == 6
    assert "CREATE TABLE IF NOT EXISTS work_issues" in connection.statements[0]
    assert "agency" in connection.statements[1].lower()
    assert "revision_requested" in connection.statements[2]
    assert "CREATE TABLE IF NOT EXISTS contradictory_review_candidates" in connection.statements[3]
    assert "CREATE TABLE IF NOT EXISTS execution_results" in connection.statements[4]
    assert "CREATE TABLE IF NOT EXISTS apu_mapping_review_events" in connection.statements[5]


def test_review_migrations_are_packaged_under_sql_directory():
    for migration, expected_name in (
        (agency_change_candidate_review.MIGRATION, "005_change_candidate_review.sql"),
        (contradictory_review_store.MIGRATION, "003_contradictory_review_candidates.sql"),
        (execution_results.MIGRATION, "010_execution_results.sql"),
        (apu_mapping_reviews.MIGRATION, "011_apu_mapping_reviews.sql"),
    ):
        assert isinstance(migration, Path)
        assert migration.name == expected_name
        assert migration.parent.name == "sql"
        assert migration.is_file()


def test_console_entrypoint_targets_composed_cockpit():
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    assert 'mvp-cockpit-api = "mvp_vertical.cockpit_composed:run"' in pyproject
