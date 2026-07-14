# MiniMax International Connection Profiles

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`

Read `../../_shared/connection-profile-schema.md` first. The Canonical Profiles table is authoritative.

## Canonical Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Text Model | Default Multimodal Model | Default Image Model | Default Music Model | Allowed Request Kinds | Default Route Map | Allowed Surface Versions | Model Allowlist | Capability Restrictions | Billing Region | Deployment Scope | Serving Region | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `MiniMax International Build` | `minimax-intl` | `build` | `template` | `official` | `https://api.minimax.io/v1` | `MINIMAX_INTL_BUILD_API_KEY` | `env` | `MiniMax-M2.7` | `none` | `image-01` | `music-2.6` | `text-chat,image-generation,music-generation` | `text-chat=chat-completions@v1;image-generation=image-generation@v1;music-generation=music-generation@v1` | `chat-completions@v1,image-generation@v1,music-generation@v1` | `catalog-selected` | `selected chat, imaging, and music rows only; video HTTP endpoint remains reference-only until a complete selected catalog/profile/URL/capability/pricing/transport contract is added` | `global` | `international` | `global` | `2026-07-14` | `evset-minimax-intl-connection-profiles-build-44575cf5b2` | `intended for implementation or production-like execution flows` |
| `plan` | `MiniMax International Plan` | `minimax-intl` | `plan` | `template` | `official` | `https://api.minimax.io/v1` | `MINIMAX_INTL_PLAN_API_KEY` | `env` | `MiniMax-M2.7` | `none` | `none` | `none` | `text-chat` | `text-chat=chat-completions@v1` | `chat-completions@v1` | `catalog-selected` | `chat-only; block imaging, music, video, CLI, and MCP multimodal flows in this skill` | `global` | `international` | `global` | `2026-07-14` | `evset-minimax-intl-connection-profiles-plan-64879f7d6b` | `intended for planning, review, and analysis flows` |

## Legacy Compatibility View

This derived table keeps the original 19-column contract. Legacy request-kind names are normalized once at the request boundary; they do not change the canonical route map.

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Chat Model | Default Vision Model | Default Imaging Model | Default Music Model | Allowed Request Kinds | Allowed API Surfaces | Model Allowlist | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build` | `MiniMax International Build` | `minimax-intl` | `build` | `template` | `official` | `https://api.minimax.io/v1` | `MINIMAX_INTL_BUILD_API_KEY` | `env` | `MiniMax-M2.7` | `none` | `image-01` | `music-2.6` | `chat,imaging,music` | `chat-completions,image-generation,music-generation` | `catalog-selected` | `selected chat, imaging, and music rows only; video HTTP endpoint remains reference-only until a complete selected catalog/profile/URL/capability/pricing/transport contract is added` | `2026-07-14` | `intended for implementation or production-like execution flows` |
| `plan` | `MiniMax International Plan` | `minimax-intl` | `plan` | `template` | `official` | `https://api.minimax.io/v1` | `MINIMAX_INTL_PLAN_API_KEY` | `env` | `MiniMax-M2.7` | `none` | `none` | `none` | `chat` | `chat-completions` | `catalog-selected` | `chat-only; block imaging, music, video, CLI, and MCP multimodal flows in this skill` | `2026-07-14` | `intended for planning, review, and analysis flows` |

## Rules

- Resolve a profile before model, surface, version, capability, URL, or price selection.
- Profile restrictions may narrow capabilities but never expand them.
- Do not fall back to another profile, region, key, surface, or version.
- Claim details are in `../../_evidence/evidence.json`.
