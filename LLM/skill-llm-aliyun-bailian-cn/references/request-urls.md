# Aliyun Bailian China Mainland Request URLs

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`
- Key: `Request Kind + Model Scope + API Surface + API Version + Endpoint Kind`

Read `../../_shared/request-url-matrix-schema.md` first. Resolve a connection profile before substituting `{Profile.Base URL}`. No row authorizes silent surface or version fallback.

## Current Matrix

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `text-chat` | `qwen3.7-plus` | `responses` | `compatible-mode-v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `body-param` | `verified` | `2026-07-14` | `evset-aliyun-bailian-cn-request-urls-text-chat-qwen3-7-plus-responses-compatible-mode-v1-0c66167e59` | `preferred new-agent surface for qwen3.7-plus chat; use the workspace-specific China Mainland base URL; the legacy /api/v2/apps/protocols/compatible-mode/v1/responses path is deprecated` |
| `multimodal-chat` | `qwen3.7-plus` | `responses` | `compatible-mode-v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `body-param` | `verified` | `2026-07-14` | `evset-aliyun-bailian-cn-request-urls-multimodal-chat-qwen3-7-plus-responses-compatible-mode-v1-c61f4aadb0` | `image-only vision via input_image; Responses does not accept video or audio, and input_file is not enabled for qwen3.7-plus` |
| `text-chat` | `catalog-selected` | `chat-completions` | `compatible-mode-v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-07-14` | `evset-aliyun-bailian-cn-request-urls-text-chat-catalog-selected-chat-completions-compatible-mode-v1-ce7f109949` | `China Mainland OpenAI-compatible path; recommended profile base URL is https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1` |
| `multimodal-chat` | `catalog-selected` | `chat-completions` | `compatible-mode-v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-07-14` | `evset-aliyun-bailian-cn-request-urls-multimodal-chat-catalog-selected-chat-completions-compatible-mode-v1-7e93bbd7ea` | `vision uses the same workspace-specific OpenAI-compatible chat path when the selected model and fields are verified` |
| `image-generation` | `z-image-turbo,qwen-image-2.0,qwen-image-2.0-pro,wan2.7-image,wan2.7-image-pro` | `dashscope-native-sync` | `native-v1` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `/services/aigc/multimodal-generation/generation` | `{Profile.Base URL}/services/aigc/multimodal-generation/generation` | `n/a` | `verified` | `2026-07-14` | `evset-aliyun-bailian-cn-request-urls-image-generation-z-image-turbo-qwen-image-2-0-qwen-image-2-0-pro-wan2-7-image-wan2-7-image-pro-d-aac61c8139` | `synchronous native image path for selected Z-Image, Qwen-Image, and Wan 2.7 rows` |
| `image-generation` | `wan2.7-image,wan2.7-image-pro` | `dashscope-native-async` | `native-v1` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `/services/aigc/image-generation/generation` | `{Profile.Base URL}/services/aigc/image-generation/generation` | `n/a` | `verified` | `2026-07-14` | `evset-aliyun-bailian-cn-request-urls-image-generation-wan2-7-image-wan2-7-image-pro-dashscope-native-async-native-v1-12ca37f56b` | `asynchronous Wan 2.7 image job submission path; pair with task polling before marking a job complete` |
| `music-generation` | `catalog-selected` | `dashscope-native` | `native-v1` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `evset-aliyun-bailian-cn-request-urls-music-generation-catalog-selected-dashscope-native-native-v1-06831ca26d` | `keep blocked until a music model sync verifies exact endpoint paths` |

## Rules

- Use only `verified` rows for sending.
- Treat `unknown` paths as hard stops.
- Do not put secrets or signed user data in a logged resolved URL.
- Claim details and official source locators are in `../../_evidence/evidence.json`.
