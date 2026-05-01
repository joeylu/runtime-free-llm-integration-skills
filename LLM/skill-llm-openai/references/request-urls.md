# OpenAI Request URLs

Use this file to resolve the final request URL after the connection profile and API surface are selected.

Read `../../_shared/request-url-matrix-schema.md` first.

## Current Matrix

| Request Kind | Model Scope | API Surface | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `catalog-selected` | `responses` | `official` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `same-url` | `verified` | `2026-05-01` | `https://platform.openai.com/docs/api-reference/responses/create` | `preferred chat surface for selected reasoning-capable rows` |
| `vision` | `catalog-selected` | `responses` | `official` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `same-url` | `verified` | `2026-05-01` | `https://platform.openai.com/docs/api-reference/responses/create` | `vision input is sent through Responses content parts` |
| `chat` | `catalog-selected` | `chat-completions-compat` | `official` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `same-url` | `verified` | `2026-05-01` | `https://platform.openai.com/docs/api-reference/chat/create` | `use only when host project needs Chat Completions compatibility` |
| `vision` | `catalog-selected` | `chat-completions-compat` | `official` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `same-url` | `verified` | `2026-05-01` | `https://platform.openai.com/docs/api-reference/chat/create` | `use only when verified options fit the compatibility surface` |
| `imaging` | `gpt-image-2` | `image-api` | `official` | `POST` | `{Profile.Base URL}` | `/images/generations` | `{Profile.Base URL}/images/generations` | `same-url` | `verified` | `2026-05-01` | `https://platform.openai.com/docs/api-reference/images/create` | `generation path for bundled image API row` |

## Rules

- Resolve `Base URL` from `connection-profiles.md` before applying the request path.
- If a gateway profile changes `Base URL`, keep the same request path only when the gateway verifies that surface.
- Do not route OpenAI hosted image-generation tools through `RequestKind = imaging` until the catalog models that hosted-tool path.
