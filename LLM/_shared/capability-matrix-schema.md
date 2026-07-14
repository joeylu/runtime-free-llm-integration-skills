# Shared Capability Matrix Schema v2

A capability row is keyed by the exact tuple:

`Request Kind + API Model + API Surface + API Version`

One row must describe exactly one surface and one version. Comma-separated surface or version lists are forbidden.

## Capability States

| State | Meaning |
| --- | --- |
| `verified` | Confirmed by a claim in the evidence manifest |
| `unsupported` | Explicitly unsupported in official documentation |
| `inherited` | Carried from an older integration and not re-verified |
| `unknown` | Not confirmed; fail closed |
| `n/a` | Not applicable to this request kind/surface |

## Required Columns

Provider matrices retain their existing capability columns and add:

| Column | Meaning |
| --- | --- |
| `Request Kind` | Canonical request kind |
| `API Model` | Exact model ID |
| `API Surface` | One exact surface only |
| `API Version` | Exact path/header version such as `v1`, `v1beta`, `provider-default`, or `none` |
| `Evidence Refs` | evidence-set IDs whose field-level claims support the row's non-unknown facts |

The remaining standard capability columns are:

`Supports Non-Stream`, `Supports Stream`, `Thinking Mode`, `Thinking Default`, `Thinking Budget Field`, `Thinking Budget Default`, `Temperature Mode`, `Temperature Defaults`, `Json Object Mode`, `Json Schema Mode`, `Tool Calling Mode`, `Strict Tool Schema Mode`, `Parallel Tool Calls`, `Tool Choice When Thinking`, `Required Tool-History Fields`, `Reasoning Effort Field`, `Reasoning Effort Values`, `Reasoning Summary Field`, `Reasoning Output Visibility`, `Supports Image Input`, `Supports Seed`, `Supports Image Size`, `Supports Image Count`, `Supports Duration Seconds`, and `Notes`.

## Exact-Surface Rule

- Resolve provider, region, connection profile, base URL, API surface, and API version before capability lookup.
- Never inherit a capability from another surface or version.
- If no exact row exists, stop before sending.
- A beta-only capability must be represented on a beta row; it must not appear as verified on the stable row.
- Caller-defined tools and provider-hosted tools are separate capabilities.

## Mode-Sensitive Gating

Resolve effective thinking first. Then apply mode-sensitive fields:

- `Temperature`, structured output, `ToolChoice`, and tool behavior must obey the exact row and transport.
- `ThinkingRequested = false` is invalid for `Thinking Mode = always-on`.
- `ThinkingBudget` requires `Thinking Budget Field = verified`.
- `ReasoningEffort` requires `Reasoning Effort Field = verified` and an allowed value.
- `Json Object Mode`, `Json Schema Mode`, and `Tool Calling Mode` must permit the effective thinking state.
- `Strict Tool Schema Mode = verified` applies only to the exact row where the provider documents strict enforcement.
- `Tool Choice When Thinking` gates `ToolChoice` after effective thinking is resolved.
- `Required Tool-History Fields` lists provider-required assistant/tool history fields; missing fields stop the request before sending.
- `unknown` and `unsupported` both block a requested feature; `unsupported` additionally means the provider explicitly rejects or omits it.

## Media Gating

- Image input requires `Supports Image Input = verified`.
- `Inputs.Seed`, `Inputs.ImageSize`, `Inputs.ImageCount`, and `Inputs.DurationSeconds` each require the matching verified field.
- Parameter ranges and conditional requirements belong in the provider transport and claim-level evidence, not only in free-form Notes.
