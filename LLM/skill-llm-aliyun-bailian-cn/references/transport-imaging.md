# Aliyun Imaging Transport

Use this file for image generation or image edit requests.

## Current State

This China Mainland skill bundles selected Aliyun imaging rows in `model-catalog.md` and base imaging capability rows in `capability-matrix.md`.

A catalog row only proves that the model is a local selectable model. It does not prove support for edit/reference images, seed, size, count, prompt rewriting, or streaming.

Do not invent imaging model names or unsupported parameters.

## Input Shape

Build the shared request envelope with:

- `RequestKind = imaging`
- optional `ConnectionProfileKey`
- `ApiSurface = dashscope-native-sync` for synchronous image generation/edit paths
- `ApiSurface = dashscope-native-async` only when `request-urls.md` verifies an asynchronous job path for the selected model
- `Model = <API Model>`
- `Inputs.Prompt = <text>`
- optional `Inputs.ReferenceImages = [...]`
- optional `Inputs.Seed`
- optional `Inputs.ImageSize`
- optional `Inputs.ImageCount`
- optional `TimeoutMs`

Before adding any optional field, verify that exact field in `capability-matrix.md`. For example, `Inputs.ReferenceImages` requires verified imaging image-input support, not just a model note that says the family can edit images.

Resolve `ResolvedRequestUrl` from `request-urls.md` before sending.

## Default Flow

Treat imaging as a job-style flow unless the capability matrix later verifies a true stream path.

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
- `Supports Non-Stream = verified` for the base job request path
- requested fields such as `Inputs.ReferenceImages`, `Inputs.Seed`, `Inputs.ImageSize`, and `Inputs.ImageCount` are verified

If any of those are missing, stop.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = imaging`
- `ImageOutputs = generated image result list`
- `Usage = normalized usage when available`
- `Transport.IsStream = false` unless verified otherwise

## UI Rule

If the caller wants UI:

- use stage-based progress instead of fake percentage
- show prompt, model, job state, elapsed time, retry count, and failure state
- show result thumbnails only after the provider returns stable result URLs or binary content
