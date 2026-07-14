# DeepSeek Connection Profiles

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`

Read `../../_shared/connection-profile-schema.md` first. The Canonical Profiles table is authoritative.

## Canonical Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Text Model | Default Multimodal Model | Default Image Model | Default Music Model | Allowed Request Kinds | Default Route Map | Allowed Surface Versions | Model Allowlist | Capability Restrictions | Billing Region | Deployment Scope | Serving Region | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `DeepSeek Build` | `deepseek` | `build` | `active` | `openai-compatible` | `https://api.deepseek.com` | `DEEPSEEK_BUILD_API_KEY` | `env` | `deepseek-v4-flash` | `none` | `none` | `none` | `text-chat` | `text-chat=chat-completions@provider-default` | `chat-completions@provider-default,beta@beta` | `catalog-selected` | `strict tool schemas require beta surface` | `global` | `global` | `global` | `2026-07-14` | `evset-deepseek-connection-profiles-build-44575cf5b2` | `intended for implementation or production-like execution flows` |
| `plan` | `DeepSeek Plan` | `deepseek` | `plan` | `active` | `openai-compatible` | `https://api.deepseek.com` | `DEEPSEEK_PLAN_API_KEY` | `env` | `deepseek-v4-flash` | `none` | `none` | `none` | `text-chat` | `text-chat=chat-completions@provider-default` | `chat-completions@provider-default` | `catalog-selected` | `strict tool schemas disabled by profile` | `global` | `global` | `global` | `2026-07-14` | `evset-deepseek-connection-profiles-plan-64879f7d6b` | `intended for planning, review, and analysis flows` |

## Legacy Compatibility View

This derived table keeps the original 19-column contract. Legacy request-kind names are normalized once at the request boundary; they do not change the canonical route map.

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Chat Model | Default Vision Model | Default Imaging Model | Default Music Model | Allowed Request Kinds | Allowed API Surfaces | Model Allowlist | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `DeepSeek Build` | `deepseek` | `build` | `active` | `openai-compatible` | `https://api.deepseek.com` | `DEEPSEEK_BUILD_API_KEY` | `env` | `deepseek-v4-flash` | `none` | `none` | `none` | `chat` | `chat-completions,beta` | `catalog-selected` | `strict tool schemas require beta surface` | `2026-07-14` | `intended for implementation or production-like execution flows` |
| `plan` | `DeepSeek Plan` | `deepseek` | `plan` | `active` | `openai-compatible` | `https://api.deepseek.com` | `DEEPSEEK_PLAN_API_KEY` | `env` | `deepseek-v4-flash` | `none` | `none` | `none` | `chat` | `chat-completions` | `catalog-selected` | `strict tool schemas disabled by profile` | `2026-07-14` | `intended for planning, review, and analysis flows` |

## Rules

- Resolve a profile before model, surface, version, capability, URL, or price selection.
- Profile restrictions may narrow capabilities but never expand them.
- Do not fall back to another profile, region, key, surface, or version.
- Claim details are in `../../_evidence/evidence.json`.
