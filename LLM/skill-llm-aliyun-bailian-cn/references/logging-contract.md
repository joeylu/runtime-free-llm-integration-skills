# Aliyun Bailian China Mainland Logging Contract

Use this file when the caller wants request logging, troubleshooting, or trace retention.

Read `../../_shared/logging-fields.md` first.

## Default Rule

Log normalized fields first. Add Aliyun-specific raw payload snapshots only when debugging value outweighs storage cost or privacy risk.

## Minimum Log Payload

Store at least:

- `provider = aliyun-bailian-cn`
- `connection_profile_key` when the host uses profiles
- `endpoint_kind`
- `api_surface`
- `base_url`
- `request_url`
- `request_kind`
- `model`
- `catalog_verification_state`
- `is_stream`
- `thinking_requested`
- `thinking_applied`
- `reasoning_effort`
- `reasoning_output_visibility`
- `temperature`
- `response_format`
- `tool_count`
- `hosted_tool_count`
- `continuation_id_present`
- `continuation_id_returned`
- `store_response`
- `cache_mode`
- `cached_input_tokens`
- `usage`
- `latency_ms`
- `finish_reason`
- `error_code`
- `error_stage`
- `retry_count`

## Helpful Provider Extras

Store these when available:

- official endpoint path
- price region
- provider request ID
- raw finish reason and raw provider status
- Responses event type and sequence number during stream debugging
- `usage.output_tokens_details.reasoning_tokens`
- `usage.x_tools` hosted-tool counts
- job ID for imaging or music

## Redaction Rules

- Do not log API keys, bearer tokens, raw `previous_response_id` values, workspace secrets, signed media URLs, MCP headers, or knowledge-base credentials by default.
- Prefer booleans such as `continuation_id_present` over the opaque continuation value.
- Raw prompts, outputs, image references, function arguments, and hosted-tool results require an explicit project retention decision.

## Fail-Fast Rule

If the user asks for detailed traces that include raw prompts, raw outputs, tool credentials, or binary references, confirm that this is intended before implementation.
