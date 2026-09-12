"""Read-only capture and qualification of Hermes presentation configuration.

This module observes only resolved configuration values exposed by the official
``hermes config get <key> --json`` command. It does not inspect or retain model
reasoning, does not prove what a user-facing surface rendered, and performs no
configuration write.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from typing import Any, Callable, Iterable


MAX_PRESENTATION_OBSERVATION_AGE_SECONDS = 300.0
MAX_FUTURE_CLOCK_SKEW_SECONDS = 30.0
_PROFILE_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
_PLATFORM_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
_DIGEST_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")

_GLOBAL_KEYS = {
    "show_reasoning": "display.show_reasoning",
    "show_commentary": "display.show_commentary",
    "interim_assistant_messages": "display.interim_assistant_messages",
    "stream_reasoning_deltas": "plugins.stream_reasoning_deltas",
}


class HermesPresentationObservationError(ValueError):
    pass


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _normalize_name(value: str, *, label: str, pattern: re.Pattern[str]) -> str:
    normalized = str(value or "").strip()
    if not normalized or not pattern.fullmatch(normalized):
        raise HermesPresentationObservationError(
            f"Hermes {label} must contain only letters, numbers, hyphens or underscores"
        )
    return normalized


def normalize_profile_name(value: str) -> str:
    return _normalize_name(value, label="profile", pattern=_PROFILE_PATTERN)


def normalize_platform_name(value: str) -> str:
    return _normalize_name(value, label="platform", pattern=_PLATFORM_PATTERN)


def _observation_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.strip())
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def _capture_key(
    *,
    profile: str,
    key: str,
    hermes_command: str,
    timeout: float,
    runner: Callable[..., Any],
) -> dict[str, Any]:
    command = [hermes_command, "-p", profile, "config", "get", key, "--json"]
    try:
        completed = runner(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
            shell=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise HermesPresentationObservationError(
            f"Hermes presentation configuration capture failed for {key}"
        ) from exc

    stdout = completed.stdout if isinstance(completed.stdout, str) else ""
    digest = "sha256:" + hashlib.sha256(stdout.encode("utf-8")).hexdigest()
    if int(completed.returncode) != 0:
        return {
            "key": key,
            "value": "unknown",
            "status": "unsupported_or_error",
            "exit_code": int(completed.returncode),
            "stdout_digest": digest,
        }

    try:
        value = json.loads(stdout.strip())
    except json.JSONDecodeError:
        return {
            "key": key,
            "value": "unknown",
            "status": "invalid_json",
            "exit_code": int(completed.returncode),
            "stdout_digest": digest,
        }

    if not isinstance(value, bool):
        return {
            "key": key,
            "value": "unknown",
            "status": "unexpected_type",
            "exit_code": int(completed.returncode),
            "stdout_digest": digest,
        }

    return {
        "key": key,
        "value": value,
        "status": "observed",
        "exit_code": int(completed.returncode),
        "stdout_digest": digest,
    }


def capture_presentation_config(
    *,
    profile: str,
    platforms: Iterable[str] | None = None,
    hermes_command: str = "hermes",
    timeout: float = 10.0,
    runner: Callable[..., Any] | None = None,
) -> dict[str, Any]:
    """Capture resolved presentation settings without writing configuration."""

    profile = normalize_profile_name(profile)
    command_name = str(hermes_command or "").strip()
    if not command_name:
        raise HermesPresentationObservationError("Hermes command is required")
    if timeout <= 0:
        raise HermesPresentationObservationError("Hermes presentation timeout must be positive")

    platform_names = sorted({normalize_platform_name(value) for value in (platforms or [])})
    run = runner or subprocess.run
    settings = {
        name: _capture_key(
            profile=profile,
            key=key,
            hermes_command=command_name,
            timeout=timeout,
            runner=run,
        )
        for name, key in _GLOBAL_KEYS.items()
    }

    platform_settings: dict[str, dict[str, Any]] = {}
    for platform in platform_names:
        platform_settings[platform] = {
            "show_reasoning": _capture_key(
                profile=profile,
                key=f"platforms.{platform}.show_reasoning",
                hermes_command=command_name,
                timeout=timeout,
                runner=run,
            ),
            "interim_assistant_messages": _capture_key(
                profile=profile,
                key=f"platforms.{platform}.interim_assistant_messages",
                hermes_command=command_name,
                timeout=timeout,
                runner=run,
            ),
        }

    security_values = [
        settings["show_reasoning"]["value"],
        settings["stream_reasoning_deltas"]["value"],
        *[
            values["show_reasoning"]["value"]
            for values in platform_settings.values()
        ],
    ]
    if any(value is True for value in security_values):
        alignment = "misaligned"
    elif any(value == "unknown" for value in security_values):
        alignment = "incomplete"
    else:
        alignment = "aligned"

    return {
        "kind": "hermes_profile_presentation_config_observation",
        "observation_source": "hermes_config_get_json_cli",
        "profile": profile,
        "captured_at": _now(),
        "settings": settings,
        "platforms": platform_settings,
        "platform_scope": platform_names,
        "configuration_alignment": alignment,
        "behavior_status": "not_evaluated",
        "raw_output_retained": False,
        "write_effect": False,
        "activation_changed": False,
        "authority_effect": "none",
        "technical_receipt_is_evidence": False,
        "non_equivalences": [
            "configuration aligned != private reasoning proven hidden",
            "global display setting != every channel behavior",
            "commentary unavailable != governed task unsafe",
            "presentation observation != task authorization",
            "presentation observation != Evidence",
        ],
    }


def qualify_presentation_config_observation(
    receipt: dict[str, Any] | None,
    *,
    expected_profile: str | None,
    observed_at: datetime | None = None,
    max_age_seconds: float = MAX_PRESENTATION_OBSERVATION_AGE_SECONDS,
) -> dict[str, Any]:
    """Validate a bounded config receipt without upgrading it to behavioral proof."""

    expected = normalize_profile_name(expected_profile) if expected_profile else None
    if receipt is None:
        return {
            "receipt_status": "not_evaluated",
            "configuration_alignment": "unknown",
            "expected_profile": expected,
            "observed_profile": None,
            "behavior_status": "not_evaluated",
            "reason": "no presentation configuration observation was supplied",
            "platform_scope": [],
            "settings": {},
            "platforms": {},
        }
    if not isinstance(receipt, dict):
        raise HermesPresentationObservationError(
            "Hermes presentation configuration observation must be an object"
        )
    if receipt.get("kind") != "hermes_profile_presentation_config_observation":
        raise HermesPresentationObservationError(
            "Hermes presentation configuration observation has an unexpected kind"
        )

    observed_profile = normalize_profile_name(str(receipt.get("profile") or ""))
    reference_time = observed_at or datetime.now(timezone.utc)
    if reference_time.tzinfo is None:
        raise HermesPresentationObservationError(
            "Hermes presentation observation reference time must be timezone-aware"
        )
    reference_time = reference_time.astimezone(timezone.utc)

    reasons: list[str] = []
    if expected is None:
        reasons.append("no expected profile was supplied")
    elif observed_profile != expected:
        reasons.append("presentation observation profile differs from expected profile")
    if receipt.get("observation_source") != "hermes_config_get_json_cli":
        reasons.append("presentation observation has an unexpected source")

    captured_at = _observation_time(receipt.get("captured_at"))
    age_seconds: float | None = None
    if captured_at is None:
        reasons.append("presentation observation has no valid timezone-aware capture time")
    else:
        age_seconds = (reference_time - captured_at).total_seconds()
        if age_seconds > max_age_seconds:
            reasons.append("presentation observation is stale")
        elif age_seconds < -MAX_FUTURE_CLOCK_SKEW_SECONDS:
            reasons.append("presentation observation capture time is in the future")

    settings = receipt.get("settings")
    platforms = receipt.get("platforms")
    if not isinstance(settings, dict) or not isinstance(platforms, dict):
        raise HermesPresentationObservationError(
            "Hermes presentation observation settings must be objects"
        )

    all_records: list[dict[str, Any]] = []
    for name in _GLOBAL_KEYS:
        record = settings.get(name)
        if not isinstance(record, dict):
            reasons.append(f"presentation observation is missing {name}")
            continue
        all_records.append(record)
    for platform, values in platforms.items():
        normalize_platform_name(platform)
        if not isinstance(values, dict):
            reasons.append(f"presentation platform {platform} has invalid settings")
            continue
        for name in ("show_reasoning", "interim_assistant_messages"):
            record = values.get(name)
            if not isinstance(record, dict):
                reasons.append(f"presentation platform {platform} is missing {name}")
                continue
            all_records.append(record)

    for record in all_records:
        digest = str(record.get("stdout_digest") or "")
        if not _DIGEST_PATTERN.fullmatch(digest):
            reasons.append("presentation observation contains an invalid output digest")
        if record.get("status") not in {
            "observed", "unsupported_or_error", "invalid_json", "unexpected_type"
        }:
            reasons.append("presentation observation contains an invalid key status")

    if receipt.get("raw_output_retained") is not False:
        reasons.append("presentation observation retained raw command output")
    if receipt.get("write_effect") is not False or receipt.get("activation_changed") is not False:
        reasons.append("presentation observation reports a mutation effect")
    if receipt.get("authority_effect") != "none":
        reasons.append("presentation observation reports an authority effect")
    if receipt.get("technical_receipt_is_evidence") is not False:
        reasons.append("presentation observation is incorrectly classified as Evidence")

    alignment = str(receipt.get("configuration_alignment") or "unknown")
    if alignment not in {"aligned", "misaligned", "incomplete"}:
        reasons.append("presentation observation has invalid configuration alignment")
        alignment = "unknown"

    receipt_status = "observed" if not reasons else "not_qualified"
    if alignment == "misaligned":
        posture_status = "not_qualified"
        posture_reason = "presentation configuration exposes or streams private reasoning"
    elif receipt_status != "observed" or alignment != "aligned":
        posture_status = "not_evaluated"
        posture_reason = "presentation configuration is incomplete or unqualified"
    else:
        posture_status = "not_evaluated"
        posture_reason = (
            "configuration is aligned but user-visible behavior still requires surface observation"
        )

    return {
        "receipt_status": receipt_status,
        "configuration_alignment": alignment,
        "expected_profile": expected,
        "observed_profile": observed_profile,
        "captured_at": captured_at.isoformat() if captured_at is not None else None,
        "age_seconds": round(age_seconds, 3) if age_seconds is not None else None,
        "platform_scope": sorted(platforms),
        "settings": settings,
        "platforms": platforms,
        "behavior_status": "not_evaluated",
        "posture_status": posture_status,
        "reason": "; ".join(reasons) if reasons else posture_reason,
        "configuration_only": True,
        "technical_receipt_is_evidence": False,
    }
