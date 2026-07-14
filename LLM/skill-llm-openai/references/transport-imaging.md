# OpenAI Imaging Transport

Use this file for direct `gpt-image-2` Image API generation and edits.

## Path Separation

- `image-api-generations` -> `POST /images/generations`
- `image-api-edits` -> `POST /images/edits`
- The Responses `image_generation` hosted tool is not a direct imaging model call. It uses a GPT-5.6 main model and is governed by `hosted-tools.md`.
- Never submit `gpt-image-2` as the main `model` of a Responses request.

## Shared Input

Generation:

- `RequestKind = imaging`
- `Model = gpt-image-2`
- `ApiSurface = image-api-generations`
- `Inputs.Prompt`

Edit:

- same base fields
- `ApiSurface = image-api-edits`
- one or more `Inputs.ReferenceImages`
- optional mask under a typed provider option

Optional verified mappings:

- `Inputs.ImageSize` -> `size`; `auto` is allowed and is the provider default, otherwise validate the explicit dimensions below
- `Inputs.ImageCount` -> `n`, range `1..10`
- `IsStream` -> `stream`
- provider option `PartialImages` -> `partial_images`, range `0..3`, only with stream
- provider option `Quality` -> `quality`, one of `auto`, `low`, `medium`, `high`
- provider option `OutputFormat` -> `output_format`, one of `png`, `jpeg`, `webp`
- provider option `OutputCompression` -> `output_compression`, range `0..100`, only for JPEG/WebP
- provider option `Background` -> `background`, one of `auto` or `opaque`; for `gpt-image-2`, reject `transparent`
- provider option `Moderation` -> `moderation`, verified values `auto` or `low`

`Inputs.Seed` is unverified and must fail fast.

## Output Size Rules

For both generation and edits, `size = "auto"` is the default and bypasses caller-side dimension parsing. Every explicit standard or arbitrary `WIDTHxHEIGHT` value must satisfy all documented constraints:

- each edge is a multiple of `16px`;
- maximum edge length is `3840px`;
- long-edge to short-edge ratio is at most `3:1`;
- total pixels are between `655,360` and `8,294,400`;
- outputs above `3,686,400` total pixels are experimental.

Do not validate only the string shape. Apply every published constraint and preserve provider errors for limits that remain provider-defined.

## Edit Rules

- One or more reference images are required; GPT Image edits accept up to `16` input images, each in a supported image format and within the documented size limit.
- A mask must match the edited image format and dimensions, be below `50MB`, and include an alpha channel.
- `gpt-image-2` always handles image inputs at high fidelity. Omit `input_fidelity`; reject caller attempts to set it.
- Transparent backgrounds are unsupported for `gpt-image-2`.
- Accept multipart file uploads or the documented JSON image reference form only when the host implementation verifies the resolved transport encoding.

## Streaming

Both generation and edit surfaces support SSE partial-image streaming.

- `partial_images` is `0..3`.
- Generation event types include `image_generation.partial_image` and the final completed event.
- Edit event types include `image_edit.partial_image` and `image_edit.completed`.
- Partial events carry base64 image data and an index/metadata according to the event schema.
- Each partial image adds `100` image-output tokens; do not present streaming previews as free.
- Do not treat a partial preview as the final artifact.

Recommended progress stages:

`validating -> preparing -> uploading -> sending -> waiting-first-event -> streaming -> decoding-final -> completed`

Never fabricate percentages.

## Output

GPT Image models return base64-encoded image data on the Image API; URL response mode is not supported for these models.

Normalize:

- final base64/binary results -> `ImageOutputs`
- partial previews -> stream progress events, not final outputs
- text/image input and image output token details -> `Usage`
- actual size, quality, background, and output format -> `ProviderMeta`

Organization verification may be required before GPT Image access. Treat that as a configuration/access error, not evidence that the model capability is unsupported.

Sources: `https://developers.openai.com/api/docs/models/gpt-image-2`, `https://developers.openai.com/api/docs/guides/image-generation`, `https://developers.openai.com/api/reference/resources/images/methods/generate`, `https://developers.openai.com/api/reference/resources/images/methods/edit`, `https://developers.openai.com/api/reference/resources/images/edit-streaming-events`.
