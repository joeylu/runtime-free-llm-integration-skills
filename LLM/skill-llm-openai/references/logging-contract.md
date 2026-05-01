# OpenAI Logging Contract

Use this file when the caller wants request logging, troubleshooting, or trace retention.

Read `../../_shared/logging-fields.md` first.

## Default Rule

Log normalized fields first.

Add OpenAI-specific raw payload snapshots only when debugging value outweighs storage cost or privacy risk.

## Minimum Log Payload

Store at least:

- `provider = openai`
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
- `reasoning_output_visibility`
- `response_format`
- `tool_count`
- `temperature`
- `usage`
- `latency_ms`
- `finish_reason`
- `error_code`
- `error_stage`
- `retry_count`

## Helpful Provider Extras

Store these when available:

- official endpoint path
- response id
- request id
- service tier
- previous response id
- conversation id
- output item ids
- reasoning encrypted-content presence
- raw status and incomplete details

## Fail-Fast Rule

If the user asks for detailed traces that include raw prompts, raw outputs, images, files, or tool arguments, confirm that this is intended before implementation.
