# MiniMax International Connection Profiles

Use this file when the host project defines named MiniMax International connection profiles.

Connection profiles choose API key references, base URLs, allowed request kinds, and profile-level restrictions. Request URL templates are stored separately in `request-urls.md`.

## Rules

- Follow `../../_shared/connection-profile-schema.md`.
- Store only secret references such as environment variable names. Do not store real API keys.
- Use provider identifier `minimax-intl`.
- Resolve `ConnectionProfileKey` before selecting the final model and API surface.
- Do not silently fall back between `build`, `plan`, API keys, base URLs, request URLs, or regions.
- A profile may narrow allowed models, request kinds, API surfaces, or features.
- A profile must not expand a model capability from `unknown` or `unsupported` to usable.
- Do not reuse this profile for MiniMax China Mainland.

## Build And Plan Profiles

`build` and `plan` are separate purpose and credential boundaries.

They currently share the same official MiniMax International base URL, but this is still profile data and must be resolved from the selected row. Do not hardcode the base URL after seeing that both rows match.

Use:

- `build` for implementation or production-like execution flows, including verified HTTP chat, imaging, and music rows
- `plan` for planning, review, and analysis flows that may use a separate key or billing boundary

The `plan` profile is intentionally chat-only in this skill. Do not expose MiniMax plan-profile image, music, video, CLI, or MCP multimodal flows unless the owner explicitly extends this skill.

## Local Profiles

These rows are templates. The host project owns whether the secret reference is active.

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Chat Model | Default Vision Model | Default Imaging Model | Default Music Model | Allowed Request Kinds | Allowed API Surfaces | Model Allowlist | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `MiniMax International Build` | `minimax-intl` | `build` | `template` | `official` | `https://api.minimax.io/v1` | `MINIMAX_INTL_BUILD_API_KEY` | `env` | `MiniMax-M2.7` | `none` | `image-01` | `music-2.6` | `chat,imaging,music` | `chat-completions,image-generation,music-generation` | `catalog-selected` | `selected chat, imaging, and music rows only; video HTTP endpoint is reference-only until shared RequestKind adds video` | `2026-05-03` | `intended for implementation or production-like execution flows` |
| `plan` | `MiniMax International Plan` | `minimax-intl` | `plan` | `template` | `official` | `https://api.minimax.io/v1` | `MINIMAX_INTL_PLAN_API_KEY` | `env` | `MiniMax-M2.7` | `none` | `none` | `none` | `chat` | `chat-completions` | `catalog-selected` | `chat-only; block imaging, music, video, CLI, and MCP multimodal flows in this skill` | `2026-05-03` | `intended for planning, review, and analysis flows` |

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
