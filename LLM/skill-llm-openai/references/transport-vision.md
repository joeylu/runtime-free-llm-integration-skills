# OpenAI Vision Transport

Use this file for text-plus-image understanding with the selected GPT-5.6 models.

## Surface Choice

Prefer Responses. Chat Completions is available only as the compatibility surface defined in `capability-matrix.md`.

## Shared Input

- `RequestKind = multimodal-chat`
- `ConnectionProfileKey`
- `Model`
- `ApiSurface`
- `Inputs.Messages`
- one or more `Inputs.Images`

Do not route image-bearing input through `RequestKind = text-chat`.

## Responses Image Mapping

Map each image to an `input_image` content block using exactly one verified source:

- `image_url` with a fully qualified URL;
- `image_url` with a base64 data URL;
- `file_id`.

Map provider option `ImageDetail` to `detail` with one of:

- `low`
- `high`
- `original`
- `auto`

Omission defaults to `auto`. For GPT-5.6, `auto` and omitted detail use the same sizing behavior as `original`: original dimensions are preserved rather than resized to a patch or pixel-dimension budget. Large images can therefore consume more tokens and increase latency. Resize before sending or select `low`/`high` when cost and latency need a tighter bound.

For caching, the image bytes/reference and `detail` value are part of the reusable prefix. Keep them identical for expected cache hits.

## Chat Completions Image Mapping

Use the documented image content form in `messages`. Preserve the same detail semantics, but do not send Responses-only reasoning, state, summary, verbosity, or hosted-tool fields.

## Unsupported Modalities

The selected GPT-5.6 rows support text and image input and text output. Audio and video input are not supported by these model rows. Do not reinterpret them as image attachments.

## Reasoning, State, Cache, Structured Output, and Tools

Apply `transport-chat.md` after the image blocks are mapped. Never drop images to make another option fit, and never move the request to a different surface silently.

## Response Mapping

Use `ResultKind = vision` and normalize text, structured content, caller tools, hosted tools, reasoning summaries/items, annotations, continuation state, and usage exactly as in `transport-chat.md`.

Source: `https://developers.openai.com/api/docs/guides/images-vision`, `https://developers.openai.com/api/reference/resources/responses/methods/create`, `https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create`, and the three selected model pages.
