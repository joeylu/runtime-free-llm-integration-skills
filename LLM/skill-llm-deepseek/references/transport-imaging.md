# DeepSeek Imaging Transport

Use this file for image generation or image edit requests.

## Current State

This skill does not bundle documented DeepSeek imaging rows yet.

Do not invent imaging model names or route chat rows into image generation.

## Input Shape

Build the shared request envelope with:

- `RequestKind = imaging`
- `ConnectionProfileKey = <profile key>` when the host uses multiple DeepSeek profiles
- `Model = <API Model>`
- `Inputs.Prompt = <text>`
- optional `Inputs.ReferenceImages = [...]`
- optional `Inputs.Seed`
- optional `Inputs.ImageSize`
- optional `Inputs.ImageCount`
- optional `TimeoutMs`

## Fail-Fast Rule

Before implementation, confirm all of these:

- the model exists in `model-catalog.md` as an `imaging` row
- the capability row exists in `capability-matrix.md`
- requested fields such as `Inputs.ReferenceImages`, `Inputs.Seed`, `Inputs.ImageSize`, and `Inputs.ImageCount` are verified

If any of those are missing, stop.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = imaging`
- `ImageOutputs = generated image result list`
- `Usage = normalized usage when available`
- `Transport.IsStream = false` unless verified otherwise
