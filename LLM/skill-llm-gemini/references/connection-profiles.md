# Gemini Connection Profiles

Use this file to describe named Gemini connection profiles.

Connection profiles choose API key references, base URLs, allowed request kinds, and profile-level restrictions.

They do not define model capabilities. Capabilities still come from `capability-matrix.md`.

## Rules

- Store only secret references such as environment variable names. Do not store real API keys.
- Resolve `ConnectionProfileKey` before selecting the final model and API surface.
- Do not silently fall back between profiles, API keys, base URLs, or API surfaces.
- A profile may narrow allowed models, request kinds, API surfaces, or features.
- A profile must not expand a model capability from `unknown` or `unsupported` to usable.
- A Gemini Developer API profile must not be reused as a Vertex AI profile unless the owner explicitly changes the endpoint and re-verifies transport behavior.

## Local Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Chat Model | Default Vision Model | Default Imaging Model | Default Music Model | Allowed Request Kinds | Allowed API Surfaces | Model Allowlist | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `Gemini Build` | `gemini` | `build` | `active` | `official` | `https://generativelanguage.googleapis.com/v1beta` | `GEMINI_BUILD_API_KEY` | `env` | `gemini-3-flash-preview` | `gemini-3-flash-preview` | `gemini-3.1-flash-image-preview` | `none` | `chat,vision,imaging` | `generate-content,stream-generate-content,image-generation` | `catalog-selected` | `none` | `2026-05-01` | `intended for implementation or production-like execution flows, including Nano Banana image generation` |
| `plan` | `Gemini Plan` | `gemini` | `plan` | `active` | `official` | `https://generativelanguage.googleapis.com/v1beta` | `GEMINI_PLAN_API_KEY` | `env` | `gemini-3-flash-preview` | `gemini-3-flash-preview` | `none` | `none` | `chat,vision` | `generate-content,stream-generate-content` | `catalog-selected` | `imaging disabled by profile unless the owner explicitly enables it` | `2026-05-01` | `intended for planning, review, and analysis flows that may use a separate key or billing boundary` |

## Custom Base URL Rule

If the owner changes `Base URL` to a gateway or proxy, also change `Endpoint Kind`.

For gateway or custom endpoints, verify support for:

- Gemini `generateContent`
- Gemini `streamGenerateContent`
- Gemini `thinkingConfig`
- structured outputs
- function calling
- image generation and image edit parts

If the endpoint does not clearly support one of those fields, block that option for the profile instead of assuming official Gemini parity.
