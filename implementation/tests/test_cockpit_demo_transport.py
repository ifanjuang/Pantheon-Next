"""The static Cockpit demo must reuse the live loader contract without network route drift."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


def _run_node(script: str) -> subprocess.CompletedProcess[str]:
    node = shutil.which("node")
    if node is None:  # pragma: no cover - depends on the runner image
        pytest.skip("Node.js is unavailable; Cockpit demo transport check skipped")
    return subprocess.run(
        [node, "-e", script],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def test_demo_bootstrap_does_not_duplicate_api_routes_or_replace_global_fetch() -> None:
    bootstrap = (COCKPIT / "demo_bootstrap.js").read_text(encoding="utf-8")
    loader = (COCKPIT / "data" / "cockpit_data_loader.js").read_text(encoding="utf-8")

    assert "window.fetch =" not in bootstrap
    assert '"/agency/' not in bootstrap
    assert '"/work/' not in bootstrap
    assert '"/decision-inbox' not in bootstrap
    assert "fetchImplFactory" in bootstrap
    assert "const ROUTES" in loader
    assert "options.fetchImplFactory?.(ROUTES)" in loader
    assert 'loadOptionalCollection(ROUTES.toolCatalog(), "items")' in loader
    assert "routes: ROUTES" not in loader


def test_demo_fixture_transport_covers_the_current_live_loader_contract() -> None:
    script = r'''
      const fs = require("fs");
      const path = require("path");

      class TestResponse {
        constructor(body, options = {}) {
          this.body = body;
          this.status = options.status ?? 200;
          this.statusText = String(this.status);
          this.headers = options.headers || {};
        }
        get ok() { return this.status >= 200 && this.status < 300; }
        async json() { return JSON.parse(this.body); }
      }

      global.Response = TestResponse;
      const cockpitRoot = path.join(process.cwd(), "mvp_vertical", "cockpit");
      const fixtureNames = new Set(["demo-data.json", "demo-work-activity.json"]);
      const nativeCalls = [];

      global.window = {
        location: { href: "https://demo.invalid/mvp_vertical/cockpit/index.html?mode=demo" },
        setTimeout,
        fetch: async input => {
          const raw = typeof input === "string" ? input : input.url;
          nativeCalls.push(raw);
          const name = path.basename(new URL(raw, window.location.href).pathname);
          if (!fixtureNames.has(name)) {
            throw new Error(`unexpected native/network fetch: ${raw}`);
          }
          return new TestResponse(fs.readFileSync(path.join(cockpitRoot, name), "utf8"), {
            status: 200,
            headers: { "Content-Type": "application/json; charset=utf-8" },
          });
        },
      };

      (async () => {
        const demoSource = fs.readFileSync(path.join(cockpitRoot, "demo_bootstrap.js"), "utf8");
        const executeDemo = new Function(`return (async () => {\n${demoSource}\n})();`);
        await executeDemo();

        const originalFactory = window.PantheonCockpitDataLoaderOptions.fetchImplFactory;
        let demoFetch = null;
        window.PantheonCockpitDataLoaderOptions = Object.freeze({
          fetchImplFactory: routes => {
            demoFetch = originalFactory(routes);
            return demoFetch;
          },
        });

        require("./mvp_vertical/cockpit/data/cockpit_data_loader.js");
        const api = window.PantheonCockpitDataLoader;
        if (!api?.create) throw new Error("loader API was not exposed");
        if ("routes" in api) throw new Error("loader route registry leaked into the public API");

        const loader = api.create();
        const tools = await loader.loadToolCatalog();
        const projects = await loader.loadAgencyProjects("demo-read-only");
        const schema = await loader.loadProjectSchema("demo-read-only");
        const bundle = await loader.loadProjectBundle("demo-vallons", "demo-read-only");

        if (!demoFetch) throw new Error("demo transport factory was not used by the loader");
        if (!tools.length) throw new Error("tool catalogue fixture was not projected");
        if (projects.length !== 4) throw new Error(`unexpected project count: ${projects.length}`);
        if (schema?.schema_id !== "agency.project.v2-demo") throw new Error("project schema fixture missing");
        if (bundle.information.length !== 3) throw new Error("VALLONS information fixture incomplete");
        if (bundle.legacyDocuments.length !== 1) throw new Error("VALLONS document fixture incomplete");
        if (bundle.knowledge.length !== 1) throw new Error("VALLONS knowledge fixture incomplete");
        if (bundle.workIssues.length !== 1 || !bundle.workIssues[0]?.work_activity) {
          throw new Error("strict Work activity fixture was not reused");
        }
        if (bundle.changeCandidates.length !== 1 || bundle.changeCandidates[0]?.status !== "pending_review") {
          throw new Error("change-candidate status filtering drifted");
        }
        if (bundle.projectAnatomy !== null) throw new Error("missing demo anatomy must remain optional");
        if (nativeCalls.length !== 2) {
          throw new Error(`loader escaped fixture transport: ${nativeCalls.join(", ")}`);
        }

        const unknown = await demoFetch("../agency/projects/demo-vallons/unmodelled-surface");
        if (unknown.status !== 404) throw new Error("unknown loader route did not fail closed");
        if (nativeCalls.length !== 2) throw new Error("unknown route fell through to native fetch");

        const write = await demoFetch("../agency/projects", { method: "POST" });
        if (write.status !== 405) throw new Error("demo write boundary regressed");
      })().catch(error => { console.error(error); process.exit(1); });
    '''
    result = _run_node(script)
    assert result.returncode == 0, result.stderr
