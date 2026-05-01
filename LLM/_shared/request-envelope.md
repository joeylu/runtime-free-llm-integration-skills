# Shared Request Envelope

Use this normalized request contract across all `skill-llm-xxxx` skills.

## Fields

| Field | Meaning |
| --- | --- |
| `RequestKind` | `chat`, `vision`, `imaging`, or `music` |
| `ConnectionProfileKey` | named connection profile such as `build` or `plan`; resolved before model selection |
| `Model` | Exact provider model value |
| `IsStream` | Request stream transport when verified |
| `ThinkingRequested` | Caller intent to request reasoning output; when omitted, the model's documented thinking default applies |
| `ThinkingBudget` | Optional provider-specific thinking budget |
| `ReasoningEffort` | Optional enum-style reasoning control such as `none`, `low`, `medium`, `high`, or `xhigh` |
| `ReasoningSummary` | Optional request for provider-visible reasoning summaries when verified |
| `Temperature` | Optional randomness control, gated by the provider capability matrix and effective thinking state |
| `ResponseFormat` | Optional structured-output requirement such as `json_object` or `json_schema`; some providers only allow it in specific thinking modes |
| `Tools` | Optional caller-defined tools or functions, gated by the provider capability matrix |
| `ToolChoice` | Optional tool-choice directive, gated by the provider capability matrix |
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

For `vision`, `Inputs.Images` is the input image list. Do not use `Inputs.ImageCount` for vision input images; `Inputs.ImageCount` is reserved for imaging output count.

`ThinkingRequested` is the provider-neutral intent. `ReasoningEffort` is the common OpenAI-style control; for example, `ReasoningEffort = none` means effective thinking is false, while `ReasoningEffort = high` means effective thinking is true.

## Fail-Fast Rules

- If `ConnectionProfileKey` is supplied, the profile must exist, be active, and allow the requested `RequestKind`, `Model`, API surface, and options.
- Do not silently fall back from one connection profile, API key, or base URL to another.
- If a requested option is not verified in the provider capability matrix, stop.
- If both `ThinkingRequested` and `ReasoningEffort` are supplied, they must describe the same effective thinking state.
- Do not silently map one request kind to another.
- Do not pass unsupported fields just because the caller supplied them.
- Put true provider-specific escape hatches under `ProviderOptions`, not under misleading shared field names.

## Example

If the caller wants image generation, use `RequestKind = imaging` and `Inputs.Prompt = "a red fox in snow"`. Do not fake this as `chat`.
