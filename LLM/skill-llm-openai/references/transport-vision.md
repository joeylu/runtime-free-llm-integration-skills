# OpenAI Vision Transport

Use this file for image-understanding requests.

## Preferred Surface

Use the Responses API by default.

Only models listed under the `vision` catalog may be used for image-understanding requests.

## Input Shape

Build the shared request envelope with:

- `RequestKind = vision`
- `ConnectionProfileKey = <profile key>` when the host uses multiple OpenAI profiles
- `Model = <API Model>`
- `Inputs.Messages = [...]`
- `Inputs.Images = [...]`
- optional `IsStream`
- optional `ReasoningEffort`
- optional `ReasoningSummary`
- optional `Temperature`
- optional `ResponseFormat`
- optional `Tools`
- optional `ToolChoice`

Example:
One vision request can include a user text message plus one or more image items.

## Image Rule

Resolve the connection profile before mapping request fields.

The selected profile must allow `vision`, the requested API surface, and the selected model.

Map `Inputs.Images` to OpenAI image input content items.

Do not route image input through rows listed only under `chat`.

If image-detail behavior matters, use provider-specific fields under `ProviderOptions` and verify them against official docs before implementation.

## Reasoning and Structured Output Rules

Use the same reasoning, structured output, and tool rules as `transport-chat.md`.

Do not silently drop images when a requested structured output or tool path is also enabled.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = vision`
- `TextContent = final understanding output`
- `StructuredContent = parsed schema output when requested and validated`
- `ToolCalls = function_call output items`
- `ReasoningSummary = provider reasoning summary when returned`
- `Usage = normalized token usage`
- `Transport.IsStream = true or false`

## UI Rule

If the caller wants UI:

- show image picker or image attachment surface
- show model selector filtered to `vision`
- show reasoning effort and structured-output controls only when compatible with the selected row
- hide controls that are not verified by the capability matrix
