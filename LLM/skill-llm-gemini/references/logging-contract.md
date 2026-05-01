# Gemini Logging Contract

Use this file when the caller wants request logging, troubleshooting, or trace retention.

Read `../../_shared/logging-fields.md` first.

## Default Rule

Log normalized fields first.

Add Gemini-specific raw payload snapshots only when debugging value outweighs storage cost or privacy risk.

## Minimum Log Payload

Store at least:

- `provider = gemini`
- `connection profile key`
- `endpoint kind`
- `request kind`
- `model`
- `catalog verification state`
- `stream or non-stream`
- `thinking level`
- `thinking requested`
- `thinking applied`
- `reasoning summary requested`
- `reasoning output visibility`
- `response format`
- `tool count`
- `temperature`
- `image size`
- `reference image count`
- `usage`
- `latency`
- `finish reason`
- `error code`
- `error stage`
- `retry count`

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
