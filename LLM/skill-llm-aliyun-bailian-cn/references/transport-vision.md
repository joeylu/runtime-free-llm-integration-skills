# Aliyun Vision Transport

Use this file for image-understanding requests.

## Input Shape

Build the shared request envelope with:

- `RequestKind = vision`
- optional `ConnectionProfileKey`
- `ApiSurface = chat-completions`
- `Model = <API Model>`
- `Inputs.Messages = [...]`
- `Inputs.Images = [...]`
- optional `IsStream`
- optional `ThinkingRequested`
- optional `ThinkingBudget`
- optional `Temperature`
- optional `ResponseFormat`

Example:
One vision request can include a user text message plus one or more image items.

## Transport Choice

Use `non-stream` as the default safe path only when `Supports Non-Stream` is `verified` or `inherited`.

Use `stream` only when `Supports Stream = verified` and the capability matrix explicitly verifies that model-kind combination.

Resolve `ResolvedRequestUrl` from `request-urls.md` before sending.

## Image Rule

Only models listed under the `vision` catalog may be used for image-understanding requests.

Do not route image input through rows listed only under `chat`.

## Effective Thinking Rule

Keep the same rule as chat:

- `ThinkingRequested` is caller intent
- `ThinkingApplied` is normalized provider result

Resolve the effective request thinking state in this order:

1. If the caller explicitly sets `ThinkingRequested`, use that value.
2. Otherwise, if `Thinking Mode = mixed`, use `Thinking Default`.
3. Otherwise, if `Thinking Mode = always-on`, use `true`.
4. Otherwise, use `false`.

If `ThinkingRequested = true` and `Thinking Mode` is `unsupported` or `unknown`, stop.

If `ThinkingRequested = false` and `Thinking Mode = always-on`, stop.

Pass `ThinkingBudget` only when `Thinking Budget Field = verified`.

## Temperature Rule

Pass `Temperature` only when `Temperature Mode` is compatible with the effective thinking state.

Do not silently drop the parameter.

## Response Format Rule

Pass `ResponseFormat` only when `Json Object Mode` is compatible with the effective thinking state.

Do not silently switch a default-on mixed-thinking model into non-thinking mode.

## Response Mapping

Map the provider result into the shared response envelope:

- `ResultKind = vision`
- `TextContent = final understanding output`
- `ThinkingContent = provider reasoning text when available`
- `Usage = normalized usage`
- `Transport.IsStream = true or false`

## UI Rule

If the caller wants UI:

- show image picker or image attachment surface
- show model selector filtered to `vision`
- show response-format control only when `Json Object Mode` is compatible with the resolved thinking state
- hide controls that are not verified by the capability matrix
