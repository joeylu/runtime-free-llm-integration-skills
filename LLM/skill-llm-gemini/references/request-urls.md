# Gemini Request URLs

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat,vision,imaging` | `all retained models` | `interactions` | `v1` | `official` | `POST` | `https://generativelanguage.googleapis.com` | `/v1/interactions` | `https://generativelanguage.googleapis.com/v1/interactions` | `body-param` | `verified` | 2026-08-06 | `https://ai.google.dev/api/interactions-api` | `Stable Interactions route; current steps schema.` |
| `chat,vision,imaging` | `all retained models` | `interactions` | `v1beta` | `official` | `POST` | `https://generativelanguage.googleapis.com` | `/v1beta/interactions` | `https://generativelanguage.googleapis.com/v1beta/interactions` | `body-param` | `verified` | 2026-08-06 | `https://ai.google.dev/api/interactions-api` | `Beta compatibility route; never switch from v1 implicitly.` |
| `chat,vision,imaging` | `all retained models` | `generate-content` | `v1beta` | `official` | `POST` | `https://generativelanguage.googleapis.com` | `/v1beta/models/{model}:generateContent` | `https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent` | `n/a` | `verified` | 2026-08-06 | `https://ai.google.dev/api/generate-content` | `Non-stream GenerateContent.` |
| `chat,vision` | `gemini-3.6-flash,gemini-3.1-pro-preview` | `stream-generate-content` | `v1beta` | `official` | `POST` | `https://generativelanguage.googleapis.com` | `/v1beta/models/{model}:streamGenerateContent?alt=sse` | `https://generativelanguage.googleapis.com/v1beta/models/{model}:streamGenerateContent?alt=sse` | `query-param` | `verified` | 2026-08-06 | `https://ai.google.dev/api/generate-content` | `Do not use for image-output rows unless exact model support is separately verified.` |

## Rule

Resolve API version explicitly. The SDK default does not authorize silent version substitution.
