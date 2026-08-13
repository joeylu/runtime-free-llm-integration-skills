# Aliyun Bailian International Request URLs

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `qwen3.8-max` | `responses` | `v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `body-param` | `verified` | 2026-08-06 | `https://help.aliyun.com/zh/model-studio/compatibility-with-openai-responses-api` | `Use exact Responses payload; no video/audio; thinking_budget unsupported.` |
| `vision` | `qwen3.8-max` | `responses` | `v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `body-param` | `verified` | 2026-08-06 | `https://help.aliyun.com/zh/model-studio/compatibility-with-openai-responses-api` | `Maintained for input_image only.` |
| `chat` | `qwen3.8-max` | `chat-completions` | `v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | 2026-08-06 | `https://help.aliyun.com/zh/model-studio/qwen-api-via-openai-chat-completions` | `OpenAI-compatible Chat Completions.` |
| `vision` | `qwen3.8-max` | `chat-completions` | `v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | 2026-08-06 | `https://help.aliyun.com/zh/model-studio/qwen-api-via-openai-chat-completions` | `Typed image/video content only.` |
| `chat` | `qwen3.8-max` | `multimodal-generation` | `v1` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `/services/aigc/multimodal-generation/generation` | `{Profile.Base URL}/services/aigc/multimodal-generation/generation` | `same-url` | `verified` | 2026-08-06 | `https://help.aliyun.com/zh/model-studio/qwen-api-via-dashscope` | `Streaming uses the same URL and requires X-DashScope-SSE: enable; non-stream omits that header.` |
| `vision` | `qwen3.8-max` | `multimodal-generation` | `v1` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `/services/aigc/multimodal-generation/generation` | `{Profile.Base URL}/services/aigc/multimodal-generation/generation` | `same-url` | `verified` | 2026-08-06 | `https://help.aliyun.com/zh/model-studio/qwen-api-via-dashscope` | `Streaming uses the same URL and requires X-DashScope-SSE: enable; non-stream omits that header.` |

## Rules

Resolve an explicit Singapore workspace or shared profile before the request path. Never use a Beijing endpoint, leave placeholders unresolved, or switch profiles silently.
