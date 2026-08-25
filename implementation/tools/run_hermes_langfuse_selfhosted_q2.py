#!/usr/bin/env python3
"""Bounded real-ingestion probe for Hermes -> self-hosted Langfuse.

Synthetic data only. The active capture mode is metadata; content markers must
not appear in the Langfuse public API responses.
"""
from __future__ import annotations

import importlib
import json
import os
import sys
import time
from pathlib import Path

import requests

BASE_URL = os.environ.get("HERMES_LANGFUSE_BASE_URL", "http://127.0.0.1:3000").rstrip("/")
PUBLIC_KEY = os.environ["HERMES_LANGFUSE_PUBLIC_KEY"]
SECRET_KEY = os.environ["HERMES_LANGFUSE_SECRET_KEY"]
HERMES_ROOT = Path(os.environ["HERMES_ROOT"]).resolve()

PROMPT_MARKER = "PANTHEON_Q2_PROMPT_MUST_NOT_BE_STORED"
TOOL_ARG_MARKER = "PANTHEON_Q2_TOOL_ARG_MUST_NOT_BE_STORED"
TOOL_RESULT_MARKER = "PANTHEON_Q2_TOOL_RESULT_MUST_NOT_BE_STORED"
FINAL_MARKER = "PANTHEON_Q2_FINAL_MUST_NOT_BE_STORED"

os.environ["HERMES_LANGFUSE_CAPTURE"] = "metadata"
os.environ["HERMES_LANGFUSE_ENV"] = "pantheon-q2"
os.environ["HERMES_LANGFUSE_RELEASE"] = "synthetic-q2"
os.environ["HERMES_LANGFUSE_SAMPLE_RATE"] = "1.0"

sys.path.insert(0, str(HERMES_ROOT))
mod_name = "plugins.observability.langfuse"
sys.modules.pop(mod_name, None)
plugin = importlib.import_module(mod_name)

client = plugin._get_langfuse()
assert client is not None, "Langfuse client did not initialize"
assert plugin._capture_mode() == "metadata"

auth = (PUBLIC_KEY, SECRET_KEY)
preflight = requests.get(f"{BASE_URL}/api/public/traces?limit=1", auth=auth, timeout=10)
assert preflight.status_code == 200, (
    f"Langfuse initialized project keys are not valid for public API readback: "
    f"status={preflight.status_code} body={preflight.text[:500]}"
)

common = {
    "task_id": "pantheon-langfuse-q2-task",
    "session_id": "pantheon-langfuse-q2-session",
    "turn_id": "pantheon-langfuse-q2-turn",
    "platform": "pantheon-q2",
    "provider": "synthetic",
    "model": "synthetic-model",
    "base_url": "synthetic://provider",
    "api_mode": "chat_completions",
}

# Current Hermes request lifecycle: pre_api_request is routed to
# on_pre_llm_request, which creates the root trace + generation. The first
# synthetic model response requests a tool, keeping the turn trace open.
plugin.on_pre_llm_request(
    **common,
    api_call_count=1,
    api_request_id="pantheon-q2-request-1",
    request_messages=[{"role": "user", "content": PROMPT_MARKER}],
    message_count=1,
    tool_count=1,
    approx_input_tokens=12,
    request_char_count=len(PROMPT_MARKER),
)
plugin.on_post_llm_call(
    **common,
    api_call_count=1,
    api_request_id="pantheon-q2-request-1",
    assistant_tool_call_count=1,
    assistant_content_chars=0,
    usage={"input_tokens": 12, "output_tokens": 3, "request_count": 1},
    finish_reason="tool_calls",
)

# One real tool observation through the same turn-scoped plugin state.
plugin.on_pre_tool_call(
    **common,
    tool_name="read_file",
    tool_call_id="pantheon-q2-tool-call",
    args={"path": "synthetic.md", "marker": TOOL_ARG_MARKER},
)
plugin.on_post_tool_call(
    **common,
    tool_name="read_file",
    tool_call_id="pantheon-q2-tool-call",
    args={"path": "synthetic.md", "marker": TOOL_ARG_MARKER},
    result=TOOL_RESULT_MARKER,
)

# Second model call completes the same turn. A non-empty assistant response
# with no tool calls drives _finish_trace(), which ends and flushes the root.
plugin.on_pre_llm_request(
    **common,
    api_call_count=2,
    api_request_id="pantheon-q2-request-2",
    request_messages=[
        {"role": "user", "content": PROMPT_MARKER},
        {"role": "tool", "name": "read_file", "tool_call_id": "pantheon-q2-tool-call", "content": TOOL_RESULT_MARKER},
    ],
    message_count=2,
    tool_count=1,
    approx_input_tokens=18,
    request_char_count=len(PROMPT_MARKER) + len(TOOL_RESULT_MARKER),
)
plugin.on_post_llm_call(
    **common,
    api_call_count=2,
    api_request_id="pantheon-q2-request-2",
    assistant_response=FINAL_MARKER,
    assistant_tool_call_count=0,
    usage={"input_tokens": 18, "output_tokens": 5, "request_count": 1},
    finish_reason="stop",
)

# Defensive finalization + synchronous SDK flush; normally the second post
# hook has already closed the trace.
plugin._finalize_all_traces()
client.flush()

# Langfuse ingestion is asynchronous; poll the public APIs until the trace is visible.
traces_payload = None
observations_payload = None
last_trace_status = None
last_trace_body = ""
last_obs_status = None
last_obs_body = ""
for _ in range(60):
    traces = requests.get(f"{BASE_URL}/api/public/traces?limit=100", auth=auth, timeout=10)
    last_trace_status = traces.status_code
    last_trace_body = traces.text[:1000]
    if traces.status_code == 200:
        payload = traces.json()
        data = payload.get("data", []) if isinstance(payload, dict) else []
        if data:
            traces_payload = payload
            obs = requests.get(f"{BASE_URL}/api/public/v2/observations?limit=100", auth=auth, timeout=10)
            last_obs_status = obs.status_code
            last_obs_body = obs.text[:1000]
            if obs.status_code == 200:
                observations_payload = obs.json()
                if observations_payload.get("data", []):
                    break
    time.sleep(1)

assert traces_payload is not None, (
    "No Langfuse trace became visible through the public API; "
    f"last_status={last_trace_status} body={last_trace_body}"
)
assert observations_payload is not None, (
    "No Langfuse observations response became available; "
    f"last_status={last_obs_status} body={last_obs_body}"
)

serialized = json.dumps(
    {"traces": traces_payload, "observations": observations_payload},
    sort_keys=True,
)
for marker in (PROMPT_MARKER, TOOL_ARG_MARKER, TOOL_RESULT_MARKER, FINAL_MARKER):
    assert marker not in serialized, f"metadata mode leaked content marker: {marker}"

trace_data = traces_payload.get("data", [])
obs_data = observations_payload.get("data", [])
assert trace_data, "Trace list is empty"
assert obs_data, "Observation list is empty"

result = {
    "kind": "hermes_langfuse_selfhosted_q2_acceptance",
    "status": "passed",
    "capture_mode": "metadata",
    "real_server_ingestion": True,
    "trace_count_observed": len(trace_data),
    "observation_count_observed": len(obs_data),
    "content_markers_stored": False,
    "langfuse_is_authority": False,
    "evidence_admitted": False,
    "pantheon_state_mutated": False,
}
print(json.dumps(result, indent=2, sort_keys=True))
