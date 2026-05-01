# Gemini Chat Transport

Use this file for text-first Gemini chat requests.

## Preferred Surface

Use Gemini Developer API `models/{model}:generateContent` for non-stream chat.

Use `models/{model}:streamGenerateContent?alt=sse` only when `Supports Stream = verified`.

## Input Shape

Build the shared request envelope with:

- `RequestKind = chat`
- `ConnectionProfileKey = <profile key>` when the host uses multiple Gemini profiles
- `Model = <API Model>`
- `Inputs.Messages = [...]`
- optional `IsStream`
- optional `ReasoningEffort`
- optional `ReasoningSummary`
- optional `Temperature`
- optional `ResponseFormat`
- optional `Tools`
- optional `ToolChoice`

Resolve the connection profile before mapping request fields.

The selected profile must allow the requested API surface and model.

## Thinking Rule

For selected Gemini 3 chat rows:

- Allowed `ReasoningEffort` values come from the selected row's `Reasoning Effort Values` in `capability-matrix.md`.
- Map each allowed `ReasoningEffort` value to `generationConfig.thinkingConfig.thinkingLevel`.
- `ReasoningSummary = true` maps to `generationConfig.thinkingConfig.includeThoughts = true`
- `ThinkingRequested = false` is invalid because the selected Gemini 3 rows cannot fully disable thinking

Example:
`gemini-3-flash-preview` allows `minimal,low,medium,high`, while `gemini-3.1-pro-preview` allows only `low,medium,high`.

Do not use `thinkingBudget` for selected Gemini 3 rows; the local matrix marks it unsupported.

Do not expose raw chain-of-thought. Return thought summaries only when requested and verified.

Preserve returned thought signatures as `ReasoningItems` or `ProviderMeta` for follow-up turns. Do not render thought signatures as user-visible reasoning.

## Structured Output Rule

`ResponseFormat = json_schema` maps to:

```json
{
  "generationConfig": {
    "responseMimeType": "application/json",
    "responseJsonSchema": {}
  }
}
```

Bare `ResponseFormat = json_object` is blocked while `Json Object Mode = unknown`.

Do not send OpenAI-compatible `response_format`.

## Tool Rule

Caller-defined tools map to Gemini `functionDeclarations`.

Use Gemini `toolConfig.functionCallingConfig` for tool choice:

- `AUTO` when the model may either answer or call a function
- `ANY` when the caller requires a function call
- `NONE` when the caller wants to disable supplied function declarations
- `VALIDATED` when structured outputs or hosted tools are combined with function declarations

Parallel function calling is verified for selected chat rows.

Strict schema adherence maps to Gemini function calling modes that ensure schema adherence; do not add OpenAI-style `strict: true`.

## Streaming Rule

For stream requests:

- use the `streamGenerateContent` API surface
- emit stage-based progress only
- aggregate text chunks into `TextContent`
- aggregate thought-summary chunks only if `ReasoningSummary = true`

Do not fake percentages.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = chat`
- `TextContent = final output text when available`
- `ReasoningSummary = thought summary parts when requested and returned`
- `ReasoningItems = thought signatures or other continuation metadata when returned`
- `ToolCalls = functionCall parts`
- `Usage = normalized prompt, output, and thinking token usage when available`
- `FinishReason = normalized provider finish reason`
- `Transport.IsStream = true or false`

## UI Rule

If the caller wants UI:

- show the model selector
- show stream toggle only for verified stream paths
- show thinking level selector only for the selected row's verified `ReasoningEffort` values
- show thought-summary toggle only when `Reasoning Summary Field = verified`
- show JSON schema output control only when compatible with the selected row
- show tool editor for verified caller-defined tools
- hide or disable unknown options with explicit reasons
