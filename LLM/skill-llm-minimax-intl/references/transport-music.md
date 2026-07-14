# MiniMax International Music Transport

- Route: `music-generation@music-generation@v1`
- Model: `music-2.6` on the `build` profile only.

## Required Base Input

- `RequestKind = music-generation`
- `ConnectionProfileKey = build`
- `ApiSurface = music-generation`
- `ApiVersion = v1`
- `Model = music-2.6`
- explicit `ProviderOptions.audio_setting` when the host does not intentionally accept provider defaults

`Inputs.Prompt` and `Inputs.Lyrics` are conditionally required. Validate them together with `ProviderOptions.is_instrumental` and `ProviderOptions.lyrics_optimizer`; do not impose a single unconditional prompt-or-lyrics rule.

## Prompt and Lyrics Condition Matrix

| Condition | `Inputs.Prompt` rule | `Inputs.Lyrics` rule |
| --- | --- | --- |
| `ProviderOptions.is_instrumental = true` | required, `1..2000` characters | optional; omit when unused |
| non-instrumental, `ProviderOptions.lyrics_optimizer = false` or omitted | optional, `0..2000` characters | required, `1..3500` characters |
| non-instrumental, `ProviderOptions.lyrics_optimizer = true`, lyrics empty | required, `1..2000` characters; provider uses it to generate lyrics | optional or empty |
| non-instrumental, `ProviderOptions.lyrics_optimizer = true`, lyrics supplied | optional, `0..2000` characters | required when supplied, `1..3500` characters |

Reject an empty prompt in instrumental mode. Also reject non-instrumental optimizer-driven lyric generation when both prompt and lyrics are empty. Do not silently enable the optimizer or instrumental mode, and do not invent missing prompt or lyrics content.

## Request Mapping

| Shared/provider field | MiniMax field |
| --- | --- |
| `Model` | `model` |
| `Inputs.Prompt` | `prompt` |
| `Inputs.Lyrics` | `lyrics` |
| `IsStream` | `stream` |
| `ProviderOptions.output_format` | `output_format` (`url` or `hex`) |
| `ProviderOptions.audio_setting` | `audio_setting` |
| `ProviderOptions.lyrics_optimizer` | `lyrics_optimizer` |
| `ProviderOptions.is_instrumental` | `is_instrumental` |

When `IsStream = true`, `output_format` must be `hex`; reject `url`. Non-stream URL results expire after 24 hours. `Inputs.DurationSeconds` and `Inputs.Seed` remain blocked because the documented row does not verify them.

## Streaming and Response Mapping

- For non-stream responses, map returned audio into `AudioOutputs` and duration/sample-rate/channel/bitrate/size into `ProviderMeta`.
- For streaming, preserve provider chunk order and assemble hex audio without logging payload bytes.
- Set `ResultKind = music` and `Transport.IsStream` to the actual mode.

Official reference: `https://platform.minimax.io/docs/api-reference/music-generation`.
