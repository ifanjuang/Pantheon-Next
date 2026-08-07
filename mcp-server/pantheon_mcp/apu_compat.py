"""Explicit V0.1 -> V0.2 APU dossier compatibility projection.

The adapter is read-only and deliberately lossy only where V0.1 lacks enough
provenance to construct a truthful V0.2 primitive. It never invents Evidence,
approval, certainty, timestamps, stable identity or source observations.
Deprecated carriers remain compatibility inputs and are never emitted as new
canonical V0.2 objects.
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from .repo import find_repo_root, read_repo_text


REGISTRY_PATH = "schemas/architecture-project-understanding/compatibility.registry.yaml"

_OBJECT_FAMILY = {
    "space": "spatial",
    "level": "spatial",
    "path": "spatial",
    "vertical_connection": "spatial",
    "boundary": "element",
    "opening": "element",
    "grid": "datum",
}


def load_compatibility_registry(root: Path | None = None) -> dict[str, Any]:
    root = root or find_repo_root()
    value = yaml.safe_load(read_repo_text(REGISTRY_PATH, root))
    if not isinstance(value, dict) or not isinstance(value.get("entries"), dict):
        raise ValueError("invalid Project Anatomy compatibility registry")
    return value


def compatibility_only_types(root: Path | None = None) -> set[str]:
    entries = load_compatibility_registry(root)["entries"]
    return {
        name
        for name, entry in entries.items()
        if isinstance(entry, dict)
        and entry.get("status") == "compatibility_only"
        and "." not in name
    }


def _items(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        return [payload]
    return []


def _put(target: dict[str, Any], object_type: str, item: dict[str, Any]) -> None:
    target.setdefault(object_type, []).append(item)


def _legacy_claim_value(value: Any) -> dict[str, Any]:
    if isinstance(value, bool):
        return {"value_type": "boolean", "value": value}
    if isinstance(value, (int, float)):
        return {"value_type": "number", "value": value}
    if isinstance(value, str):
        return {"value_type": "text", "value": value}
    if isinstance(value, dict) and len(value) == 1:
        unit, scalar = next(iter(value.items()))
        if isinstance(scalar, bool):
            return {"value_type": "boolean", "value": scalar, "basis": f"legacy-key:{unit}"}
        if isinstance(scalar, (int, float)):
            converted: dict[str, Any] = {"value_type": "number", "value": scalar}
            if unit != "count":
                converted["unit"] = str(unit)
            else:
                converted["basis"] = "legacy-key:count"
            return converted
    if isinstance(value, (dict, list)):
        return {"value_type": "structured", "value": deepcopy(value)}
    raise ValueError("unsupported legacy claim value")


def _legacy_stable_object(item: dict[str, Any], report: dict[str, Any]) -> dict[str, Any]:
    object_id = str(item.get("stable_object_id") or "").strip()
    project_ref = str(item.get("scope_id") or "").strip()
    object_kind = str(item.get("kind") or "").strip()
    if not object_id:
        raise ValueError("legacy stable_object missing stable_object_id")
    if item.get("scope_type") != "project" or not project_ref:
        raise ValueError(
            f"legacy stable_object {object_id} cannot be adapted without exact project scope"
        )
    object_family = _OBJECT_FAMILY.get(object_kind)
    if object_family is None:
        raise ValueError(f"legacy stable_object {object_id} has unsupported kind {object_kind!r}")

    result: dict[str, Any] = {
        "stable_object_id": object_id,
        "project_ref": project_ref,
        "object_family": object_family,
    }
    human_ref = str(item.get("human_ref") or "").strip()
    if human_ref:
        result["nomenclature"] = {"display_name": human_ref}

    matches = item.get("matches") or []
    if matches:
        report["warnings"].append(
            f"stable_object:{object_id}: {len(matches)} inline V0.1 match(es) retained only in compatibility input; "
            "no source_representation or identity relation was invented"
        )
        report["unprojected_legacy_matches"] += len(matches)
    if item.get("notes"):
        report["warnings"].append(
            f"stable_object:{object_id}: legacy notes were not projected into APU V0.2; use Information"
        )
    return result


def _legacy_requirement(item: dict[str, Any]) -> dict[str, Any]:
    requirement_id = str(item.get("requirement_id") or "").strip()
    program_ref = str(item.get("from_program") or "").strip()
    kind = str(item.get("kind") or "").strip()
    if not requirement_id or not program_ref:
        raise ValueError("legacy requirement requires requirement_id and from_program")
    if item.get("modality") != "required":
        raise ValueError(
            f"legacy requirement {requirement_id} is not required-modality and cannot be projected as prescriptive intent"
        )

    target = item.get("target") or {}
    value = item.get("value")
    if kind == "area_min":
        selector: dict[str, Any] = {
            "object_family": "spatial",
            "attribute_key": "area",
        }
        space_function = target.get("space_function") if isinstance(target, dict) else None
        if space_function:
            selector["classification_scheme"] = "legacy.space_function"
            selector["classification_value"] = str(space_function)
        requirement_kind = "attribute"
        constraint = {
            "operator": "min",
            "attribute_key": "area",
            "expected_value": _legacy_claim_value(value),
        }
    elif kind == "group_count":
        classification = target.get("classification") if isinstance(target, dict) else None
        if not isinstance(classification, dict):
            raise ValueError(
                f"legacy requirement {requirement_id} group_count lacks classification target"
            )
        selector = {
            "classification_scheme": str(classification.get("scheme") or "").strip(),
            "classification_value": str(classification.get("value") or "").strip(),
        }
        if not selector["classification_scheme"] or not selector["classification_value"]:
            raise ValueError(
                f"legacy requirement {requirement_id} has incomplete classification target"
            )
        requirement_kind = "count"
        constraint = {
            "operator": "count_exact",
            "expected_value": _legacy_claim_value(value),
        }
    else:
        raise ValueError(
            f"legacy requirement {requirement_id} kind {kind!r} has no reviewed V0.2 adapter"
        )

    result: dict[str, Any] = {
        "requirement_id": requirement_id,
        "source": {"source_type": "program", "source_ref": program_ref},
        "requirement_kind": requirement_kind,
        "target": {"selector": selector},
        "constraint": constraint,
        "source_authority": item.get("source_authority"),
        "proof_status": item.get("proof_status"),
    }
    for key in ("human_ref", "scope_type", "scope_id", "tolerance", "evidence_refs", "notes"):
        if item.get(key) is not None:
            result[key] = deepcopy(item[key])
    return result


def _legacy_attribute_claim(
    item: dict[str, Any], report: dict[str, Any]
) -> dict[str, Any]:
    claim_id = str(item.get("attribute_claim_id") or "").strip()
    about = item.get("about") or {}
    stable_object_id = str(about.get("stable_object_id") or "").strip()
    attribute = str(about.get("attribute") or "").strip()
    modality = str(item.get("modality") or "").strip()
    if not claim_id or not stable_object_id or not attribute:
        raise ValueError("legacy attribute_claim lacks id/about reference")
    if modality == "required":
        raise ValueError(
            f"legacy attribute_claim {claim_id} uses required modality; prescriptive intent must migrate as requirement"
        )
    assertion_mode = {
        "observed": "observed",
        "proposed": "proposed",
        "as_built": "as_built",
    }.get(modality)
    if assertion_mode is None:
        raise ValueError(
            f"legacy attribute_claim {claim_id} has unsupported modality {modality!r}"
        )

    result: dict[str, Any] = {
        "attribute_claim_id": claim_id,
        "subject_ref": {"entity_type": "stable_object", "entity_id": stable_object_id},
        "attribute_key": attribute,
        "value": _legacy_claim_value(item.get("value")),
        "assertion_mode": assertion_mode,
        "source_authority": item.get("source_authority"),
        "proof_status": item.get("proof_status"),
    }
    for source_key, target_key in (
        ("certainty", "certainty"),
        ("tolerance", "tolerance"),
        ("derived_from", "derivation_refs"),
        ("evidence_refs", "evidence_refs"),
        ("notes", "notes"),
    ):
        if item.get(source_key) is not None:
            result[target_key] = deepcopy(item[source_key])

    deprecated_governance = [
        key
        for key in ("approval_state", "allowed_use", "forbidden_use")
        if item.get(key) is not None
    ]
    if deprecated_governance:
        report["warnings"].append(
            f"attribute_claim:{claim_id}: dropped embedded governance field(s) "
            + ", ".join(deprecated_governance)
            + "; approval/use grants remain external"
        )
    if "regulatory_claim" in (item.get("allowed_use") or []):
        approved = item.get("approval_state") == "approved_for_contractual_action"
        has_evidence = bool(item.get("evidence_refs"))
        if not (approved and has_evidence):
            report["regulatory_claims_without_approval"].append(
                f"attribute_claim:{claim_id}"
            )
    return result


def _legacy_claim_lookup(dossier: dict[str, Any]) -> dict[tuple[str, str], str]:
    lookup: dict[tuple[str, str], str] = {}
    for item in _items(dossier.get("attribute_claim")):
        about = item.get("about") or {}
        object_id = str(about.get("stable_object_id") or "").strip()
        attribute = str(about.get("attribute") or "").strip()
        claim_id = str(item.get("attribute_claim_id") or "").strip()
        if object_id and attribute and claim_id:
            lookup[(object_id, attribute)] = claim_id
    return lookup


def _legacy_derivation(
    item: dict[str, Any], claim_lookup: dict[tuple[str, str], str]
) -> dict[str, Any]:
    derivation_id = str(item.get("derivation_id") or "").strip()
    produces = item.get("produces") or {}
    if not derivation_id or not isinstance(produces, dict):
        raise ValueError("legacy derivation lacks derivation_id/produces")
    key = (
        str(produces.get("stable_object_id") or "").strip(),
        str(produces.get("attribute") or "").strip(),
    )
    claim_id = claim_lookup.get(key)
    if not claim_id:
        raise ValueError(
            f"legacy derivation {derivation_id} output cannot be tied to one explicit attribute_claim"
        )
    result: dict[str, Any] = {
        "derivation_id": derivation_id,
        "produces": [{"claim_type": "attribute_claim", "claim_id": claim_id}],
        "method": str(item.get("method") or "").strip(),
    }
    if not result["method"]:
        raise ValueError(f"legacy derivation {derivation_id} lacks method")
    for key_name in (
        "inputs",
        "method_penalty",
        "rule",
        "produced_certainty_score",
        "produced_tolerance",
        "notes",
    ):
        if item.get(key_name) is not None:
            result[key_name] = deepcopy(item[key_name])
    return result


def _is_legacy(otype: str, item: dict[str, Any]) -> bool:
    if otype == "stable_object":
        return "project_ref" not in item and any(
            key in item for key in ("scope_id", "kind", "matches", "proof_status")
        )
    if otype == "requirement":
        return "source" not in item and "from_program" in item
    if otype == "attribute_claim":
        return "subject_ref" not in item and "about" in item
    if otype == "derivation":
        return isinstance(item.get("produces"), dict)
    return False


def adapt_v01_dossier(dossier: dict[str, Any]) -> dict[str, Any]:
    """Project legacy input into canonical V0.2 validation material.

    The returned ``canonical_dossier`` is validation material only. When legacy
    input is present, ``canonical_emission_allowed`` is false so callers cannot
    silently persist or emit the projection as authoritative V0.2 state.
    """
    if not isinstance(dossier, dict):
        raise ValueError("dossier must be a mapping")

    registry = load_compatibility_registry()
    deprecated_types = compatibility_only_types()
    claim_lookup = _legacy_claim_lookup(dossier)
    canonical: dict[str, Any] = {}
    compatibility_records: dict[str, Any] = {}
    report: dict[str, Any] = {
        "legacy_detected": False,
        "input_posture": "v0.2",
        "canonical_emission_allowed": True,
        "authority_transfer": False,
        "deprecated_input_types": [],
        "adapted_records": [],
        "warnings": [],
        "errors": [],
        "unprojected_legacy_matches": 0,
        "regulatory_claims_without_approval": [],
        "human_decisions_required": [],
        "registry_id": registry.get("registry_id"),
    }

    for otype, payload in dossier.items():
        items = _items(payload)
        if not items and payload not in ([], {}):
            report["errors"].append(f"{otype}: compatibility input is not object/list")
            continue

        if otype in deprecated_types:
            report["legacy_detected"] = True
            report["deprecated_input_types"].append(otype)
            compatibility_records[otype] = deepcopy(payload)
            if otype == "deviation":
                for idx, item in enumerate(items):
                    if item.get("resolution") == "pending_human":
                        report["human_decisions_required"].append(
                            f"deviation[{idx}]: legacy deviation pending human resolution"
                        )
            continue

        for idx, item in enumerate(items):
            if not _is_legacy(otype, item):
                _put(canonical, otype, deepcopy(item))
                continue
            report["legacy_detected"] = True
            try:
                if otype == "stable_object":
                    converted = _legacy_stable_object(item, report)
                elif otype == "requirement":
                    converted = _legacy_requirement(item)
                elif otype == "attribute_claim":
                    converted = _legacy_attribute_claim(item, report)
                elif otype == "derivation":
                    converted = _legacy_derivation(item, claim_lookup)
                else:  # pragma: no cover - guarded by _is_legacy
                    raise ValueError(f"no compatibility adapter for {otype}")
            except ValueError as exc:
                report["errors"].append(f"{otype}[{idx}]: {exc}")
                continue
            _put(canonical, otype, converted)
            report["adapted_records"].append(f"{otype}[{idx}]")

    report["deprecated_input_types"] = sorted(set(report["deprecated_input_types"]))
    if report["legacy_detected"]:
        report["input_posture"] = "v0.1_compatibility"
        report["canonical_emission_allowed"] = False
    return {
        "canonical_dossier": canonical,
        "compatibility_records": compatibility_records,
        "compatibility": report,
    }
