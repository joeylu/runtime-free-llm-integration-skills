# Aliyun Bailian China Mainland Logging Contract

Use this file when the caller wants request logging, troubleshooting, or trace retention.

Read `../../_shared/logging-fields.md` first.

## Default Rule

Log normalized fields first.

Add Aliyun-specific raw payload snapshots only when debugging value outweighs storage cost or privacy risk.

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
- price region
- provider request id
- job id for imaging or music
- raw finish reason
- raw provider status

## Fail-Fast Rule

If the user asks for detailed traces that include raw prompts, raw outputs, or binary references, confirm that this is intended before implementation.
