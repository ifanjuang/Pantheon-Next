-- Structured human review of Project ChangeCandidates.
-- A revision request closes the current proposal without mutating the Project.

ALTER TABLE agency_change_candidates
    ADD COLUMN IF NOT EXISTS review_annotations JSONB NOT NULL DEFAULT '[]'::jsonb;
ALTER TABLE agency_change_candidates
    ADD COLUMN IF NOT EXISTS decision_note TEXT;

ALTER TABLE agency_change_candidates
    DROP CONSTRAINT IF EXISTS agency_change_candidates_status_check;
ALTER TABLE agency_change_candidates
    ADD CONSTRAINT agency_change_candidates_status_check
    CHECK (status IN ('pending_review', 'revision_requested', 'applied', 'rejected', 'stale'));

ALTER TABLE agency_change_candidate_events
    DROP CONSTRAINT IF EXISTS agency_change_candidate_events_event_type_check;
ALTER TABLE agency_change_candidate_events
    ADD CONSTRAINT agency_change_candidate_events_event_type_check
    CHECK (event_type IN ('proposed', 'revision_requested', 'applied', 'rejected', 'stale'));

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
          FROM pg_constraint
         WHERE conname = 'agency_change_candidates_review_annotations_check'
           AND conrelid = 'agency_change_candidates'::regclass
    ) THEN
        ALTER TABLE agency_change_candidates
            ADD CONSTRAINT agency_change_candidates_review_annotations_check
            CHECK (jsonb_typeof(review_annotations) = 'array');
    END IF;
END;
$$;
