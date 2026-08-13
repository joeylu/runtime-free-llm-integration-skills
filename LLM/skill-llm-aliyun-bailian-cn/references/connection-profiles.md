# Aliyun Bailian China Mainland Connection Profiles

Connection profiles supply Base URLs and references to required connection inputs. The request supplies the model, and `request-urls.md` supplies the final path.

## Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Non-Secret Config Refs | Non-Secret Config Sources | Placeholder Bindings | Request Kinds | API Surfaces | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `cn-openai-runtime` | `Aliyun Bailian CN workspace OpenAI-compatible` | `aliyun-bailian-cn` | `runtime` | `template` | `openai-compatible` | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1` | `ALIYUN_BAILIAN_CN_API_KEY` | `env` | `ALIYUN_BAILIAN_CN_WORKSPACE_ID` | `env,user-setting,config-file,external` | `{WorkspaceId} <- ALIYUN_BAILIAN_CN_WORKSPACE_ID` | `chat,vision` | `responses,chat-completions` | `Only exact retained Qwen rows are maintained; Responses has narrower media and field support than Chat Completions.` | 2026-08-13 | `Recommended production profile. Workspace ID and API Key must belong to the same China Mainland workspace.` |
| `cn-native-runtime` | `Aliyun Bailian CN workspace DashScope native` | `aliyun-bailian-cn` | `runtime` | `template` | `provider-compatible` | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/api/v1` | `ALIYUN_BAILIAN_CN_API_KEY` | `env` | `ALIYUN_BAILIAN_CN_WORKSPACE_ID` | `env,user-setting,config-file,external` | `{WorkspaceId} <- ALIYUN_BAILIAN_CN_WORKSPACE_ID` | `chat,vision,imaging` | `multimodal-generation,image-generation` | `Exact family-specific payload, create path, and polling path only.` | 2026-08-13 | `Recommended production profile for Qwen-Image and Wan direct-model APIs.` |
| `cn-shared-openai-runtime` | `Aliyun Bailian CN shared OpenAI-compatible` | `aliyun-bailian-cn` | `runtime` | `template` | `openai-compatible` | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `ALIYUN_BAILIAN_CN_API_KEY` | `env` | `n/a` | `n/a` | `n/a` | `chat,vision` | `responses,chat-completions` | `Existing centralized domain; explicitly selected alternative with lower isolation than a workspace-specific domain.` | 2026-08-13 | `No workspace ID is required. Never select this as an implicit fallback.` |
| `cn-shared-native-runtime` | `Aliyun Bailian CN shared DashScope native` | `aliyun-bailian-cn` | `runtime` | `template` | `provider-compatible` | `https://dashscope.aliyuncs.com/api/v1` | `ALIYUN_BAILIAN_CN_API_KEY` | `env` | `n/a` | `n/a` | `n/a` | `chat,vision,imaging` | `multimodal-generation,image-generation` | `Existing centralized native domain; exact family-specific request paths still apply.` | 2026-08-13 | `No workspace ID is required. Never select this as an implicit fallback.` |

## Rules

- Read `workspace-configuration.md` before resolving a profile.
- Resolve the profile and all declared inputs before constructing the final request URL.
- An unresolved `{WorkspaceId}` is `config_error`; do not guess, omit, or replace it with an account ID.
- Workspace-specific and shared profiles are separate explicit choices. Never switch between them automatically.
- Store references only; never store actual API keys or user workspace IDs in this skill.
- A gateway or proxy is a new endpoint kind and must be re-verified field by field.
