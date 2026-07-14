# Aliyun Bailian International Request URLs

Use this file to resolve the final request URL after the connection profile and API surface are resolved.

Read `../../_shared/request-url-matrix-schema.md` first.

## Current Matrix

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `qwen3.7-max` | `responses` | v1 | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `body-param` | `verified` | `2026-07-13` | `https://www.alibabacloud.com/help/en/model-studio/compatibility-with-openai-responses-api` | `preferred new-agent surface for qwen3.7-max chat; use the workspace-specific Singapore base URL; the legacy /api/v2/apps/protocols/compatible-mode/v1/responses path is deprecated` |
| `chat` | `documented-models` | `chat-completions` | v1 | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-07-13` | `https://www.alibabacloud.com/help/en/model-studio/text-generation ; https://www.alibabacloud.com/help/en/model-studio/deep-thinking` | `International OpenAI-compatible path; recommended Singapore profile base URL is https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` |
| `vision` | `documented-models` | `chat-completions` | v1 | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `unknown` | `unverified` | `no documented International vision rows` | `keep blocked until an International vision row is documented and verified` |
| `imaging` | `documented-models` | `dashscope-native-sync` | v1 | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `no documented International imaging rows` | `keep blocked until an International imaging model sync verifies the exact sync endpoint path` |
| `imaging` | `documented-models` | `dashscope-native-async` | v1 | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `no documented International imaging rows` | `keep blocked until an International imaging model sync verifies the exact async endpoint path` |
| `music` | `documented-models` | `dashscope-native` | v1 | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `no documented International music rows` | `keep blocked until an International music model sync verifies exact endpoint paths` |

## Rules

- Use only International/Singapore base URLs in this skill.
- Do not fall back to `https://dashscope.aliyuncs.com`.
- Resolve the profile first so `{Profile.Base URL}` matches the resolved endpoint kind.
- Do not put API keys in request URL templates.
