# OpenAI Imaging Transport

Use this file for image generation or image edit requests.

## Current Selected Surface

Use the Image API with `gpt-image-2` for the bundled selected imaging path.

OpenAI also exposes image generation through a Responses hosted tool, but this skill does not currently model that hosted-tool path as a selected local imaging row.

Do not wire `gpt-5.5` plus the Responses image-generation hosted tool as `RequestKind = imaging` unless the catalog and capability matrix are expanded for that exact path.

## Input Shape

Build the shared request envelope with:

- `RequestKind = imaging`
- `ConnectionProfileKey = <profile key>` when the host uses multiple OpenAI profiles
- `Model = <API Model>`
- `Inputs.Prompt = <text>`
- optional `Inputs.ReferenceImages = [...]`
- optional `Inputs.ImageSize`
- optional `Inputs.ImageCount`
- optional `TimeoutMs`
- optional `IsStream`
- optional `ProviderOptions.Surface = image-api`

Before adding any optional field, verify that exact field in `references/capability-matrix.md`.

Resolve the connection profile before mapping request fields.

The selected profile must allow `imaging`, `image-api`, and the selected model.

## Flow Rule

For `gpt-image-2`, non-stream Image API requests can be treated as completed-response flows.

For stream requests, use stage-based progress and partial-image events. Do not fake percentages.

Recommended stage pattern:

- `validating`
- `preparing`
- `sending`
- `waiting-first-byte`
- `streaming`
- `downloading-result`
- `local-processing`
- `completed`

## Fail-Fast Rule

Before implementation, confirm all of these:

- the model exists in `references/model-catalog.md`
- the capability row exists in `references/capability-matrix.md`
- `Supports Non-Stream = verified` for the base request path
- `Supports Stream = verified` before using partial-image streaming
- requested fields such as `Inputs.ReferenceImages`, `Inputs.ImageSize`, and `Inputs.ImageCount` are verified

If any of those are missing, stop.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = imaging`
- `ImageOutputs = generated image result list`
- `Usage = normalized text, image input, and image output token usage when available`
- `Transport.IsStream = true or false`

## UI Rule

If the caller wants UI:

- use stage-based progress instead of fake percentage
- show prompt, model, surface, stream state, elapsed time, retry count, and failure state
- show partial images only when stream events return stable partial image data
- show final thumbnails only after the provider returns final base64, URLs, or binary content
