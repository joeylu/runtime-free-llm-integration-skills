# Shared Request Envelope

Use this normalized request contract across all `skill-llm-xxxx` skills.

## Fields

| Field | Meaning |
| --- | --- |
| `RequestKind` | `chat`, `vision`, `imaging`, or `music` |
| `Model` | Exact provider model value |
| `IsStream` | Request stream transport when verified |
| `ThinkingRequested` | Caller intent to request reasoning output; when omitted, the model's documented thinking default applies |
| `ThinkingBudget` | Optional provider-specific thinking budget |
| `Temperature` | Optional randomness control, gated by the provider capability matrix and effective thinking state |
| `ResponseFormat` | Optional structured-output requirement such as `json_object`; some providers only allow it in specific thinking modes |
| `IncludeUsage` | Whether normalized usage should be returned when available |
| `TimeoutMs` | Full request timeout |
| `Cancellation` | Cancellation handle from the host platform |
| `ProgressCallback` | Shared progress emitter |
| `Inputs` | Request payload union by `RequestKind` |
| `ProviderOptions` | Provider-specific extras that do not fit the shared fields |
| `Metadata` | Caller-defined non-provider metadata |

## Inputs By Request Kind

| Request Kind | Required Inputs | Common Optional Inputs |
| --- | --- | --- |
| `chat` | `Messages` | none |
| `vision` | `Messages`, `Images` | none |
| `imaging` | `Prompt` | `ReferenceImages`, `Seed`, `ImageSize`, `ImageCount` |
| `music` | `Prompt` | `Lyrics`, `DurationSeconds`, `Seed` |

Keep these request-kind-specific options under `Inputs`.

Example:
Use `Inputs.Seed` and `Inputs.ImageSize`, not top-level `Seed` or `ImageSize`.

## Fail-Fast Rules

- If a requested option is not verified in the provider capability matrix, stop.
- Do not silently map one request kind to another.
- Do not pass unsupported fields just because the caller supplied them.
- Put true provider-specific escape hatches under `ProviderOptions`, not under misleading shared field names.

## Example

If the caller wants image generation, use `RequestKind = imaging` and `Inputs.Prompt = "a red fox in snow"`. Do not fake this as `chat`.
