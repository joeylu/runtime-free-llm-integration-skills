# Aliyun Logging Contract

Use this file when the caller wants request logging, troubleshooting, or trace retention.

Read `../_shared/logging-fields.md` first.

## Default Rule

Log normalized fields first.

Add Aliyun-specific raw payload snapshots only when debugging value outweighs storage cost or privacy risk.

## Minimum Log Payload

Store at least:

- `provider = aliyun-bailian`
- `connection profile key` when the host uses profiles
- `request kind`
- `model`
- `catalog verification state`
- `stream or non-stream`
- `thinking requested`
- `thinking applied`
- `temperature`
- `usage`
- `latency`
- `finish reason`
- `error code`
- `error stage`
- `retry count`

## Helpful Provider Extras

Store these when available:

- official endpoint path
- provider request id
- job id for imaging or music
- raw finish reason
- raw provider status

## Fail-Fast Rule

If the user asks for detailed traces that include raw prompts, raw outputs, or binary references, confirm that this is intended before implementation.
