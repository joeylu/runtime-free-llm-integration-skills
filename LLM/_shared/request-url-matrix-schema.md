# Shared Request URL Matrix Schema v2

Resolve the exact request URL before capability lookup and before sending.

## Required Key

`Request Kind + Model Scope + API Surface + API Version + Endpoint Kind`

## Required Columns

| Column | Meaning |
| --- | --- |
| `Request Kind` | Canonical request kind |
| `Model Scope` | Exact model ID, comma-separated IDs sharing the same endpoint, or `catalog-selected` |
| `API Surface` | One exact surface |
| `API Version` | Exact API version encoded by path/header/query, or `none` / `provider-default` |
| `Endpoint Kind` | `official`, `openai-compatible`, `provider-compatible`, `gateway`, or `custom` |
| `HTTP Method` | Exact method |
| `Base URL` | Exact base URL or `{Profile.Base URL}` |
| `Request Path Template` | Exact path without secret data |
| `Request URL Template` | Base plus path |
| `Stream Variant` | `same-url`, `body-param`, `query-param`, `same-url-sse`, `separate-url`, `n/a`, or `unknown` |
| `Request URL Status` | `verified`, `inherited`, `unknown`, or `removed` |
| `Last Verified At` | Exact review date or `unverified` |
| `Evidence Refs` | Endpoint evidence-set IDs |
| `Notes` | Surface-specific constraints |

## Rules

- Surface names do not imply versions. Store the version explicitly.
- Stable versions are preferred for new integrations when feature parity is verified.
- Beta versions remain explicit compatibility rows; do not silently rewrite stable to beta or beta to stable.
- `Base URL` alone never identifies a complete request.
- API keys, signed URLs, and user secrets must not appear in URL templates.
- If the final URL or required version is unknown, stop.
