# Shared Request Envelope

Use this normalized request contract across all `skill-llm-xxxx` skills.

## Fields

| Field | Meaning |
| --- | --- |
| `RequestKind` | `chat`, `vision`, `imaging`, or `music` |
| `ConnectionProfileKey` | named connection profile such as `build` or `plan`; resolved before model routing |
| `ApiSurface` | exact provider API surface chosen for the request, such as `responses`, `chat-completions`, `interactions`, `generate-content`, `dashscope-native-sync`, or `dashscope-native-async` |
| `ApiVersion` | exact provider API version from the resolved request-URL row |
| `EndpointKind` | exact endpoint kind from the resolved request-URL row |
| `RouteKey` | canonical full route key; must equal the five resolved route components |
| `ResolvedBaseUrl` | exact non-secret base URL resolved from the connection profile |
| `ResolvedRequestUrl` | exact non-secret request URL resolved from provider `request-urls.md` |
| `Model` | exact provider model value |
| `IsStream` | request stream transport when verified |
| `Instructions` | optional top-level system/developer instruction when the resolved surface documents a separate instruction field |
| `ThinkingRequested` | caller intent to request reasoning; when omitted, the documented model-and-surface default applies |
| `ThinkingBudget` | optional provider-specific thinking budget; never send it on a surface that uses only enum-style effort |
| `ReasoningEffort` | optional enum-style reasoning control such as `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, or `max` |
| `ReasoningSummary` | optional request for provider-visible reasoning summaries when verified |
| `Temperature` | optional randomness control, gated by the exact capability row and effective thinking state |
| `MaxOutputTokens` | optional output-token limit, mapped only when the resolved transport verifies the wire field and range |
| `ResponseFormat` | optional structured-output requirement such as `json_object` or `json_schema`; some providers allow it only in specific thinking modes or surfaces |
| `Tools` | optional caller-defined function tools, gated by `Tool Calling Mode` in the exact capability row |
| `HostedTools` | optional provider-hosted tools such as provider web search or code execution; verify each exact tool type separately from caller-defined functions |
| `ToolChoice` | optional tool-choice directive; the transport must verify whether it applies to caller-defined tools, hosted tools, or both |
| `ContinuationId` | optional opaque provider-issued continuation ID returned by a prior normalized response |
| `StoreResponse` | optional provider-side response persistence control; map only when the exact surface documents the wire field and continuation consequences |
| `CacheMode` | optional normalized cache intent: `provider-default`, `disabled`, `session`, or `explicit` |
| `CacheKey` | optional provider cache-routing key when the resolved surface verifies one |
| `CacheRetention` | optional provider cache-retention value when the resolved surface verifies one |
| `IncludeUsage` | whether normalized usage should be returned when available |
| `TimeoutMs` | full request timeout |
| `Cancellation` | cancellation handle from the host platform |
| `ProgressCallback` | shared progress emitter |
| `Inputs` | request payload union by `RequestKind` |
| `ProviderOptions` | typed provider-specific extras that do not fit shared fields |
| `Metadata` | caller-defined non-provider metadata |

## Inputs By Request Kind

| Request Kind | Required Inputs | Common Optional Inputs |
| --- | --- | --- |
| `chat` | `Messages` or a provider-verified direct text input | none |
| `vision` | `Messages`, `Images` | none |
| `imaging` | `Prompt` | `ReferenceImages`, `Seed`, `ImageSize`, `ImageCount` |
| `music` | `Prompt` | `Lyrics`, `DurationSeconds`, `Seed` |

Keep request-kind-specific options under `Inputs`.

Example:
Use `Inputs.Seed` and `Inputs.ImageSize`, not top-level `Seed` or `ImageSize`.

For `vision`, `Inputs.Images` is the input image list. Do not use `Inputs.ImageCount` for vision input images; `Inputs.ImageCount` is reserved for imaging output count.

`ThinkingRequested` is provider-neutral intent. `ReasoningEffort` is an enum-style control whose exact allowed values and wire mapping come from the resolved `RequestKind + Model + ApiSurface + ApiVersion + EndpointKind` capability row and transport.

`ContinuationId` is provider-neutral storage for a provider-issued state ID. Examples of wire mappings include `previous_response_id` or `previous_interaction_id`; the provider transport owns that mapping.

## Tool Separation Rules

- `Tools` contains only caller-defined functions whose execution is owned by the host project.
- `HostedTools` contains only tools executed by the provider.
- Do not place a provider-hosted web search declaration into `Tools` just because both providers use a wire field named `tools`.
- Do not infer caller-defined function support from hosted-tool support, or vice versa.
- Normalize provider-hosted execution results into `HostedToolCalls`, not `ToolCalls`.

## Continuation Rules

- Reuse `ContinuationId` only with the same provider, region, connection profile, base URL, API surface, and compatible model family unless official provider docs explicitly allow a broader scope.
- Do not silently convert `ContinuationId` into a full message-history replay or the reverse.
- If `StoreResponse = false` makes the returned ID unusable for continuation, do not advertise that ID as reusable; record the limitation in `ProviderMeta` or `Warnings`.
- If the resolved surface requires signed thought items, encrypted reasoning items, function-call IDs, or other continuation state, preserve them in `ReasoningItems` or typed `ProviderOptions` as directed by the provider transport.
- If required continuation state is missing or was altered, stop before sending.

## Cache Rules

- `CacheMode = provider-default` means do not add cache-specific request fields or headers.
- `CacheMode = disabled`, `session`, or `explicit` requires exact provider-and-surface verification.
- Do not silently enable caching because it may change retention, cost, latency, or data-handling behavior.
- Do not send `CacheKey` or `CacheRetention` unless the resolved transport documents the exact wire mapping.

## Fail-Fast Rules

- If `ConnectionProfileKey` is supplied, the profile must exist, be active, and allow the requested `RequestKind`, `Model`, API surface, and options.
- Resolve `ApiSurface`, `ApiVersion`, `EndpointKind`, `RouteKey`, `ResolvedBaseUrl`, and `ResolvedRequestUrl` before capability lookup and before sending.
- Resolve capabilities by the exact full `RouteKey`.
- Do not silently fall back from one connection profile, API key, base URL, API surface, request URL, model, or state-management method to another.
- If a requested option is not verified in the exact provider capability row or transport, stop.
- If both `ThinkingRequested` and `ReasoningEffort` are supplied, they must describe the same effective thinking state.
- Do not silently map one request kind to another.
- Do not pass unsupported fields just because the caller supplied them.
- Do not put API keys, signed URLs, or other secrets in `ResolvedRequestUrl`, `Metadata`, or loggable provider options.
- Put true provider-specific escape hatches under typed `ProviderOptions`, not under misleading shared field names.

## Example

For a stateful Responses request, select `ApiSurface = responses`, pass the previous normalized `ContinuationId`, and let the provider transport map it to the documented wire field. Do not send both a continuation ID and a reconstructed full history unless that provider explicitly documents the combination.
