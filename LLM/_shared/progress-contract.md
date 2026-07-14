# Shared Progress Contract

Use this state model across all `skill-llm-xxxx` skills.

## Progress Fields

| Field | Meaning |
| --- | --- |
| `FlowLabel` | human-readable request label |
| `StageKey` | stable machine-friendly stage key |
| `StageLabel` | human-readable stage label |
| `Detail` | short extra detail text |
| `RequestKind` | canonical request kind |
| `Model` | exact provider model |
| `ThinkingEnabled` | whether the request asked for thinking |
| `IsStreaming` | whether the transport is stream-based |
| `HasRemoteActivity` | whether provider-side activity has started |
| `IsLocalProcessing` | whether remote work is done and local work is still running |
| `ChunkCount` | number of stream chunks received |
| `ResultItemCount` | number of completed media, files, or other result items |
| `RetryCount` | number of retries so far |
| `StartedAtUtc` | absolute request start time |
| `StageStartedAtUtc` | absolute stage start time |
| `LastRemoteActivityAtUtc` | last observed provider activity time |
| `PossiblyStalled` | whether the request may be stalled |
| `IsCompleted` | whether the request finished successfully |
| `IsFailed` | whether the request failed |
| `IsCanceled` | whether the request was canceled |
| `IsTimedOut` | whether the request timed out |
| `FailureCode` | shared error code when failed |
| `FailureReason` | short failure text when failed |

## Base State Machine

`idle -> validating -> preparing -> sending|submitting-job -> waiting-first-byte|waiting-result|waiting-provider-accept -> streaming|polling-job -> downloading-result -> local-processing -> completed`

Any active stage may transition to `failed`, `canceled`, or `timed-out`.

## Percent Rule

Do not fabricate progress percentages. Expose a numeric percentage only when the provider returns a documented, stable progress value. Otherwise report stage, elapsed time, last activity age, chunk count, and result count.

## Request-Kind Notes

- `text-chat`, `multimodal-chat`, `speech-generation`, `transcription`, and `realtime-audio` commonly use `waiting-first-byte` and `streaming` when their exact surface supports streaming.
- `image-generation`, `music-generation`, and `video-generation` may use `submitting-job`, `waiting-provider-accept`, `polling-job`, and `downloading-result` when their exact transport is asynchronous.
- The selected request kind does not determine sync versus async by itself; the exact URL and capability rows do.

## Example

For streaming text, `ChunkCount` grows during `streaming`. For an asynchronous image job, `ResultItemCount` remains `0` until stable outputs are available.
