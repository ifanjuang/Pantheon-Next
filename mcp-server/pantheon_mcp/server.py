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

from . import doctor, passports, policy, source_map
from .repo import find_repo_root

mcp = FastMCP(
    "pantheon-policy-server",
    instructions=(
        "Pantheon Next policy plane: read doctrine, validate capability "
        "passports, classify requests on the E/V/K/C axes and run read-only "
        "doctor checks. Decisions are data: the gate decides, the human "
        "decides. This server never executes, sends, writes, approves, "
        "installs, schedules or promotes memory."
    ),
)


def _dump(data) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


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
    try:
        data = yaml.safe_load(request_yaml)
    except yaml.YAMLError as exc:
        return _dump({"result": "error", "problems": [f"invalid YAML: {exc}"]})
    if not isinstance(data, dict):
        data = {"intent": str(data or "")}
    return _dump(policy.classify_request(data))


@mcp.tool()
def check_external_action(description: str) -> str:
    """Report what legitimizing an external action requires. The action is
    blocked by default and never performed here."""
    return _dump(policy.check_external_action(description))


@mcp.tool()
def run_doctor_checks() -> str:
    """Run the read-only governance doctor checks over the repository."""
    return _dump(doctor.run_all())


def main() -> None:
    find_repo_root()  # fail fast with a clear message if the repo is absent
    mcp.run()  # stdio transport


if __name__ == "__main__":
    main()
