# OpenAI Chat Transport

Use this file for text-first requests with the documented GPT-5.6 models.

## Surface Choice

- Prefer `responses`.
- Use `chat-completions` only for explicit compatibility requirements and only with fields verified on that exact row.
- Do not move a request between surfaces after route resolution.

## Shared Input

Required:

- `RequestKind = chat`
- `ConnectionProfileKey`
- `Model`
- `ApiSurface`
- `Inputs.Messages` or a provider-verified direct text input

Optional fields are allowed only when the exact capability row and this transport verify their wire mapping.

## Responses Request Mapping

Map:

- `Model` -> `model`
- `Instructions` -> `instructions`
- message/input items -> `input`
- `IsStream` -> `stream`
- `MaxOutputTokens` -> `max_output_tokens`
- `ContinuationId` -> `previous_response_id`
- `StoreResponse` -> `store`
- `ReasoningEffort` -> `reasoning.effort`
- `ThinkingRequested = false` with no explicit effort -> `reasoning.effort = "none"`
- `ThinkingRequested = true` with no explicit effort -> omit `reasoning.effort` and use the verified `medium` default
- provider option `ReasoningMode` -> `reasoning.mode`
- provider option `ReasoningContext` -> `reasoning.context`
- `ReasoningSummary = auto` -> `reasoning.summary = "auto"`; any other normalized value is unverified and must stop
- provider option `TextVerbosity` -> `text.verbosity`, one of `low`, `medium`, `high`
- `ResponseFormat` -> `text.format`
- caller functions -> `tools` items of type `function`
- hosted tools -> `tools` declarations gated through `hosted-tools.md`
- `ToolChoice` -> the verified Responses `tool_choice` form

### Reasoning

- Allowed effort values: `none`, `low`, `medium`, `high`, `xhigh`, `max`.
- Omitted effort defaults to `medium`. If `ThinkingRequested` and `ReasoningEffort` are both present, they must agree.
- `none` means `ThinkingApplied = false`; every other allowed value means `ThinkingApplied = true`.
- `ReasoningMode` accepts `standard` or `pro`; omission means `standard`. Mode and effort are independent.
- Pro mode remains the same documented model ID. Do not switch to a separate Pro slug.
- `ReasoningContext` accepts `auto`, `current_turn`, or `all_turns`; omission is equivalent to `auto`.
- Raw reasoning is not visible. `reasoning.summary = "auto"` may return a provider-visible summary; encrypted content is opaque state.
- Reasoning tokens are billed as output tokens and count inside `max_output_tokens` together with visible output.
- Handle `status = incomplete` and `incomplete_details.reason = max_output_tokens`; visible output may be absent when the limit is consumed during reasoning.

### Stateful Continuation

For stored state:

1. send the previous normalized `ContinuationId` as `previous_response_id`;
2. keep provider, profile, base URL, surface, and compatible GPT-5.6 family fixed;
3. use `reasoning.context = all_turns` only when prior reasoning remains relevant;
4. do not also replay a reconstructed full history unless the application intentionally follows a documented hybrid path;
5. do not combine `previous_response_id` with a Responses `conversation` field.

`previous_response_id` does not automatically carry prior `instructions`; resend required instructions on every turn.

### Stateless or Zero-Data-Retention Continuation

When `store = false` or the organization requires stateless handling:

1. include `reasoning.encrypted_content` on every request;
2. preserve every returned output item without mutation;
3. preserve assistant `phase` values;
4. append new input and replay the complete required history;
5. preserve function calls, function outputs, IDs, caller linkage, and reasoning items.

Do not advertise a response ID as reusable when the resolved storage mode does not support that continuation.

### Structured Output

- `json_schema` maps to `text.format.type = json_schema`; validate the schema and prefer strict adherence.
- `json_object` maps to `text.format.type = json_object`; the prompt must explicitly instruct the model to produce JSON.
- Treat refusals, incomplete responses, tool calls, and interruptions separately from schema-valid output.
- Do not parse a refusal or partial response as successful structured content.

### Caller-Defined Functions

- Use `strict: true` for stable schemas.
- Strict schemas require `additionalProperties: false` and every property in `required`; represent optional values with a nullable type.
- Preserve each returned `call_id`.
- Return results as `function_call_output` items with the matching `call_id`.
- Preserve reasoning and all intervening output items across consecutive tool calls.
- `parallel_tool_calls = false` guarantees zero or one caller function call. Parallel caller functions are unavailable when built-in tools are present.

### Hosted Tools

Gate every declaration through `hosted-tools.md`. Keep hosted executions separate from caller functions in both state and normalized output.

## Chat Completions Mapping

Map only verified compatibility fields:

- `Model` -> `model`
- `Inputs.Messages` -> `messages`
- `IsStream` -> `stream`
- `MaxOutputTokens` -> `max_completion_tokens`
- `ReasoningEffort` -> `reasoning_effort`
- `ThinkingRequested = false` with no explicit effort -> `reasoning_effort = "none"`
- `ThinkingRequested = true` with no explicit effort -> omit `reasoning_effort` and use the verified `medium` default
- provider option `TextVerbosity` -> `verbosity`, one of `low`, `medium`, `high`
- `ResponseFormat` -> `response_format`
- caller-defined functions -> Chat Completions `tools`
- `ToolChoice` -> verified Chat Completions `tool_choice`
- `parallel_tool_calls` only for caller functions

Chat Completions reasoning rules:

- Allowed `reasoning_effort` values for the documented GPT-5.6 models are `none`, `low`, `medium`, `high`, `xhigh`, and `max`; do not send the generic `minimal` enum value.
- Omitted effort defaults to `medium`. If `ThinkingRequested` and `ReasoningEffort` are both present, they must agree.
- `none` means `ThinkingApplied = false`; every other allowed value means `ThinkingApplied = true`.
- Reasoning tokens are included in completion-token accounting, but this surface does not return Responses reasoning summaries or reusable encrypted reasoning items.

Do not send from this skill on Chat Completions:

- `ReasoningSummary`
- `reasoning.mode` or any Chat-shaped guess for Pro mode
- `reasoning.context`
- `previous_response_id`
- encrypted reasoning-item continuation
- Responses `text.format` or `text.verbosity`; use Chat Completions `response_format` and `verbosity` instead
- provider-hosted tools unless a later exact tool-and-surface sync adds them

Chat Completions is stateless for this skill: the host owns visible message history. A stored completion ID is not the same as Responses reasoning continuation.

## Prompt Caching

Prompt caching applies to eligible prompts of at least 1024 tokens.

- Shared `CacheKey` -> `prompt_cache_key`.
- `CacheMode = provider-default` sends no cache-control fields and leaves automatic caching behavior to OpenAI.
- `CacheMode = explicit` -> `prompt_cache_options.mode = "explicit"` and requires at least one verified explicit breakpoint.
- `CacheMode = disabled` -> `prompt_cache_options.mode = "explicit"` with no explicit breakpoints; the documented result is no cache read/write and no cache-write charge.
- `CacheMode = session` is not a verified OpenAI mapping and must stop.
- `CacheRetention = 30m` -> `prompt_cache_options.ttl = "30m"`; `30m` is the only verified value and default minimum lifetime. Reject every other value.
- Explicit breakpoints use `prompt_cache_breakpoint: {"mode":"explicit"}`.
- Responses permits breakpoints on `input_text`, `input_image`, and `input_file` blocks. Chat Completions permits them on `text`, `image_url`, `input_audio`, `file`, and `refusal` blocks; this skill still does not enable audio request kinds.
- Each request can create at most four new cache writes. In implicit mode, the latest-message breakpoint consumes one slot, leaving at most three new explicit writes; explicit mode permits up to four. Cache reads consider up to the latest 50 conversation breakpoints.
- Reject deprecated `prompt_cache_retention` for GPT-5.6.
- A stable `prompt_cache_key` is required for the more reliable matching behavior; keep total traffic across prefixes for one key near the documented `15 requests/minute` and partition higher-volume traffic deterministically.
- Cache writes cost `1.25x` the uncached input rate. Log both cache reads and writes and select the correct short/long context price band.

Responses usage paths:

- `usage.input_tokens_details.cached_tokens`
- `usage.input_tokens_details.cache_write_tokens`

Chat Completions usage paths:

- `usage.prompt_tokens_details.cached_tokens`
- `usage.prompt_tokens_details.cache_write_tokens`

## Sampling Fail-Closed Rule

This sync did not establish exact GPT-5.6 support for `temperature`, `top_p`, `logprobs`, or `top_logprobs` on each surface. Omit them. If supplied, return a pre-send capability error rather than forwarding or silently dropping them.

## Streaming and Safeguards

- Use SSE handling for `stream = true`.
- Preserve item/event ordering and assemble final text, structured content, tool calls, reasoning summaries, and usage by event type.
- GPT-5.6 safeguards may pause generation for several seconds mid-stream. Do not treat a temporary silent interval as a disconnected socket without the caller's verified timeout/heartbeat policy.
- Honor cancellation and the full request timeout; never retry a non-idempotent tool loop blindly.
- For end-user applications, send a stable privacy-preserving `safety_identifier`; log only a hash or opaque surrogate.

## Response Mapping

Normalize:

- response `id` -> `ContinuationId` only when continuation is usable
- final output text -> `TextContent`
- validated schema data -> `StructuredContent`
- caller function calls -> `ToolCalls`
- provider-hosted executions -> `HostedToolCalls`
- provider-visible reasoning summary -> `ReasoningSummary`
- encrypted/opaque reasoning items -> `ReasoningItems`
- annotations/citations -> `Annotations`
- cached, cache-write, reasoning, input, and output token details -> `Usage`
- provider status and incomplete details -> `FinishReason` and `ProviderMeta`

Sources: `https://developers.openai.com/api/docs/guides/latest-model`, `https://developers.openai.com/api/docs/guides/reasoning`, `https://developers.openai.com/api/docs/guides/prompt-caching`, `https://developers.openai.com/api/docs/guides/function-calling`, `https://developers.openai.com/api/docs/guides/structured-outputs`, `https://developers.openai.com/api/reference/resources/responses/methods/create`, `https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create`.
