# Gemini Connection Profiles

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`

Read `../../_shared/connection-profile-schema.md` first. The Canonical Profiles table is authoritative.

## Canonical Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Text Model | Default Multimodal Model | Default Image Model | Default Music Model | Allowed Request Kinds | Default Route Map | Allowed Surface Versions | Model Allowlist | Capability Restrictions | Billing Region | Deployment Scope | Serving Region | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `Gemini Build` | `gemini` | `build` | `active` | `official` | `https://generativelanguage.googleapis.com` | `GEMINI_BUILD_API_KEY` | `env` | `gemini-3.5-flash` | `gemini-3.5-flash` | `gemini-3.1-flash-image` | `none` | `text-chat,multimodal-chat,image-generation` | `text-chat=interactions@v1;multimodal-chat=interactions@v1;image-generation=interactions@v1` | `interactions@v1,generate-content@v1beta,stream-generate-content@v1beta` | `catalog-selected` | `custom Interactions safety settings blocked; explicit cache only on generate-content; no cross-surface fallback` | `global` | `global` | `global` | `2026-07-14` | `evset-gemini-connection-profiles-build-44575cf5b2` | `new work defaults to interactions; compatibility surfaces require explicit selection` |
| `plan` | `Gemini Plan` | `gemini` | `plan` | `active` | `official` | `https://generativelanguage.googleapis.com` | `GEMINI_PLAN_API_KEY` | `env` | `gemini-3.5-flash` | `gemini-3.5-flash` | `none` | `none` | `text-chat,multimodal-chat` | `text-chat=interactions@v1;multimodal-chat=interactions@v1` | `interactions@v1,generate-content@v1beta,stream-generate-content@v1beta` | `gemini-3.5-flash,gemini-3.1-pro-preview` | `imaging disabled; custom Interactions safety settings blocked; explicit cache only on generate-content` | `global` | `global` | `global` | `2026-07-14` | `evset-gemini-connection-profiles-plan-64879f7d6b` | `planning and review boundary with a distinct key or billing boundary` |

## Legacy Compatibility View

This derived table keeps the original 19-column contract. Legacy request-kind names are normalized once at the request boundary; they do not change the canonical route map.

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Chat Model | Default Vision Model | Default Imaging Model | Default Music Model | Allowed Request Kinds | Allowed API Surfaces | Model Allowlist | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `Gemini Build` | `gemini` | `build` | `active` | `official` | `https://generativelanguage.googleapis.com` | `GEMINI_BUILD_API_KEY` | `env` | `gemini-3.5-flash` | `gemini-3.5-flash` | `gemini-3.1-flash-image` | `none` | `chat,vision,imaging` | `interactions,generate-content,stream-generate-content` | `catalog-selected` | `custom Interactions safety settings blocked; explicit cache only on generate-content; no cross-surface fallback` | `2026-07-14` | `new work defaults to interactions; compatibility surfaces require explicit selection` |
| `plan` | `Gemini Plan` | `gemini` | `plan` | `active` | `official` | `https://generativelanguage.googleapis.com` | `GEMINI_PLAN_API_KEY` | `env` | `gemini-3.5-flash` | `gemini-3.5-flash` | `none` | `none` | `chat,vision` | `interactions,generate-content,stream-generate-content` | `gemini-3.5-flash,gemini-3.1-pro-preview` | `imaging disabled; custom Interactions safety settings blocked; explicit cache only on generate-content` | `2026-07-14` | `planning and review boundary with a distinct key or billing boundary` |

## Rules

- Resolve a profile before model, surface, version, capability, URL, or price selection.
- Profile restrictions may narrow capabilities but never expand them.
- Do not fall back to another profile, region, key, surface, or version.
- Claim details are in `../../_evidence/evidence.json`.
