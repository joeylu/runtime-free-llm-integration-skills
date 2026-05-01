# Aliyun Bailian International Connection Profiles

Use this file when the host project defines named Aliyun Bailian International / DashScope connection profiles.

Connection profiles choose API key references, base URLs, allowed request kinds, and profile-level restrictions. Request URL templates are stored separately in `request-urls.md`.

## Rules

- Follow `../../_shared/connection-profile-schema.md`.
- Store only secret references such as environment variable names. Do not store real API keys.
- Use provider identifier `aliyun-bailian-intl`.
- Resolve `ConnectionProfileKey` before selecting the final model and API surface.
- Do not silently fall back from one profile, API key, base URL, request URL, or region to another.
- A profile may narrow allowed models, request kinds, API surfaces, or features.
- A profile must not expand a model capability from `unknown` or `unsupported` to usable.
- If a profile points to a gateway or OpenAI-compatible endpoint, verify that the endpoint supports the requested Aliyun API surface before wiring advanced fields.

## Local Profiles

These rows are templates. The host project owns whether the secret reference is active.

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Chat Model | Default Vision Model | Default Imaging Model | Default Music Model | Allowed Request Kinds | Allowed API Surfaces | Model Allowlist | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `intl-runtime` | `Aliyun Bailian International Runtime` | `aliyun-bailian-intl` | `runtime` | `template` | `openai-compatible` | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `qwen3.6-max-preview` | `none` | `none` | `none` | `chat` | `chat-completions` | `catalog-selected` | `only selected International catalog rows are allowed` | `2026-05-01` | `OpenAI-compatible International endpoint template` |
| `intl-native-runtime` | `Aliyun Bailian International Native Runtime` | `aliyun-bailian-intl` | `runtime` | `template` | `provider-compatible` | `https://dashscope-intl.aliyuncs.com/api/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `none` | `none` | `none` | `none` | `imaging,music` | `dashscope-native-sync,dashscope-native-async,dashscope-native` | `catalog-selected` | `no selected International native imaging or music rows yet` | `2026-05-01` | `DashScope native International endpoint template` |

## Custom Base URL Rule

If the owner changes `Base URL` to a gateway or proxy, also change `Endpoint Kind`.

For gateway or custom endpoints, verify support for:

- OpenAI-compatible Chat Completions
- DashScope native job APIs
- streaming
- thinking fields
- structured output
- imaging job submission and polling

If the endpoint does not clearly support one of those fields, block that option for the profile instead of assuming official Aliyun parity.
