# MiniMax China Mainland Imaging Transport

- `SchemaVersion: 2`
- `LastReviewedAt: 2026-07-14`
- Route: `image-generation@image-generation@v1`
- Selected model: `image-01` on the `build` profile only.

## Required Input

- `RequestKind = image-generation`
- `ConnectionProfileKey = build`
- `ApiSurface = image-generation`
- `ApiVersion = v1`
- `Model = image-01`
- `Inputs.Prompt`, length at most `1500` characters

## Verified Optional Mapping

| Shared/provider field | MiniMax field | Validation |
| --- | --- | --- |
| `Inputs.Seed` | `seed` | integer |
| `Inputs.ImageCount` | `n` | integer `1..9`; default is provider-defined `1` when omitted |
| `Inputs.ImageSize = WIDTHxHEIGHT` | `width`, `height` | both `512..2048`, both divisible by `8` |
| `ProviderOptions.aspect_ratio` | `aspect_ratio` | `1:1`, `16:9`, `4:3`, `3:2`, `2:3`, `3:4`, `9:16`, or `21:9` |
| `ProviderOptions.response_format` | `response_format` | `url` or `base64` |
| `ProviderOptions.prompt_optimizer` | `prompt_optimizer` | boolean |

Reject a request that sends both explicit width/height and `aspect_ratio`. The provider documents that `aspect_ratio` takes precedence; this transport rejects the ambiguous combination instead of silently ignoring the shared size.

`response_format` defaults to `url` when omitted. Returned URLs expire after 24 hours; do not treat them as durable storage.

## Unsupported or Unknown Boundary

- Streaming remains blocked unless the exact capability row becomes verified.
- Reference-image input is not enabled on this text-to-image surface. A separate image-to-image route requires its own URL, capability, pricing, and transport row.
- Do not invent image-size defaults in the shared envelope.

## Response Mapping

- `ResultKind = image-generation`
- returned URLs or base64 values -> `ImageOutputs`
- response `id` -> provider trace metadata
- success/failed counts -> `ProviderMeta`
- `Transport.IsStream = false`

Official reference: `https://platform.minimaxi.com/docs/api-reference/image-generation-t2i`.
