# Aliyun Bailian International Workspace Configuration

This file declares the connection inputs required before an Agent can construct a Singapore request URL. It never stores the user's actual values.

## Configuration Inputs

| Ref | Type | Sensitivity | Allowed Sources | Required When | Value Contract | Binds To |
| --- | --- | --- | --- | --- | --- | --- |
| `ALIYUN_BAILIAN_INTL_API_KEY` | `string` | `secret` | `env` | every Singapore profile | API Key issued for the Singapore region and the selected billing plan | `Authorization: Bearer ...` |
| `ALIYUN_BAILIAN_INTL_WORKSPACE_ID` | `string` | `non-secret` | `env,user-setting,config-file,external` | `intl-openai-runtime` or `intl-native-runtime` | exact business-space ID from the Model Studio `API Host` or workspace details; pass only the workspace-ID hostname label, not a full URL or host; treat it as opaque and do not invent or normalize a prefix | `{WorkspaceId}` in the selected Base URL |

`ALIYUN_BAILIAN_INTL_WORKSPACE_ID` is a repository-defined configuration reference, not an Alibaba Cloud predefined environment-variable name.

## How To Obtain It

Copy `API Host` from the API Key creation result or the workspace-management page. Example: for `llm-example.ap-southeast-1.maas.aliyuncs.com`, the workspace ID is `llm-example`.

## Profile Resolution

| Profile Key | Workspace ID Required | Resolved Base URL |
| --- | --- | --- |
| `intl-openai-runtime` | `yes` | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` |
| `intl-native-runtime` | `yes` | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/api/v1` |
| `intl-shared-openai-runtime` | `no` | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |
| `intl-shared-native-runtime` | `no` | `https://dashscope-intl.aliyuncs.com/api/v1` |

## Fail-Fast Rules

- Require an explicit profile key and resolve every placeholder before URL serialization.
- If a workspace profile is selected and `ALIYUN_BAILIAN_INTL_WORKSPACE_ID` is missing, empty, or leaves `{WorkspaceId}` unresolved, return `config_error` and stop.
- Reject a workspace value containing a URL scheme, path, query, fragment, whitespace, or unresolved braces; the value must be the exact workspace-ID hostname label.
- Never infer a workspace ID or switch to a shared profile automatically.
- Model, endpoint URL, API Key, and billing plan must be compatible; Singapore and China Mainland credentials are not interchangeable.
- A workspace-specific domain accepts only an API Key belonging to that workspace. A shared DashScope International domain can use API Keys from different workspaces.
- A workspace-specific direct-model profile carries the workspace in the hostname; a shared profile does not. Do not add `X-DashScope-WorkSpace` to these routes unless a separate application-API contract explicitly requires it.

## Official Sources

- `https://help.aliyun.com/zh/model-studio/regions/`
- `https://help.aliyun.com/zh/model-studio/base-url`
