from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
BOOTSTRAP = COCKPIT / "live_bootstrap.js"
LOADER = COCKPIT / "data" / "cockpit_data_loader.js"
PROJECTION = COCKPIT / "projection" / "cockpit_projection.js"


def test_data_loader_is_loaded_before_projection() -> None:
    bootstrap = BOOTSTRAP.read_text(encoding="utf-8")
    loader = '"data/cockpit_data_loader.js"'
    projection = '"projection/cockpit_projection.js"'

    assert loader in bootstrap
    assert bootstrap.index(loader) < bootstrap.index(projection)


def test_projection_delegates_network_transport() -> None:
    source = PROJECTION.read_text(encoding="utf-8")

    assert "window.PantheonCockpitDataLoader.create()" in source
    assert "dataLoader.loadAgencyProjects(state.token)" in source
    assert "dataLoader.loadProjectSchema(state.token)" in source
    assert "dataLoader.loadProjectBundle(state.project, state.token)" in source
    assert "fetch(" not in source


def test_data_loader_has_a_bounded_read_only_role() -> None:
    source = LOADER.read_text(encoding="utf-8")

    for endpoint in (
        "../agency/projects?limit=200",
        "../agency/schema/project",
        "/information",
        "/documents",
        "/knowledge",
        "/work-issues",
        "/change-candidates?status=pending_review&limit=100",
    ):
        assert endpoint in source

    assert "../v1/agency/" not in source

    for forbidden in (
        "document.",
        "render",
        "navigator",
        "ChangeCandidate",
        "Evidence",
        "dispatch",
        "approve",
        "apply",
        "reject",
    ):
        assert forbidden not in source


def test_data_loader_and_projection_parse_in_node() -> None:
    for path in (LOADER, PROJECTION):
        subprocess.run(["node", "--check", str(path)], check=True, capture_output=True, text=True)


def test_data_loader_keeps_optional_metadata_failures_non_blocking() -> None:
    script = f"""
global.window = {{ fetch: async () => ({{
  ok: false,
  statusText: "Unavailable",
  json: async () => ({{ detail: "Unavailable" }}),
}}) }};
require({str(LOADER)!r});
(async () => {{
  const loader = window.PantheonCockpitDataLoader.create();
  const registries = await loader.loadRegistry("registry.json", "values");
  const tools = await loader.loadToolCatalog();
  if (registries.length !== 0 || tools.length !== 0) process.exit(1);
}})().catch(() => process.exit(2));
"""
    subprocess.run(["node", "-e", script], check=True, capture_output=True, text=True)