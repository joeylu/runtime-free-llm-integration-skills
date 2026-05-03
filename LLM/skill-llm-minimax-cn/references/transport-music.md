# MiniMax China Mainland Music Transport

Use this file for build-profile MiniMax China Mainland music generation requests.

## Current State

This skill selects `music-2.6` for build-profile HTTP Music Generation.

`ConnectionProfileKey = plan` must block `RequestKind = music`. Do not route plan-profile music work to CLI, MCP, chat, or any hidden fallback in this skill.

## Input Shape

Build the shared request envelope with:

- `RequestKind = music`
- `ConnectionProfileKey = build` when MiniMax profiles are used
- `ApiSurface = music-generation`
- `Model = music-2.6`
- `Inputs.Prompt = <style or music prompt>`
- `Inputs.Lyrics = <lyrics text>`
- `ProviderOptions.audio_setting = <explicit MiniMax audio setting object>`
- optional `TimeoutMs`

MiniMax music generation is documented as generating a song from lyrics and a prompt. Treat `Inputs.Lyrics` as required for `music-2.6`.

Do not invent `audio_setting` defaults. This local transport requires the host or owner to provide exact `sample_rate`, `bitrate`, and `format` values in `ProviderOptions.audio_setting`, or to sync the docs and record verified provider defaults first.

Before adding `Inputs.DurationSeconds`, `Inputs.Seed`, or streaming, check `capability-matrix.md`. Current selected rows do not verify those options.

Resolve `ResolvedRequestUrl` from `request-urls.md` before sending.

## Request Mapping

Map the provider request body as:

| Shared Field | MiniMax Field |
| --- | --- |
| `Model` | `model` |
| `Inputs.Prompt` | `prompt` |
| `Inputs.Lyrics` | `lyrics` |
| `ProviderOptions.audio_setting` | `audio_setting` |

## Default Flow

Treat music as direct non-stream HTTP unless a later sync verifies streaming.

Recommended stage pattern:

- `validating`
- `preparing`
- `submitting-request`
- `waiting-provider`
- `downloading-result`
- `local-processing`
- `completed`

## Fail-Fast Rule

Before implementation, confirm all of these:

- the selected profile allows `music`
- the selected model is `music-2.6`
- `Inputs.Prompt` and `Inputs.Lyrics` are present
- `ProviderOptions.audio_setting` is explicit
- `request-urls.md` has a verified `music-generation` row
- `Supports Non-Stream = verified`
- requested fields such as `Inputs.DurationSeconds`, `Inputs.Seed`, and stream are verified

If any requirement is missing, stop.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = music`
- `AudioOutputs = generated audio result list`
- `Usage = normalized usage when available`
- `Transport.IsStream = false`

## UI Rule

If the caller wants UI:

- disable MiniMax music for plan profile
- show only `music-2.6` unless a sync selects more music rows
- collect prompt and lyrics separately
- expose provider audio settings as explicit advanced controls
- expose audio preview only after the provider returns stable result URLs or binary content
