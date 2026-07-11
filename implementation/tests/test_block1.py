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
from mvp_vertical.contract import (
    ContractError,
    assert_source_in_scope,
    load_contract,
    resolve_source_within,
)
from mvp_vertical.runner import (
    RunnerInvariantError,
    _assert_no_external_authorization,
    run,
)


def _write_contract(tmp_path: Path, sources: list[str]) -> Path:
    """Minimal schema-shaped contract with a chosen source list, for path tests."""
    data = {
        "object_type": "task_contract",
        "object_id": "mvp.test.tc",
        "contract_id": "mvp.test.tc",
        "status": "candidate",
        "declared_scope": {"dossier": "test", "sources": sources},
        "forbidden_scope": [],
        "expected_output": {"type": "result_candidate"},
    }
    p = tmp_path / "tc.yaml"
    p.write_text(yaml.safe_dump(data), encoding="utf-8")
    return p


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


# Gate 2 (adoption review): source path boundary — absolute / traversal /
# symlink. These run without pgvector so the guard is exercised in every lane.

def test_contract_rejects_absolute_declared_source(tmp_path):
    with pytest.raises(ContractError):
        load_contract(_write_contract(tmp_path, ["/etc/passwd"]))


def test_contract_rejects_traversing_declared_source(tmp_path):
    with pytest.raises(ContractError):
        load_contract(_write_contract(tmp_path, ["../../etc/passwd"]))


def test_resolve_source_rejects_symlink_escape(tmp_path):
    root = tmp_path / "repo"
    (root / "dossiers").mkdir(parents=True)
    secret = tmp_path / "secret.md"
    secret.write_text("out of tree", encoding="utf-8")
    (root / "dossiers" / "leak.md").symlink_to(secret)
    with pytest.raises(ContractError):
        resolve_source_within(root, "dossiers/leak.md", "mvp.test.tc")


def test_resolve_source_accepts_in_tree(tmp_path):
    root = tmp_path / "repo"
    (root / "d").mkdir(parents=True)
    f = root / "d" / "ok.md"
    f.write_text("in tree", encoding="utf-8")
    assert resolve_source_within(root, "d/ok.md", "mvp.test.tc") == f.resolve()


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


# Gate 6 (adoption review): external-send. The send-intent match is advisory
# routing to a clearer refusal, and the real guarantee is structural — so
# these run without pgvector (the refusal returns before any retrieval).

@pytest.mark.parametrize(
    "question",
    [
        "transmets la réponse au client",
        "peux-tu expédier ce courrier ?",
        "fais suivre au maître d'ouvrage",
        "forward this to the client",
    ],
)
def test_send_intent_paraphrases_are_refused(contract, question):
    out = run(None, contract, question)  # conn unused: refusal precedes retrieval
    assert out.kind == "refusal"
    assert out.documents[0]["refusal"]["reason"] == "forbidden_scope"


def test_runner_never_authorizes_external_action():
    # The structural invariant, made explicit: any object asserting external
    # authorization or a gate-only outcome is a hard error, never a candidate.
    with pytest.raises(RunnerInvariantError):
        _assert_no_external_authorization([{"object_id": "x", "external_action_authorized": True}])
    with pytest.raises(RunnerInvariantError):
        _assert_no_external_authorization([{"object_id": "x", "status": "sent"}])
    # a well-formed, non-authorizing object passes
    _assert_no_external_authorization([{"object_id": "x", "status": "draft_to_review",
                                        "external_action_authorized": False}])


def test_output_validates_against_vendored_schema(conn, contract, ingested):
    import jsonschema
    schema = yaml.safe_load((ROOT / "vendor/pantheon/mvp_governed_loop_objects.schema.yaml").read_text())
    out = run(conn, contract, "le devis de reprise correspond-il au périmètre du CCTP pour le lot 06 ?")
    for doc in out.documents:
        jsonschema.validate(doc, schema)
