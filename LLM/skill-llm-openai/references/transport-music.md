# OpenAI Music Transport

Use this file for music or audio generation requests.

## Current State

This skill does not bundle selected OpenAI music rows yet.

Do not invent music model names or route text-to-speech, transcription, or realtime voice through `RequestKind = music` unless the shared request-kind contract is explicitly expanded.

## Input Shape

Build the shared request envelope with:

- `RequestKind = music`
- `Model = <API Model>`
- `Inputs.Prompt = <text>`
- optional `Inputs.Lyrics = <text>`
- optional `Inputs.DurationSeconds`
- optional `Inputs.Seed`
- optional `TimeoutMs`

## Fail-Fast Rule

Before implementation, confirm all of these:

- the model exists in `references/model-catalog.md`
- the capability row exists in `references/capability-matrix.md`
- requested fields such as `Inputs.DurationSeconds` and `Inputs.Seed` are verified

If any of those are missing, stop.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = music`
- `AudioOutputs = generated audio result list`
- `Usage = normalized usage when available`
