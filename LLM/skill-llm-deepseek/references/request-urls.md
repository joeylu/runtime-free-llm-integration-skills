# DeepSeek Request URLs

Use this file to resolve the final request URL after the connection profile and API surface are resolved.

Read `../../_shared/request-url-matrix-schema.md` first.

## Current Matrix

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `documented-models` | `chat-completions` | v1 | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-05-01` | `https://api-docs.deepseek.com/api/create-chat-completion` | `default DeepSeek OpenAI-compatible chat surface` |
| `chat` | `documented-models` | `beta` | v1 | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/beta/chat/completions` | `{Profile.Base URL}/beta/chat/completions` | `body-param` | `verified` | `2026-05-01` | `https://api-docs.deepseek.com/guides/function_calling` | `required for strict function calling when the profile allows beta` |

## Rules

- Use the beta URL only when the resolved profile allows the `beta` surface.
- Do not silently retry from beta to non-beta or from non-beta to beta.
- Treat Anthropic compatibility as a separate surface only after adding an exact verified request URL row.
