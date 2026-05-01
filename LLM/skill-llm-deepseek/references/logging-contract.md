# DeepSeek Logging Contract

Use this file when the caller wants request logging, troubleshooting, or trace retention.

Read `../../_shared/logging-fields.md` first.

## Default Rule

Log normalized fields first.

Add DeepSeek-specific raw payload snapshots only when debugging value outweighs storage cost or privacy risk.

## Minimum Log Payload

Store at least:

- `provider = deepseek`
- `connection profile key`
- `endpoint kind`
- `request kind`
- `model`
- `catalog verification state`
- `stream or non-stream`
- `thinking requested`
- `thinking applied`
- `reasoning effort`
- `temperature`
- `response format`
- `tool count`
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
- cache-hit input tokens
- cache-miss input tokens
- raw finish reason
- raw provider status

## Fail-Fast Rule

If the user asks for detailed traces that include raw prompts, raw outputs, raw reasoning, or tool arguments, confirm that this is intended before implementation.
