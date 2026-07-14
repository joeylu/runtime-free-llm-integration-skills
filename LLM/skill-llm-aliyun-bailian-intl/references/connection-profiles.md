# Aliyun Bailian International Connection Profiles

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
| `intl-runtime` | `Aliyun Bailian International Runtime` | `aliyun-bailian-intl` | `runtime` | `template` | `openai-compatible` | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `chat` | `responses,chat-completions` | `qwen3.7-max chat may use responses or chat-completions; the `qwen3.7-max` is documented as text-only; use a separately documented vision-capable snapshot or model for image input, so vision is blocked` | `2026-07-14` | `recommended workspace-specific Singapore endpoint; replace {WorkspaceId} before use` |
| `intl-native-runtime` | `Aliyun Bailian International Native Runtime` | `aliyun-bailian-intl` | `runtime` | `template` | `provider-compatible` | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/api/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `imaging,music` | `dashscope-native-sync,dashscope-native-async,dashscope-native` | `no documented International native imaging or music rows yet` | `2026-07-14` | `recommended workspace-specific DashScope native Singapore endpoint; replace {WorkspaceId} before use` |

## Custom Base URL Rule

If the owner changes `Base URL` to a gateway or proxy, also change `Endpoint Kind`.

The official legacy Singapore domains remain callable, but new templates should use the workspace-specific domains above. Treat an unresolved `{WorkspaceId}` as `config_error`; do not silently fall back to a legacy domain.

For gateway or custom endpoints, verify support for:

- OpenAI-compatible Responses
- OpenAI-compatible Chat Completions
- DashScope native job APIs
- streaming
- thinking fields
- structured output
- imaging job submission and polling

If the endpoint does not clearly support one of those fields, block that option for the profile instead of assuming official Aliyun parity.
