-- H2: apply one explicitly authorized add_match_to_existing_object command.
--
-- Existing pre-H2 command rows remain readable but deliberately non-applicable:
-- their target revisions are NULL because no truthful historical freshness can be
-- reconstructed after the fact.
--
-- Composed startup replays migrations, so every schema evolution below is guarded
-- on the catalog. No already-applied startup should reacquire an unnecessary
-- ACCESS EXCLUSIVE lock merely to discover that the column or constraint exists.

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
         WHERE table_name = 'apu_write_command_candidates'
           AND column_name = 'expected_owner_revision'
    ) THEN
        ALTER TABLE apu_write_command_candidates
            ADD COLUMN expected_owner_revision INTEGER;
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
         WHERE table_name = 'apu_write_command_candidates'
           AND column_name = 'expected_object_revision'
    ) THEN
        ALTER TABLE apu_write_command_candidates
            ADD COLUMN expected_object_revision INTEGER;
    END IF;
END;
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'apu_write_command_owner_revision_positive'
           AND conrelid = 'apu_write_command_candidates'::regclass
    ) THEN
        ALTER TABLE apu_write_command_candidates
            ADD CONSTRAINT apu_write_command_owner_revision_positive
            CHECK (expected_owner_revision IS NULL OR expected_owner_revision >= 1)
            NOT VALID;
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'apu_write_command_object_revision_positive'
           AND conrelid = 'apu_write_command_candidates'::regclass
    ) THEN
        ALTER TABLE apu_write_command_candidates
            ADD CONSTRAINT apu_write_command_object_revision_positive
            CHECK (expected_object_revision IS NULL OR expected_object_revision >= 1)
            NOT VALID;
    END IF;

    IF EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'apu_write_command_owner_revision_positive'
           AND conrelid = 'apu_write_command_candidates'::regclass
           AND NOT convalidated
    ) THEN
        ALTER TABLE apu_write_command_candidates
            VALIDATE CONSTRAINT apu_write_command_owner_revision_positive;
    END IF;
    IF EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'apu_write_command_object_revision_positive'
           AND conrelid = 'apu_write_command_candidates'::regclass
           AND NOT convalidated
    ) THEN
        ALTER TABLE apu_write_command_candidates
            VALIDATE CONSTRAINT apu_write_command_object_revision_positive;
    END IF;
END;
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
         WHERE table_name = 'agency_apu_events'
           AND column_name = 'command_ref'
    ) THEN
        ALTER TABLE agency_apu_events ADD COLUMN command_ref TEXT;
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
         WHERE table_name = 'agency_apu_events'
           AND column_name = 'authorization_ref'
    ) THEN
        ALTER TABLE agency_apu_events ADD COLUMN authorization_ref TEXT;
    END IF;
END;
$$;

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
            ON DELETE RESTRICT NOT VALID;
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
            ON DELETE RESTRICT NOT VALID;
    END IF;

    IF EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'agency_apu_events_command_ref_fkey'
           AND conrelid = 'agency_apu_events'::regclass
           AND NOT convalidated
    ) THEN
        ALTER TABLE agency_apu_events
            VALIDATE CONSTRAINT agency_apu_events_command_ref_fkey;
    END IF;
    IF EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'agency_apu_events_authorization_ref_fkey'
           AND conrelid = 'agency_apu_events'::regclass
           AND NOT convalidated
    ) THEN
        ALTER TABLE agency_apu_events
            VALIDATE CONSTRAINT agency_apu_events_authorization_ref_fkey;
    END IF;
END;
$$;

CREATE UNIQUE INDEX IF NOT EXISTS agency_apu_source_match_command_once
    ON agency_apu_events (command_ref)
    WHERE event_type = 'source_match_applied' AND command_ref IS NOT NULL;

CREATE INDEX IF NOT EXISTS agency_apu_source_match_authorization_lookup
    ON agency_apu_events (authorization_ref)
    WHERE event_type = 'source_match_applied' AND authorization_ref IS NOT NULL;
