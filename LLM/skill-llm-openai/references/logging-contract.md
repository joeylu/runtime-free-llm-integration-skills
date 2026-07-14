# OpenAI Logging Contract

Read `../../_shared/logging-fields.md` first. Log normalized fields by default and redact provider payloads.

## Required Core Fields

- `provider = openai`
- `connection_profile_key`
- `endpoint_kind`
- `api_surface`
- redacted/normalized `base_url` and `request_url`
- `request_kind`
- exact full `model`
- `catalog_verification_state`
- `is_stream`
- `response_format`
- caller `tool_count` and hosted `hosted_tool_types` separately
- `latency_ms`, `retry_count`, `finish_reason`, `error_code`, `error_stage`
- normalized `usage`

## GPT-5.6 Reasoning and State

Store when available:

- `reasoning_effort`
- `reasoning_mode`
- requested and effective `reasoning_context`
- `reasoning_summary_requested`
- `reasoning_summary_present`
- `reasoning_tokens`
- `previous_response_id_present` rather than the full ID when correlation is unnecessary
- hashed response/continuation ID when correlation is required
- `store_response`
- `encrypted_reasoning_present` and item count, never encrypted bytes
- assistant `phase` values or counts
- `status` and structured `incomplete_details`

Never log raw reasoning.

## Prompt Cache

Store:

- hashed `prompt_cache_key`, never a key that contains user data
- `prompt_cache_mode`
- `prompt_cache_ttl`
- explicit breakpoint count and placement category, not the content itself
- `cached_tokens`
- `cache_write_tokens`
- estimated cache-read and cache-write cost using the exact context band

Reject or alert on `prompt_cache_retention` for GPT-5.6.

## Tooling

Store separately:

- caller function names/counts/call IDs as hashes when needed
- hosted tool types, call counts, status, latency, and separately metered cost items
- programmatic-tool program/call/output item counts and linkage status
- MCP server identifier as an allowlisted logical name, not URL credentials or OAuth tokens
- computer/shell/code-interpreter environment ID only when non-secret and needed for correlation

Do not log raw tool arguments or tool outputs unless the owner explicitly approves the privacy and retention impact.

## Vision and Imaging

Store:

- image count, media type, dimensions, byte count, and detail level
- do not log image bytes, base64, signed URLs, or file contents by default
- for imaging: surface, size, quality, output format, compression, background, requested partial-image count, actual partial-event count, and final output count

## Safeguards and Reliability

Store:

- hashed/opaque `safety_identifier`, never the original end-user identifier
- safeguard pause count and duration when observable
- first-event latency, largest stream gap, cancellation stage, and timeout stage
- provider request ID and response ID in redacted/hashed form when required for support

## Prohibited Secrets

Never log:

- `Authorization` headers or API keys
- MCP credentials/OAuth tokens
- signed file or image URLs
- encrypted reasoning bytes
- raw prompts, outputs, images, files, or tool payloads without explicit approved trace mode
