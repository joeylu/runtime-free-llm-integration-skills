# Shared Capability Matrix Schema

Use this file to keep every provider skill's capability matrix shaped the same way.

A capability row is keyed by the exact tuple:

`RequestKind + API Model + API Surface + API Version + Endpoint Kind`

Read `route-key-schema.md` first. Do not resolve capabilities by model name alone. The same model can expose different thinking controls, structured output, tools, state handling, or streaming behavior on different API surfaces.

## Capability States

| State | Meaning |
| --- | --- |
| `verified` | confirmed from official provider docs during an explicit sync task |
| `unsupported` | officially confirmed as not supported |
| `inherited` | carried from an older project-specific toolchain or skill and not yet re-checked against official docs |
| `unknown` | not confirmed and too risky to assume |
| `n/a` | not applicable to that request kind or API surface |

## Required Columns

| Column | Meaning |
| --- | --- |
| `Route Key` | canonical full route key from `route-key-schema.md` |
| `Model Type` | compatibility request-kind field: `chat`, `vision`, `imaging`, `music`, `speech`, or `transcription` |
| `API Model` | exact provider model identifier |
| `API Surface` | exact provider API surface from `request-urls.md`; one surface per row |
| `API Version` | exact API version from the matching request URL row |
| `Endpoint Kind` | exact endpoint kind from the matching request URL row |
| `Supports Non-Stream` | whether a non-stream request path is allowed on the listed surface |
| `Supports Stream` | whether a stream request path is allowed on the listed surface |
| `Thinking Mode` | `mixed`, `always-on`, `unsupported`, `unknown`, or `n/a` |
| `Thinking Default` | default effective thinking state or default reasoning-effort value when the caller omits thinking controls |
| `Thinking Budget Field` | whether a separate thinking budget field is officially documented on the listed surface |
| `Thinking Budget Default` | official default or maximum budget value, if the docs expose one |
| `Temperature Mode` | `all-modes`, `thinking-only`, `non-thinking-only`, `provider-default-only`, `unsupported`, `unknown`, or `n/a` |
| `Temperature Defaults` | official default value or per-mode default values |
| `Json Object Mode` | `all-modes`, `non-thinking-only`, `thinking-only`, `unsupported`, `unknown`, or `n/a` |
| `Json Schema Mode` | `all-modes`, `non-thinking-only`, `thinking-only`, `unsupported`, `unknown`, or `n/a` |
| `Tool Calling Mode` | caller-defined function/tool support: `all-modes`, `non-thinking-only`, `thinking-only`, `unsupported`, `unknown`, or `n/a` |
| `Strict Tool Schema Mode` | whether strict schema adherence for caller-defined tool/function arguments is verified |
| `Parallel Tool Calls` | whether parallel caller-defined tool/function calls are verified |
| `Reasoning Effort Field` | whether an enum-style reasoning effort field is officially documented on the listed surface |
| `Reasoning Effort Values` | accepted normalized request values, such as `none,minimal,low,medium,high,xhigh,max`; put provider wire mapping in Notes or transport |
| `Reasoning Summary Field` | whether provider-visible reasoning summaries are officially documented |
| `Reasoning Output Visibility` | `raw`, `summary`, `encrypted`, `usage-only`, `none`, `unknown`, or `n/a` |
| `Supports Image Input` | whether image input is allowed |
| `Supports Seed` | whether seed is supported |
| `Supports Image Size` | whether image size is supported |
| `Supports Image Count` | whether `Inputs.ImageCount` is supported for imaging output count |
| `Supports Duration Seconds` | whether duration is supported |
| `Last Verified At` | absolute verification date for this route row |
| `Source` | one or more exact official URLs supporting the route-level capability claims |
| `Notes` | short explanation, surface/version-specific restriction, or field-level evidence note |

## Row Resolution Rules

- Resolve the connection profile, `ApiSurface`, `ApiVersion`, and `EndpointKind` before capability lookup.
- Match the exact full `RouteKey`.
- Keep one API surface and one API version per row. Duplicate a row when current facts match, so later version-specific changes remain expressible.
- Do not inherit a verified capability across API surfaces, versions, endpoint kinds, profiles, or regions.
- If no exact row exists, stop with a capability error before sending.
- Provider-hosted tools are not caller-defined function tools. Verify hosted tools in the provider transport or a dedicated hosted-tool matrix; never infer them from `Tool Calling Mode`.

## Gating Rules

- `stream`, `thinking budget`, `seed`, `image size`, imaging output `image count`, and `duration` should require `verified` unless a provider skill explicitly says otherwise.
- A provider skill may allow a base `non-stream` path when `Supports Non-Stream = inherited`, but it must say that explicitly.
- If a requested capability is `unsupported`, stop.
- If a requested capability is `unknown`, stop.
- Use `n/a` instead of `unknown` when a capability does not belong to that request kind or API surface.

Resolve the effective thinking state before checking mode-sensitive capabilities:

1. If the caller sets `ReasoningEffort`, map `none` to `off` and `minimal`, `low`, `medium`, `high`, `xhigh`, or `max` to `on` unless the provider transport explicitly documents a different compatibility mapping.
2. If the caller explicitly sets `ThinkingRequested`, use that value, unless it conflicts with `ReasoningEffort`.
3. Otherwise, if `Thinking Mode = mixed`, map `Thinking Default`: `off`, `false`, or `none` means `off`; `on`, `true`, `minimal`, `low`, `medium`, `high`, `xhigh`, or `max` means `on`; `adaptive` remains `adaptive`.
4. Otherwise, if `Thinking Mode = always-on`, effective thinking is `on`.
5. Otherwise, effective thinking is `off`.

Do not collapse `adaptive` to a Boolean in the shared layer. The exact provider transport must document whether adaptive is equivalent to on for gating, provider-controlled, or incompatible with a requested mode-sensitive field. If that mapping is absent, stop before sending.

If the effective thinking state is needed for a requested mode-sensitive option and `Thinking Default = unknown`, stop unless the caller supplies an explicit verified thinking control.

Then gate the request like this:

- `ThinkingRequested = true` requires `Thinking Mode = mixed` or `always-on`.
- `ThinkingRequested = false` is invalid when `Thinking Mode = always-on`.
- `ThinkingBudget` requires `Thinking Budget Field = verified` on the resolved surface.
- `ReasoningEffort` requires `Reasoning Effort Field = verified` and an allowed value in `Reasoning Effort Values` on the resolved surface.
- `ReasoningSummary` requires `Reasoning Summary Field = verified`.
- `Temperature` requires `Temperature Mode` to be compatible with the effective thinking state. If `Temperature Mode = provider-default-only`, omit the field and reject caller-supplied `Temperature`; provider-specific transports must apply the same rule to sibling sampling fields such as `top_p` and `top_k`.
- `ResponseFormat = json_object` requires `Json Object Mode` to be compatible with the effective thinking state.
- `ResponseFormat = json_schema` requires `Json Schema Mode` to be compatible with the effective thinking state.
- Caller-defined function/tool definitions require `Tool Calling Mode` to be compatible with the effective thinking state.
- Strict tool/function schemas require `Strict Tool Schema Mode = verified`.
- Parallel tool calls require `Parallel Tool Calls = verified`.

For `vision`, `Inputs.Images` means input images; do not use `Supports Image Count` to gate vision input image count.

For `imaging`, treat `Supports Image Input` as verified only when the provider docs confirm image input for the exact requested imaging flow, such as edit input or reference images. Do not infer edit/reference-image support from a base text-to-image row.

If the docs publish only one model-wide temperature default, record it as `all-modes: <value>` in `Temperature Defaults`.

## Stream Verification Rule

Do not require a model-specific stream example in every case.

`Supports Stream` may be set to `verified` when either:

1. an official model-specific page or example explicitly shows stream support for that model and API surface, or
2. an official provider stream transport document covers the protocol family and API surface, an official model-family page places that model in the same callable family, and there is no official statement that stream is unsupported for that model

When using rule 2:

- record the evidence chain in `Notes`
- keep the evidence inside the same provider, model family, and API surface
- do not spill a Qwen stream rule onto GLM, Kimi, Wan, or other families unless official docs for that family also cover stream
- if the transport doc and model-family page do not clearly align, keep `Supports Stream = unknown`

## Thinking Verification Rule

Do not treat `thinking` as a plain yes or no field.

You may set `Thinking Mode`, `Thinking Default`, and `Thinking Budget Field` from official:

- deep-thinking or reasoning-mode docs
- model capability tables
- parameter reference pages
- official examples that explicitly show `enable_thinking` or an equivalent field

Important:

- a model list that only exposes a maximum reasoning length does not by itself verify that a caller-set budget field exists
- when a default-on or default-off rule is documented, record it in `Thinking Default`
- when the same model uses different thinking controls on different surfaces or API versions, create separate rows

## Temperature Verification Rule

Do not treat `temperature` as a simple support toggle.

You may set `Temperature Mode` and `Temperature Defaults` from official:

- parameter reference pages
- parameter default tables
- model-family docs that explicitly scope the defaults by mode and API surface

If the provider docs distinguish thinking and non-thinking defaults, record both.

Use `provider-default-only` when official guidance says the model is optimized for provider defaults and callers should not alter sampling controls. In that state, record `provider default; caller override blocked` in `Temperature Defaults`.

## Json Object Verification Rule

Do not collapse structured output into a simple supported or unsupported flag.

You may set `Json Object Mode` from official:

- structured-output docs
- model capability tables
- provider model pages that explicitly scope structured output to a specific mode and API surface

Example:
If `Json Object Mode = non-thinking-only` and `Thinking Default = on`, a caller asking for `json_object` must also explicitly set `ThinkingRequested = false`.

## Json Schema Verification Rule

Treat strict schema adherence as separate from basic JSON mode.

You may set `Json Schema Mode` from official:

- structured-output docs
- model capability pages
- API reference pages that explicitly document `json_schema` or equivalent schema-constrained output on the resolved surface

Do not infer `json_schema` support from `json_object` support.

## Tool Calling Verification Rule

Track caller-defined tool/function calling separately from structured text output and provider-hosted tools.

You may set `Tool Calling Mode`, `Strict Tool Schema Mode`, and `Parallel Tool Calls` from official:

- function-calling or tool-calling docs
- model capability pages
- API reference pages that document strict function schemas or parallel tool calls on the resolved surface

Do not treat provider-hosted tools, such as web search or image generation tools, as proof that caller-defined function tools are supported.

## Reasoning Effort Verification Rule

Some providers expose reasoning as enum-style effort instead of a boolean thinking toggle.

When official docs expose a field such as `reasoning.effort`, update:

- `Reasoning Effort Field`
- `Reasoning Effort Values`
- `Thinking Mode`
- `Thinking Default`
- `API Surface`

Map `none` to effective thinking `off`; map `minimal`, `low`, `medium`, `high`, `xhigh`, or `max` to effective thinking `on`, unless the exact provider transport documents compatibility aliases.

If the default effort is not documented for the exact model and surface, set `Thinking Default = unknown` and require the caller to choose an explicit effort before using mode-sensitive options.

## Reasoning Output Visibility Rule

Do not assume raw chain-of-thought is visible.

Use:

- `raw` only when official docs expose raw reasoning text
- `summary` when docs expose summaries but not raw reasoning
- `encrypted` when docs expose encrypted reasoning items for continuation
- `usage-only` when docs expose only reasoning-token usage
- `none` when docs explicitly say reasoning output is not exposed
- `unknown` when the skill has not verified visibility

If visibility differs by surface, create separate rows.

## Examples

For an inherited chat model, `Supports Non-Stream = inherited` can be acceptable, while `Supports Stream = unknown` must still block stream wiring.

For `qwen3.7-plus` on `chat-completions`, `Thinking Default = on` and `Json Object Mode = non-thinking-only` means JSON output must fail fast unless the caller explicitly disables thinking.

For `qwen3.7-plus` on `responses`, `Thinking Default = medium`, `Reasoning Effort Values = none,minimal,low,medium,high`, and `Thinking Budget Field = unsupported` mean the request must use `reasoning.effort` rather than `thinking_budget`.
