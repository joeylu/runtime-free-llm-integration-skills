# Aliyun Music Transport

Use this file for music or audio generation requests.

## Current State

This skill defines the contract and flow for music, but no concrete Aliyun music model rows are bundled yet.

Do not invent music model names or unsupported parameters.

## Input Shape

Build the shared request envelope with:

- `RequestKind = music-generation`
- optional `ConnectionProfileKey`
- `ApiSurface = dashscope-native`
- `Model = <API Model>`
- `Inputs.Prompt = <text>`
- optional `Inputs.Lyrics = <text>`
- optional `Inputs.DurationSeconds`
- optional `Inputs.Seed`
- optional `TimeoutMs`

Resolve `ResolvedRequestUrl` from `request-urls.md` before sending.

## Default Flow

Treat music as a job-style flow unless the capability matrix later verifies a true stream path.

Recommended stage pattern:

- `validating`
- `preparing`
- `submitting-job`
- `waiting-provider-accept`
- `polling-job`
- `downloading-result`
- `local-processing`
- `completed`

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
- `Transport.IsStream = false` unless verified otherwise

## UI Rule

If the caller wants UI:

- use stage-based progress instead of fake percentage
- show prompt, model, job state, elapsed time, retry count, and failure state
- expose audio preview only after the provider returns stable result URLs or binary content
