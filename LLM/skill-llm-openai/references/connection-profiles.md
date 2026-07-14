# OpenAI Connection Profiles

Connection profiles supply base URLs and credential references. The request supplies the model, and `request-urls.md` supplies the final path.

## Rules

- Store secret references only.
- Resolve the profile before the final request URL.
- Match model capabilities through `model-catalog.md` and `capability-matrix.md`.
- Never silently change profile, base URL, credential, region, API surface, or request path.
- Re-verify advanced fields for gateways and custom endpoints.

## Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Request Kinds | API Surfaces | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `OpenAI Build` | `openai` | `build` | `active` | `official` | `https://api.openai.com/v1` | `OPENAI_BUILD_API_KEY` | `env` | `chat,vision,imaging` | `responses,chat-completions,image-api-generations,image-api-edits` | `none` | `2026-07-13` | `implementation and production-like execution; Responses preferred for chat/vision` |
| `plan` | `OpenAI Plan` | `openai` | `plan` | `active` | `official` | `https://api.openai.com/v1` | `OPENAI_PLAN_API_KEY` | `env` | `chat,vision` | `responses,chat-completions` | `imaging disabled unless profile owner explicitly enables it` | `2026-07-13` | `planning, review, and analysis with a separate key or billing boundary` |

## Custom Endpoint Rule

When `Base URL` changes from the official endpoint:

1. set `Endpoint Kind = gateway` or another explicit value;
2. verify each request path independently;
3. narrow `API Surfaces` to observed, documented support;
4. keep every unverified advanced capability fail-closed.
