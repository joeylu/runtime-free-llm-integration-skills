# Shared Logging Fields

Use these normalized fields across all `skill-llm-xxxx` integrations.

## Minimum Fields

| Field | Meaning |
| --- | --- |
| `provider` | exact provider identifier, including regional split |
| `connection_profile_key` | selected profile key such as `build`, `plan`, or `runtime` |
| `endpoint_kind` | endpoint kind such as `official`, `openai-compatible`, `gateway`, or `custom` |
| `api_surface` | exact resolved provider API surface |
| `api_version` | exact resolved API version |
| `base_url` | resolved non-secret base URL |
| `request_url` | resolved non-secret request URL with secret query values redacted |
| `request_kind` | canonical request kind |
| `model` | exact provider model |
| `billing_region` | resolved billing region |
| `deployment_scope` | resolved deployment scope |
| `serving_region` | resolved serving region |
| `is_stream` | whether stream transport was used |
| `thinking_requested` | caller intent |
| `thinking_applied` | normalized provider result |
| `reasoning_effort` | applied enum-style reasoning effort when available |
| `reasoning_output_visibility` | `raw`, `summary`, `encrypted`, `usage-only`, `none`, or another verified state |
| `temperature` | applied temperature when available |
| `response_format` | requested structured-output mode when available |
| `tool_count` | number of caller-defined tools supplied |
| `hosted_tool_count` | number of provider-hosted tools supplied |
| `continuation_id_present` | whether an opaque continuation ID was supplied; do not log its value by default |
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

`provider_request_id`, `job_id`, `raw_request_snapshot`, `raw_response_snapshot`, `catalog_verification_state`, `reasoning_summary_requested`, `continuation_id_returned`, `hosted_tool_usage`, `image_size`, `reference_image_count`, `result_count`, and `warnings`.

## Rules

- Log normalized fields first so dashboards and troubleshooting remain provider-agnostic.
- Do not log API keys, bearer tokens, signed query strings, raw presigned media URLs, raw continuation IDs, credentials embedded in tool definitions, or unredacted user secrets.
- Logging a request must not imply that an unverified route, price, or capability is valid.
