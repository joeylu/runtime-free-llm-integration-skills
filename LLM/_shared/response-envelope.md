# Shared Response Envelope

Use this normalized response contract across all `skill-llm-xxxx` skills.

## Fields

| Field | Meaning |
| --- | --- |
| `ResultKind` | `chat`, `vision`, `imaging`, `music`, `speech`, or `transcription` |
| `Model` | exact provider model value that produced the result |
| `TextContent` | final text output |
| `StructuredContent` | parsed structured output when a verified schema mode was requested |
| `ThinkingContent` | provider raw reasoning text only when official docs explicitly expose it |
| `ReasoningSummary` | provider-visible reasoning summary when available |
| `ReasoningItems` | provider-specific thought signatures, encrypted reasoning items, or other reasoning continuation items |
| `ToolCalls` | normalized caller-defined function/tool calls |
| `HostedToolCalls` | normalized provider-hosted tool execution records, kept separate from caller-defined tool calls |
| `Annotations` | normalized citations, URL annotations, file references, or grounding metadata when available |
| `ContinuationId` | opaque provider-issued response, interaction, or conversation ID that may be used for a verified follow-up |
| `ImageOutputs` | generated image result list |
| `AudioOutputs` | generated audio result list |
| `Usage` | normalized usage or billing summary, including cache and reasoning details when returned |
| `FinishReason` | normalized completion reason |
| `ThinkingRequested` | whether the caller asked for thinking |
| `ThinkingApplied` | whether the provider actually applied thinking |
| `Transport` | stream or non-stream metadata |
| `Timing` | request and stage timing summary |
| `Warnings` | non-fatal diagnostic warnings that do not change requested capability semantics |
| `ProviderMeta` | provider-specific response metadata |

## Rules

- Keep result data normalized even when the provider payload is irregular.
- Put provider-specific leftovers under `ProviderMeta`.
- Return `ThinkingRequested` and `ThinkingApplied` separately. They are not the same thing.
- Do not put raw chain-of-thought into `ThinkingContent` unless official docs explicitly expose raw reasoning text.
- Put provider summaries in `ReasoningSummary`, not `ThinkingContent`, when the provider exposes only a summary.
- Put signed thought items or encrypted reasoning continuation state in `ReasoningItems`; do not render them to users.
- Put validated schema output in `StructuredContent`; keep raw final text in `TextContent` only when the provider returns one.
- Put caller-defined tool/function calls in `ToolCalls`.
- Put provider-hosted tool execution records in `HostedToolCalls`; do not mix them with caller-owned function calls.
- Preserve `ContinuationId` exactly as returned, but treat it as opaque and provider-scoped.
- For job-style flows such as imaging or music, use `ImageOutputs` or `AudioOutputs` rather than stuffing URLs into `TextContent`.
- For `speech`, put generated audio in `AudioOutputs`; keep provider timing/alignment data in `ProviderMeta` unless a host defines a separate normalized alignment layer.
- For `transcription`, put the final transcript in `TextContent`; keep word/character timing, speaker labels, detected language, audio duration, and other provider detail in `ProviderMeta`.
- Do not use `Warnings` to justify silent fallback, silent degradation, or continuing after an unverified capability. Those cases must be errors before sending or explicit user-approved changes.

## Example

For a Responses-style result, map the provider response ID to `ContinuationId`, final output text to `TextContent`, reasoning summary items to `ReasoningSummary`, and provider-hosted web-search records to `HostedToolCalls`.
