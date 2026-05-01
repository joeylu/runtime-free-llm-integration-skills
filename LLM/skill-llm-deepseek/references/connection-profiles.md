# DeepSeek Connection Profiles

Use this file to describe named DeepSeek connection profiles.

Connection profiles choose API key references, base URLs, allowed request kinds, and profile-level restrictions.

They do not define model capabilities. Capabilities still come from `capability-matrix.md`.

## Rules

- Store only secret references such as environment variable names. Do not store real API keys.
- Resolve `ConnectionProfileKey` before selecting the final model and API surface.
- Do not silently fall back between profiles, API keys, base URLs, or compatibility surfaces.
- A profile may narrow allowed models, request kinds, API surfaces, or features.
- A profile must not expand a model capability from `unknown` or `unsupported` to usable.
- Strict tool schemas require an active profile that allows the DeepSeek beta surface.

## Local Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Chat Model | Default Vision Model | Default Imaging Model | Default Music Model | Allowed Request Kinds | Allowed API Surfaces | Model Allowlist | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `DeepSeek Build` | `deepseek` | `build` | `active` | `openai-compatible` | `https://api.deepseek.com` | `DEEPSEEK_BUILD_API_KEY` | `env` | `deepseek-v4-flash` | `none` | `none` | `none` | `chat` | `chat-completions,anthropic-compat,beta` | `catalog-selected` | `strict tool schemas require beta surface` | `2026-05-01` | `intended for implementation or production-like execution flows` |
| `plan` | `DeepSeek Plan` | `deepseek` | `plan` | `active` | `openai-compatible` | `https://api.deepseek.com` | `DEEPSEEK_PLAN_API_KEY` | `env` | `deepseek-v4-flash` | `none` | `none` | `none` | `chat` | `chat-completions,anthropic-compat` | `catalog-selected` | `strict tool schemas disabled by profile` | `2026-05-01` | `intended for planning, review, and analysis flows` |

## Custom Base URL Rule

If the owner changes `Base URL` to a gateway or proxy, also change `Endpoint Kind`.

For gateway or custom endpoints, verify support for:

- DeepSeek OpenAI-compatible Chat Completions
- thinking mode
- streaming
- JSON output
- function calling
- beta strict tool schemas

If the endpoint does not clearly support one of those fields, block that option for the profile instead of assuming official DeepSeek parity.
