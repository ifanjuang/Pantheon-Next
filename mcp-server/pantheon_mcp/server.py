"""MCP stdio projection of the transport-neutral Pantheon policy service.

Every primitive is read-only and side-effect-free.  The server returns policy,
validation and candidate data; it never executes, sends, writes, approves,
installs, schedules, routes providers or promotes memory.
"""

from __future__ import annotations

import json

import yaml
from mcp.server.fastmcp import FastMCP

from . import source_map
from .repo import find_repo_root
from .service import PantheonPolicyService

mcp = FastMCP(
    "pantheon-policy-server",
    instructions=(
        "Pantheon Next read-only policy plane. Consult doctrine, classify requests, "
        "prepare candidates and validate caller-provided structures or evidence. "
        "Decisions are data: Hermes enforces and executes outside Pantheon; the "
        "human decides consequential effects."
    ),
)


def _dump(data) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def _load_yaml_document(raw: str):
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        return None, _dump({"result": "error", "problems": [f"invalid YAML: {exc}"]})
    if not isinstance(data, dict):
        data = {"intent": str(data or "")}
    return data, None


def _service() -> PantheonPolicyService:
    return PantheonPolicyService()


# MCP resources remain direct governed-source projections.
for _key in source_map.SOURCES:

    def _make_reader(key: str):
        def _read() -> str:
            return _dump(_service().read_doctrine(key))

        return _read

    _rel, _title = source_map.SOURCES[_key]
    mcp.resource(
        f"pantheon://{_key}",
        name=_key,
        description=f"{_title} — {_rel} (labeled with authority and status)",
        mime_type="application/json",
    )(_make_reader(_key))


@mcp.tool()
def list_sources() -> str:
    """List governed sources with authority, status and fingerprints."""
    return _dump(_service().list_sources())


@mcp.tool()
def read_doctrine(key: str) -> str:
    """Read one allowlisted governed source; arbitrary paths are not accepted."""
    return _dump(_service().read_doctrine(key))


@mcp.tool()
def explain_governance_structure(source_key: str = "") -> str:
    """Explain repository placement without creating parallel doctrine."""
    return _dump(_service().explain_governance_structure(source_key))


@mcp.tool()
def get_consultation_catalog() -> str:
    """Return the honest availability map for policy consultation surfaces."""
    return _dump(_service().consultation_catalog())


@mcp.tool()
def explain_architecture(topic: str) -> str:
    """Explain one allowlisted architecture topic from governed sources."""
    return _dump(_service().explain_architecture(topic))


@mcp.tool()
def get_capability_status(status_yaml: str) -> str:
    """Qualify a caller-provided capability observation; perform no live probe."""
    data, error = _load_yaml_document(status_yaml)
    return error or _dump(_service().qualify_capability_status(data))


@mcp.tool()
def validate_passport(passport_yaml: str) -> str:
    """Validate a capability passport candidate; validation is not authorization."""
    data, error = _load_yaml_document(passport_yaml)
    return error or _dump(_service().validate_passport(data))


@mcp.tool()
def classify_request(request_yaml: str) -> str:
    """Classify a request on the governed consequence, verification and approval axes."""
    data, error = _load_yaml_document(request_yaml)
    return error or _dump(_service().classify_request(data))


@mcp.tool()
def evaluate_preflight(preflight_yaml: str) -> str:
    """Return candidate-work eligibility and missing gates without authorizing effects."""
    data, error = _load_yaml_document(preflight_yaml)
    return error or _dump(_service().evaluate_preflight(data))


@mcp.tool()
def prepare_task_contract_skeleton(request_yaml: str) -> str:
    """Prepare a non-executable Task Contract candidate skeleton."""
    data, error = _load_yaml_document(request_yaml)
    return error or _dump(_service().prepare_task_contract(data))


@mcp.tool()
def prepare_evidence_pack_skeleton(request_yaml: str) -> str:
    """Prepare an Evidence Pack candidate skeleton; do not validate truth."""
    data, error = _load_yaml_document(request_yaml)
    return error or _dump(_service().prepare_evidence_pack(data))


@mcp.tool()
def check_external_action(description: str) -> str:
    """Return the blocked-by-default legitimacy path for an external action."""
    return _dump(_service().check_external_action(description))


@mcp.tool()
def run_doctor_checks() -> str:
    """Run fail-closed, read-only repository governance checks."""
    return _dump(_service().run_doctor())


@mcp.tool()
def validate_apu_dossier(dossier_yaml: str) -> str:
    """Validate a candidate APU dossier; canonize and approve nothing."""
    data, error = _load_yaml_document(dossier_yaml)
    return error or _dump(_service().validate_apu_dossier(data))


@mcp.tool()
def verify_install(evidence_yaml: str) -> str:
    """Classify installation posture from caller-provided evidence only."""
    data, error = _load_yaml_document(evidence_yaml)
    return error or _dump(_service().verify_install(data))


@mcp.tool()
def verify_observability(evidence_yaml: str) -> str:
    """Classify observability posture from caller-provided evidence only."""
    data, error = _load_yaml_document(evidence_yaml)
    return error or _dump(_service().verify_observability(data))


@mcp.tool()
def verify_backup(evidence_yaml: str) -> str:
    """Classify recoverability posture from caller-provided evidence only."""
    data, error = _load_yaml_document(evidence_yaml)
    return error or _dump(_service().verify_backup(data))


@mcp.tool()
def verify_exposure(evidence_yaml: str) -> str:
    """Classify exposure posture from caller-provided evidence only."""
    data, error = _load_yaml_document(evidence_yaml)
    return error or _dump(_service().verify_exposure(data))


@mcp.tool()
def verify_update(evidence_yaml: str) -> str:
    """Classify update availability from caller-provided version evidence only."""
    data, error = _load_yaml_document(evidence_yaml)
    return error or _dump(_service().verify_update(data))


@mcp.tool()
def load_verification_preset(preset_yaml: str) -> str:
    """Validate and project a verification preset into a data-gathering plan."""
    data, error = _load_yaml_document(preset_yaml)
    return error or _dump(_service().load_verification_preset(data))


@mcp.tool()
def plan_context_pack(request_yaml: str) -> str:
    """Prepare boundaries for a caller-assembled scoped Context Pack candidate."""
    data, error = _load_yaml_document(request_yaml)
    return error or _dump(_service().plan_context_pack(data))


@mcp.tool()
def validate_context_pack(context_pack_yaml: str) -> str:
    """Validate one caller-provided Context Pack against the governed schema."""
    data, error = _load_yaml_document(context_pack_yaml)
    return error or _dump(_service().validate_context_pack(data))


def main() -> None:
    find_repo_root()
    mcp.run()


if __name__ == "__main__":
    main()
