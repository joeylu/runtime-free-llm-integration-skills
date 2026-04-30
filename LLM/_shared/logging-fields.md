# Shared Logging Fields

Use these normalized fields across all `skill-llm-xxxx` integrations.

## Minimum Fields

| Field | Meaning |
| --- | --- |
| `provider` | provider identifier such as `aliyun-bailian` |
| `connection_profile_key` | selected connection profile key such as `build` or `plan` |
| `endpoint_kind` | endpoint kind such as `official`, `gateway`, or `custom` |
| `request_kind` | `chat`, `vision`, `imaging`, or `music` |
| `model` | exact provider model |
| `is_stream` | whether stream transport was used |
| `thinking_requested` | caller intent |
| `thinking_applied` | normalized provider result |
| `reasoning_effort` | applied enum-style reasoning effort when available |
| `reasoning_output_visibility` | whether the provider returned raw, summary, encrypted, usage-only, or no reasoning output |
| `temperature` | applied temperature when available |
| `response_format` | requested structured-output mode when available |
| `tool_count` | number of caller-defined tools supplied |
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
- `result_count`
- `warnings`

## Rule

Log normalized fields first so dashboards and troubleshooting stay provider-agnostic.
