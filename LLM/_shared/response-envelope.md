# Shared Response Envelope

Use this normalized response contract across all `skill-llm-xxxx` skills.

## Fields

| Field | Meaning |
| --- | --- |
| `ResultKind` | `chat`, `vision`, `imaging`, or `music` |
| `Model` | Exact provider model value that produced the result |
| `TextContent` | Final text output |
| `ThinkingContent` | Provider reasoning or thinking text when available |
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
- For job-style flows such as imaging or music, use `ImageOutputs` or `AudioOutputs` rather than stuffing URLs into `TextContent`.
- Do not use `Warnings` to justify silent fallback, silent degradation, or continuing after an unverified capability. Those cases must be errors before sending or explicit user-approved changes.

## Example

If a music request returns two audio files, put them in `AudioOutputs`, keep `ResultKind = music`, and keep `TextContent` empty unless the provider also returned text.
