# Aliyun Chat Transport

Use this file for text-first direct-model chat requests.

## Input Shape

Build the shared request envelope with:

- `RequestKind = chat`
- optional `ConnectionProfileKey`
- `Model = <API Model>`
- `Inputs.Messages = [...]`
- optional `IsStream`
- optional `ThinkingRequested`
- optional `ThinkingBudget`
- optional `Temperature`
- optional `ResponseFormat`

## Transport Choice

Use `non-stream` when the caller wants a single completed response and `Supports Non-Stream` is `verified` or `inherited`.

Use `stream` only when `Supports Stream = verified` and the capability matrix verifies the requested model and option combination.

For Aliyun sync work, `Supports Stream = verified` may come from the official stream transport doc plus the matching official text-model family page. It does not require a model-row-specific stream example every time.

## Effective Thinking Rule

Treat `ThinkingRequested` as caller intent, not guaranteed provider behavior.

Resolve the effective request thinking state in this order:

1. If the caller explicitly sets `ThinkingRequested`, use that value.
2. Otherwise, if `Thinking Mode = mixed`, use `Thinking Default`.
3. Otherwise, if `Thinking Mode = always-on`, use `true`.
4. Otherwise, use `false`.

Return both:

- `ThinkingRequested`
- `ThinkingApplied`

If `ThinkingRequested = true` and `Thinking Mode` is `unsupported` or `unknown`, stop before wiring the request.

If `ThinkingRequested = false` and `Thinking Mode = always-on`, stop before wiring the request.

Pass `ThinkingBudget` only when `Thinking Budget Field = verified`.

## Temperature Rule

Pass `Temperature` only when `Temperature Mode` is compatible with the effective thinking state.

Do not silently drop the parameter.

## Response Format Rule

Pass `ResponseFormat` only when `Json Object Mode` is compatible with the effective thinking state.

Example:
If `Thinking Default = on` and `Json Object Mode = non-thinking-only`, the caller must explicitly set `ThinkingRequested = false` before sending `json_object`.

Do not silently downgrade strict structured output.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = chat`
- `TextContent = final assistant text`
- `ThinkingContent = provider reasoning text when available`
- `Usage = normalized token or billing usage when available`
- `FinishReason = normalized provider finish reason`
- `Transport.IsStream = true or false`

## UI Rule

If the caller wants UI:

- show the model selector
- show stream toggle only for verified stream paths
- show thinking toggle only when `Thinking Mode = mixed`
- show temperature control only when `Temperature Mode` is compatible with the resolved thinking state
- show response-format control only when `Json Object Mode` is compatible with the resolved thinking state
