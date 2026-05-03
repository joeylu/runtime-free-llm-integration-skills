# MiniMax International Chat Transport

Use this file after resolving:

- `ConnectionProfileKey`
- `ApiSurface = chat-completions`
- `ResolvedBaseUrl`
- `ResolvedRequestUrl`
- `Model`
- capability-matrix gates

`ConnectionProfileKey` must be either `build` or `plan` unless the host project explicitly defines another MiniMax International profile. Even when both profiles use `https://api.minimax.io/v1`, resolve `ResolvedBaseUrl` from the selected profile and use that profile's API key reference.

## Request Mapping

MiniMax International chat uses the OpenAI-compatible Chat Completions request shape.

Map shared request fields like this:

| Shared Field | MiniMax OpenAI-Compatible Field |
| --- | --- |
| `Model` | `model` |
| `Inputs.Messages` | `messages` |
| `IsStream` | `stream` |
| `Temperature` | `temperature` only after capability verification |

Do not pass `ResponseFormat`, `Tools`, `ToolChoice`, `ReasoningEffort`, `ThinkingBudget`, or strict tool-schema fields until `capability-matrix.md` verifies the exact option.

## Thinking Output Mapping

MiniMax M2.7 OpenAI-compatible responses may put thinking output at the start of `message.content` inside `<think>...</think>` tags.

When present:

- put the tagged thinking text in `ThinkingContent`
- put the remaining answer text in `TextContent`
- set `ThinkingApplied = true`
- keep the original provider content under `ProviderMeta` when diagnostic retention is enabled

If the content cannot be split safely, keep the raw content in `TextContent` and fail with `parse_error` only when the caller explicitly required separated thinking.

## Streaming

Use the same request URL when `IsStream = true`; MiniMax selects streaming through the request body.

For stream chunks:

- emit progress stage `waiting-first-byte` until the first chunk
- increment `ChunkCount` during `streaming`
- assemble content in order
- apply the same thinking-output mapping after the final assembled content is complete

## Response Mapping

Map the provider response into `../../_shared/response-envelope.md`:

| Shared Field | Source |
| --- | --- |
| `ResultKind` | `chat` |
| `Model` | response model when present, otherwise requested model |
| `TextContent` | final assistant content after thinking split |
| `ThinkingContent` | extracted think-tag content when present |
| `Usage` | provider usage fields when present |
| `FinishReason` | provider finish reason when present |
| `Transport` | stream or non-stream metadata |
| `ProviderMeta` | MiniMax-specific response leftovers |

## Errors

Map failures into `../../_shared/error-contract.md`.

Use:

- `config_error` when `MINIMAX_INTL_BUILD_API_KEY`, `MINIMAX_INTL_PLAN_API_KEY`, or the selected profile is missing
- `request_url_error` when the request URL row is missing, unknown, or region-mismatched
- `capability_unverified` when a requested option is `unknown`
- `unsupported_option` when a requested option is `unsupported`
- `provider_error` for non-success provider responses
- `parse_error` when the response shape cannot be normalized safely
