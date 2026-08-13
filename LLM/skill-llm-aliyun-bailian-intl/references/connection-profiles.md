# Aliyun Bailian International Connection Profiles

Connection profiles supply Base URLs and references to required connection inputs. The request supplies the model, and `request-urls.md` supplies the final path.

## Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Non-Secret Config Refs | Non-Secret Config Sources | Placeholder Bindings | Request Kinds | API Surfaces | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `intl-openai-runtime` | `Aliyun Bailian Singapore workspace OpenAI-compatible` | `aliyun-bailian-intl` | `runtime` | `template` | `openai-compatible` | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `ALIYUN_BAILIAN_INTL_WORKSPACE_ID` | `env,user-setting,config-file,external` | `{WorkspaceId} <- ALIYUN_BAILIAN_INTL_WORKSPACE_ID` | `chat,vision` | `responses,chat-completions` | `Only qwen3.8-max is maintained; Responses media is image-only.` | 2026-08-13 | `Recommended production profile. Workspace ID and API Key must belong to the same Singapore workspace.` |
| `intl-native-runtime` | `Aliyun Bailian Singapore workspace DashScope native` | `aliyun-bailian-intl` | `runtime` | `template` | `provider-compatible` | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/api/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `ALIYUN_BAILIAN_INTL_WORKSPACE_ID` | `env,user-setting,config-file,external` | `{WorkspaceId} <- ALIYUN_BAILIAN_INTL_WORKSPACE_ID` | `chat,vision` | `multimodal-generation` | `Only qwen3.8-max is maintained.` | 2026-08-13 | `Recommended production profile; never use a Beijing endpoint.` |
| `intl-shared-openai-runtime` | `Aliyun Bailian Singapore shared OpenAI-compatible` | `aliyun-bailian-intl` | `runtime` | `template` | `openai-compatible` | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `n/a` | `n/a` | `n/a` | `chat,vision` | `responses,chat-completions` | `Existing centralized domain; explicitly selected alternative with lower isolation than a workspace-specific domain.` | 2026-08-13 | `No workspace ID is required. Never select this as an implicit fallback.` |
| `intl-shared-native-runtime` | `Aliyun Bailian Singapore shared DashScope native` | `aliyun-bailian-intl` | `runtime` | `template` | `provider-compatible` | `https://dashscope-intl.aliyuncs.com/api/v1` | `ALIYUN_BAILIAN_INTL_API_KEY` | `env` | `n/a` | `n/a` | `n/a` | `chat,vision` | `multimodal-generation` | `Only qwen3.8-max is maintained.` | 2026-08-13 | `No workspace ID is required. Never select this as an implicit fallback.` |

## Rules

- Read `workspace-configuration.md` before resolving a profile.
- Resolve the profile and all declared inputs before constructing the final request URL.
- An unresolved `{WorkspaceId}` is `config_error`; do not guess, omit, or replace it with an account ID.
- Workspace-specific and shared profiles are separate explicit choices. Never switch profiles or regions automatically.
- Store references only; never store actual API keys or user workspace IDs in this skill.
