# Aliyun Bailian China Mainland Request URLs

Use this file to resolve the final request URL after the connection profile and API surface are selected.

Read `../../_shared/request-url-matrix-schema.md` first.

## Current Matrix

| Request Kind | Model Scope | API Surface | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `catalog-selected` | `chat-completions` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-05-01` | `https://help.aliyun.com/zh/model-studio/use-qwen-by-calling-api` | `China Mainland OpenAI-compatible path; template profile base URL is https://dashscope.aliyuncs.com/compatible-mode/v1` |
| `vision` | `catalog-selected` | `chat-completions` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-05-01` | `https://help.aliyun.com/zh/model-studio/vision-model` | `vision uses the OpenAI-compatible chat path when the selected model and fields are verified` |
| `imaging` | `z-image-turbo,qwen-image-2.0,qwen-image-2.0-pro,wan2.7-image,wan2.7-image-pro` | `dashscope-native-sync` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `/services/aigc/multimodal-generation/generation` | `{Profile.Base URL}/services/aigc/multimodal-generation/generation` | `n/a` | `verified` | `2026-05-01` | `https://help.aliyun.com/zh/model-studio/z-image-api-reference ; https://help.aliyun.com/zh/model-studio/qwen-image-api ; https://help.aliyun.com/zh/model-studio/wan-image-generation-and-editing-api-reference` | `synchronous native image path for selected Z-Image, Qwen-Image, and Wan 2.7 rows` |
| `imaging` | `wan2.7-image,wan2.7-image-pro` | `dashscope-native-async` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `/services/aigc/image-generation/generation` | `{Profile.Base URL}/services/aigc/image-generation/generation` | `n/a` | `verified` | `2026-05-01` | `https://help.aliyun.com/zh/model-studio/wan-image-generation-and-editing-api-reference` | `asynchronous Wan 2.7 image job submission path; pair with task polling before marking a job complete` |
| `music` | `catalog-selected` | `dashscope-native` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `no selected music rows` | `keep blocked until a music model sync verifies exact endpoint paths` |

## Rules

- Use only China Mainland base URLs in this skill.
- Do not fall back to `https://dashscope-intl.aliyuncs.com`.
- Resolve the profile first so `{Profile.Base URL}` matches the selected endpoint kind.
- Do not put API keys in request URL templates.
