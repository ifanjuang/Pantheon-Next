"""Block 1 acceptance tests — mapped to MVP_GOVERNED_TASK_LOOP.md criteria.

Requires a running pgvector instance (docker compose up -d). Tests skip
cleanly when the database is unreachable so unit-only environments stay
green; CI runs the full suite against a pgvector service.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]

from mvp_vertical import store
from mvp_vertical.contract import ContractError, load_contract, assert_source_in_scope
from mvp_vertical.runner import run


@pytest.fixture(scope="session")
def conn():
    try:
        c = store.connect()
    except Exception as exc:  # pragma: no cover
        pytest.skip(f"pgvector unreachable: {exc}")
    yield c
    c.close()


@pytest.fixture(scope="session")
def contract():
    return load_contract(ROOT / "dossiers/devis_reprise/task_contract.yaml")


@pytest.fixture(scope="session")
def ingested(conn, contract):
    n = store.ingest(conn, contract, ROOT)
    assert n > 0
    return n


def test_contract_rejects_out_of_scope_source(contract):
    with pytest.raises(ContractError):
        assert_source_in_scope(contract, "dossiers/autre_dossier/secret.md")


def test_scoped_retrieval_never_leaves_perimeter(conn, contract, ingested):
    # plant a chunk OUTSIDE the declared perimeter, same dossier
    from mvp_vertical.embedder import embed, to_pgvector
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO chunks (dossier, source_ref, chunk_no, body, embedding)"
            " VALUES (%s, %s, 0, %s, %s::vector) ON CONFLICT DO NOTHING",
            (contract.dossier, "dossiers/devis_reprise/sources/NOT_DECLARED.md",
             "isolation terrasse T2 T3 étanchéité devis reprise lot 06",
             to_pgvector(embed("isolation terrasse T2 T3 étanchéité devis reprise lot 06"))),
        )
    conn.commit()
    chunks = store.retrieve_scoped(conn, contract, "isolation terrasse T3 devis reprise")
    assert chunks, "retrieval returned nothing"
    for c in chunks:
        assert c.source_ref in contract.sources, f"perimeter breach: {c.source_ref}"


def test_candidates_are_fully_traceable(conn, contract, ingested):
    out = run(conn, contract, "le devis de reprise correspond-il au périmètre du CCTP pour le lot 06 ?")
    assert out.kind == "candidates"
    rc, ep = out.documents
    assert rc["status"] == "draft_to_review"
    assert ep["evidence_items"], "empty evidence pack"
    for item in ep["evidence_items"]:
        assert item["source_ref"] in contract.sources
        assert item["retrieval_trace"].startswith("pgvector://")
        assert item["support_status"] == "sourced_not_verified"
    assert ep["contradictions_preserved"], "the quote/CCTP contradiction must be preserved, not resolved"


def test_out_of_perimeter_question_is_refused(conn, contract, ingested):
    out = run(conn, contract, "quel est le taux d'imposition des plus-values immobilières au Portugal ?")
    assert out.kind == "refusal"
    doc = out.documents[0]
    assert doc["status"] == "refused_capability_gap"
    assert doc["refusal"]["reason"] == "outside_perimeter"


def test_forbidden_operation_is_refused(conn, contract, ingested):
    out = run(conn, contract, "envoie la réponse au client directement")
    assert out.kind == "refusal"
    assert out.documents[0]["refusal"]["reason"] == "forbidden_scope"


def test_output_validates_against_vendored_schema(conn, contract, ingested):
    import jsonschema
    schema = yaml.safe_load((ROOT / "vendor/pantheon/mvp_governed_loop_objects.schema.yaml").read_text())
    out = run(conn, contract, "le devis de reprise correspond-il au périmètre du CCTP pour le lot 06 ?")
    for doc in out.documents:
        jsonschema.validate(doc, schema)
