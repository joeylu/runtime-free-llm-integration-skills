# Aliyun Bailian China Mainland Request URLs

Use this file to resolve the final request URL after the connection profile and API surface are resolved.

Read `../../_shared/request-url-matrix-schema.md` first.

## Current Matrix

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `qwen3.7-plus,qwen3.7-max` | `responses` | `v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `body-param` | `verified` | `2026-07-14` | `https://help.aliyun.com/zh/model-studio/compatibility-with-openai-responses-api` | `preferred new-agent surface for qwen3.7-plus or qwen3.7-max chat; use the workspace-specific China Mainland base URL; the legacy /api/v2/apps/protocols/compatible-mode/v1/responses path is deprecated` |
| `vision` | `qwen3.7-plus` | `responses` | `v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `body-param` | `verified` | `2026-07-13` | `https://help.aliyun.com/zh/model-studio/qwen-api-via-openai-responses` | `image-only vision via input_image; Responses does not accept video or audio, and input_file is not enabled for qwen3.7-plus` |
| `chat` | `documented-models` | `chat-completions` | `v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-07-13` | `https://help.aliyun.com/zh/model-studio/qwen-api-via-openai-chat-completions` | `China Mainland OpenAI-compatible path; recommended profile base URL is https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1` |
| `vision` | `documented-models` | `chat-completions` | `v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-07-13` | `https://help.aliyun.com/zh/model-studio/qwen-api-via-openai-chat-completions ; https://help.aliyun.com/zh/model-studio/vision-model` | `vision uses the same workspace-specific OpenAI-compatible chat path when the documented model and fields are verified` |
| `imaging` | `z-image-turbo,qwen-image-2.0,qwen-image-2.0-pro,wan2.7-image,wan2.7-image-pro` | `dashscope-native-sync` | `v1` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `/services/aigc/multimodal-generation/generation` | `{Profile.Base URL}/services/aigc/multimodal-generation/generation` | `n/a` | `verified` | `2026-05-01` | `https://help.aliyun.com/zh/model-studio/z-image-api-reference ; https://help.aliyun.com/zh/model-studio/qwen-image-api ; https://help.aliyun.com/zh/model-studio/wan-image-generation-and-editing-api-reference` | `synchronous native image path for the documented Z-Image, Qwen-Image, and Wan 2.7 rows` |
| `imaging` | `wan2.7-image,wan2.7-image-pro` | `dashscope-native-async` | `v1` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `/services/aigc/image-generation/generation` | `{Profile.Base URL}/services/aigc/image-generation/generation` | `n/a` | `verified` | `2026-05-01` | `https://help.aliyun.com/zh/model-studio/wan-image-generation-and-editing-api-reference` | `asynchronous Wan 2.7 image job submission path; pair with task polling before marking a job complete` |
| `music` | `documented-models` | `dashscope-native` | `v1` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `no documented music rows` | `keep blocked until a music model sync verifies exact endpoint paths` |

## Rules

- Use only China Mainland base URLs in this skill.
- Do not fall back to `https://dashscope-intl.aliyuncs.com`.
- Resolve the profile first so `{Profile.Base URL}` matches the resolved endpoint kind.
- Do not put API keys in request URL templates.
