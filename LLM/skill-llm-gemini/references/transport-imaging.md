# Gemini Imaging Transport

Use this file for Gemini image generation or conversational image edit requests.

## Current Selected Surface

Use Gemini Developer API `models/{model}:generateContent` with Nano Banana image models.

Selected imaging rows:

- `gemini-3.1-flash-image-preview` for Nano Banana 2 Preview
- `gemini-3-pro-image-preview` for Nano Banana Pro Preview
- `gemini-2.5-flash-image` for Nano Banana

Do not wire Imagen rows through this skill until the catalog and capability matrix are expanded for that exact family.

## Input Shape

Build the shared request envelope with:

- `RequestKind = imaging`
- `ConnectionProfileKey = <profile key>` when the host uses multiple Gemini profiles
- `Model = <API Model>`
- `Inputs.Prompt = <text>`
- optional `Inputs.ReferenceImages = [...]`
- optional `Inputs.ImageSize`
- optional `ProviderOptions.AspectRatio`
- optional `ReasoningEffort` for verified Gemini 3 image rows
- optional `ReasoningSummary` for verified Gemini 3 image rows
- optional `TimeoutMs`

Before adding any optional field, verify that exact field in `capability-matrix.md`.

Resolve the connection profile before mapping request fields.

The selected profile must allow `imaging`, `generate-content`, and the selected model.

## Flow Rule

For selected Gemini imaging rows, non-stream `generateContent` requests can be treated as completed-response flows.

Use stage-based progress:

- `validating`
- `preparing`
- `sending`
- `waiting-first-byte`
- `downloading-result`
- `local-processing`
- `completed`

Do not fake percentages.

## Reference Image Rule

`Inputs.ReferenceImages` maps to additional Gemini content image parts only when `Supports Image Input = verified`.

For Gemini 3 image models, official docs verify up to 14 reference images, but the shared `Inputs.ImageCount` field means output count, not reference-image count.

If the caller asks for output image count and `Supports Image Count = unknown`, stop.

## Image Size Rule

For Gemini 3 image rows:

- map `Inputs.ImageSize` to `generationConfig.imageConfig.imageSize`
- map `ProviderOptions.AspectRatio` to `generationConfig.imageConfig.aspectRatio`

For `gemini-2.5-flash-image`:

- only `aspectRatio` is locally verified
- block `Inputs.ImageSize` unless a later sync verifies it for that model

## Thinking Rule

For `gemini-3.1-flash-image-preview`:

- thinking is always on
- `ReasoningEffort = minimal | high` maps to `thinkingConfig.thinkingLevel`
- `ReasoningSummary = true` maps to `thinkingConfig.includeThoughts = true`

For `gemini-3-pro-image-preview`, thinking is verified but controllable thinking levels are still `unknown`; block `ReasoningEffort` until synced.

For `gemini-2.5-flash-image`, thinking is unsupported.

## Fail-Fast Rule

Before implementation, confirm all of these:

- the model exists in `model-catalog.md`
- the capability row exists in `capability-matrix.md`
- `Supports Non-Stream = verified` for the base request path
- requested fields such as `Inputs.ReferenceImages`, `Inputs.ImageSize`, `Inputs.ImageCount`, and `ReasoningEffort` are verified

If any of those are missing, stop.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = imaging`
- `ImageOutputs = generated image result list from inlineData or file data`
- `TextContent = any returned text explanation when present`
- `ReasoningSummary = thought summary parts when requested and returned`
- `ReasoningItems = thought signatures or other continuation metadata when returned`
- `Usage = normalized text, image input, image output, and thinking token usage when available`
- `Transport.IsStream = false`

## UI Rule

If the caller wants UI:

- show prompt, model, connection profile, elapsed time, retry count, and failure state
- show image reference controls only for models with verified image input
- show image size controls only for verified image-size rows
- show output image count only when `Supports Image Count = verified`
- show thought-summary controls only when verified
- show final thumbnails only after the provider returns final inline image data or files
