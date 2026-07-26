CREATE EXTENSION IF NOT EXISTS unaccent;

CREATE TABLE IF NOT EXISTS agency_projects (
    project_id TEXT PRIMARY KEY,
    code TEXT NOT NULL UNIQUE,
    display_name TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    status TEXT,
    phase TEXT,
    location TEXT,
    primary_client TEXT,
    tags JSONB NOT NULL DEFAULT '[]'::jsonb,
    contacts JSONB NOT NULL DEFAULT '[]'::jsonb,
    attributes JSONB NOT NULL DEFAULT '{}'::jsonb,
    owner_system TEXT NOT NULL DEFAULT 'postgres' CHECK (owner_system = 'postgres'),
    revision INTEGER NOT NULL DEFAULT 1 CHECK (revision >= 1),
    created_by TEXT NOT NULL,
    updated_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Existing development databases may predate the extensible Project fields.
ALTER TABLE agency_projects
    ADD COLUMN IF NOT EXISTS contacts JSONB NOT NULL DEFAULT '[]'::jsonb;
ALTER TABLE agency_projects
    ADD COLUMN IF NOT EXISTS attributes JSONB NOT NULL DEFAULT '{}'::jsonb;

CREATE INDEX IF NOT EXISTS agency_projects_code_lookup
    ON agency_projects (lower(code));
CREATE INDEX IF NOT EXISTS agency_projects_name_lookup
    ON agency_projects (lower(display_name));

-- People and Organizations remain optional directory sources. They are not
-- related to projects by a participation table; each Project owns its current
-- contacts snapshot in agency_projects.contacts.
CREATE TABLE IF NOT EXISTS agency_people (
    person_id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    address TEXT,
    owner_system TEXT NOT NULL DEFAULT 'postgres' CHECK (owner_system = 'postgres'),
    revision INTEGER NOT NULL DEFAULT 1 CHECK (revision >= 1),
    created_by TEXT NOT NULL,
    updated_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS agency_organizations (
    organization_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    address TEXT,
    siret TEXT,
    owner_system TEXT NOT NULL DEFAULT 'postgres' CHECK (owner_system = 'postgres'),
    revision INTEGER NOT NULL DEFAULT 1 CHECK (revision >= 1),
    created_by TEXT NOT NULL,
    updated_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Retired legacy model. This repository is still pre-production; keeping a
-- second project/contact model would create sync ambiguity, so schema init
-- removes the obsolete relation table when upgrading an existing dev database.
DROP TABLE IF EXISTS agency_project_participations;

-- Unified Information card. A source revision owns one visible index. Editing
-- summary/details never changes that index. Once acted, the row is immutable at
-- the domain layer; a later source creates one new working row in the same series.
CREATE TABLE IF NOT EXISTS agency_information_cards (
    information_id TEXT PRIMARY KEY,
    series_id TEXT NOT NULL,
    project_id TEXT NOT NULL REFERENCES agency_projects(project_id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    source_type TEXT NOT NULL,
    source_ref TEXT,
    source_note TEXT,
    source_version TEXT,
    index_label TEXT NOT NULL,
    information_date DATE,
    summary TEXT NOT NULL DEFAULT '',
    details TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL CHECK (status IN ('draft', 'in_progress', 'acted', 'superseded')),
    limits JSONB NOT NULL DEFAULT '[]'::jsonb,
    type_tags JSONB NOT NULL DEFAULT '[]'::jsonb,
    subject_tags JSONB NOT NULL DEFAULT '[]'::jsonb,
    author TEXT,
    base_acted_id TEXT REFERENCES agency_information_cards(information_id) ON DELETE RESTRICT,
    previous_source_id TEXT REFERENCES agency_information_cards(information_id) ON DELETE RESTRICT,
    revision INTEGER NOT NULL DEFAULT 1 CHECK (revision >= 1),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    acted_at TIMESTAMPTZ,
    CHECK (source_ref IS NOT NULL OR source_note IS NOT NULL),
    CHECK ((status = 'acted' AND acted_at IS NOT NULL) OR status <> 'acted')
);

CREATE INDEX IF NOT EXISTS agency_information_project_lookup
    ON agency_information_cards (project_id, series_id, created_at DESC);

CREATE UNIQUE INDEX IF NOT EXISTS agency_information_one_working_version
    ON agency_information_cards (series_id)
    WHERE status IN ('draft', 'in_progress');

CREATE UNIQUE INDEX IF NOT EXISTS agency_information_one_current_acted
    ON agency_information_cards (series_id)
    WHERE status = 'acted';

CREATE TABLE IF NOT EXISTS agency_project_events (
    event_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES agency_projects(project_id) ON DELETE RESTRICT,
    event_type TEXT NOT NULL CHECK (event_type IN ('project_created', 'project_updated')),
    actor TEXT NOT NULL,
    actor_kind TEXT NOT NULL CHECK (actor_kind IN ('human', 'hermes', 'system')),
    expected_revision INTEGER NOT NULL CHECK (expected_revision >= 0),
    resulting_revision INTEGER NOT NULL CHECK (resulting_revision = expected_revision + 1),
    idempotency_key TEXT NOT NULL UNIQUE,
    payload_digest TEXT NOT NULL,
    payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    result_snapshot JSONB NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- A ChangeCandidate is an envelope around a proposed Project-attributes change.
-- The Project keeps its own business status; candidate status never replaces it.
CREATE TABLE IF NOT EXISTS agency_change_candidates (
    candidate_id TEXT PRIMARY KEY,
    entity_type TEXT NOT NULL CHECK (entity_type = 'project'),
    entity_id TEXT NOT NULL REFERENCES agency_projects(project_id) ON DELETE RESTRICT,
    base_revision INTEGER NOT NULL CHECK (base_revision >= 1),
    proposer TEXT NOT NULL,
    proposer_kind TEXT NOT NULL CHECK (proposer_kind IN ('human', 'hermes', 'system')),
    changes JSONB NOT NULL,
    reason TEXT,
    source_refs JSONB NOT NULL DEFAULT '[]'::jsonb,
    proposal_digest TEXT NOT NULL,
    idempotency_key TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL CHECK (status IN ('pending_review', 'applied', 'rejected', 'stale')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    decided_at TIMESTAMPTZ,
    decided_by TEXT,
    applied_revision INTEGER,
    CHECK (jsonb_typeof(changes) = 'array'),
    CHECK (jsonb_typeof(source_refs) = 'array')
);

CREATE INDEX IF NOT EXISTS agency_change_candidates_project_lookup
    ON agency_change_candidates (entity_id, status, created_at DESC);

CREATE TABLE IF NOT EXISTS agency_change_candidate_events (
    event_id TEXT PRIMARY KEY,
    candidate_id TEXT NOT NULL REFERENCES agency_change_candidates(candidate_id) ON DELETE RESTRICT,
    event_type TEXT NOT NULL CHECK (event_type IN ('proposed', 'applied', 'rejected', 'stale')),
    actor TEXT NOT NULL,
    actor_kind TEXT NOT NULL CHECK (actor_kind IN ('human', 'hermes', 'system')),
    idempotency_key TEXT NOT NULL UNIQUE,
    payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION reject_agency_project_event_mutation()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE EXCEPTION 'agency_project_events are append-only';
END;
$$;

CREATE OR REPLACE FUNCTION reject_agency_change_candidate_event_mutation()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE EXCEPTION 'agency_change_candidate_events are append-only';
END;
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'agency_project_events_no_update'
          AND tgrelid = 'agency_project_events'::regclass
    ) THEN
        CREATE TRIGGER agency_project_events_no_update
        BEFORE UPDATE ON agency_project_events
        FOR EACH ROW EXECUTE FUNCTION reject_agency_project_event_mutation();
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'agency_project_events_no_delete'
          AND tgrelid = 'agency_project_events'::regclass
    ) THEN
        CREATE TRIGGER agency_project_events_no_delete
        BEFORE DELETE ON agency_project_events
        FOR EACH ROW EXECUTE FUNCTION reject_agency_project_event_mutation();
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'agency_change_candidate_events_no_update'
          AND tgrelid = 'agency_change_candidate_events'::regclass
    ) THEN
        CREATE TRIGGER agency_change_candidate_events_no_update
        BEFORE UPDATE ON agency_change_candidate_events
        FOR EACH ROW EXECUTE FUNCTION reject_agency_change_candidate_event_mutation();
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'agency_change_candidate_events_no_delete'
          AND tgrelid = 'agency_change_candidate_events'::regclass
    ) THEN
        CREATE TRIGGER agency_change_candidate_events_no_delete
        BEFORE DELETE ON agency_change_candidate_events
        FOR EACH ROW EXECUTE FUNCTION reject_agency_change_candidate_event_mutation();
    END IF;
END;
$$;
