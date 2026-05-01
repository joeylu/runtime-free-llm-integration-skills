# Gemini Vision Transport

Use this file for Gemini image-understanding requests.

## Preferred Surface

Use Gemini Developer API `models/{model}:generateContent` for non-stream vision.

Use `models/{model}:streamGenerateContent?alt=sse` only when `Supports Stream = verified`.

## Input Shape

Build the shared request envelope with:

- `RequestKind = vision`
- `ConnectionProfileKey = <profile key>` when the host uses multiple Gemini profiles
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

Resolve the connection profile before mapping request fields.

The selected profile must allow `vision`, the requested API surface, and the selected model.

## Image Input Rule

Map each image to a Gemini content part using one verified provider-supported input method:

- inline image data
- Files API file reference
- URL or blob only if the host SDK and provider docs verify it for that language/runtime

Do not move image inputs into prompt text.

If the caller requests multiple input images and the provider limit matters, verify that limit from Gemini docs or stop and ask for sync. Do not use `Supports Image Count` for vision input images.

## Thinking Rule

Use the same Gemini 3 thinking rules as `transport-chat.md`.

Do not disable thinking for selected Gemini 3 vision rows.

Do not expose raw chain-of-thought.

Preserve returned thought signatures as `ReasoningItems` or `ProviderMeta` for follow-up turns. Do not render thought signatures as user-visible reasoning.

## Structured Output Rule

Use the same JSON schema mapping as `transport-chat.md`.

Bare `ResponseFormat = json_object` is blocked while `Json Object Mode = unknown`.

## Tool Rule

Caller-defined tools map to Gemini `functionDeclarations`.

Use Gemini tool-choice modes only after verifying the selected model row supports tools.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = vision`
- `TextContent = final output text when available`
- `ReasoningSummary = thought summary parts when requested and returned`
- `ReasoningItems = thought signatures or other continuation metadata when returned`
- `ToolCalls = functionCall parts`
- `Usage = normalized prompt, output, image-input, and thinking token usage when available`
- `FinishReason = normalized provider finish reason`
- `Transport.IsStream = true or false`

## UI Rule

If the caller wants UI:

- show image upload/input controls only for `RequestKind = vision`
- show model selector and connection profile selector
- show stream toggle only for verified stream paths
- show thinking level and thought-summary controls only when verified
- show structured-output and tool controls only when verified
- keep unsupported imaging controls hidden; image generation belongs to `RequestKind = imaging`
