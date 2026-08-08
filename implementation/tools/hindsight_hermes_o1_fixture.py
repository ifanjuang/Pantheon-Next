#!/usr/bin/env python3
"""Deterministic OpenAI-compatible model fixture for the O1 memory lab.

The fixture never impersonates Hindsight. It only makes the model side call the
real `hindsight_recall` tool exposed by Hermes, then verifies that the returned
tool content contains the synthetic marker.
"""

from __future__ import annotations

import argparse
import json
import threading
import time
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit

MARKER = "PANTHEON_O1_SYNTHETIC_MEMORY_MARKER"


def _tool_name(item: Any) -> str:
    if not isinstance(item, dict):
        return ""
    fn = item.get("function")
    return str(fn.get("name") or "") if isinstance(fn, dict) else str(item.get("name") or "")


class State:
    def __init__(self, journal: Path) -> None:
        self.journal = journal
        self.lock = threading.Lock()
        self.calls = 0
        self.recall_tool_seen = False
        self.marker_seen_in_tool_result = False

    def record(self, payload: dict[str, Any]) -> None:
        with self.lock:
            self.journal.parent.mkdir(parents=True, exist_ok=True)
            with self.journal.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps({"at": time.time(), **payload}, sort_keys=True) + "\n")

    def snapshot(self) -> dict[str, Any]:
        with self.lock:
            return {
                "provider_calls": self.calls,
                "recall_tool_seen": self.recall_tool_seen,
                "marker_seen_in_tool_result": self.marker_seen_in_tool_result,
            }


class Handler(BaseHTTPRequestHandler):
    server_version = "PantheonO1Fixture/1"

    @property
    def state(self) -> State:
        return self.server.state  # type: ignore[attr-defined]

    def log_message(self, fmt: str, *args: object) -> None:
        del fmt, args

    def _read_json(self) -> dict[str, Any]:
        size = int(self.headers.get("Content-Length", "0") or "0")
        value = json.loads((self.rfile.read(size) if size else b"{}").decode())
        if not isinstance(value, dict):
            raise ValueError("body must be an object")
        return value

    def _send_json(self, status: int, value: dict[str, Any]) -> None:
        raw = json.dumps(value).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def _send_sse(self, events: Iterable[dict[str, Any]]) -> None:
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Connection", "close")
        self.end_headers()
        for event in events:
            self.wfile.write(("data: " + json.dumps(event) + "\n\n").encode())
        self.wfile.write(b"data: [DONE]\n\n")
        self.wfile.flush()

    def do_GET(self) -> None:  # noqa: N802
        path = urlsplit(self.path).path
        if path == "/health":
            self._send_json(200, {"status": "ok"})
        elif path == "/v1/models":
            self._send_json(200, {"object": "list", "data": [{"id": "o1-lab-model"}]})
        elif path == "/_lab/state":
            self._send_json(200, self.state.snapshot())
        else:
            self._send_json(404, {"error": "not found"})

    def do_POST(self) -> None:  # noqa: N802
        if urlsplit(self.path).path != "/v1/chat/completions":
            self._send_json(404, {"error": "not found"})
            return
        body = self._read_json()
        tools = body.get("tools") if isinstance(body.get("tools"), list) else []
        names = sorted({name for name in map(_tool_name, tools) if name})
        messages = body.get("messages") if isinstance(body.get("messages"), list) else []
        tool_results = [m for m in messages if isinstance(m, dict) and m.get("role") == "tool"]
        with self.state.lock:
            self.state.calls += 1
            self.state.recall_tool_seen = self.state.recall_tool_seen or "hindsight_recall" in names
            self.state.marker_seen_in_tool_result = self.state.marker_seen_in_tool_result or any(
                MARKER in str(m.get("content") or "") for m in tool_results
            )
        self.state.record({"path": "/v1/chat/completions", "tool_names": names, "tool_result_count": len(tool_results)})

        if not tool_results:
            if "hindsight_recall" not in names:
                self._send_json(500, {"error": "hindsight_recall was not exposed by Hermes"})
                return
            response = self._tool_call()
        else:
            ok = any(MARKER in str(m.get("content") or "") for m in tool_results)
            response = self._final(ok)
        self._emit(body, response)

    def _tool_call(self) -> dict[str, Any]:
        return {
            "id": "chatcmpl-o1-tool",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": "o1-lab-model",
            "choices": [{
                "index": 0,
                "message": {"role": "assistant", "content": None, "tool_calls": [{
                    "id": "call-o1-recall",
                    "type": "function",
                    "function": {"name": "hindsight_recall", "arguments": json.dumps({"query": "O1 synthetic memory marker"})},
                }]},
                "finish_reason": "tool_calls",
            }],
            "usage": {"prompt_tokens": 8, "completion_tokens": 4, "total_tokens": 12},
        }

    def _final(self, ok: bool) -> dict[str, Any]:
        text = "O1_HINDSIGHT_RECALL_COMPLETED" if ok else "O1_HINDSIGHT_RECALL_MISSING_MARKER"
        return {
            "id": "chatcmpl-o1-final",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": "o1-lab-model",
            "choices": [{"index": 0, "message": {"role": "assistant", "content": text}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 8, "completion_tokens": 4, "total_tokens": 12},
        }

    def _emit(self, request: dict[str, Any], response: dict[str, Any]) -> None:
        if request.get("stream") is not True:
            self._send_json(200, response)
            return
        choice = response["choices"][0]
        message = choice["message"]
        delta: dict[str, Any] = {"role": "assistant"}
        if message.get("tool_calls"):
            delta["tool_calls"] = [dict(call, index=i) for i, call in enumerate(message["tool_calls"])]
        else:
            delta["content"] = message.get("content") or ""
        base = {"id": response["id"], "object": "chat.completion.chunk", "created": response["created"], "model": response["model"]}
        self._send_sse([
            {**base, "choices": [{"index": 0, "delta": delta, "finish_reason": None}]},
            {**base, "choices": [{"index": 0, "delta": {}, "finish_reason": choice["finish_reason"]}]},
        ])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9020)
    parser.add_argument("--journal", type=Path, required=True)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    server.state = State(args.journal)  # type: ignore[attr-defined]
    server.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
