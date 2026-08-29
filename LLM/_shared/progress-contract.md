# Shared Progress Contract

Use this state model across all `skill-llm-xxxx` skills.

## Progress Fields

| Field | Meaning |
| --- | --- |
| `FlowLabel` | Human-readable request label |
| `StageKey` | Stable machine-friendly stage key |
| `StageLabel` | Human-readable stage label |
| `Detail` | Short extra detail text |
| `RequestKind` | `chat`, `vision`, `imaging`, `music`, `speech`, or `transcription` |
| `Model` | Exact provider model |
| `ThinkingEnabled` | Whether the request asked for thinking |
| `IsStreaming` | Whether the transport is stream-based |
| `HasRemoteActivity` | Whether provider-side activity has started |
| `IsLocalProcessing` | Whether remote work is done and local work is still running |
| `ChunkCount` | Number of stream chunks received |
| `ResultItemCount` | Number of completed images, files, or other result items |
| `RetryCount` | Number of retries so far |
| `StartedAtUtc` | Absolute request start time |
| `StageStartedAtUtc` | Absolute stage start time |
| `LastRemoteActivityAtUtc` | Last observed provider activity time |
| `PossiblyStalled` | Whether the request may be stalled |
| `IsCompleted` | Whether the request finished successfully |
| `IsFailed` | Whether the request failed |
| `IsCanceled` | Whether the request was canceled |
| `IsTimedOut` | Whether the request timed out |
| `FailureCode` | Shared error code when failed |
| `FailureReason` | Short failure text when failed |

## Base State Machine

Use this base flow:

`idle -> validating -> preparing -> sending|submitting-job -> waiting-first-byte|waiting-result|waiting-provider-accept -> streaming|polling-job -> downloading-result -> local-processing -> completed`

Any active stage may transition to:

- `failed`
- `canceled`
- `timed-out`

## Percent Rule

Do not fake progress percentages.

Only expose a numeric percent when the provider returns a stable job progress value that the caller can trust.

Until then, use:

- current stage
- elapsed time
- last activity age
- chunk count
- result item count

## Request-Kind Notes

- `chat` and `vision` usually care about `waiting-first-byte` and `streaming`.
- `imaging` and `music` usually care about `submitting-job`, `waiting-provider-accept`, `polling-job`, and `downloading-result`.
- `speech` HTTP streaming usually uses `waiting-first-byte` then `streaming`; non-stream speech usually uses `waiting-result`.
- `transcription` batch requests usually use `waiting-result`. When a provider accepts asynchronous webhook delivery, the request may end at provider acceptance while the transcript remains incomplete until the external delivery path finishes.

## Example

For a stream chat request, `ChunkCount` grows during `streaming`. For an image generation job, `ResultItemCount` stays `0` until the provider has stable outputs.
