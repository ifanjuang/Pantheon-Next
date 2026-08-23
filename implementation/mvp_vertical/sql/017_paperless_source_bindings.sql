CREATE TABLE IF NOT EXISTS paperless_source_bindings (
    document_id TEXT PRIMARY KEY REFERENCES source_documents(document_id) ON DELETE CASCADE,
    backing_resource TEXT NOT NULL DEFAULT 'paperless_ngx' CHECK (backing_resource = 'paperless_ngx'),
    paperless_document_id BIGINT NOT NULL CHECK (paperless_document_id > 0),
    paperless_version_id TEXT NOT NULL CHECK (length(paperless_version_id) > 0),
    storage_reference TEXT NOT NULL CHECK (length(storage_reference) > 0),
    original_filename TEXT NOT NULL CHECK (length(original_filename) > 0),
    source_digest TEXT NOT NULL CHECK (length(source_digest) > 0),
    bound_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS paperless_source_binding_external_lookup
    ON paperless_source_bindings (paperless_document_id, paperless_version_id);
