ALTER TABLE hermes_execution_admissions
    ADD COLUMN IF NOT EXISTS work_issue_version INTEGER;

ALTER TABLE hermes_execution_admissions
    ADD COLUMN IF NOT EXISTS ttl_seconds INTEGER;

ALTER TABLE hermes_execution_admissions
    ADD COLUMN IF NOT EXISTS expires_at TIMESTAMPTZ;

CREATE TABLE IF NOT EXISTS hermes_execution_admission_events (
    event_id TEXT PRIMARY KEY,
    admission_id TEXT NOT NULL REFERENCES hermes_execution_admissions(admission_id) ON DELETE RESTRICT,
    event_type TEXT NOT NULL CHECK (event_type = 'revoked'),
    actor TEXT NOT NULL,
    reason TEXT NOT NULL,
    idempotency_key TEXT NOT NULL UNIQUE,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS hermes_execution_admission_events_lookup
    ON hermes_execution_admission_events (admission_id, occurred_at DESC);

CREATE UNIQUE INDEX IF NOT EXISTS hermes_execution_admission_single_revocation
    ON hermes_execution_admission_events (admission_id)
    WHERE event_type = 'revoked';

CREATE OR REPLACE FUNCTION reject_hermes_execution_admission_event_mutation()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE EXCEPTION 'hermes_execution_admission_events are append-only';
END;
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'hermes_execution_admission_events_no_update'
          AND tgrelid = 'hermes_execution_admission_events'::regclass
    ) THEN
        CREATE TRIGGER hermes_execution_admission_events_no_update
        BEFORE UPDATE ON hermes_execution_admission_events
        FOR EACH ROW EXECUTE FUNCTION reject_hermes_execution_admission_event_mutation();
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'hermes_execution_admission_events_no_delete'
          AND tgrelid = 'hermes_execution_admission_events'::regclass
    ) THEN
        CREATE TRIGGER hermes_execution_admission_events_no_delete
        BEFORE DELETE ON hermes_execution_admission_events
        FOR EACH ROW EXECUTE FUNCTION reject_hermes_execution_admission_event_mutation();
    END IF;
END;
$$;
