# ElevenLabs Model Update

Use this file only for an explicit ElevenLabs model/API sync.

## Maintained Models

- TTS/dialogue: `eleven_v3`
- batch STT: `scribe_v2`

## Official Sources

- https://elevenlabs.io/docs/overview/models
- https://elevenlabs.io/docs/api-reference/authentication
- https://elevenlabs.io/docs/api-reference/text-to-speech/convert
- https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps
- https://elevenlabs.io/docs/api-reference/text-to-speech/stream
- https://elevenlabs.io/docs/api-reference/text-to-speech/stream-with-timestamps
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream-with-timestamps
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/ttd-websocket?explorer=true
- https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tdd
- https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/tts-vs-ttd-websockets
- https://elevenlabs.io/docs/api-reference/speech-to-text/convert
- https://elevenlabs.io/docs/overview/capabilities/speech-to-text/
- https://elevenlabs.io/pricing/api
- https://elevenlabs.io/docs/changelog/

## Update Steps

1. Verify exact model IDs and whether either has a documented replacement.
2. Re-verify every maintained route independently; do not infer HTTP/WebSocket parity.
3. Check whether `eleven_v3` remains unsupported on the standard TTS WebSocket.
4. Check Text-to-Dialogue WebSocket Beta status, workspace-access requirement, exact message schema, default model, and price.
5. Re-verify TTS/dialogue request limits, output-format enums, v3-specific voice-setting support, and deprecated fields.
6. Re-verify Scribe v2 source fields. Prefer `file XOR source_url`; confirm whether `cloud_storage_url` has been removed.
7. Resolve the current official Scribe file-size conflict before changing the local 3 GB fail-closed ceiling.
8. Re-verify Scribe duration rules if a host needs local duration validation.
9. Re-verify STT diarization, multi-channel, keyterm, entity, speaker-role, webhook, response, and pricing behavior.
10. Update catalog, request URLs, capability matrix, parameters, transports, pricing, logging notes, and changelog together.

## Scope Guard

Do not add `scribe_v2_realtime`, `eleven_v3_conversational`, Multi-Context WebSocket, or other ElevenLabs models during a normal sync unless the user explicitly approves expanding the maintained scope.
