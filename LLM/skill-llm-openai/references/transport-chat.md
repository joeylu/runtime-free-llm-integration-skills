# OpenAI Chat Transport

Use this file for text-first direct-model chat requests.

## Preferred Surface

Use the Responses API by default.

Use Chat Completions only when the host project explicitly requires Chat Completions compatibility and every requested option is verified for that surface.

## Input Shape

Build the shared request envelope with:

- `RequestKind = chat`
- `ConnectionProfileKey = <profile key>` when the host uses multiple OpenAI profiles
- `Model = <API Model>`
- `Inputs.Messages = [...]`
- optional `IsStream`
- optional `ReasoningEffort`
- optional `ReasoningSummary`
- optional `Temperature`
- optional `ResponseFormat`
- optional `Tools`
- optional `ToolChoice`

## Reasoning Rule

Resolve the connection profile before mapping request fields.

The selected profile must allow the requested API surface and model.

Map `ReasoningEffort` to OpenAI `reasoning.effort`.

Use this effective thinking mapping:

- `none` means `ThinkingApplied = false`
- `low`, `medium`, `high`, and `xhigh` mean `ThinkingApplied = true`

If the caller supplies both `ThinkingRequested` and `ReasoningEffort`, they must agree.

If `Reasoning Effort Field = unknown`, do not synthesize an OpenAI reasoning request from `ThinkingRequested`.

If `ReasoningEffort` is omitted and the capability row has `Thinking Default = unknown`, do not use thinking-dependent gating unless the caller chooses a verified explicit reasoning value.

Do not expose raw `ThinkingContent` unless official docs verify raw reasoning text for the selected model and response shape. For current selected OpenAI chat rows, map reasoning summaries to `ReasoningSummary`.

## Structured Output Rule

For Responses API:

- `ResponseFormat = json_schema` maps to `text.format.type = json_schema`
- `ResponseFormat = json_object` maps to `text.format.type = json_object`

Prefer `json_schema` when the caller provides a schema.

If the caller uses `json_object`, require explicit JSON instructions in the prompt or system/developer message because OpenAI JSON mode requires that context.

## Tool Rule

Caller-defined tools map to OpenAI `function` tools.

Do not treat OpenAI-hosted tools such as web search, file search, code interpreter, computer use, MCP, or image generation as caller-defined tools.

Strict tool schemas require `Strict Tool Schema Mode = verified`.

Parallel tool calls require `Parallel Tool Calls = verified`.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = chat`
- `TextContent = final output text when available`
- `StructuredContent = parsed schema output when requested and validated`
- `ToolCalls = function_call output items`
- `ReasoningSummary = provider reasoning summary when returned`
- `ReasoningItems = encrypted or provider-specific reasoning items when returned`
- `Usage = normalized token usage including cached and reasoning tokens when available`
- `FinishReason = normalized provider finish reason or status`
- `Transport.IsStream = true or false`

## UI Rule

If the caller wants UI:

- show the model selector
- show stream toggle only for verified stream paths
- show reasoning effort selector with official values
- show reasoning summary selector only when verified
- show schema editor for verified `json_schema`
- show tool editor for verified caller-defined tools
- hide or disable unknown options with explicit reasons
