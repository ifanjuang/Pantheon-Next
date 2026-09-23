#!/usr/bin/env python3
"""Qualify the Linux-visible AFFAIRES mount used by Workspace Cockpit/Hindsight.

This operator-run probe writes one short-lived source/cartouche pair inside the
provided mount root, verifies the exact hidden-cartouche convention, exercises
rename + reconcile, observes whether Linux inotify events propagate through the
mount, then removes the probe directory.

The inotify result is diagnostic only: periodic reconcile remains the convergence
guarantee for remote/NAS filesystems.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import threading
import time
import uuid


REPO_ROOT = Path(__file__).resolve().parents[2]
SERVER = REPO_ROOT / "implementation" / "workspace_cockpit" / "server.py"


def _module():
    spec = importlib.util.spec_from_file_location("workspace_cockpit_server", SERVER)
    if not spec or not spec.loader:
        raise RuntimeError(f"cannot load Workspace Cockpit server: {SERVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write_cartouche(path: Path, *, source: str, document_id: str) -> None:
    path.write_text(
        f"""---
schema: pantheon/cartouche/v1
document_id: {document_id}
source: {source}
type: QUALIFICATION_PROBE
---
# AFFAIRES mount qualification

Temporary probe generated from the Linux host.
""",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Linux path of the mounted NAS AFFAIRES root")
    parser.add_argument("--keep", action="store_true", help="keep the probe directory for inspection")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"not a directory: {root}")

    module = _module()
    probe_name = f"PANTHEON_QUALIFICATION_{uuid.uuid4().hex[:8]}"
    probe = root / probe_name
    document_id = f"probe-{uuid.uuid4().hex}"
    state_dir = Path(tempfile.mkdtemp(prefix="pantheon-affaires-qualification-state-"))

    report: dict[str, object] = {
        "root": str(root),
        "probe": str(probe),
        "projection": module.PROJECTION_ID,
        "dotfile_roundtrip": False,
        "initial_projection": False,
        "rename_projection": False,
        "identity_preserved": False,
        "reconcile_rebuild": False,
        "inotify": "not-tested",
        "cleanup": False,
    }

    try:
        probe.mkdir()
        source = probe / "probe.pdf"
        cartouche = probe / ".probe.pdf.md"
        source.write_bytes(b"%PDF-1.4\n% Pantheon qualification probe\n")
        _write_cartouche(cartouche, source=source.name, document_id=document_id)

        report["dotfile_roundtrip"] = cartouche.is_file() and cartouche.read_text(encoding="utf-8").startswith("---")

        initial = module.scan_workspaces([("probe", probe)], max_depth=1)
        documents = [
            card for card in initial["workspaces"][0]["cards"]
            if card["kind"] == "document"
        ]
        if len(documents) != 1:
            raise RuntimeError(f"expected one projected document, got {len(documents)}")
        first = documents[0]
        if first["status"] != "COMPLETE":
            raise RuntimeError(f"initial pair is not COMPLETE: {first}")
        report["initial_projection"] = True

        renamed_source = probe / "probe-renamed.pdf"
        renamed_cartouche = probe / ".probe-renamed.pdf.md"
        source.rename(renamed_source)
        cartouche.rename(renamed_cartouche)
        _write_cartouche(renamed_cartouche, source=renamed_source.name, document_id=document_id)

        renamed = module.scan_workspaces([("probe", probe)], max_depth=1)
        documents = [
            card for card in renamed["workspaces"][0]["cards"]
            if card["kind"] == "document"
        ]
        if len(documents) != 1:
            raise RuntimeError(f"expected one renamed projected document, got {len(documents)}")
        second = documents[0]
        if second["status"] != "COMPLETE":
            raise RuntimeError(f"renamed pair is not COMPLETE: {second}")
        report["rename_projection"] = True
        report["identity_preserved"] = second["document_id"] == document_id == first["document_id"]

        state_db = state_dir / "index.sqlite3"
        index = module.WorkspaceIndex(
            [("probe", probe)],
            1,
            state_db,
            reconcile_seconds=60,
            debounce_seconds=0.05,
            enable_watcher=False,
        )
        snapshot = index.reconcile("mount-qualification")
        report["reconcile_rebuild"] = bool(
            state_db.is_file()
            and snapshot["document_count"] == 1
            and snapshot["workspaces"][0]["cards"][0]["document_id"] == document_id
        )

        observed = threading.Event()
        watcher = module._InotifyWatcher([("probe", probe)], 1, observed.set)
        if watcher.start():
            try:
                event_source = probe / "event.txt"
                event_source.write_text("event probe", encoding="utf-8")
                report["inotify"] = "observed" if observed.wait(2.0) else "not-observed-reconcile-required"
                event_source.unlink(missing_ok=True)
            finally:
                watcher.stop()
        else:
            report["inotify"] = "unavailable-reconcile-required"

        required = (
            report["dotfile_roundtrip"],
            report["initial_projection"],
            report["rename_projection"],
            report["identity_preserved"],
            report["reconcile_rebuild"],
        )
        report["qualified"] = all(required)
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0 if report["qualified"] else 1
    finally:
        shutil.rmtree(state_dir, ignore_errors=True)
        if args.keep:
            report["cleanup"] = False
        else:
            shutil.rmtree(probe, ignore_errors=True)
            report["cleanup"] = not probe.exists()


if __name__ == "__main__":
    raise SystemExit(main())
