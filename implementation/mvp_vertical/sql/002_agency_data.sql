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
    owner_system TEXT NOT NULL DEFAULT 'postgres' CHECK (owner_system = 'postgres'),
    revision INTEGER NOT NULL DEFAULT 1 CHECK (revision >= 1),
    created_by TEXT NOT NULL,
    updated_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS agency_projects_code_lookup
    ON agency_projects (lower(code));
CREATE INDEX IF NOT EXISTS agency_projects_name_lookup
    ON agency_projects (lower(display_name));

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

CREATE TABLE IF NOT EXISTS agency_project_participations (
    participation_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES agency_projects(project_id) ON DELETE CASCADE,
    person_id TEXT REFERENCES agency_people(person_id) ON DELETE SET NULL,
    organization_id TEXT REFERENCES agency_organizations(organization_id) ON DELETE SET NULL,
    label TEXT,
    role TEXT NOT NULL,
    participation_type TEXT,
    owner_system TEXT NOT NULL DEFAULT 'postgres' CHECK (owner_system = 'postgres'),
    revision INTEGER NOT NULL DEFAULT 1 CHECK (revision >= 1),
    created_by TEXT NOT NULL,
    updated_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (person_id IS NOT NULL OR organization_id IS NOT NULL OR label IS NOT NULL)
);

CREATE INDEX IF NOT EXISTS agency_participations_project_lookup
    ON agency_project_participations (project_id, role);

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

CREATE OR REPLACE FUNCTION reject_agency_project_event_mutation()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE EXCEPTION 'agency_project_events are append-only';
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
END;
$$;
