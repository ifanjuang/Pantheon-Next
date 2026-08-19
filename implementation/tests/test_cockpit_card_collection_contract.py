import json
from pathlib import Path
import shutil
import subprocess

import pytest


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
REGISTRY = COCKPIT / "registries" / "navigation_registry.json"
ASSEMBLER = COCKPIT / "projection" / "child_collection_assembler.js"
DATA_LOADER = COCKPIT / "data" / "cockpit_data_loader.js"
COCKPIT_PROJECTION = COCKPIT / "projection" / "cockpit_projection.js"
LIVE_ADAPTER = COCKPIT / "live_collection_adapter.js"


def _run_node(body: str) -> subprocess.CompletedProcess[str]:
    node = shutil.which("node")
    if node is None:  # pragma: no cover - runner dependent
        pytest.skip("Node.js is unavailable; Card/Collection behavior check skipped")
    return subprocess.run(
        [node, "--input-type=module", "-e", body],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def test_root_navigation_registry_does_not_own_entity_child_assembly() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    assert registry["revision"] == 1
    assert "entity_collections" not in registry


def test_child_collection_assembler_projects_loaded_and_available_relations() -> None:
    result = _run_node(
        f"""
        globalThis.window = {{
          PantheonDecisionRequestProjection: {{
            normalize(value) {{ return value; }},
            rootCard() {{ return {{ entity_id: "space:decisions" }}; }},
          }},
          PantheonProjectAnatomyProjection: {{ projectCards() {{ return null; }} }},
          PantheonGlobalDecisionRequests: [],
          PantheonProjectDecisionRequests: [],
        }};
        await import({json.dumps(ASSEMBLER.as_uri())});

        const cards = new Map([["space:affaires", {{ entity_id: "space:affaires" }}]]);
        const children = new Map();
        const state = {{
          cards,
          children,
          projects: [{{ project_id: "P1" }}, {{ project_id: "P2" }}],
          information: [],
          legacyDocuments: [],
          workIssues: [],
          changeCandidates: [],
          currentRuns: [],
          knowledge: [],
          projectAnatomy: null,
        }};
        const putCard = model => {{ cards.set(model.entity_id, model); return model.entity_id; }};
        const setChildren = (parent, ids) => children.set(parent, ids.slice());
        const normalizeProject = item => ({{
          entity_id: `project:${{item.project_id}}`,
          entity_type: "project",
          source_project_id: item.project_id,
        }});

        window.PantheonChildCollectionAssembler.assemble({{
          rootItemIds: ["space:affaires"],
          sourcesFor() {{ return ["projects"]; }},
          state,
          selected: {{ project_id: "P1", contacts: [] }},
          selectedProjectId: "P1",
          selectedCardId: "project:P1",
          putCard,
          setChildren,
          normalizeProject,
          normalizeKnowledge: value => value,
          normalizeChangeCandidate: value => value,
          normalizeCurrentRun: value => value,
          normalizeContacts(projectId) {{ return {{ entity_id: `project:${{projectId}}:contacts` }}; }},
          normalizeInformation: value => value,
          normalizeLegacyDocument: value => value,
          normalizeWork: value => value,
          buildToolCards() {{ return []; }},
          workData: value => value,
          currentRunItems() {{ return []; }},
        }});

        const root = cards.get("space:affaires");
        const selected = cards.get("project:P1");
        const unloaded = cards.get("project:P2");
        if (root.child_collection?.state !== "loaded") throw new Error("root collection not projected loaded");
        if (root.child_collection?.collection_id !== "children:space:affaires") throw new Error("root collection identity missing");
        if (selected.child_collection?.state !== "loaded") throw new Error("selected project not projected loaded");
        if (selected.child_collection?.can_add !== true) throw new Error("selected project lost create capability");
        if (unloaded.child_collection?.state !== "available") throw new Error("unloaded project not projected available");
        if (unloaded.child_collection?.load_action?.kind !== "project_bundle") throw new Error("project load action missing");
        """
    )
    assert result.returncode == 0, result.stderr


def test_data_loader_is_transport_only_for_project_and_decision_reads() -> None:
    source = DATA_LOADER.read_text(encoding="utf-8")

    assert "async function loadChildCollection(action, token)" in source
    assert 'if (action.kind === "project_bundle") return loadProjectBundle(contextId, token);' in source
    assert "loadChildCollection," in source
    assert "document." not in source
    assert "PantheonProjectDecisionRequests =" not in source.split("function create", 1)[1].split("window.PantheonGlobalDecisionRequests", 1)[0]
    assert "PantheonGlobalDecisionRequests =" not in source.split("function create", 1)[1].split("window.PantheonGlobalDecisionRequests", 1)[0]


def test_cockpit_projection_descends_from_projected_child_action_and_rejects_stale_loads() -> None:
    source = COCKPIT_PROJECTION.read_text(encoding="utf-8")

    assert 'model.entity_type === "project"' not in source
    assert 'model?.entity_type === "project"' not in source
    assert "function canDescend(model)" in source
    assert 'childCollection?.state === "available"' in source
    assert "Boolean(childCollection.load_action)" in source
    assert '$("v2-descend").disabled = !canDescend(model);' in source
    assert "collection_id: childCollection.collection_id" in source
    assert "|| `children:${model.entity_id}`" not in source
    assert "let projectLoadGeneration = 0;" in source
    assert "const generation = ++projectLoadGeneration;" in source
    assert source.count("if (generation !== projectLoadGeneration) return;") >= 3
    assert "dataLoader.loadChildCollection(childLoadAction, token)" in source
    assert "window.PantheonProjectDecisionRequests = Object.freeze" in source
    assert "window.PantheonGlobalDecisionRequests = Object.freeze" in source
    assert 'parentEntityId = snapshot.path[snapshot.path.length - 1]?.parent_entity_id || null' in source


def test_missing_token_releases_load_control_after_invalidating_an_older_request() -> None:
    source = COCKPIT_PROJECTION.read_text(encoding="utf-8")

    guard = source.index("if (!token) {")
    release = source.index("loadButton.disabled = false;", guard)
    message = source.index('return setMessage("Clé d’accès requise pour lire Agency Data.");', guard)

    assert 'const loadButton = $("v2-load");' in source
    assert guard < release < message
    assert "if (generation === projectLoadGeneration) loadButton.disabled = false;" in source


def test_live_collection_adapter_uses_explicit_parent_relation_not_id_parsing() -> None:
    source = LIVE_ADAPTER.read_text(encoding="utf-8")

    assert 'model?.entity_type === "project"' not in source
    assert 'parent?.entity_type === "project"' not in source
    assert "CHILD_COLLECTION_PREFIX" not in source
    assert "parentIdForCollection" not in source
    assert "currentParentEntityId" in source
    assert "model?.child_collection?.collection_id === id" in source
    assert "parent?.child_collection?.can_add === true" in source
    assert "parent?.child_collection?.create_action" in source


def test_live_collection_states_keep_not_loaded_distinct_from_empty() -> None:
    source = LIVE_ADAPTER.read_text(encoding="utf-8")

    assert '{ state: "none", models: [] }' in source
    assert '{ state: "available", models: [], collection: model.child_collection }' in source
    assert '{ state: "loaded", models: loaded }' in source
    assert '{ state: "empty", models: [] }' in source


def test_information_projection_keeps_source_index_separate_from_technical_revision() -> None:
    source = COCKPIT_PROJECTION.read_text(encoding="utf-8")

    assert "index: item.index_label || null" in source
    assert "technical_revision: item.revision || null" in source
    assert '["Révision technique", text(item.revision, "Non renseignée")]' in source
    assert '["Mis à jour le", text(item.updated_at, "Non renseigné")]' in source
