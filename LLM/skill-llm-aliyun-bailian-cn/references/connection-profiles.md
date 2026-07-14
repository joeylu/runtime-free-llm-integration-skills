# Aliyun Bailian China Mainland Connection Profiles

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
| `cn-runtime` | `Aliyun Bailian CN Runtime` | `aliyun-bailian-cn` | `runtime` | `template` | `openai-compatible` | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1` | `ALIYUN_BAILIAN_CN_API_KEY` | `env` | `chat,vision` | `responses,chat-completions` | `Responses is verified for qwen3.7-plus chat and image-only vision; video/audio vision remains on chat-completions; native imaging uses a separate DashScope API base URL` | `2026-07-13` | `recommended workspace-specific China Mainland endpoint; replace {WorkspaceId} before use` |
| `cn-native-runtime` | `Aliyun Bailian CN Native Runtime` | `aliyun-bailian-cn` | `runtime` | `template` | `provider-compatible` | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/api/v1` | `ALIYUN_BAILIAN_CN_API_KEY` | `env` | `imaging,music` | `dashscope-native-sync,dashscope-native-async,dashscope-native` | `exact model-family request URL must be resolved from request-urls.md` | `2026-07-13` | `recommended workspace-specific DashScope native endpoint; replace {WorkspaceId} before use` |

## Custom Base URL Rule

If the owner changes `Base URL` to a gateway or proxy, also change `Endpoint Kind`.

The official legacy domains remain callable, but new templates should use the workspace-specific domains above. Treat an unresolved `{WorkspaceId}` as `config_error`; do not silently fall back to a legacy domain.

For gateway or custom endpoints, verify support for:

- OpenAI-compatible Responses
- OpenAI-compatible Chat Completions
- DashScope native job APIs
- streaming
- thinking fields
- structured output
- imaging job submission and polling

If the endpoint does not clearly support one of those fields, block that option for the profile instead of assuming official Aliyun parity.
