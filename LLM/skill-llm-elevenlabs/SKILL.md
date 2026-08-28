---
name: skill-llm-elevenlabs
description: Runtime contract for ElevenLabs direct-model integration using exactly `eleven_v3` for text-to-speech/dialogue and `scribe_v2` for batch speech-to-text. Covers official authentication, HTTP and streaming routes, timestamp variants, Eleven v3 Text-to-Dialogue WebSocket, model parameters, pricing, response mapping, and fail-fast restrictions. It constructs requests only and never executes them.
---

# Skill LLM ElevenLabs

## Purpose

Build a validated ElevenLabs request for `eleven_v3` speech generation or `scribe_v2` batch transcription after the model and capability have been selected by the user or host project. This skill is not a model selector, voice selector, or execution layer.

## Read Order

Read shared schemas first, then:

1. `references/connection-profiles.md`
2. `references/request-urls.md`
3. `references/model-catalog.md`
4. `references/capability-matrix.md`
5. `references/model-parameters.md`
6. the matching transport:
   - `references/transport-speech.md`
   - `references/transport-dialogue.md`
   - `references/transport-transcription.md`
7. `references/pricing-matrix.md` only when cost matters
8. `references/logging-contract.md` when logging matters
9. `references/model-sync.md` only during an explicit update

## Runtime Rules

- Provider identifier is `elevenlabs`; maintained model IDs are exactly `eleven_v3` and `scribe_v2`.
- Authentication uses the `xi-api-key` header from the secret reference `ELEVENLABS_API_KEY`. Ordinary maintained requests do not require a workspace ID.
- Resolve the full route key before validating fields or serializing a request.
- Always send the maintained `model_id` explicitly. In particular, ElevenLabs TTS endpoints default to another model when `model_id` is omitted; never rely on that default.
- `eleven_v3` single-voice Text to Speech and multi-speaker Text to Dialogue are different surfaces. Do not rewrite one into the other.
- Standard Text-to-Speech WebSocket `/v1/text-to-speech/{voice_id}/stream-input` does not support `eleven_v3`. For the maintained v3 WebSocket flow use the Text-to-Dialogue WebSocket only.
- The Text-to-Dialogue WebSocket is a Beta Service and currently requires workspace-level product access plus Text-to-Speech permission. A missing entitlement is a capability/configuration failure; never switch to `eleven_v3_conversational`.
- `scribe_v2` is batch transcription. `scribe_v2_realtime` is not maintained by this skill and must not be substituted.
- New Scribe v2 integrations use exactly one of `file` or `source_url`. `cloud_storage_url` is deprecated and must not be emitted by new code.
- `unknown` is fail-closed. Do not infer a field, limit, output format, pricing rule, or WebSocket message from another ElevenLabs product or model.

## Request Kinds

- `speech`: Eleven v3 single-voice TTS or Text-to-Dialogue generation
- `transcription`: Scribe v2 batch audio/video transcription

## Out of Scope

- `eleven_v3_conversational`
- `scribe_v2_realtime`
- standard TTS WebSocket for `eleven_v3`
- Text-to-Dialogue Multi-Context WebSocket
- Flows asynchronous speech generation (`/v1/flows/text-to-speech`), even though that API can target `eleven_v3`; it was not part of this revision's approved runtime surfaces
- other ElevenLabs TTS/STT models
- voice cloning, voice design, voice changer, Speech Engine, ElevenAgents, dubbing, sound effects, music, forced alignment, or Studio
- model/voice recommendation, automatic fallback, request execution, deployment, or webhook hosting
