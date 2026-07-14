# DeepSeek Connection Profiles

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
| `build` | `DeepSeek Build` | `deepseek` | `build` | `active` | `openai-compatible` | `https://api.deepseek.com` | `DEEPSEEK_BUILD_API_KEY` | `env` | `chat` | `chat-completions,beta` | `strict tool schemas require beta surface` | `2026-05-01` | `intended for implementation or production-like execution flows` |
| `plan` | `DeepSeek Plan` | `deepseek` | `plan` | `active` | `openai-compatible` | `https://api.deepseek.com` | `DEEPSEEK_PLAN_API_KEY` | `env` | `chat` | `chat-completions` | `strict tool schemas disabled by profile` | `2026-05-01` | `intended for planning, review, and analysis flows` |

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
