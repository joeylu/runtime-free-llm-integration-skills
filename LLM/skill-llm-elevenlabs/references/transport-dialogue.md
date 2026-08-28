# ElevenLabs Eleven v3 Text-to-Dialogue Transport

Use for the four HTTP dialogue surfaces and the maintained single-context Text-to-Dialogue WebSocket.

## HTTP Normalized Input

Required:

- `RequestKind = speech`
- `Model = eleven_v3`
- `Inputs.DialogueInputs`: ordered list of `{Text, VoiceId}`

Map to wire `inputs[] = {text, voice_id}`.

## HTTP Gates

- At least one dialogue input is required.
- Every input needs non-empty text and a non-empty voice ID.
- Maximum unique voice IDs: 10.
- Fail closed when total `inputs[].text` exceeds 2,000 characters. The current endpoint says longer requests can terminate early in streaming or return a validation error; this skill does not knowingly send an unreliable oversized request.
- Always send `model_id = eleven_v3` even though current HTTP endpoints default to it.
- `settings` is a documented object, but its exact request-side nested field whitelist is not sufficiently verified in this skill. Reject non-empty `settings` until that nested contract is explicitly synced.

## HTTP Response Mapping

- `dialogue-convert`: binary audio -> `AudioOutputs[0]`.
- `dialogue-stream`: streamed audio chunks -> one normalized audio output/sink.
- `dialogue-convert-with-timestamps`: decode `audio_base64`; put `voice_segments`, `alignment`, and `normalized_alignment` in `ProviderMeta`.
- `dialogue-stream-with-timestamps`: decode each `audio_base64` chunk; accumulate/publish `voice_segments` and alignment in `ProviderMeta`.

## Text-to-Dialogue WebSocket

Route:

`wss://api.elevenlabs.io/v1/text-to-dialogue/stream-input?model_id=eleven_v3`

Rules:

1. This is a Beta Service. Require confirmed workspace-level product access and an API key with Text-to-Speech permission before treating the route as available.
2. Authenticate with the resolved ElevenLabs credential. Header authentication is preferred in server-side hosts. Do not put a persistent API key into a browser URL.
3. The first JSON message must register `voices`. `eleven_v3` supports up to 10 registered voices on this protocol.
4. Send content in `inputs`, each item containing `text`, registered `voice_id`, and optional `new_turn`.
5. Handle provider audio messages as base64 audio chunks. Treat `is_final_audio_for_turn` as a turn boundary signal, not necessarily the end of the socket.
6. Support documented control messages `flush`, `close_socket`, and `keep_alive` only. The current guide says `keep_alive` resets a 20-second receive timeout.
7. Do not send `seed`; WebSocket seed support is `unknown` in this skill.
8. Do not accept the provider's default `eleven_v3_conversational`; model_id must be explicit `eleven_v3`.
9. Do not rewrite to the Text-to-Speech WebSocket.
10. Do not use the Multi-Context Text-to-Dialogue WebSocket; it is outside this approved scope.

## Audio Boundary Note

When exact turn boundaries matter, prefer an output format whose buffering behavior is appropriate for the host. Do not infer codec boundary guarantees that are not in the selected format/protocol documentation.

## Sources

- https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream-with-timestamps
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/ttd-websocket?explorer=true
- https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tdd
