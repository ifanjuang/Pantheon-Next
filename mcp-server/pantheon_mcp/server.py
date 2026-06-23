"""MCP wiring (stdio). All logic lives in the importable modules so it can
be tested without the SDK; this file only exposes it.

Every primitive here is read-only and side-effect-free. The server refuses
any request to act (send, write, merge, approve, promote, install,
schedule, route, execute).
"""

from __future__ import annotations

import json

import yaml
from mcp.server.fastmcp import FastMCP

from . import apu, backup, contracts, doctor, exposure, install, observability, passports, policy, source_map, update
from .repo import find_repo_root

mcp = FastMCP(
    "pantheon-policy-server",
    instructions=(
        "Pantheon Next policy plane: read doctrine, validate capability "
        "passports, classify requests on the E/V/K/C axes, prepare candidate "
        "Task Contract / Evidence Pack skeletons and run read-only doctor "
        "checks. Decisions are data: the gate decides, the human decides. "
        "This server never executes, sends, writes, approves, installs, "
        "schedules or promotes memory."
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


# ---------------------------------------------------------------- resources
for _key in source_map.SOURCES:

    def _make_reader(key: str):
        def _read() -> str:
            return _dump(source_map.read_source(key))

        return _read

    _rel, _title = source_map.SOURCES[_key]
    mcp.resource(
        f"pantheon://{_key}",
        name=_key,
        description=f"{_title} — {_rel} (labeled with authority and status)",
        mime_type="application/json",
    )(_make_reader(_key))


# -------------------------------------------------------------------- tools
@mcp.tool()
def list_sources() -> str:
    """List every governed source with its file, authority and status."""
    return _dump(source_map.list_sources())


@mcp.tool()
def read_doctrine(key: str) -> str:
    """Read one governed source (full body), labeled with authority/status."""
    return _dump(source_map.read_source(key))


@mcp.tool()
def validate_passport(passport_yaml: str) -> str:
    """Validate a capability passport (YAML) against the template shape and
governance rules. Validation is not authorization."""
    try:
        data = yaml.safe_load(passport_yaml)
    except yaml.YAMLError as exc:
        return _dump({"valid": False, "problems": [f"invalid YAML: {exc}"]})
    return _dump(passports.validate_passport(data or {}))


@mcp.tool()
def classify_request(request_yaml: str) -> str:
    """Classify a described request on the K/V/C axes and state the gates it
must pass. Any request asking this server to act is refused."""
    data, error = _load_yaml_document(request_yaml)
    if error:
        return error
    return _dump(policy.classify_request(data))


@mcp.tool()
def prepare_task_contract_skeleton(request_yaml: str) -> str:
    """Prepare a Task Contract candidate skeleton. It is not executable and
not approved; it is a review object for Hermes/human use."""
    data, error = _load_yaml_document(request_yaml)
    if error:
        return error
    return _dump(contracts.prepare_task_contract_skeleton(data))


@mcp.tool()
def prepare_evidence_pack_skeleton(request_yaml: str) -> str:
    """Prepare an Evidence Pack candidate skeleton. It supports review and
never validates truth or writes the Registre Probatoire."""
    data, error = _load_yaml_document(request_yaml)
    if error:
        return error
    return _dump(contracts.prepare_evidence_pack_skeleton(data))


@mcp.tool()
def check_external_action(description: str) -> str:
    """Report what legitimizing an external action requires. The action is
blocked by default and never performed here."""
    return _dump(policy.check_external_action(description))


@mcp.tool()
def run_doctor_checks() -> str:
    """Run the read-only governance doctor checks over the repository."""
    return _dump(doctor.run_all())


@mcp.tool()
def validate_apu_dossier(dossier_yaml: str) -> str:
    """Validate a candidate Architecture Project Understanding dossier against the
governance schemas and return the gate posture as data. Read-only: nothing is
executed, canonized or approved. The dossier is a mapping of object_type ->
object(s)."""
    data, error = _load_yaml_document(dossier_yaml)
    if error:
        return error
    return _dump(apu.validate_apu_dossier(data))


@mcp.tool()
def verify_install(evidence_yaml: str) -> str:
    """Verify a component install from provided log / health / check evidence and
return the verdict as data (is it installed, does it answer, are its checks
green). Read-only: it performs no probe, no NAS access, installs nothing and
decides nothing. Insufficient evidence is reported as a capability gap."""
    data, error = _load_yaml_document(evidence_yaml)
    if error:
        return error
    return _dump(install.verify_install(data))


@mcp.tool()
def verify_observability(evidence_yaml: str) -> str:
    """Verify a component's observability posture from provided signal / freshness
/ error evidence and return the verdict as data (can we see it: observable /
degraded / blind / unknown). Read-only: it performs no probe, no NAS access, no
metrics query and decides nothing. Insufficient evidence is a capability gap."""
    data, error = _load_yaml_document(evidence_yaml)
    if error:
        return error
    return _dump(observability.verify_observability(data))


@mcp.tool()
def verify_backup(evidence_yaml: str) -> str:
    """Verify a component's backup / recoverability posture from provided
backup / freshness / restore evidence and return the verdict as data (if it
dies, can we get it back: protected / degraded / unprotected / unknown).
Read-only: it performs no probe, no NAS access, runs no backup or restore and
decides nothing. Insufficient evidence is a capability gap."""
    data, error = _load_yaml_document(evidence_yaml)
    if error:
        return error
    return _dump(backup.verify_backup(data))


@mcp.tool()
def verify_exposure(evidence_yaml: str) -> str:
    """Verify a component's exposure-surface safety from provided reach / auth /
scope evidence and return the verdict as data (is it exposed without a guard:
guarded / degraded / exposed / unknown). Read-only: it performs no probe, no NAS
access, opens no port, sends nothing and decides nothing. Insufficient evidence
is a capability gap."""
    data, error = _load_yaml_document(evidence_yaml)
    if error:
        return error
    return _dump(exposure.verify_exposure(data))


@mcp.tool()
def verify_update(evidence_yaml: str) -> str:
    """Verify update availability from a provided current and available version
and return the verdict as data (is it current: current / update_available /
ahead / unknown). Read-only: it performs no probe, no network fetch, no NAS
access, no update and decides nothing. Insufficient evidence is a capability
gap."""
    data, error = _load_yaml_document(evidence_yaml)
    if error:
        return error
    return _dump(update.verify_update(data))


def main() -> None:
    find_repo_root()  # fail fast with a clear message if the repo is absent
    mcp.run()  # stdio transport


if __name__ == "__main__":
    main()
