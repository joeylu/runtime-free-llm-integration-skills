# MiniMax International Connection Profiles

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
| `build` | `MiniMax International Build` | `minimax-intl` | `build` | `template` | `official` | `https://api.minimax.io/v1` | `MINIMAX_INTL_BUILD_API_KEY` | `env` | `chat,vision,imaging,music` | `chat-completions,image-generation,music-generation` | `chat, vision, imaging, and music endpoints; video HTTP endpoint is reference-only until shared RequestKind adds video` | `2026-07-14` | `intended for implementation or production-like execution flows` |
| `plan` | `MiniMax International Plan` | `minimax-intl` | `plan` | `template` | `official` | `https://api.minimax.io/v1` | `MINIMAX_INTL_PLAN_API_KEY` | `env` | `chat` | `chat-completions` | `chat only; image, music, and video access is not verified for this profile` | `2026-07-14` | `intended for planning, review, and analysis flows` |

## Custom Base URL Rule

If the owner changes one profile's `Base URL` to a gateway or proxy, also change that row's `Endpoint Kind`.

For gateway or custom endpoints, verify support for:

- MiniMax OpenAI-compatible Chat Completions
- MiniMax official Image Generation
- MiniMax official Music Generation
- MiniMax official Video Generation links when used as reference-only documentation
- streaming
- thinking output shape
- temperature

If the endpoint does not clearly support one of those fields, block that option for the profile instead of assuming official MiniMax parity. Do not copy a gateway base URL from `build` to `plan`, or from `plan` to `build`, unless the owner explicitly configures both rows.
