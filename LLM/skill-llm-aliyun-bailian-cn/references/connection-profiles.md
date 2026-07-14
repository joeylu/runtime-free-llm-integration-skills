# Aliyun Bailian China Mainland Connection Profiles

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`

Read `../../_shared/connection-profile-schema.md` first. The Canonical Profiles table is authoritative.

## Canonical Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Text Model | Default Multimodal Model | Default Image Model | Default Music Model | Allowed Request Kinds | Default Route Map | Allowed Surface Versions | Model Allowlist | Capability Restrictions | Billing Region | Deployment Scope | Serving Region | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `cn-runtime` | `Aliyun Bailian CN Runtime` | `aliyun-bailian-cn` | `runtime` | `template` | `openai-compatible` | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1` | `ALIYUN_BAILIAN_CN_API_KEY` | `env` | `qwen3.7-plus` | `qwen3.7-plus` | `none` | `none` | `text-chat,multimodal-chat` | `text-chat=responses@compatible-mode-v1;multimodal-chat=responses@compatible-mode-v1` | `responses@compatible-mode-v1,chat-completions@compatible-mode-v1` | `catalog-selected` | `Responses is verified for qwen3.7-plus chat and image-only vision; video/audio vision remains on chat-completions; native imaging uses a separate DashScope API base URL` | `china-mainland` | `china-mainland` | `beijing` | `2026-07-14` | `evset-aliyun-bailian-cn-connection-profiles-cn-runtime-7f0cc9b297` | `recommended workspace-specific China Mainland endpoint; replace {WorkspaceId} before use` |
| `cn-native-runtime` | `Aliyun Bailian CN Native Runtime` | `aliyun-bailian-cn` | `runtime` | `template` | `provider-compatible` | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/api/v1` | `ALIYUN_BAILIAN_CN_API_KEY` | `env` | `none` | `none` | `z-image-turbo` | `none` | `image-generation` | `image-generation=dashscope-native-sync@native-v1` | `dashscope-native-sync@native-v1,dashscope-native-async@native-v1` | `catalog-selected` | `selected native image-generation rows only; music-generation remains blocked until a selected model, exact URL, capability, role, price, and transport contract are all verified` | `china-mainland` | `china-mainland` | `beijing` | `2026-07-14` | `evset-aliyun-bailian-cn-connection-profiles-cn-native-runtime-97a8c36645` | `recommended workspace-specific DashScope native endpoint; replace {WorkspaceId} before use` |

## Legacy Compatibility View

This derived table keeps the original 19-column contract. Legacy request-kind names are normalized once at the request boundary; they do not change the canonical route map.

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Default Chat Model | Default Vision Model | Default Imaging Model | Default Music Model | Allowed Request Kinds | Allowed API Surfaces | Model Allowlist | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `cn-runtime` | `Aliyun Bailian CN Runtime` | `aliyun-bailian-cn` | `runtime` | `template` | `openai-compatible` | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1` | `ALIYUN_BAILIAN_CN_API_KEY` | `env` | `qwen3.7-plus` | `qwen3.7-plus` | `none` | `none` | `chat,vision` | `responses,chat-completions` | `catalog-selected` | `Responses is verified for qwen3.7-plus chat and image-only vision; video/audio vision remains on chat-completions; native imaging uses a separate DashScope API base URL` | `2026-07-14` | `recommended workspace-specific China Mainland endpoint; replace {WorkspaceId} before use` |
| `cn-native-runtime` | `Aliyun Bailian CN Native Runtime` | `aliyun-bailian-cn` | `runtime` | `template` | `provider-compatible` | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/api/v1` | `ALIYUN_BAILIAN_CN_API_KEY` | `env` | `none` | `none` | `z-image-turbo` | `none` | `imaging` | `dashscope-native-sync,dashscope-native-async` | `catalog-selected` | `selected native image-generation rows only; music-generation remains blocked until a selected model, exact URL, capability, role, price, and transport contract are all verified` | `2026-07-14` | `recommended workspace-specific DashScope native endpoint; replace {WorkspaceId} before use` |

## Rules

- Resolve a profile before model, surface, version, capability, URL, or price selection.
- Profile restrictions may narrow capabilities but never expand them.
- Do not fall back to another profile, region, key, surface, or version.
- Claim details are in `../../_evidence/evidence.json`.
