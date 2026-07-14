# DeepSeek Music Transport

Use this file for music or audio generation requests.

## Current State

This skill does not bundle documented DeepSeek music rows yet.

Do not invent music model names.

## Input Shape

Build the shared request envelope with:

- `RequestKind = music`
- `ConnectionProfileKey = <profile key>` when the host uses multiple DeepSeek profiles
- `Model = <API Model>`
- `Inputs.Prompt = <text>`
- optional `Inputs.Lyrics = <text>`
- optional `Inputs.DurationSeconds`
- optional `Inputs.Seed`
- optional `TimeoutMs`

## Fail-Fast Rule

Before implementation, confirm all of these:

- the model exists in `model-catalog.md`
- the capability row exists in `capability-matrix.md`
- requested fields such as `Inputs.DurationSeconds` and `Inputs.Seed` are verified

If any of those are missing, stop.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = music`
- `AudioOutputs = generated audio result list`
- `Usage = normalized usage when available`
