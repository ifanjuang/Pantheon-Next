import json
import re
from pathlib import Path


IMPLEMENTATION_ROOT = Path(__file__).resolve().parents[1]
LAB = IMPLEMENTATION_ROOT / "labs" / "a2ui-cockpit"
FIXTURE = LAB / "fixtures" / "research-summary.a2ui.json"

PROTOCOL_VERSION = "v0.9.1"
CATALOG_ID = "urn:pantheon:a2ui:research-summary:v0.1"
SURFACE_ID = "pantheon-research-summary"
ALLOWED_COMPONENTS = {"Column", "Row", "Text", "Card", "Divider", "Button"}
ALLOWED_ACTIONS = {"pantheon.prepare_hermes_handoff"}
SECRET_KEY = re.compile(
    r"(^|_)(authorization|api_?key|access_?token|refresh_?token|password|passwd|secret|cookie|session_?id)($|_)",
    re.IGNORECASE,
)


def _messages():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def _walk(value):
    if isinstance(value, dict):
        for key, nested in value.items():
            yield key, nested
            yield from _walk(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from _walk(nested)


def test_a2ui_research_fixture_is_bounded_v091_projection():
    messages = _messages()
    assert 1 <= len(messages) <= 8
    assert {message["version"] for message in messages} == {PROTOCOL_VERSION}

    creates = [message["createSurface"] for message in messages if "createSurface" in message]
    assert creates == [
        {
            "surfaceId": SURFACE_ID,
            "catalogId": CATALOG_ID,
            "sendDataModel": False,
        }
    ]

    components = [
        component
        for message in messages
        if "updateComponents" in message
        for component in message["updateComponents"]["components"]
    ]
    assert len(components) <= 64
    assert {component["component"] for component in components} <= ALLOWED_COMPONENTS
    assert all(component.get("id") for component in components)

    actions = [component["action"] for component in components if component.get("action")]
    assert actions
    assert all("functionCall" not in action for action in actions)
    assert {action["event"]["name"] for action in actions} <= ALLOWED_ACTIONS


def test_a2ui_research_fixture_contains_no_secret_like_ui_state():
    messages = _messages()
    data_values = [
        message["updateDataModel"].get("value")
        for message in messages
        if "updateDataModel" in message
    ]
    assert data_values

    for value in data_values:
        serialized = json.dumps(value, ensure_ascii=False).encode("utf-8")
        assert len(serialized) <= 128 * 1024
        for key, _nested in _walk(value):
            assert not SECRET_KEY.search(str(key)), key


def test_a2ui_lab_has_no_business_transport_or_browser_persistence_path():
    main = (LAB / "main.js").read_text(encoding="utf-8")
    guard = (LAB / "guard.js").read_text(encoding="utf-8")
    readme = (LAB / "README.md").read_text(encoding="utf-8")

    forbidden_runtime_tokens = (
        "fetch(",
        "XMLHttpRequest",
        "WebSocket",
        "localStorage",
        "sessionStorage",
        "indexedDB",
        "navigator.sendBeacon",
        'method: "POST"',
        "Authorization",
        "X-Pantheon-",
    )
    assert not any(token in main for token in forbidden_runtime_tokens)

    assert 'version: PROTOCOL_VERSION' in main
    assert 'new MessageProcessor' in main
    assert 'executed: false' in main
    assert 'persisted: false' in main
    assert 'authorized: false' in main

    assert "functionCall is forbidden" in guard
    assert "Unknown A2UI action rejected" in guard
    assert "sendDataModel=true is forbidden" in guard
    assert "Secret-like field rejected" in guard

    assert "lab present != Cockpit integration" in readme
    assert "direct generated-button -> business endpoint routing" in readme


def test_a2ui_lab_dependency_and_protocol_pins_are_explicit():
    package = json.loads((LAB / "package.json").read_text(encoding="utf-8"))
    assert package["dependencies"] == {
        "@a2ui/lit": "0.10.3",
        "@a2ui/web_core": "0.10.6",
        "lit": "3.3.3",
    }
    assert package["devDependencies"] == {"vite": "8.2.2"}

    catalog = (LAB / "catalog.js").read_text(encoding="utf-8")
    assert f'export const CATALOG_ID = "{CATALOG_ID}"' in catalog
    for component in ALLOWED_COMPONENTS:
        assert f'"{component}"' in catalog
    assert "new Catalog(" in catalog
    assert "selectedComponents," in catalog
    assert "[]," in catalog
