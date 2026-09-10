"""Marker API wrapper that releases its auto-spawned vLLM container when idle."""

from __future__ import annotations

import asyncio
import json
import logging
import os
import subprocess
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from marker.scripts.server import app, app_data


LOGGER = logging.getLogger("pantheon.marker-idle-vram")
IDLE_SECONDS = max(0, int(os.environ.get("MARKER_GPU_IDLE_SECONDS", "600")))
RELEASE_OLLAMA = os.environ.get("MARKER_RELEASE_OLLAMA", "1") == "1"
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")

_state_lock = asyncio.Lock()
_active_requests = 0
_activity_generation = 0
_release_task: asyncio.Task[None] | None = None


def _inference_manager() -> Any | None:
    models = app_data.get("models")
    if not isinstance(models, dict):
        return None
    return models.get("inference_manager")


def _surya_sentinel() -> Path:
    return Path.home() / ".cache" / "datalab" / "surya" / "vllm_server.json"


def _release_loaded_ollama_models() -> None:
    """Best-effort VRAM hand-off before Marker starts or wakes its VLM."""
    if not RELEASE_OLLAMA:
        return
    try:
        with urllib.request.urlopen(f"{OLLAMA_BASE_URL}/api/ps", timeout=5) as response:
            payload = json.load(response)
        names = [model.get("name") for model in payload.get("models", [])]
        for name in filter(None, names):
            body = json.dumps({"model": name, "keep_alive": 0}).encode("utf-8")
            request = urllib.request.Request(
                f"{OLLAMA_BASE_URL}/api/generate",
                data=body,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(request, timeout=120):
                pass
            LOGGER.info("released Ollama model %s before Marker OCR", name)
    except (OSError, ValueError, urllib.error.URLError) as exc:
        LOGGER.warning("could not release Ollama before Marker OCR: %s", exc)


def _release_marker_vllm() -> None:
    """Stop only the local Surya vLLM container recorded by this Marker user."""
    manager = _inference_manager()
    backend = getattr(manager, "backend", None)
    handle = getattr(backend, "handle", None)
    if handle is None:
        return
    if not getattr(handle, "spawned_by_us", False):
        LOGGER.info("leaving externally managed Surya inference server running")
        return

    sentinel = _surya_sentinel()
    try:
        record = json.loads(sentinel.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        record = {}
    container = record.get("cleanup_id")
    if record.get("cleanup_kind") != "docker" or not isinstance(container, str):
        LOGGER.warning("cannot safely identify Marker's Surya vLLM container")
        return
    if not container.startswith("surya-vllm-") or not container.removeprefix("surya-vllm-").isdigit():
        LOGGER.warning("refusing unexpected Surya container name %r", container)
        return

    result = subprocess.run(
        ["docker", "stop", container],
        check=False,
        capture_output=True,
        text=True,
        timeout=45,
    )
    if result.returncode != 0 and "No such container" not in result.stderr:
        LOGGER.warning("could not stop %s: %s", container, result.stderr.strip())
        return

    try:
        sentinel.unlink(missing_ok=True)
    finally:
        manager.stop()
    LOGGER.info("released Marker vLLM after %s seconds idle", IDLE_SECONDS)


async def _release_after_idle(generation: int) -> None:
    try:
        await asyncio.sleep(IDLE_SECONDS)
        async with _state_lock:
            if _active_requests == 0 and _activity_generation == generation:
                await asyncio.to_thread(_release_marker_vllm)
    except asyncio.CancelledError:
        return


@app.middleware("http")
async def marker_gpu_lifecycle(request, call_next):
    """Serialize GPU ownership changes around Marker conversion requests."""
    global _active_requests, _activity_generation, _release_task

    if request.method != "POST" or request.url.path not in {"/marker", "/marker/upload"}:
        return await call_next(request)

    async with _state_lock:
        _activity_generation += 1
        generation = _activity_generation
        _active_requests += 1
        if _release_task is not None:
            _release_task.cancel()
            _release_task = None
        await asyncio.to_thread(_release_loaded_ollama_models)

    try:
        return await call_next(request)
    finally:
        async with _state_lock:
            _active_requests -= 1
            if _active_requests == 0 and IDLE_SECONDS > 0:
                _release_task = asyncio.create_task(_release_after_idle(generation))
