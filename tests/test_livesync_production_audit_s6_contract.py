from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "implementation-livesync-production-audit-s6.yml"


def _workflow() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_s6_pins_exact_stable_release_and_cli() -> None:
    raw = _workflow()
    assert "32e827692f1a552cd581de9da45cecd0711573d3" in raw
    assert "LIVESYNC_VERSION: 1.0.18" in raw
    assert "LIVESYNC_CLI_VERSION: 1.0.18-cli" in raw
    assert "npm ci" in raw
    assert "latest" not in raw.lower()
    assert "edge" not in raw.lower()


def test_s6_separates_complete_production_and_cli_production_audits() -> None:
    raw = _workflow()
    assert "npm audit --json" in raw
    assert "npm audit --omit=dev --json" in raw
    assert "npm audit --omit=dev --workspace self-hosted-livesync-cli --json" in raw
    assert "npm ls --omit=dev --workspace self-hosted-livesync-cli --all --json" in raw
    assert "productionNames" in raw
    assert "cliProductionNames" in raw


def test_s6_records_findings_without_claiming_security_authorization() -> None:
    raw = _workflow()
    assert "status: 'classified'" in raw
    assert "security_qualified: false" in raw
    assert "exploitability_assessed: false" in raw
    assert "nas_deployment_tested: false" in raw
    assert "runtime_success_is_authorization: false" in raw
    assert "audit_exit_codes" in raw


def test_s6_keeps_reports_as_bounded_ci_artifacts() -> None:
    raw = _workflow()
    assert "livesync-audit-all.json" in raw
    assert "livesync-audit-production.json" in raw
    assert "livesync-audit-cli-production.json" in raw
    assert "livesync-cli-production-tree.json" in raw
    assert "livesync-production-audit-s6-summary.json" in raw
    assert "retention-days: 14" in raw
