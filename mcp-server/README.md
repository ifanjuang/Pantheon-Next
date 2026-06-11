# Pantheon MCP policy server (`mcp-server/`)

Status: implementation candidate — first slice of the bounded module described in `CLAUDE.md`, built per the phases of `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`. Candidate until reviewed.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

This module is the read-only policy / validation MCP surface of the monorepo. It serves and validates capability passports and exposes the governance core to Hermes Agent and OpenWebUI. It returns policy decisions **as data**: the gate decides, the human decides.

## Boundary

The server is read-only and side-effect-free. It does not and must not:

```text
execute a capability        send anything externally
write files or state        merge code
approve outputs             promote memory / write the Registre Probatoire
install skills              schedule jobs
route providers             run hidden workflows
```

Any request asking the server to perform such an effect is refused with a report pointing to the Task Contract / gate path (Phase 7 refusal posture).

## What it exposes

**Resources** — every entry of the canonical source map (Phase 1/2), served as `pantheon://<key>` and labeled with the file, authority and status declared by `AUTHORITY_INDEX.md`. The server never invents doctrine: missing files report `exists: false`, candidates report as candidates.

**Tools** (Phase 4, all validation-only):

| Tool | Returns |
|---|---|
| `list_sources` | the source map with authority/status per file |
| `read_doctrine(key)` | one source, full body, labeled |
| `validate_passport(passport_yaml)` | shape report + governance gaps (validation ≠ authorization) |
| `classify_request(request_yaml)` | consequence K0–K4, required verification V0–V4, approval ceiling C0–C5, required gates |
| `check_external_action(description)` | blocked-by-default report with the legitimization path |
| `run_doctor_checks()` | read-only repo checks (mandatory files, runtime-phrase guard, retired-vocabulary worklist) |

## Install and run (stdio)

```bash
cd mcp-server
pip install -e .
pantheon-mcp-server          # or: python -m pantheon_mcp
```

Environment:

```text
PANTHEON_REPO_PATH   path to the Pantheon Next checkout (default: auto-detected
                     by walking up from the module to CLAUDE.md)
```

Client configuration example (Hermes Agent / any MCP client):

```json
{
  "mcpServers": {
    "pantheon-policy": {
      "command": "pantheon-mcp-server",
      "env": { "PANTHEON_REPO_PATH": "/repo" }
    }
  }
}
```

NAS posture (see `PANTHEON_CONTROL_BOUNDARY.md` / PR #72 history): mount the repository read-only (`…/Pantheon-Next:/repo:ro`); the server needs no Docker socket, no credentials, no write access.

## Tests

```bash
python3 -m unittest discover -s mcp-server/tests
```

The tests cover the source map, path-escape protection, passport validation (valid and unsafe fixtures), axis classification, the refusal posture and the doctor checks. They are read-only.

## Layout

```text
mcp-server/
  pantheon_mcp/
    repo.py         read-only, root-confined repository access
    source_map.py   Phase 1 — canonical source map + authority labeling
    passports.py    capability passport validation (template-mirrored)
    policy.py       K/V/C classification, refusals, external-action gate
    doctor.py       read-only doctor checks (mirrors governance CI)
    server.py       FastMCP wiring only (stdio)
  fixtures/         fictional passports for tests
  tests/            read-only unit tests
```

The logic modules import without the MCP SDK; only `server.py` requires it. The root `pyproject.toml`, `schemas/` and `tests/` are untouched: this module carries its own packaging.

## Final rule

```text
The MCP Policy Server may frame the work.
It may not do the work.
It may prepare candidates.
It may not approve them.
```
