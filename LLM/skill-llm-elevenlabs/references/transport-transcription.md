# ElevenLabs Scribe v2 Batch Transcription Transport

Use only for `transcription::scribe_v2::stt-batch::v1::official`.

## Request Shape

Endpoint: `POST /v1/speech-to-text`

Content type: multipart/form-data.

Required:

- `model_id = scribe_v2`
- exactly one maintained source:
  - `Inputs.AudioFile -> file`, or
  - `Inputs.SourceUrl -> source_url`

Do not emit `cloud_storage_url` in new code. It is deprecated by ElevenLabs in favor of `source_url`.

## Source Rules

- Reject requests with neither source or both sources.
- `source_url` may point to provider-supported hosted audio/video URLs, including hosted services documented by ElevenLabs.
- Do not log a raw source URL because it can contain credentials or signed query parameters.
- Official current documentation conflicts on uploaded-file ceiling: the overview says 3 GB while the endpoint reference says under 5.0 GB. This skill fails closed at `<3 GB`. The conflict must remain visible; do not silently raise the limit.
- Exact maximum duration is left `unknown` because current official overview wording is internally inconsistent. If a host needs local duration pre-validation, re-verify before adding a hard cap.

## Maintained Parameters

Use only fields whitelisted in `model-parameters.md`, including when needed:

- `language_code`
- `tag_audio_events`
- `num_speakers`
- `timestamps_granularity`
- `diarize`
- `diarization_threshold`
- `file_format`
- `temperature`
- `seed`
- `keyterms`
- `use_multi_channel`
- entity detection/redaction controls
- `no_verbatim`
- `use_speaker_library`
- `detect_speaker_roles`
- webhook fields

Do not infer nested values that the whitelist does not state.

## Compatibility Gates

- `num_speakers` is 1..32.
- `diarization_threshold` is valid only when `diarize=true` and `num_speakers=null`.
- Speaker-library identification requires diarization.
- Speaker-role detection requires diarization and cannot be combined with multi-channel.
- Multi-channel currently supports up to 5 channels; each channel is billed for the full duration.
- Combined multi-channel output requires timestamps; do not use `timestamps_granularity=none` for that flow.
- Preserve endpoint-documented entity-detection/redaction incompatibilities; do not let a generic UI create invalid combinations.
- Keyterms are paid prompting controls and have provider length/count/character restrictions.

## Webhook Delivery

`webhook=true` is still Scribe v2 batch transcription, not realtime STT.

When enabled:

- the POST can return before transcription is available;
- do not set normalized `IsCompleted=true` merely because the provider accepted the request;
- a configured STT webhook is required for final delivery;
- unresolved webhook configuration is `config_error`;
- this repository does not host or deploy the webhook receiver.

## Response Mapping

For direct response mode:

- response `text` -> normalized `TextContent`;
- `language_code`, `language_probability`, `words`, speaker IDs, timestamps, `audio_duration_secs`, entities, channel metadata, and other STT detail -> `ProviderMeta`;
- do not flatten word timestamps into plain transcript text.

For separate multi-channel output, preserve the channel index/structure under `ProviderMeta` rather than concatenating channels without provenance.

## Pricing-Sensitive Features

The current API pricing page publishes:

- Scribe v2 base transcription: $0.22/hour;
- entity detection: $0.070/hour add-on;
- keyterm prompting: $0.050/hour add-on.

Other endpoint-described percentage surcharges must be treated from their exact endpoint rule, not derived from these three prices.

## Sources

- https://elevenlabs.io/docs/api-reference/speech-to-text/convert
- https://elevenlabs.io/docs/api-reference/speech-to-text/convert?explorer=true
- https://elevenlabs.io/docs/overview/capabilities/speech-to-text/
- https://elevenlabs.io/docs/overview/models
- https://elevenlabs.io/pricing/api
