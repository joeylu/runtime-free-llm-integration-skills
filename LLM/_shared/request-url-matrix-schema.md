# Shared Request URL Matrix Schema

Use this file to keep provider request URL data structured and separate from model selection.

`connection-profiles.md` resolves the base URL and API key. `request-urls.md` resolves the exact HTTP method and request URL template for one request kind, model scope, and API surface.

## Required Columns

| Column | Meaning |
| --- | --- |
| `Request Kind` | One of `chat`, `vision`, `imaging`, or `music` |
| `Model Scope` | Exact model IDs, model-family pattern, `catalog-selected`, or `all` |
| `API Surface` | Provider surface such as `responses`, `chat-completions`, `generate-content`, `dashscope-native-sync`, or `dashscope-native-async` |
| `Endpoint Kind` | `official`, `openai-compatible`, `provider-compatible`, `gateway`, or `custom` |
| `HTTP Method` | Request method such as `POST` |
| `Base URL` | Exact base URL, SDK base URL, or `{Profile.Base URL}` when profile-owned |
| `Request Path Template` | Path and query template relative to `Base URL`, or `n/a` when `Base URL` is already the full request URL |
| `Request URL Template` | Full URL template after combining base URL and path |
| `Stream Variant` | `same-url`, `query-param`, `body-param`, `separate-url`, or `n/a` |
| `Request URL Status` | `verified`, `inherited`, `unknown`, or `project-owned` |
| `Last Verified At` | Absolute verification date or `unverified` |
| `Source` | Exact official source URL or explicit inherited/project-owned note |
| `Notes` | Short explanation |

## Rules

- Resolve `ConnectionProfileKey` first, then resolve the row whose `Request Kind`, `Model Scope`, `API Surface`, and `Endpoint Kind` match the selected transport.
- Store URL templates, not secrets. Do not put API keys, tokens, signed URLs, or tenant secrets in this file.
- Prefer templates that compose from `Base URL` plus `Request Path Template`.
- If an SDK accepts a base URL but the raw HTTP request uses a longer endpoint, store both the SDK base URL and the final request URL template.
- If a provider has separate regional domains, model each regional provider or profile explicitly. Do not hide region switching behind one generic URL template.
- If the request URL is project-owned because the profile points to a gateway, keep `Request URL Status = project-owned` and require the project to supply the URL template.
- If the selected request URL row is missing, `unknown`, or incompatible with the profile endpoint kind, stop with `request_url_error`.
- Do not silently fall back from one request URL to another.
- When logging request URLs, redact secret query parameters and signed URL material before storage.

## Example

| Request Kind | Model Scope | API Surface | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `catalog-selected` | `chat-completions` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-05-01` | `official provider docs` | `stream is selected by request body when verified` |
