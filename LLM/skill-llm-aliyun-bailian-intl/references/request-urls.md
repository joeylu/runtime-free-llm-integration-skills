# Aliyun Bailian International Request URLs

Use this file to resolve the final request URL after the connection profile and API surface are selected.

Read `../../_shared/request-url-matrix-schema.md` first.

## Current Matrix

| Request Kind | Model Scope | API Surface | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `catalog-selected` | `chat-completions` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-05-01` | `https://www.alibabacloud.com/help/en/model-studio/use-qwen-by-calling-api` | `International OpenAI-compatible path; template profile base URL is https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |
| `vision` | `catalog-selected` | `chat-completions` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `unknown` | `unverified` | `no selected International vision rows` | `keep blocked until an International vision row is selected and verified` |
| `imaging` | `catalog-selected` | `dashscope-native-sync` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `no selected International imaging rows` | `keep blocked until an International imaging model sync verifies the exact sync endpoint path` |
| `imaging` | `catalog-selected` | `dashscope-native-async` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `no selected International imaging rows` | `keep blocked until an International imaging model sync verifies the exact async endpoint path` |
| `music` | `catalog-selected` | `dashscope-native` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `no selected International music rows` | `keep blocked until an International music model sync verifies exact endpoint paths` |

## Rules

- Use only International/Singapore base URLs in this skill.
- Do not fall back to `https://dashscope.aliyuncs.com`.
- Resolve the profile first so `{Profile.Base URL}` matches the selected endpoint kind.
- Do not put API keys in request URL templates.
