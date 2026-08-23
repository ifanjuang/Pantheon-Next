# OpenWebUI Document Card candidate

`pantheon_document_cards.py` is a read-only OpenWebUI Tool candidate. It calls
the internal Pantheon MVP cockpit API and returns persistent Rich UI embeds.

It exposes two tools:

- `list_project_documents(parent_project_id)`;
- `show_document_card(document_id)`.

The Tool does not connect to PostgreSQL or the NAS directly. It cannot ingest,
rename, move, approve, send or promote anything. Original previews use a
five-minute signed URL; the API key is never placed in the embedded HTML.

Install only after review by an OpenWebUI administrator. Configure its Valves:

```text
api_url = http://cockpit-api:8081
api_key = the same value as MVP_COCKPIT_API_KEY
```

The key field is masked. Enable OpenWebUI valve encryption as documented by
OpenWebUI if the deployment must also encrypt this value at rest.

The browser-facing preview address is configured separately on the API with
`MVP_COCKPIT_PUBLIC_URL`, for example `https://pantheon.local`.
