# OpenAI Request URLs

Resolve the exact request URL only after the profile, request kind, model, and API surface are fixed.

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `gpt-5.6-sol,gpt-5.6-terra,gpt-5.6-luna` | `responses` | v1 | `official` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `same-url` | `verified` | `2026-07-13` | `https://developers.openai.com/api/reference/resources/responses/methods/create` | `preferred for reasoning, state, tools, and structured outputs` |
| `vision` | `gpt-5.6-sol,gpt-5.6-terra,gpt-5.6-luna` | `responses` | v1 | `official` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `same-url` | `verified` | `2026-07-13` | `https://developers.openai.com/api/reference/resources/responses/methods/create` | `input_image content items; detail defaults to auto` |
| `chat` | `gpt-5.6-sol,gpt-5.6-terra,gpt-5.6-luna` | `chat-completions` | v1 | `official` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `same-url` | `verified` | `2026-07-13` | `https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create` | `compatibility surface only; apply its narrower capability row` |
| `vision` | `gpt-5.6-sol,gpt-5.6-terra,gpt-5.6-luna` | `chat-completions` | v1 | `official` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `same-url` | `verified` | `2026-07-13` | `https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create` | `compatibility image-input surface; do not inherit Responses state fields` |
| `imaging` | `gpt-image-2` | `image-api-generations` | v1 | `official` | `POST` | `{Profile.Base URL}` | `/images/generations` | `{Profile.Base URL}/images/generations` | `same-url-sse` | `verified` | `2026-07-13` | `https://developers.openai.com/api/reference/resources/images/methods/generate` | `direct image generation, including partial-image streaming` |
| `imaging` | `gpt-image-2` | `image-api-edits` | v1 | `official` | `POST` | `{Profile.Base URL}` | `/images/edits` | `{Profile.Base URL}/images/edits` | `same-url-sse` | `verified` | `2026-07-13` | `https://developers.openai.com/api/reference/resources/images/methods/edit` | `direct image edit, including partial-image streaming` |

## Rules

- Join the base URL and request path exactly once; avoid `//` and duplicate `/v1` segments.
- `stream: true` does not change these URLs.
- Do not send `gpt-image-2` to `/responses` as the main model. A Responses image-generation hosted-tool request uses a GPT-5.6 mainline model and is governed by `hosted-tools.md`, not the direct `imaging` rows.
- Do not map direct Image API requests to `RequestKind = chat` or `vision`.
