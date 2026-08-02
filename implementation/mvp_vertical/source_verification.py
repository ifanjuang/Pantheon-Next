"""Deterministic contract for source-aligned document verification observations.

A verification report compares one exact structured compilation with one exact
source version. It records candidate mismatch observations only; it does not
establish truth, Evidence, professional validation or authorization.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Any


VERIFICATION_STATUSES = {
    "not_observed",
    "no_mismatch_observed",
    "mismatch_observed",
    "inconclusive",
    "review_required",
}

OBSERVATION_KINDS = {
    "missing_page",
    "missing_region",
    "changed_number",
    "changed_symbol",
    "changed_unit",
    "corrupted_table",
    "altered_equation",
    "incorrect_reading_order",
    "empty_section",
    "double_ocr_degradation",
    "other",
}

SEVERITIES = {"notice", "warning", "blocking"}


def _require_text(name: str, value: str) -> str:
    normalized = str(value or "").strip()
    if not normalized:
        raise ValueError(f"{name} is required")
    return normalized


def _digest(payload: Any) -> str:
    canonical = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class SourceVerificationObservation:
    kind: str
    severity: str
    source_locator: str
    derivative_locator: str
    message: str
    expected_digest: str | None = None
    observed_digest: str | None = None

    def __post_init__(self) -> None:
        if self.kind not in OBSERVATION_KINDS:
            raise ValueError(f"unsupported observation kind: {self.kind}")
        if self.severity not in SEVERITIES:
            raise ValueError(f"unsupported observation severity: {self.severity}")
        object.__setattr__(self, "source_locator", _require_text("source_locator", self.source_locator))
        object.__setattr__(
            self,
            "derivative_locator",
            _require_text("derivative_locator", self.derivative_locator),
        )
        object.__setattr__(self, "message", _require_text("message", self.message))

    def as_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "severity": self.severity,
            "source_locator": self.source_locator,
            "derivative_locator": self.derivative_locator,
            "message": self.message,
            "expected_digest": self.expected_digest,
            "observed_digest": self.observed_digest,
        }


@dataclass(frozen=True)
class SourceVerificationReport:
    source_version_id: str
    source_digest: str
    compilation_id: str
    compilation_output_digest: str
    binding_id: str
    binding_version: str
    execution_id: str
    parameters_profile: str
    coverage_complete: bool
    observations: tuple[SourceVerificationObservation, ...] = ()
    inconclusive_reasons: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for field in (
            "source_version_id",
            "source_digest",
            "compilation_id",
            "compilation_output_digest",
            "binding_id",
            "binding_version",
            "execution_id",
            "parameters_profile",
        ):
            object.__setattr__(self, field, _require_text(field, getattr(self, field)))
        if not isinstance(self.coverage_complete, bool):
            raise ValueError("coverage_complete must be a boolean observation")
        observations = tuple(self.observations)
        if any(not isinstance(item, SourceVerificationObservation) for item in observations):
            raise ValueError("observations must contain SourceVerificationObservation values")
        object.__setattr__(self, "observations", observations)
        object.__setattr__(
            self,
            "inconclusive_reasons",
            tuple(dict.fromkeys(_require_text("inconclusive_reason", reason) for reason in self.inconclusive_reasons)),
        )

    @property
    def status(self) -> str:
        if any(item.severity == "blocking" for item in self.observations):
            return "review_required"
        if self.inconclusive_reasons or not self.coverage_complete:
            return "inconclusive"
        if self.observations:
            return "mismatch_observed"
        return "no_mismatch_observed"

    @property
    def report_id(self) -> str:
        identity = {
            "source_version_id": self.source_version_id,
            "source_digest": self.source_digest,
            "compilation_id": self.compilation_id,
            "compilation_output_digest": self.compilation_output_digest,
            "binding_id": self.binding_id,
            "binding_version": self.binding_version,
            "execution_id": self.execution_id,
            "parameters_profile": self.parameters_profile,
            "coverage_complete": self.coverage_complete,
            "observations": [item.as_dict() for item in self.observations],
            "inconclusive_reasons": self.inconclusive_reasons,
        }
        return f"svr-{_digest(identity)[:24]}"

    def as_dict(self) -> dict[str, Any]:
        status = self.status
        if status not in VERIFICATION_STATUSES:
            raise AssertionError(f"invalid derived verification status: {status}")
        return {
            "report_id": self.report_id,
            "source_version_id": self.source_version_id,
            "source_digest": self.source_digest,
            "compilation_id": self.compilation_id,
            "compilation_output_digest": self.compilation_output_digest,
            "produced_by": {
                "binding_id": self.binding_id,
                "binding_version": self.binding_version,
                "execution_id": self.execution_id,
                "parameters_profile": self.parameters_profile,
            },
            "coverage_complete": self.coverage_complete,
            "status": status,
            "observations": [item.as_dict() for item in self.observations],
            "inconclusive_reasons": list(self.inconclusive_reasons),
            "authority": {
                "is_source_truth": False,
                "is_evidence": False,
                "is_professional_validation": False,
            },
        }


def not_observed_verification() -> dict[str, Any]:
    """Return the explicit projection used before any verification run exists."""
    return {
        "status": "not_observed",
        "report_id": None,
        "coverage_complete": False,
        "observation_count": 0,
        "authority": {
            "is_source_truth": False,
            "is_evidence": False,
            "is_professional_validation": False,
        },
    }
