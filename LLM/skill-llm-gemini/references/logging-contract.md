# Gemini Logging Contract

Use this file when the caller wants request logging, troubleshooting, or trace retention.

Read `../../_shared/logging-fields.md` first.

## Default Rule

Log normalized fields first.

Add Gemini-specific raw payload snapshots only when debugging value outweighs storage cost or privacy risk.

## Minimum Log Payload

Store at least:

- `provider = gemini`
- `connection_profile_key`
- `endpoint_kind`
- `api_surface`
- `base_url`
- `request_url`
- `request_kind`
- `model`
- `catalog_verification_state`
- `is_stream`
- `reasoning_effort`
- `thinking_requested`
- `thinking_applied`
- `reasoning_summary_requested`
- `reasoning_output_visibility`
- `response_format`
- `tool_count`
- `temperature`
- `image_size`
- `reference_image_count`
- `usage`
- `latency_ms`
- `finish_reason`
- `error_code`
- `error_stage`
- `retry_count`

## Helpful Provider Extras

Store these when available:

- official endpoint path
- request id
- candidate count
- safety ratings
- prompt feedback
- thought signature presence
- thought summary presence
- inline image output count
- provider finish reason

## Fail-Fast Rule

If the user asks for detailed traces that include raw prompts, raw outputs, images, files, function arguments, thought summaries, or thought signatures, confirm that this is intended before implementation.
