-- Executable project-scoped APU owner for Project Anatomy H1.
--
-- This persistence stores an explicitly reviewed bootstrap dossier and exposes it
-- for server-side reads. It does not expose automatic stable-object creation,
-- admit Evidence, canonize claims, authorize tasks or let Hermes write APU state.

CREATE TABLE IF NOT EXISTS agency_apu_project_state (
    project_id TEXT PRIMARY KEY REFERENCES agency_projects(project_id) ON DELETE RESTRICT,
    revision INTEGER NOT NULL CHECK (revision >= 1),
    created_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS agency_apu_objects (
    object_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES agency_projects(project_id) ON DELETE RESTRICT,
    object_kind TEXT NOT NULL CHECK (
        object_kind IN ('space', 'boundary', 'opening', 'path', 'level', 'grid', 'vertical_connection')
    ),
    proof_status TEXT NOT NULL CHECK (proof_status IN (
        'candidate', 'source_missing', 'source_incomplete', 'source_complete_for_task',
        'source_superseded', 'contradictory_evidence', 'authority_too_low',
        'requires_more_evidence', 'accepted_as_support', 'rejected', 'obsolete', 'superseded'
    )),
    stable_object JSONB NOT NULL CHECK (jsonb_typeof(stable_object) = 'object'),
    object_identity JSONB CHECK (object_identity IS NULL OR jsonb_typeof(object_identity) = 'object'),
    payload_digest TEXT NOT NULL,
    revision INTEGER NOT NULL DEFAULT 1 CHECK (revision >= 1),
    created_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    retired_at TIMESTAMPTZ,
    retired_by TEXT,
    UNIQUE (project_id, object_id),
    CHECK (stable_object ->> 'stable_object_id' = object_id),
    CHECK (stable_object ->> 'kind' = object_kind),
    CHECK (stable_object ->> 'proof_status' = proof_status),
    CHECK (stable_object ->> 'scope_type' = 'project'),
    CHECK (stable_object ->> 'scope_id' = project_id),
    CHECK (
        object_identity IS NULL
        OR (
            object_identity ->> 'stable_id' = object_id
            AND object_identity ->> 'object_kind' = object_kind
        )
    ),
    CHECK (
        (retired_at IS NULL AND retired_by IS NULL)
        OR (retired_at IS NOT NULL AND retired_by IS NOT NULL)
    )
);

CREATE INDEX IF NOT EXISTS agency_apu_objects_project_lookup
    ON agency_apu_objects (project_id, retired_at, object_kind, object_id);

CREATE TABLE IF NOT EXISTS agency_apu_object_relations (
    relation_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES agency_projects(project_id) ON DELETE RESTRICT,
    relation_type TEXT NOT NULL CHECK (relation_type IN (
        'contains', 'part_of', 'located_in', 'mounted_on', 'hosted_by', 'faces',
        'serves', 'depends_on', 'adjacent_to', 'connected_to', 'separated_by',
        'opens_to', 'crosses', 'penetrates', 'aligns_with', 'above', 'below',
        'near', 'opposite', 'left_of', 'right_of', 'belongs_to_zone',
        'belongs_to_system', 'belongs_to_group', 'has_phase_state'
    )),
    from_object_id TEXT NOT NULL,
    to_object_id TEXT NOT NULL,
    relation_payload JSONB NOT NULL CHECK (jsonb_typeof(relation_payload) = 'object'),
    payload_digest TEXT NOT NULL,
    revision INTEGER NOT NULL DEFAULT 1 CHECK (revision >= 1),
    created_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    retired_at TIMESTAMPTZ,
    retired_by TEXT,
    UNIQUE (project_id, relation_id),
    FOREIGN KEY (project_id, from_object_id)
        REFERENCES agency_apu_objects(project_id, object_id) ON DELETE RESTRICT,
    FOREIGN KEY (project_id, to_object_id)
        REFERENCES agency_apu_objects(project_id, object_id) ON DELETE RESTRICT,
    CHECK (from_object_id <> to_object_id),
    CHECK (relation_payload ->> 'relation_id' = relation_id),
    CHECK (relation_payload ->> 'type' = relation_type),
    CHECK (relation_payload ->> 'from' = from_object_id),
    CHECK (relation_payload ->> 'to' = to_object_id),
    CHECK (
        (retired_at IS NULL AND retired_by IS NULL)
        OR (retired_at IS NOT NULL AND retired_by IS NOT NULL)
    )
);

CREATE INDEX IF NOT EXISTS agency_apu_relations_project_lookup
    ON agency_apu_object_relations (project_id, retired_at, relation_type, relation_id);
CREATE INDEX IF NOT EXISTS agency_apu_relations_from_lookup
    ON agency_apu_object_relations (project_id, from_object_id, retired_at);
CREATE INDEX IF NOT EXISTS agency_apu_relations_to_lookup
    ON agency_apu_object_relations (project_id, to_object_id, retired_at);

CREATE TABLE IF NOT EXISTS agency_apu_events (
    event_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES agency_projects(project_id) ON DELETE RESTRICT,
    event_type TEXT NOT NULL CHECK (event_type IN (
        'reviewed_dossier_imported',
        'source_match_applied',
        'object_retired',
        'relation_retired'
    )),
    expected_revision INTEGER NOT NULL CHECK (expected_revision >= 0),
    resulting_revision INTEGER NOT NULL CHECK (resulting_revision = expected_revision + 1),
    actor TEXT NOT NULL,
    idempotency_key TEXT NOT NULL UNIQUE,
    payload_digest TEXT NOT NULL,
    payload JSONB NOT NULL DEFAULT '{}'::jsonb CHECK (jsonb_typeof(payload) = 'object'),
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE INDEX IF NOT EXISTS agency_apu_events_project_lookup
    ON agency_apu_events (project_id, occurred_at, event_id);

CREATE OR REPLACE FUNCTION reject_agency_apu_event_mutation()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE EXCEPTION 'agency_apu_events are append-only';
END;
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'agency_apu_events_no_update'
          AND tgrelid = 'agency_apu_events'::regclass
    ) THEN
        CREATE TRIGGER agency_apu_events_no_update
        BEFORE UPDATE ON agency_apu_events
        FOR EACH ROW EXECUTE FUNCTION reject_agency_apu_event_mutation();
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'agency_apu_events_no_delete'
          AND tgrelid = 'agency_apu_events'::regclass
    ) THEN
        CREATE TRIGGER agency_apu_events_no_delete
        BEFORE DELETE ON agency_apu_events
        FOR EACH ROW EXECUTE FUNCTION reject_agency_apu_event_mutation();
    END IF;
END;
$$;
