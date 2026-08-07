-- H2: apply one explicitly authorized add_match_to_existing_object command.
--
-- Existing pre-H2 command rows remain readable but deliberately non-applicable:
-- their target revisions are NULL because no truthful historical freshness can be
-- reconstructed after the fact.

ALTER TABLE apu_write_command_candidates
    ADD COLUMN IF NOT EXISTS expected_owner_revision INTEGER;
ALTER TABLE apu_write_command_candidates
    ADD COLUMN IF NOT EXISTS expected_object_revision INTEGER;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'apu_write_command_owner_revision_positive'
          AND conrelid = 'apu_write_command_candidates'::regclass
    ) THEN
        ALTER TABLE apu_write_command_candidates
            ADD CONSTRAINT apu_write_command_owner_revision_positive
            CHECK (expected_owner_revision IS NULL OR expected_owner_revision >= 1);
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'apu_write_command_object_revision_positive'
          AND conrelid = 'apu_write_command_candidates'::regclass
    ) THEN
        ALTER TABLE apu_write_command_candidates
            ADD CONSTRAINT apu_write_command_object_revision_positive
            CHECK (expected_object_revision IS NULL OR expected_object_revision >= 1);
    END IF;
END;
$$;

ALTER TABLE agency_apu_events
    ADD COLUMN IF NOT EXISTS command_ref TEXT;
ALTER TABLE agency_apu_events
    ADD COLUMN IF NOT EXISTS authorization_ref TEXT;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'agency_apu_events_command_ref_fkey'
          AND conrelid = 'agency_apu_events'::regclass
    ) THEN
        ALTER TABLE agency_apu_events
            ADD CONSTRAINT agency_apu_events_command_ref_fkey
            FOREIGN KEY (command_ref)
            REFERENCES apu_write_command_candidates(command_id)
            ON DELETE RESTRICT;
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'agency_apu_events_authorization_ref_fkey'
          AND conrelid = 'agency_apu_events'::regclass
    ) THEN
        ALTER TABLE agency_apu_events
            ADD CONSTRAINT agency_apu_events_authorization_ref_fkey
            FOREIGN KEY (authorization_ref)
            REFERENCES apu_write_authorization_events(authorization_id)
            ON DELETE RESTRICT;
    END IF;
END;
$$;

CREATE UNIQUE INDEX IF NOT EXISTS agency_apu_source_match_command_once
    ON agency_apu_events (command_ref)
    WHERE event_type = 'source_match_applied' AND command_ref IS NOT NULL;

CREATE INDEX IF NOT EXISTS agency_apu_source_match_authorization_lookup
    ON agency_apu_events (authorization_ref)
    WHERE event_type = 'source_match_applied' AND authorization_ref IS NOT NULL;
