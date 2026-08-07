-- H4c: evolve the existing project-scoped APU owner to Project Anatomy V0.2.
--
-- The H1 identity table and H2 event history remain authoritative historical
-- records. V0.2 canonical payloads are added alongside V0.1 compatibility data;
-- no migration fabricates source representations, claims, Evidence or approval.

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_attribute
         WHERE attrelid = 'agency_apu_project_state'::regclass
           AND attname = 'model_version'
           AND NOT attisdropped
    ) THEN
        ALTER TABLE agency_apu_project_state
            ADD COLUMN model_version INTEGER NOT NULL DEFAULT 1;
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_attribute
         WHERE attrelid = 'agency_apu_project_state'::regclass
           AND attname = 'model_authority_ref'
           AND NOT attisdropped
    ) THEN
        ALTER TABLE agency_apu_project_state
            ADD COLUMN model_authority_ref TEXT;
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'agency_apu_project_state_model_version_check'
           AND conrelid = 'agency_apu_project_state'::regclass
    ) THEN
        ALTER TABLE agency_apu_project_state
            ADD CONSTRAINT agency_apu_project_state_model_version_check
            CHECK (model_version IN (1, 2));
    END IF;
END;
$$;

DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM pg_attribute
         WHERE attrelid = 'agency_apu_objects'::regclass
           AND attname = 'object_kind'
           AND attnotnull
    ) THEN
        ALTER TABLE agency_apu_objects ALTER COLUMN object_kind DROP NOT NULL;
    END IF;
    IF EXISTS (
        SELECT 1 FROM pg_attribute
         WHERE attrelid = 'agency_apu_objects'::regclass
           AND attname = 'proof_status'
           AND attnotnull
    ) THEN
        ALTER TABLE agency_apu_objects ALTER COLUMN proof_status DROP NOT NULL;
    END IF;
    IF EXISTS (
        SELECT 1 FROM pg_attribute
         WHERE attrelid = 'agency_apu_objects'::regclass
           AND attname = 'stable_object'
           AND attnotnull
    ) THEN
        ALTER TABLE agency_apu_objects ALTER COLUMN stable_object DROP NOT NULL;
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_attribute
         WHERE attrelid = 'agency_apu_objects'::regclass
           AND attname = 'object_family'
           AND NOT attisdropped
    ) THEN
        ALTER TABLE agency_apu_objects ADD COLUMN object_family TEXT;
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_attribute
         WHERE attrelid = 'agency_apu_objects'::regclass
           AND attname = 'canonical_stable_object'
           AND NOT attisdropped
    ) THEN
        ALTER TABLE agency_apu_objects ADD COLUMN canonical_stable_object JSONB;
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_attribute
         WHERE attrelid = 'agency_apu_objects'::regclass
           AND attname = 'canonical_payload_digest'
           AND NOT attisdropped
    ) THEN
        ALTER TABLE agency_apu_objects ADD COLUMN canonical_payload_digest TEXT;
    END IF;
END;
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'agency_apu_objects_v02_family_check'
           AND conrelid = 'agency_apu_objects'::regclass
    ) THEN
        ALTER TABLE agency_apu_objects
            ADD CONSTRAINT agency_apu_objects_v02_family_check
            CHECK (
                object_family IS NULL OR object_family IN (
                    'spatial', 'element', 'assembly', 'material',
                    'system', 'datum', 'group', 'type_definition'
                )
            );
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'agency_apu_objects_v02_payload_check'
           AND conrelid = 'agency_apu_objects'::regclass
    ) THEN
        ALTER TABLE agency_apu_objects
            ADD CONSTRAINT agency_apu_objects_v02_payload_check
            CHECK (
                canonical_stable_object IS NULL OR (
                    jsonb_typeof(canonical_stable_object) = 'object'
                    AND canonical_stable_object ->> 'stable_object_id' = object_id
                    AND canonical_stable_object ->> 'project_ref' = project_id
                    AND canonical_stable_object ->> 'object_family' = object_family
                    AND canonical_payload_digest IS NOT NULL
                )
            );
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
         WHERE conname = 'agency_apu_objects_has_identity_payload'
           AND conrelid = 'agency_apu_objects'::regclass
    ) THEN
        ALTER TABLE agency_apu_objects
            ADD CONSTRAINT agency_apu_objects_has_identity_payload
            CHECK (stable_object IS NOT NULL OR canonical_stable_object IS NOT NULL);
    END IF;
END;
$$;

CREATE INDEX IF NOT EXISTS agency_apu_objects_v02_project_lookup
    ON agency_apu_objects (project_id, object_family, object_id)
    WHERE canonical_stable_object IS NOT NULL;

CREATE TABLE IF NOT EXISTS agency_apu_source_representations (
    representation_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES agency_projects(project_id) ON DELETE RESTRICT,
    source_kind TEXT NOT NULL CHECK (
        source_kind IN (
            'revit', 'ifc', 'drawing', 'drawing_takeoff', 'image',
            'photo', 'manual', 'scan', 'point_cloud', 'other'
        )
    ),
    proof_status TEXT NOT NULL CHECK (proof_status IN (
        'candidate', 'source_missing', 'source_incomplete', 'source_complete_for_task',
        'source_superseded', 'contradictory_evidence', 'authority_too_low',
        'requires_more_evidence', 'accepted_as_support', 'rejected', 'obsolete', 'superseded'
    )),
    representation_payload JSONB NOT NULL CHECK (jsonb_typeof(representation_payload) = 'object'),
    payload_digest TEXT NOT NULL,
    revision INTEGER NOT NULL DEFAULT 1 CHECK (revision >= 1),
    created_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    CHECK (representation_payload ->> 'representation_id' = representation_id),
    CHECK (representation_payload ->> 'project_ref' = project_id),
    CHECK (representation_payload ->> 'source_kind' = source_kind),
    CHECK (representation_payload ->> 'proof_status' = proof_status),
    UNIQUE (project_id, representation_id)
);

CREATE INDEX IF NOT EXISTS agency_apu_source_representations_project_lookup
    ON agency_apu_source_representations (project_id, source_kind, representation_id);

CREATE TABLE IF NOT EXISTS agency_apu_attribute_claims (
    claim_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES agency_projects(project_id) ON DELETE RESTRICT,
    subject_entity_type TEXT NOT NULL CHECK (
        subject_entity_type IN ('stable_object', 'source_representation')
    ),
    subject_entity_id TEXT NOT NULL,
    attribute_key TEXT NOT NULL,
    assertion_mode TEXT NOT NULL CHECK (
        assertion_mode IN ('observed', 'proposed', 'derived', 'human_asserted', 'as_built')
    ),
    source_authority TEXT NOT NULL,
    proof_status TEXT NOT NULL,
    claim_payload JSONB NOT NULL CHECK (jsonb_typeof(claim_payload) = 'object'),
    payload_digest TEXT NOT NULL,
    created_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    CHECK (claim_payload ->> 'attribute_claim_id' = claim_id),
    CHECK (claim_payload -> 'subject_ref' ->> 'entity_type' = subject_entity_type),
    CHECK (claim_payload -> 'subject_ref' ->> 'entity_id' = subject_entity_id),
    CHECK (claim_payload ->> 'attribute_key' = attribute_key)
);

CREATE INDEX IF NOT EXISTS agency_apu_attribute_claims_subject_lookup
    ON agency_apu_attribute_claims (project_id, subject_entity_type, subject_entity_id, attribute_key);

CREATE TABLE IF NOT EXISTS agency_apu_relation_claims (
    claim_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES agency_projects(project_id) ON DELETE RESTRICT,
    subject_entity_type TEXT NOT NULL CHECK (
        subject_entity_type IN ('stable_object', 'source_representation')
    ),
    subject_entity_id TEXT NOT NULL,
    relation_type TEXT NOT NULL CHECK (relation_type ~ '^[a-z][a-z0-9_.-]*$'),
    object_entity_type TEXT NOT NULL CHECK (
        object_entity_type IN ('stable_object', 'source_representation')
    ),
    object_entity_id TEXT NOT NULL,
    assertion_mode TEXT NOT NULL CHECK (
        assertion_mode IN ('observed', 'proposed', 'derived', 'human_asserted', 'as_built')
    ),
    source_authority TEXT NOT NULL,
    proof_status TEXT NOT NULL,
    claim_payload JSONB NOT NULL CHECK (jsonb_typeof(claim_payload) = 'object'),
    payload_digest TEXT NOT NULL,
    created_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    CHECK (claim_payload ->> 'relation_claim_id' = claim_id),
    CHECK (claim_payload -> 'subject_ref' ->> 'entity_type' = subject_entity_type),
    CHECK (claim_payload -> 'subject_ref' ->> 'entity_id' = subject_entity_id),
    CHECK (claim_payload ->> 'relation_type' = relation_type),
    CHECK (claim_payload -> 'object_ref' ->> 'entity_type' = object_entity_type),
    CHECK (claim_payload -> 'object_ref' ->> 'entity_id' = object_entity_id),
    CHECK (
        relation_type <> 'identity.represents'
        OR (
            subject_entity_type = 'source_representation'
            AND object_entity_type = 'stable_object'
        )
    )
);

CREATE INDEX IF NOT EXISTS agency_apu_relation_claims_subject_lookup
    ON agency_apu_relation_claims (project_id, subject_entity_type, subject_entity_id, relation_type);
CREATE INDEX IF NOT EXISTS agency_apu_relation_claims_object_lookup
    ON agency_apu_relation_claims (project_id, object_entity_type, object_entity_id, relation_type);

CREATE TABLE IF NOT EXISTS agency_apu_v02_owner_migrations (
    migration_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES agency_projects(project_id) ON DELETE RESTRICT,
    from_version INTEGER NOT NULL CHECK (from_version = 1),
    to_version INTEGER NOT NULL CHECK (to_version = 2),
    owner_revision INTEGER NOT NULL CHECK (owner_revision >= 1),
    source_authority_ref TEXT NOT NULL,
    compatibility_report JSONB NOT NULL CHECK (jsonb_typeof(compatibility_report) = 'object'),
    payload_digest TEXT NOT NULL,
    actor TEXT NOT NULL,
    idempotency_key TEXT NOT NULL UNIQUE,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    UNIQUE (project_id, to_version)
);

CREATE OR REPLACE FUNCTION agency_apu_v02_entity_exists(
    expected_project_id TEXT,
    entity_type_value TEXT,
    entity_id_value TEXT
)
RETURNS BOOLEAN
LANGUAGE plpgsql
STABLE
AS $$
DECLARE
    found BOOLEAN;
BEGIN
    IF entity_type_value = 'stable_object' THEN
        SELECT EXISTS (
            SELECT 1 FROM agency_apu_objects
             WHERE project_id = expected_project_id
               AND object_id = entity_id_value
               AND canonical_stable_object IS NOT NULL
        ) INTO found;
        RETURN found;
    ELSIF entity_type_value = 'source_representation' THEN
        SELECT EXISTS (
            SELECT 1 FROM agency_apu_source_representations
             WHERE project_id = expected_project_id
               AND representation_id = entity_id_value
        ) INTO found;
        RETURN found;
    END IF;
    RETURN FALSE;
END;
$$;

CREATE OR REPLACE FUNCTION validate_agency_apu_v02_attribute_claim()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT agency_apu_v02_entity_exists(
        NEW.project_id, NEW.subject_entity_type, NEW.subject_entity_id
    ) THEN
        RAISE EXCEPTION 'V0.2 attribute claim subject is unknown or belongs to another Project';
    END IF;
    RETURN NEW;
END;
$$;

CREATE OR REPLACE FUNCTION validate_agency_apu_v02_relation_claim()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT agency_apu_v02_entity_exists(
        NEW.project_id, NEW.subject_entity_type, NEW.subject_entity_id
    ) THEN
        RAISE EXCEPTION 'V0.2 relation claim subject is unknown or belongs to another Project';
    END IF;
    IF NOT agency_apu_v02_entity_exists(
        NEW.project_id, NEW.object_entity_type, NEW.object_entity_id
    ) THEN
        RAISE EXCEPTION 'V0.2 relation claim object is unknown or belongs to another Project';
    END IF;
    RETURN NEW;
END;
$$;

CREATE OR REPLACE FUNCTION reject_agency_apu_v02_record_mutation()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE EXCEPTION 'Project Anatomy V0.2 source/claim/migration records are append-only';
END;
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
         WHERE tgname = 'agency_apu_attribute_claims_validate'
           AND tgrelid = 'agency_apu_attribute_claims'::regclass
    ) THEN
        CREATE TRIGGER agency_apu_attribute_claims_validate
        BEFORE INSERT ON agency_apu_attribute_claims
        FOR EACH ROW EXECUTE FUNCTION validate_agency_apu_v02_attribute_claim();
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
         WHERE tgname = 'agency_apu_relation_claims_validate'
           AND tgrelid = 'agency_apu_relation_claims'::regclass
    ) THEN
        CREATE TRIGGER agency_apu_relation_claims_validate
        BEFORE INSERT ON agency_apu_relation_claims
        FOR EACH ROW EXECUTE FUNCTION validate_agency_apu_v02_relation_claim();
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
         WHERE tgname = 'agency_apu_source_representations_append_only'
           AND tgrelid = 'agency_apu_source_representations'::regclass
    ) THEN
        CREATE TRIGGER agency_apu_source_representations_append_only
        BEFORE UPDATE OR DELETE ON agency_apu_source_representations
        FOR EACH ROW EXECUTE FUNCTION reject_agency_apu_v02_record_mutation();
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
         WHERE tgname = 'agency_apu_attribute_claims_append_only'
           AND tgrelid = 'agency_apu_attribute_claims'::regclass
    ) THEN
        CREATE TRIGGER agency_apu_attribute_claims_append_only
        BEFORE UPDATE OR DELETE ON agency_apu_attribute_claims
        FOR EACH ROW EXECUTE FUNCTION reject_agency_apu_v02_record_mutation();
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
         WHERE tgname = 'agency_apu_relation_claims_append_only'
           AND tgrelid = 'agency_apu_relation_claims'::regclass
    ) THEN
        CREATE TRIGGER agency_apu_relation_claims_append_only
        BEFORE UPDATE OR DELETE ON agency_apu_relation_claims
        FOR EACH ROW EXECUTE FUNCTION reject_agency_apu_v02_record_mutation();
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
         WHERE tgname = 'agency_apu_v02_owner_migrations_append_only'
           AND tgrelid = 'agency_apu_v02_owner_migrations'::regclass
    ) THEN
        CREATE TRIGGER agency_apu_v02_owner_migrations_append_only
        BEFORE UPDATE OR DELETE ON agency_apu_v02_owner_migrations
        FOR EACH ROW EXECUTE FUNCTION reject_agency_apu_v02_record_mutation();
    END IF;
END;
$$;
