# OpenAI Connection Profiles

Use this file to describe named OpenAI connection profiles such as `build` and `plan`.

Connection profiles choose API key references, base URLs, allowed request kinds, and profile-level restrictions.

They do not define model capabilities. Capabilities still come from `capability-matrix.md`.

## Rules

- Store only secret references such as environment variable names. Do not store real API keys.
- Resolve `ConnectionProfileKey` before selecting the final model and API surface.
- Do not silently fall back from `plan` to `build`, or from `build` to `plan`.
- Do not silently fall back from one `Base URL` to another.
- A profile may narrow allowed models, request kinds, API surfaces, or features.
- A profile must not expand a model capability from `unknown` or `unsupported` to usable.
- If a profile points to a gateway or custom OpenAI-compatible endpoint, verify that the endpoint supports the requested API surface before wiring advanced fields.

## Local Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Chat Model | Default Vision Model | Default Imaging Model | Default Music Model | Allowed Request Kinds | Allowed API Surfaces | Model Allowlist | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `OpenAI Build` | `openai` | `build` | `active` | `official` | `https://api.openai.com/v1` | `OPENAI_BUILD_API_KEY` | `env` | `gpt-5.5` | `gpt-5.5` | `gpt-image-2` | `none` | `chat,vision,imaging` | `responses,image-api,chat-completions-compat` | `catalog-selected` | `none` | `2026-04-30` | `intended for implementation or production-like execution flows` |
| `plan` | `OpenAI Plan` | `openai` | `plan` | `active` | `official` | `https://api.openai.com/v1` | `OPENAI_PLAN_API_KEY` | `env` | `gpt-5.5` | `gpt-5.5` | `none` | `none` | `chat,vision` | `responses,chat-completions-compat` | `catalog-selected` | `imaging disabled by profile unless the owner explicitly enables it` | `2026-04-30` | `intended for planning, review, and analysis flows that may use a separate key or billing boundary` |

## Custom Base URL Rule

If the owner changes `Base URL` to a gateway or OpenAI-compatible proxy, also change `Endpoint Kind`.

Example:
Use `Endpoint Kind = gateway` when `Base URL` points to an internal gateway instead of `https://api.openai.com/v1`.

For gateway or custom endpoints, verify support for:

- Responses API
- Chat Completions compatibility
- structured outputs
- streaming
- reasoning fields
- tool calling
- image generation or image edits

If the endpoint does not clearly support one of those fields, block that option for the profile instead of assuming official OpenAI parity.
