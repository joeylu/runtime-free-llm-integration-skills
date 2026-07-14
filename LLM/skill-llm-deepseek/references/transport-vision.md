# DeepSeek Vision Transport

Use this file for image-understanding requests.

## Current State

This skill does not bundle documented DeepSeek vision rows yet.

Do not route image input through rows listed only under `chat`.

## Input Shape

Build the shared request envelope with:

- `RequestKind = vision`
- `ConnectionProfileKey = <profile key>` when the host uses multiple DeepSeek profiles
- `Model = <API Model>`
- `Inputs.Messages = [...]`
- `Inputs.Images = [...]`

## Fail-Fast Rule

Before implementation, confirm all of these:

- the model exists in `model-catalog.md` as a `vision` row
- the capability row exists in `capability-matrix.md`
- `Supports Image Input = verified`

If any of those are missing, stop.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = vision`
- `TextContent = final understanding output`
- `Usage = normalized usage`
