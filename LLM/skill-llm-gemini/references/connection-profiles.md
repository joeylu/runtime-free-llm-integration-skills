# Gemini Connection Profiles

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
| `build` | `Gemini Build` | `gemini` | `build` | `active` | `official` | `https://generativelanguage.googleapis.com` | `GEMINI_BUILD_API_KEY` | `env` | `chat,vision,imaging` | `interactions,generate-content,stream-generate-content` | `custom Interactions safety settings blocked; explicit cache only on generate-content; no cross-surface fallback` | `2026-07-13` | `stable Interactions v1 is the primary Interactions surface; compatibility surfaces require an explicit request` |
| `plan` | `Gemini Plan` | `gemini` | `plan` | `active` | `official` | `https://generativelanguage.googleapis.com` | `GEMINI_PLAN_API_KEY` | `env` | `chat,vision` | `interactions,generate-content,stream-generate-content` | `imaging disabled; custom Interactions safety settings blocked; explicit cache only on generate-content` | `2026-07-13` | `planning and review boundary with a distinct key or billing boundary` |

## Resolution Rules

- The base URL excludes an API version. `request-urls.md` owns `/v1beta` paths.
- Do not append the API key as a query parameter in a loggable URL. Prefer the `x-goog-api-key` header or the official SDK credential path.
- Resolve a profile before choosing a model or surface.
- Do not silently move between `build` and `plan`, official and proxy endpoints, or Interactions and GenerateContent.

## Custom Endpoint Rule

When replacing the official host with a gateway or proxy, set a non-official `Endpoint Kind` and independently verify:

- `/v1beta/interactions`, including SSE step events
- GenerateContent and StreamGenerateContent paths
- `previous_interaction_id`, `store`, and response step shapes
- thinking levels, structured output, caller functions, hosted tools, media parts, and image output
- request and response size limits

Block every feature for which parity is not proven.
