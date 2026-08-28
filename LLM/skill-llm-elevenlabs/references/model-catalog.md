# ElevenLabs Model Catalog

Read `../../_shared/model-catalog-schema.md` first.

| Model Type | Operation | Input Modalities | Output Modalities | Flow Kind | API Model | Status | Identifier Kind | Resolves To | Effective From | Deprecates At | Retires At | Replacement Model | Region Scope | Context Window Tokens | Max Input Tokens | Max Output Tokens | Notes | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `speech` | `speech-generation` | `text` | `audio` | `text-to-speech,text-to-dialogue` | `eleven_v3` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `unknown` | `global` | `n/a` | `n/a` | `n/a` | `Flagship expressive TTS; 70+ languages; 5,000-character TTS model limit; supports Text to Dialogue.` | `2026-08-23` | `https://elevenlabs.io/docs/overview/models` |
| `transcription` | `speech-transcription` | `audio,video` | `text` | `speech-to-text` | `scribe_v2` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `unknown` | `global` | `n/a` | `n/a` | `n/a` | `Batch STT in 90+ languages with word timestamps, diarization up to 32 speakers, keyterms, entity detection, and audio tagging.` | `2026-08-23` | `https://elevenlabs.io/docs/overview/models ; https://elevenlabs.io/docs/overview/capabilities/speech-to-text/` |

## Catalog Boundary

`eleven_v3_conversational` and `scribe_v2_realtime` are different model IDs and are intentionally not maintained. Exact-name matching must not treat either as an alias of the rows above.
