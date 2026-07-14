# DeepSeek Request URLs

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`
- Key: `Request Kind + Model Scope + API Surface + API Version + Endpoint Kind`

Read `../../_shared/request-url-matrix-schema.md` first. Resolve a connection profile before substituting `{Profile.Base URL}`. No row authorizes silent surface or version fallback.

## Current Matrix

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `text-chat` | `catalog-selected` | `chat-completions` | `provider-default` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-07-14` | `evset-deepseek-request-urls-text-chat-catalog-selected-chat-completions-provider-default-84cc8f81df` | `default DeepSeek OpenAI-compatible chat surface` |
| `text-chat` | `catalog-selected` | `beta` | `beta` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/beta/chat/completions` | `{Profile.Base URL}/beta/chat/completions` | `body-param` | `verified` | `2026-07-14` | `evset-deepseek-request-urls-text-chat-catalog-selected-beta-beta-d926bceeb3` | `strict function schemas only; equivalent to base URL https://api.deepseek.com/beta plus /chat/completions; no automatic retry to the standard surface` |

## Rules

- Use only `verified` rows for sending.
- Treat `unknown` paths as hard stops.
- Do not put secrets or signed user data in a logged resolved URL.
- Claim details and official source locators are in `../../_evidence/evidence.json`.
