from implementation.labs.google_drive_read.adapter import (
    AUTHORITY,
    DriveReadScope,
    GoogleDriveReadError,
    direct_google_list_request,
    nango_google_list_request,
    normalize_list_response,
)


def _payload(**overrides):
    payload = {
        "incompleteSearch": False,
        "files": [
            {
                "id": "file-1",
                "name": "CCTP.pdf",
                "mimeType": "application/pdf",
                "parents": ["folder-a"],
                "modifiedTime": "2026-09-02T05:00:00Z",
                "version": "17",
                "webViewLink": "https://drive.google.com/file/d/file-1/view",
                "md5Checksum": "abc123",
                "trashed": False,
            }
        ],
    }
    payload.update(overrides)
    return payload


def test_direct_and_nango_use_same_bounded_drive_query_semantics():
    scope = DriveReadScope(folder_id="folder-a", drive_id="drive-1")
    direct = direct_google_list_request(scope)
    nango = nango_google_list_request(
        scope,
        provider_config_key="google-drive-project",
        connection_id="opaque-connection",
    )

    assert direct["method"] == "GET"
    assert nango["method"] == "GET"
    assert direct["params"] == nango["params"]
    assert direct["params"]["q"] == "'folder-a' in parents and trashed = false"
    assert direct["params"]["corpora"] == "drive"
    assert direct["params"]["driveId"] == "drive-1"
    assert direct["params"]["includeItemsFromAllDrives"] is True
    assert direct["params"]["supportsAllDrives"] is True


def test_normalization_preserves_locator_but_does_not_create_source_digest():
    candidate = normalize_list_response(DriveReadScope("folder-a"), _payload())[0]

    assert candidate.source_locator == "gdrive://file/file-1"
    assert candidate.content_checksum == "abc123"
    assert candidate.provider_version == "17"
    assert candidate.requires_content_hash is True
    assert not hasattr(candidate, "source_digest")


def test_google_native_document_without_md5_still_requires_content_hash():
    payload = _payload()
    payload["files"][0].update(
        {
            "name": "Compte rendu",
            "mimeType": "application/vnd.google-apps.document",
            "md5Checksum": None,
        }
    )

    candidate = normalize_list_response(DriveReadScope("folder-a"), payload)[0]
    assert candidate.content_checksum is None
    assert candidate.requires_content_hash is True


def test_out_of_scope_item_fails_closed_even_if_provider_returns_it():
    payload = _payload()
    payload["files"][0]["parents"] = ["folder-b"]

    try:
        normalize_list_response(DriveReadScope("folder-a"), payload)
    except GoogleDriveReadError as exc:
        assert "outside explicit folder scope" in str(exc)
    else:
        raise AssertionError("out-of-scope provider result was accepted")


def test_incomplete_search_fails_closed():
    try:
        normalize_list_response(DriveReadScope("folder-a"), _payload(incompleteSearch=True))
    except GoogleDriveReadError as exc:
        assert "incomplete" in str(exc)
    else:
        raise AssertionError("incomplete provider inventory was accepted")


def test_trashed_item_fails_closed():
    payload = _payload()
    payload["files"][0]["trashed"] = True

    try:
        normalize_list_response(DriveReadScope("folder-a"), payload)
    except GoogleDriveReadError as exc:
        assert "trashed" in str(exc)
    else:
        raise AssertionError("trashed provider item was accepted")


def test_shared_drive_mismatch_fails_closed():
    payload = _payload()
    payload["files"][0]["driveId"] = "drive-b"

    try:
        normalize_list_response(DriveReadScope("folder-a", "drive-a"), payload)
    except GoogleDriveReadError as exc:
        assert "shared-drive scope" in str(exc)
    else:
        raise AssertionError("cross-drive provider item was accepted")


def test_lab_exposes_no_write_or_authority_surface():
    assert AUTHORITY == {
        "read_only": True,
        "owns_credentials": False,
        "admits_source": False,
        "creates_source_digest": False,
        "decides_currentness": False,
        "admits_evidence": False,
        "authorizes": False,
        "persists_state": False,
        "write_surface": False,
    }
