from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sqlite3
import sys
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "implementation" / "workspace_cockpit" / "hindsight_producer.py"


def _module():
    spec = importlib.util.spec_from_file_location("workspace_hindsight_producer", PRODUCER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _snapshot(card: dict | None) -> dict:
    return {
        "workspaces": [
            {
                "name": "Affaires",
                "available": True,
                "cards": [] if card is None else [card],
                "errors": [],
            }
        ]
    }


def _card(path: str = "Notice.pdf", *, status: str = "COMPLETE", representation: str = "source") -> dict:
    return {
        "workspace": "Affaires",
        "kind": "document",
        "path": path,
        "name": Path(path).name,
        "status": status,
        "document_id": "doc-notice",
        "title": "Notice technique",
        "project": "LIEUREY",
        "phase": "DCE",
        "document_type": "NOTICE",
        "index": "C",
        "document_date": "2026-09-12",
        "issuer": "IFJA",
        "tags": ["structure", "ossature bois"],
        "summary": "Derived cartouche summary that must not become source metadata.",
        "source_sha256": None,
        "source_sha256_verified": None,
        "hindsight_eligible": status == "COMPLETE",
        "hindsight_representation_candidate": representation,
    }


class FakeClient:
    def __init__(self, statuses: list[str] | None = None) -> None:
        self.bank_id = "affaires-test"
        self.statuses = list(statuses or ["completed"])
        self.retains: list[dict] = []
        self.polls: list[str] = []

    def retain_file(self, source: Path, **kwargs):
        self.retains.append({"source": source, **kwargs})
        return f"op-{len(self.retains)}"

    def operation_status(self, operation_id: str):
        self.polls.append(operation_id)
        status = self.statuses.pop(0) if self.statuses else "completed"
        return {"operation_id": operation_id, "status": status, "error_message": None}


def _row(db: Path) -> dict:
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    try:
        row = con.execute("SELECT * FROM hindsight_sync").fetchone()
        assert row is not None
        return dict(row)
    finally:
        con.close()


def test_source_candidate_submits_then_completes_without_duplicate_retain(tmp_path: Path) -> None:
    module = _module()
    source = tmp_path / "Notice.pdf"
    source.write_bytes(b"%PDF-source-v1")
    db = tmp_path / "state" / "index.sqlite3"
    client = FakeClient(["completed"])
    producer = module.HindsightProducer(
        roots=[("Affaires", tmp_path)],
        state_db=db,
        client=client,
        max_submits_per_reconcile=4,
    )

    first = producer.reconcile(_snapshot(_card()))
    assert first["submitted"] == 1
    assert len(client.retains) == 1
    call = client.retains[0]
    assert call["source"] == source
    assert call["document_id"] == "doc-notice:source"
    assert call["metadata"]["pantheon_document_id"] == "doc-notice"
    assert call["metadata"]["project_hint"] == "LIEUREY"
    assert "document_index" not in call["metadata"]
    assert "document_date" not in call["metadata"]
    assert "summary" not in call["metadata"]
    assert "project_hint:lieurey" in call["tags"]
    assert "tag:ossature-bois" in call["tags"]
    assert _row(db)["status"] == "SUBMITTED"

    second = producer.reconcile(_snapshot(_card()))
    assert second["completed"] == 1
    assert client.polls == ["op-1"]
    assert len(client.retains) == 1
    assert _row(db)["status"] == "COMPLETED"


def test_source_change_waits_for_active_operation_before_replacement(tmp_path: Path) -> None:
    module = _module()
    source = tmp_path / "Notice.pdf"
    source.write_bytes(b"%PDF-source-v1")
    db = tmp_path / "state.sqlite3"
    client = FakeClient(["processing", "completed"])
    producer = module.HindsightProducer(
        roots=[("Affaires", tmp_path)],
        state_db=db,
        client=client,
    )

    producer.reconcile(_snapshot(_card()))
    source.write_bytes(b"%PDF-source-v2")

    active = producer.reconcile(_snapshot(_card()))
    assert active["pending"] == 1
    assert len(client.retains) == 1

    replaced = producer.reconcile(_snapshot(_card()))
    assert replaced["submitted"] == 1
    assert len(client.retains) == 2
    assert client.retains[1]["document_id"] == "doc-notice:source"
    assert _row(db)["operation_id"] == "op-2"


def test_check_and_cartouche_candidates_never_submit_source_file(tmp_path: Path) -> None:
    module = _module()
    (tmp_path / "Notice.pdf").write_bytes(b"%PDF")
    db = tmp_path / "state.sqlite3"
    client = FakeClient()
    producer = module.HindsightProducer(
        roots=[("Affaires", tmp_path)],
        state_db=db,
        client=client,
    )

    producer.reconcile(_snapshot(_card(status="CHECK")))
    producer.reconcile(_snapshot(_card(representation="cartouche")))
    assert client.retains == []


def test_completed_document_becomes_stale_without_remote_delete(tmp_path: Path) -> None:
    module = _module()
    (tmp_path / "Notice.pdf").write_bytes(b"%PDF")
    db = tmp_path / "state.sqlite3"
    client = FakeClient(["completed"])
    producer = module.HindsightProducer(
        roots=[("Affaires", tmp_path)],
        state_db=db,
        client=client,
    )

    producer.reconcile(_snapshot(_card()))
    producer.reconcile(_snapshot(_card()))
    stale = producer.reconcile(_snapshot(None))

    assert stale["stale"] == 1
    assert stale["delete_missing"] is False
    assert _row(db)["status"] == "STALE"
    assert not hasattr(client, "delete_document")


def test_completed_document_becomes_blocked_when_bundle_still_exists_but_is_ineligible(tmp_path: Path) -> None:
    module = _module()
    (tmp_path / "Notice.pdf").write_bytes(b"%PDF")
    db = tmp_path / "state.sqlite3"
    client = FakeClient(["completed"])
    producer = module.HindsightProducer(
        roots=[("Affaires", tmp_path)],
        state_db=db,
        client=client,
    )

    producer.reconcile(_snapshot(_card()))
    producer.reconcile(_snapshot(_card()))
    blocked = producer.reconcile(_snapshot(_card(status="CHECK")))

    assert blocked["blocked"] == 1
    assert _row(db)["status"] == "BLOCKED"


def test_candidate_path_must_resolve_inside_exact_workspace_root(tmp_path: Path) -> None:
    module = _module()
    root = tmp_path / "AFFAIRES"
    root.mkdir()
    outside = tmp_path / "escape.pdf"
    outside.write_bytes(b"%PDF")
    db = tmp_path / "state.sqlite3"
    client = FakeClient()
    producer = module.HindsightProducer(
        roots=[("Affaires", root)],
        state_db=db,
        client=client,
    )

    producer.reconcile(_snapshot(_card("../escape.pdf")))
    assert client.retains == []


class _Response:
    def __init__(self, payload: dict) -> None:
        self.payload = json.dumps(payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return self.payload


def test_http_client_matches_hindsight_0101_file_retain_multipart_contract(tmp_path: Path) -> None:
    module = _module()
    source = tmp_path / "Notice.pdf"
    source.write_bytes(b"EXACT-PDF-BYTES")
    captured = {}

    def fake_urlopen(request, timeout):
        captured["request"] = request
        captured["timeout"] = timeout
        return _Response({"operation_ids": ["op-123"]})

    client = module.HindsightHTTPClient(
        "http://127.0.0.1:8888",
        "affaires",
        parser="markitdown",
        timeout_seconds=7,
    )
    with patch.object(module, "urlopen", fake_urlopen):
        operation_id = client.retain_file(
            source,
            document_id="doc-notice:source",
            context="AFFAIRES professional source document",
            tags=["workspace:affaires"],
            metadata={"pantheon_document_id": "doc-notice"},
        )

    assert operation_id == "op-123"
    request = captured["request"]
    assert request.full_url.endswith("/v1/default/banks/affaires/files/retain")
    assert captured["timeout"] == 7
    assert request.get_header("Content-type").startswith("multipart/form-data; boundary=")
    body = request.data
    assert b'name="request"' in body
    assert b'name="files"; filename="Notice.pdf"' in body
    assert b"EXACT-PDF-BYTES" in body
    assert b'"parser":"markitdown"' in body
    assert b'"document_id":"doc-notice:source"' in body
    assert b'"timestamp":"unset"' in body


def test_poll_error_is_persisted_without_resubmitting_active_operation(tmp_path: Path) -> None:
    module = _module()
    (tmp_path / "Notice.pdf").write_bytes(b"%PDF")
    db = tmp_path / "state.sqlite3"

    class PollFailureClient(FakeClient):
        def operation_status(self, operation_id: str):
            self.polls.append(operation_id)
            raise RuntimeError("temporary Hindsight outage")

    client = PollFailureClient()
    producer = module.HindsightProducer(
        roots=[("Affaires", tmp_path)],
        state_db=db,
        client=client,
    )

    producer.reconcile(_snapshot(_card()))
    state = producer.reconcile(_snapshot(_card()))

    assert len(client.retains) == 1
    assert client.polls == ["op-1"]
    assert state["submitted"] == 1
    assert _row(db)["last_error"] == "temporary Hindsight outage"


def test_http_client_rejects_oversize_source_before_buffering_or_network(tmp_path: Path) -> None:
    module = _module()
    source = tmp_path / "Notice.pdf"
    source.write_bytes(b"12345")
    client = module.HindsightHTTPClient(
        "http://127.0.0.1:8888",
        "affaires",
        max_file_bytes=4,
    )

    with patch.object(module, "urlopen") as mocked:
        try:
            client.retain_file(
                source,
                document_id="doc-notice:source",
                context="AFFAIRES professional source document",
                tags=["workspace:affaires"],
                metadata={"pantheon_document_id": "doc-notice"},
            )
        except RuntimeError as exc:
            assert "exceeds Hindsight upload bound" in str(exc)
        else:
            raise AssertionError("oversize source should be rejected")

    mocked.assert_not_called()
