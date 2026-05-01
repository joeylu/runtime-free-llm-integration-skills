# Gemini Request URLs

Use this file to resolve the final request URL after the connection profile and API surface are selected.

Read `../../_shared/request-url-matrix-schema.md` first.

## Current Matrix

| Request Kind | Model Scope | API Surface | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `catalog-selected` | `generate-content` | `official` | `POST` | `{Profile.Base URL}` | `/models/{model}:generateContent` | `{Profile.Base URL}/models/{model}:generateContent` | `n/a` | `verified` | `2026-05-01` | `https://ai.google.dev/api/generate-content` | `non-stream Gemini Developer API chat surface` |
| `vision` | `catalog-selected` | `generate-content` | `official` | `POST` | `{Profile.Base URL}` | `/models/{model}:generateContent` | `{Profile.Base URL}/models/{model}:generateContent` | `n/a` | `verified` | `2026-05-01` | `https://ai.google.dev/api/generate-content` | `vision inputs are content parts on the same surface` |
| `imaging` | `catalog-selected` | `generate-content` | `official` | `POST` | `{Profile.Base URL}` | `/models/{model}:generateContent` | `{Profile.Base URL}/models/{model}:generateContent` | `n/a` | `verified` | `2026-05-01` | `https://ai.google.dev/api/generate-content` | `Nano Banana rows use generateContent` |
| `chat` | `catalog-selected` | `stream-generate-content` | `official` | `POST` | `{Profile.Base URL}` | `/models/{model}:streamGenerateContent?alt=sse` | `{Profile.Base URL}/models/{model}:streamGenerateContent?alt=sse` | `separate-url` | `verified` | `2026-05-01` | `https://ai.google.dev/api/generate-content#method:-models.streamgeneratecontent` | `streaming chat path` |
| `vision` | `catalog-selected` | `stream-generate-content` | `official` | `POST` | `{Profile.Base URL}` | `/models/{model}:streamGenerateContent?alt=sse` | `{Profile.Base URL}/models/{model}:streamGenerateContent?alt=sse` | `separate-url` | `verified` | `2026-05-01` | `https://ai.google.dev/api/generate-content#method:-models.streamgeneratecontent` | `streaming vision path when capability matrix verifies it` |

## Rules

- Replace `{model}` with the exact `API Model` selected from `model-catalog.md`.
- Do not put the API key in `Request URL Template`; keep it in the configured credential path.
- Do not use Vertex AI regional URLs in this Gemini Developer API skill.
