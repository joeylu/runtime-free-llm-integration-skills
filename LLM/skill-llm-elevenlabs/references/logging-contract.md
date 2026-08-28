# ElevenLabs Logging Contract

Read `../../_shared/logging-fields.md` first.

## Minimum Log Payload

Store normalized fields first, including:

- `provider = elevenlabs`
- `connection_profile_key`
- `endpoint_kind`
- `api_surface`
- `base_url`
- redacted `request_url`
- `request_kind`
- exact `model`
- `is_stream`
- `usage` when returned/derived by the host from provider billing metadata
- `latency_ms`
- `error_code`
- `error_stage`
- `retry_count`

## Speech Extras

When useful, store:

- voice ID or a stable host-side alias; hash it if project privacy policy requires
- character count, not raw text
- output format
- whether timestamps were requested
- dialogue input count and unique voice count
- WebSocket chunk count and turn-final event count
- whether `enable_logging=false` was requested

Do not log raw generated audio by default.

## Transcription Extras

When useful, store:

- `source_kind = file|source_url`, never the raw URL
- upload byte size
- known/returned audio duration
- requested and detected language code
- diarization flag and speaker count
- timestamp granularity
- keyterm count, not raw keyterms by default
- entity feature flags/categories, not detected sensitive entity values by default
- multi-channel flag/channel count
- webhook enabled flag; hash opaque webhook IDs when stored

Do not log raw audio/video, raw transcript, raw signed source URLs, or extracted sensitive entities by default.

## Secret Rule

Never log:

- `ELEVENLABS_API_KEY` or `xi-api-key` values
- single-use tokens
- signed/authenticated source URLs
- raw WebSocket credential messages

Detailed raw payload capture requires explicit host/user approval and a privacy review.
