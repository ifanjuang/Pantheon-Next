-- Append-only reviews for individual APU mapping candidates.
-- A review can prepare a later write operation but never mutates APU itself.

CREATE TABLE IF NOT EXISTS apu_mapping_review_events (
    review_id TEXT PRIMARY KEY,
    execution_result_id TEXT NOT NULL REFERENCES execution_results(execution_result_id) ON DELETE RESTRICT,
    result_ref TEXT NOT NULL REFERENCES execution_result_items(result_id) ON DELETE RESTRICT,
    mapping_ref TEXT NOT NULL,
    action TEXT NOT NULL CHECK (action IN (
        'select_existing_object', 'mark_unmatched', 'needs_clarification', 'reject_mapping'
    )),
    selected_stable_object_ref TEXT,
    clarification_question TEXT,
    note TEXT,
    reviewer TEXT NOT NULL,
    idempotency_key TEXT NOT NULL UNIQUE,
    payload_digest TEXT NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (
        (action = 'select_existing_object' AND selected_stable_object_ref IS NOT NULL)
        OR (action <> 'select_existing_object' AND selected_stable_object_ref IS NULL)
    ),
    CHECK (
        (action = 'needs_clarification' AND clarification_question IS NOT NULL)
        OR action <> 'needs_clarification'
    )
);

CREATE OR REPLACE FUNCTION reject_apu_mapping_review_mutation()
RETURNS trigger AS $$
BEGIN
    RAISE EXCEPTION 'APU mapping review events are append-only';
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS apu_mapping_reviews_append_only ON apu_mapping_review_events;
CREATE TRIGGER apu_mapping_reviews_append_only
BEFORE UPDATE OR DELETE ON apu_mapping_review_events
FOR EACH ROW EXECUTE FUNCTION reject_apu_mapping_review_mutation();
