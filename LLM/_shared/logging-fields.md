# Shared Logging Fields

Use these normalized fields across all `skill-llm-xxxx` integrations.

## Minimum Fields

| Field | Meaning |
| --- | --- |
| `provider` | provider identifier such as `aliyun-bailian-cn` or `aliyun-bailian-intl` |
| `connection_profile_key` | resolved connection profile key such as `build` or `plan` |
| `endpoint_kind` | endpoint kind such as `official`, `gateway`, or `custom` |
| `api_surface` | provider API surface such as `responses`, `chat-completions`, `generate-content`, or `dashscope-native-sync` |
| `base_url` | resolved non-secret base URL |
| `request_url` | resolved non-secret request URL with secret query values redacted |
| `request_kind` | `chat`, `vision`, `imaging`, `video`, `music`, `speech`, or `transcription` |
| `model` | exact provider model |
| `is_stream` | whether stream transport was used |
| `thinking_requested` | caller intent |
| `thinking_applied` | normalized provider result |
| `reasoning_effort` | applied enum-style reasoning effort when available |
| `reasoning_output_visibility` | whether the provider returned raw, summary, encrypted, usage-only, or no reasoning output |
| `temperature` | applied temperature when available |
| `response_format` | requested structured-output mode when available |
| `tool_count` | number of caller-defined tools supplied |
| `hosted_tool_count` | number of provider-hosted tools supplied |
| `continuation_id_present` | whether a provider continuation ID was supplied; do not log the opaque value by default |
| `store_response` | requested provider-side persistence setting when available |
| `cache_mode` | normalized cache intent when available |
| `cached_input_tokens` | provider-reported cache-hit input tokens when available |
| `usage` | normalized usage summary |
| `latency_ms` | end-to-end latency |
| `finish_reason` | normalized completion reason |
| `error_code` | shared error code when failed |
| `error_stage` | shared error stage when failed |
| `retry_count` | retry count |
| `started_at` | absolute start timestamp |
| `ended_at` | absolute end timestamp |

## Optional Fields

- `provider_request_id`
- `job_id`
- `raw_request_snapshot`
- `raw_response_snapshot`
- `catalog_verification_state`
- `reasoning_summary_requested`
- `continuation_id_returned`
- `hosted_tool_usage`
- `image_size`
- `video_resolution`
- `video_duration_seconds`
- `video_aspect_ratio`
- `video_task_type`
- `video_task_status`
- `reference_image_count`
- `reference_video_count`
- `reference_audio_count`
- `result_count`
- `voice_id`
- `output_format`
- `source_kind`
- `audio_duration_seconds`
- `speaker_count`
- `timestamp_granularity`
- `warnings`

## Rule

Log normalized fields first so dashboards and troubleshooting stay provider-agnostic.

Do not log API keys, signed query strings, bearer tokens, raw presigned media URLs, raw continuation IDs, or provider-hosted tool credentials by default.
