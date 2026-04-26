# Shared Capability Matrix Schema

Use this file to keep every provider skill's capability matrix shaped the same way.

## Capability States

| State | Meaning |
| --- | --- |
| `verified` | confirmed from official provider docs during an explicit sync task |
| `unsupported` | officially confirmed as not supported |
| `inherited` | carried from an older project-specific toolchain or skill and not yet re-checked against official docs |
| `unknown` | not confirmed and too risky to assume |
| `n/a` | not applicable to that request kind |

## Required Columns

| Column | Meaning |
| --- | --- |
| `Model Type` | `chat`, `vision`, `imaging`, or `music` |
| `API Model` | exact provider model identifier |
| `Supports Non-Stream` | whether a non-stream request path is allowed |
| `Supports Stream` | whether a stream request path is allowed |
| `Thinking Mode` | `mixed`, `always-on`, `unsupported`, `unknown`, or `n/a` |
| `Thinking Default` | default effective thinking state when the caller omits `ThinkingRequested` |
| `Thinking Budget Field` | whether a separate thinking budget field is officially documented |
| `Thinking Budget Default` | official default or maximum budget value, if the docs expose one |
| `Temperature Mode` | `all-modes`, `thinking-only`, `non-thinking-only`, `unsupported`, `unknown`, or `n/a` |
| `Temperature Defaults` | official default value or per-mode default values |
| `Json Object Mode` | `all-modes`, `non-thinking-only`, `thinking-only`, `unsupported`, `unknown`, or `n/a` |
| `Supports Image Input` | whether image input is allowed |
| `Supports Seed` | whether seed is supported |
| `Supports Image Size` | whether image size is supported |
| `Supports Image Count` | whether multi-image count is supported |
| `Supports Duration Seconds` | whether duration is supported |
| `Notes` | short explanation or source note |

## Gating Rules

- `stream`, `thinking budget`, `seed`, `image size`, `image count`, and `duration` should require `verified` unless a provider skill explicitly says otherwise.
- A provider skill may allow a base `non-stream` path when `Supports Non-Stream = inherited`, but it must say that explicitly.
- If a requested capability is `unsupported`, stop.
- If a requested capability is `unknown`, stop.
- Use `n/a` instead of `unknown` when a capability does not belong to that request kind.

Resolve the effective thinking state before checking mode-sensitive capabilities:

1. If the caller explicitly sets `ThinkingRequested`, use that value.
2. Otherwise, if `Thinking Mode = mixed`, use `Thinking Default`.
3. Otherwise, if `Thinking Mode = always-on`, effective thinking is `true`.
4. Otherwise, effective thinking is `false`.

Then gate the request like this:

- `ThinkingRequested = true` requires `Thinking Mode = mixed` or `always-on`.
- `ThinkingRequested = false` is invalid when `Thinking Mode = always-on`.
- `ThinkingBudget` requires `Thinking Budget Field = verified`.
- `Temperature` requires `Temperature Mode` to be compatible with the effective thinking state.
- `ResponseFormat = json_object` requires `Json Object Mode` to be compatible with the effective thinking state.

For `imaging`, treat `Supports Image Input` as verified only when the provider docs confirm image input for the exact requested imaging flow, such as edit input or reference images. Do not infer edit/reference-image support from a base text-to-image row.

If the docs publish only one model-wide temperature default, record it as `all-modes: <value>` in `Temperature Defaults`.

## Stream Verification Rule

Do not require a model-specific stream example in every case.

`Supports Stream` may be set to `verified` when either:

1. an official model-specific page or example explicitly shows stream support for that model, or
2. an official provider stream transport document covers the protocol family, and an official model-family page places that model in the same callable family, and there is no official statement that stream is unsupported for that model

When using rule 2:

- record the evidence chain in `Notes`
- keep the evidence inside the same provider and model family
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

## Temperature Verification Rule

Do not treat `temperature` as a simple support toggle.

You may set `Temperature Mode` and `Temperature Defaults` from official:

- parameter reference pages
- parameter default tables
- model-family docs that explicitly scope the defaults by mode

If the provider docs distinguish thinking and non-thinking defaults, record both.

## Json Object Verification Rule

Do not collapse structured output into a simple supported or unsupported flag.

You may set `Json Object Mode` from official:

- structured-output docs
- model capability tables
- provider model pages that explicitly scope structured output to a specific mode

Example:
If `Json Object Mode = non-thinking-only` and `Thinking Default = on`, a caller asking for `json_object` must also explicitly set `ThinkingRequested = false`.

## Example

For an inherited chat model, `Supports Non-Stream = inherited` can be acceptable, while `Supports Stream = unknown` must still block stream wiring.

For `qwen3.6-plus`, `Thinking Mode = mixed`, `Thinking Default = on`, and `Json Object Mode = non-thinking-only` means strict JSON output must fail fast unless the caller explicitly disables thinking.
