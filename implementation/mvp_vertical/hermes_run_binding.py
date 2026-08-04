"""Stateless external binding from one Pantheon launch reservation to Hermes Runs API.

This module belongs to the external execution side. It may call Hermes because it
is not Pantheon Next. It owns no queue, scheduler, retry worker, provider router or
background poller. Every launch is an explicit one-shot operation:

    observe reviewed Hermes surface
    -> reserve one admitted launch in Pantheon
    -> POST exactly one /v1/runs request
    -> report the returned run_id to Pantheon

A network ambiguity never triggers an automatic retry. The immutable reservation is
left for operator reconciliation so a second Hermes run cannot be created silently.
"""

from __future__ import annotations

import json
from typing import Any

from .hermes_runs_observer import HermesRunsApiObserver

MAX_RUN_INPUT_CHARS = 140_000
MAX_RUNTIME_OUTPUT_CHARS = 200_000
RUN_INSTRUCTIONS = """You are executing one Pantheon-admitted read-only work item.
Use only the supplied immutable launch context snapshot for the initial task.
Do not widen scope, mutate Agency Data, transmit externally, install or activate
capabilities, promote memory, admit Evidence, or treat runtime success as truth.
Any consequential follow-up requires a separate Pantheon effect gate.
Return candidate material for human/governance review."""


class HermesRunBindingError(RuntimeError):
    pass


class HermesRunBindingNotQualified(HermesRunBindingError):
    pass


class HermesLaunchReplayRequiresReconciliation(HermesRunBindingError):
    pass


class HermesRunSubmissionUnknown(HermesRunBindingError):
    def __init__(self, message: str, *, launch_reservation_id: str):
        super().__init__(message)
        self.launch_reservation_id = launch_reservation_id


class HermesRunRegistrationUnknown(HermesRunBindingError):
    def __init__(self, message: str, *, launch_reservation_id: str, run_id: str):
        super().__init__(message)
        self.launch_reservation_id = launch_reservation_id
        self.run_id = run_id


def _json_response(response: Any, *, surface: str) -> dict[str, Any]:
    try:
        response.raise_for_status()
    except Exception as exc:
        raise HermesRunBindingError(f"{surface} request failed") from exc
    try:
        payload = response.json()
    except Exception as exc:
        raise HermesRunBindingError(f"{surface} response is not valid JSON") from exc
    if not isinstance(payload, dict):
        raise HermesRunBindingError(f"{surface} response must be an object")
    return payload


def _as_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    try:
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    except Exception:
        return str(value)


class PantheonRunBridgeClient:
    """HTTP client for the bounded Pantheon-side reservation/start/return seam."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        actor: str,
        *,
        timeout: float = 10.0,
        client: Any | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._actor = actor.strip()
        self._timeout = timeout
        self._client = client
        if not self._base_url or not self._api_key or not self._actor:
            raise HermesRunBindingError("Pantheon base_url, api_key and actor are required")

    def _request(self, method: str, path: str, *, body: dict[str, Any]) -> dict[str, Any]:
        client = self._client
        owns = client is None
        if owns:
            import httpx
            client = httpx.Client(timeout=self._timeout)
        try:
            response = client.request(
                method,
                self._base_url + path,
                json=body,
                headers={
                    "Authorization": f"Bearer {self._api_key}",
                    "X-Pantheon-Hermes-Actor": self._actor,
                },
                timeout=self._timeout,
            )
            return _json_response(response, surface=f"Pantheon {path}")
        finally:
            if owns:
                client.close()

    def reserve_launch(self, *, admission_id: str, idempotency_key: str) -> dict[str, Any]:
        return self._request(
            "POST",
            f"/hermes/execution-admissions/{admission_id}/launch-reservations",
            body={"idempotency_key": idempotency_key},
        )

    def record_start(
        self,
        *,
        admission_id: str,
        run_id: str,
        expected_issue_version: int,
        launch_reservation_id: str,
        idempotency_key: str,
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            f"/hermes/execution-admissions/{admission_id}/runs/start",
            body={
                "run_id": run_id,
                "expected_issue_version": expected_issue_version,
                "launch_reservation_id": launch_reservation_id,
                "idempotency_key": idempotency_key,
            },
        )

    def record_return(
        self,
        *,
        admission_id: str,
        run_id: str,
        expected_issue_version: int,
        normalized_return: dict[str, Any],
        result_candidate: dict[str, Any] | None,
        idempotency_key: str,
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            f"/hermes/execution-admissions/{admission_id}/runs/{run_id}/return",
            body={
                "normalized_return": normalized_return,
                "result_candidate": result_candidate,
                "expected_issue_version": expected_issue_version,
                "idempotency_key": idempotency_key,
            },
        )


class HermesRunsHttpClient:
    """Minimal reviewed Hermes Runs API client; no provider/model/memory headers."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        *,
        timeout: float = 15.0,
        client: Any | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._timeout = timeout
        self._client = client
        if not self._base_url or not self._api_key:
            raise HermesRunBindingError("Hermes base_url and api_key are required")

    def _request(self, method: str, path: str, *, body: dict[str, Any] | None = None) -> dict[str, Any]:
        client = self._client
        owns = client is None
        if owns:
            import httpx
            client = httpx.Client(timeout=self._timeout)
        try:
            response = client.request(
                method,
                self._base_url + path,
                json=body,
                headers={"Authorization": f"Bearer {self._api_key}"},
                timeout=self._timeout,
            )
            return _json_response(response, surface=f"Hermes {path}")
        finally:
            if owns:
                client.close()

    def submit(self, *, input_text: str, session_id: str) -> dict[str, Any]:
        return self._request(
            "POST",
            "/v1/runs",
            body={
                "input": input_text,
                "session_id": session_id,
                "instructions": RUN_INSTRUCTIONS,
            },
        )

    def get_status(self, run_id: str) -> dict[str, Any]:
        return self._request("GET", f"/v1/runs/{run_id}")


class ExternalHermesRunBinding:
    """One-shot junction between a governed admission and the external Hermes run."""

    def __init__(
        self,
        *,
        observer: HermesRunsApiObserver,
        pantheon: PantheonRunBridgeClient,
        hermes: HermesRunsHttpClient,
    ) -> None:
        self._observer = observer
        self._pantheon = pantheon
        self._hermes = hermes

    def launch(self, *, admission_id: str, idempotency_key: str) -> dict[str, Any]:
        observation = self._observer.observe()
        if observation.get("runs_api_status") != "compatible":
            raise HermesRunBindingNotQualified("Hermes Runs API is not compatible")
        if observation.get("safety_status") != "qualified":
            raise HermesRunBindingNotQualified(
                "Hermes governed runtime posture is not qualified: "
                f"{observation.get('safety_status')}"
            )

        reservation = self._pantheon.reserve_launch(
            admission_id=admission_id,
            idempotency_key=f"{idempotency_key}:reserve",
        )
        reservation_id = str(reservation.get("launch_reservation_id") or "")
        if not reservation_id:
            raise HermesRunBindingError("Pantheon launch reservation is missing its identity")
        if reservation.get("replayed") is True:
            raise HermesLaunchReplayRequiresReconciliation(
                "launch reservation replayed; automatic Hermes submission retry is forbidden"
            )

        snapshot = reservation.get("snapshot")
        if not isinstance(snapshot, dict):
            raise HermesRunBindingError("Pantheon launch reservation is missing its snapshot")
        input_text = json.dumps(
            {
                "pantheon_launch": {
                    "admission_id": admission_id,
                    "launch_reservation_id": reservation_id,
                    "snapshot_digest": reservation.get("snapshot_digest"),
                    "governance_note": "This immutable snapshot bootstraps one read-only admitted run.",
                },
                "launch_context_snapshot": snapshot,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
        if len(input_text) > MAX_RUN_INPUT_CHARS:
            raise HermesRunBindingError(
                f"Hermes run input exceeds {MAX_RUN_INPUT_CHARS} characters"
            )

        try:
            submitted = self._hermes.submit(input_text=input_text, session_id=admission_id)
        except Exception as exc:
            raise HermesRunSubmissionUnknown(
                "Hermes run submission outcome is unknown; do not retry automatically",
                launch_reservation_id=reservation_id,
            ) from exc

        run_id = str(submitted.get("run_id") or "").strip()
        if not run_id:
            raise HermesRunSubmissionUnknown(
                "Hermes accepted the request without a usable run_id; do not retry automatically",
                launch_reservation_id=reservation_id,
            )

        try:
            started = self._pantheon.record_start(
                admission_id=admission_id,
                run_id=run_id,
                expected_issue_version=int(reservation["work_issue_version"]),
                launch_reservation_id=reservation_id,
                idempotency_key=f"{idempotency_key}:start",
            )
        except Exception as exc:
            raise HermesRunRegistrationUnknown(
                "Hermes returned a run_id but Pantheon start registration failed; reconcile explicitly",
                launch_reservation_id=reservation_id,
                run_id=run_id,
            ) from exc

        work_issue = started.get("work_issue") or {}
        return {
            "kind": "external_hermes_run_launch_receipt",
            "admission_id": admission_id,
            "launch_reservation_id": reservation_id,
            "snapshot_id": reservation.get("snapshot_id"),
            "snapshot_digest": reservation.get("snapshot_digest"),
            "run_id": run_id,
            "hermes_submission_status": submitted.get("status"),
            "runtime_start_recorded": started.get("runtime_start_recorded") is True,
            "return_expected_issue_version": work_issue.get("version"),
            "session_id": admission_id,
            "session_memory_header_sent": False,
            "runtime_submission_performed": True,
            "automatic_retry_performed": False,
            "provider_routing_performed": False,
            "model_override_performed": False,
            "technical_receipt_is_evidence": False,
            "observation": observation,
            "non_equivalences": [
                "launch reservation != dispatch",
                "runtime submission != Evidence",
                "Hermes run started != task success",
                "session_id correlation != memory promotion",
                "session_id correlation != X-Hermes-Session-Key",
                "qualified runtime posture != task authorization",
                "qualified tool surface != production activation",
            ],
        }

    def reconcile_once(
        self,
        *,
        launch_receipt: dict[str, Any],
        idempotency_key: str,
    ) -> dict[str, Any]:
        """Observe one run once and record a terminal return when safely mappable.

        This is not a poll loop. ``cancelled`` is deliberately not mapped to the
        current normalized return vocabulary; it remains an observed runtime state.
        """
        admission_id = str(launch_receipt.get("admission_id") or "")
        run_id = str(launch_receipt.get("run_id") or "")
        expected_version = launch_receipt.get("return_expected_issue_version")
        if not admission_id or not run_id or not isinstance(expected_version, int):
            raise HermesRunBindingError("launch receipt is incomplete for reconciliation")

        status = self._hermes.get_status(run_id)
        runtime_status = str(status.get("status") or "").strip().lower()
        if runtime_status in {"started", "running", "stopping", "pending"}:
            return {
                "kind": "hermes_run_reconciliation",
                "run_id": run_id,
                "runtime_status": runtime_status,
                "pantheon_return_recorded": False,
                "scheduler_effect": False,
                "retry_effect": False,
            }
        if runtime_status == "cancelled":
            return {
                "kind": "hermes_run_reconciliation",
                "run_id": run_id,
                "runtime_status": runtime_status,
                "pantheon_return_recorded": False,
                "reason": "cancelled has no normalized Work Issue return mapping in this slice",
                "scheduler_effect": False,
                "retry_effect": False,
            }

        trace_refs = [f"hermes://runs/{run_id}"]
        result_candidate: dict[str, Any] | None = None
        if runtime_status == "completed":
            output = _as_text(status.get("output") or "")
            if len(output) > MAX_RUNTIME_OUTPUT_CHARS:
                raise HermesRunBindingError(
                    f"Hermes runtime output exceeds {MAX_RUNTIME_OUTPUT_CHARS} characters"
                )
            summary = output.strip() or "Hermes run completed without textual output."
            summary = summary[:20_000]
            normalized = {
                "outcome": "result_candidate",
                "summary": summary,
                "trace_refs": trace_refs,
                "result_refs": [],
                "evidence_candidate_refs": [],
            }
            result_candidate = {
                "result_type": "hermes_run_output",
                "candidate_payload": {
                    "output": output,
                    "runtime_status": runtime_status,
                },
                "confidence_note": None,
                "known_limits": [
                    "Runtime output has not been admitted as Evidence or canonical truth."
                ],
                "open_questions": [],
                "source_refs": [],
                "missing_evidence": [],
            }
        elif runtime_status == "failed":
            detail = _as_text(status.get("error") or status.get("output") or "Hermes run failed.")
            normalized = {
                "outcome": "failed",
                "summary": detail[:20_000] or "Hermes run failed.",
                "trace_refs": trace_refs,
                "result_refs": [],
                "evidence_candidate_refs": [],
            }
        else:
            return {
                "kind": "hermes_run_reconciliation",
                "run_id": run_id,
                "runtime_status": runtime_status or "unknown",
                "pantheon_return_recorded": False,
                "reason": "runtime status is not mapped by this first reconciliation slice",
                "scheduler_effect": False,
                "retry_effect": False,
            }

        recorded = self._pantheon.record_return(
            admission_id=admission_id,
            run_id=run_id,
            expected_issue_version=expected_version,
            normalized_return=normalized,
            result_candidate=result_candidate,
            idempotency_key=f"{idempotency_key}:return",
        )
        return {
            "kind": "hermes_run_reconciliation",
            "run_id": run_id,
            "runtime_status": runtime_status,
            "pantheon_return_recorded": True,
            "recorded": recorded,
            "scheduler_effect": False,
            "retry_effect": False,
            "technical_receipt_is_evidence": False,
        }
