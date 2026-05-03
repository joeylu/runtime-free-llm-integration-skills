# MiniMax International Imaging Transport

Use this file for build-profile MiniMax International text-to-image requests.

## Current State

This skill selects `image-01` for build-profile HTTP image generation.

`ConnectionProfileKey = plan` must block `RequestKind = imaging`. Do not route plan-profile image work to CLI, MCP, chat, or any hidden fallback in this skill.

## Input Shape

Build the shared request envelope with:

- `RequestKind = imaging`
- `ConnectionProfileKey = build` when MiniMax profiles are used
- `ApiSurface = image-generation`
- `Model = image-01`
- `Inputs.Prompt = <text>`
- optional `Inputs.Seed` only because the capability matrix marks seed verified
- optional `Inputs.ImageCount` only because the capability matrix marks `n` verified
- optional `ProviderOptions.aspect_ratio`
- optional `ProviderOptions.response_format`
- optional `ProviderOptions.prompt_optimizer`
- optional `TimeoutMs`

Do not use `Inputs.ImageSize` for MiniMax `aspect_ratio`. `Inputs.ImageSize` means an explicit shared image-size field; `aspect_ratio` is a provider option such as `16:9`.

Before adding `Inputs.ReferenceImages`, `Inputs.ImageSize`, or streaming, check `capability-matrix.md`. Current selected rows do not verify those options.

Resolve `ResolvedRequestUrl` from `request-urls.md` before sending.

## Request Mapping

Map the provider request body as:

| Shared Field | MiniMax Field |
| --- | --- |
| `Model` | `model` |
| `Inputs.Prompt` | `prompt` |
| `Inputs.Seed` | `seed` |
| `Inputs.ImageCount` | `n` |
| `ProviderOptions.aspect_ratio` | `aspect_ratio` |
| `ProviderOptions.response_format` | `response_format` |
| `ProviderOptions.prompt_optimizer` | `prompt_optimizer` |

Do not invent defaults for provider options. If the host wants a fixed aspect ratio, response format, or prompt optimizer value, make that config explicit.

## Default Flow

Treat imaging as direct non-stream HTTP unless a later sync verifies streaming.

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

- the selected profile allows `imaging`
- the selected model is `image-01`
- `request-urls.md` has a verified `image-generation` row
- `Supports Non-Stream = verified`
- every requested optional field is `verified` or is an explicitly supplied provider option documented above

If any requirement is missing, stop.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = imaging`
- `ImageOutputs = generated image result list`
- `Usage = normalized usage when available`
- `Transport.IsStream = false`

## UI Rule

If the caller wants UI:

- disable MiniMax imaging for plan profile
- show only `image-01` unless a sync selects more imaging rows
- expose provider options as advanced controls, not shared fields
- show result thumbnails only after the provider returns stable result URLs or binary content
