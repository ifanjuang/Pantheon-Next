-- Append-only execution results and review dispositions.
-- Runtime return, review disposition and APU adoption remain separate facts.

CREATE TABLE IF NOT EXISTS execution_results (
    execution_result_id TEXT PRIMARY KEY,
    task_contract_ref TEXT NOT NULL,
    project_ref TEXT,
    producer JSONB NOT NULL,
    produced_at TIMESTAMPTZ NOT NULL,
    evidence_pack_candidate_ref TEXT,
    authority JSONB NOT NULL,
    payload_digest TEXT NOT NULL,
    idempotency_key TEXT NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS execution_result_items (
    result_id TEXT PRIMARY KEY,
    execution_result_id TEXT NOT NULL REFERENCES execution_results(execution_result_id) ON DELETE RESTRICT,
    result_kind TEXT NOT NULL CHECK (result_kind IN (
        'fragment_qualification', 'document_alignment', 'spatial_observation',
        'apu_object_mapping', 'relation_candidate', 'contradiction_candidate',
        'work_issue_candidate'
    )),
    schema_ref TEXT NOT NULL,
    payload JSONB NOT NULL,
    payload_digest TEXT NOT NULL,
    ordinal INT NOT NULL CHECK (ordinal >= 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (execution_result_id, ordinal)
);

CREATE TABLE IF NOT EXISTS execution_clarification_requests (
    clarification_id TEXT PRIMARY KEY,
    execution_result_id TEXT NOT NULL REFERENCES execution_results(execution_result_id) ON DELETE RESTRICT,
    related_result_refs JSONB NOT NULL DEFAULT '[]'::jsonb,
    question TEXT NOT NULL,
    answer_kind TEXT NOT NULL CHECK (answer_kind IN (
        'free_text', 'single_choice', 'multiple_choice', 'confirmation', 'source_request'
    )),
    options JSONB NOT NULL DEFAULT '[]'::jsonb,
    rationale TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (jsonb_typeof(related_result_refs) = 'array'),
    CHECK (jsonb_typeof(options) = 'array')
);

CREATE TABLE IF NOT EXISTS execution_result_review_dispositions (
    disposition_id TEXT PRIMARY KEY,
    result_ref TEXT NOT NULL REFERENCES execution_result_items(result_id) ON DELETE RESTRICT,
    disposition TEXT NOT NULL CHECK (disposition IN (
        'pending', 'needs_clarification', 'accepted_for_mapping', 'rejected', 'superseded'
    )),
    reviewer TEXT NOT NULL,
    reviewer_kind TEXT NOT NULL CHECK (reviewer_kind IN ('human', 'system')),
    note TEXT,
    idempotency_key TEXT NOT NULL UNIQUE,
    payload_digest TEXT NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION reject_execution_result_mutation()
RETURNS trigger AS $$
BEGIN
    RAISE EXCEPTION 'execution result records are append-only';
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS execution_results_append_only ON execution_results;
CREATE TRIGGER execution_results_append_only
BEFORE UPDATE OR DELETE ON execution_results
FOR EACH ROW EXECUTE FUNCTION reject_execution_result_mutation();

DROP TRIGGER IF EXISTS execution_result_items_append_only ON execution_result_items;
CREATE TRIGGER execution_result_items_append_only
BEFORE UPDATE OR DELETE ON execution_result_items
FOR EACH ROW EXECUTE FUNCTION reject_execution_result_mutation();

DROP TRIGGER IF EXISTS execution_clarifications_append_only ON execution_clarification_requests;
CREATE TRIGGER execution_clarifications_append_only
BEFORE UPDATE OR DELETE ON execution_clarification_requests
FOR EACH ROW EXECUTE FUNCTION reject_execution_result_mutation();

DROP TRIGGER IF EXISTS execution_dispositions_append_only ON execution_result_review_dispositions;
CREATE TRIGGER execution_dispositions_append_only
BEFORE UPDATE OR DELETE ON execution_result_review_dispositions
FOR EACH ROW EXECUTE FUNCTION reject_execution_result_mutation();
