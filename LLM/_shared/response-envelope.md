# Shared Response Envelope

Use this normalized response contract across all `skill-llm-xxxx` skills.

## Fields

| Field | Meaning |
| --- | --- |
| `ResultKind` | `chat`, `vision`, `imaging`, or `music` |
| `Model` | Exact provider model value that produced the result |
| `TextContent` | Final text output |
| `StructuredContent` | Parsed structured output when a verified schema mode was requested |
| `ThinkingContent` | Provider reasoning or thinking text when available |
| `ReasoningSummary` | Provider-visible reasoning summary when available |
| `ReasoningItems` | Provider-specific reasoning items, such as encrypted continuation items |
| `ToolCalls` | Normalized caller-defined tool/function calls |
| `ImageOutputs` | Generated image result list |
| `AudioOutputs` | Generated audio result list |
| `Usage` | Normalized usage or billing summary |
| `FinishReason` | Normalized completion reason |
| `ThinkingRequested` | Whether the caller asked for thinking |
| `ThinkingApplied` | Whether the provider actually applied thinking |
| `Transport` | Stream or non-stream metadata |
| `Timing` | Request and stage timing summary |
| `Warnings` | Non-fatal diagnostic warnings that do not change requested capability semantics |
| `ProviderMeta` | Provider-specific response metadata |

## Rules

- Keep result data normalized even when the provider payload is irregular.
- Put provider-specific leftovers under `ProviderMeta`.
- Return `ThinkingRequested` and `ThinkingApplied` separately. They are not the same thing.
- Do not put raw chain-of-thought into `ThinkingContent` unless official docs explicitly expose raw reasoning text.
- Put provider summaries in `ReasoningSummary`, not `ThinkingContent`, when the provider exposes only a summary.
- Put validated schema output in `StructuredContent`; keep the raw final text in `TextContent` only when the provider returns one.
- Put caller-defined tool/function calls in `ToolCalls`; do not mix them with provider-hosted tool metadata.
- For job-style flows such as imaging or music, use `ImageOutputs` or `AudioOutputs` rather than stuffing URLs into `TextContent`.
- Do not use `Warnings` to justify silent fallback, silent degradation, or continuing after an unverified capability. Those cases must be errors before sending or explicit user-approved changes.

## Example

If a music request returns two audio files, put them in `AudioOutputs`, keep `ResultKind = music`, and keep `TextContent` empty unless the provider also returned text.
