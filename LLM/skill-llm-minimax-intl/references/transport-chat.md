# MiniMax International Chat Transport

Use `MiniMax-M3` through the OpenAI-compatible Chat Completions surface documented in `request-urls.md`.

## Request Mapping

| Shared Field | MiniMax Field | Rule |
| --- | --- | --- |
| `Model` | `model` | exact catalog model ID |
| `Inputs.Messages` | `messages` | required; supports text, image, video, and tool-call content |
| `IsStream` | `stream` | boolean; default `false` |
| `MaxOutputTokens` | `max_completion_tokens` | `1..524288`; recommended `131072` |
| `Temperature` | `temperature` | range `[0,2]`; default `1` |
| `Tools` | `tools` | function tools supported |
| `ProviderOptions.thinking` | `thinking` | omit for adaptive thinking or send an officially documented M3 value |
| `ProviderOptions.reasoning_split` | `reasoning_split` | output-format switch only |
| `ProviderOptions.service_tier` | `service_tier` | `standard` or `priority`; priority pricing is 1.5x standard |

Use `max_completion_tokens`; `max_tokens` is deprecated.

`reasoning_split = true` moves thinking content into provider reasoning fields. It does not enable or disable thinking.

For `MiniMax-M3`, an omitted `thinking` field selects the documented `adaptive` default. Preserve `adaptive` as the resolved default state in diagnostics; for mode-sensitive gating on this exact Chat Completions route, the official MiniMax mapping treats adaptive as thinking on. Sending `thinking.type = disabled` explicitly selects non-thinking mode. Do not copy this default or mapping to Responses, Anthropic-compatible, or any other surface.

## Multimodal Messages

`MiniMax-M3` accepts image and video content in messages. This skill maps image input through the shared vision contract. Add video mapping only when the host project has an explicit typed video-input contract.

## Streaming

Use the same request URL with `stream = true`. Preserve chunk order, reasoning fields, tool-call fragments, usage, finish reason, errors, and cancellation.

## Response Mapping

- assistant answer -> `TextContent`
- provider thinking output -> `ThinkingContent`
- function calls -> `ToolCalls`
- usage -> `Usage`
- provider finish reason -> `FinishReason`
- stream metadata -> `Transport`

Stop before sending when the request uses an unknown capability, an incompatible profile or surface, or an output limit outside the documented range.

Official reference: `https://platform.minimax.io/docs/api-reference/text-chat-openai`.
