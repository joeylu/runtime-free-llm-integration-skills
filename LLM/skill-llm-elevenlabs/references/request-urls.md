# ElevenLabs Request URLs

Use this file to resolve the final route after the connection profile and API surface are known.

Read `../../_shared/request-url-matrix-schema.md` first.

## Current Matrix

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `speech` | `eleven_v3` | `tts-convert` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/v1/text-to-speech/{VoiceId}` | `{Profile.Base URL}/v1/text-to-speech/{VoiceId}` | `separate-url` | `verified` | `2026-08-23` | `https://elevenlabs.io/docs/api-reference/text-to-speech/convert` | `single-voice non-stream audio` |
| `speech` | `eleven_v3` | `tts-convert-with-timestamps` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/v1/text-to-speech/{VoiceId}/with-timestamps` | `{Profile.Base URL}/v1/text-to-speech/{VoiceId}/with-timestamps` | `separate-url` | `verified` | `2026-08-23` | `https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps` | `single-voice non-stream audio plus character timing` |
| `speech` | `eleven_v3` | `tts-stream` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/v1/text-to-speech/{VoiceId}/stream` | `{Profile.Base URL}/v1/text-to-speech/{VoiceId}/stream` | `separate-url` | `verified` | `2026-08-23` | `https://elevenlabs.io/docs/api-reference/text-to-speech/stream` | `single-voice chunked audio stream` |
| `speech` | `eleven_v3` | `tts-stream-with-timestamps` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/v1/text-to-speech/{VoiceId}/stream/with-timestamps` | `{Profile.Base URL}/v1/text-to-speech/{VoiceId}/stream/with-timestamps` | `separate-url` | `verified` | `2026-08-23` | `https://elevenlabs.io/docs/api-reference/text-to-speech/stream-with-timestamps` | `streamed JSON audio chunks plus alignment` |
| `speech` | `eleven_v3` | `dialogue-convert` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/v1/text-to-dialogue` | `{Profile.Base URL}/v1/text-to-dialogue` | `separate-url` | `verified` | `2026-08-23` | `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert` | `multi-speaker non-stream dialogue audio` |
| `speech` | `eleven_v3` | `dialogue-stream` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/v1/text-to-dialogue/stream` | `{Profile.Base URL}/v1/text-to-dialogue/stream` | `separate-url` | `verified` | `2026-08-23` | `https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream` | `multi-speaker streamed dialogue audio` |
| `speech` | `eleven_v3` | `dialogue-convert-with-timestamps` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/v1/text-to-dialogue/with-timestamps` | `{Profile.Base URL}/v1/text-to-dialogue/with-timestamps` | `separate-url` | `verified` | `2026-08-23` | `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps` | `dialogue audio plus voice segments and character timing` |
| `speech` | `eleven_v3` | `dialogue-stream-with-timestamps` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/v1/text-to-dialogue/stream/with-timestamps` | `{Profile.Base URL}/v1/text-to-dialogue/stream/with-timestamps` | `separate-url` | `verified` | `2026-08-23` | `https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream-with-timestamps` | `streamed JSON dialogue audio plus voice/timing metadata` |
| `speech` | `eleven_v3` | `dialogue-websocket` | `v1` | `official` | `GET` | `wss://api.elevenlabs.io` | `/v1/text-to-dialogue/stream-input?model_id=eleven_v3` | `wss://api.elevenlabs.io/v1/text-to-dialogue/stream-input?model_id=eleven_v3` | `n/a` | `verified` | `2026-08-23` | `https://elevenlabs.io/docs/api-reference/text-to-dialogue/ttd-websocket?explorer=true ; https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tdd` | `WebSocket upgrade; keep model_id explicit; product entitlement may be required` |
| `transcription` | `scribe_v2` | `stt-batch` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/v1/speech-to-text` | `{Profile.Base URL}/v1/speech-to-text` | `n/a` | `verified` | `2026-08-23` | `https://elevenlabs.io/docs/api-reference/speech-to-text/convert` | `multipart batch transcription; webhook delivery is an option on the same endpoint` |

## Route Rules

- Keep every surface distinct even when request bodies share fields.
- Do not rewrite `tts-*` into `dialogue-*` or the reverse.
- Do not use `/v1/text-to-speech/{voice_id}/stream-input` for `eleven_v3`; ElevenLabs explicitly excludes v3 from that WebSocket.
- Do not route `scribe_v2` to the realtime WebSocket.
- Query options such as `output_format` and `enable_logging` are appended only when allowed by the exact transport.

## Sources

- https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/tts-vs-ttd-websockets
- https://elevenlabs.io/docs/api-reference/text-to-speech/convert
- https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps
- https://elevenlabs.io/docs/api-reference/text-to-speech/stream
- https://elevenlabs.io/docs/api-reference/text-to-speech/stream-with-timestamps
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream-with-timestamps
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/ttd-websocket?explorer=true
- https://elevenlabs.io/docs/api-reference/speech-to-text/convert
