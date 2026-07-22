"""Transport-neutral application facade for Pantheon policy projections.

The service owns no runtime state and performs no external effect.  MCP and HTTP
adapters call this facade so policy meaning is implemented once.  Every result
is data for a runtime enforcement point and, where consequential, a human gate.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

import yaml
from jsonschema import Draft202012Validator

from . import (
    apu,
    backup,
    consultation,
    contracts,
    doctor,
    exposure,
    install,
    observability,
    passports,
    policy,
    presets,
    source_map,
    update,
)
from .repo import find_repo_root, read_repo_text

POLICY_CONTRACT = "pantheon.policy.v1"


def _canonical_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _git_dir(root: Path) -> Path | None:
    marker = root / ".git"
    if marker.is_dir():
        return marker
    if marker.is_file():
        line = marker.read_text(encoding="utf-8").strip()
        if line.startswith("gitdir:"):
            target = Path(line.removeprefix("gitdir:").strip())
            return target if target.is_absolute() else (root / target).resolve()
    return None


def repository_commit(root: Path | None = None) -> str:
    """Return the checked-out commit without invoking git or writing state."""
    override = os.getenv("PANTHEON_REPO_COMMIT", "").strip()
    if override:
        return override

    root = root or find_repo_root()
    git_dir = _git_dir(root)
    if git_dir is None:
        return "unknown"
    try:
        head = (git_dir / "HEAD").read_text(encoding="utf-8").strip()
    except OSError:
        return "unknown"
    if not head.startswith("ref:"):
        return head or "unknown"

    ref = head.removeprefix("ref:").strip()
    try:
        return (git_dir / ref).read_text(encoding="utf-8").strip() or "unknown"
    except OSError:
        pass

    try:
        packed = (git_dir / "packed-refs").read_text(encoding="utf-8")
    except OSError:
        return "unknown"
    for line in packed.splitlines():
        if not line or line.startswith(("#", "^")):
            continue
        sha, _, candidate_ref = line.partition(" ")
        if candidate_ref == ref:
            return sha
    return "unknown"


def _approval_rank(value: str | None) -> int:
    if not isinstance(value, str) or len(value) != 2 or not value.startswith("C"):
        return -1
    try:
        return int(value[1])
    except ValueError:
        return -1


class PantheonPolicyService:
    """Single read-only facade shared by MCP and HTTP transports."""

    def __init__(self, root: Path | None = None):
        self.root = root or find_repo_root()

    def _project(
        self,
        operation: str,
        payload: dict[str, Any],
        *,
        source_mode: str,
        input_value: Any | None = None,
    ) -> dict[str, Any]:
        result = dict(payload)
        result.setdefault("contract", POLICY_CONTRACT)
        result.setdefault("operation", operation)
        result.setdefault("source_mode", source_mode)
        result.setdefault("authority_effect", "none")
        result.setdefault("authorization_effect", "none")
        result.setdefault("write_effect", False)
        result.setdefault("execution_effect", False)
        result.setdefault("evaluated_at", datetime.now(timezone.utc).isoformat())
        result.setdefault(
            "repository",
            {
                "version": source_map.repository_version(self.root),
                "commit": repository_commit(self.root),
            },
        )
        if input_value is not None:
            result.setdefault("input_sha256", _canonical_sha256(input_value))
        return result

    def meta(self) -> dict[str, Any]:
        return self._project(
            "meta.read",
            {
                "result": "described",
                "service": "pantheon-policy-api",
                "mode": "read_only",
                "implemented_surfaces": [
                    "consultation",
                    "policy_classification",
                    "policy_preflight",
                    "candidate_preparation",
                    "governance_validation",
                    "provided_evidence_verification",
                    "context_pack_planning_and_validation",
                ],
                "non_equivalences": consultation.NON_EQUIVALENCES,
            },
            source_mode="repository_and_implementation_status",
        )

    def repository_state(self) -> dict[str, Any]:
        return self._project(
            "repository.state.read",
            {
                "result": "observed_read_only",
                "repository_accessible": True,
                "declared_version": source_map.repository_version(self.root),
                "checked_out_commit": repository_commit(self.root),
                "repo_path": str(self.root),
                "runtime_probe_performed": False,
                "limits": [
                    "Repository state is not runtime health.",
                    "A readable checkout is not an approved or safe capability.",
                ],
            },
            source_mode="local_read_only_checkout",
        )

    def consultation_catalog(self) -> dict[str, Any]:
        return self._project(
            "consultation.catalog",
            consultation.consultation_catalog(),
            source_mode="repository_and_implementation_status",
        )

    def list_sources(self) -> dict[str, Any]:
        return self._project(
            "sources.list",
            source_map.list_sources(),
            source_mode="governed_repository_sources",
        )

    def read_doctrine(self, key: str) -> dict[str, Any]:
        return self._project(
            "sources.read",
            source_map.read_source(key),
            source_mode="governed_repository_source",
            input_value={"key": key},
        )

    def explain_governance_structure(self, source_key: str = "") -> dict[str, Any]:
        return self._project(
            "governance.structure.explain",
            source_map.explain_structure(source_key),
            source_mode="governed_repository_sources",
            input_value={"source_key": source_key},
        )

    def explain_architecture(self, topic: str) -> dict[str, Any]:
        return self._project(
            "architecture.explain",
            consultation.explain_architecture(topic),
            source_mode="governed_sources_and_bounded_projection",
            input_value={"topic": topic},
        )

    def qualify_capability_status(self, candidate: dict[str, Any]) -> dict[str, Any]:
        return self._project(
            "capability_status.qualify",
            consultation.qualify_capability_status(candidate),
            source_mode="provided_status_candidate",
            input_value=candidate,
        )

    def classify_request(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._project(
            "policy.request.classify",
            policy.classify_request(request),
            source_mode="provided_request_candidate_and_governed_policy",
            input_value=request,
        )

    def evaluate_preflight(self, candidate: dict[str, Any]) -> dict[str, Any]:
        """Evaluate whether candidate work may proceed and which gates remain.

        The V0 service never authorizes an external or canonical effect.  Gate
        references are caller-provided signals, not authenticated decisions.
        """
        request = candidate.get("request")
        if not isinstance(request, dict):
            request = {
                key: value
                for key, value in candidate.items()
                if key not in {"gate_signals", "request"}
            }
        gate_signals = candidate.get("gate_signals")
        gate_signals = gate_signals if isinstance(gate_signals, dict) else {}
        classification = policy.classify_request(request)

        missing: list[str] = []
        scope = request.get("scope") if isinstance(request.get("scope"), dict) else {}
        if not scope.get("scope_type") or not scope.get("scope_id"):
            missing.append("declared_scope")
        if classification.get("task_contract_required") and not gate_signals.get(
            "task_contract_ref"
        ):
            missing.append("reviewed_task_contract_ref")
        if classification.get("evidence_required") and not gate_signals.get(
            "evidence_pack_candidate_ref"
        ):
            missing.append("evidence_pack_candidate_ref")
        if classification.get("blocked_until_gate") and not gate_signals.get(
            "human_decision_ref"
        ):
            missing.append("human_decision_ref")

        required_ceiling = classification.get("required_approval_ceiling")
        provided_level = gate_signals.get("human_decision_level")
        if gate_signals.get("human_decision_ref") and _approval_rank(provided_level) < _approval_rank(
            required_ceiling
        ):
            missing.append("human_decision_level_at_required_ceiling")

        if classification.get("result") == "refused":
            disposition = "blocked_invalid_request"
        elif "declared_scope" in missing:
            disposition = "blocked_pending_scope"
        elif "reviewed_task_contract_ref" in missing:
            disposition = "blocked_pending_task_contract"
        elif "evidence_pack_candidate_ref" in missing:
            disposition = "blocked_pending_evidence"
        elif any(item.startswith("human_decision") for item in missing):
            disposition = "blocked_pending_human_decision"
        elif classification.get("consequence_level") in {"K3", "K4"}:
            disposition = "eligible_with_gate_signals_unverified"
        else:
            disposition = "eligible_for_candidate_work"

        candidate_work_allowed = disposition in {
            "eligible_for_candidate_work",
            "eligible_with_gate_signals_unverified",
        }
        response = {
            "result": "evaluated",
            "policy_disposition": disposition,
            "candidate_work_allowed": candidate_work_allowed,
            "external_effect_allowed": False,
            "canonical_effect_allowed": False,
            "classification": classification,
            "missing_requirements": missing,
            "provided_gate_signals": {
                key: gate_signals.get(key)
                for key in (
                    "task_contract_ref",
                    "evidence_pack_candidate_ref",
                    "human_decision_ref",
                    "human_decision_level",
                )
                if key in gate_signals
            },
            "gate_signal_validation_performed": False,
            "runtime_enforcement": (
                "must_block_external_and_canonical_effects"
                if classification.get("consequence_level") in {"K3", "K4"}
                else "candidate_work_only"
            ),
            "next_human_decision": (
                "review the listed missing requirements"
                if missing
                else "review any consequential effect outside this service"
            ),
            "limits": [
                "A provided reference is not authenticated evidence or approval.",
                "This service does not execute, send, write, approve or promote memory.",
            ],
        }
        return self._project(
            "policy.preflight.evaluate",
            response,
            source_mode="provided_request_and_gate_signals",
            input_value=candidate,
        )

    def prepare_task_contract(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._project(
            "candidate.task_contract.prepare",
            contracts.prepare_task_contract_skeleton(request),
            source_mode="provided_request_candidate_and_governed_policy",
            input_value=request,
        )

    def prepare_evidence_pack(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._project(
            "candidate.evidence_pack.prepare",
            contracts.prepare_evidence_pack_skeleton(request),
            source_mode="provided_request_candidate_and_governed_policy",
            input_value=request,
        )

    def check_external_action(self, description: str) -> dict[str, Any]:
        return self._project(
            "policy.external_action.check",
            policy.check_external_action(description),
            source_mode="provided_action_description_and_governed_policy",
            input_value={"description": description},
        )

    def validate_passport(self, candidate: dict[str, Any]) -> dict[str, Any]:
        return self._project(
            "validation.capability_passport",
            passports.validate_passport(candidate),
            source_mode="provided_candidate_and_governance_template",
            input_value=candidate,
        )

    def validate_apu_dossier(self, candidate: dict[str, Any]) -> dict[str, Any]:
        return self._project(
            "validation.apu_dossier",
            apu.validate_apu_dossier(candidate),
            source_mode="provided_candidate_and_governance_schemas",
            input_value=candidate,
        )

    def _verify(
        self,
        operation: str,
        verifier: Callable[[dict[str, Any]], dict[str, Any]],
        evidence: dict[str, Any],
    ) -> dict[str, Any]:
        return self._project(
            operation,
            verifier(evidence),
            source_mode="provided_evidence_candidate",
            input_value=evidence,
        )

    def verify_install(self, evidence: dict[str, Any]) -> dict[str, Any]:
        return self._verify("verification.install", install.verify_install, evidence)

    def verify_observability(self, evidence: dict[str, Any]) -> dict[str, Any]:
        return self._verify(
            "verification.observability", observability.verify_observability, evidence
        )

    def verify_backup(self, evidence: dict[str, Any]) -> dict[str, Any]:
        return self._verify("verification.backup", backup.verify_backup, evidence)

    def verify_exposure(self, evidence: dict[str, Any]) -> dict[str, Any]:
        return self._verify("verification.exposure", exposure.verify_exposure, evidence)

    def verify_update(self, evidence: dict[str, Any]) -> dict[str, Any]:
        return self._verify("verification.update", update.verify_update, evidence)

    def load_verification_preset(self, candidate: dict[str, Any]) -> dict[str, Any]:
        return self._project(
            "verification.preset.load",
            presets.load_verification_preset(candidate),
            source_mode="provided_verification_preset_candidate",
            input_value=candidate,
        )

    def run_doctor(self) -> dict[str, Any]:
        return self._project(
            "governance.doctor.run",
            doctor.run_all(),
            source_mode="local_read_only_checkout",
        )

    def plan_context_pack(self, request: dict[str, Any]) -> dict[str, Any]:
        required = ["purpose", "scope", "target_surface", "included_doctrine"]
        missing = [field for field in required if not request.get(field)]
        return self._project(
            "context_pack.plan",
            {
                "result": "invalid" if missing else "candidate_plan",
                "object": "CONTEXT_PACK_PLAN_CANDIDATE",
                "missing_requirements": missing,
                "submitted_scope": request.get("scope"),
                "target_surface": request.get("target_surface"),
                "included_doctrine": request.get("included_doctrine", []),
                "producer_responsibility": [
                    "collect only explicitly scoped context",
                    "preserve source references and status",
                    "exclude cross-project material",
                    "submit the assembled pack for schema validation",
                ],
                "pantheon_responsibility": [
                    "state boundaries and required fields",
                    "validate the assembled candidate",
                    "report gaps without retrieving private context",
                ],
                "forbidden": [
                    "implicit context collection",
                    "runtime execution",
                    "memory promotion",
                    "treating the pack as evidence or approval",
                ],
            },
            source_mode="provided_context_pack_plan_request",
            input_value=request,
        )

    def validate_context_pack(self, candidate: dict[str, Any]) -> dict[str, Any]:
        schema = yaml.safe_load(read_repo_text("schemas/context_pack.schema.yaml", self.root))
        validator = Draft202012Validator(schema)
        problems = [
            {
                "path": ".".join(str(part) for part in error.absolute_path),
                "message": error.message,
            }
            for error in sorted(validator.iter_errors(candidate), key=lambda item: list(item.path))
        ]
        return self._project(
            "context_pack.validate",
            {
                "result": "invalid" if problems else "valid_candidate",
                "valid": not problems,
                "problems": problems,
                "canonical_effect": False,
                "approval_effect": "none",
                "retrieval_performed": False,
                "limits": [
                    "Schema validity is not authorization, evidence or approved memory.",
                    "The service validates only the caller-provided candidate.",
                ],
            },
            source_mode="provided_context_pack_candidate_and_governance_schema",
            input_value=candidate,
        )
