"""Synthetic regression for exact-source fallback across IFJA source families."""

from __future__ import annotations

import asyncio
import json
import os
import socket
import subprocess
import sys
import time
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "implementation/hermes/skills/ifja-vault-search/scripts"
sys.path.insert(0, str(SCRIPTS))

from ifja_vault_sources import VaultSourceError, VaultSources  # noqa: E402


@pytest.fixture()
def vaults(tmp_path: Path) -> tuple[VaultSources, dict[str, Path]]:
    affaires = tmp_path / "affaires"
    documentaires = tmp_path / "documentaires"
    floquet = affaires / "_Projets" / "Floquet"
    longueil = affaires / "_Projets" / "Longueil"
    cerfa = floquet / "Production" / "Permis" / "cerfa_PC_FLOQUET" / "cerfa_PC_FLOQUET.md"
    visit = longueil / "LONGUEIL VISITE 260917.md"
    plui = longueil / "Urbanisme" / "PLUi Terroir de Caux UB1 extrait.md"
    maf = documentaires / "MAF" / "PERMIS" / "MAF_OUTILS_PERMIS.md"
    for path in (cerfa, visit, plui, maf):
        path.parent.mkdir(parents=True, exist_ok=True)
    cerfa.write_text("# CERFA Floquet\nSurface déclarée : exemple fictif.\n", encoding="utf-8")
    visit.write_text("# Visite Longueil\nTerrain observé : exemple fictif.\n", encoding="utf-8")
    plui.write_text("# Zone UB1\nRègle à vérifier sur le projet.\n", encoding="utf-8")
    maf.write_text("# Outil MAF\nConseil général, sans fait de projet.\n", encoding="utf-8")
    return VaultSources(affaires, documentaires), {
        "cerfa": cerfa, "visit": visit, "plui": plui, "maf": maf,
    }


def test_project_is_resolved_before_permit_terms_and_longueil_is_not_absent(vaults) -> None:
    reader, files = vaults
    found = reader.find_projects("Longueil")
    assert found["items"] == [{
        "project_ref": "_Projets/Longueil", "name": "Longueil", "match": "exact_name"
    }]
    inventory = reader.list_project_sources("_Projets/Longueil", "permis")
    paths = {item["source_path"] for item in inventory["items"]}
    assert paths == {str(files["visit"]), str(files["plui"])}
    assert {item["source_path"] for item in inventory["items"][:2]} == {
        str(files["visit"]), str(files["plui"])
    }
    assert inventory["path_match_is_content_support"] is False
    assert str(files["cerfa"]) not in paths


def test_nested_floquet_cerfa_is_read_at_exact_lines_not_from_a_directory(vaults) -> None:
    reader, files = vaults
    inventory = reader.list_project_sources("_Projets/Floquet", "permis CERFA")
    assert inventory["items"][0]["source_path"] == str(files["cerfa"])
    hit = reader.search_markdown(str(files["cerfa"]), "surface", "_Projets/Floquet")
    assert hit["hits"][0]["line"] == 2
    assert hit["search_hit_is_source_inspection"] is False
    passage = reader.read_markdown_lines(str(files["cerfa"]), 2, 1, "_Projets/Floquet")
    assert passage["lines"] == [{"line": 2, "text": "Surface déclarée : exemple fictif."}]
    assert passage["source_family"] == "AFFAIRES"
    with pytest.raises(VaultSourceError, match="Markdown file"):
        reader.read_markdown_lines(str(files["cerfa"].parent), project_ref="_Projets/Floquet")


def test_maf_stays_documentary_and_cross_project_reads_are_rejected(vaults) -> None:
    reader, files = vaults
    maf = reader.read_markdown_lines(str(files["maf"]))
    assert maf["source_family"] == "DOCUMENTAIRES"
    assert maf["evidence_admitted"] is False
    with pytest.raises(VaultSourceError, match="must not be presented as a project"):
        reader.read_markdown_lines(str(files["maf"]), project_ref="_Projets/Longueil")
    with pytest.raises(VaultSourceError, match="does not belong"):
        reader.read_markdown_lines(str(files["cerfa"]), project_ref="_Projets/Longueil")
    with pytest.raises(VaultSourceError, match="does not belong"):
        reader.search_markdown(str(files["visit"]), "terrain", project_ref="_Projets/Floquet")


def test_reader_rejects_escape_symlinks_and_unbounded_results(vaults, tmp_path: Path) -> None:
    reader, files = vaults
    outside = tmp_path / "outside.md"
    outside.write_text("private", encoding="utf-8")
    link = files["visit"].parent / "outside.md"
    link.symlink_to(outside)
    with pytest.raises(VaultSourceError, match="outside"):
        reader.read_markdown_lines(str(outside))
    with pytest.raises(VaultSourceError, match="not a directory or link"):
        reader.read_markdown_lines(str(link), project_ref="_Projets/Longueil")
    with pytest.raises(VaultSourceError, match="project_ref"):
        reader.list_project_sources("_Projets/Longueil/../Floquet")
    with pytest.raises(VaultSourceError, match="between 1 and"):
        reader.read_markdown_lines(str(files["visit"]), max_lines=1000,
                                   project_ref="_Projets/Longueil")


def test_runtime_binding_is_explicitly_read_only_and_bounded() -> None:
    script = (SCRIPTS / "ifja_vault_mcp.py").read_text(encoding="utf-8")
    configure = (ROOT / "deployment/ubuntu/configure-hermes-activity-projection").read_text(
        encoding="utf-8"
    )
    for tool in (
        "find_ifja_projects", "list_ifja_project_sources",
        "search_ifja_markdown", "read_ifja_markdown_lines",
    ):
        assert tool in script and tool in configure
    assert "read_only_hint=True" in script
    assert '"ifja-vault-read"' in configure
    assert '"prompts": false, "resources": false' in configure
    assert '"sampling": {"enabled": false}' in configure
    assert "--bind-local-mcp requires --with-ifja-adapter" in configure
    assert 'IFJA_VAULT_MCP_URL="http://127.0.0.1:8021/mcp"' in configure
    assert '"headers": {"Authorization": ("Bearer " + $vault_token)}' in configure


def test_local_service_keeps_vault_acl_off_hermes_and_authenticates_http() -> None:
    installer = (ROOT / "deployment/ubuntu/configure-ifja-vault-read-local").read_text(
        encoding="utf-8"
    )
    assert "User=pantheon-docling" in installer
    assert "Group=pantheon-docling" in installer
    assert "--apply [--enable]" in installer
    assert "openssl rand -hex 32" in installer
    assert "ProtectSystem=strict" in installer
    assert "setfacl" not in installer
    assert '"127.0.0.1"' in (SCRIPTS / "ifja_vault_mcp.py").read_text(encoding="utf-8")


def test_http_guard_rejects_requests_without_the_service_token() -> None:
    pytest.importorskip("mcp")
    from ifja_vault_mcp import BearerGuard

    reached = []
    messages = []

    async def app(scope, receive, send):
        reached.append(scope["type"])

    async def receive():
        return {"type": "http.request", "body": b"", "more_body": False}

    async def send(message):
        messages.append(message)

    async def exercise():
        guard = BearerGuard(app, "a" * 32)
        await guard({"type": "http", "headers": []}, receive, send)
        assert messages[0]["status"] == 401
        assert not reached
        messages.clear()
        await guard({"type": "http", "headers": [(b"authorization", b"Bearer " + b"a" * 32)]},
                    receive, send)
        assert reached == ["http"]

    asyncio.run(exercise())


def test_mcp_registers_only_the_four_read_only_tools() -> None:
    pytest.importorskip("mcp")
    import ifja_vault_mcp

    tools = asyncio.run(ifja_vault_mcp.mcp.list_tools())
    assert {tool.name for tool in tools} == {
        "find_ifja_projects", "list_ifja_project_sources",
        "search_ifja_markdown", "read_ifja_markdown_lines",
    }
    assert all(tool.annotations.read_only_hint is True for tool in tools)
    assert all(tool.annotations.destructive_hint is False for tool in tools)


def test_stdio_mcp_opens_only_the_selected_synthetic_project(vaults) -> None:
    pytest.importorskip("mcp")
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    reader, files = vaults
    parameters = StdioServerParameters(
        command=sys.executable,
        args=[str(SCRIPTS / "ifja_vault_mcp.py")],
        env={
            **os.environ,
            "IFJA_AFFAIRES_ROOT": str(reader.affaires_root),
            "IFJA_DOCUMENTAIRES_ROOT": str(reader.documentaires_root),
        },
    )

    async def exercise() -> None:
        async with stdio_client(parameters) as (receive, send):
            async with ClientSession(receive, send) as session:
                await session.initialize()
                projects = await session.call_tool("find_ifja_projects", {"designation": "Longueil"})
                found = json.loads(projects.content[0].text)
                assert found["items"][0]["project_ref"] == "_Projets/Longueil"
                inventory = await session.call_tool("list_ifja_project_sources", {
                    "project_ref": "_Projets/Longueil", "topic": "permis"
                })
                listed = json.loads(inventory.content[0].text)
                assert {item["source_path"] for item in listed["items"]} == {
                    str(files["visit"]), str(files["plui"])
                }
                crossing = await session.call_tool("read_ifja_markdown_lines", {
                    "source_path": str(files["cerfa"]), "project_ref": "_Projets/Longueil"
                })
                assert json.loads(crossing.content[0].text)["status"] == "error"

    asyncio.run(exercise())


def test_authenticated_http_mcp_reads_longueil_but_not_floquet(vaults, tmp_path: Path) -> None:
    pytest.importorskip("mcp")
    import httpx2 as httpx
    from mcp import ClientSession
    from mcp.client.streamable_http import streamable_http_client

    reader, files = vaults
    token = "synthetic-test-token-0123456789abcdef"
    token_file = tmp_path / "token"
    token_file.write_text(token, encoding="ascii")
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]

    process = subprocess.Popen(
        [sys.executable, str(SCRIPTS / "ifja_vault_mcp.py"), "--http"],
        env={
            **os.environ,
            "IFJA_AFFAIRES_ROOT": str(reader.affaires_root),
            "IFJA_DOCUMENTAIRES_ROOT": str(reader.documentaires_root),
            "IFJA_VAULT_TOKEN_FILE": str(token_file),
            "IFJA_VAULT_MCP_PORT": str(port),
        },
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    url = f"http://127.0.0.1:{port}/mcp"
    try:
        for _ in range(100):
            if process.poll() is not None:
                pytest.fail(f"HTTP MCP exited: {process.stderr.read().decode(errors='replace')}")
            try:
                response = httpx.get(url, timeout=0.2)
                assert response.status_code == 401
                break
            except httpx.ConnectError:
                time.sleep(0.05)
        else:
            pytest.fail("HTTP MCP did not start on loopback")

        async def exercise() -> None:
            async with httpx.AsyncClient(headers={"Authorization": f"Bearer {token}"}) as client:
                async with streamable_http_client(url, http_client=client) as (receive, send):
                    async with ClientSession(receive, send) as session:
                        await session.initialize()
                        inventory = await session.call_tool("list_ifja_project_sources", {
                            "project_ref": "_Projets/Longueil", "topic": "permis",
                        })
                        listed = json.loads(inventory.content[0].text)
                        assert {item["source_path"] for item in listed["items"]} == {
                            str(files["visit"]), str(files["plui"]),
                        }
                        crossing = await session.call_tool("read_ifja_markdown_lines", {
                            "source_path": str(files["cerfa"]),
                            "project_ref": "_Projets/Longueil",
                        })
                        assert json.loads(crossing.content[0].text)["status"] == "error"

        asyncio.run(exercise())
    finally:
        process.terminate()
        try:
            process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.communicate(timeout=5)
