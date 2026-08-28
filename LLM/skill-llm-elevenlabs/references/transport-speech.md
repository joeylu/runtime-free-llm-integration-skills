# ElevenLabs Eleven v3 Text-to-Speech Transport

Use for `tts-convert`, `tts-convert-with-timestamps`, `tts-stream`, and `tts-stream-with-timestamps` only.

## Normalized Input

Required:

- `RequestKind = speech`
- `Model = eleven_v3`
- `Inputs.Text`
- `Inputs.VoiceId`

Optional maintained mappings:

- `Inputs.LanguageCode -> language_code`
- `Inputs.Seed -> seed`
- typed `ProviderOptions.ElevenLabs` fields from `model-parameters.md`

## Serialization

1. Put `Inputs.VoiceId` into the route path.
2. Put `Inputs.Text` into body `text`.
3. Always put `model_id = eleven_v3` in the body. Do not use the endpoint default.
4. Put `output_format`, `enable_logging`, and deprecated latency field only in the query location documented by the exact endpoint. New code must not use deprecated fields.
5. Put `language_code`, verified `voice_settings`, pronunciation dictionary locators, seed, continuity fields, and normalization fields in the JSON body only when whitelisted.
6. Send `xi-api-key` from the resolved credential reference.

## Input Gates

- Reject empty text.
- Reject text longer than the maintained 5,000-character `eleven_v3` TTS limit; splitting must be an explicit host operation.
- Reject missing `VoiceId`.
- Reject `voice_settings.similarity_boost`, `voice_settings.use_speaker_boost`, and `voice_settings.speed` for `eleven_v3` under current v3-specific guidance.
- Reject `voice_settings.style` until v3-specific request support is re-verified.
- Do not use SSML `<break>` tags as a v3 pause mechanism. V3 uses prompting/audio tags and punctuation.

## Streaming

- `tts-stream` returns binary/streaming audio chunks. Append chunks to one normalized `AudioOutputs` item or pass them to the host audio sink without converting them to text.
- `tts-stream-with-timestamps` returns streamed JSON carrying `audio_base64` plus alignment. Decode audio into `AudioOutputs`; preserve alignment in `ProviderMeta`.
- These are HTTP streaming routes. They are not WebSockets.
- Never use `/v1/text-to-speech/{voice_id}/stream-input` with `eleven_v3`; official docs explicitly exclude v3 from that WebSocket.

## Non-Stream Response Mapping

- `tts-convert`: response audio -> `AudioOutputs[0]`.
- `tts-convert-with-timestamps`: decode `audio_base64` -> `AudioOutputs[0]`; place `alignment` and `normalized_alignment` under `ProviderMeta`.
- Preserve provider request IDs in `ProviderMeta` when returned; do not treat them as cross-model continuation IDs.

## Failure Rules

- HTTP 4xx/5xx is not a signal to switch model, voice, route, output format, or tier.
- If a requested output format needs a higher plan and the provider rejects it, return the provider error; do not downgrade the format automatically.
- `enable_logging=false` without Enterprise zero-retention entitlement is a capability/configuration error, not a reason to retry with logging enabled.

## Sources

- https://elevenlabs.io/docs/overview/models
- https://elevenlabs.io/docs/api-reference/text-to-speech/convert
- https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps
- https://elevenlabs.io/docs/api-reference/text-to-speech/stream
- https://elevenlabs.io/docs/api-reference/text-to-speech/stream-with-timestamps
- https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/tts-vs-ttd-websockets
- https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech
