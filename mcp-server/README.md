# Pantheon MCP policy server (`mcp-server/`)

Status: implemented read-only / partial / protected path — implementation artifact, not authority; broader coverage remains to verify.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

This module is the read-only policy / validation MCP surface of the monorepo. It serves governed sources, explains allowlisted architecture placements, qualifies caller-provided capability-status candidates, validates capability passports and candidate Architecture Project Understanding dossiers, and verifies component installs, observability posture, backup recoverability, exposure-surface safety and update availability from provided evidence. It exposes the governance core to Hermes Agent and OpenWebUI and returns decisions **as data**: the gate decides, the human decides.

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

**Resources** — every entry of the canonical source map (Phase 1/2), served as `pantheon://<key>` and labeled with the file, authority and repository state declared by the effective authority-index corpus (`AUTHORITY_INDEX.md` plus its registered sub-indexes), together with the document's own `Status:` header when present. The server never invents doctrine: an unindexed source stays `authority: not indexed`, missing files report `exists: false`, and candidates report as candidates.

**Tools** (all read-only consultation, validation or candidate preparation):

| Tool | Returns |
|---|---|
| `list_sources` | the source map with authority/status per file |
| `read_doctrine(key)` | one source, full body, labeled |
| `explain_governance_structure(source_key="")` | read-only wiki view of the governance sections, why they exist and their traced sources; optional focus by source key |
| `get_consultation_catalog()` | honest availability map: implemented read-only, partial and documented-non-implemented consultation surfaces |
| `explain_architecture(topic)` | bounded placement, purpose, rationale, forbidden responsibilities and governed source references for Pantheon, Hermes, OpenWebUI, Pantheon Control, MCP/API, capability, knowledge, memory and evidence topics |
| `get_capability_status(status_yaml)` | qualifies a *provided* observation on the Hermes dashboard axes (`listed`, `detected`, `installed`, `configured`, `enabled`, `reachable`, `health`) plus separate governance, task-use, update and rollback axes; performs no live inventory or runtime probe and grants no authorization |
| `validate_passport(passport_yaml)` | shape report + governance gaps (validation ≠ authorization) |
| `classify_request(request_yaml)` | consequence K0–K4, required verification V0–V4, approval ceiling C0–C5, required gates |
| `check_external_action(description)` | blocked-by-default report with the legitimization path |
| `run_doctor_checks()` | fail-closed read-only repo checks with explicit `pass`, `fail`, `not_run` or `capability_gap` outcomes, per-check counts and an aggregate result |
| `validate_apu_dossier(dossier_yaml)` | validates a candidate Architecture Project Understanding dossier against the governance schemas and returns the gate posture as data: schema errors, unresolved references, `posture: candidate-only`, `canonical_effect: false`, regulatory claims lacking approval, and the human decisions required |
| `verify_install(evidence_yaml)` | classifies a component install from *provided* log / health / check evidence and returns the verdict as data (installed, answers, checks green; `green` / `degraded` / `absent` / `unknown`). Read-only: it probes nothing, accesses no NAS, installs nothing and decides nothing; insufficient evidence is a capability gap |
| `verify_observability(evidence_yaml)` | classifies a component's observability posture from *provided* signal-inventory / freshness / error evidence and returns the verdict as data (can we see it: `observable` / `degraded` / `blind` / `unknown`). Read-only: it queries nothing, accesses no NAS and decides nothing; insufficient evidence is a capability gap |
| `verify_backup(evidence_yaml)` | classifies a component's backup / recoverability posture from *provided* backup-presence / freshness / restore evidence and returns the verdict as data (if it dies, can we get it back: `protected` / `degraded` / `unprotected` / `unknown`). Read-only: it runs no backup or restore, accesses no NAS and decides nothing; insufficient evidence is a capability gap |
| `verify_exposure(evidence_yaml)` | classifies a component's exposure-surface safety from *provided* reach / auth / scope evidence and returns the verdict as data (is it exposed without a guard: `guarded` / `degraded` / `exposed` / `unknown`). Read-only: it opens no port, accesses no NAS, sends nothing and decides nothing; insufficient evidence is a capability gap |
| `verify_update(evidence_yaml)` | classifies update availability from a *provided* current and available version and returns the verdict as data (is it current: `current` / `update_available` / `ahead` / `unknown`). Read-only: it fetches nothing, accesses no NAS, updates nothing and decides nothing; insufficient evidence is a capability gap |
| `load_verification_preset(preset_yaml)` | validates a per-module verification preset against its schema and projects it into a verification plan as data: for each active verification, its thresholds and the evidence fields a producer should gather. Read-only: it runs no verification, gathers no evidence, probes nothing and decides nothing |

### Governance Doctor result contract

`run_doctor_checks()` reports six checks. Mandatory files, runtime-language,
cascade-rule, register-instance and vertical-slice validation are mandatory.
The retired-vocabulary worklist is informational.

Each check returns:

```text
status: pass | fail | not_run | capability_gap
mandatory: true | false
counts: expected, evaluated, passed, failed, not_run
message and check-specific details
```

The aggregate is healthy only when every mandatory check ran and returned
`pass`. A missing corpus or schema returns `not_run`; an unavailable required
validator returns `capability_gap`; malformed YAML, invalid schemas and failed
validation return `fail`. None of those states can be reported as green.

### Authority resolution contract

The source map and governance coverage CI load the same effective authority
catalog: the master `AUTHORITY_INDEX.md` plus only the sub-indexes it registers.
Resolution supports exact paths, directory rows and globs. An exact row takes
precedence over a grouped row. Every resolved answer includes the originating
index, table row and line; missing coverage is `not_indexed`, and incompatible
equally specific rows fail closed as `conflict`.

`explain_governance_structure` is a navigation layer over that catalog. It helps
Hermes find a rule and understand why related documents are grouped, but it is
not a parallel wiki database and grants no authority of its own.

## Install and run (stdio)

```bash
python3 -m pip install "mcp-server/.[test]"
pantheon-mcp-server          # or: python -m pantheon_mcp
```

Environment:

```text
PANTHEON_REPO_PATH   path to the Pantheon Next checkout (default: auto-detected
                     by walking up from the module to CLAUDE.md)
```

Hermes Agent reads MCP configuration from `~/.hermes/config.yaml`
under `mcp_servers`. A minimal native fragment for the on-demand policy/wiki is
maintained at
`templates/hermes/connection/pantheon_policy_mcp.template.yaml`:

```yaml
mcp_servers:
  pantheon-policy:
    command: "/opt/pantheon-mcp/.venv/bin/pantheon-mcp-server"
    env:
      PANTHEON_REPO_PATH: "/repo"
    enabled: true
    supports_parallel_tool_calls: true
    tools:
      include:
        - list_sources
        - read_doctrine
        - explain_governance_structure
        - get_consultation_catalog
        - explain_architecture
        - get_capability_status
      prompts: false
      resources: false
    sampling:
      enabled: false
```

Adapt the absolute executable path on the external Hermes host. The template is
a configuration candidate, not proof that the server is installed, reachable,
registered, approved or used.

NAS posture (see `PANTHEON_CONTROL_BOUNDARY.md` / PR #72 history): mount the repository read-only (`…/Pantheon-Next:/repo:ro`); the server needs no Docker socket, no credentials, no write access.

The transport-neutral consultation response contract is documented in
[`docs/CONSULTATION_CONTRACT.md`](docs/CONSULTATION_CONTRACT.md). A future HTTP
projection may reuse it. The external Hermes dashboard plugin can produce a
partial live inventory, but this MCP performs no inventory or probe. No HTTP API, knowledge
retrieval, Mem0/Memvid lookup, user/project authorization service or remote MCP
transport is implemented by this module today.

## APU validation CLI

`validate_apu_dossier` is also available as a read-only command, for validating a
candidate Architecture Project Understanding dossier outside the MCP transport:

```bash
pantheon-apu-validate path/to/dossier.yaml   # or: cat dossier.yaml | pantheon-apu-validate -
```

It prints the gate posture report as JSON and exits `0` when the dossier is ok,
`1` on schema / reference / gate errors (so it can gate a script). Like the tool,
it validates and reports only; it executes, canonizes and approves nothing.

## Install verification CLI

`verify_install` is also available as a read-only command, for classifying a
component install from provided evidence outside the MCP transport:

```bash
pantheon-verify-install path/to/evidence.yaml   # or: cat evidence.yaml | pantheon-verify-install -
```

It prints the verdict report as JSON and exits `0` only when the verdict is
`green`, `1` otherwise (degraded / absent / unknown, or an input error), so it
can gate a script. Like the tool, it performs no probe, no NAS access, installs
nothing and decides nothing.

## Observability verification CLI

`verify_observability` is also available as a read-only command, for classifying
a component's observability posture from provided evidence outside the MCP
transport:

```bash
pantheon-verify-observability path/to/evidence.yaml   # or: cat evidence.yaml | pantheon-verify-observability -
```

It prints the verdict report as JSON and exits `0` only when the verdict is
`observable`, `1` otherwise (degraded / blind / unknown, or an input error), so it
can gate a script. Like the tool, it queries nothing, accesses no NAS and decides
nothing.

## Backup verification CLI

`verify_backup` is also available as a read-only command, for classifying a
component's backup / recoverability posture from provided evidence outside the MCP
transport:

```bash
pantheon-verify-backup path/to/evidence.yaml   # or: cat evidence.yaml | pantheon-verify-backup -
```

It prints the verdict report as JSON and exits `0` only when the verdict is
`protected`, `1` otherwise (degraded / unprotected / unknown, or an input error),
so it can gate a script. Like the tool, it runs no backup or restore, accesses no
NAS and decides nothing.

## Exposure verification CLI

`verify_exposure` is also available as a read-only command, for classifying a
component's exposure-surface safety from provided evidence outside the MCP
transport:

```bash
pantheon-verify-exposure path/to/evidence.yaml   # or: cat evidence.yaml | pantheon-verify-exposure -
```

It prints the verdict report as JSON and exits `0` only when the verdict is
`guarded`, `1` otherwise (degraded / exposed / unknown, or an input error), so it
can gate a script. Like the tool, it opens no port, accesses no NAS, sends nothing
and decides nothing.

## Update verification CLI

`verify_update` is also available as a read-only command, for classifying update
availability from a provided current and available version outside the MCP
transport:

```bash
pantheon-verify-update path/to/evidence.yaml   # or: cat evidence.yaml | pantheon-verify-update -
```

It prints the verdict report as JSON and exits `0` only when the verdict is
`current`, `1` otherwise (update_available / ahead / unknown, or an input error),
so it can gate a script. Like the tool, it fetches nothing, accesses no NAS,
updates nothing and decides nothing.

## Verification preset CLI

`load_verification_preset` is also available as a read-only command, for
validating a per-module verification preset and projecting it into a verification
plan outside the MCP transport:

```bash
pantheon-load-verification-preset path/to/preset.yaml   # or: cat preset.yaml | pantheon-load-verification-preset -
```

It prints the plan as JSON and exits `0` when the preset is valid, `1` on schema or
input errors, so it can gate a script. Like the tool, it runs no verification,
gathers no evidence and decides nothing.

## Tests

```bash
python3 -m unittest discover -s mcp-server/tests
```

The tests cover the effective authority-index source map, path-escape protection, the consultation catalog, architecture explanations, capability-status qualification, passport validation (valid and unsafe fixtures), axis classification, the refusal posture, the doctor checks and the APU dossier validation (schema errors, reference resolution, regulatory-claim gating, gate posture). They are read-only.

## Layout

```text
mcp-server/
  pantheon_mcp/
    repo.py         read-only, root-confined repository access
    authority_index.py shared exact/group/glob authority resolver (read-only)
    source_map.py   source map, authority labels and governance structure guide
    consultation.py transport-neutral catalog, architecture and status projections
    passports.py    capability passport validation (template-mirrored)
    policy.py       K/V/C classification, refusals, external-action gate
    doctor.py       read-only doctor checks (mirrors governance CI)
    apu.py          candidate APU dossier validation + gate posture (read-only)
    install.py      install / liveness verification from provided evidence (read-only)
    observability.py    observability posture verification from provided evidence (read-only)
    backup.py       backup / recoverability verification from provided evidence (read-only)
    exposure.py     exposure-surface safety verification from provided evidence (read-only)
    update.py       update-availability verification from provided evidence (read-only)
    presets.py      verification preset reader: validate + project into a plan (read-only)
    cli.py          read-only CLI entry point for APU dossier validation
    install_cli.py  read-only CLI entry point for install verification
    observability_cli.py  read-only CLI entry point for observability verification
    backup_cli.py   read-only CLI entry point for backup verification
    exposure_cli.py read-only CLI entry point for exposure verification
    update_cli.py   read-only CLI entry point for update verification
    presets_cli.py  read-only CLI entry point for the verification preset reader
    server.py       FastMCP wiring only (stdio)
  fixtures/         fictional passports for tests
  tests/            read-only unit tests
```

The logic modules import without the MCP SDK; only `server.py` requires it. The
repository root is deliberately non-distributable; this module carries the only
Python package metadata and explicit package list.

## Final rule

```text
The MCP Policy Server may frame the work.
It may not do the work.
It may prepare candidates.
It may not approve them.
```
