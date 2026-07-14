# Aliyun Bailian International / Singapore Request URLs

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`
- Key: `Request Kind + Model Scope + API Surface + API Version + Endpoint Kind`

Read `../../_shared/request-url-matrix-schema.md` first. Resolve a connection profile before substituting `{Profile.Base URL}`. No row authorizes silent surface or version fallback.

## Current Matrix

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `text-chat` | `qwen3.7-max` | `responses` | `compatible-mode-v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/responses` | `{Profile.Base URL}/responses` | `body-param` | `verified` | `2026-07-14` | `evset-aliyun-bailian-intl-request-urls-text-chat-qwen3-7-max-responses-compatible-mode-v1-77ce4d7860` | `preferred new-agent surface for qwen3.7-max chat; use the workspace-specific Singapore base URL; the legacy /api/v2/apps/protocols/compatible-mode/v1/responses path is deprecated` |
| `text-chat` | `catalog-selected` | `chat-completions` | `compatible-mode-v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-07-14` | `evset-aliyun-bailian-intl-request-urls-text-chat-catalog-selected-chat-completions-compatible-mode-v1-ce7f109949` | `International OpenAI-compatible path; recommended Singapore profile base URL is https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` |
| `multimodal-chat` | `catalog-selected` | `chat-completions` | `compatible-mode-v1` | `openai-compatible` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `unknown` | `unverified` | `evset-aliyun-bailian-intl-request-urls-multimodal-chat-catalog-selected-chat-completions-compatible-mode-v1-7e93bbd7ea` | `keep blocked until an International vision row is selected and verified` |
| `image-generation` | `catalog-selected` | `dashscope-native-sync` | `native-v1` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `evset-aliyun-bailian-intl-request-urls-image-generation-catalog-selected-dashscope-native-sync-native-v1-dd39eee98d` | `keep blocked until an International imaging model sync verifies the exact sync endpoint path` |
| `image-generation` | `catalog-selected` | `dashscope-native-async` | `native-v1` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `evset-aliyun-bailian-intl-request-urls-image-generation-catalog-selected-dashscope-native-async-native-v1-912efcdfc7` | `keep blocked until an International imaging model sync verifies the exact async endpoint path` |
| `music-generation` | `catalog-selected` | `dashscope-native` | `native-v1` | `provider-compatible` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `evset-aliyun-bailian-intl-request-urls-music-generation-catalog-selected-dashscope-native-native-v1-06831ca26d` | `keep blocked until an International music model sync verifies exact endpoint paths` |

## Rules

- Use only `verified` rows for sending.
- Treat `unknown` paths as hard stops.
- Do not put secrets or signed user data in a logged resolved URL.
- Claim details and official source locators are in `../../_evidence/evidence.json`.
