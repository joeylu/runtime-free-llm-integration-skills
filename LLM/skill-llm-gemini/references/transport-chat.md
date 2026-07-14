# Gemini Chat Transport

Use this for `RequestKind = chat` after profile, model, surface, URL, and capability resolution.

## Surface Resolution

- New integration: use `interactions`.
- Existing compatibility integration: keep `generate-content` or `stream-generate-content` only when explicitly requested.
- Never retry a failed request on a different surface automatically.

## Interactions Request Mapping

Map normalized fields as follows:

| Shared Field | Interactions Field | Rule |
| --- | --- | --- |
| `Model` | `model` | exact catalog ID in the body |
| `Inputs.Messages` | `input` | map to ordered text or typed input items |
| `Instructions` | `system_instruction` | re-send on every continued interaction |
| `IsStream` | `stream` | same endpoint; true returns SSE step events |
| `ContinuationId` | `previous_interaction_id` | use only with a stored compatible Interaction |
| `StoreResponse` | `store` | default is true; false prevents later ID continuation |
| `ReasoningEffort` | `generation_config.thinking_level` | only allowed values from the exact capability row |
| `ReasoningSummary` | `generation_config.thinking_summaries` | map `true` to `"auto"`; omit when false or unspecified |
| `MaxOutputTokens` | `generation_config.max_output_tokens` | validate against the documented model maximum |
| `Tools` | `tools` entries of type `function` | caller executes these functions |
| `HostedTools` | provider tool declarations | validate through `hosted-tools.md` |
| `ToolChoice` | `generation_config.tool_choice` | allow only `auto`, `any`, `none`, or explicit Preview `validated`; do not invent OpenAI-style values |
| `ResponseFormat = json_schema` | `response_format = {"type":"text","mime_type":"application/json","schema":...}` | validate returned JSON before normalization |

`previous_interaction_id` preserves conversation history only. Re-send `tools`, `system_instruction`, and `generation_config` on each continued turn.

`validated` tool choice is Preview and is the only verified strict function-schema mode in this skill. It requires explicit Preview opt-in. Parallel and compositional caller-function calls are verified on Interactions; aggregate every streamed `arguments_delta` by function-call step before execution.

Interactions stores requests by default. On paid projects, official documentation currently states a 55-day default retention; free-tier retention is one day. Treat `StoreResponse` as a data-governance decision, not merely a convenience flag.

## GenerateContent Request Mapping

- Map messages into ordered `contents` with provider roles and parts.
- Map `Instructions` to `systemInstruction`.
- Map `ReasoningEffort` to `generationConfig.thinkingConfig.thinkingLevel`.
- Map `ReasoningSummary = true` to `generationConfig.thinkingConfig.includeThoughts = true`.
- Map `ResponseFormat = json_schema` to `generationConfig.responseMimeType = application/json` plus `generationConfig.responseJsonSchema`.
- Map caller functions under `tools[].functionDeclarations`.
- Map `ToolChoice` only to verified GenerateContent `toolConfig.functionCallingConfig.mode` values (`AUTO`, `ANY`, or `NONE`). Do not map Interactions Preview `validated` onto this surface.
- Strict function-schema adherence and parallel caller-function calls remain `unknown` on the compatibility surfaces in this skill; fail fast when either is requested.
- Use the separate StreamGenerateContent URL only for `IsStream = true`.

GenerateContent has no server-side `ContinuationId` in this contract. Multi-turn requests must resend the complete ordered history, including model thought signatures and all function calls/results required by the provider.

## Thinking and Sampling

- `gemini-3.5-flash`: default `medium`; allowed `minimal`, `low`, `medium`, `high`.
- `gemini-3.1-pro-preview`: default `high`; allowed `low`, `medium`, `high`.
- `minimal` can still reason.
- Reject `ThinkingBudget` and legacy `thinking_budget`.
- Reject caller-supplied `Temperature`, `top_p`, and `top_k`; the official migration guidance recommends the provider defaults.
- Do not set `candidate_count` for documented Gemini 3.x rows.

## Caller-Defined Function Loop

Validate the complete function round before sending results back:

1. Preserve every provider function-call ID and function name.
2. Execute only functions defined by the caller and approved by the host.
3. Return exactly one matching result for each preceding call unless the provider explicitly permits otherwise.
4. Ensure result `id` or `call_id`, name, and result count match the preceding calls.
5. Put multimodal function output inside the function result, not as unrelated sibling content.
6. Append any user-facing instruction to the function-result text instead of injecting a separate higher-authority part.

Interactions should return a validation error for mismatches. GenerateContent may instead finish with empty output and `STOP`; detect that condition and raise a tool-state error rather than treating it as success.

## Structured Output

For `json_schema`, validate both the schema sent and the JSON received. Provider schema support is not a substitute for application-level validation.

Structured output combined with tools is Preview for Gemini 3 models. Require an explicit Preview opt-in and retain a warning in `ProviderMeta`.

Bare `json_object` remains blocked because this local contract has not verified equivalent strict behavior.

## Cache Behavior

- Interactions: `CacheMode = provider-default` only. Implicit caching is automatic. Explicit cache resources are unsupported on this surface. For `gemini-3.5-flash` and `gemini-3.1-pro-preview`, the current minimum input size for an implicit cache hit is 4,096 tokens. Read cache-hit usage from `usage.total_cached_tokens`.
- GenerateContent: `provider-default` is allowed; `explicit` requires a pre-created cache resource name mapped to `cachedContent`. Cache creation, TTL updates, and deletion are separate operations and are not inferred from a request.
- Do not map `StoreResponse = false` to cache disablement.

## Streaming

Interactions streams observable step events, including `step.start`, typed `step.delta`, `step.stop`, and a terminal Interaction event; GenerateContent streams candidate chunks. They are not interchangeable parsers.

For either surface:

- use a real SSE parser
- preserve event order
- handle cancellation and full-request timeout
- accumulate text, function, hosted-tool, usage, and finish metadata separately
- for a `thought` step, accumulate `thought_summary` only into `ReasoningSummary` and retain `thought_signature` only as opaque continuation state
- for a `function_call` step, concatenate `arguments_delta` fragments before JSON parsing or execution
- emit `completed` only after `interaction.completed` or the compatibility surface's clean terminal response

## Response Mapping

- final model text -> `TextContent`
- validated JSON -> `StructuredContent`
- caller function calls -> `ToolCalls`
- provider tool activity -> `HostedToolCalls`
- grounding/citations -> `Annotations`
- Interaction `id` -> `ContinuationId` only when reusable
- non-stream `thought` step `summary` or stream `thought_summary` deltas -> `ReasoningSummary`
- non-stream thought `signature` or stream `thought_signature` deltas -> opaque `ReasoningItems`
- Interactions `usage.total_thought_tokens` and `usage.total_cached_tokens` -> surface-qualified fields in `Usage`
- GenerateContent `usageMetadata.thoughtsTokenCount` and `usageMetadata.cachedContentTokenCount` -> surface-qualified fields in `Usage`
- provider finish state -> normalized `FinishReason`

Never expose raw model thoughts or thought signatures as `ThinkingContent`.
