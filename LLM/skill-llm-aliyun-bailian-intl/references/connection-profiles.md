# Aliyun Bailian International / Singapore Connection Profiles

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`

Read `../../_shared/connection-profile-schema.md` first. The Canonical Profiles table is authoritative.

## Canonical Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Text Model | Default Multimodal Model | Default Image Model | Default Music Model | Allowed Request Kinds | Default Route Map | Allowed Surface Versions | Model Allowlist | Capability Restrictions | Billing Region | Deployment Scope | Serving Region | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `intl-runtime` | `Aliyun Bailian International Runtime` | `aliyun-bailian-intl` | `runtime` | `template` | `openai-compatible` | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `qwen3.7-max` | `none` | `none` | `none` | `text-chat` | `text-chat=responses@compatible-mode-v1` | `responses@compatible-mode-v1,chat-completions@compatible-mode-v1` | `catalog-selected` | `qwen3.7-max chat may use responses or chat-completions; the selected alias resolves to the text-only 2026-05-20 snapshot, so vision is blocked` | `singapore` | `international` | `singapore` | `2026-07-14` | `evset-aliyun-bailian-intl-connection-profiles-intl-runtime-94eeb93ba0` | `recommended workspace-specific Singapore endpoint; replace {WorkspaceId} before use` |
| `intl-native-runtime` | `Aliyun Bailian International Native Runtime` | `aliyun-bailian-intl` | `runtime` | `disabled` | `provider-compatible` | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/api/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `none` | `none` | `none` | `none` | `none` | `none` | `none` | `none` | `reference-only endpoint template; no selected International native image or music contract exists` | `singapore` | `international` | `singapore` | `2026-07-14` | `evset-aliyun-bailian-intl-connection-profiles-intl-native-runtime-411e5ecce1` | `recommended workspace-specific DashScope native Singapore endpoint; replace {WorkspaceId} before use` |

## Legacy Compatibility View

This derived table keeps the original 19-column contract. Legacy request-kind names are normalized once at the request boundary; they do not change the canonical route map.

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Chat Model | Default Vision Model | Default Imaging Model | Default Music Model | Allowed Request Kinds | Allowed API Surfaces | Model Allowlist | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `intl-runtime` | `Aliyun Bailian International Runtime` | `aliyun-bailian-intl` | `runtime` | `template` | `openai-compatible` | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `qwen3.7-max` | `none` | `none` | `none` | `chat` | `responses,chat-completions` | `catalog-selected` | `qwen3.7-max chat may use responses or chat-completions; the selected alias resolves to the text-only 2026-05-20 snapshot, so vision is blocked` | `2026-07-14` | `recommended workspace-specific Singapore endpoint; replace {WorkspaceId} before use` |
| `intl-native-runtime` | `Aliyun Bailian International Native Runtime` | `aliyun-bailian-intl` | `runtime` | `disabled` | `provider-compatible` | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/api/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `none` | `none` | `none` | `none` | `none` | `none` | `none` | `reference-only endpoint template; no selected International native image or music contract exists` | `2026-07-14` | `recommended workspace-specific DashScope native Singapore endpoint; replace {WorkspaceId} before use` |

## Rules

- Resolve a profile before model, surface, version, capability, URL, or price selection.
- Profile restrictions may narrow capabilities but never expand them.
- Do not fall back to another profile, region, key, surface, or version.
- Claim details are in `../../_evidence/evidence.json`.
