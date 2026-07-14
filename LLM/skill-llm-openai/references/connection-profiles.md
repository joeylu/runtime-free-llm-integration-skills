# OpenAI Connection Profiles

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`

Read `../../_shared/connection-profile-schema.md` first. The Canonical Profiles table is authoritative.

## Canonical Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Text Model | Default Multimodal Model | Default Image Model | Default Music Model | Allowed Request Kinds | Default Route Map | Allowed Surface Versions | Model Allowlist | Capability Restrictions | Billing Region | Deployment Scope | Serving Region | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `OpenAI Build` | `openai` | `build` | `active` | `official` | `https://api.openai.com/v1` | `OPENAI_BUILD_API_KEY` | `env` | `gpt-5.6-sol` | `gpt-5.6-sol` | `gpt-image-2` | `none` | `text-chat,multimodal-chat,image-generation` | `text-chat=responses@v1;multimodal-chat=responses@v1;image-generation=image-api-generations@v1` | `responses@v1,chat-completions@v1,image-api-generations@v1,image-api-edits@v1` | `catalog-selected` | `none` | `global` | `global` | `global` | `2026-07-14` | `evset-openai-connection-profiles-build-44575cf5b2` | `implementation and production-like execution; Responses preferred for chat/vision` |
| `plan` | `OpenAI Plan` | `openai` | `plan` | `active` | `official` | `https://api.openai.com/v1` | `OPENAI_PLAN_API_KEY` | `env` | `gpt-5.6-sol` | `gpt-5.6-sol` | `none` | `none` | `text-chat,multimodal-chat` | `text-chat=responses@v1;multimodal-chat=responses@v1` | `responses@v1,chat-completions@v1` | `catalog-selected` | `imaging disabled unless profile owner explicitly enables it` | `global` | `global` | `global` | `2026-07-14` | `evset-openai-connection-profiles-plan-64879f7d6b` | `planning, review, and analysis with a separate key or billing boundary` |

## Legacy Compatibility View

This derived table keeps the original 19-column contract. Legacy request-kind names are normalized once at the request boundary; they do not change the canonical route map.

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Chat Model | Default Vision Model | Default Imaging Model | Default Music Model | Allowed Request Kinds | Allowed API Surfaces | Model Allowlist | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `OpenAI Build` | `openai` | `build` | `active` | `official` | `https://api.openai.com/v1` | `OPENAI_BUILD_API_KEY` | `env` | `gpt-5.6-sol` | `gpt-5.6-sol` | `gpt-image-2` | `none` | `chat,vision,imaging` | `responses,chat-completions,image-api-generations,image-api-edits` | `catalog-selected` | `none` | `2026-07-14` | `implementation and production-like execution; Responses preferred for chat/vision` |
| `plan` | `OpenAI Plan` | `openai` | `plan` | `active` | `official` | `https://api.openai.com/v1` | `OPENAI_PLAN_API_KEY` | `env` | `gpt-5.6-sol` | `gpt-5.6-sol` | `none` | `none` | `chat,vision` | `responses,chat-completions` | `catalog-selected` | `imaging disabled unless profile owner explicitly enables it` | `2026-07-14` | `planning, review, and analysis with a separate key or billing boundary` |

## Rules

- Resolve a profile before model, surface, version, capability, URL, or price selection.
- Profile restrictions may narrow capabilities but never expand them.
- Do not fall back to another profile, region, key, surface, or version.
- Claim details are in `../../_evidence/evidence.json`.
