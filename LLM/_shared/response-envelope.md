# Shared Response Envelope

Use this normalized response contract across all `skill-llm-xxxx` skills.

## Fields

| Field | Meaning |
| --- | --- |
| `ResultKind` | one canonical request kind: `text-chat`, `multimodal-chat`, `image-generation`, `speech-generation`, `transcription`, `realtime-audio`, `music-generation`, or `video-generation` |
| `Model` | exact provider model value that produced the result |
| `TextContent` | final text output |
| `StructuredContent` | parsed structured output when a verified schema mode was requested |
| `ThinkingContent` | provider-exposed raw reasoning text only when the exact official contract exposes it |
| `ReasoningSummary` | provider-visible reasoning summary when available |
| `ReasoningItems` | provider-specific signatures, encrypted reasoning items, or other continuation state |
| `ToolCalls` | normalized caller-defined function/tool calls |
| `HostedToolCalls` | normalized provider-hosted tool execution records, separate from caller-defined calls |
| `Annotations` | normalized citations, URL annotations, file references, or grounding metadata |
| `ContinuationId` | opaque provider-issued response, interaction, or conversation ID usable only on a verified follow-up route |
| `ImageOutputs` | generated image result list |
| `AudioOutputs` | generated or returned audio result list |
| `VideoOutputs` | generated video result list |
| `TranscriptionContent` | normalized transcription result when applicable |
| `Usage` | normalized usage or billing summary, including cache and reasoning details when returned |
| `FinishReason` | normalized completion reason |
| `ThinkingRequested` | whether the caller asked for thinking |
| `ThinkingApplied` | whether the provider actually applied thinking |
| `Transport` | stream or non-stream metadata |
| `Timing` | request and stage timing summary |
| `Warnings` | non-fatal diagnostics that do not change requested capability semantics |
| `ProviderMeta` | provider-specific response metadata |

## Rules

- `ResultKind` uses canonical names. Legacy names may be accepted only before request normalization and must never appear in a canonical result.
- Keep result data normalized even when the provider payload is irregular; put provider-specific leftovers under `ProviderMeta`.
- Return `ThinkingRequested` and `ThinkingApplied` separately.
- Never expose hidden chain-of-thought. Populate `ThinkingContent` only when the provider intentionally returns reasoning text under its public API contract; otherwise use `ReasoningSummary`, `ReasoningItems`, usage, or no reasoning field.
- Put validated schema output in `StructuredContent`.
- Keep caller-defined `ToolCalls` separate from provider-hosted `HostedToolCalls`.
- Preserve `ContinuationId` exactly, but treat it as opaque, sensitive, provider-scoped, surface-scoped, and version-scoped.
- Use `ImageOutputs`, `AudioOutputs`, and `VideoOutputs` for media results rather than placing URLs in `TextContent`.
- `Warnings` must not justify silent fallback, silent degradation, or continuing after an unverified capability.

## Example

For a Responses-style result, map the provider response ID to `ContinuationId`, final output text to `TextContent`, visible reasoning summaries to `ReasoningSummary`, and provider-hosted web-search records to `HostedToolCalls`.
