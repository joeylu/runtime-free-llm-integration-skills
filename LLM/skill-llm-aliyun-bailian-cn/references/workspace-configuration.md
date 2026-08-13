# Aliyun Bailian China Mainland Workspace Configuration

This file declares the connection inputs required before an Agent can construct a China Mainland request URL. It never stores the user's actual values.

## Configuration Inputs

| Ref | Type | Sensitivity | Allowed Sources | Required When | Value Contract | Binds To |
| --- | --- | --- | --- | --- | --- | --- |
| `ALIYUN_BAILIAN_CN_API_KEY` | `string` | `secret` | `env` | every China Mainland profile | API Key issued for the China Mainland region and the selected billing plan | `Authorization: Bearer ...` |
| `ALIYUN_BAILIAN_CN_WORKSPACE_ID` | `string` | `non-secret` | `env,user-setting,config-file,external` | `cn-openai-runtime` or `cn-native-runtime` | exact business-space ID from the Model Studio `API Host` or workspace details; pass only the workspace-ID hostname label, not a full URL or host; treat it as opaque and do not invent or normalize a prefix | `{WorkspaceId}` in the selected Base URL |

`ALIYUN_BAILIAN_CN_WORKSPACE_ID` is a repository-defined configuration reference, not an Alibaba Cloud predefined environment-variable name.

## How To Obtain It

Copy `API Host` from either:

1. the dialog shown after creating an API Key; or
2. the workspace-management page.

Example: when `API Host` is `llm-example.cn-beijing.maas.aliyuncs.com`, the workspace ID is `llm-example`.

## Profile Resolution

| Profile Key | Workspace ID Required | Resolved Base URL |
| --- | --- | --- |
| `cn-openai-runtime` | `yes` | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1` |
| `cn-native-runtime` | `yes` | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/api/v1` |
| `cn-shared-openai-runtime` | `no` | `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| `cn-shared-native-runtime` | `no` | `https://dashscope.aliyuncs.com/api/v1` |

## Fail-Fast Rules

- Before URL serialization, require an explicit profile key and resolve every placeholder declared by that profile.
- If a workspace profile is selected and `ALIYUN_BAILIAN_CN_WORKSPACE_ID` is missing, empty, or leaves `{WorkspaceId}` unresolved, return `config_error` and stop.
- Reject a workspace value containing a URL scheme, path, query, fragment, whitespace, or unresolved braces; the value must be the exact workspace-ID hostname label.
- Never infer a workspace ID from the API Key, account ID, region, project name, or model ID.
- Never switch from a workspace profile to a shared profile automatically. The caller must explicitly select the shared profile.
- Model, endpoint URL, API Key, and billing plan must be compatible; China Mainland and International credentials are not interchangeable.
- A workspace-specific domain accepts only an API Key belonging to that workspace. A shared DashScope domain can use API Keys from different workspaces.
- A workspace-specific direct-model profile carries the workspace in the hostname; a shared profile does not. Do not add `X-DashScope-WorkSpace` to these routes; use it only when a separate application-API contract explicitly requires it.
- For asynchronous image jobs, task creation and polling must reuse the same profile, region, workspace when applicable, and API Key.

## Minimal Configuration Example

```text
ConnectionProfileKey=cn-native-runtime
ALIYUN_BAILIAN_CN_WORKSPACE_ID=llm-example
ALIYUN_BAILIAN_CN_API_KEY=<secret reference resolved by the host>
```

This resolves the native Base URL to:

```text
https://llm-example.cn-beijing.maas.aliyuncs.com/api/v1
```

## Official Sources

- `https://help.aliyun.com/zh/model-studio/regions/`
- `https://help.aliyun.com/zh/model-studio/base-url`
- `https://help.aliyun.com/zh/model-studio/qwen-image-generation-and-editing-api-reference`
