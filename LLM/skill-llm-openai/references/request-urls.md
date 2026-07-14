# OpenAI Request URLs

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`
- Key: `Request Kind + Model Scope + API Surface + API Version + Endpoint Kind`

Read `../../_shared/request-url-matrix-schema.md` first. Resolve a connection profile before substituting `{Profile.Base URL}`. No row authorizes silent surface or version fallback.

## Current Matrix

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `text-chat` | `gpt-5.6-sol,gpt-5.6-terra,gpt-5.6-luna` | `responses` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `same-url` | `verified` | `2026-07-14` | `evset-openai-request-urls-text-chat-gpt-5-6-sol-gpt-5-6-terra-gpt-5-6-luna-responses-v1-60b4f982f5` | `preferred for reasoning, state, tools, and structured outputs` |
| `multimodal-chat` | `gpt-5.6-sol,gpt-5.6-terra,gpt-5.6-luna` | `responses` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `same-url` | `verified` | `2026-07-14` | `evset-openai-request-urls-multimodal-chat-gpt-5-6-sol-gpt-5-6-terra-gpt-5-6-luna-responses-v1-c2458a6eab` | `input_image content items; detail defaults to auto` |
| `text-chat` | `gpt-5.6-sol,gpt-5.6-terra,gpt-5.6-luna` | `chat-completions` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `same-url` | `verified` | `2026-07-14` | `evset-openai-request-urls-text-chat-gpt-5-6-sol-gpt-5-6-terra-gpt-5-6-luna-chat-completions-v1-fd85305b0e` | `compatibility surface only; apply its narrower capability row` |
| `multimodal-chat` | `gpt-5.6-sol,gpt-5.6-terra,gpt-5.6-luna` | `chat-completions` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `same-url` | `verified` | `2026-07-14` | `evset-openai-request-urls-multimodal-chat-gpt-5-6-sol-gpt-5-6-terra-gpt-5-6-luna-chat-completions-v1-967b685558` | `compatibility image-input surface; do not inherit Responses state fields` |
| `image-generation` | `gpt-image-2` | `image-api-generations` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/images/generations` | `{Profile.Base URL}/images/generations` | `same-url-sse` | `verified` | `2026-07-14` | `evset-openai-request-urls-image-generation-gpt-image-2-image-api-generations-v1-ef07855ca7` | `direct image generation, including partial-image streaming` |
| `image-generation` | `gpt-image-2` | `image-api-edits` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/images/edits` | `{Profile.Base URL}/images/edits` | `same-url-sse` | `verified` | `2026-07-14` | `evset-openai-request-urls-image-generation-gpt-image-2-image-api-edits-v1-3fa0c46630` | `direct image edit, including partial-image streaming` |

## Rules

- Use only `verified` rows for sending.
- Treat `unknown` paths as hard stops.
- Do not put secrets or signed user data in a logged resolved URL.
- Claim details and official source locators are in `../../_evidence/evidence.json`.
