from pathlib import Path

from mvp_vertical import cockpit_composed, contradictory_review_store


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

    methods_by_path = {
        route.path: set(getattr(route, "methods", None) or set())
        for route in app.routes
        if hasattr(route, "path") and hasattr(route, "methods")
    }
    assert "POST" in methods_by_path["/v1/projects/{project_id}/contradictory-reviews"]
    assert "GET" in methods_by_path["/v1/projects/{project_id}/contradictory-reviews"]
    assert "GET" in methods_by_path["/v1/contradictory-reviews/{review_id}"]


def test_composed_initializer_replays_review_migration_after_dependencies(monkeypatch):
    connection = FakeConnection()
    monkeypatch.setattr(cockpit_composed.store, "connect", lambda: connection)

    cockpit_composed.initialize_composed_schema()

    assert connection.commits == 1
    assert connection.closed is True
    assert len(connection.statements) == 3
    assert "CREATE TABLE IF NOT EXISTS work_issues" in connection.statements[0]
    assert "agency" in connection.statements[1].lower()
    assert "CREATE TABLE IF NOT EXISTS contradictory_review_candidates" in connection.statements[2]


def test_review_migration_is_packaged_under_sql_directory():
    migration = contradictory_review_store.MIGRATION
    assert isinstance(migration, Path)
    assert migration.name == "003_contradictory_review_candidates.sql"
    assert migration.parent.name == "sql"
    assert migration.is_file()


def test_console_entrypoint_targets_composed_cockpit():
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    assert 'mvp-cockpit-api = "mvp_vertical.cockpit_composed:run"' in pyproject
