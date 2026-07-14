# Aliyun Bailian International/Singapore Chat Transport

Use this file for text-first direct-model requests to the Singapore deployment.

## Surface Choice

Use `responses` for new `qwen3.7-max` agent flows that need provider-managed continuation, enum-style reasoning effort, Session Cache, provider-hosted tools, or Responses event streaming.

Use `chat-completions` for compatibility flows that need manual message history, `enable_thinking`, `thinking_budget`, `preserve_thinking`, or the legacy Chat Completions thinking controls.

The `qwen3.7-max` alias currently resolves to the text-only `qwen3.7-max-2026-05-20` snapshot. Do not route image input through this model.

Do not silently switch surfaces. Resolve the exact capability row by:

`RequestKind = text-chat + Model + ApiSurface`

## Shared Input Shape

Build the shared request envelope with:

- `RequestKind = text-chat`
- optional `ConnectionProfileKey`
- `ApiSurface = responses | chat-completions`
- `Model = <API Model>`
- `Inputs.Messages = [...]` or a direct text input only on `responses`
- optional `Instructions`
- optional `IsStream`
- only the reasoning, tool, continuation, cache, temperature, and response-format fields verified for the selected surface

Resolve `ResolvedRequestUrl` from `request-urls.md` before sending.

## Responses Surface

### Request Mapping

For `ApiSurface = responses`:

- map a direct text input or message array to `input`
- map `Instructions` to `instructions`
- map `ReasoningEffort` to `reasoning.effort`
- allow only `none`, `minimal`, `low`, `medium`, or `high`
- use the provider default `medium` when no reasoning control is supplied
- map `ThinkingRequested = false` to `reasoning.effort = none`
- map `ThinkingRequested = true` with no explicit effort to `reasoning.effort = medium`
- map `Temperature` to `temperature` only in the documented range `[0, 2)`
- map `Tools` to custom entries with `type = function`
- map `HostedTools` to the verified built-in tool entries below
- map `ToolChoice` only according to the rules below
- map `ContinuationId` to `previous_response_id`
- map `StoreResponse` to `store`; the provider default is `true`
- map `IsStream` to `stream`

Do not send `thinking_budget`; it is unsupported on Responses.

Do not use `enable_thinking` as the primary control. Official docs state that `reasoning.effort` takes precedence and that `enable_thinking` will be deprecated on this surface.

Do not send `response_format`, `json_object`, `json_schema`, strict function-schema flags, `parallel_tool_calls`, `background`, or any unlisted OpenAI Responses parameter. The provider states that unlisted parameters are ignored; this skill blocks them before sending.

`ReasoningSummary` has no separate wire toggle in this transport. When reasoning is enabled, normalize returned reasoning `summary` items into `ReasoningSummary`.

### Caller-Defined Function Loop

Custom functions are verified on this surface.

- Each definition uses `type = function`, `name`, `description`, and an optional JSON Schema `parameters` object.
- A model function request is returned as an output item with `type = function_call`.
- Return the host result as `type = function_call_output`.
- The output `call_id` must exactly match the model's `call_id`.
- In an explicit input-item replay, place `function_call_output` immediately after its matching `function_call` item.
- Do not claim strict-schema enforcement; no `strict` request field is documented.
- Do not request parallel tool calls; no parallel-call request control is documented.

### Tool Choice

The default is `auto`.

Allowed string values are `auto`, `none`, and `required`. `required` is valid only when the supplied tool list contains exactly one tool.

The documented object form uses `type = allowed_tools`, `mode = auto|required`, and a list of allowed tool descriptors. The same one-tool restriction applies to `mode = required`.

Reject any other tool-choice form before sending.

### Continuation and Storage

The response `id` maps to normalized `ContinuationId`.

For a follow-up request:

- reuse it only with the same provider, Singapore deployment, connection profile, base URL, API surface, and compatible model family
- send only the new input with `previous_response_id`; do not resend a reconstructed complete history
- a new `input` and `previous_response_id` may be used together because the provider appends the new input to the stored context
- resend `Instructions` when needed because prior-turn `instructions` are not inherited
- do not combine `previous_response_id` with an unimplemented `conversation` flow

A response ID is valid for 7 days. If `store = false`, the response cannot be referenced later through `previous_response_id`. Do not expose its ID as a reusable continuation token.

Treat an expired, missing, cross-profile, or rejected ID as a provider/state error. Do not silently reconstruct history or switch surfaces.

### Session Cache

Map normalized cache intent as follows:

- `CacheMode = provider-default`: omit the cache header
- `CacheMode = session`: send `x-dashscope-session-cache: enable`
- `CacheMode = disabled`: send `x-dashscope-session-cache: disable`
- `CacheMode = explicit`: block until this transport defines an exact explicit-cache mapping

Session Cache requires at least 1024 prompt tokens and has a 5-minute lifetime. It does not guarantee a hit. Record `usage.input_tokens_details.cached_tokens` when returned.

Do not enable Session Cache silently because it changes server-side retention, billing, and latency behavior.

### Provider-Hosted Tools

For `qwen3.7-max`, the following built-in types are verified by the official Responses parameter reference and supported-model list:

| Hosted Tool Type | Status | Thinking Requirement | Additional Constraint |
| --- | --- | --- | --- |
| `web_search` | `verified` | none documented | normalize search actions and sources |
| `web_extractor` | `verified` | none documented for `qwen3.7-max` | must be supplied together with `web_search` |
| `code_interpreter` | `verified` | required for `qwen3.7-max`; reject `ReasoningEffort = none` | normalize code, logs, and container metadata |

Do not infer support for `web_search_image`, `image_search`, `file_search`, `mcp`, or other hosted tool types merely because the generic API page lists them. Add them only after the project verifies their exact model, region, credentials, and payload contract.

Provider-hosted tools may be combined with custom functions, but their results belong in `HostedToolCalls`, not `ToolCalls`.

### Streaming

For `IsStream = true`, process Responses events, not Chat Completions deltas.

At minimum:

- order events by `sequence_number`
- append `response.output_text.delta`
- append `response.reasoning_summary_text.delta` to the reasoning summary, never to raw thinking content
- capture function and hosted-tool output items from `response.output_item.added` and `response.output_item.done`
- capture web-search and code-interpreter state events when emitted
- treat `response.completed` as the authoritative final response and usage record
- surface provider failure, cancellation, or incomplete states; do not retry as non-stream or on another surface

### Response Mapping

Map:

- `ResultKind = chat`
- `TextContent = output_text or assembled output_text parts`
- `ReasoningSummary = reasoning summary text`
- `ToolCalls = custom function_call items`
- `HostedToolCalls = provider-hosted call/output items`
- `Annotations = output annotations and hosted-tool sources`
- `ContinuationId = response.id` only when reusable under the storage rule
- `Usage = input, output, total, cached, reasoning, billing-detail, and hosted-tool usage when returned`
- `Transport.IsStream = true or false`

Do not map reasoning summaries into `ThinkingContent`.

## Chat Completions Surface

### Request Mapping

For `ApiSurface = chat-completions`:

- map `Inputs.Messages` to `messages`
- map explicit `ThinkingRequested` to `enable_thinking`
- pass `ThinkingBudget` only when the exact capability row verifies it
- pass `ProviderOptions.PreserveThinking = true` only when the exact model row verifies `preserve_thinking`
- pass `Temperature` only when the exact row and effective thinking state allow it
- pass `ResponseFormat = json_object` only when the exact row and effective thinking state allow it
- map `IsStream` to `stream`

For `qwen3.7-max`, `preserve_thinking = true` includes historical assistant `reasoning_content` in the next input and therefore in input-token billing. Do not enable it by default.

`ContinuationId`, `StoreResponse`, `HostedTools`, and `CacheMode = session` are not Chat Completions controls in this skill. Block them instead of translating them to another mechanism.

Caller-defined function mode compatibility remains blocked while `Tool Calling Mode = unknown` for the selected Chat Completions row.

### Effective Thinking and Structured Output

Resolve effective thinking from the explicit request and then the exact row default.

For `qwen3.7-max`, both `json_object` and `json_schema` are blocked because structured output is explicitly unsupported on the selected Chat Completions row.

Never silently turn thinking off to satisfy a response-format request.

### Response Mapping

Map:

- `ResultKind = chat`
- `TextContent = final assistant text`
- `ThinkingContent = reasoning_content when returned`
- `Usage = normalized token and cache usage when available`
- `FinishReason = normalized provider finish reason`
- `Transport.IsStream = true or false`

## UI Rule

When both surfaces are allowed:

- display the surface selector
- show `ReasoningEffort`, continuation, storage, Session Cache, and hosted tools only for Responses
- show the thinking toggle, thinking budget, preserve-thinking option, and compatible response format only for Chat Completions
- show temperature only when the exact row allows it
- clear or reject incompatible values when the surface changes; never preserve and silently drop them

## Official Sources

- `https://www.alibabacloud.com/help/en/model-studio/qwen-api-via-openai-responses`
- `https://www.alibabacloud.com/help/en/model-studio/compatibility-with-openai-responses-api`
- `https://www.alibabacloud.com/help/en/model-studio/text-generation`
- `https://www.alibabacloud.com/help/en/model-studio/context-cache`
