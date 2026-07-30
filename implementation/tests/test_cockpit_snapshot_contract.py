"""Behavior contract for CockpitSnapshot.

The snapshot is the single projection shape the cockpit consumes, whatever
produces it (demo fixture, live renderer, future server endpoint). It is pure
data, so it is exercised for real here rather than asserted as text.

Key property: an incompatible or identity-less projection is REFUSED and stays
visible as a refusal. It is never coerced into a partial success.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
SNAPSHOT = COCKPIT / "v3" / "collection" / "cockpit_snapshot.js"
LIVE_PROVIDER = COCKPIT / "v3" / "providers" / "live_provider.js"


def _run_module(body: str) -> subprocess.CompletedProcess[str]:
    node = shutil.which("node")
    if node is None:  # pragma: no cover - depends on the runner image
        pytest.skip("Node.js is unavailable; JavaScript behavior check skipped")
    source = SNAPSHOT.read_text(encoding="utf-8") + "\n" + body
    return subprocess.run(
        [node, "--input-type=module", "-e", source],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def _run_imports(body: str) -> subprocess.CompletedProcess[str]:
    node = shutil.which("node")
    if node is None:  # pragma: no cover - depends on the runner image
        pytest.skip("Node.js is unavailable; JavaScript behavior check skipped")
    return subprocess.run(
        [node, "--input-type=module", "-e", body],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def test_snapshot_is_versioned_and_keeps_identity_and_position() -> None:
    result = _run_module(
        """
        const snapshot = createSnapshot({
          source: "demo",
          collection: { id: "projects", title: "Affaires", canCreate: true },
          items: [{ id: "a" }, { id: "b" }, { id: "c" }],
          index: 2,
        });

        if (snapshot.snapshot_version !== SNAPSHOT_VERSION) throw new Error("snapshot is not versioned");
        if (snapshot.collection.can_create !== true) throw new Error("creatability lost");
        if (snapshot.navigation.active_index !== 2) throw new Error("position lost");
        if (snapshot.navigation.active_entity_id !== "c") throw new Error("identity lost");
        if (!snapshot.generated_at) throw new Error("freshness marker missing");

        const read = readSnapshot(snapshot);
        if (!read.ok) throw new Error("a freshly built snapshot must validate");

        const empty = createSnapshot({ items: [] });
        if (empty.navigation.active_index !== -1) throw new Error("empty collection must have no active index");
        """
    )
    assert result.returncode == 0, result.stderr


def test_incompatible_or_identityless_snapshots_are_refused() -> None:
    result = _run_module(
        """
        const older = { snapshot_version: "cockpit.snapshot.v0", items: [] };
        const refusedVersion = readSnapshot(older);
        if (refusedVersion.ok) throw new Error("an unknown version must be refused");
        if (refusedVersion.reason !== SNAPSHOT_REFUSALS.INCOMPATIBLE_VERSION) throw new Error("wrong refusal reason");
        if (!refusedVersion.detail) throw new Error("a refusal must stay explainable");

        if (readSnapshot(null).ok) throw new Error("a non-object must be refused");
        if (readSnapshot({ snapshot_version: SNAPSHOT_VERSION }).ok) throw new Error("missing items must be refused");

        const orphan = createSnapshot({ items: [{ id: "ok" }, { title: "no identity" }] });
        const refusedIdentity = readSnapshot(orphan);
        if (refusedIdentity.ok) throw new Error("an item without stable identity must be refused");
        if (refusedIdentity.reason !== SNAPSHOT_REFUSALS.ITEM_WITHOUT_IDENTITY) throw new Error("wrong refusal reason");

        // A refusal is a result, never a half-built snapshot.
        if ("snapshot" in refusedIdentity) throw new Error("a refusal must not carry a coerced snapshot");
        """
    )
    assert result.returncode == 0, result.stderr


def test_live_provider_preserves_invalid_items_for_explicit_refusal() -> None:
    result = _run_imports(
        f"""
        import {{ createLiveProvider }} from {json.dumps(LIVE_PROVIDER.as_uri())};
        import {{ readSnapshot, SNAPSHOT_REFUSALS }} from {json.dumps(SNAPSHOT.as_uri())};

        const snapshot = createLiveProvider().toSnapshot({{
          key: "projects",
          siblings: [
            {{ entity_id: "project-1", title: "Valid" }},
            {{ title: "Missing identity" }},
          ],
        }});

        if (snapshot.items.length !== 2) throw new Error("the provider silently removed an invalid card");
        const result = readSnapshot(snapshot);
        if (result.ok) throw new Error("the invalid live projection must be refused");
        if (result.reason !== SNAPSHOT_REFUSALS.ITEM_WITHOUT_IDENTITY) throw new Error("wrong refusal reason");
        """
    )
    assert result.returncode == 0, result.stderr


def test_server_owned_fields_are_carried_but_not_interpreted() -> None:
    # Comments state the doctrine ("visible != authorized"), so the check looks
    # at code only.
    code = "\n".join(
        line for line in SNAPSHOT.read_text(encoding="utf-8").splitlines()
        if not line.lstrip().startswith("//")
    )

    # `actions` / `schemas` are server contracts: the cockpit passes them through
    # and must not derive authorization from them.
    assert "actions" in code
    assert "schemas" in code
    for forbidden in ("authorized", "permission", "canApply", "allowWrite"):
        assert forbidden not in code, forbidden


def test_demo_and_live_providers_emit_the_same_contract() -> None:
    demo = (COCKPIT / "v3" / "providers" / "demo_provider.js").read_text(encoding="utf-8")
    live = LIVE_PROVIDER.read_text(encoding="utf-8")

    for source in (demo, live):
        assert "createSnapshot" in source
        assert "cockpit_snapshot.js" in source
    assert 'source: "demo"' in demo
    assert 'source: "live"' in live


def test_demo_fixture_still_feeds_the_demo_provider() -> None:
    fixture = json.loads((COCKPIT / "demo-data.json").read_text(encoding="utf-8"))

    assert fixture["projects"], "the demo universe must not be empty"
    for project in fixture["projects"]:
        assert project["project_id"], "every fixture project needs a stable identity"
