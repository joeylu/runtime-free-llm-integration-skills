# Aliyun Bailian China Mainland Vision Transport

Use this file for image-understanding requests with a model resolved from the `vision` catalog.

## Surface Choice

`qwen3.7-plus` has two verified image-understanding surfaces:

- `responses`: image-only vision through `input_image`, with Responses reasoning, continuation, tools, and streaming semantics
- `chat-completions`: compatibility path for image and video inputs, manual history, `thinking_budget`, `preserve_thinking`, and the verified non-thinking `json_object` mode

Do not silently switch surfaces. Resolve:

`RequestKind = vision + qwen3.7-plus + ApiSurface`

## Shared Input Shape

Build:

- `RequestKind = vision`
- optional `ConnectionProfileKey`
- `ApiSurface = responses | chat-completions`
- `Model = qwen3.7-plus`
- `Inputs.Messages = [...]`
- `Inputs.Images = [...]`
- optional `IsStream`
- only fields verified by the exact surface row

Resolve `ResolvedRequestUrl` before sending.

## Responses Mapping

Reuse every `responses` rule in `transport-chat.md`, including reasoning effort, functions, hosted tools, continuation, storage, Session Cache, stream events, unsupported fields, and response mapping.

Map each image to a user content item with `type = input_image` and a valid public `image_url` accepted by the provider.

Constraints:

- at least one image is required for `RequestKind = vision`
- Responses does not accept video or audio input
- do not map `Inputs.Images` to `input_file`; the current API reference limits `input_file` to `qwen3.5-ocr`, which is not this row
- do not send a vision request through a chat-only capability row
- do not infer image limits from the Chat Completions vision table; apply only limits documented for the resolved Responses payload

Return final text in `TextContent`, reasoning summaries in `ReasoningSummary`, and hosted tool records in `HostedToolCalls`. Do not populate raw `ThinkingContent` from Responses summaries.

## Chat Completions Mapping

Reuse the `chat-completions` rules in `transport-chat.md`.

Map text and media into the provider's documented multimodal message content format. The documented model documentation supports image and video understanding on this surface.

For the resolved row:

- thinking defaults on
- `ThinkingBudget` and `preserve_thinking` are available when mapped exactly
- temperature is allowed in both thinking modes with the documented mode-specific defaults
- `json_object` is non-thinking-only
- `json_schema` and caller-defined function mode compatibility remain blocked while unverified

Never disable thinking automatically to satisfy `json_object`.

Map raw `reasoning_content` to `ThinkingContent` only when returned by Chat Completions.

## UI Rule

- filter the model selector to documented `vision` rows
- display a surface selector for `qwen3.7-plus`
- on Responses, accept images only and hide video/audio attachment controls
- on Chat Completions, expose only documented image/video inputs
- show surface-specific reasoning, cache, continuation, tool, and response-format controls
- clear or reject incompatible values when the surface changes

## Official Sources

- `https://help.aliyun.com/zh/model-studio/qwen-api-via-openai-responses`
- `https://help.aliyun.com/zh/model-studio/vision`
- `https://help.aliyun.com/zh/model-studio/qwen-api-via-openai-chat-completions`
