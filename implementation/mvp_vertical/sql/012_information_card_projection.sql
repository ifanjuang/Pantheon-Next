CREATE TABLE IF NOT EXISTS agency_information_projection_metadata (
    information_id TEXT PRIMARY KEY REFERENCES agency_information_cards(information_id) ON DELETE CASCADE,
    source_date DATE,
    received_at TIMESTAMPTZ,
    issued_at TIMESTAMPTZ,
    media_types JSONB NOT NULL DEFAULT '["text"]'::jsonb,
    contact_refs JSONB NOT NULL DEFAULT '[]'::jsonb,
    revision INTEGER NOT NULL DEFAULT 1 CHECK (revision >= 1),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Compatibility for an unmerged earlier draft of this migration. The projection
-- must derive backing_mode from document links instead of storing a second truth.
ALTER TABLE agency_information_projection_metadata
    DROP COLUMN IF EXISTS backing_mode;

CREATE TABLE IF NOT EXISTS agency_information_document_links (
    information_id TEXT NOT NULL REFERENCES agency_information_cards(information_id) ON DELETE CASCADE,
    document_id TEXT NOT NULL REFERENCES source_documents(document_id) ON DELETE RESTRICT,
    role TEXT NOT NULL CHECK (role IN ('primary', 'supporting', 'attachment')),
    observed_version INTEGER CHECK (observed_version IS NULL OR observed_version >= 1),
    observed_digest TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (information_id, document_id)
);

CREATE INDEX IF NOT EXISTS agency_information_document_links_document_lookup
    ON agency_information_document_links (document_id, information_id);

CREATE TABLE IF NOT EXISTS agency_information_projection_events (
    event_id TEXT PRIMARY KEY,
    information_id TEXT NOT NULL REFERENCES agency_information_cards(information_id) ON DELETE RESTRICT,
    event_type TEXT NOT NULL CHECK (event_type IN ('projection_metadata_updated', 'document_link_added', 'document_link_removed')),
    actor TEXT NOT NULL,
    actor_kind TEXT NOT NULL CHECK (actor_kind IN ('human', 'system')),
    expected_revision INTEGER NOT NULL CHECK (expected_revision >= 0),
    resulting_revision INTEGER NOT NULL CHECK (resulting_revision = expected_revision + 1),
    idempotency_key TEXT NOT NULL UNIQUE,
    payload_digest TEXT NOT NULL,
    payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    result_snapshot JSONB NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION reject_agency_information_projection_event_mutation()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE EXCEPTION 'agency_information_projection_events is append-only';
END;
$$;

DROP TRIGGER IF EXISTS agency_information_projection_events_no_update ON agency_information_projection_events;
CREATE TRIGGER agency_information_projection_events_no_update
BEFORE UPDATE ON agency_information_projection_events
FOR EACH ROW EXECUTE FUNCTION reject_agency_information_projection_event_mutation();

DROP TRIGGER IF EXISTS agency_information_projection_events_no_delete ON agency_information_projection_events;
CREATE TRIGGER agency_information_projection_events_no_delete
BEFORE DELETE ON agency_information_projection_events
FOR EACH ROW EXECUTE FUNCTION reject_agency_information_projection_event_mutation();