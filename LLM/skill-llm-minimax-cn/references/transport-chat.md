# MiniMax China Mainland Chat Transport

- `SchemaVersion: 2`
- `LastReviewedAt: 2026-07-14`
- Route: `text-chat@chat-completions@v1`
- Reviewed candidate route: `multimodal-chat@chat-completions@v1` for `MiniMax-M3`; candidate status does not make it selectable.

Resolve `ConnectionProfileKey`, `ApiSurface`, `ApiVersion`, `ResolvedRequestUrl`, and the exact capability row before mapping fields.

## Request Mapping

| Shared Field | MiniMax Field | Gate |
| --- | --- | --- |
| `Model` | `model` | selected catalog row |
| `Inputs.Messages` | `messages` | required |
| `IsStream` | `stream` | verified |
| `MaxOutputTokens` | `max_completion_tokens` | verified range below |
| `Temperature` | `temperature` | verified; `0 <= value <= 2` |
| `Tools` | `tools` | function tools verified |
| `ProviderOptions.service_tier` | `service_tier` | `standard` or `priority`; pricing scope must match |
| `ProviderOptions.reasoning_split` | `reasoning_split` | boolean output-format switch; it does not enable/disable thinking |

Do not send deprecated `max_tokens`. `ToolChoice`, strict tool-schema semantics, and parallel-tool semantics remain fail-closed while their exact capability fields are `unknown`.

## Output-Limit Rule

- `MiniMax-M2.7` and `MiniMax-M2.7-highspeed`: `1..204800`; official recommended value `65536`.
- `MiniMax-M3`: `1..524288`; official recommended value `131072`.

A recommendation is not a maximum. Reject values above the exact model maximum before sending.

## Thinking Rule

- M2.x thinking cannot be disabled. Reject `ThinkingRequested = false` and any normalized effort meaning no thinking.
- MiniMax-M3 defaults to adaptive thinking when `thinking` is omitted. Because M3 is locally `not-selected`, do not route to it unless the catalog/profile is explicitly changed first.
- `reasoning_split = true` separates provider thinking into `reasoning_content` and `reasoning_details`; it does not change whether thinking occurs.

For M2.7 responses that return `<think>...</think>` inside assistant content, separate the leading thinking block only when it can be parsed deterministically. Otherwise keep the raw content and emit a warning; do not delete text.

## Multimodal Candidate Boundary

`MiniMax-M3` official messages support text, image, video, and tool-call content. This repository currently models only image input under `multimodal-chat`; video content remains blocked until a typed shared input rule and role/content matrix are added.

## Streaming

Use the same URL with `stream = true`. Preserve chunk order, tool-call fragments, provider reasoning fields, usage, finish reason, and cancellation. Apply any think-tag split only after complete assembly.

## Response Mapping

- `ResultKind = text-chat` or `multimodal-chat` according to the selected canonical request kind
- assistant answer -> `TextContent`
- provider reasoning fields or safely parsed think block -> `ThinkingContent`
- function calls -> `ToolCalls`
- usage -> `Usage`
- provider finish reason -> `FinishReason`
- stream metadata -> `Transport`

## Fail-Fast Rule

Stop before sending when the profile/model/route is not allowed, a requested field is `unknown` or `unsupported`, `MaxOutputTokens` is out of range, M2.x thinking is requested off, or a `priority` tier lacks a matching price row.

Official reference: `https://platform.minimaxi.com/docs/api-reference/text-chat-openai`.
