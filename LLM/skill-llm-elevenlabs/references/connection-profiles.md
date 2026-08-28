# ElevenLabs Connection Profiles

Read `../../_shared/connection-profile-schema.md` first.

## Authentication Invariants

- Secret reference: `ELEVENLABS_API_KEY`.
- HTTP authentication header: `xi-api-key: <resolved secret>`.
- Do not put the API key in a URL or logs.
- No workspace ID is required for the maintained ordinary TTS, Text-to-Dialogue HTTP, or Scribe v2 requests.
- Text-to-Dialogue WebSocket access can be enabled at the workspace level, but the WebSocket request still does not take a workspace-ID path/query field.

## Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Request Kinds | API Surfaces | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `runtime` | `ElevenLabs Runtime` | `elevenlabs` | `runtime` | `active` | `official` | `https://api.elevenlabs.io` | `ELEVENLABS_API_KEY` | `env` | `speech,transcription` | `tts-convert,tts-convert-with-timestamps,tts-stream,tts-stream-with-timestamps,dialogue-convert,dialogue-stream,dialogue-convert-with-timestamps,dialogue-stream-with-timestamps,dialogue-websocket,stt-batch` | `dialogue-websocket requires workspace-level product access; zero-retention enable_logging=false is Enterprise-only` | `2026-08-23` | `WebSocket route uses the same api.elevenlabs.io host with wss:// as specified in request-urls.md; the same API key reference is used.` |

## Custom Base URL Rule

Changing the host to a gateway or proxy requires changing `Endpoint Kind` and re-verifying every maintained HTTP and WebSocket route. Do not assume a gateway supports binary streaming, multipart upload, WebSocket upgrade, or ElevenLabs-specific headers.

## Sources

- https://elevenlabs.io/docs/api-reference/authentication
- https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tdd

## Authentication scope

This maintained runtime profile uses `xi-api-key` from `ELEVENLABS_API_KEY`. ElevenLabs single-use token authentication is not maintained here; do not synthesize or substitute it.
