# Shared Request URL Matrix Schema

`connection-profiles.md` resolves the base URL and credential reference. `request-urls.md` resolves the HTTP method and full URL template for one request kind, model scope, API surface, and API version.

Read `route-key-schema.md` first.

## Required Columns

| Column | Meaning |
| --- | --- |
| `Request Kind` | provider skill request kind |
| `Model Scope` | exact model IDs, model-family pattern, `documented-models`, or `all` |
| `API Surface` | exact provider API surface |
| `API Version` | exact version in the path or protocol, or `n/a` |
| `Endpoint Kind` | `official`, `openai-compatible`, `provider-compatible`, `gateway`, or `custom` |
| `HTTP Method` | request method such as `POST` |
| `Base URL` | exact base URL or `{Profile.Base URL}` |
| `Request Path Template` | path and query template relative to `Base URL`, or `n/a` |
| `Request URL Template` | full URL template |
| `Stream Variant` | `same-url`, `query-param`, `body-param`, `separate-url`, or `n/a` |
| `Request URL Status` | `verified`, `inherited`, `unknown`, or `project-owned` |
| `Last Verified At` | absolute verification date or `unverified` |
| `Source` | exact official URL or explicit project-owned note |
| `Notes` | short routing constraint |

## Rules

- Match request kind, model scope, API surface, API version, and endpoint kind exactly.
- Store URL templates, never secrets or signed user URLs.
- Keep regional domains explicit.
- Stop when the matching row is missing, `unknown`, or incompatible with the resolved profile.
- Never silently fall back to another URL, surface, version, or region.
- Redact secret query parameters before logging resolved URLs.
