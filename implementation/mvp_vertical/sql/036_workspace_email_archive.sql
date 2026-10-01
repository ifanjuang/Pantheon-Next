-- Workspace e-mail archive technical projection.
--
-- This state coordinates a visible AFFAIRES HTML/attachment projection. It is
-- not Project identity, Evidence, professional truth or effect authorization.

CREATE TABLE IF NOT EXISTS workspace_email_bundles (
    bundle_id TEXT PRIMARY KEY,
    provider_account_ref TEXT NOT NULL CHECK (btrim(provider_account_ref) <> ''),
    gmail_thread_id TEXT NOT NULL CHECK (btrim(gmail_thread_id) <> ''),
    current_gmail_message_id TEXT NOT NULL CHECK (btrim(current_gmail_message_id) <> ''),
    current_raw_sha256 TEXT NOT NULL CHECK (current_raw_sha256 ~ '^[a-f0-9]{64}$'),
    source_id TEXT NOT NULL REFERENCES agency_sources(source_id) ON DELETE RESTRICT,
    affaire_name TEXT NOT NULL CHECK (btrim(affaire_name) <> ''),
    affaire_state TEXT NOT NULL CHECK (affaire_state IN ('active', 'archived')),
    destination_subdir TEXT NOT NULL,
    html_relative_path TEXT NOT NULL CHECK (btrim(html_relative_path) <> ''),
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    UNIQUE (provider_account_ref, gmail_thread_id)
);

CREATE INDEX IF NOT EXISTS workspace_email_bundles_source_lookup
    ON workspace_email_bundles (source_id, updated_at DESC);

CREATE TABLE IF NOT EXISTS workspace_email_visible_attachments (
    destination_key TEXT NOT NULL,
    content_sha256 TEXT NOT NULL CHECK (content_sha256 ~ '^[a-f0-9]{64}$'),
    byte_size BIGINT NOT NULL CHECK (byte_size >= 0),
    media_type TEXT,
    visible_relative_path TEXT NOT NULL CHECK (btrim(visible_relative_path) <> ''),
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    PRIMARY KEY (destination_key, content_sha256),
    UNIQUE (destination_key, visible_relative_path)
);

CREATE TABLE IF NOT EXISTS workspace_email_attachment_occurrences (
    provider_account_ref TEXT NOT NULL CHECK (btrim(provider_account_ref) <> ''),
    gmail_message_id TEXT NOT NULL CHECK (btrim(gmail_message_id) <> ''),
    mime_part_index INTEGER NOT NULL CHECK (mime_part_index >= 0),
    original_filename TEXT NOT NULL,
    content_sha256 TEXT NOT NULL CHECK (content_sha256 ~ '^[a-f0-9]{64}$'),
    byte_size BIGINT NOT NULL CHECK (byte_size >= 0),
    media_type TEXT,
    visible_relative_path TEXT NOT NULL CHECK (btrim(visible_relative_path) <> ''),
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    PRIMARY KEY (provider_account_ref, gmail_message_id, mime_part_index)
);

CREATE INDEX IF NOT EXISTS workspace_email_attachment_occurrences_digest_lookup
    ON workspace_email_attachment_occurrences (content_sha256, created_at);

COMMENT ON TABLE workspace_email_bundles IS
    'Mutable current visible Gmail-thread projection in AFFAIRES; it is not Source identity, Project identity or Evidence.';
COMMENT ON TABLE workspace_email_visible_attachments IS
    'Technical per-destination deduplication map for visible attachment projections.';
COMMENT ON TABLE workspace_email_attachment_occurrences IS
    'Per-message MIME occurrence provenance; same bytes may be referenced by many occurrences.';
