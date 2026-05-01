# DeepSeek Chat Transport

Use this file for text-first DeepSeek chat requests.

## Preferred Surface

Use DeepSeek's OpenAI-compatible Chat Completions API by default.

Use the beta surface only when the requested feature requires it and the selected connection profile allows it.

## Input Shape

Build the shared request envelope with:

- `RequestKind = chat`
- `ConnectionProfileKey = <profile key>` when the host uses multiple DeepSeek profiles
- `Model = <API Model>`
- `Inputs.Messages = [...]`
- optional `IsStream`
- optional `ThinkingRequested`
- optional `ReasoningEffort`
- optional `Temperature`
- optional `ResponseFormat`
- optional `Tools`
- optional `ToolChoice`

## Thinking Rule

Resolve the connection profile before mapping request fields.

The selected profile must allow the requested API surface and model.

Map thinking controls like this:

- `ThinkingRequested = true` -> `thinking.type = enabled`
- `ThinkingRequested = false` -> `thinking.type = disabled`
- `ReasoningEffort = none` -> `thinking.type = disabled`
- `ReasoningEffort = high` -> `thinking.type = enabled` and `reasoning_effort = high`
- `ReasoningEffort = max` -> `thinking.type = enabled` and `reasoning_effort = max`
- `ReasoningEffort = low` or `medium` -> `thinking.type = enabled` and `reasoning_effort = high`
- `ReasoningEffort = xhigh` -> `thinking.type = enabled` and `reasoning_effort = max`

Do not use OpenAI Responses-style `reasoning.effort`.

Do not accept or pass `ThinkingBudget` for the selected DeepSeek V4 rows. The capability matrix marks `Thinking Budget Field = unsupported`; use `ReasoningEffort` instead.

If the caller sends both `ThinkingRequested` and `ReasoningEffort`, they must agree.

Preserve prior assistant `reasoning_content` when that assistant message included tool calls; official DeepSeek docs say omitting it in follow-up requests can return a 400 error.

When the prior assistant message did not include tool calls, `reasoning_content` may be omitted because DeepSeek says it will be ignored if passed.

## Temperature Rule

Pass `Temperature` only when effective thinking is false.

Official thinking-mode docs say thinking mode does not support temperature and related sampling parameters.

## Structured Output Rule

`ResponseFormat = json_object` maps to:

```json
{"response_format":{"type":"json_object"}}
```

Do not claim `json_schema` support unless `Json Schema Mode` is verified.

## Tool Rule

Caller-defined tools map to OpenAI-compatible function tools.

Strict tool schemas require `Strict Tool Schema Mode = verified` and a connection profile that allows the DeepSeek beta surface.

Parallel tool calls remain blocked while `Parallel Tool Calls = unknown`.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = chat`
- `TextContent = final output text when available`
- `ThinkingContent = reasoning_content when returned`
- `ToolCalls = function_call output items`
- `Usage = normalized token usage including cache-hit and cache-miss tokens when available`
- `FinishReason = normalized provider finish reason`
- `Transport.IsStream = true or false`

## UI Rule

If the caller wants UI:

- show the model selector
- show stream toggle only for verified stream paths
- show thinking toggle because selected V4 rows are mixed-thinking
- do not show a thinking budget control for selected V4 rows
- show JSON object output control only when compatible with the selected row
- show tool editor for verified caller-defined tools
- hide or disable unknown options with explicit reasons
